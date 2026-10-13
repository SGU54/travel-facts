# design2.py — ALL CSS lives here (bug log #1). Brand: assets/brands/romeforamericans.json.
import base64, os
BUILD = os.path.dirname(os.path.abspath(__file__))

def _font(fn):
    with open(f"{BUILD}/fonts/{fn}", "rb") as fh:
        return base64.b64encode(fh.read()).decode()

FACES = "".join(
    f"@font-face{{font-family:'{fam}';font-style:{sty};font-weight:{wt};"
    f"src:url(data:font/ttf;base64,{_font(fn)}) format('truetype')}}"
    for fam, sty, wt, fn in [
        ("IM Fell English", "normal", "400", "IMFellEnglish-Regular.ttf"),
        ("IM Fell English", "italic", "400", "IMFellEnglish-Italic.ttf"),
        ("Sorts Mill Goudy", "normal", "400", "SortsMillGoudy-Regular.ttf"),
        ("Sorts Mill Goudy", "italic", "400", "SortsMillGoudy-Italic.ttf"),
        ("IBM Plex Mono", "normal", "400", "IBMPlexMono-Regular.ttf"),
        ("IBM Plex Mono", "normal", "500", "IBMPlexMono-Medium.ttf"),
    ])

CSS = FACES + """
:root{
  --paper:#F6EEDB; --ink:#2B241A; --accent:#8A3324; --gilt:#C9A84C;
  --muted:#7A6B4E; --soft:#9C8C6B; --line:#DED0AF; --line-soft:#E7DCC0;
  --zone:#E9DEC2; --stone:#E3D6B4; --deep:#6E241D; --water:#CFD8CE;
  --display:'IM Fell English',serif; --body:'Sorts Mill Goudy',Georgia,serif;
  --mono:'IBM Plex Mono',monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#8a8172;font-family:var(--body);color:var(--ink);
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ── page ── */
.page{width:8.5in;height:11in;padding:0.85in;position:relative;background:var(--paper);
  color:var(--ink);overflow:hidden;margin:0 auto;page-break-after:always}
.page.bleed{padding:0}
.folio{position:absolute;bottom:0.42in;left:0.85in;right:0.85in;display:flex;
  justify-content:space-between;font-family:var(--mono);font-size:8px;letter-spacing:.18em;
  text-transform:uppercase;color:var(--soft)}
.folio b{color:var(--muted);font-weight:500}

/* ── type scale (measured, shipped) ── */
.eyebrow{font-family:var(--mono);font-size:8px;letter-spacing:.28em;text-transform:uppercase;
  color:var(--accent);margin-bottom:19px}
.eyebrow span{color:var(--soft)}
h1.t{font-family:var(--display);font-weight:400;font-size:44px;line-height:1.06;
  margin-bottom:19px;text-wrap:balance}
h2.s{font-family:var(--display);font-weight:400;font-size:21px;line-height:1.2;
  margin:26px 0 10px;color:var(--ink)}
.standfirst{font-family:var(--body);font-style:italic;font-size:18px;line-height:1.45;
  color:var(--muted);margin-bottom:22px;padding-bottom:20px;border-bottom:1px solid var(--line-soft)}
p.b{font-size:13.4px;line-height:1.68;margin-bottom:12px;text-align:justify;
  hyphens:auto;-webkit-hyphens:auto}
p.b + p.b{text-indent:0}
.cap1:first-letter{font-family:var(--display);font-size:56px;line-height:.82;float:left;
  padding:6px 8px 0 0;color:var(--accent)}
.pull.side{float:right;width:2.15in;margin:6px 0 14px 22px;padding:14px 0 12px;
  border-top:2px solid var(--accent);border-bottom:1px solid var(--line);
  font-family:var(--display);font-size:17.5px;line-height:1.46;color:var(--deep)}
.aside{font-size:11.3px;line-height:1.62;color:var(--muted);background:var(--zone);
  border:1px solid var(--line);border-left:3px solid var(--gilt);padding:12px 14px;margin:20px 0}
.aside b{color:var(--ink);font-weight:400;font-family:var(--mono);font-size:9.5px;
  letter-spacing:.14em;text-transform:uppercase}
.note{font-size:11px;line-height:1.66;color:var(--muted);margin-top:14px;
  padding-top:10px;border-top:1px solid var(--line-soft)}

/* ── provenance marks ── */
.mk{font-family:var(--mono);font-size:9px;letter-spacing:.06em;white-space:nowrap}
.mk.est{color:var(--muted)} .mk.off{color:var(--accent)}
.mk.sur{color:var(--gilt)}  .mk.vol{color:var(--deep)}

/* ── ledger ── */
.led-h{font-family:var(--mono);font-size:8px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--soft);display:flex;justify-content:space-between;align-items:baseline;
  margin-top:6px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.led-h .cols{color:var(--muted);letter-spacing:.12em}
table.led{width:100%;border-collapse:collapse;font-size:12px;line-height:1.5}
.led td{padding:7px 0;border-bottom:1px solid var(--line-soft);vertical-align:top}
.led td.num{text-align:right;font-family:var(--mono);font-size:10.5px;color:var(--deep);
  white-space:nowrap;padding-left:14px}
.led td .sub{display:block;font-size:10.8px;color:var(--muted);line-height:1.45}

/* ── decision page ── */
.dq{font-family:var(--display);font-size:30px;line-height:1.12;margin-bottom:14px}
.dnum{position:absolute;top:0.85in;right:0.85in;text-align:right}
.dnum .n{font-family:var(--display);font-size:40px;color:var(--accent);line-height:1}
.dnum .c{font-family:var(--mono);font-size:8px;letter-spacing:.24em;text-transform:uppercase;
  color:var(--soft);display:block;margin-top:4px}
.verdict{margin-top:16px;padding:14px 16px;background:var(--zone);
  border:1px solid var(--line);border-left:4px solid var(--accent);
  font-size:13px;line-height:1.6}
.verdict b{font-family:var(--mono);font-size:9px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--accent);display:block;margin-bottom:5px;font-weight:500}
.fa{display:flex;gap:22px;margin-top:14px}
.fa>div{flex:1}
.fa h4{font-family:var(--mono);font-size:8px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--muted);padding-bottom:6px;border-bottom:1px solid var(--line);margin-bottom:7px}
.fa li{font-size:11.4px;line-height:1.55;margin:0 0 6px 14px;color:var(--ink)}

/* ── figures — .map AND .photo together, always (bug log #6, #7) ── */
.map,.photo{margin:4px 0 22px}
.map svg,.photo img{width:100%;display:block;border:1px solid var(--line-soft)}
.photo.wide img{height:2.25in;object-fit:cover}
.photo.band img{height:2.35in;object-fit:cover}
.photo.strip img{height:1.6in;object-fit:cover}
.page > .photo:nth-last-child(2){margin-bottom:0}
.cov .covstrip{margin:0}
.cov .covstrip img{width:100%;height:1.5in;object-fit:cover;display:block;border:1px solid var(--line-soft)}
.map figcaption,.photo figcaption{margin-top:10px;padding-top:8px;
  border-top:1px solid var(--line-soft);font-family:var(--mono);font-size:7.5px;
  line-height:1.6;letter-spacing:.05em;color:var(--muted)}
.fign{color:var(--accent);letter-spacing:.16em}

/* ── checklist ── */
.ck{width:100%;border-collapse:collapse;font-size:12.2px;line-height:1.5}
.ck td{padding:8px 0;border-bottom:1px solid var(--line-soft);vertical-align:top}
.ck td.box{width:22px;color:var(--accent);font-size:11px}
.ck td.when{width:1.45in;font-family:var(--mono);font-size:9px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--deep);padding-right:10px}

/* ── contents ── */
.toc{width:100%;border-collapse:collapse;font-size:13px;line-height:1.5}
.toc td{padding:5.5px 0;border-bottom:1px solid var(--line-soft);vertical-align:baseline}
.toc td.pg{text-align:right;font-family:var(--mono);font-size:10px;color:var(--deep);width:40px}
.toc td.sec{font-family:var(--mono);font-size:8px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--accent);border-bottom:none;padding-top:15px}
.toc .it{color:var(--muted);font-style:italic;font-size:11.5px}

/* ── failure modes ── */
.fm{margin-bottom:13px;padding-left:14px;border-left:2px solid var(--line)}
.fm h4{font-family:var(--body);font-weight:400;font-size:13.4px;margin-bottom:2px}
.fm h4 .x{font-family:var(--mono);font-size:9px;color:var(--accent);letter-spacing:.1em}
.fm p{font-size:11.6px;line-height:1.58;color:var(--muted)}
.fm p b{color:var(--ink);font-weight:400}
.cons{font-family:var(--mono);font-size:8px;letter-spacing:.24em;text-transform:uppercase;
  color:var(--paper);background:var(--ink);display:inline-block;padding:4px 10px;margin:4px 0 14px}

/* ── wallet card ── */
.wallet{border:2px solid var(--ink);background:var(--paper);padding:0;margin-top:8px}
.wallet .wh{background:var(--ink);color:var(--paper);font-family:var(--mono);font-size:9px;
  letter-spacing:.26em;text-transform:uppercase;padding:8px 14px;display:flex;justify-content:space-between}
.wallet .wb{display:flex}
.wallet .wc{flex:1;padding:12px 14px;font-size:10.8px;line-height:1.62}
.wallet .wc+.wc{border-left:1px solid var(--line)}
.wallet .wc h5{font-family:var(--mono);font-size:8px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--accent);margin-bottom:6px}
.wallet .wc div{margin-bottom:5px}
.scissor{font-family:var(--mono);font-size:8px;color:var(--soft);letter-spacing:.3em;
  text-align:center;margin:6px 0}

/* ── field sheet ── */
.fs-band{background:var(--ink);color:var(--paper);margin:-0.85in -0.85in 26px;padding:22px 0.85in}
.fs-band .eyebrow{color:var(--gilt);margin-bottom:8px}
.fs-band h1{font-family:var(--display);font-weight:400;font-size:34px;color:var(--paper)}
.fs-band .standfirst{border:none;color:#cfc4a6;margin:6px 0 0;padding:0;font-size:14px}
table.fst{width:100%;border-collapse:collapse;font-size:11.6px;line-height:1.5}
.fst th{font-family:var(--mono);font-size:8px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--soft);text-align:left;padding:6px 0;border-bottom:1px solid var(--line)}
.fst td{padding:6.5px 0;border-bottom:1px solid var(--line-soft);vertical-align:top}
.fst td.v{font-family:var(--mono);font-size:10.5px;color:var(--deep);white-space:nowrap;
  padding-right:16px}
.fst td.src{font-size:10.2px;color:var(--muted)}

/* ── hood grid ── */
.hoods{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.hood h4{font-family:var(--display);font-weight:400;font-size:15px;margin:6px 0 2px}
.hood .m{font-family:var(--mono);font-size:8px;letter-spacing:.14em;color:var(--deep);
  text-transform:uppercase}
.hood p{font-size:10.6px;line-height:1.5;color:var(--muted)}
.hood svg{width:100%;display:block;border:1px solid var(--line-soft)}

/* ── neighborhood assessments ── */
.na{display:grid;grid-template-columns:33% 1fr;gap:14px;align-items:start;margin-bottom:16px;padding-bottom:13px;border-bottom:1px solid var(--line-soft)}
.na .loc svg{width:100%;display:block;border:1px solid var(--line-soft)}
.na h3{font-family:var(--display);font-weight:400;font-size:19px;margin-bottom:3px}
.na .crit{font-family:var(--mono);font-size:8.5px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--deep);margin-bottom:6px}
.na .crit b{color:var(--soft);font-weight:400}
.na p{font-size:11.8px;line-height:1.6}
.na .call{font-size:11.4px;font-style:italic;color:var(--deep);margin-top:4px}

/* ── cover ── */
.cov{width:8.5in;height:11in;position:relative;background:var(--paper);overflow:hidden;
  page-break-after:always}
.cov .frame{position:absolute;inset:0.42in;border:1.5px solid var(--ink);
  outline:1px solid var(--ink);outline-offset:5px}
.cov .in{position:absolute;inset:0.42in;padding:0.55in 0.6in;display:flex;
  flex-direction:column}
.cov .brand{font-family:var(--mono);font-size:9px;letter-spacing:.34em;text-transform:uppercase;
  color:var(--accent);display:flex;justify-content:space-between}
.cov .brand span{color:var(--soft)}
.cov h1{font-family:var(--display);font-weight:400;font-size:104px;line-height:.98;
  margin:0.32in 0 0.14in;color:var(--ink)}
.cov h1 i{font-style:italic;color:var(--accent)}
.cov .sub{font-family:var(--body);font-style:italic;font-size:17px;line-height:1.5;
  color:var(--muted);max-width:5.6in}
.cov .dev{margin:0.26in 0 0.18in}
.cov .dev svg{width:100%;display:block}
.cov .capline{font-family:var(--mono);font-size:8px;letter-spacing:.24em;text-transform:uppercase;
  color:var(--muted);border-top:1.5px solid var(--ink);padding-top:9px;display:flex;
  justify-content:space-between}
.cov .strip{margin-top:0.16in}
.cov .strip img{width:100%;height:1.6in;object-fit:cover;display:block;
  border:1px solid var(--ink)}
.cov .foot{margin-top:auto;display:flex;justify-content:space-between;align-items:baseline;
  font-family:var(--mono);font-size:8.5px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--muted)}
.cov .foot b{color:var(--deep);font-weight:500}

/* ── decision header banner (numeral + meta, no corner collision) ── */
.dhead{display:flex;align-items:center;gap:16px;margin-bottom:16px;
  padding-bottom:14px;border-bottom:2px solid var(--ink)}
.dhead .dn{font-family:var(--display);font-size:52px;line-height:.85;color:var(--accent)}
.dhead .dmeta{display:flex;flex-direction:column;gap:3px}
.dhead .dk{font-family:var(--mono);font-size:8.5px;letter-spacing:.26em;text-transform:uppercase;
  color:var(--soft)}
.dhead .dcat{font-family:var(--display);font-size:22px;color:var(--ink);line-height:1}
/* ── decision question ── */
.dq{font-family:var(--display);font-size:27px;line-height:1.12;margin:0 0 14px}

/* ── drop cap for opening essay ── */
.drop:first-letter{font-family:var(--display);font-size:62px;line-height:.8;float:left;
  padding:6px 9px 0 0;color:var(--accent)}

/* ── contents (div rows, not a table) ── */
.toc{margin-top:4px}
.tocrow{display:flex;justify-content:space-between;align-items:baseline;
  padding:7.5px 0;border-bottom:1px solid var(--line-soft)}
.tocrow .tt{font-size:13px;color:var(--ink)}
.tocrow .tp,.tocrow .tnum{font-family:var(--mono);font-size:9.5px;color:var(--deep);
  letter-spacing:.14em;padding-left:16px}
.toc-note{font-family:var(--mono);font-size:8.4px;line-height:1.6;letter-spacing:.02em;
  color:var(--muted);margin-top:16px;padding-top:11px;border-top:1px solid var(--line-soft)}

/* ── how-to-read marks table ── */
table.marks{width:100%;border-collapse:collapse;margin:6px 0 4px}
.marks td{padding:9px 0;border-bottom:1px solid var(--line-soft);vertical-align:top;
  font-size:11.6px;line-height:1.5;color:var(--ink)}
.marks td.m{width:34px;text-align:center}
.marks td.md{width:1.15in;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--deep);padding-right:12px}

/* ── refusals ── */
.ref{margin-top:6px}
.ri{margin-bottom:13px;padding-left:15px;border-left:2px solid var(--gilt)}
.ri h4{font-family:var(--display);font-weight:400;font-size:17px;margin-bottom:3px;color:var(--ink)}
.ri p{font-size:11.5px;line-height:1.58;color:var(--muted)}
.ri p i{color:var(--ink);font-style:italic}

/* ── opening plate ── */
.op-plate{text-align:center;margin:0.55in 0 0.42in}
.op-brand{font-family:var(--display);font-size:40px;letter-spacing:.02em;color:var(--ink)}
.op-rule{width:1.1in;height:2px;background:var(--accent);margin:14px auto}
.op-sub{font-family:var(--mono);font-size:9px;letter-spacing:.32em;text-transform:uppercase;
  color:var(--soft)}

/* ── closing colophon ── */
.colophon{margin-top:26px;padding-top:16px;border-top:2px solid var(--ink);text-align:center}
.colophon .cbrand{font-family:var(--display);font-size:22px;color:var(--ink);margin-bottom:8px}
.colophon p{font-family:var(--mono);font-size:8.4px;line-height:1.7;letter-spacing:.04em;
  color:var(--muted);max-width:32em;margin:0 auto}

/* ── field-sheet band header + change log ── */
.fst .fk{font-family:var(--mono);font-size:9px;letter-spacing:.3em;text-transform:uppercase;
  color:var(--gilt)}
.fst .fmeta{font-family:var(--mono);font-size:8px;letter-spacing:.16em;text-transform:uppercase;
  color:#cfc4a6;margin-top:5px}
.cl{margin-top:16px;border:1px solid var(--line);background:var(--zone);padding:12px 14px}
.cl .clh{font-family:var(--mono);font-size:8px;letter-spacing:.24em;text-transform:uppercase;
  color:var(--accent);margin-bottom:6px}
.cl .clr{font-size:11px;line-height:1.55;color:var(--ink)}
.cl .clr b{font-family:var(--mono);font-size:9.5px;color:var(--deep)}
.fsfoot{font-family:var(--body);font-style:italic;font-size:11.5px;line-height:1.5;
  color:var(--muted);margin-top:18px;padding-top:12px;border-top:1px solid var(--line-soft)}

/* ── hood grid: name + walk labels under each mini ── */
.hood .mini svg{width:100%;display:block;border:1px solid var(--line-soft)}
.hood .hn{font-family:var(--display);font-weight:400;font-size:14.5px;margin:6px 0 1px}
.hood .hw{font-family:var(--mono);font-size:7.5px;letter-spacing:.1em;color:var(--deep);
  text-transform:uppercase}

/* ── misc ── */
.hr{border:0;border-top:1px solid var(--line);margin:20px auto;max-width:200px}
.clear{clear:both}
sup.x{font-family:var(--mono);font-size:8px;color:var(--accent)}
"""
