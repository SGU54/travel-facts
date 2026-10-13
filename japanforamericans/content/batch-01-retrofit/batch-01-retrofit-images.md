# Batch-01 retrofit — image manifest

5 **in-body images only** (heroes are untouched — these 5 articles already have working
heroes). Content now lives on the Untitled volume, alongside every other site's content
(`travel-facts/<site>/content/`) — NOT in the site repo (`content/` there is gitignored
working-file storage and stays empty between sessions).

Body images and hero images are kept in **separate folders** per batch going forward, so
there's no ambiguity about which is which: `hero-images/` (existing convention, all
batch-01..10 folders renamed to this) and `body-images/` (new — this batch is the first
to use it). Download the 5 images below, in order, into:

```
/Volumes/Untitled/travel-facts/japanforamericans/content/batch-01-retrofit/body-images/
```

(any filenames — the upload script sorts by numeric prefix if you name them
`1_...png` .. `5_...png`, otherwise by download time). Then, **from the site repo root**
(the script and its R2 credentials live there, not on the volume):

```
cd /Users/sg54/Desktop/travel-sites/japanforamericans
node scripts/upload-batch.mjs \
  /Volumes/Untitled/travel-facts/japanforamericans/content/batch-01-retrofit/body-images \
  /Volumes/Untitled/travel-facts/japanforamericans/content/batch-01-retrofit/import-batch-01-retrofit.array.json \
  --body-only
```

`--body-only` is a new flag (added during this retrofit) that skips hero targets — only
needed for a retrofit pass like this one where the heroes aren't changing. It will show
you the mapping and ask to confirm before uploading anything.

Pick images that are **≥1600px landscape, free commercial license, no recognizable
faces, no brand/logo signage**. Unsplash and Pexels are both free-commercial/no-attribution.

---

### 1. do-americans-need-visa-japan-1
**Article:** Do Americans Need a Visa for Japan?
**Brief:** A calm, well-lit international arrivals hall at a Japanese airport — clean
signage, a few travelers with luggage, welcoming rather than bureaucratic.
- https://unsplash.com/s/photos/narita-airport
- https://unsplash.com/s/photos/haneda-airport
- https://www.pexels.com/search/airport%20arrival%20hall/

### 2. flights-to-japan-from-us-1
**Article:** Flights to Japan from the US
**Brief:** Airplane wing view at sunset/sunrise through a cabin window during a
long-haul flight — calm, aspirational.
- https://unsplash.com/s/photos/airplane-wing-sunset
- https://unsplash.com/s/photos/airplane-window-clouds
- https://www.pexels.com/search/airplane%20window%20sunset/

### 3. is-japan-safe-for-americans-1
**Article:** Is Japan Safe for American Travelers?
**Brief:** A calm, well-lit Japanese city street at dusk or night — soft lighting,
storefronts, safe and inviting. No police/emergency imagery.
- https://unsplash.com/s/photos/tokyo-street-night
- https://unsplash.com/s/photos/kyoto-street-evening
- https://www.pexels.com/search/japan%20street%20night/

### 4. money-in-japan-cash-cards-ic-1
**Article:** Money in Japan: Cash, Cards & IC Cards Explained
**Brief:** An IC card (Suica/Pasmo) being tapped at a train ticket gate, or yen
banknotes/coins on a small tray at a shop counter — everyday, practical.
- https://unsplash.com/s/photos/suica-card
- https://unsplash.com/s/photos/yen-banknotes
- https://www.pexels.com/search/japan%20train%20ticket%20gate/

### 5. japan-etiquette-for-americans-1 ⚠ composite/specific scene
**Article:** Japan Etiquette: 10 Things Americans Should Know
**Brief:** Shoes lined up at a genkan (entryway) with slippers set out — traditional
Japanese home or ryokan interior, warm and inviting. This exact scene is uncommon in
free stock — if nothing close comes up after two searches, widen to the strongest
on-theme shot of a **ryokan interior or entrance** instead of forcing the literal shoes.
- https://unsplash.com/s/photos/ryokan-entrance
- https://unsplash.com/s/photos/japanese-slippers
- https://www.pexels.com/search/ryokan%20interior/
