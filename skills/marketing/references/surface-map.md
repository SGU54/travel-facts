# M4 — Placement: the site-wide surface map

Where the guide appears beyond the article page — intent-gated, never reach-gated.
The question per surface is always: is the reader in a decision moment the guide
resolves? Reach is not the goal; relevance at the right moment is.

## The map (ranked by intent)

| surface | reader's moment | placement | hook source | /go/ src |
|---|---|---|---|---|
| trip-builder tool (`/build-my-trip`) | actively sequencing — peak intent on the site | one callout in/under the result panel: the guide does this in depth | sequencing hook | `build-tool` |
| logistics category pages (Itineraries, Getting Around, Where to Stay, Plan Your Trip — plus site-specific ones like Ferries) | self-selected into the guide's subject | ONE band at the listing's foot | that category's swamp | `category-<slug>` |
| article pages | reading a swamp | the three 5c surfaces (band, inline, aside) | article's swamp tag | `end-band` / `inline` / `aside` |
| related-articles rail | just finished, choosing next | the guide as one card among "Keep reading" | article's swamp | `related` |
| homepage | front door, mixed intent | ONE band below the fold (near Featured Guides) | general thesis | `home` |
| global header + footer | everywhere | one quiet nav link "The Guide" (nav furniture — doesn't count toward caps) | — | `nav` |
| 404 | lost | one recovery line → /guide | — | `404` |
| DRY category pages (Food, Etiquette, Safety…) | not a logistics decision | **NOTHING** | — | — |

## The rules

1. **One per page, site-wide.** The article density cap (≤2 besides the aside)
   extends to every page type: one guide surface per non-article page, maximum. The
   nav link is furniture and exempt.
2. **Intent-gated.** Dry pages stay dry — forcing the guide onto Food & Drink is the
   meadow-with-a-bog error at page level. The doctrine's proportionality rule applies
   to the whole site.
3. **Context supplies the hook.** Where there's no article tag, the category or tool
   context picks the door (Ferries category → ferry-day hook). Never one generic line
   everywhere.
4. **Never twice in one short journey.** Homepage band + category band + article
   surfaces would show the guide five times before the reader reads anything. If a
   journey stacks surfaces, the earlier/weaker one yields (homepage yields to
   category; category yields to article).
5. **All gated + logged the same way.** Every placement obeys
   `guideReady() && ads_enabled` (the admin toggle kills them ALL at once) and routes
   through `/go/guide/{src}` — so common.link_clicks tells you which surface across
   the whole site earns its place.
6. **Data cuts, not opinions.** Build the two highest-intent additions first
   (build-tool, logistics categories); ship; after a month of clicks, cut what's
   dead. Never scale a placement that hasn't earned clicks on site one.

6. **The wet-map is code you ADAPT, not doctrine you assume.** The mechanism
   lives in the site's `GuideCategoryBand.tsx` (`CATEGORY_SWAMP`: category
   slug → swamp door) and ships with fleet-default entries. The M4 pass edits
   that map to THIS site's real category slugs and THIS site's swamp ids from
   `article-list.json` — an entry matching nothing simply never fires
   (fail-closed), which also means a forgotten adaptation fails SILENT, not
   loud: verify each wet category actually renders its band. A door no
   category opens (Rome: `money`) is reachable only through swamp-tagged
   articles — tag them or accept that hook dark.
