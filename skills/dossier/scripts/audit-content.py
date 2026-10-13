#!/usr/bin/env python3
"""Check visible source HTML against the text in one final PDF.

Usage: audit-content.py SOURCE.html OUTPUT.pdf [--critical-json FILE] [--json]
Exit 0: PASS; 1: content differences; 2: BLOCKED or INCONCLUSIVE.
Run separately for the book, Field Sheet, and any phone edition. This checks
text conservation, not factual accuracy, reading order, or semantic agreement.
"""
import argparse
from collections import Counter, defaultdict
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unicodedata


# Source scripts never run. Use print computed styles so CSS-hidden content is
# excluded, while clipped/overflowing content remains EXPECTED and can fail.
SOURCE_JS = r'''
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL, fileURLToPath} = require('node:url');
function loadPW() {
  const roots = [process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,
    path.dirname(process.execPath) + '/node_modules'];
  try { return require('playwright'); } catch (_) {}
  for (const root of roots.filter(Boolean)) {
    try { return require(path.join(root, 'playwright')); } catch (_) {}
  }
  throw Error('Node Playwright is unavailable; install playwright and Chromium.');
}
(async () => {
  const pw = loadPW();
  const launch = {headless: true, args: ['--no-sandbox']};
  if (process.env.DOSSIER_CHROMIUM_EXECUTABLE)
    launch.executablePath = process.env.DOSSIER_CHROMIUM_EXECUTABLE;
  const browser = await pw.chromium.launch(launch);
  try {
    const context = await browser.newContext({javaScriptEnabled: false});
    const page = await context.newPage();
    await page.emulateMedia({media: 'print'});
    const loadIssues = [];
    await page.route('**/*', route => {
      const r = route.request(), url = r.url();
      if (/^https?:/.test(url)) {
        if (r.resourceType() === 'stylesheet')
          loadIssues.push('External stylesheet was not loaded: ' + url);
        return route.abort();
      }
      return route.continue();
    });
    await page.goto(pathToFileURL(path.resolve(process.argv[1])).href,
      {waitUntil: 'load', timeout: 30000});
    const cssTexts = await page.evaluate(() => [...document.querySelectorAll('style')].map(s => s.textContent));
    const localSheets = await page.evaluate(() => [...document.querySelectorAll('link[rel~="stylesheet"]')].map(s => s.href));
    for (const href of localSheets) {
      if (href.startsWith('file:')) {
        try { cssTexts.push(fs.readFileSync(fileURLToPath(href), 'utf8')); }
        catch (_) { loadIssues.push('Local stylesheet could not be read: ' + href); }
      }
    }
    const data = await page.evaluate((cssTexts) => {
      const issues = [], furniture = [], tables = [], generatedRefs = [];
      const counterElements = new Set();
      const skipTags = new Set(['SCRIPT','STYLE','TEMPLATE','NOSCRIPT','HEAD',
        'META','LINK','TITLE','DESC','DEFS','CLIPPATH','MASK','METADATA']);
      const skipSelector = '[data-content-audit="furniture"],.runninghead,' +
        '.running-head,.running-header,.runningfooter,.running-footer,' +
        '.folio,.page-number,[class*="pagedjs_margin"]';
      let hasPageCounter = false;
      function strings(css) {
        return [...css.matchAll(/"((?:\\.|[^"\\])*)"|'((?:\\.|[^'\\])*)'/g)]
          .map(m => (m[1] === undefined ? m[2] : m[1])
            .replace(/\\([0-9a-f]{1,6})\s?/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
            .replace(/\\(.)/gs, '$1')).join('');
      }
      function cssRules(rules) {
        for (const rule of rules) {
          if (rule.type === 6) { // @page, including its margin boxes
            const css = rule.cssText;
            hasPageCounter ||= /counter\(\s*page\b/.test(css);
            for (const m of css.matchAll(/content\s*:\s*([^;}]+)/g)) {
              const literal = strings(m[1]);
              if (literal.trim()) furniture.push(literal);
            }
          } else if (rule.cssRules) cssRules(rule.cssRules);
        }
      }
      for (const sheet of document.styleSheets) {
        try { cssRules(sheet.cssRules); }
        catch (_) { issues.push('A stylesheet could not be inspected.'); }
      }
      // Native Chromium drops Paged.js-only declarations from CSSOM. Read the
      // authored declarations too, then resolve their selectors in this DOM.
      for (const raw of cssTexts) {
        const css = raw.replace(/\/\*[\s\S]*?\*\//g, '');
        for (const match of css.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
          const selector = match[1].trim(), declarations = match[2];
          if (/string-set\s*:\s*[\w-]+\s+content\(\s*text\s*\)/.test(declarations)) {
            try {
              for (const el of document.querySelectorAll(selector))
                if (el.textContent.trim()) furniture.push(el.textContent.trim());
            } catch (_) { issues.push('Unresolved named-string selector: ' + selector); }
          }
          if (/content\s*:\s*target-counter\(\s*attr\(\s*href\s*\)\s*,\s*page\s*\)/.test(declarations)) {
            const base = selector.replace(/::(?:before|after)\b/g, '');
            try {
              for (const el of document.querySelectorAll(base)) {
                const href = el.getAttribute('href') || '';
                if (el.tagName !== 'A' || !href.startsWith('#')) {
                  issues.push('Generated page reference is not a local anchor: ' + href); continue;
                }
                const id = decodeURIComponent(href.slice(1));
                if (!document.getElementById(id)) {
                  issues.push('Generated page reference has no source target: ' + href); continue;
                }
                if (!counterElements.has(el)) generatedRefs.push({href: id, label: el.textContent.trim()});
                counterElements.add(el);
              }
            } catch (_) { issues.push('Unresolved page-reference selector: ' + selector); }
          }
        }
      }
      function pseudo(el, name) {
        const value = getComputedStyle(el, name).content;
        if (!value || /^(none|normal)$/.test(value)) return '';
        if (/^url\(/.test(value)) return '';
        if (/\b(counter|counters|target-counter|string)\(/.test(value)) {
          if (counterElements.has(el) && /target-counter\(/.test(value)) return '';
          issues.push('Unresolved generated body text ' + name + ' on ' + el.tagName);
          return '';
        }
        return strings(value);
      }
      function walk(node) {
        if (node.nodeType === Node.TEXT_NODE) return node.nodeValue;
        if (node.nodeType !== Node.ELEMENT_NODE) return '';
        const el = node, tag = el.tagName.toUpperCase();
        if (skipTags.has(tag)) return '';
        if (el.matches(skipSelector)) {
          if (el.textContent.trim()) furniture.push(el.textContent.trim());
          return '';
        }
        const style = getComputedStyle(el);
        if (el.hidden || style.display === 'none' || style.visibility === 'hidden' ||
            style.visibility === 'collapse' || style.contentVisibility === 'hidden' ||
            Number(style.opacity) === 0) return '';
        if (tag === 'BR') return '\n';
        const block = !['inline','contents','inline-block'].includes(style.display) ||
          ['TD','TH','TEXT','TSPAN'].includes(tag);
        const value = pseudo(el, '::before') + [...el.childNodes].map(walk).join('') +
          pseudo(el, '::after');
        if (tag === 'TR' && el.closest('thead')) tables.push(value.trim());
        return block ? '\n' + value + '\n' : value;
      }
      if (!document.body) throw Error('HTML has no body.');
      if (document.querySelector('.pagedjs_page'))
        issues.push('Use the pre-pagination source HTML, not a paginated DOM snapshot.');
      const text = walk(document.body);
      return {text, furniture_texts: furniture, table_headers: tables,
        generated_page_refs: generatedRefs,
        has_page_counter: hasPageCounter,
        has_cover: !!document.querySelector('.cover,.coverpage'),
        issues: [...new Set(issues)]};
    }, cssTexts);
    data.issues.push(...loadIssues);
    process.stdout.write(JSON.stringify(data));
  } finally { await browser.close(); }
})().catch(e => {process.stderr.write(String(e.stack || e)); process.exitCode = 2;});
'''


