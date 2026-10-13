-- TEMPLATE: render with scripts/render-schema.py; never execute this file directly.
-- NEW SITE ONLY. Fail if the schema already exists; existing sites need a reviewed
-- differential migration. Rendering is not proof that a database migration ran.
-- Supabase roles anon/authenticated/service_role must exist on the target.
BEGIN;

CREATE SCHEMA {{SITE_SCHEMA}};
REVOKE ALL ON SCHEMA {{SITE_SCHEMA}} FROM PUBLIC;
GRANT USAGE ON SCHEMA {{SITE_SCHEMA}} TO anon, authenticated, service_role;

CREATE TABLE {{SITE_SCHEMA}}.categories (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name text NOT NULL CHECK (length(btrim(name)) > 0),
  slug text NOT NULL UNIQUE CHECK (length(btrim(slug)) > 0),
  description text,
  parent_id bigint REFERENCES {{SITE_SCHEMA}}.categories(id) ON DELETE SET NULL,
  display_order integer NOT NULL DEFAULT 999,
  featured_image text,
  created_at timestamptz NOT NULL DEFAULT now(),
  CHECK (parent_id IS NULL OR parent_id <> id)
);
CREATE INDEX categories_parent_idx ON {{SITE_SCHEMA}}.categories(parent_id);
CREATE INDEX categories_order_idx ON {{SITE_SCHEMA}}.categories(display_order);

CREATE TABLE {{SITE_SCHEMA}}.articles (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  title text NOT NULL CHECK (length(btrim(title)) > 0),
  slug text NOT NULL UNIQUE CHECK (length(btrim(slug)) > 0),
  content text NOT NULL DEFAULT '',
  excerpt text,
  featured_image text,
  category_id bigint REFERENCES {{SITE_SCHEMA}}.categories(id) ON DELETE SET NULL,
  status text NOT NULL DEFAULT 'draft' CHECK (status IN ('draft','published','archived')),
  author text,
  is_featured boolean NOT NULL DEFAULT false,
  featured_order integer,
  swamp text,
  piece text,
  published_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  revision bigint NOT NULL DEFAULT 0,
  CHECK (status <> 'published' OR (published_at IS NOT NULL AND length(btrim(content)) > 0))
);
CREATE INDEX articles_status_idx ON {{SITE_SCHEMA}}.articles(status, published_at DESC);
CREATE INDEX articles_category_idx ON {{SITE_SCHEMA}}.articles(category_id);
CREATE INDEX articles_featured_idx ON {{SITE_SCHEMA}}.articles(is_featured, featured_order)
  WHERE is_featured;

-- Public presentation settings only. NEVER store credentials or subscriber data here.
CREATE TABLE {{SITE_SCHEMA}}.site_settings (
  id boolean PRIMARY KEY DEFAULT true CHECK (id),
  hero_image text,
  hero_eyebrow text,
  hero_title text,
  hero_lead text,
  guide_ads_enabled boolean NOT NULL DEFAULT false,
  guide_checkout_url text NOT NULL DEFAULT '',
  guide_price text NOT NULL DEFAULT '',
  guide_cover text NOT NULL DEFAULT '',
  updated_at timestamptz NOT NULL DEFAULT now()
);
INSERT INTO {{SITE_SCHEMA}}.site_settings(id) VALUES (true);

-- Local audit option for a NEW isolated site. A verified existing fleet audit
-- contract can be used instead in a reviewed migration; never create a competing
-- audit source on a live site merely because this template contains one.
CREATE TABLE {{SITE_SCHEMA}}.audit_log (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  request_id text NOT NULL UNIQUE CHECK (length(btrim(request_id)) > 0),
  actor_id text NOT NULL CHECK (length(btrim(actor_id)) > 0),
  action text NOT NULL CHECK (length(btrim(action)) > 0),
  target_table text NOT NULL,
  target_id text,
  before_value jsonb,
  after_value jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE FUNCTION {{SITE_SCHEMA}}.touch_article() RETURNS trigger
LANGUAGE plpgsql SET search_path = pg_catalog AS $travel_touch$
BEGIN
  NEW.updated_at = now();
  NEW.revision = OLD.revision + 1;
  RETURN NEW;
END;
$travel_touch$;
CREATE TRIGGER articles_touch BEFORE UPDATE ON {{SITE_SCHEMA}}.articles
FOR EACH ROW EXECUTE FUNCTION {{SITE_SCHEMA}}.touch_article();

CREATE FUNCTION {{SITE_SCHEMA}}.touch_settings() RETURNS trigger
LANGUAGE plpgsql SET search_path = pg_catalog AS $travel_settings$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$travel_settings$;
CREATE TRIGGER site_settings_touch BEFORE UPDATE ON {{SITE_SCHEMA}}.site_settings
FOR EACH ROW EXECUTE FUNCTION {{SITE_SCHEMA}}.touch_settings();

ALTER TABLE {{SITE_SCHEMA}}.categories ENABLE ROW LEVEL SECURITY;
ALTER TABLE {{SITE_SCHEMA}}.articles ENABLE ROW LEVEL SECURITY;
ALTER TABLE {{SITE_SCHEMA}}.site_settings ENABLE ROW LEVEL SECURITY;
ALTER TABLE {{SITE_SCHEMA}}.audit_log ENABLE ROW LEVEL SECURITY;

-- Ordinary authenticated users have PUBLIC read scope, not admin privileges.
CREATE POLICY categories_public_read ON {{SITE_SCHEMA}}.categories
FOR SELECT TO anon, authenticated USING (true);
CREATE POLICY articles_published_read ON {{SITE_SCHEMA}}.articles
FOR SELECT TO anon, authenticated
USING (status = 'published' AND published_at IS NOT NULL AND published_at <= now());
CREATE POLICY settings_public_read ON {{SITE_SCHEMA}}.site_settings
FOR SELECT TO anon, authenticated USING (true);
-- No public write policy; no public policy at all on audit_log.

REVOKE ALL ON ALL TABLES IN SCHEMA {{SITE_SCHEMA}} FROM PUBLIC, anon, authenticated, service_role;
REVOKE ALL ON ALL SEQUENCES IN SCHEMA {{SITE_SCHEMA}} FROM PUBLIC, anon, authenticated, service_role;
REVOKE EXECUTE ON ALL FUNCTIONS IN SCHEMA {{SITE_SCHEMA}} FROM PUBLIC, anon, authenticated, service_role;
GRANT SELECT ON {{SITE_SCHEMA}}.categories, {{SITE_SCHEMA}}.articles,
  {{SITE_SCHEMA}}.site_settings TO anon, authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON {{SITE_SCHEMA}}.categories,
  {{SITE_SCHEMA}}.articles, {{SITE_SCHEMA}}.site_settings TO service_role;
GRANT SELECT, INSERT ON {{SITE_SCHEMA}}.audit_log TO service_role;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA {{SITE_SCHEMA}} TO service_role;

-- Future migrations must opt in to grants and RLS explicitly for their creator.
ALTER DEFAULT PRIVILEGES IN SCHEMA {{SITE_SCHEMA}}
  REVOKE ALL ON TABLES FROM PUBLIC, anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA {{SITE_SCHEMA}}
  REVOKE ALL ON SEQUENCES FROM PUBLIC, anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA {{SITE_SCHEMA}}
  REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC, anon, authenticated, service_role;

COMMIT;
