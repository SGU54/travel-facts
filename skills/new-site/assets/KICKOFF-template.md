Launch <SLUG> — Stage 1 (Architecture) of the travel-empire skill.
Invoke the skill and follow references/1-architecture.md.

EVERYTHING IS ALREADY PROVISIONED. Do not ask me for access, credentials, API
keys, logins, or permission to use them. They are in place and you can verify
each one yourself:
 · Supabase — shared fleet project; keys already in apps/*/.env.local. This
   site's schema is `<SCHEMA>`.
 · R2 media — keys in apps/admin/.env.local. Host img.sgfleetmedia.com, folder
   <SLUG>. The object key IS the public_id, with no extension, so an
   explicit ContentType on upload is mandatory (hard rule 10).
 · GitHub — git credentials work for SGU54 repos; clone and push directly.
 · Vercel, Namecheap and Google Search Console — all logged in in Chrome; use
   the browser tools. Enable Web Analytics on the SITE project (dashboard →
   Analytics → Enable) — <Analytics/> renders either way but shows Demo Data until then. <DOMAIN> is already registered at Namecheap.
 · Vercel CLI — ALREADY LOGGED IN. The launcher ran `vercel login` before this
   session started, precisely so you never have to ask me to click through the
   dashboard. Use the CLI for everything:
       npx vercel link                      # connect this dir to the project
       npx vercel env add <KEY> production  # set a variable (reads stdin)
       npx vercel env ls                    # confirm what is actually set
   Create the two projects, set their env vars and deploy from the CLI. Do not
   ask me to do any of it by hand.
 · Playwright is installed in barcelonaforamericans/node_modules; PIL is
   available for contact sheets. There is no ImageMagick.

The site is scaffolded from template v5.8. READ CHANGELOG-v5.8.md FIRST — it
documents four failure classes that are completely silent, and three of them
bite during launch specifically.

FIRST TASK — THE ADMIN SECRETS AND THE ADMIN PORTAL
Do this before anything else; the admin is how I review every later stage.

 1. GENERATE both admin secrets yourself. Do not ask me for them, do not reuse
    another site's, and do not print either value in chat — a secret that goes
    through a transcript is a secret you have to rotate.

      openssl rand -base64 24   # ADMIN_PASSWORD
      openssl rand -hex 32      # ADMIN_SESSION_SECRET

    Write them straight into apps/admin/.env.local (ADMIN_PASSWORD and
    ADMIN_SESSION_SECRET). When you are done, tell me only that they are set
    and that I can read ADMIN_PASSWORD out of that file — never the value.
    Both are required: apps/admin/lib/auth.ts REFUSES to start in production
    without ADMIN_SESSION_SECRET rather than falling back to a dev default,
    and /api/auth/login errors without ADMIN_PASSWORD.

 2. STAND UP THE ADMIN PORTAL. Two Vercel projects come from the SAME repo
    (DEPLOY.md §2):
      <SLUG>-site   → Root Directory apps/site   → the domain + www
      <SLUG>-admin  → Root Directory apps/admin  → Vercel URL only,
                                deliberately NO public domain
    Install Command is `npm install` at the REPO ROOT for both, so the
    workspace links @travel/config and @travel/db. Set the env vars on BOTH
    projects — missing on one is the classic "works locally, breaks on deploy"
    trap. ADMIN_PASSWORD and ADMIN_SESSION_SECRET go on the admin project only.

 3. VERIFY THE ADMIN BEFORE MOVING ON, on a preview deploy (DEPLOY.md §5):
    /login accepts the password, and the dashboard's category count matches
    `<SCHEMA>.categories`. A wrong-schema read shows another site's counts or
    zero — that is the failure this check exists to catch, and it looks like
    success if you only check that the page loads.
    Then put the admin's production URL into common.sites.admin_url.

WHERE THINGS LIVE
 · TEXT — facts.json, article-list.json, state.json, corrections.json, the SQL
   seed, audits → /Users/sg54/Desktop/travel-sites/travel-facts/<SLUG>
   That is a git repo on LOCAL disk. Commit and push it.
 · IMAGES → /Volumes/Untitled/travel-facts/<SLUG>/content/...
   NEVER run git under /Volumes/Untitled — it is exFAT and corrupts git
   objects; that is measured, not theoretical. And never push images to
   GitHub: accounts get suspended for using repos as storage.

THE TWO COMMANDS THAT PROVE STAGE 1 (run after the first deploy, before anything else)
   node /Users/sg54/Desktop/travel-sites/_fleet-audit-2026-10-14/scripts/onboard-check.mjs <SCHEMA> <SLUG> <DOMAIN> --sql-out /Users/sg54/Desktop/travel-sites/travel-facts/<SLUG>/onboard-<SCHEMA>.sql
   node /Users/sg54/Desktop/travel-sites/_fleet-audit-2026-10-14/scripts/fleet-gate.mjs --sites <SCHEMA>
 Both print "checked N of N". Do not report Stage 1 done while either has a FAIL.
 (The SQL file the first one writes is the one thing you paste into the Supabase SQL editor.)

DO THESE DURING STAGE 1, NOT "AT LAUNCH" — each one fails silently
 1. Register the site in common.sites BEFORE the first deploy
    (supabase/common/ONBOARD_SITE.sql, and DEPLOY.md §0b). Verify by POSTing to
    /api/subscribe and reading the BODY for "stored":true. A 200 proves
    nothing — the route is fail-soft. Skip this and every email the lead magnet
    collects is discarded with no error anywhere.
 2. Confirm apps/site/middleware.ts is present and that the Vercel alias
    (<SLUG>-site.vercel.app) returns X-Robots-Tag: noindex. Without
    it the whole site ships a second, fully crawlable copy.
 3. Add the Google Search Console DOMAIN property (sc-domain:, verified by a
    DNS TXT record at Namecheap) and submit the sitemap. Read the TXT value
    from the DOM — it is visually truncated on screen, and GSC shows a green
    "sitemap sent" toast over a row that may already say it could not fetch.

HOW I WANT YOU TO WORK
 · Propose and verify; don't assume. Check the rendered page, not the markup.
 · A gate that prints PASS has not necessarily checked anything — read its
   counts before trusting it.
 · Facts come from the fact pipeline, never invented, and never freeze a live
   price into prose or config.
 · Design comes LAST (Stage 5) and is my call. Keep the skeleton neutral until
   then — do not pick a palette, fonts or a logo. When you reach Stage 5, ask
   me for the <DESTINATION> thesis first.
 · Tell me plainly when something is blocked or when you are unsure, rather
   than guessing and moving on.

START HERE
Read state.json if it exists. Do the admin secrets and the admin portal first
(above), then draft the category list and the article list for my approval,
and run the Stage 1c opportunity gate over the article list. Do not write any
articles yet.
