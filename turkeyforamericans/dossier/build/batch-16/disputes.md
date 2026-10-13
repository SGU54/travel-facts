# Batch 16 — panel reconciliation

deepseek + grok, 23 leaf facts each. Both parsed (deepseek needed markdown
fences stripped, same as every Thailand panel).

## The hardened prompt worked

| panel | marked `verified` | citing an official domain |
|---|---|---|
| Thailand batch 19 (before hardening) | 24 / 40 | **2** |
| Thailand batch 20 (after) | 9 / 30 | 9 |
| **Turkey batch 16 — deepseek** | 1 | **1** |
| **Turkey batch 16 — grok** | 5 | **4** |

Naming the previous failure with numbers keeps working where the abstract rule
didn't. Both models also filled `_open_questions` honestly rather than
inventing values.

## The finding that reshapes the batch

**All four private-hospital cost figures came back null from both models**, and
both listed them in `_open_questions`:

- `health.er_visit_cost_private_try`
- `health.fracture_treatment_cost_private_try`
- `health.inpatient_night_cost_private_try`
- `pharmacy.walkin_clinic_cost_try`

No official or named-hospital self-pay tariff for a foreign patient exists
publicly. This is Thailand's Vein A again — the data isn't thin, it isn't
published at all.

**Article 1 was designed around those numbers.** It gets the Thailand fallback:
reduce to the sourceable mechanics and *delete* the price sentences rather than
estimate them. The article is still worth writing — see below.

## What replaced them

While verifying grok's emergency-obligation fact I found two mechanics
**neither model returned**, both from the same instrument (Regulation on
International Health Tourism and Tourist Health, Official Gazette 32882,
26 April 2025):

1. **`health.ministry_sets_health_tourism_prices`** — pricing for services under
   international health tourism and tourist health is *set by the Ministry of
   Health*, and facilities must itemise services on the invoice. This is
   precisely why no public self-pay price list turns up: the pricing sits in a
   ministry framework, not a hospital tariff page. It converts the null from a
   hole into an explanation.

2. **`health.two_regimes_tourist_vs_medical_tourism`** — the same regulation
   covers two different populations: someone who *travels to Turkey for
   treatment*, and a visitor who *falls ill while there*. Search results
   conflate them constantly, and an article that borrowed medical-tourism rules
   (authorisation certificates, complication insurance) to describe an injured
   holidaymaker would be wrong. Reported, not resolved — a good book node.

## Arbitrations

**`health.state_emergency_obligation_foreigners` — downgraded, value kept.**
grok marked it `verified` citing a private legal-publishing site. The *value*
is right: three independent legal publishers quote identical text — admission
of foreign patients for emergency care and unconditional medical intervention
are obligatory, and charges are collected *after* care. But the URL is not the
Official Gazette and I did not open the Gazette. `verify_recommended`.

**`health.air_ambulance_repatriation_usd` — NOT PRINTED.**
Three sources, three non-overlapping ranges: deepseek USD 60–80k (an Indian
embassy page, Turkey-to-elsewhere), grok USD 100–250k (an air-ambulance
operator's own marketing), and grok's note citing US State Dept at 20–200k.
Not averaged. The article says repatriation is separately and enormously
costly and quoted per case — no figure.

**`medication.common_us_restricted` — single source, categories only.**
grok returned null and flagged it open. deepseek's families (narcotic
analgesics, ADHD stimulants, benzodiazepines) are the standard controlled
classes and are consistent with the MFA customs rule. Usable as *categories*.
No brand named as banned without a TİTCK listing.

**`insurance.balloon_classification` — both agree, and it is the Call 4 fact.**
Both describe hot-air ballooning as excluded from base policies under aviation
or adventure-sports clauses unless explicitly listed or bought as an add-on.
grok adds that Turkish operator liability (SHGM-mandated) covers the operator's
liability for injury during the flight but not the passenger's own medical,
evacuation or trip-interruption costs. **That gap — operator-covered vs
passenger-covered — is the balloon node the book needs.** Reported here as
mechanics; the call stays in the book.

## Revised article 1

`turkey-healthcare-cost-without-insurance` →
**`turkey-hospital-billing-what-to-expect`**

It no longer reports prices, because there are none to report. It reports:

- the three hospital types and who bills whom
- the emergency obligation: treatment first, charges collected after
- that emergency transport itself *is* chargeable
- deposit / prepayment / guarantee-of-payment practice for non-emergency care
- direct-billing vs pay-and-claim
- that pricing sits in a Ministry framework, not a public tariff — which is why
  a traveler cannot price this in advance

That last line is a better article than the price table would have been, and
it hands the book a real edge: *you cannot get a number in advance, so the
decision has to be made another way.*

## Status of the block

25 facts: 4 `verified` (all on official `.gov.tr` domains), 21
`verify_recommended`, 5 carrying `value: null` whose sentences are **deleted,
never softened**.
