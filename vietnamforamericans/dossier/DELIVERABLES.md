# Vietnam, End to End. — Stage A3 deliverables for the site · 2026-10-14

These are the strings the site's Stage 5c surfaces need (`packages/config/site.ts` → `SITE.guide`),
written from the shipped decisions. Hooks are RAW: accurate first, punchy second; the `marketing`
skill's three-part test (name the wrong move → concrete stake → open loop) strengthens them before
they ship. ★ = the user's call.

## ★ Name (A3)

**Vietnam, End to End.** — default. Alternatives proposed: *Vietnam, in Sequence.* · *Vietnam, Top to Bottom.*

Backfill (admin, dry-run by default; `dry_run:false` writes 39 spans across 39 articles):
```
POST https://vietnamforamericans-admin.vercel.app/api/guide-name-backfill
{ "name": "Vietnam, End to End.", "dry_run": true }
```

## Thesis (the master hook)

> A thousand-mile country, two weeks, three seasons that never agree — and the ticket is bought
> before anyone looks at a weather table. The order that keeps the trip whole.

## The book's own numbers (never invented)

| field | value |
|---|---|
| pages | 76 (the book) + 7 (the Field Sheet) + 108 (phone edition) — v4, 2026-10-17 |
| decisions | 11 |
| failureModes | 23 rows in three ledgers (hospital 7 · days 10 · money 6) — v4 |
| figures | 14 computed figures + 32 plates — v4 |
| priceAnchor | *(left empty — no book figure is a dollar amount; the stakes are days and refusals)* |

## Hooks by swamp id (`hooks` — band-shaped, two beats)

| swamp id | hook |
|---|---|
| north-south-routing | Direction is decided by three things you settle before you ask the question: the airline map, the month, and the e-visa form. The book shows which end to start from for your month, and where the slack goes. |
| halong-bay-cruise-choice | A one-night cruise claims two days of a northern leg that has four. The book prices the bay, Ninh Bình and Sapa in days, so the leg holds what it can. |
| visa-choice | Four fields on the e-visa form are binding and none can be changed from inside the country. The book settles the route shape first, so the form is filled in for the trip you will actually take. |
| motorbike-or-driver | The shop hands you the keys against a photocopy; the insurer reads the policy after the crash. The book covers every leg of a first trip without renting a bike, legally. |
| long-leg-transport | Fly above five hundred miles, never below a hundred and fifty, and take the one train that is the day's best hour. The book sorts every leg by distance, with the overnight legs that have no fallback. |
| mekong-day-vs-overnight | The floating market is finishing at the hour the coach circuits leave the city. The book prices each ending of the trip in days — the delta, Phú Quốc, Côn Đảo, the city — and says which the last block can absorb. |
| cash-vs-card | Cards work in four cities and stop; the ATM fee is flat and the cap is low. The book turns that into one withdrawal rule and a cash boundary around the itinerary. |
| hoian-base-choice | Three bases an hour apart produce three trips, and the tailor needs two full days. The book scores them on what each costs per day, and when the season takes the beach off the table. |
| sapa-trek-choice | Sapa is five hours of mountain road each way with no flight behind it. The book says when the mountains earn that, and when Ninh Bình gives the landscape for a fifth of the travel. |
| tet-timing | Tết does not make one week inconvenient; it pulls every transport booking months earlier and inverts city and coast prices. The book says whether to go through it or around it, and what to fix the day the dates are known. |

## Aside hooks (`asideHooks` — the shortest, self-doubt-driven form)

| swamp id | aside |
|---|---|
| north-south-routing | Did the ticket pick your direction before the weather did? |
| halong-bay-cruise-choice | Does the northern leg still hold Ninh Bình once the cruise has taken two days? |
| visa-choice | Did you name the gate you will actually leave by? |
| motorbike-or-driver | Who pays the hospital if the shop never asked for a licence? |
| long-leg-transport | Is this the leg to fly, the leg to train, or the one with no fallback? |
| mekong-day-vs-overnight | Will the coach be at Cái Răng while it is running? It never is. |
| cash-vs-card | How far off the main line can your cash take you? |
| hoian-base-choice | Will you be inside the town at seven, or driving to it at noon? |
| sapa-trek-choice | Is the trek the reason, or was Sapa just on a list? |
| tet-timing | Does one mid-trip flight carry the whole plan through Tết week? |

