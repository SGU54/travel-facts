#!/usr/bin/env python3
"""Local DOM/PDF adapter. JSON on stdin/stdout; never fetch URLs or execute HTML."""
import html as escapes
import json
import re
import sys
from urllib.parse import urljoin, urlparse


def dom(source):
    try:
        from lxml import html
    except ImportError as exc:
        raise ValueError("lxml is required; install scripts/requirements.txt with the selected Python") from exc
    if not isinstance(source, str) or not source.strip():
        raise ValueError("HTML must be a nonempty string")
    return html.fragment_fromstring(source, create_parent="div")


def classes(node):
    return set((node.get("class") or "").split())


def text(node):
    return re.sub(r"\s+", " ", node.text_content()).strip()


def inspect(source):
    root = dom(source)
    result = {"text": text(root), "elements": [], "links": [], "images": [], "spans": [], "headings": [], "comments": []}
    for n in root.iterdescendants():
        if not isinstance(n.tag, str):
            if n.text:
                result["comments"].append(n.text)
            continue
        tag = n.tag.lower()
        attrs = dict(n.attrib)
        ancestors = [x.tag for x in n.iterancestors() if isinstance(x.tag, str)]
        result["elements"].append({"tag": tag, "attrs": attrs})
        if tag == "a":
            result["links"].append({"attrs": attrs, "text": text(n), "ancestors": ancestors})
        if tag == "img":
            result["images"].append({"attrs": attrs})
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            result["headings"].append({"level": int(tag[1]), "text": text(n)})
        if classes(n) & {"fact", "aff", "guide"}:
            result["spans"].append({"tag": tag, "attrs": attrs, "text": text(n), "nested": any(classes(x) & {"fact", "aff", "guide"} for x in n.iterancestors())})
    return result


def sections(source, base_url=None):
    """Collect whole H2 sections in document order, including every paragraph/list."""
    root = dom(source)
    out = []
    current = None
    blocks = {"p", "div", "section", "article", "h3", "h4", "h5", "h6", "li", "ul", "ol", "table", "tr", "blockquote", "br"}

    def append(value):
        if current is not None and value:
            current["parts"].append(value)

    def walk(n):
        nonlocal current
        if not isinstance(n.tag, str):
            return
        tag = n.tag.lower()
        if tag in {"script", "style", "template"}:
            return
        if tag in {"h1", "h2"}:
            current = {"heading": text(n), "level": int(tag[1]), "parts": [], "unsupported": set()}
            out.append(current)
            return
        if current is not None and tag in {"table", "dl"}:
            current["unsupported"].add(tag)
        if current is not None and ((tag == "ol" and (n.get("start") or n.get("reversed") is not None)) or (tag == "li" and n.get("value"))):
            current["unsupported"].add("custom list numbering")
        if tag in blocks:
            append("\n")
        if tag == "li":
            parent = n.getparent()
            if parent is not None and parent.tag == "ol":
                siblings = [x for x in parent if x.tag == "li"]
                append(f"{siblings.index(n) + 1}. ")
            else:
                append("• ")
        append(n.text)
        for child in n:
            walk(child)
            append(child.tail)
        if tag == "a" and n.get("href"):
            href = urljoin(base_url, n.get("href")) if base_url else n.get("href")
            if urlparse(href).scheme in {"http", "https"} and href != text(n):
                append(f" ({href})")
        if tag in blocks:
            append("\n")

    walk(root)
    return [{"heading": x["heading"], "body": "\n".join(line for line in (re.sub(r"[\t \r\f\v]+", " ", line).strip() for line in "".join(x["parts"]).split("\n")) if line), "unsupported": sorted(x["unsupported"])} for x in out if x["level"] == 2]


