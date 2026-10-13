# Greece, in Order. — build source

A paid PDF decision-manual built from the greeceforamericans corpus (80 articles)
using the dossier skill. Ships with 8 real photographs + 12 computed figures.

## Reproduce

    pip install playwright pypdf pillow fonttools --break-system-packages
    playwright install chromium
    cp fonts/*.ttf ~/.fonts/ && fc-cache -f    # so SVG figures resolve the display face
    python3 build.py                            # -> dossier3.html
    python3 render-paged.py                      # -> dossier.pdf (43pp)

## Modules

- `geo.py`         real coordinates + corpus-stated ferry/wind/pace facts
- `design.py`      THE CSS — single source of truth (paged page model, Greece tokens, one baseline)
- `maps.py`        12 computed figures + the cover device
- `content.py`     the 9 decisions (the analytical heart)
- `prose.py`       front matter, essays, surrounding chapters, Field Sheet content
- `fieldsheet.py`  the dated annex (volatile figures only)
- `build.py`       assembles dossier3.html; PHOTOS registry maps A0x.jpg -> decisions
- `render-paged.py`   Paged.js render + feathering (photos & map figures are feedable plates)
- `photos/opt/`    the 8 print-optimized photographs (EXIF stripped)
- `corpus.json`    the source corpus
- `brand.json`     derived brand (Meltemi Press — Aegean whitewash palette)
- `state.json`     build decisions + final state
- `gate-outputs/`  the four gate reports

## Gates (all green)

- audit-book:      CLEAN — Ship
- audit-furniture: PASS (pass `--paper F4EFE6`)
- audit-depth:     MINED
- audit-synthesis: STRONG