## Inline hooks (`inlineHooks` — connective, deepen rather than repeat)

| swamp id | inline |
|---|---|
| north-south-routing | The direction is the residue of the month, the airline map and the visa form; the manual works the three together and puts the slack where the storm is. |
| halong-bay-cruise-choice | The bay, Ninh Bình and Sapa compete for the same four or five days; the manual prices each in days before anything is booked. |
| visa-choice | Duration, entries, port in, port out: the manual settles the trip's shape first, then fills the form once. |
| motorbike-or-driver | The licence, the insurer and the legs the alternatives reach are one decision; the manual makes it with the State Department's own words on the page. |
| long-leg-transport | Distance decides the mode; the manual draws every first-trip leg against the hours each option really costs door to door. |
| mekong-day-vs-overnight | The last block of days has a price for each ending; the manual sets the delta against the islands and the city on one scale. |
| cash-vs-card | A flat fee and a low cap turn into one rule, and the rule draws the itinerary's cash boundary. |
| hoian-base-choice | The base sets which hours you are in the town, and the season decides whether the beach base works at all. |
| sapa-trek-choice | The road is the cost; the manual weighs it against the bay and Ninh Bình for the days the northern leg actually has. |
| tet-timing | A single lunar date reorders every other booking; the manual says which to lock first. |

## Inline CTAs (`inlineCtas` — a benefit, never the title)

| swamp id | cta |
|---|---|
| north-south-routing | See which end to start from for your month. |
| halong-bay-cruise-choice | See what the northern leg can hold. |
| visa-choice | See what the form commits you to. |
| motorbike-or-driver | See every leg covered without renting. |
| long-leg-transport | See which legs fly and which one trains. |
| mekong-day-vs-overnight | See what the last block can absorb. |
| cash-vs-card | See the one withdrawal rule. |
| hoian-base-choice | See which base and how many nights. |
| sapa-trek-choice | See when Sapa earns its road. |
| tet-timing | See whether to go through it or around it. |

## Decision teasers (`decisionTeasers`, index → `teaserBySwamp`)

0 How many days do you really have, and how many regions do they buy? · 1 Which month, and which end do you start from? · 2 What does the e-visa form commit you to? · 3 Ride it yourself, ride pillion, or hire the driver? · 4 Fly, train, or sleep through it — leg by leg? · 5 The bay, Ninh Bình, or Sapa — which one does the northern leg carry? · 6 Hội An, An Bàng, or Đà Nẵng — and how many nights does the tailor need? · 7 What can the last block of days absorb? · 8 Which beach — and does the month leave you a choice? · 9 Your dates touch Tết. Go through it, or around it? · 10 How much cash, and where does the card quietly stop?

teaserBySwamp: north-south-routing→1 · halong-bay-cruise-choice→5 · visa-choice→2 · motorbike-or-driver→3 · long-leg-transport→4 · mekong-day-vs-overnight→7 · cash-vs-card→10 · hoian-base-choice→6 · sapa-trek-choice→5 · tet-timing→9

## Decision chain (`decisionChains`, one chain, entry article `vietnam-itinerary-first-timers`)

"Before you touch the e-visa form":
1. How many days do you really have? → `/category/one-week` (door north-south-routing)
2. Which month, and which end do you start from? → `/category/best-time-to-visit` (door north-south-routing) · note: the day count fixes the regions, but the month decides which end is in season — the ticket should follow the weather, not precede it
3. What does the e-visa form commit you to? → `/category/entry-and-visa` (door visa-choice) · note: direction and days are set, but the form also names the exit gate — a Cambodia loop or a river exit must be decided before applying
4. The bay, Ninh Bình, or Sapa? → `/category/halong-bay-sapa` (door halong-bay-cruise-choice) · note: the visa's duration is now fixed, so the northern leg has a hard day budget and the cruise claims two of them

## Method entries (`methodEntries` — "Why we make this call")

