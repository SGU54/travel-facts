#!/bin/sh
# build → compose (atelier) → render both documents
set -e
cd "$(dirname "$0")"
python3 build-html.py
rm -f dossier3.raw.html
python3 compose.py .
python3 render-both.py .