WORD = r"[^\W_]+(?:'[^\W_]+)*"
TOKEN_RE = re.compile(WORD + r"|[€$£%°±≤≥×÷◆◈◇●▲]|(?<=\d)[+−–—-](?=\d)", re.UNICODE)
HYPHENS = "\u00ad\u2010\u2011-"


class AuditBlocked(Exception):
    pass


def canonical(text):
    """Normalize typography, never erase letters, accents, digits, or negation."""
    return (unicodedata.normalize('NFKC', text).casefold()
            .replace('\u00ad', '').replace('\u200b', '').replace('\ufeff', '')
            .replace('\u2019', "'").replace('\u2018', "'")
            .replace('\u2212', '-').replace('\u2013', '-').replace('\u2014', '-'))


def tokens(text):
    return TOKEN_RE.findall(canonical(text))


def source_data(source):
    node = os.environ.get('CODEX_PRIMARY_RUNTIME_NODE') or shutil.which('node')
    if not node:
        return static_source_data(source, 'Node is unavailable.')
    try:
        proc = subprocess.run([node, '-e', SOURCE_JS, str(source.resolve())],
                              capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return static_source_data(source, 'Source DOM inspection failed: ' + str(exc))
    if proc.returncode:
        return static_source_data(source, 'Source DOM inspection failed: ' + proc.stderr.strip()[-1000:])
    try:
        data = json.loads(proc.stdout)
        data['parser'] = 'computed-print-dom'
        return data
    except (ValueError, TypeError) as exc:
        raise AuditBlocked('Source DOM inspection returned invalid JSON.') from exc


def static_source_data(source, browser_error):
    """An explicit, restricted fallback; arbitrary unevaluated CSS cannot pass.

    Simple HTML with no stylesheet can still be checked when Chromium is not
    installed. Stylesheets/cascade, unresolved inline visibility, SVG use, and
    CSS-generated text require computed styles and make this INCONCLUSIVE.
    """
    try:
        from lxml import html as lhtml
    except ImportError as exc:
        raise AuditBlocked(browser_error + '\nThe static fallback also needs lxml.') from exc
    try:
        root = lhtml.document_fromstring(source.read_text(encoding='utf-8'))
    except Exception as exc:
        raise AuditBlocked('HTML could not be parsed: ' + str(exc)) from exc
    issues, furniture, headers = [], [], []
    if root.xpath('//style | //link[contains(translate(@rel,"STYLESHEET","stylesheet"),"stylesheet")]'):
        issues.append('Computed print styles unavailable; the static fallback cannot validate stylesheets. ' + browser_error)
    skip_tags = {'script','style','template','noscript','head','meta','link','title',
                 'desc','defs','clippath','mask','metadata'}
    skip_classes = {'runninghead','running-head','running-header','runningfooter',
                    'running-footer','folio','page-number'}
    blocks = {'html','body','main','article','section','div','p','h1','h2','h3','h4',
              'h5','h6','ul','ol','li','table','thead','tbody','tfoot','tr','td','th',
              'figure','figcaption','blockquote','text','tspan','header','footer'}
    def walk(el):
        if not isinstance(el.tag, str): return ''
        tag = el.tag.rsplit('}', 1)[-1].lower()
        if tag in skip_tags: return ''
        classes = set(el.get('class', '').split())
        if el.get('data-content-audit') == 'furniture' or classes.intersection(skip_classes):
            furniture.append(''.join(el.itertext()).strip())
            return ''
        style = el.get('style', '').lower()
        if 'hidden' in el.attrib or re.search(r'(?:^|;)\s*display\s*:\s*none\b', style):
            return ''
        if re.search(r'(?:^|;)\s*(?:opacity\s*:\s*0(?:\.0+)?\s*(?:;|$)|visibility\s*:\s*(?:hidden|collapse)\b)', style):
            if any('visibility' in c.get('style','') for c in el.iterdescendants()):
                issues.append('Nested visibility overrides require computed print styles.')
            return ''
        if re.search(r'(?:display|visibility|opacity)\s*:[^;]*var\(', style):
            issues.append('Inline visibility depends on an unevaluated CSS variable.')
        if tag == 'use': issues.append('SVG use references require computed source inspection.')
        if tag == 'br': return '\n'
        value = el.text or ''
        for child in el:
            value += walk(child) + (child.tail or '')
        if tag == 'tr' and any(str(a.tag).lower() == 'thead' for a in el.iterancestors()):
            headers.append(value.strip())
        return '\n' + value + '\n' if tag in blocks else value
    bodies = root.xpath('//body')
    if not bodies: raise AuditBlocked('HTML has no body.')
    text = walk(bodies[0])
    return {'text': text, 'furniture_texts': furniture, 'table_headers': headers,
            'generated_page_refs': [],
            'has_page_counter': False,
            'has_cover': bool(root.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," cover ") or contains(concat(" ",normalize-space(@class)," ")," coverpage ")]')),
            'issues': list(dict.fromkeys(issues)), 'parser': 'restricted-static-html',
            'parser_note': 'Browser unavailable; only a stylesheet-free source may pass this fallback.'}


