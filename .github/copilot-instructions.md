# Copilot instructions for licoproj

Short actionable guidance to get productive fast in this monorepo. Key app: `packages/licoimg` (Vite + Vanilla JS) — fully client-side.

## Key files & directories
- `packages/licoimg/src/main.js` — core app logic and UI state (`state`, `renderGallery`, `openLightbox`)
- `packages/licoimg/index.html` — DOM (ids referenced in `main.js`), `style.css` for visuals
- `packages/licoimg/vite.config.js` — base path = `/licoimg/`, build `outDir: 'docs'`
- `.agent/` — agent rules, commit guidelines, conventions; read before PR
- `.github/workflows/jekyll-gh-pages.yml` — production deploy copies `packages/licoimg/docs` → `_site`

## Quick dev & deploy
- `npm install` (root)
- `npm run dev` → serve `packages/licoimg` locally (usually `http://localhost:5173`)
- `npm run build` → production output to `packages/licoimg/docs/`
- `npm run preview` → preview production build
- GH Pages action copies `packages/licoimg/docs` into `_site` (see `.github/workflows/jekyll-gh-pages.yml`)

## Conventions & patterns
- No frameworks — direct DOM API. Pattern: read `state` → mutate → call `renderGallery()`/`openLightbox()`.
- `state.images` holds items; each item: `{src, name, type, id}` where id is `Date.now() + Math.random()`.
- Files are added via `handleFiles()`; `FileReader` stores Data URLs (in-memory). Keep privacy and avoid uploads.
- Video handling is separate: `lightbox-video` is used and zoom/pan is disabled for videos.
- Use Prettier settings in `.vscode/.prettierrc.toml`.

## Changes & features
- For UI additions, edit `index.html` and add event bindings in `main.js`; prefer discrete functions for new interactions.
- For a toolbar example: add HTML in `index.html`, then get element by ID in `main.js` and register event listeners — mutate `state` and call `renderGallery()` or update `openLightbox()` as appropriate.
- New dependencies: add to root `package.json` and run `npm install`; prefer no runtime deps unless unavoidable.

## Quick example: persistent storage
Add this near `main.js` initialization to persist `state.images`:
```js
const persisted = localStorage.getItem('licoimg.images');
if (persisted) state.images = JSON.parse(persisted);
// After adding files:
localStorage.setItem('licoimg.images', JSON.stringify(state.images));
```

## Performance & security
- Data URLs use memory — avoid loading many huge files. Consider `createObjectURL()` or downscaling if needed.
- Keep client-only behavior — do not add server credentials or trackers.

## Tests & CI
- There are currently no frontend unit tests. If adding tests, create `packages/licoimg/test/` and use a JS test runner (e.g., `vitest`) and update root `package.json` accordingly.
- Run Prettier before PRs (settings in `.vscode/.prettierrc.toml`).

## Commits & PRs
- Use `.agent/workflows/commit.md` rules (English only): `Type: Subject` (e.g., `Feat: Add toolbar for rotation`).
- Keep changes atomic; run `npm run dev` and `npm run build` locally before PR.

## Quick searches
- `renderGallery`, `openLightbox`, `state.images`, `handleFiles`.

## What to avoid
- No server-side logic; preserve client-only nature. If adding backend behavior, add a clear service boundary and update workflows.
- Do not modify `docs/` layout without updating the deploy action.

## Questions & clarifications
If behavior is unclear, review `packages/licoimg/README.md`, `.agent/` rules, and `index.html`. Ask for clarifications in PR descriptions.

---
Thanks — ask to iterate on any part you want expanded.
