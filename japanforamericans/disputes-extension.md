# Disputes — fact extension (rail passes, IC cards, seasonal)

Reconciled 2026-09-16 from three panel members: **claude** (member #1), **deepseek**, **grok**.

Per `2-facts.md` step 5, a field where sources disagree is **left null in facts.json** and listed
here with each source's value. Never silently pick one; never average. Each needs a human ruling
against an official source before the affected article is written.

---

## 1. `ic_cards.physical_card_availability` — DIRECT CONTRADICTION ⚠ blocks 2 articles

The two external sources say opposite things about whether a visitor can buy a normal
unregistered Suica/Pasmo today.

| source | value | status claimed | source_url |
|---|---|---|---|
| claude | Suspended since 2023 (chip shortage); availability has shifted more than once since | verify_recommended | jreast.co.jp (authority named, page not fetched) |
| deepseek | **Still suspended** as of 2026; Welcome Suica the only reliable tourist option; PASMO PASSPORT ended Oct 2024 | verified | japantravel.navitime.com — **not an official source** |
| grok | **Resumed 1 March 2025**; ¥500 refundable deposit, widely available at JR East machines | verify_recommended | none given |

**Why it matters:** `mobile-suica-american-iphone` and `ic-card-day-pass-or-single-ticket` both
turn on what a reader can actually buy on arrival. Getting this backwards strands someone at a
ticket machine.

**Ruling needed:** check JR East's own English page. Note that grok's "resumed 1 March 2025"
is specific enough to be checkable, and deepseek's claim carries a non-official source, so the
burden of proof currently sits with deepseek.

---

## 2. `rail_passes.where_to_buy` — DIRECT CONTRADICTION ⚠

| source | value |
|---|---|
| claude | Online, or from sales offices and major JR stations in Japan |
| deepseek | **In-person sales at stations inside Japan ended 30 September 2023** |
| grok | Available at "major JR stations and travel centers after arrival (same prices)" |

**Why it matters:** a reader who plans to buy on arrival and cannot has lost the pass option
entirely. This is a trip-breaking error, not a detail.

**Ruling needed:** japanrailpass.net purchase page.

---

## 3. `ic_cards.mobile_topup_us_cards` — PARTIAL DISPUTE (Visa) ⚠ highest-value field

Agreed by all three: **American Express works**. Agreed: Discover and UnionPay do not.

| source | position on US-issued Visa |
|---|---|
| claude | Frequently refused for Suica top-ups |
| grok | Frequently refused — payment-network restriction on foreign Visa for Suica recharges |
| deepseek | **Accepted** (lists Visa, Mastercard, Amex, JCB) — but concedes "reports vary on Visa/Mastercard reliability; Amex most consistently reported working" |

**Reading:** 2 of 3 say Visa fails, and deepseek's own note undercuts its own answer. This is the
exact point where an American traveller fails at a gate, so it should not ship on a 2-1 vote.

**Ruling needed:** this field is a strong candidate for a Stage 6 `check` config rather than a
frozen prose value — it is behavioural, unannounced when it changes, and perishable.

---

## 4. `rail_passes.break_even_trips` — RESOLVED BY ARITHMETIC, not by vote

This was never a pollable fact — it is division. Computed from the reconciled prices:

```
7-day ordinary pass          ¥50,000
Tokyo–Kyoto reserved Hikari  ¥13,850  → 3.61 one-way legs ≈ 1.8 round trips
Tokyo–Shin-Osaka reserved    ¥14,400  → 3.47 one-way legs ≈ 1.7 round trips
```

claude said 3–4 legs; grok said 2–3 round trips (4–6 legs). Both bracket the answer, neither is
right. **The pass needs roughly four long legs — about two round trips — to pay for itself**, and
slightly fewer in practice because it also covers local JR and the Narita Express.

Recompute if any price changes. See dispute 5.

---

## 5. NEW FACT the panel surfaced — a price rise on 1 October 2026 ⚠ URGENT

Neither the spec nor claude's pass asked about this. Both external sources raised it
independently:

- **deepseek:** "A further ~5-6% increase is scheduled for October 1, 2026 (7-day Ordinary to
  ¥53,000)"
- **grok:** "From 1 Oct 2026 overseas-agent prices rise"; "~5-6% rise for overseas-agent
  purchases from 1 Oct 2026"

**Today is 2026-09-16. That is roughly two weeks away.**

Consequences if confirmed:
- every price in this extension has a two-week shelf life
- `break_even_trips` must be recomputed at ¥53,000 (→ 3.83 legs on the Kyoto route, still ~2
  round trips, so the conclusion survives — but the arithmetic in prose would be wrong)
