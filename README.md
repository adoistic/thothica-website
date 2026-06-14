# Thothica — website

The marketing site for **Thothica**, built around the data-ontology positioning: we turn fragmented knowledge into operational intelligence.

**Live:** https://thothica.com (GitHub Pages, custom domain via the `CNAME` file; the `adoistic.github.io/thothica-website` URL redirects here)

It is a single static page. No framework, no build step, no dependencies. Hand-written HTML and CSS with a few lines of vanilla JavaScript for scroll reveals. Type is set in [Fraunces](https://fonts.google.com/specimen/Fraunces) (display) and [Teachers](https://fonts.google.com/specimen/Teachers) (UI/body), served from Google Fonts. The palette is the Thothica warm brown/cream system, anchored on espresso `#2e2013`.

## Structure

```
thothica-website/
├── index.html          # the page (also holds all SEO / OG / JSON-LD head tags)
├── styles.css          # all styling (CSS variables drive the theme)
├── 404.html            # branded not-found page (served by GitHub Pages)
├── robots.txt          # crawl rules + sitemap pointer
├── sitemap.xml         # one URL (the homepage)
├── llms.txt            # plain-text site description for LLMs / AI crawlers (llmstxt.org)
├── site.webmanifest    # PWA manifest (icons, theme color)
├── assets/
│   ├── thothica-logo.png      # full logo (icon + wordmark)
│   ├── og-image.jpg           # 1200×630 social share card (WhatsApp/LinkedIn/X…)
│   ├── favicon.ico            # multi-size 16/32/48
│   ├── favicon-16.png, favicon-32.png
│   ├── apple-touch-icon.png   # 180×180, iOS home screen
│   └── icon-192.png, icon-512.png  # PWA / manifest
└── _build/             # scratch only (OG image source HTML); git-ignored
```

## Run locally

No build step. Serve the folder and open it:

```sh
python3 -m http.server 8000
# → http://localhost:8000
```

(Opening `index.html` directly works too, but a server is closer to production and lets relative paths and the manifest resolve correctly.)

## Editing copy

All page copy lives directly in `index.html`. It is the single source of truth — the wording is deliberate, so edit it there. Section anchors: `#what`, `#capabilities`, `#sectors`.

## SEO & social

Everything a crawler or a share-preview needs is already wired up in `index.html` and the root files:

- **Title + meta description**, canonical URL, `robots`, `theme-color`, author.
- **Open Graph** tags (used by WhatsApp, LinkedIn, Facebook, Slack, iMessage) pointing at `assets/og-image.jpg` (1200×630, ~56 KB — under WhatsApp's ~300 KB preview limit).
- **Twitter/X** `summary_large_image` card.
- **JSON-LD** `Organization` structured data for search engines.
- **`sitemap.xml`** + **`robots.txt`**.
- **`llms.txt`** — a clean, link-rich description of the whole site so LLMs and AI search engines can understand and "navigate" it without rendering the page.
- **Favicons** for every surface (browser tab, iOS, Android/PWA).

### Regenerating the OG share image

The card is rendered from `_build/og-image.html` with headless Chrome, then compressed:

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1200,630 --virtual-time-budget=4000 \
  --screenshot=_build/og-raw.png "file://$PWD/_build/og-image.html"
magick _build/og-raw.png -quality 86 assets/og-image.jpg
```

Tip: after changing it, re-scrape the URL in the [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) and [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) to bust their caches. WhatsApp pulls its preview from the OG tags too.

## Analytics & cookie consent

Google Analytics 4 with **Consent Mode v2** and a region-aware consent banner (`consent.js`).

**To turn it on:** set your GA4 Measurement ID in `index.html` — find:

```js
window.THOTHICA_GA_ID = 'G-XXXXXXXXXX';   // ← replace with your real ID
```

Until that's a real ID (`G-…`), nothing loads and no banner shows. To get an ID: [analytics.google.com](https://analytics.google.com) → Admin → create a GA4 property → a Web data stream for `thothica.com` → copy the Measurement ID.

**How consent works (matches the law per region):**

| Region | Behavior |
|---|---|
| EEA + UK + Switzerland (GDPR) | **Opt-in.** Analytics stays denied until the visitor clicks Accept. Enforced by IP via Consent Mode region defaults, server-side. |
| US (California CCPA/CPRA + other states) | **Opt-out.** Analytics on by default with a notice and a "Do Not Sell or Share" opt-out. Honors the browser **Global Privacy Control** signal automatically. |
| India (DPDP) + rest of world | **Notice + opt-out** (lenient). |

Region is detected client-side (GeoJS) only to choose the banner wording; if detection fails it falls back to the strict opt-in banner. The choice is stored in `localStorage` and re-openable via the **Privacy choices** link in the footer. No advertising signals are used (all `ad_*` storage denied everywhere).

## Deploy (GitHub Pages)

This repo is already on GitHub. To serve it on Pages:

1. Repo → **Settings → Pages**.
2. **Build and deployment → Source: Deploy from a branch.**
3. Branch: `main`, folder: `/ (root)`. Save.
4. Wait ~1 minute. The site goes live at `https://adoistic.github.io/thothica-website/`.

Any push to `main` re-publishes automatically.

## Connecting the custom domain (thothica.com) later

You already run a different site at `thothica.com` hosted elsewhere, so the goal is to cut over **without downtime**. Recommended order:

**1. Test on a subdomain first (zero risk to the live site).**
At your DNS provider, add a record:

```
CNAME   new.thothica.com   →   adoistic.github.io
```

In repo **Settings → Pages → Custom domain**, enter `new.thothica.com`, save (this writes a `CNAME` file to the repo). Once DNS propagates, the site is live at `https://new.thothica.com` while `thothica.com` stays untouched. Verify everything looks right.

**2. Update the base URL in the repo** (so canonical/OG/sitemap point at the real domain). Find-and-replace across `index.html`, `sitemap.xml`, `robots.txt`, and `llms.txt`:

```
https://adoistic.github.io/thothica-website   →   https://thothica.com
```

(There's a comment block at the top of `index.html` marking this.) Also update `404.html` and the manifest `start_url` paths from `/thothica-website/` to `/` since the custom domain serves from the root. Commit and push.

**3. Cut over the apex domain when ready.** Point `thothica.com` at GitHub Pages:

```
A      thothica.com   →   185.199.108.153
A      thothica.com   →   185.199.109.153
A      thothica.com   →   185.199.110.153
A      thothica.com   →   185.199.111.153
AAAA   thothica.com   →   2606:50c0:8000::153
AAAA   thothica.com   →   2606:50c0:8001::153
AAAA   thothica.com   →   2606:50c0:8002::153
AAAA   thothica.com   →   2606:50c0:8003::153
CNAME  www.thothica.com  →  adoistic.github.io
```

Remove the old host's records for the apex at the same time. Set the custom domain to `thothica.com` in Settings → Pages, then enable **Enforce HTTPS** once the certificate is issued (a few minutes to a few hours).

> Heads up: changing the apex `A`/`AAAA` records is the moment the live site switches from the old host to this one. Do it only after step 1 looks perfect on the subdomain. DNS can take up to ~24h to fully propagate, though it's usually minutes.

## Credits

Design and build by Adnan, Thothica. Logo: the Thothica ibis (after Thoth). Fonts: Fraunces and Teachers (Google Fonts, open source).
