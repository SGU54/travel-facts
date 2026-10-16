# knowledge/ — Vietnam country knowledge DB (guidebook-derived)

Built from legally borrowed guidebooks read in the Internet Archive viewer (controlled digital lending). Learning material only.

## Rules that govern every file here
1. **Own words only.** Nothing is quoted. No sentence, table or list is reproduced from a book. Entries are paraphrased claims with a page pointer so a human can go back to the source.
2. **Everything dated 2013–2017 is a LEAD.** `status: "lead"` means: plausible, sourced, **unverified**. It must be checked against a current official source before it is trusted, written into an article, or promoted into `facts.json`. Hard rule 1 of the project (no unverified prices) applies in full.
3. **`status: "context"`** = durable background (history, geography, culture) that does not go stale on a 2-year horizon. Still paraphrase-only.
4. **`status: "conflict"`** = the book disagrees with `facts.json` or `corrections.json`. The project's fact layer wins. Each conflict is also logged in `../disputes.md` under "Guidebook leads vs facts.json".
5. **`status: "obsolete"`** = the book's claim is known to be superseded (e.g. visa-on-arrival letters, Victoria Express train). Kept so nobody re-imports it from another old book.
6. Never copy a directory/listing (hotel, restaurant, operator addresses). Named businesses appear only as `leads` with a reason to check they still exist.

## Files
| file | what it holds |
|---|---|
| `sources.json` | book registry: ID, edition, what was read, what was skipped |
| `regions.json` | per-region orientation: what the region is, bases, the book's "getting around" verdicts |
| `seasons.json` | climate, festival calendar, when-to-go logic, Tet mechanics |
| `transport.json` | arrival, intercity (air/rail/bus/car/boat), local transport, border crossings |
| `costs.json` | every money figure the books give, all `lead`, plus structural money rules |
| `rules.json` | visa, customs, health, safety, police, photography, legal norms |
| `culture-etiquette.json` | peoples, religion, manners, table, dress, language facts, shopping behaviour |
| `history-context.json` | the historical spine an American reader needs, in the book's framing |
| `food.json` | cuisine regions, eating customs, dish glossary (names only), street-food safety |
| `coverage-gaps.md` | topics the books cover vs our published `article-list.json`, both directions |
| `fact-wishlist.md` | fact keys the books quantify that `facts.json` lacks, with the primary source that would settle each; P1 rows feed the next facts build |
| `decision-gaps.md` | choices the books describe but never resolve — dossier material |
| `raw-notes/` | working notes per book (paraphrase, page-tagged). Not a deliverable; the JSON is |
| `state.json` | reading progress per book, so a later session can resume |

## Entry schema (all JSON files)
```json
{
  "id": "topic.slug",
  "claim": "paraphrase in our words",
  "status": "lead | context | conflict | obsolete",
  "vintage": 2015,
  "source": { "book": "dk-2015", "page": 283 },
  "verify_against": "which official source would settle it",
  "conflict_with": "facts.json key or corrections.json id, when status=conflict",
  "related_articles": ["slug", "slug"],
  "note": "free text"
}
```
`source.book` keys are defined in `sources.json`.
