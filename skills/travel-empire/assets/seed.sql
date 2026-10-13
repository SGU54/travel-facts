-- TEMPLATE: render with scripts/render-schema.py and approved categories JSON.
-- No fixed category count. Existing identical rows are safe to repeat; a changed
-- taxonomy stops for a differential migration instead of silently overwriting it.
--
-- NO TEMP TABLE (real incident, 2026-10-11, twice): several SQL runners,
-- including the Supabase dashboard's SQL Editor, do not reliably execute a
-- pasted multi-statement script as one client-side session — a temp table
-- created in one statement was gone by the very next one ("relation ... does
-- not exist"), even after removing ON COMMIT DROP and adding an explicit
-- DROP TABLE IF EXISTS. That ruled out a transaction-boundary problem: temp
-- tables are SESSION-scoped, so if the runner sends each statement over a
-- different pooled connection, no amount of transaction wrapping fixes it.
-- Fix: everything is ONE statement — a single DO block that re-reads the
-- category JSON with jsonb_to_recordset() as needed. One statement cannot be
-- split by a runner that batches per top-level statement.
DO $travel_seed$
DECLARE
  payload jsonb := {{CATEGORY_JSON}};
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM jsonb_to_recordset(payload) AS r(name text, slug text, parent_slug text, display_order integer)
  ) THEN
    RAISE EXCEPTION 'Approved categories are empty';
  END IF;

  IF EXISTS (
    SELECT 1
    FROM jsonb_to_recordset(payload) AS child(name text, slug text, parent_slug text, display_order integer)
    LEFT JOIN jsonb_to_recordset(payload) AS parent(name text, slug text, parent_slug text, display_order integer)
      ON parent.slug = child.parent_slug
    WHERE child.parent_slug IS NOT NULL
      AND (parent.slug IS NULL OR parent.parent_slug IS NOT NULL OR child.slug = child.parent_slug)
  ) THEN
    RAISE EXCEPTION 'Categories must have valid parents and at most two levels';
  END IF;

  IF EXISTS (
    SELECT 1
    FROM jsonb_to_recordset(payload) AS wanted(name text, slug text, parent_slug text, display_order integer)
    JOIN {{SITE_SCHEMA}}.categories actual ON actual.slug = wanted.slug
    LEFT JOIN {{SITE_SCHEMA}}.categories parent ON parent.id = actual.parent_id
    WHERE actual.name IS DISTINCT FROM wanted.name
       OR actual.display_order IS DISTINCT FROM wanted.display_order
       OR parent.slug IS DISTINCT FROM wanted.parent_slug
  ) THEN
    RAISE EXCEPTION 'Existing category differs: prepare a reviewed taxonomy migration';
  END IF;

  INSERT INTO {{SITE_SCHEMA}}.categories(name, slug, parent_id, display_order)
  SELECT name, slug, NULL, display_order
  FROM jsonb_to_recordset(payload) AS r(name text, slug text, parent_slug text, display_order integer)
  WHERE parent_slug IS NULL
  ON CONFLICT (slug) DO NOTHING;

  INSERT INTO {{SITE_SCHEMA}}.categories(name, slug, parent_id, display_order)
  SELECT child.name, child.slug, parent.id, child.display_order
  FROM jsonb_to_recordset(payload) AS child(name text, slug text, parent_slug text, display_order integer)
  JOIN {{SITE_SCHEMA}}.categories parent ON parent.slug = child.parent_slug
  WHERE child.parent_slug IS NOT NULL
  ON CONFLICT (slug) DO NOTHING;

  IF (
    SELECT count(*) FROM jsonb_to_recordset(payload) AS r(name text, slug text, parent_slug text, display_order integer)
  ) <> (
    SELECT count(*)
    FROM jsonb_to_recordset(payload) AS wanted(name text, slug text, parent_slug text, display_order integer)
    JOIN {{SITE_SCHEMA}}.categories actual ON actual.slug = wanted.slug
  ) THEN
    RAISE EXCEPTION 'Seed coverage mismatch';
  END IF;
END;
$travel_seed$;
