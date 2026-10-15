#!/bin/zsh
# chain.sh — the full rebuild, in the order the gates expect. Run from build/.
set -e
cd "$(dirname "$0")"
export CODEX_PRIMARY_RUNTIME_NODE_MODULES=/Users/sg54/Desktop/travel-sites/barcelonaforamericans/node_modules
python3 evidence.py
python3 build3.py | tail -4
python3 ~/.claude/skills/dossier/scripts/compile-guide.py . | tail -2
python3 render-docs.py book 2>&1 | tail -6
python3 render-docs.py sheet 2>&1 | tail -2
python3 add-nav.py . | tail -3
python3 render-phone.py . 2>&1 | tail -2
python3 add-nav.py . --pdf dossier-phone.pdf --html _book.html | tail -2
python3 emit-manuscript.py . | tail -2
python3 freehook.py | tail -1
python3 - <<'PY' 2>&1 | tail -1
import importlib.util, os, sys
sys.argv=sys.argv[:1]
src=open('render-paged.py').read().replace('\nif __name__ == "__main__":\n    render()\n','\n')
spec=importlib.util.spec_from_file_location('rp','render-paged.py'); rp=importlib.util.module_from_spec(spec); sys.modules['rp']=rp
exec(compile(src,'render-paged.py','exec'), rp.__dict__)
rp.render('freehook.html','freehook.pdf')
PY
python3 check-svg-text.py . 2>&1 | tail -2
echo "── chain done ──"
