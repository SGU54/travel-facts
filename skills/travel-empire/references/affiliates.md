# Affiliates (Stage 4, step 6)

Referral links are a separate, explicit phase — never mixed into writing or internal
linking (internal = SEO/engagement; referral = revenue; different intent, different pass).

## Three placement types per article

1. **Info box** — after the first H2: short contextual recommendation.
2. **Comparison table** — hotel/tour articles: options with price ranges + booking links.
3. **CTA box** — before the conclusion: the primary affiliate button.

## Mapping — by category SLUG (language-neutral)

The mapping keys on the category's canonical slug, never its display name, so it works
across every site language. Localized display names live in the DB.

| category_slug | Primary | Secondary |
|---------------|---------|-----------|
| where-to-stay | Booking.com | Airbnb |
| itineraries / day-trips | Viator | GetYourGuide |
| visas-and-documents | iVisa | — |
| getting-there / flights | Skyscanner | — |
| insurance-and-safety | SafetyWing | — |
| things-to-do | GetYourGuide | Viator |
| food-and-drink | **None — deliberate trust builder** | — |

Only programs actually approved for the site (declared in `SITE_CONFIG.affiliates`) may be
used. Per-site monetization tags (e.g. Travelpayouts) use THIS site's own ID — never
another site's (hard rule 6).

## Commission reference

| Program | Network | Commission |
|---------|---------|-----------|
| Booking.com | CJ Affiliate | ~4% of booking |
| GetYourGuide | Direct (`gyg.me/CODE`) | 8% |
| Viator | Direct / TripAdvisor | 8% |
| Skyscanner | Direct | CPC/CPA |
| SafetyWing | Direct | 10% recurring |
| iVisa | Direct | $20–50 flat |

## Mandatory disclosure

Every article containing affiliate links carries a disclosure in the SITE'S language,
placed near the first affiliate link or in the article footer. Canonical English source
string (translate per site):

> "This article contains affiliate links. If you book through them we earn a small
> commission at no extra cost to you."

Example localization (Spanish): "Este artículo contiene enlaces de afiliado. Si reservas a
través de nuestros enlaces recibimos una pequeña comisión sin coste adicional para ti."

The per-site translated string lives in `SITE_CONFIG.affiliates.disclosure`;
validate-batch.mjs checks for its presence.

## Rules

- **Natural, not forced.** A link belongs where a reader genuinely wants to act. Food
  articles intentionally carry none.
- **Never invent prices or properties** to justify a link — pull from facts.json pools.
