# Bali, in Its Own Time. — Stage A3 deliverables for the site · 2026-10-15

These are the strings the site's Stage 5c surfaces need (`packages/config/site.ts` → `SITE.guide`),
written from the shipped decisions. Hooks are RAW: accurate first, punchy second; the `marketing`
skill's three-part test (name the wrong move → concrete stake → open loop) strengthens them before
they ship. ★ = the user's call.

## ★ Name (A3)

**Bali, in Its Own Time.** — default; it carries the site's live thesis ("Bali keeps its own time")
into the book. Alternatives proposed: *Bali, Night by Night.* · *Bali, Base by Base.*

Backfill (admin, dry-run by default; `dry_run:false` writes the 45 guide-spans; the fleet backfills
WITHOUT the trailing full stop because the span sits mid-sentence):
```
POST https://baliforamericans-admin.vercel.app/api/guide-name-backfill
{ "name": "Bali, in Its Own Time", "dry_run": true }
```

## Thesis (the master hook)

> Ninety miles wide, measured in hours. Sixteen hours from home, one boat that answers to the sea,
> and a day the island stops. Where the nights go, and in what order.

## The book's own numbers (never invented)

| field | value |
|---|---|
| pages | 91 (the book) + 9 (the Field Sheet) + 127 (phone edition) + 4 (free sample) |
| decisions | 11 |
| failureModes | 20 rows in three ledgers (trip or hospital 6 · days 8 · money 6) |
| figures | 16 computed figures + 38 plates |
| priceAnchor | *(left empty — no book figure is a dollar amount; the stakes are nights, the sea and a chain of clauses)* |

## Hooks by swamp id (`hooks` — band-shaped, two beats)

| swamp id | hook |
|---|---|
| base-split | Every base comes with a list of what it is far from, and the list is the decision. The manual counts your nights, divides by three, and puts the bases in the order the arrival hour, the sea and the airport run impose. |
| traffic-time | The site prints no drive time because none would be true at the hour you read it. The manual replaces the clock with a rule: three or four stops in one direction, grouped by the base each sight is a short outing from. |
| wet-dry-season | July is the driest month, the fullest, and the one the strait is roughest in. The manual lays the four calendars side by side and says which coast and which length your month points to. |
| scooter-liability | The shop checks the deposit, not the licence class; the insurer reads the policy after the crash. The manual settles the chain at home and shows which base makes the scooter unnecessary. |
| boat-day-buffer | An island leg at the end of the trip puts the only weather-dependent link against the flight home. The manual places it in the middle, with the buffer the site's own margin requires. |
| holiday-collision | Nyepi closes the airport for twenty-four hours on a date that moves, and in 2027 it sits inside nine days without a working day. The manual says whether to go through it or around it, and how far clear to land. |
| entry-stack | A passport test, a visa, a levy, an arrival card and a customs declaration, on five sites with five deadlines. The manual puts them in the only order that works, starting months out and ending seventy-two hours before you land. |
| long-haul-arrival | No nonstop exists, so the hub, the ticket and the arrival hour are three decisions wearing one fare. The manual says which hub, why one ticket, and how far the first bed should be from the terminal. |
| health-chain | A pill that was legal at the pharmacy is a narcotic at the border; the clinic wants a deposit; the policy reads its scooter clause afterwards. The manual draws the chain and says which link to settle first. |
| money-leak | Six small percentages land on the same dollar, and the QR codes at every counter are closed to American apps. The manual says which two are removed at home and how to read the foot of the menu. |

## Aside hooks (`asideHooks` — the shortest, self-doubt-driven form)

| swamp id | aside |
|---|---|
| base-split | Did you book the beach first and spend the dawn hours asleep? |
| traffic-time | How many of today's stops are in the same direction? |
| wet-dry-season | Is July dry, or just dry on land? |
| scooter-liability | Does your licence have a motorcycle class, or just a scooter in the driveway? |
| boat-day-buffer | Is the boat back the day before the flight? |
| holiday-collision | Which day does the island stop this year, in Bali's calendar, not yours? |
| entry-stack | Did you renew the passport before you bought the visa? |
| long-haul-arrival | What local hour do you land, and how far is the first bed? |
| health-chain | Which class is your prescription in? |
| money-leak | Which of the six percentages did you leave at home? |

## Inline hooks (`inlineHooks` — connective, deepen rather than repeat)

| swamp id | inline |
|---|---|
| base-split | The nights decide the bases and three pins decide their order; the manual works the two together and puts the last night where the airport run is shortest. |
| traffic-time | Miles are stable and hours are not; the manual sorts every outing by the base it is a short outing from, so the day is planned from a rule. |
| wet-dry-season | Rain, crowd, surf coast and the strait run on four calendars; the manual overlays them and reads off the month's coast and its buffer. |
| scooter-liability | The licence class, the police stop and the insurer are one chain; the manual makes the call with the State Department's and the statute's own words on the page. |
| boat-day-buffer | The crossing has no fallback and the dry season is not the calm season; the manual prices each island leg in days and places it where a cancellation costs least. |
| holiday-collision | A moving date closes the airport and a holiday cluster closes the offices; the manual lays a trip over the decree, not a blog. |
| entry-stack | Five systems, one passport number; the manual settles the order so that no later form is filled against a document you no longer carry. |
| long-haul-arrival | The hub sets the final leg, the ticket sets who owns a delay, the arrival hour sets night one; the manual decides all three before the fare. |
| health-chain | Medicine class, border, clinic, policy, animal: the manual draws how they connect and where the base joins them. |
| money-leak | Two fees are the bank's, two are regulations, one is contested; the manual says which card, how much cash, and why no plan depends on a QR code. |

