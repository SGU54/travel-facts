#!/usr/bin/env bash
# make-bootstrap.sh — write a one-shot bootstrap script for a NEW fleet site, then
# (optionally) run it in a new Terminal window. It generates; it does not execute.
#
# Usage:
#   make-bootstrap.sh <slug> <schema> <domain> <destination> [--open] [--handoff-only]
#
# Changes vs the 2026-10-13 version (fleet audit 2026-10-14):
#   · the kickoff prompt is GENERATED from assets/KICKOFF-template.md (no hand copy)
#   · pre-flight: domain registered, disk ≥ 2 GB, donor env present — printed as "checked N of N"
#   · the template zip is the NEWEST travel-template-v*.zip in the repo, not a constant
#   · the generated script ends by printing the onboard-check / fleet-gate commands
set -euo pipefail

SLUG="${1:?usage: make-bootstrap.sh <slug> <schema> <domain> <destination> [--open] [--handoff-only]}"
SCHEMA="${2:?missing <schema>}"
DOMAIN="${3:?missing <domain>}"
DEST="${4:?missing <destination>}"
OPEN=""; HANDOFF_ONLY=""
for a in "${@:5}"; do case "$a" in --open) OPEN=1;; --handoff-only) HANDOFF_ONLY=1;; *) echo "unknown flag: $a"; exit 1;; esac; done

ROOT="/Users/sg54/Desktop/travel-sites"
FACTS_REPO="$ROOT/travel-facts"
VOLUME="/Volumes/Untitled/travel-facts"
DONOR="${DONOR:-vietnamforamericans}"          # override with DONOR=<slug> env
AUDIT="$ROOT/_fleet-audit-2026-10-14/scripts"  # until adopted into fleet_ops/scripts
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/bootstrap-$SLUG.sh"
KICKOFF="$ROOT/$(echo "$SCHEMA" | tr '[:lower:]' '[:upper:]')-KICKOFF.md"

say() { printf '\n\033[1;36m== %s\033[0m\n' "$1"; }

# ── pre-flight (used to be three hand steps) ─────────────────────────────────
checks=0; fails=0
pf() { checks=$((checks+1)); if [ "$1" = ok ]; then printf 'PASS  %-22s %s\n' "$2" "$3"; else fails=$((fails+1)); printf 'FAIL  %-22s %s\n' "$2" "$3"; fi; }
ns="$(dig +short NS "$DOMAIN" @8.8.8.8 2>/dev/null | head -1)"
[ -n "$ns" ] && pf ok "domain registered" "NS $ns" || pf fail "domain registered" "no NS answer for $DOMAIN — register it first"
free_kb="$(df -k / | awk 'NR==2{print $4}')"
[ "$free_kb" -ge 2097152 ] && pf ok "disk ≥ 2 GB" "$((free_kb/1024/1024)) GB free" || pf fail "disk ≥ 2 GB" "$((free_kb/1024)) MB free — clear .next/ and dormant node_modules/ first: $(find "$ROOT" -maxdepth 2 -name .next -type d 2>/dev/null | head -3 | tr '\n' ' ')"
if [ -z "$HANDOFF_ONLY" ]; then
  if [ -f "$ROOT/$DONOR/apps/admin/.env.local" ] && [ -f "$ROOT/$DONOR/apps/site/.env.local" ] && grep -q '^SUPABASE_SERVICE_ROLE_KEY=.\+' "$ROOT/$DONOR/apps/admin/.env.local"; then pf ok "donor env ($DONOR)" "both .env.local present with fleet keys"; else pf fail "donor env ($DONOR)" "missing — set DONOR=<live site slug>"; fi
  if [ -e "$ROOT/$SLUG" ]; then pf fail "site folder absent" "$ROOT/$SLUG exists — use --handoff-only"; else pf ok "site folder absent" "$ROOT/$SLUG"; fi
else
  [ -d "$ROOT/$SLUG" ] && pf ok "site folder present" "$ROOT/$SLUG" || pf fail "site folder present" "--handoff-only needs $ROOT/$SLUG"
fi
echo "checked $checks of $checks pre-flight · $fails FAIL"
[ "$fails" -eq 0 ] || { echo "REFUSING: fix the FAIL rows above."; exit 1; }

# ── kickoff prompt: generated, never hand-copied ─────────────────────────────
if [ ! -f "$KICKOFF" ]; then
  sed -e "s|<SLUG>|$SLUG|g" -e "s|<SCHEMA>|$SCHEMA|g" -e "s|<DOMAIN>|$DOMAIN|g" -e "s|<DESTINATION>|$DEST|g" "$SKILL_DIR/assets/KICKOFF-template.md" > "$KICKOFF"
  echo "wrote $KICKOFF (from the template; edit it before --open if you want to add context)"
else
  echo "kickoff exists, left untouched: $KICKOFF"
fi

