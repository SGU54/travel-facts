# Batch-17 retrofit — image manifest (final batch)

4 in-body images (places-to-visit + itinerary cluster). Download into
`/Volumes/Untitled/travel-facts/japanforamericans/content/batch-17-retrofit/body-images/`,
then from the site repo root:
```
cd /Users/sg54/Desktop/travel-sites/japanforamericans
node scripts/upload-batch.mjs \
  /Volumes/Untitled/travel-facts/japanforamericans/content/batch-17-retrofit/body-images \
  /Volumes/Untitled/travel-facts/japanforamericans/content/batch-17-retrofit/import-batch-17-retrofit.array.json \
  --body-only
```

### 1. best-places-to-visit-in-japan-1
Mt Fuji reflected in a Hakone lake with a red torii gate in the foreground, no recognizable faces.
- https://unsplash.com/s/photos/hakone-fuji-torii
- https://www.pexels.com/search/hakone%20lake%20fuji/

### 2. japan-itinerary-7-days-1
The Kyoto-bound Shinkansen departing a Tokyo Station platform, no recognizable faces.
- https://unsplash.com/s/photos/shinkansen-platform
- https://www.pexels.com/search/shinkansen%20station/

### 3. 2-weeks-in-japan-itinerary-1
The Itsukushima Shrine torii gate at Miyajima at high tide appearing to float on the sea, no recognizable faces.
- https://unsplash.com/s/photos/miyajima-torii
- https://www.pexels.com/search/miyajima%20floating%20torii/

### 4. 3-weeks-in-japan-itinerary-1
A traditional thatched-roof farmhouse in Shirakawa-go surrounded by mountains, no recognizable faces.
- https://unsplash.com/s/photos/shirakawa-go
- https://www.pexels.com/search/shirakawago%20village/

---

**This is the last image manifest.** Once all 17 batches' body images are sourced and
uploaded (batch-01-retrofit through batch-17-retrofit, listed in
`state.json` → `retrofit.images_pending`), the only remaining task is running
`japanforamericans-facts.sql` against `common.facts` (service role, Supabase SQL editor).
