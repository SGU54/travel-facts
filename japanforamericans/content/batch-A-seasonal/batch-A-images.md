# Batch A — image manifest (seasonal)

**10 images: 5 heroes + 5 in-body.** These are new articles, so each needs both.

Download **in this exact order** into `content/batch-A-seasonal/hero-images/` and
`content/batch-A-seasonal/body-images/` respectively — `upload-batch.mjs` maps by
download order and stops on a count mismatch.

Every link below is a **page to pick from, not a direct download.** Before saving, check:

- live, landscape, **≥1600px wide**
- Unsplash / Pexels license (free commercial, no attribution)
- **no recognizable faces**, no brand or logo signage in the foreground
  (distant, incidental signage is fine — realism beats sterility)

Only Unsplash and Pexels. Gallery-search URLs are constructed and always resolve; the
specific photo pages were surfaced by search and are pre-vetted single shots.

---

## 1 — `cherry-blossom-season-japan-hero`

**Brief:** cherry trees in full bloom over a Kyoto or Tokyo canal path, people walking
beneath at a natural density. Daylight. Not an empty staged shot, not a close-up of one
branch — the article is about a season and a crowd, not a flower.

- https://unsplash.com/photos/cherry-blossoms-arch-over-a-canal-with-people-walking-KDjYIvQF1YI ← closest to brief (Philosopher's Path, people present)
- https://unsplash.com/photos/cherry-blossoms-line-a-canal-path-with-stone-walkway-0mufRTPZxsc
- https://unsplash.com/s/photos/kyoto-sakura
- https://www.pexels.com/search/kyoto%20cherry%20blossom/

## 2 — `cherry-blossom-season-japan-1`

**Brief:** blossom viewing as a social occasion — people sitting under the trees in a park,
picnic sheets, ordinary density. This is the "hanami is a party, not a spectator sport"
point in the body.

⚠ **Hard slot.** Groups of seated people means faces. Widen rather than hunt: a wide,
high, or back-view shot of a crowded park under blossom carries the point without close
portraits.

- https://unsplash.com/s/photos/hanami
- https://unsplash.com/s/photos/japanese-cherry-blossom
- https://www.pexels.com/search/hanami/

---

## 3 — `golden-week-japan-what-closes-hero`

**Brief:** a Japanese public space at holiday density — a packed shopping street, a station
concourse, a crowded temple approach. Orderly rather than chaotic. Daylight. The subject is
scale of domestic crowd, so a landmark is not needed and a wide frame is better.

- https://unsplash.com/s/photos/tokyo-crowd
- https://unsplash.com/s/photos/shibuya-crossing
- https://www.pexels.com/search/tokyo%20crowd/

## 4 — `golden-week-japan-what-closes-1`

**Brief:** a packed train platform or a full Shinkansen concourse — the "reserved seats sell
out" point made visually.

⚠ **Hard slot.** Platform crowd shots are usually face-heavy. Fallback: a long shot down a
platform, or a departure board dense with services, which carries the same idea cleanly.

- https://unsplash.com/s/photos/japan-train-platform
- https://unsplash.com/s/photos/shinkansen
- https://www.pexels.com/search/japan%20train%20station/

---

## 5 — `autumn-foliage-japan-timing-hero`

**Brief:** Japanese maple in deep red over a Kyoto temple garden or stone path, late
afternoon light. A few visitors visible for scale is good; an empty garden reads as a
postcard and undersells the crowding the article discusses.

- https://unsplash.com/s/photos/momiji ← tagged japanese maple / red leaves / kyoto
- https://unsplash.com/s/photos/autumn-japan
- https://unsplash.com/s/photos/japanese-garden
- https://www.pexels.com/search/autumn%20in%20japan/

## 6 — `autumn-foliage-japan-timing-1`

**Brief:** autumn colour away from the famous gardens — a maple over an ordinary street, a
riverbank, a hillside path. Supports the "colour beyond the celebrated gardens" section, so
it should deliberately NOT look like a landmark.

- https://unsplash.com/s/photos/japanese-maple-tree
- https://unsplash.com/s/photos/maple-tree
- https://www.pexels.com/search/japanese%20maple/

---

## 7 — `obon-japan-mid-august-hero`

**Brief:** Japanese lanterns glowing at a summer night festival. Warm light, evening. The
lantern is the visual shorthand for Obon and carries it without needing a crowd.

- https://unsplash.com/photos/japanese-lanterns-hanging-at-a-night-festival-N-wOawq58Co
- https://unsplash.com/photos/many-illuminated-lanterns-at-an-outdoor-festival-at-night-jd6EupgO8yc
- https://unsplash.com/photos/glowing-japanese-lanterns-at-a-night-festival-guEJrCgWtGs
- https://unsplash.com/s/photos/japan-summer-festival

## 8 — `obon-japan-mid-august-1`

**Brief:** a neighbourhood Bon Odori — people in yukata dancing in a circle around a raised
platform, summer evening.

⚠ **Hardest slot in the batch.** The literal scene is scarce in free stock and is inherently
face-heavy. Two fallbacks, in order of preference:
1. A yukata-and-lantern street scene from behind, no faces.
2. **Background + AI prompt.** Pick a strong evening festival background from the links
   below and I will write the generation prompt — that route has produced the better images
   on this site before.

- https://unsplash.com/s/photos/yukata
- https://unsplash.com/s/photos/japanese-festival
- https://www.pexels.com/search/japanese%20festival/

---

## 9 — `japan-rainy-season-typhoons-hero`

**Brief:** a Japanese garden or temple path in rain — wet stone, saturated green moss, a
clear umbrella if one appears. Atmospheric rather than bleak: the article argues June is
undervalued, so the image must make wet Japan look appealing, not miserable.

- https://unsplash.com/s/photos/japan-rain
- https://unsplash.com/s/photos/kyoto-rain
- https://www.pexels.com/search/rain%20japan/

## 10 — `japan-rainy-season-typhoons-1`

**Brief:** hydrangeas in rain at a temple, or a moss garden at peak saturation — the "gardens
look extraordinary in wet weather" point.

- https://unsplash.com/s/photos/hydrangea-japan
- https://unsplash.com/s/photos/moss-garden
- https://www.pexels.com/search/hydrangea/

---

## After the images are in

```bash
# once per repo, if not already installed
npm install @aws-sdk/client-s3

node scripts/upload-batch.mjs <folder> content/batch-A-seasonal/import-batch-A.array.json
```

Then — **mandatory, and the single most common way this pipeline ships a broken page** —
convert every `<!-- IMAGE_SLOT_1 -->` into a real figure tag before pushing:

```html
<figure><img src="https://img.sgfleetmedia.com/cdn-cgi/image/format=auto,width=1200/japanforamericans/articles/<slug>-1" alt="<the slot brief>" loading="lazy" /></figure>
```

`width=1200` is not decoration: without it Cloudflare serves the original at full resolution
into a 700px column. Pass condition: grep the finished JSON for `IMAGE_SLOT` → **zero**.