def _untrack(text, vocabulary):
    """Repair a tracked heading only when the actual letters form a source word."""
    parts = re.split(r'(\s{2,})', text)
    changed = False
    for i in range(0, len(parts), 2):
        chars = parts[i].split()
        if len(chars) >= 3 and all(len(c) == 1 and c.isalpha() for c in chars):
            joined = ''.join(chars)
            if canonical(joined) in vocabulary:
                parts[i] = joined
                changed = True
    return ''.join(parts), changed


def _join_wraps(text, vocabulary):
    # Only a line-end hyphen plus a real following fragment can be joined.
    # No dictionary completion: "ared" can never become "compared" here.
    pat = re.compile(r"([^\W_]+)[\u00ad\u2010\u2011-][ \t]*\n+[ \t]*([^\W_]+)", re.UNICODE)
    def join(match):
        candidate = match[1] + match[2]
        return candidate if canonical(candidate) in vocabulary else match[0]
    return pat.sub(join, text)


def generated_page_refs(doc, refs):
    """Resolve only declared local TOC folios; never excuse arbitrary numbers.

    The target must exist in the PDF's named destinations, and its label plus
    physical page number must be printed within a matching clickable region.
    Custom/reset page numbering needs a separate adapter and cannot pass here.
    """
    verified, issues, used = [], [], set()
    if not refs: return verified, issues
    try:
        names = doc.resolve_names()
    except (AttributeError, RuntimeError, ValueError):
        return [], ['Named PDF destinations could not be resolved for generated TOC folios.']
    for ref in refs:
        target = names.get(ref['href']) or names.get('/' + ref['href'])
        if not target or not isinstance(target.get('page'), int) or target['page'] < 0:
            issues.append('No PDF named destination for generated page reference #' + ref['href'])
            continue
        folio = str(target['page'] + 1)
        label = tokens(ref['label'])
        if not label:
            issues.append('Generated page reference has an empty label: #' + ref['href'])
            continue
        found = None
        for page_number, page in enumerate(doc, 1):
            for index, link in enumerate(page.get_links()):
                linked_page = link.get('page')
                # MuPDF reports a /Fit named-link destination as a one-based
                # numeric string, unlike its zero-based integer GoTo form.
                if link.get('kind') == 4 and isinstance(linked_page, str) and linked_page.isdigit():
                    linked_page = int(linked_page) - 1
                if (page_number, index) in used or linked_page != target['page']:
                    continue
                # External links must never supply evidence for a local folio.
                if link.get('uri'): continue
                rect = link['from'] + (-1, -1, 1, 1)
                region = page.get_textbox(rect)
                region = '\n'.join(_untrack(line, set(label))[0] for line in region.splitlines())
                observed = tokens(region)
                if (occurrence_count(observed, label) >= 1 and
                    observed.count(folio) >= label.count(folio) + 1):
                    found = (page_number, index)
                    verified.append({**ref, 'folio': folio, 'page': page_number})
                    used.add(found)
                    break
            if found: break
        if not found:
            issues.append('Generated TOC folio not verified in its local link rectangle: #' + ref['href'])
    return verified, issues