HANDOFF_BLOCK=$(cat <<EOT
say "Vercel CLI login (a browser window opens if needed)"
if npx --yes vercel whoami >/dev/null 2>&1; then echo "   already logged in as \$(npx --yes vercel whoami 2>/dev/null)"; else npx --yes vercel login; fi

say "After the first deploy, the session MUST run (it is in the kickoff too):"
echo "   node $AUDIT/onboard-check.mjs $SCHEMA $SLUG $DOMAIN --sql-out $FACTS_REPO/$SLUG/onboard-$SCHEMA.sql"
echo "   node $AUDIT/fleet-gate.mjs --sites $SCHEMA"

say "Starting Claude in $ROOT/$SLUG"
cd "$ROOT/$SLUG"
# Prompt FIRST: --add-dir is variadic and swallows anything after it.
exec claude "\$(cat "$KICKOFF")" --add-dir "$FACTS_REPO" "$VOLUME"
EOT
)

if [ -n "$HANDOFF_ONLY" ]; then
  { echo '#!/usr/bin/env bash'; echo "# bootstrap-$SLUG.sh (HANDOFF ONLY) — generated $(date '+%Y-%m-%d %H:%M'). Creates and overwrites nothing."; echo 'set -euo pipefail'; echo "say() { printf '\n\033[1;36m== %s\033[0m\n' \"\$1\"; }"; echo "$HANDOFF_BLOCK"; } > "$OUT"
else
  TPL_DIR="/tmp/tpl-repo-$SLUG"
  cat > "$OUT" <<EOT
#!/usr/bin/env bash
# bootstrap-$SLUG.sh — generated $(date '+%Y-%m-%d %H:%M') by the new-site skill.
# Stands up $SLUG from the NEWEST template zip and hands off to a Claude session.
# Safe to read before running. Stops at the first failure.
set -euo pipefail
ROOT="$ROOT"; SLUG="$SLUG"; SCHEMA="$SCHEMA"; DOMAIN="$DOMAIN"; SITE="\$ROOT/\$SLUG"
say() { printf '\n\033[1;36m== %s\033[0m\n' "\$1"; }

say "Fetching the newest template zip"
rm -rf "$TPL_DIR"; git clone --quiet https://github.com/SGU54/travel-template.git "$TPL_DIR"
ZIP="\$(ls "$TPL_DIR"/travel-template-v*.zip | sort -V | tail -1)"
echo "   using \$(basename "\$ZIP")  (all: \$(ls "$TPL_DIR"/travel-template-v*.zip | xargs -n1 basename | tr '\n' ' '))"
mkdir -p "\$SITE"; cd "\$SITE"; unzip -q "\$ZIP"

say "Copying fleet-shared credentials from $DONOR"
cp "\$ROOT/$DONOR/apps/admin/.env.local" apps/admin/.env.local
cp "\$ROOT/$DONOR/apps/site/.env.local"  apps/site/.env.local
say "Pointing the env at \$SCHEMA / \$DOMAIN (admin secrets blanked for the session to generate)"
/usr/bin/sed -i '' -e "s|^SUPABASE_DB_SCHEMA=.*|SUPABASE_DB_SCHEMA=\$SCHEMA|" -e "s|^MEDIA_FOLDER=.*|MEDIA_FOLDER=\$SLUG|" -e "s|^NEXT_PUBLIC_SITE_URL=.*|NEXT_PUBLIC_SITE_URL=https://www.\$DOMAIN|" -e "s|^ADMIN_BASE_URL=.*|ADMIN_BASE_URL=https://\$SLUG-admin.vercel.app|" -e "s|^ADMIN_PASSWORD=.*|ADMIN_PASSWORD=|" -e "s|^ADMIN_SESSION_SECRET=.*|ADMIN_SESSION_SECRET=|" apps/admin/.env.local
/usr/bin/sed -i '' -e "s|^NEXT_PUBLIC_SITE_URL=.*|NEXT_PUBLIC_SITE_URL=https://www.\$DOMAIN|" apps/site/.env.local
grep -c '^SUPABASE_DB_SCHEMA=\$SCHEMA\$' apps/admin/.env.local >/dev/null || { echo "env rewrite failed"; exit 1; }

say "npm install (repo root — links @travel/config and @travel/db)"
npm install
say "skeleton-check --template (fails on any font @import — hard rule 17)"
node scripts/skeleton-check.mjs --template

say "Creating the text and image working directories"
mkdir -p "$FACTS_REPO/\$SLUG" "$VOLUME/\$SLUG/content"

$HANDOFF_BLOCK
EOT
fi
chmod +x "$OUT"; echo "wrote $OUT"
if [ -n "$OPEN" ]; then
  [ -f "$KICKOFF" ] || { echo "REFUSING to open: $KICKOFF missing."; exit 1; }
  osascript -e "tell application \"Terminal\" to do script \"bash '$OUT'\"" -e 'tell application "Terminal" to activate' >/dev/null
  echo "opened a new Terminal window running it"
else
  echo "review it, then:  bash '$OUT'   (or re-run with --open)"
fi
