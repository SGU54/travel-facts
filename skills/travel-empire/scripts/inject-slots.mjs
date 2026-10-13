/**
 * inject-slots.mjs — one-time affiliate-slot pass over existing articles.
 *
 * Follows the writing-step rules (3-writing.md) exactly, applied retroactively:
 *   · slots by INTENT: a role is only allowed where the category's content
 *     genuinely matches it (stay content → hotels; sights/tickets → tours;
 *     day-trips → rail; planning/when-to-go → flights; safety/packing →
 *     insurance; food/etiquette/piazzas → NOTHING).
 *   · the anchor is REAL EXISTING PROSE — we wrap a natural phrase already in
 *     the article ("where to stay", "book tickets online", "travel insurance"),
 *     never inject new copy, never "click here".
 *   · max 2 slots per article, max 1 per role; first natural match wins.
 *   · DOM, never regex-on-HTML (hard rule 3): cheerio text-node surgery. Never
 *     inside <a>, headings, or .fact spans.
 *   · neighborhoods carry data-item (e.g. trastevere) — the per-article AREA
 *     override; everything else stays bare (defaults to the destination).
 *
 * Usage: node inject-slots.mjs <export.json> <out.json> <report.md>
 */
import { readFileSync, writeFileSync } from 'node:fs';
import * as cheerio from 'cheerio';

const [, , inPath, outPath, reportPath] = process.argv;
const arts = JSON.parse(readFileSync(inPath, 'utf8'));

// ── category → allowed roles (order = priority when both could match) ────────
const CAT_ROLES = {
  'best-areas-to-stay': ['hotels'],
  'hotels-and-boutique': ['hotels'],
  'budget-and-family': ['hotels'],
  'trastevere': ['hotels'],
  'monti-and-esquilino': ['hotels'],
  'testaccio-and-ostiense': ['hotels'],
  'centro-storico': ['hotels'],
  'ghetto-and-campo': ['hotels'],
  'ancient-rome': ['tours'],
  'vatican': ['tours'],
  'museums-and-galleries': ['tours'],
  'tickets-and-passes': ['tours'],
  'piazzas-and-fountains': [],            // free sights — nothing bookable
  'rome-in-1-3-days': ['tours', 'hotels'],
  'rome-in-4-plus-days': ['tours', 'hotels'],
  'day-trips': ['rail'],
  'when-to-go': ['flights'],
  'arrival-and-airports': [],             // getting FROM the airport — flight already booked
  'safety-and-scams': ['insurance'],
  'packing-and-connectivity': ['insurance'],
  // everything else: no slots
};

// neighborhood categories → data-item override for hotels
const AREA_ITEM = {
  'trastevere': 'trastevere',
  'monti-and-esquilino': 'monti',
  'testaccio-and-ostiense': 'testaccio',
  'centro-storico': 'centro storico rome',
  'ghetto-and-campo': 'jewish ghetto rome',
};

