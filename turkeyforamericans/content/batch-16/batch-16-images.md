# Batch 16 — image manifest (10 files)

Download in this order. Filenames are the R2 public IDs — upload each
into `turkeyforamericans/articles/` with EXACTLY the name in the first column.

**Registers rule (this batch is health/insurance):** no patients, no faces, no
injuries, no ambulances in use, no emergency-room interiors, no medical
procedures, no readable personal documents. A factual article tips into a
scare-article the moment a photograph shows distress. Exteriors, empty rooms
and flat lays only.

Unsplash and Pexels ONLY. Landscape 3:2 or 4:3, 1600px or wider.

| file | article | what it shows | search |
|---|---|---|---|
| `bringing-medication-into-turkey-hero` | bringing-medication-into-turkey | prescription medication in original labelled packaging beside a passport on a plain surface, flat lay, no readable personal details | [Unsplash](https://unsplash.com/s/photos/medication%20packaging%20passport%20table) · [Pexels](https://www.pexels.com/search/medication%20packaging%20passport%20table/) |
| `bringing-medication-into-turkey-1` | bringing-medication-into-turkey | an open suitcase corner with a small clear toiletry bag and packaged medication, tidy, anonymous, no faces, no labels legible | [Unsplash](https://unsplash.com/s/photos/open%20suitcase%20packing%20organised) · [Pexels](https://www.pexels.com/search/open%20suitcase%20packing%20organised/) |
| `turkey-getting-treated-pharmacy-clinic-er-hero` | turkey-getting-treated-pharmacy-clinic-er | exterior of a Turkish pharmacy at night with the green neon ECZANE cross lit, street level, no people | [Unsplash](https://unsplash.com/s/photos/pharmacy%20green%20cross%20sign%20night) · [Pexels](https://www.pexels.com/search/pharmacy%20green%20cross%20sign%20night/) |
| `turkey-getting-treated-pharmacy-clinic-er-1` | turkey-getting-treated-pharmacy-clinic-er | a quiet Turkish clinic corridor or waiting area, empty, daylight, no patients, no medical equipment in use, no distress | [Unsplash](https://unsplash.com/s/photos/empty%20clinic%20corridor%20daylight) · [Pexels](https://www.pexels.com/search/empty%20clinic%20corridor%20daylight/) |
| `turkey-hospital-billing-what-to-expect-hero` | turkey-hospital-billing-what-to-expect | exterior of a modern Turkish private hospital building, daylight, no patients, no ambulances, no signage identifying a named group | [Unsplash](https://unsplash.com/s/photos/modern%20hospital%20building%20exterior) · [Pexels](https://www.pexels.com/search/modern%20hospital%20building%20exterior/) |
| `turkey-hospital-billing-what-to-expect-1` | turkey-hospital-billing-what-to-expect | hospital reception or admissions desk, wide and anonymous, no patients, no faces, no visible documents | [Unsplash](https://unsplash.com/s/photos/hospital%20reception%20desk%20empty) · [Pexels](https://www.pexels.com/search/hospital%20reception%20desk%20empty/) |
| `turkey-insurance-exclusions-activities-hero` | turkey-insurance-exclusions-activities | paragliders in the air above the Ölüdeniz coastline, distant, no identifiable faces, no injury or distress | [Unsplash](https://unsplash.com/s/photos/paragliding%20Oludeniz%20Turkey%20coast) · [Pexels](https://www.pexels.com/search/paragliding%20Oludeniz%20Turkey%20coast/) |
| `turkey-insurance-exclusions-activities-1` | turkey-insurance-exclusions-activities | scooters parked in a row on a Turkish coastal street, no riders, no faces, no visible plates | [Unsplash](https://unsplash.com/s/photos/scooters%20parked%20street%20Turkey) · [Pexels](https://www.pexels.com/search/scooters%20parked%20street%20Turkey/) |
| `us-travel-insurance-turkey-what-it-covers-hero` | us-travel-insurance-turkey-what-it-covers | travel documents, passport and a phone on a plain surface, flat lay, no faces, no identifiable policy paperwork | [Unsplash](https://unsplash.com/s/photos/passport%20travel%20documents%20flat%20lay) · [Pexels](https://www.pexels.com/search/passport%20travel%20documents%20flat%20lay/) |
| `us-travel-insurance-turkey-what-it-covers-1` | us-travel-insurance-turkey-what-it-covers | itemised paperwork and receipts on a desk, anonymous, no readable text, no personal details | [Unsplash](https://unsplash.com/s/photos/receipts%20paperwork%20desk) · [Pexels](https://www.pexels.com/search/receipts%20paperwork%20desk/) |

## Flagged slots

- **`turkey-hospital-billing-what-to-expect-1`** (reception desk) — the risk is
  catching a patient or a legible sign. Widen to an empty lobby or an
  architectural interior rather than a healthcare-branded one.
- **`turkey-getting-treated-pharmacy-clinic-er-1`** (clinic corridor) — search
  results skew to stock hospital scenes with staff and patients. An empty,
  well-lit corridor or waiting area is the target; if nothing clean turns up,
  substitute a second pharmacy exterior rather than settle for a scene with
  people in it.
- **`turkey-insurance-exclusions-activities-hero`** — paragliders must be
  distant specks against sky or coastline. Anything close enough to read a
  face or a harness reads as a risk photo, which is the wrong register for an
  article about policy wording.

## After upload

Confirm 10 files, not 20 — macOS writes `._` AppleDouble twins when copying to
FAT/exFAT or a network share. `dot_clean .` or
`find . -name '._*' -delete` before uploading, and
`export COPYFILE_DISABLE=1` in `~/.zshrc` to stop it recurring.