- the two rail articles should be written with **fact-spans on every price from the start**, and
  the seed SQL run before publication, so the values update from the DB instead of going stale
  the week they ship
- grok's detail that the rise may apply to *overseas-agent* purchases specifically, not all
  channels, needs confirming — it changes the advice, not just the number

**Ruling needed before writing either rail article.**

---

## 6. `ic_cards.day_passes_tokyo` — MINOR, needs the official page

claude: ¥800 / ¥1,200 / ¥1,500 for 24/48/72h. grok: "typically ¥900–¥1,600 depending on
coverage". deepseek: null. Not a contradiction so much as nobody being certain. tokyometro.jp
settles it, and the Metro-vs-Toei coverage split matters as much as the price.

---

## Status discipline applied during reconciliation

deepseek returned `"status": "verified"` on eleven fields while citing japan-guide.com,
uscreditcards101.com and japantravel.navitime.com. None is an official source. Per
`3-writing.md` ("never self-promote AI research to verified") and the spec's own field shape
("for 'verified' the source_url MUST be the official page you checked"), every one of those was
**downgraded to `verify_recommended`** on merge.

grok's `verified` claims on rail pricing cite japanrailpass.net and a jreast.co.jp press PDF —
those are official, and were left at the status grok gave them pending one confirmation pass.

---

# RULINGS — resolved 2026-09-16 by fetching official pages and searching

| # | field | ruling | who was right |
|---|---|---|---|
| 1 | `ic_cards.physical_card_availability` | Unregistered Suica/PASMO **resumed 1 March 2025**; ¥500 deposit, ¥1,000-10,000 at station machines | **grok** |
| 2 | `rail_passes.where_to_buy` | In-Japan station **purchase** ended 1 Oct 2023. Online or overseas Exchange Order; the voucher is *exchanged* in Japan, which is not the same as buying | **deepseek** |
| 3 | `ic_cards.mobile_topup_us_cards` | US-issued **Visa refused** in Apple Wallet; Mastercard and Amex work | **claude + grok** |
| 4 | `ic_cards.day_passes_tokyo` | ¥1,000 / ¥1,500 / ¥2,000 and it covers Metro **and** Toei | **nobody** |
| 5 | `seasonal.public_holidays_list` | 16 holidays, fetched from the Cabinet Office | n/a — not a dispute, just unanswered |

## What each ruling added beyond settling the argument

**2 — purchase vs exchange.** The reason three sources disagreed is that two different things happen at a
JR station: you cannot BUY a pass there, but you can EXCHANGE a voucher there. Both external sources were
describing something real. The article has to make that distinction or a reader plans the wrong thing.

**3 — three details nobody asked for.** A US Mastercard tops up Suica but **not PASMO**. The Suica app
sometimes accepts a card Wallet refuses. And top-ups fail for everyone during a nightly maintenance window
until about 04:00 JST — a failure that looks like a card problem and is not. Any of the three is the
difference between a working phone and a traveller stuck at a gate.

**4 — a name collision.** The tourist **Tokyo Subway Ticket** (Metro + Toei) is a different product from the
plain **Tokyo Metro 24-hour ticket** (Metro only). claude's error came from conflating them. The clock also
runs a full 24/48/72 hours from first tap, not until midnight.

## The 1 October 2026 price rise — CONFIRMED on the official page

Overseas-agency prices rise from 1 Oct 2026: 7-day ordinary **¥53,000** (from ¥50,000), 14-day ¥84,000,
21-day ¥105,000; Green ¥74,000 / ¥116,000 / ¥147,000. **Buying online through the official site is not
affected.**

deepseek had the figure, grok had the scope; each was right about half. The channel split is the real
story, because from 1 October the standing advice inverts: online becomes cheaper than an agent.

Break-even rechecked: the online ¥50,000 arithmetic stands (3.6 legs ≈ two round trips). At the agency
price of ¥53,000 it becomes 3.83 legs — still about two round trips, so the conclusion survives the rise.

## Panel scorecard, for future weighting

- **grok** — 2 right, 1 wrong, and gave the most precise figures throughout. Cited official sources
  (japanrailpass.net, a jreast.co.jp press PDF).
- **deepseek** — 1 right, 3 wrong, and marked **eleven** fields `verified` while citing japan-guide.com,
  uscreditcards101.com and navitime. Every one was downgraded on merge. Its one win was a real one.
- **claude (me)** — 1 right, 2 wrong. Wrong on Tokyo pass prices and on the purchase-vs-exchange
  distinction.

The lesson is the skill's own: a confident `verified` from a model citing a travel blog is worth less than
a `verify_recommended` that names the right authority. Status discipline caught three of the four errors
before they reached prose.
