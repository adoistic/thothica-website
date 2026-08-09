"""The one page shell every generated page is stamped from.

Both generators import this, so the head, nav and footer cannot drift apart.
Bump V whenever styles.css changes.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
V = 24

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<title>{title} · Thothica</title>
<meta name="description" content="{description}" />
<link rel="canonical" href="https://thothica.com{url}" />
<meta name="robots" content="index, follow" />
<meta name="theme-color" content="#000000" />
<meta name="author" content="Thothica" />

<link rel="icon" href="/assets/favicon.ico?v={v}" sizes="any" />
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png?v={v}" />
<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16.png?v={v}" />
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png?v={v}" />
<link rel="manifest" href="/site.webmanifest?v={v}" />

<meta property="og:type" content="article" />
<meta property="og:site_name" content="Thothica" />
<meta property="og:title" content="{title} · Thothica" />
<meta property="og:description" content="{description}" />
<meta property="og:url" content="https://thothica.com{url}" />
<meta property="og:image" content="https://thothica.com/assets/og-image.jpg" />
<meta property="og:image:type" content="image/jpeg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:locale" content="en_US" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title} · Thothica" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="https://thothica.com/assets/og-image.jpg" />

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Teachers:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/styles.css?v={v}" />
<script>document.documentElement.className += ' js';</script>

<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="top">
  <div class="wrap nav">
    <a class="nav-logo" href="/" aria-label="Thothica home"><img src="/assets/thothica-logo-black.png" alt="Thothica" width="383" height="110" /></a>
    <button class="nav-burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav-links">
      <span></span><span></span><span></span>
    </button>
    <nav id="nav-links" aria-label="Sections">
      <a href="/case-studies/">Case studies</a>
      <a href="/use-cases/">Use cases</a>
      <a href="/#open-source">Open source</a>
    </nav>
  </div>
</header>

<main id="main">
  <div class="wrap">
    <div class="doc">
{body}
    </div>
  </div>
</main>

<section class="cta">
  <div class="wrap">
    <p>Tell us your hardest problem. <em>We will solve it.</em></p>
  </div>
</section>

<footer>
  <div class="wrap">
    <img src="/assets/thothica-logo-white.png" alt="Thothica" width="383" height="110" />
    <a class="mail" href="mailto:hello@thothica.com">hello@thothica.com</a>
    <p class="fine">Thothica Private Limited · New Delhi<button id="cookie-prefs" class="consent-manage" type="button" style="display:none">Privacy choices</button></p>
  </div>
</footer>

<script>
(function(){{
  var nav = document.querySelector('.nav');
  var btn = nav && nav.querySelector('.nav-burger');
  if (!btn) return;
  function set(open){{
    nav.classList.toggle('open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }}
  btn.addEventListener('click', function(){{ set(!nav.classList.contains('open')); }});
  nav.querySelectorAll('nav a').forEach(function(a){{
    a.addEventListener('click', function(){{ set(false); }});
  }});
  document.addEventListener('keydown', function(e){{
    if (e.key === 'Escape' && nav.classList.contains('open')) {{ set(false); btn.focus(); }}
  }});
}})();
</script>
</body>
</html>
"""

ARTICLE_LD = """{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "%s",
  "description": "%s",
  "url": "https://thothica.com%s",
  "publisher": {{ "@type": "Organization", "name": "Thothica", "url": "https://thothica.com/" }},
  "author": {{ "@type": "Organization", "name": "Thothica" }},
  "isAccessibleForFree": true
}}"""

INDEX_LD = """{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "%s",
  "description": "%s",
  "url": "https://thothica.com%s",
  "publisher": {{ "@type": "Organization", "name": "Thothica", "url": "https://thothica.com/" }}
}}"""

REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Moved · Thothica</title>
<link rel="canonical" href="https://thothica.com{to}" />
<meta name="robots" content="noindex" />
<meta http-equiv="refresh" content="0; url={to}" />
</head>
<body><p>This page has moved to <a href="{to}">{to}</a>.</p></body>
</html>
"""


def write(section, slug, title, description, url, jsonld, body):
    out = ROOT / section / slug / "index.html" if slug else ROOT / section / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    html = SHELL.format(title=title, description=description, url=url, v=V,
                        jsonld=jsonld, body=body.rstrip() + "\n")
    out.write_text(html, encoding="utf-8")
    return out


def write_redirect(path, to):
    out = ROOT / path / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(REDIRECT.format(to=to), encoding="utf-8")
    return out