def inject(request):
    from lxml import etree, html
    root = dom(request["html"])
    before = root.text_content()
    protected = lambda: [etree.tostring(n, with_tail=False) for n in root.iterdescendants() if isinstance(n.tag, str) and classes(n) & {"fact", "guide"}]
    protected_before = protected()
    existing = [n for n in root.iterdescendants() if isinstance(n.tag, str) and "aff" in classes(n)]
    occupied = {n.get("data-aff") for n in existing}
    count = len(existing)
    placed = []
    forbidden = {"a", "h1", "h2", "h3", "h4", "h5", "h6", "script", "style", "code", "pre", "button", "textarea"}

    def permitted(context):
        chain = [context, *context.iterancestors()]
        return not any((isinstance(x.tag, str) and x.tag.lower() in forbidden) or classes(x) & {"fact", "aff", "guide"} for x in chain)

    def slots(p):
        for n in p.iter():
            if isinstance(n.tag, str) and n.text and permitted(n):
                yield n, "text", n.text
            if n is not p and n.tail and n.getparent() is not None and permitted(n.getparent()):
                yield n, "tail", n.tail

    for rule in request["rules"]:
        if count >= request["max_slots"]:
            break
        role = rule["role"]
        if role in occupied:
            continue
        done = False
        for phrase in rule["phrases"]:
            for p in root.iter("p"):
                if not permitted(p):
                    continue
                for holder, field, value in list(slots(p)):
                    hit = re.search(re.escape(phrase), value, flags=re.IGNORECASE)
                    if not hit:
                        continue
                    prefix = value[max(0, hit.start() - 50):hit.start()]
                    if re.search(r"\b(?:no|not|without|never|don't|doesn't|isn't|aren't|sans|pas|sin)\s*(?:\w+\s+){0,3}$", prefix, flags=re.IGNORECASE):
                        continue
                    span = etree.Element("span", {"class": "aff", "data-aff": role})
                    if rule.get("item"):
                        span.set("data-item", rule["item"])
                    span.text = value[hit.start():hit.end()]
                    span.tail = value[hit.end():]
                    setattr(holder, field, value[:hit.start()])
                    if field == "text":
                        holder.insert(0, span)
                    else:
                        holder.addnext(span)
                    placed.append({"role": role, "phrase": span.text, "item": rule.get("item")})
                    occupied.add(role)
                    count += 1
                    done = True
                    break
                if done:
                    break
            if done:
                break
    if root.text_content() != before or protected() != protected_before:
        raise ValueError("DOM transformation changed text or protected fact/guide spans")
    rendered = escapes.escape(root.text or "", quote=False) + "".join(html.tostring(n, encoding="unicode") for n in root)
    return {"html": rendered if placed else request["html"], "placed": placed, "existing_slots": len(existing), "total_slots": count}


def pdf(path, margins=None):
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise ValueError("pypdf is required; install scripts/requirements.txt with the selected Python") from exc
    reader = PdfReader(path, strict=True)
    if reader.is_encrypted:
        raise ValueError("Unexpected encrypted PDF")
    all_text, body_text = [], []
    for page in reader.pages:
        kept = []
        top = float((margins or {}).get("top", 0))
        bottom = float((margins or {}).get("bottom", 0))
        height = float(page.mediabox.height)

        def visitor(value, cm, tm, _font, _size):
            # Transform text origin to page coordinates. Remove only the declared
            # margin regions, never numeric strings (body copy may contain them).
            y = tm[4] * cm[1] + tm[5] * cm[3] + cm[5]
            if bottom - 0.1 <= y <= height - top + 0.1:
                kept.append(value)

        all_text.append(page.extract_text(visitor_text=visitor) or "")
        body_text.append("".join(kept))
    return {"pages": len(reader.pages), "text": "\n".join(all_text), "bodyText": "\n".join(body_text)}


def main():
    if "--help" in sys.argv:
        print("Internal adapter: JSON stdin {mode: inspect|sections|inject|pdf, ...}. Never accesses the network.")
        return
    request = json.load(sys.stdin)
    mode = request.get("mode")
    if mode == "inspect":
        result = inspect(request["html"])
    elif mode == "sections":
        result = sections(request["html"], request.get("base_url"))
    elif mode == "inject":
        result = inject(request)
    elif mode == "pdf":
        result = pdf(request["path"], request.get("margins"))
    else:
        raise ValueError("Unknown adapter mode")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"HTML/PDF check failed: {exc}", file=sys.stderr)
        sys.exit(1)
