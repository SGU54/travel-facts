# Next.js App Router — Rules & Gotchas

Read this **before writing any Next.js file**. Every rule here is a bug actually hit in production.

## CSS and fonts

- **Web fonts load from a `<link>` in `app/layout.tsx`, built from `SITE.brand.fonts`. There is
  NO font `@import` in `globals.css` — ever.** (Hard rule 17.) The reason: `globals.css` also
  does `@import './tokens.css'`, and PostCSS **inlines** that file, so its `:root{…}` lands at the
  top of the compiled stylesheet. Any font `@import` is then no longer the first rule, which the
  CSS spec says makes it invalid; browsers drop it **without any error** and every face falls
  back to Georgia / Impact / system-ui. Vietnam shipped like this and was found by an outside
  reader; Rome was still shipping like this on 2026-10-14 (`document.fonts` loaded = 0 of 3).
  `scripts/skeleton-check.mjs` fails on a font `@import`; `fleet-gate FONTS` and
  `render-check fontsLoaded` prove the served result.

```tsx
// app/layout.tsx — the only place fonts are requested
<head>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
  <link rel="stylesheet" href={googleFontsHref(SITE.brand.fonts)} />   {/* renders nothing while fonts are <placeholders> */}
</head>
```

```css
/* app/globals.css — tokens first, tailwind next, NO font @import */
@import './tokens.css';

@tailwind base;
@tailwind components;
@tailwind utilities;
```

- **`span.fact` is an INLINE contract.** A design class took `.fact` for a block with padding and
  cut sentences into three across 31 of 100 articles. `globals.css` carries a specificity-(0,1,1)
  guard pinning `span.fact[data-fact]{display:inline}`; never name a design class `.fact`.

## Server vs client components

- **Never call `cookies()` inside `layout.tsx`.** It throws a server-side exception. Do auth
  checks per page or in a client component.
- **`'use client'` only on components that need state or events.** Fetch data in server
  components and pass it down as props. The DB-driven `Header` is a client component but
  receives `navigation` as a prop from the server `layout`.

## Forms & mutations

- **No HTML `<form action=... method=...>` in the App Router.** Use a client component with
  `fetch()` + handlers, or server actions. All admin create/update/delete flows use `fetch`.

## Routing

- **API route files must sit at the exact path** — the folder structure IS the URL.
  Login: `app/api/auth/login/route.ts`. We put this in the wrong folder twice.
- A `route.ts` exports named HTTP methods: `export async function GET/POST/PUT/DELETE`.
- **`/go/guide/[src]` validates `src` against the surface list** (hard rule 18). A dynamic
  segment that accepts anything becomes a log full of minified JavaScript.

## Monorepo / folders

- **Confirm which `app/` you are editing.** `apps/site` vs `apps/admin` — a `pwd` first.

## Deploy / caching

- **`export const revalidate = 60`** on dynamic pages (home, category, article).
- **`/guide` is `force-dynamic`** — its live-ness is a runtime toggle (first-click-404 bug).
- **Verify on a Vercel preview deploy before promoting.** After a push, confirm the deployed
  commit hash (`npx vercel inspect <url>`).
- **A push to `main` on any site repo deploys production immediately.** Fleet-wide commits
  (2026-10-14 05:04: eight sites in eleven seconds) are normal; a measurement taken across a
  deploy must be re-taken.

## Cloudflare R2 (image service)

- **Store only the bare object key** — no extension, no domain. The full URL is built from
  `SITE_CONFIG.media` at render time.
- **Set `ContentType` explicitly on every upload.**
- **Every in-body delivery URL carries `width=1200`**, options sorted (`format=auto,width=1200`).
  Without it Cloudflare serves the original — 3.7 MB into a 700 px column (Morocco, 34 images).
- **The upload folder depends on the SURFACE, not the image type.** Media page → `media/`;
  article editor → `articles/`.
- **Paginate `ListObjectsV2`.** **Scope DELETE to this site's folder; 403 otherwise.**
- **Cloudflare limits:** no chained transformations; source under 100 megapixels (error 9413);
  a derivative is cached `immutable` for a year — re-key, don't overwrite.

## Third-party scripts

- **None.** Analytics is `@vercel/analytics` (`<Analytics/>` in layout — and the project's
  Web Analytics must be ENABLED in Vercel or the dashboard shows "Demo Data"; Vietnam and
  Bali were in that state at launch). No affiliate "drive" scripts, no tag managers: the
  one outbound mechanism is `/go/` (hard rule 6). `render-check.mjs` inventories every
  `<script src>` host.

## Editing discipline

- For **new or large files, deliver the whole file**. Small targeted diffs only for tiny edits.
