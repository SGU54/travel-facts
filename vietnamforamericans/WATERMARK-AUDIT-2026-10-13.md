# Unsplash+ watermark audit — vietnamforamericans

**Date:** 2026-10-13
**Scope:** all 100 published article heroes + all 96 distinct in-body images = 196 images.
**Result:** 11 watermarked images across 9 articles. **ALL 11 REPLACED — RESOLVED.**

---

## How this was checked, and why

Three automated detectors were written and all three failed. The watermark is a
regular grid of faint light-grey "Unsplash+" text, so periodicity looked like
the obvious signal — but a photograph contains far stronger periodic structure
(train-carriage windows, railings, roof tiles, rice terraces) and every detector
ranked those above the real positives. The last one scored the known-watermarked
Hội An image at 97 while a verified-clean train photo scored 854.

**What works: looking, at 1:1.** The watermark is invisible below roughly 700px
wide, which is why it survived image selection in the first place — a contact
sheet at 300px shows nothing. Every image here was cut at native resolution
(no resizing) into 330×215 crops and read on contact sheets. Suspects were then
re-cut at 640×420 from a *different* region of the frame to confirm.

Images whose first crop was near-white (blown skies, white tables) were re-cut
from their darkest mid-tone window, because light grey on white is invisible.
All eight came back clean.

**Do not add an image to this site from a contact sheet.** Check it at full size.

---

## HEROES — 5 of 100

| # | Article | Where it shows |
|---|---------|----------------|
| 1 | `best-cooking-classes-vietnam` | article, category, any card |
| 2 | `best-street-food-tours-hanoi-saigon` | article, category, any card |
| 3 | `hoi-an-travel-guide` | article, category, **homepage Destinations tile**, **/category/where-to-go** |
| 4 | `sim-card-vs-esim-vietnam` | article, category, **homepage Latest guides** |
| 5 | `vegetarian-vegan-food-vietnam` | article, category, any card |

## IN-BODY — 6 of 96

| # | Image id | Article |
|---|----------|---------|
| 1 | `best-cooking-classes-vietnam-1` | best-cooking-classes-vietnam |
| 2 | `hoi-an-tailors-how-to-order-1` | hoi-an-tailors-how-to-order |
| 3 | `vegetarian-vegan-food-vietnam-1` | vegetarian-vegan-food-vietnam |
| 4 | `vietnam-itinerary-first-timers-1` | vietnam-itinerary-first-timers |
| 5 | `vietnam-itinerary-for-families-1` | vietnam-itinerary-for-families |
| 6 | `where-to-stay-hoian-danang-1` | where-to-stay-hoian-danang |

Two articles are hit twice (hero **and** body): `best-cooking-classes-vietnam`
and `vegetarian-vegan-food-vietnam`.

---

## RESOLVED — what was done

All 11 files were re-sourced from regular Unsplash and re-uploaded to R2 under
the **same object keys**, so no database row changed (the key is the public_id —
hard rule 10). Each replacement was verified at native resolution before upload
and again from the CDN after.

**Then they had to be re-keyed, and this is the part worth remembering.**
Replacing the object under the same key left the watermark live: Cloudflare
caches each transformed derivative at `/cdn-cgi/image/<opts>/<key>` with
`max-age=31536000, immutable`, and the article's derivative had been built
before the replacement. It was declared fixed on the strength of three transform
variants returning `cf-cache-status: MISS` — but the article requests different
transform options, and that one was a HIT with age 39595. **Check the exact URL
the page asks for, not a representative one.**

With no Cloudflare API token available, the fix is a new key: all 11 were copied
to `<id>-v2` and `articles.featured_image`, the in-body `<img src>` (through a
DOM) and `categories.featured_image` repointed — `scripts/rekey-corrected-images.mjs`.
Re-keying also surfaced two more category tiles pointing at watermarked heroes
(`food-tours-cooking-classes`, `vegetarian-dietary-needs`) that the first pass
had missed. Verified on the 11 exact derivatives the live pages request: all
`MISS`, all clean.

### The root cause, and the filter that prevents it

Unsplash's search API marks every paid preview with `plus: true` /
`premium: true` and serves it from `plus.unsplash.com` instead of
`images.unsplash.com`. Nothing in the original sourcing filtered on that. The
replacement script refuses any result carrying either flag or the plus host —
**it rejected 40 Unsplash+ results across 11 searches, about a quarter of
everything returned.** Any future sourcing must apply the same filter.

### Replacements (Unsplash License, free for commercial use)

| Object key | Photographer | Source |
|---|---|---|
| `best-cooking-classes-vietnam-hero` | Trường Trung Cấp Kinh Tế Du Lịch TP.HCM (CET) | unsplash.com/photos/GF_XTjtTSgc |
| `best-street-food-tours-hanoi-saigon-hero` | Frida Aguilar Estrada | unsplash.com/photos/PEgu_IdF1BM |
| `hoi-an-travel-guide-hero` | Mario La Pergola | unsplash.com/photos/0dxVxggDQSU |
| `sim-card-vs-esim-vietnam-hero` | Samsung Memory | unsplash.com/photos/eNRPdRgvA4U |
| `vegetarian-vegan-food-vietnam-hero` | Jamie Trinh | unsplash.com/photos/pHQKkShMNyQ |
| `best-cooking-classes-vietnam-1` | Mauro Lima | unsplash.com/photos/-ts92kxGCLk |
| `hoi-an-tailors-how-to-order-1` | Zainab Iqbal | unsplash.com/photos/lcI46gCA_6U |
| `vegetarian-vegan-food-vietnam-1` | Lee Milo | unsplash.com/photos/Xcsk_wVJWgo |
| `vietnam-itinerary-first-timers-1` | Gary Cacciatore | unsplash.com/photos/nT0DsYcXbbY |
| `vietnam-itinerary-for-families-1` | Florian Delée | unsplash.com/photos/EeukLUjiea4 |
| `where-to-stay-hoian-danang-1` | allPhoto Bangkok | unsplash.com/photos/tYd9AaYofn8 |

One slot needed re-sourcing after the first pass: every candidate returned for
the vegetarian article contained meat (bún chả, pork phở, fish). A vegetarian
guide illustrated with pork is a worse error than a watermark, so that query
was re-run against vegetarian terms.

`categories.featured_image` for **where-to-go** was repointed to the Cát Bà
karst while the Hội An file was compromised, and moved back to
`hoi-an-travel-guide-hero` once it was clean — it is the better tile for
"Where to go", and it is now the real old town at dusk rather than a
watermarked preview.

---

## Verified clean

The other 185 images. Spot-verified at 640×420 from two different regions:
`sapa-trekking-guide`, `halong-bay-day-trip-vs-overnight-cruise`,
`best-time-to-visit-vietnam`, `vietnam-itinerary-3-weeks`,
`vietnam-itinerary-14-days`, `hanoi-old-quarter-guide`, `train-street-hanoi`,
`da-nang-travel-guide`, `hue-imperial-city-guide`, `my-son-sanctuary-guide`,
`hai-van-pass-guide`, `marble-mountains-guide`,
`hoian-vs-anbang-vs-danang-where-to-base`, `mui-ne-guide`,
`chau-doc-cambodia-border-crossing`, `best-mekong-delta-homestay-tours`.

The four photographs in the homepage hero collage are all on that list.