// ── role → anchor-phrase patterns (matched against PLAIN TEXT of <p> nodes) ──
// Ordered: the first pattern that matches anywhere in the article wins for that
// role. Patterns capture a SHORT natural span (3–40 chars) to wrap.
const PHRASES = {
  hotels: [
    /where to stay(?: in [A-Z][\w'’ ]+)?/i,
    /neighborhoods? to stay(?: in)?/i,
    /place to stay/i,
    /stay(?:ing)? (?:in|near) [A-Z][\w'’ ]+/,
    /bas(?:e|ing) yourself(?: near [A-Z][\w'’ ]+)?/i,
    /book(?:ing)? (?:your |a )?(?:hotel|room|accommodation)s?(?: early| ahead| in advance)?/i,
    /(?:hotels?|guesthouses?|B&Bs?) (?:in|near|around) [A-Z][\w'’ ]+/,
    /hotel or apartment/i,
    /the specific hotel/i,
    /accommodation/i,
    /book early/i,
  ],
  tours: [
    /book (?:your )?tickets? (?:online|in advance|ahead)/i,
    /(?:skip[- ]the[- ]line|timed[- ]entry) tickets?/i,
    /book(?:ing)? (?:in advance|ahead|online)/i,
    /book everything ahead/i,
    /guided tours?/i,
    /reserve (?:your )?(?:slot|entry|tickets?)/i,
    /tickets? sell out/i,
    /timed entr(?:y|ies)/i,
  ],
  rail: [
    /(?:regional |high-speed |direct )?train tickets?/i,
    /high-speed trains?/i,
    /regional train/i,
    /take the (?:regional )?train/i,
    /(?:the |a )?(?:direct |regional )?train from [A-Z][\w'’ ]+/,
    /buy return tickets/i,
    /book ahead/i,
    /trains? (?:run|leave|depart)/i,
    /by (?:regional )?train/i,
  ],
  flights: [
    /book (?:your )?flights?(?: early| ahead| in advance)?/i,
    /flights? from the US/i,
    /nonstop flights?/i,
    /airfares?/i,
  ],
  insurance: [
    /travel insurance/i,
  ],
};

const MAX_SLOTS_PER_ARTICLE = 2;

// text-node surgery: wrap the first regex match found in a valid text node.
function injectRole($, role, item) {
  const patterns = PHRASES[role] || [];
  for (const re of patterns) {
    let done = false;
    $('p').each((_, p) => {
      if (done) return;
      const $p = $(p);
      // walk direct + nested text nodes, skipping forbidden parents
      const walk = (node) => {
        if (done || !node) return;
        for (const child of node.childNodes ?? []) {
          if (done) return;
          if (child.type === 'text') {
            const parentTag = child.parent?.name;
            const parentClass = child.parent?.attribs?.class || '';
            if (parentTag === 'a' || /fact|aff/.test(parentClass)) continue;
            const text = child.data || '';
            const m = text.match(re);
            if (m && m[0].length >= 3 && m[0].length <= 60) {
              const i = m.index;
              // NEGATION GUARD: "No high-speed train needed", "without booking" —
              // wrapping a negated phrase in a booking link is a lie. Skip if the
              // preceding words negate the match.
              const before30 = text.slice(Math.max(0, i - 30), i);
              if (/\b(?:no|not|without|never|isn['’]t|aren['’]t|don['’]t|doesn['’]t)\s*(?:\w+\s+){0,2}$/i.test(before30)) continue;
              const before = text.slice(0, i);
              const hit = m[0];
              const after = text.slice(i + hit.length);
              const itemAttr = item ? ` data-item="${item}"` : '';
              const span = `<span class="aff" data-aff="${role}"${itemAttr}>${hit}</span>`;
              $(child).replaceWith(before + span + after);
              done = true;
              return;
            }
          } else if (child.type === 'tag' && !['a', 'h1', 'h2', 'h3', 'h4', 'script', 'style'].includes(child.name)) {
            walk(child);
          }
        }
      };
      walk(p);
    });
    if (done) return re.source;
  }
  return null;
}

const report = [];
let touched = 0, totalSlots = 0;
const roleCount = {};

for (const a of arts) {
  const roles = CAT_ROLES[a.category_slug] ?? [];
  if (!roles.length || !a.content) continue;
  const $ = cheerio.load(a.content, undefined, false);
  const placed = [];
  for (const role of roles) {
    if (placed.length >= MAX_SLOTS_PER_ARTICLE) break;
    const item = role === 'hotels' ? AREA_ITEM[a.category_slug] : undefined;
    const pattern = injectRole($, role, item);
    if (pattern) {
      placed.push({ role, item: item ?? '(destination)', pattern });
      roleCount[role] = (roleCount[role] ?? 0) + 1;
      totalSlots++;
    }
  }
  if (placed.length) {
    a.content = $.html();
    touched++;
    report.push(`## ${a.slug}  [${a.category_slug}]`);
    for (const p of placed) {
      // show the wrapped phrase in context
      const m = a.content.match(new RegExp(`<span class="aff" data-aff="${p.role}"[^>]*>([^<]+)</span>`));
      report.push(`- **${p.role}** → “${m ? m[1] : '?'}”  (item: ${p.item})`);
    }
    report.push('');
  }
}

writeFileSync(outPath, JSON.stringify(arts, null, 2));
writeFileSync(
  reportPath,
  `# Slot-injection report — ${new Date().toISOString().slice(0, 10)}\n\n` +
    `Articles touched: ${touched} of ${arts.length} · slots placed: ${totalSlots}\n` +
    `By role: ${Object.entries(roleCount).map(([r, n]) => `${r} ${n}`).join(' · ')}\n\n` +
    report.join('\n')
);
console.log(`touched ${touched}/${arts.length} articles, ${totalSlots} slots`);
console.log('by role:', roleCount);
