-- tag-swamps.sql — japanforamericans (regenerated 2026-09-17)
-- ============================================================================
-- Sets japan.articles.swamp so each guide surface opens the door matching the
-- article, instead of falling back to the generic thesis.
--
-- WHY THIS REPLACES THE PREVIOUS FILE: the version in the repo wrote a different
-- generation of swamp ids — base / daytrip / eating / entry / money / ryokan /
-- sequencing / temples — none of which exist in SITE_CONFIG.guide.hooks. It had
-- also never been run: articles.swamp is null across the board, which is why the
-- end band and the inline marker (both swamp-gated) never rendered on any
-- article while the aside and the mobile card, which are not gated, did.
--
-- Ids below come from article-list.json, which is the source of truth for the
-- vein, and every one is verified to have a hook in the site config.
-- Idempotent: re-running is safe.
-- ============================================================================

update japan.articles set swamp = null;

-- cash-access — 1 article(s)
update japan.articles set swamp = 'cash-access' where slug in (
  'money-in-japan-cash-cards-ic'
);

-- ic-card-transit — 7 article(s)
update japan.articles set swamp = 'ic-card-transit' where slug in (
  'getting-around-kyoto',
  'ic-card-day-pass-or-single-ticket',
  'ic-card-wont-open-gate-fare-adjustment',
  'mobile-suica-american-iphone',
  'navigating-japanese-train-stations',
  'suica-pasmo-ic-card-guide',
  'tokyo-subway-explained'
);

-- jr-pass-economics — 5 article(s)
update japan.articles set swamp = 'jr-pass-economics' where slug in (
  'green-car-or-ordinary-japan-rail-pass',
  'how-to-ride-the-shinkansen',
  'japan-rail-pass-worth-it',
  'japan-rail-route-cost-without-pass',
  'regional-jr-passes-vs-national'
);

-- route-sequencing — 20 article(s)
update japan.articles set swamp = 'route-sequencing' where slug in (
  '1-week-in-japan-itinerary',
  '10-days-in-japan-itinerary',
  '2-weeks-in-japan-itinerary',
  '3-weeks-in-japan-itinerary',
  '5-days-in-japan-itinerary',
  'best-day-trips-from-kyoto',
  'best-day-trips-from-tokyo',
  'best-places-to-visit-in-japan',
  'flights-to-japan-from-us',
  'getting-around-japan-trains-jr-pass',
  'hakone-day-trip-guide',
  'himeji-castle-day-trip-guide',
  'how-to-plan-first-japan-itinerary',
  'japan-itinerary-7-days',
  'japan-itinerary-ideas',
  'kamakura-day-trip-guide',
  'kansai-airport-to-kyoto-osaka',
  'nara-day-trip-guide',
  'nikko-day-trip-guide',
  'tokyo-airport-transfers'
);

-- ryokan-onsen — 5 article(s)
update japan.articles set swamp = 'ryokan-onsen' where slug in (
  'best-onsen-towns-near-tokyo-kyoto',
  'japan-etiquette-for-americans',
  'onsen-etiquette-for-foreigners',
  'tattoos-and-onsen',
  'what-is-a-ryokan'
);

-- seasonal-timing — 7 article(s)
update japan.articles set swamp = 'seasonal-timing' where slug in (
  'autumn-foliage-japan-timing',
  'best-time-to-visit-japan',
  'cherry-blossom-season-japan',
  'golden-week-japan-what-closes',
  'japan-rainy-season-typhoons',
  'obon-japan-mid-august',
  'winter-in-japan-snow-onsen'
);

-- verify:
--   select swamp, count(*) from japan.articles group by swamp order by 2 desc;
-- every non-null swamp must appear in SITE_CONFIG.guide.hooks (cash-access is
-- deliberately hook-less: its surfaces fall back to the thesis, fail-open).