1. **Do not rent a motorbike** · choice: every leg of a first trip is covered without self-drive · dependsOn: the State Department's statement that a US licence and an IDP are invalid, and that insurance may not pay after an accident · unknown: how often insurers actually refuse · reversal: a Vietnamese licence conversion route for short-stay visitors · refused: printing anecdotal "I rode and was fine" evidence.
2. **No ATM fee or cap figure** · choice: the structural rule (flat fee, low cap → the maximum, rarely) · dependsOn: the corpus-wide structure · unknown: any bank's own foreign-card tariff, which no primary source publishes · reversal: a bank publishing a schedule · refused: copying a blog's number.
3. **Tết dates printed only on the Field Sheet** · choice: the book carries the mechanism, the sheet the date · dependsOn: Government Office Document 10065/VPCP-KGVX (4–10 Feb 2027) · unknown: 2028 · reversal: a revised announcement · refused: a date frozen in a book that outlives it.

## Site config and operator settings still ★

- `SITE.guide.name/thesis/pages/decisions/failureModes/figures/hooks/asideHooks/inlineHooks/inlineCtas/decisionTeasers/teaserBySwamp/decisionChains/chainArticles/methodEntries` ← the values above (branch `guide-vietnam-end-to-end`, not pushed).
- `SITE.guide.cover` ← media keys of `build/cover-web.jpg` (exported; upload is the operator's).
- `site_settings.guide_price` (fleet default **$24**), `guide_checkout_url` (a Stripe payment link with `after_completion` → `/guide/success?session_id=`), `guide_ads_enabled` — all set from the admin Guide panel; the product goes live only when all three exist.
- The backfill above, after the name is confirmed.

## Added 2026-10-17 — raw hooks for the two new swamps (★ user confirms; marketing skill strengthens)

The DB now carries `swamp` = `halong-or-ninh-binh` on two-days-from-hanoi-halong-or-ninh-binh and
`hue-how-long` on how-many-days-for-hue; until `SITE.guide.hooks` has these keys the surfaces fall
back to the thesis.

| swamp id | hook (band) | aside | inline |
|---|---|---|---|
| halong-or-ninh-binh | The bay is cancelled by the port authority, not the operator, and a two-day window has nowhere to reschedule into. The book turns the forecast into the call — boat or rowboat — and keeps the other as the same-morning fallback. | Is the forecast for your two days calm enough to put them on a boat? | Which of the two you give the days to is one node in the month-by-region table the book is built on. |
| hue-how-long | Three guidebooks give Huế three answers because they never say whose trip they are planning. The book sets Huế's nights by what you came for, out of the same pool that pays for Hội An and Hanoi. | Is Huế a base or a stop on the way through — and did the pool of nights decide, or the itinerary you copied? | How many nights Huế takes is settled with the rest of the central-coast allocation in the book. |

### Strengthened 2026-10-17 (marketing three-part test) — shipped to `SITE.guide` in site.ts

| swamp id | band | aside | inline | CTA |
|---|---|---|---|---|
| halong-or-ninh-binh | You'll want the overnight cruise for your two free days. The port authority grounds every boat at once, and a two-day window has nowhere to move to. The manual prices the bay, Ninh Bình and Sapa in days, so the leg still holds when the bay doesn't sail. | Two days, one boat, and a port authority that grounds them all. Is Ninh Bình already in the plan? | The bay, Ninh Bình and Sapa are paid for from the same four or five days; the manual prices each before the forecast gets a vote. | See what the northern leg can hold when the bay doesn't sail. |
| hue-how-long | You'll give Huế the single night the itinerary templates give it, and see the citadel or the tombs but not both. The manual sets Huế's nights from the same pool that pays for Hội An and Hanoi, by what you came for. | One night in Huế means the citadel or the tombs. Which one were you going to drop? | Huế's nights come out of Hội An's; the manual allocates the central coast as one block, by trip length and by history, beach or food. | See how many nights Huế takes from the pool. |

Both written against what v3 actually holds (D06 prices the northern leg in days and names the port authority as the canceller; D07 allocates the central-coast nights). They do not promise the v4 forecast rule or the Huế-by-interest rule until v4 ships. Unproven until link_clicks speak.