def pdf_data(pdf, source):
    try:
        import fitz
    except ImportError as exc:
        raise AuditBlocked('PyMuPDF is required: install pymupdf.') from exc
    vocabulary = set(tokens(source['text']))
    pages, repairs, ignored = [], [], []
    try:
        doc = fitz.open(pdf)
    except Exception as exc:
        raise AuditBlocked('PDF could not be opened: ' + str(exc)) from exc
    with doc:
        if not len(doc) or doc.needs_pass:
            raise AuditBlocked('PDF has no pages or requires a password.')
        refs, ref_issues = generated_page_refs(doc, source.get('generated_page_refs', []))
        for number, page in enumerate(doc, 1):
            lines = []
            for block in page.get_text('dict')['blocks']:
                for line in block.get('lines', []):
                    spans = line['spans']
                    txt = ''.join(s['text'] for s in spans)
                    # Some PDF producers keep the cap and first line in one
                    # line, adding a synthetic space between the font runs.
                    if len(spans) >= 2:
                        first = spans[0]
                        rest = ''.join(s['text'] for s in spans[1:])
                        stem = re.match(r'\s*([^\W_]+)', rest, re.UNICODE)
                        small = max(s['size'] for s in spans[1:])
                        if (len(first['text'].strip()) == 1 and
                            first['text'].strip().isalpha() and first['size'] >= small * 1.6 and
                            stem and canonical(first['text'].strip() + stem[1]) in vocabulary):
                            txt = first['text'].strip() + rest.lstrip()
                            repairs.append({'page': number, 'kind': 'geometric drop cap'})
                    txt, changed = _untrack(txt, vocabulary)
                    if changed: repairs.append({'page': number, 'kind': 'tracked lettering'})
                    if txt.strip():
                        lines.append({'text': txt, 'bbox': list(line['bbox']),
                                      'size': max(s['size'] for s in spans)})
            # A floated drop cap can be extracted before its heading or after
            # its third line. Reattach the EXISTING glyph using its geometry.
            sizes = sorted(l['size'] for l in lines if len(l['text']) > 12)
            normal = sizes[len(sizes)//2] if sizes else 0
            for cap in list(lines):
                if not (normal and cap['size'] >= normal * 1.6 and
                        len(cap['text'].strip()) == 1 and cap['text'].strip().isalpha()):
                    continue
                x0, y0, x1, y1 = cap['bbox']
                candidates = sorted((l for l in lines if l is not cap and l['size'] < cap['size']
                    and l['bbox'][0] >= x1 - 3 and y0 - 2 <= l['bbox'][1] <= y1),
                    key=lambda l: (l['bbox'][1], l['bbox'][0]))
                if not candidates: continue
                target = candidates[0]
                match = re.match(r'\s*([^\W_]+)', target['text'], re.UNICODE)
                if match and canonical(cap['text'].strip() + match[1]) in vocabulary:
                    target['text'] = cap['text'].strip() + target['text'].lstrip()
                    lines.remove(cap)
                    repairs.append({'page': number, 'kind': 'geometric drop cap'})
            lines.sort(key=lambda l: (round(l['bbox'][1], 1), l['bbox'][0]))
            pages.append({'number': number, 'height': page.rect.height, 'lines': lines})

    # Only edge text can be furniture. Preserve all cover text. Repeated edge
    # strings and @page literals are explainable exclusions, never body tokens.
    edge_occ = defaultdict(set)
    for page in pages:
        for line in page['lines']:
            y0, y1 = line['bbox'][1], line['bbox'][3]
            if y1 < page['height'] * .07 or y0 > page['height'] * .93:
                edge_occ[' '.join(tokens(line['text']))].add(page['number'])
    furniture = {' '.join(tokens(s)) for s in source['furniture_texts'] if tokens(s)}
    headers = Counter(' '.join(tokens(s)) for s in source['table_headers'] if tokens(s))
    seen_headers = Counter()
    out_pages = []
    for page in pages:
        out = []
        for line in page['lines']:
            key = ' '.join(tokens(line['text']))
            y0, y1 = line['bbox'][1], line['bbox'][3]
            edge = y1 < page['height'] * .07 or y0 > page['height'] * .93
            cover = page['number'] == 1 and source['has_cover']
            reason = None
            if edge and not cover:
                if key in furniture or (key and len(edge_occ[key]) >= 2):
                    reason = 'running furniture at page edge'
                elif source['has_page_counter'] and key == str(page['number']):
                    reason = 'generated page counter at page edge'
            if key in headers:
                seen_headers[key] += 1
                if seen_headers[key] > headers[key] and y0 < page['height'] * .25:
                    reason = 'repeated table header near page top'
            if reason:
                ignored.append({'page': page['number'], 'reason': reason, 'text': line['text']})
            else:
                out.append(line['text'])
        out_pages.append({'page': page['number'], 'text': '\n'.join(out)})
    # Joining across a page seam happens after running furniture was removed.
    text = _join_wraps('\n'.join(p['text'] for p in out_pages), vocabulary)
    return {'text': text, 'pages': out_pages, 'repairs': repairs, 'ignored': ignored,
            'page_count': len(pages), 'generated_page_refs': refs, 'issues': ref_issues}


def critical_specs(path):
    if path is None: return []
    try:
        specs = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise AuditBlocked('Critical JSON could not be read: ' + str(exc)) from exc
    if not isinstance(specs, list) or not specs:
        raise AuditBlocked('Critical JSON must be a non-empty list of {id,text,min_occurrences}.')
    ids = set()
    for spec in specs:
        if not isinstance(spec, dict) or not isinstance(spec.get('id'), str) or not spec['id'].strip():
            raise AuditBlocked('Every critical snippet needs a non-empty string id.')
        if spec['id'] in ids:
            raise AuditBlocked('Duplicate critical snippet id: ' + spec['id'])
        ids.add(spec['id'])
        if not isinstance(spec.get('text'), str) or not tokens(spec['text']):
            raise AuditBlocked('Critical snippet text must contain words or numbers: ' + spec['id'])
        minimum = spec.get('min_occurrences', 1)
        if isinstance(minimum, bool) or not isinstance(minimum, int) or minimum < 1:
            raise AuditBlocked('min_occurrences must be an integer >= 1: ' + spec['id'])
        spec['min_occurrences'] = minimum
    return specs


def occurrence_count(haystack, needle):
    n = len(needle)
    return sum(haystack[i:i+n] == needle for i in range(len(haystack)-n+1))


def audit(source_path, pdf_path, critical_path=None):
    report = {'status': 'BLOCKED', 'source': str(source_path), 'pdf': str(pdf_path),
              'scope': 'text conservation only; not factual or semantic validation',
              'issues': [], 'missing': [], 'unexpected': [], 'critical': []}
    try:
        for path in [source_path, pdf_path]:
            if not path.is_file(): raise AuditBlocked('Missing file: ' + str(path))
        specs = critical_specs(critical_path)
        source = source_data(source_path)
        expected = tokens(source['text'])
        if not expected: raise AuditBlocked('No visible source text was parsed; cannot pass an empty comparison.')
        rendered = pdf_data(pdf_path, source)
        actual = tokens(rendered['text'])
        if not actual: raise AuditBlocked('No PDF text was extracted; scan/outlined text needs review, not PASS.')
        if '\ufffd' in rendered['text'] or '\ufffd' in source['text']:
            report['issues'].append('Replacement glyph U+FFFD prevents a reliable text comparison.')
        report['issues'].extend(source['issues'])
        report['issues'].extend(rendered['issues'])
        generated = [ref['folio'] for ref in rendered['generated_page_refs']]
        expected_counts, actual_counts = Counter(expected + generated), Counter(actual)
        for label, delta in [('missing', expected_counts - actual_counts),
                             ('unexpected', actual_counts - expected_counts)]:
            report[label] = [{'token': t, 'count': n} for t, n in sorted(delta.items())]
        for spec in specs:
            needle = tokens(spec['text'])
            source_count = occurrence_count(expected, needle)
            pdf_count = occurrence_count(actual, needle)
            report['critical'].append({**spec, 'source_occurrences': source_count,
                'pdf_occurrences': pdf_count,
                'status': 'PASS' if min(source_count, pdf_count) >= spec['min_occurrences'] else 'FAIL'})
        missing_set = {item['token'] for item in report['missing']}
        unexpected_set = {item['token'] for item in report['unexpected']}
        report['source_examples'] = [line.strip()[:240] for line in source['text'].splitlines()
                                    if missing_set.intersection(tokens(line))][:12]
        report['pdf_examples'] = [{'page': p['page'], 'text': line.strip()[:240]}
            for p in rendered['pages'] for line in p['text'].splitlines()
            if unexpected_set.intersection(tokens(line))][:12]
        report.update(source_tokens=len(expected), expected_tokens=len(expected) + len(generated), pdf_tokens=len(actual),
                      pages=rendered['page_count'], normalizations=rendered['repairs'],
                      excluded_furniture=rendered['ignored'], source_parser=source['parser'],
                      generated_page_refs=rendered['generated_page_refs'])
        if source.get('parser_note'): report['parser_note'] = source['parser_note']
        changed = report['missing'] or report['unexpected'] or any(
            item['status'] != 'PASS' for item in report['critical'])
        report['status'] = 'INCONCLUSIVE' if report['issues'] else ('FAIL' if changed else 'PASS')
    except AuditBlocked as exc:
        report['issues'].append(str(exc))
    except Exception as exc:
        # A parser error must never turn into a silent successful release.
        report['issues'].append(type(exc).__name__ + ': ' + str(exc))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--critical-json', type=Path)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    report = audit(args.source, args.pdf, args.critical_json)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print('CONTENT ' + report['status'] + ' · ' + str(args.pdf))
        if 'source_tokens' in report:
            print(f"  source {report['source_tokens']} tokens + {len(report['generated_page_refs'])} verified navigation tokens; PDF {report['pdf_tokens']} tokens; {report['pages']} pages")
            print('  source parser: ' + report['source_parser'])
        for issue in report['issues']: print('  review: ' + issue)
        for label in ['missing', 'unexpected']:
            for item in report[label][:25]: print(f"  {label}: {item['token']!r} ×{item['count']}")
        for item in report['critical']:
            print(f"  critical {item['id']}: {item['status']} (source {item['source_occurrences']}, PDF {item['pdf_occurrences']}, minimum {item['min_occurrences']})")
        for item in report.get('pdf_examples', [])[:5]:
            print(f"  PDF p.{item['page']}: {item['text']}")
        print('  A PASS does not validate facts, semantic consistency, clipping, or reading order; inspect the rendered pages.')
    return 0 if report['status'] == 'PASS' else (1 if report['status'] == 'FAIL' else 2)


if __name__ == '__main__':
    sys.exit(main())