## Inline CTAs (`inlineCtas` — a benefit, never the title)

| swamp id | cta |
|---|---|
| base-split | See which base first, and how many nights each. |
| traffic-time | See what a day holds from your base. |
| wet-dry-season | See which coast your month points to. |
| scooter-liability | See every journey covered without a scooter. |
| boat-day-buffer | See where the island leg goes. |
| holiday-collision | See whether to go through Nyepi or around it. |
| entry-stack | See the five steps in the only order that works. |
| long-haul-arrival | See which hub, and how far the first bed. |
| health-chain | See which link to settle first. |
| money-leak | See the two fees you can remove at home. |

## Decision teasers (`decisionTeasers`, index → `teaserBySwamp`)

0 How many nights do you really have, and how many bases do they buy? · 1 Which base first, which last, and where does the boat go? · 2 Which month, and which coast does it point to? · 3 What does the entry stack commit you to, and in what order? · 4 Ride it yourself, ride pillion, or hire the driver? · 5 A day trip, island nights, the Gilis, or none — and where in the trip? · 6 How many stops does a day hold, and from which base? · 7 Your dates touch March. Through Nyepi, or around it? · 8 Which hub, one ticket or two, and what hour do you land? · 9 What breaks the chain: the medicine bag, the deposit, or the policy? · 10 Which card, how much cash, and where do the small percentages land?

teaserBySwamp: base-split→1 · traffic-time→6 · wet-dry-season→2 · scooter-liability→4 · boat-day-buffer→5 · holiday-collision→7 · entry-stack→3 · long-haul-arrival→8 · health-chain→9 · money-leak→10

## Decision chain (`decisionChains`, one chain, entry article `how-many-days-in-bali`)

"Before you book the beach":
1. How many nights do you really have? → `/category/by-trip-length` (door base-split)
2. Which base first, which last, and where does the boat go? → `/category/choosing-your-base` (door base-split) · note: the nights fix the number of bases, but the arrival hour, the sea and the airport run fix their order — the beach is last, not first
3. Which month, and which coast does it point to? → `/category/when-to-go` (door wet-dry-season) · note: the order is set, but the month decides which coast the surf is on and how much slack the boat needs — July is dry and rough at once
4. A day trip, island nights, the Gilis, or none? → `/category/boats-and-ferries` (door boat-day-buffer) · note: the month has set the buffer; the island leg now has a fixed number of days it can cost and a fixed place in the middle

## Method entries (`methodEntries` — "Why we make this call")

1. **No scooter on a car-only licence** · choice: every journey of a first trip is covered by a driver, an app or your feet · dependsOn: Law 22/2009's separate motorcycle class and the State Department's statement that a US licence alone is not recognised · unknown: whether any insurer would pay regardless · reversal: an official page stating a car licence covers a scooter · refused: "everyone rides" as evidence.
2. **No drive time anywhere in the book** · choice: road miles, the site's own, and a live-map rule · dependsOn: the site's measured distances and its refusal to freeze a duration · unknown: the hour you read it · reversal: none; a duration is wrong by construction · refused: copying a blog's "45 minutes to Ubud".
3. **The island leg in the middle third** · choice: the boat back at least one full day before the flight, two in July, August or the wet months · dependsOn: the harbour master's sailing approvals, the May 2023 wave forecast and the August 2025 capsizing as reported · unknown: any cancellation rate · reversal: a published cancellation record · refused: inventing a rate.
4. **Nyepi dates from the decree only** · choice: the book carries the mechanism, the sheet the date · dependsOn: the 2027 joint ministerial decree and the Hindu holiday letter · unknown: the 2027 airport hours · reversal: the operator's announcement · refused: a date from a blog that was true last year.

## Site config and operator settings still ★

- `SITE.guide.name/thesis/pages/decisions/failureModes/figures/hooks/asideHooks/inlineHooks/inlineCtas/decisionTeasers/teaserBySwamp/decisionChains/chainArticles/methodEntries` ← the values above (branch `guide-bali-in-its-own-time`, not pushed).
- `SITE.guide.cover` ← Cloudinary public_id of `build/cover-web.jpg` (exported; upload is the operator's). `previewImages` ← `build/preview-1..3.jpg` (contents, Decision 02 figure page, the bases figure).
- `site_settings.guide_price` (fleet default **$24**, country rule), `guide_checkout_url` (a Stripe payment link with `after_completion` → `/guide/success?session_id=`), `guide_ads_enabled` — all set from the admin Guide panel; the product goes live only when all three exist.
- The backfill above, after the name is confirmed.
