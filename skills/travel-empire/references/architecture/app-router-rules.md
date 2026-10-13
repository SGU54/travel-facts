# Next.js App Router — Rules &amp; Gotchas

Read this **before writing any Next.js file**. Every rule here is a bug actually hit in production, with the hours to prove it. Following them prevents the cryptic errors.

## CSS

- **`@import` must be the FIRST line of `globals.css`**, before the `@tailwind` directives.
  Placing the font `@import` after `@tailwind` silently breaks font loading.

```css
@import url('https://fonts.googleapis.com/css2?family=...&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;
```

## Server vs client components

- **Never call `cookies()` inside `layout.tsx`.** It throws a server-side exception
  (we saw "Digest: 2625991887"). Do auth checks in a client component (read state) or
  per-page, not in the root layout.
- **`'use client'` only on components that need state or events.** Fetch data in server
  components and pass it down as props. The DB-driven `Header` is a client component
  (it has dropdown state) but receives `navigation` as a prop from the server `layout`.
- An async server `layout.tsx` CAN fetch data (e.g. `getNavigation()`) and pass it to a
  client `Header`. That is the correct pattern for database-driven navigation.

## Forms &amp; mutations

- **No HTML `<form action=... method=...>` in the App Router.** It crashes the page.
  Use a client component with `fetch()` calls and `onClick` handlers, or server actions.
  All admin create/update/delete flows use `fetch` + client handlers.

## Routing

- **API route files must sit at the exact path** — the folder structure IS the URL.
  - Login: `app/api/auth/login/route.ts` (NOT `app/login/route.ts`, NOT `app/api/login/route.ts`).
  - We put this in the wrong folder twice; double-check the path before debugging logic.
- A `route.ts` exports named HTTP methods: `export async function GET/POST/PUT/DELETE`.
  Order of the functions in the file does not matter; the path does.

## Monorepo / folders

- **Confirm which `app/` you are editing.** With site + admin in one repo it is easy to
  edit the wrong one, push, and see nothing change. Clear app names (`apps/site`,
  `apps/admin`) and a quick `pwd`/path check prevent this.

## Deploy / caching

- **Use `export const revalidate = 60`** on dynamic pages (home, category, article) so
  edits appear within a minute.
- **Verify on a Vercel preview deploy before promoting to production.** Do not debug on
  the live site via screenshots (we did; it is slow and risky).
- After a push, confirm the new commit hash is the one Vercel actually deployed.

## Cloudflare R2 (image service)

- **Store only the bare object key** in the database — no extension, no domain. The full URL
  is built from `SITE_CONFIG.media` at render time. This is what let the whole fleet change
  CDN without touching one database row.
- **Set `ContentType` explicitly on every upload.** With no extension in the key it is the
  only signal that an object is an image; get it wrong and browsers download instead of
  displaying. On a resumed or partial upload run, re-derive it from the file's magic bytes
  rather than assuming — a skipped file with no Content-Type ships as
  `application/octet-stream`.
- **The upload folder depends on the SURFACE, not the image type.** Media library page →
  `media/`; article editor (hero OR body) → `articles/`. A real bug had the same button
  writing to two different folders depending on which handler ran.
- **Paginate `ListObjectsV2`.** A single unpaginated page silently hides the NEWEST uploads
  once a folder passes the limit — the symptom is "my upload vanished", not an error.
- **Scope DELETE to this site's folder and refuse anything else with a 403.** The bucket is
  shared across the fleet and the token writes everywhere, so one site's admin could
  otherwise delete another site's images — which its database-level guard cannot see.
- **Cloudflare limits worth knowing:** transformations cannot be chained in one URL; the
  source must be under 100 megapixels (error 9413); and billing counts unique variants, so
  emit transformation options in sorted order.

## Editing discipline

- For **new or large files, deliver the whole file** — find/replace on big files
  introduced errors. Use small targeted diffs only for tiny, known-safe edits.
