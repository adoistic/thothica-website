#!/usr/bin/env python3
"""Stamp the case-study pages from one shared shell.

There is no build step on this site: the generated HTML is committed and served
directly. This script exists so the head, nav and footer cannot drift across
pages. Edit the body content here and re-run it; never hand-edit the output.

    python3 _build/make-case-studies.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
V = 21  # asset cache version; bump when styles.css changes

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
      <a href="/#use-cases">Use cases</a>
      <a href="/#open-source">Open source</a>
    </nav>
  </div>
</header>

<main id="main">
  <div class="wrap">
{body}
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
  "name": "Case studies",
  "description": "%s",
  "url": "https://thothica.com/case-studies/",
  "publisher": {{ "@type": "Organization", "name": "Thothica", "url": "https://thothica.com/" }}
}}"""


def crumb():
    return ('    <p class="crumb"><a href="/case-studies/">Case studies</a></p>\n')


PAGES = []

# ─────────────────────────────────────────────────────────── index
PAGES.append(dict(
    slug="", url="/case-studies/",
    title="Case studies",
    description="Five systems Thothica has built: an AI layer over five live government portals, a century-old archive mapped into a citable graph, a comic production line where every panel is sourced, an unattended newsroom, and handwritten registers turned into verified rows.",
    jsonld=INDEX_LD % "Five systems Thothica has built, across government, publishing, research and events.",
    body="""    <p class="eyebrow">Case studies</p>

    <h1>Five systems, one method.</h1>

    <p class="lede">Different industries, different data, different technology underneath. In each one the first job was the same: write down what the data means before building anything on top of it.</p>

    <p class="note">Clients are described rather than named. Named references are available under a confidentiality undertaking.</p>

    <ol class="idx">
      <li><a href="/case-studies/government-portals/">
        <span class="m">1</span>
        <span>
          <span class="idx-k">Government · five live portals</span>
          <span class="idx-t">An AI layer that reads five portals and changes none of them</span>
          <p>Five state government portals, each built on different technology and each storing its data differently. One layer, rebuilt against every schema, that answers an official's question from that portal's own records and can write nothing back.</p>
        </span>
      </a></li>
      <li><a href="/case-studies/think-tank-archive/">
        <span class="m">2</span>
        <span>
          <span class="idx-k">Think tank · historical archive</span>
          <span class="idx-t">A century of writing, mapped into something you can question</span>
          <p>Two thousand scanned PDFs became a library where you can ask who wrote about whom, on what subject, and in what words. Every claim in the map is pinned to a quotation that survives a substring check, or it is thrown away.</p>
        </span>
      </a></li>
      <li><a href="/case-studies/comic-production/">
        <span class="m">3</span>
        <span>
          <span class="idx-k">Publishing · comic production line</span>
          <span class="idx-t">Hundreds of comic books, every line traced to a source</span>
          <p>Ten million words of research turned into a navigable corpus, then into finished scripts where each beat carries a pointer to an exact line in an exact file, and a gate refuses the script if a pointer does not resolve.</p>
        </span>
      </a></li>
      <li><a href="/case-studies/cricket-content-engine/">
        <span class="m">4</span>
        <span>
          <span class="idx-k">Media · unattended newsroom</span>
          <span class="idx-t">A newsroom that runs without anyone in it</span>
          <p>An engine that reads live signals, plans its own slate, writes in the publisher's voice, checks itself against fetched sources, and stops at an editor. Its taxonomy is a declared ontology that fails the build when it is broken.</p>
        </span>
      </a></li>
      <li><a href="/case-studies/olympiad-forms/">
        <span class="m">5</span>
        <span>
          <span class="idx-k">Education · handwritten registers</span>
          <span class="idx-t">Handwritten registers into rows nobody has to re-check</span>
          <p>School registration sheets filled in by hand, read at scale, and reconciled against the paper's own arithmetic. The promise is not perfect accuracy. It is that nothing wrong ships silently.</p>
        </span>
      </a></li>
    </ol>
""",
))

# ─────────────────────────────────────────────── 1. government portals
PAGES.append(dict(
    slug="government-portals", url="/case-studies/government-portals/",
    title="An AI layer on five live government portals",
    description="Five state government portals on different technology stacks, each given a plain-language layer over its own records. The layer only reads, and every figure it reports traces back to the rows it came from.",
    jsonld=ARTICLE_LD % ("An AI layer on five live government portals",
                         "Five state government portals on different technology stacks, each given a plain-language layer over its own records.",
                         "/case-studies/government-portals/"),
    body=crumb() + """
    <h1>An AI layer that reads five portals and <em>changes none of them.</em></h1>

    <p class="lede">A state government ran five separate portals. Different departments, different purposes, different technology, and five different ideas about how to store the same kinds of facts. Officials could see their own screens. Nobody could ask a question across the records.</p>

    <div class="stats">
      <div><b>5</b><span>live portals carrying the layer</span></div>
      <div><b>4</b><span>different technologies underneath</span></div>
      <div><b>115,652</b><span>decisions made about what one portal's data meant</span></div>
      <div><b>0</b><span>writes back into any source system</span></div>
    </div>

    <h2>What was actually wrong</h2>
    <div class="sec body-w">
      <p>None of these portals were broken. Each did its job. The problem was that the meaning of the data lived outside the software, in the heads of the officers who had worked with it for years. They knew which status code really meant an application was stuck, which date field was reliable, and which table you had to join to get a number a minister could be shown.</p>
      <p>So every non-routine question became a request to a person. That person exported a spreadsheet, cleaned it by hand, and produced a figure nobody else could reproduce.</p>
    </div>

    <h2>The layer sits on top and reads down</h2>

    <div class="fig">
      <div class="layers">
        <div class="box"><span class="box-k">Where people work</span><span class="box-t">A question in plain language</span><p>An officer asks how many applications in a district are waiting on one document, and gets an answer with the rows behind it.</p></div>
        <div class="up">▲ reads only ▲</div>
        <div class="box inv"><span class="box-k">What we added</span><span class="box-t">The ontology, then the layer on it</span><p>A written record of what each measure means and every way it can legitimately be broken down: by district, by scheme, by month, by status. The layer answers from that record, not from a guess.</p></div>
        <div class="up">▲ reads only ▲</div>
        <div class="box"><span class="box-k">What already existed</span><span class="box-t">The five portals and their databases</span><p>Untouched. Same screens, same tables, same logins, same release process.</p></div>
      </div>
      <p class="fig-cap"><b>The arrows only point up.</b> The layer holds read permission and nothing else, so it cannot alter a record even if it is asked to. For a government system that is not a technical detail, it is the reason the work could be approved at all.</p>
    </div>

    <h2>What we wrote down before writing software</h2>
    <div class="sec body-w">
      <p>For each portal we built a catalogue of two things: the measures the portal actually tracks, and the dimensions each measure can be cut by. That sounds administrative. It is the whole job. Until it exists, a question like "show me pending applications by district" has no single correct answer, because two officers will disagree about what "pending" means.</p>
    </div>

    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">Step 1</span><span class="box-t">Read the schema</span><p>Every table, column and relationship in the portal's own database.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Step 2</span><span class="box-t">Write the meanings</span><p>What each measure is, in the words the department already uses, and who owns the decision it feeds.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Step 3</span><span class="box-t">Classify the free text</span><p>Complaints and remarks typed by hundreds of hands, sorted into a fixed set of categories so they can be counted.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Step 4</span><span class="box-t">Answer, with the receipt</span><p>Every figure carries the rows it came from, so a number can be defended rather than trusted.</p></div>
      </div>
      <p class="fig-cap"><b>Step 3 is where the volume is.</b> On one portal the classifiers made 115,652 separate decisions about what a piece of text meant. No team reads a quarter of a million free-text entries by hand, which is why that intelligence had never existed before.</p>
    </div>

    <h2>The part that answers "is this repeatable?"</h2>
    <div class="sec body-w">
      <p>We built this layer five times. Each portal was written in a different framework, sat on a different database engine, and modelled its domain differently. One was an old application that had to be rebuilt on a modern platform before anything could be added to it.</p>
      <p>Across all five, the sequence above did not change. What changed was the content of the catalogue, because that is the part that is specific to a department.</p>
    </div>

    <div class="tbl-scroll">
    <table class="tbl">
      <tr><th>Changed every time</th><th>Did not change once</th></tr>
      <tr><td>The database schema</td><td>Reading the schema before writing anything</td></tr>
      <tr><td>The framework and language</td><td>Writing down measures and their dimensions</td></tr>
      <tr><td>The measures a department cares about</td><td>Classifying free text into a fixed set</td></tr>
      <tr><td>The vocabulary staff use</td><td>Tracing every figure back to its rows</td></tr>
      <tr><td>What counts as a decision</td><td>Read-only by construction</td></tr>
    </table>
    </div>

    <h2>What it found that nobody asked for</h2>
    <div class="sec body-w">
      <p>Once the free text was structured, patterns appeared that no report had been built to look for. On one portal the classification surfaced a duplicate-registration signal precise enough to act on. On another, a public form had been quietly absorbing automated attack attempts for a long time; turning the logs into a structured map of who was probing what also revealed a missing rate limit.</p>
      <p>Neither was the brief. Both are what happens when data that used to be unreadable becomes countable.</p>
    </div>
""",
))

# ─────────────────────────────────────────────── 2. think tank archive
PAGES.append(dict(
    slug="think-tank-archive", url="/case-studies/think-tank-archive/",
    title="A century of writing, mapped",
    description="Two thousand scanned PDFs of a historical intellectual tradition, turned into a library you can question: who wrote about whom, on what subject, in what words. Every claim pinned to a quotation that passes a substring check.",
    jsonld=ARTICLE_LD % ("A century of writing, mapped",
                         "Two thousand scanned PDFs turned into a citable, questionable library of a historical intellectual tradition.",
                         "/case-studies/think-tank-archive/"),
    body=crumb() + """
    <h1>A century of writing, mapped into <em>something you can question.</em></h1>

    <p class="lede">A think tank held the written record of an intellectual tradition going back to the 1850s: speeches, pamphlets, books, periodicals. More than two thousand PDFs, most of them photographs of printed pages, on a website that was slow to load and impossible to search. The collection existed. The knowledge in it did not.</p>

    <div class="stats">
      <div><b>1,000+</b><span>primary works catalogued</span></div>
      <div><b>2,000+</b><span>source PDFs, mostly page scans</span></div>
      <div><b>506</b><span>writers identified and classified</span></div>
      <div><b>5</b><span>languages searchable</span></div>
    </div>

    <h2>Step one was making the pages readable at all</h2>
    <div class="sec body-w">
      <p>A scan is a picture. A search engine cannot read a picture, and neither can software that wants to know who is mentioned on page forty. So the first pass turned the pictures into text, across five languages and several scripts, including printed material old enough to have unusual typesetting.</p>
      <p>That gave us words. It did not give us knowledge, and this is where most digitisation projects stop.</p>
    </div>

    <h2>The ontology is the part that mattered</h2>

    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">Layer 1</span><span class="box-t">Works</span><p>What kind of document each item is: a speech, a pamphlet, a book, an article in a periodical. Which run or series it belongs to, and where in that run.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Layer 2</span><span class="box-t">People</span><p>Every writer, resolved to one identity across scripts, spellings and initials, so one person stays one person however a byline was printed.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Layer 3</span><span class="box-t">Relations</span><p>Who wrote what, who is the subject of what, who is mentioned inside what, and who was arguing with whom.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">Layer 4</span><span class="box-t">Positions</span><p>Where each writer sits in the tradition, on several independent axes, judged from what the collection actually shows about them.</p></div>
      </div>
      <p class="fig-cap"><b>Most archive projects build layer 1 and call it a catalogue.</b> Layers 3 and 4 are what turn a catalogue into something you can ask questions of.</p>
    </div>

    <h2>Every relation carries its own evidence</h2>
    <div class="sec body-w">
      <p>A statement like "this author engaged with that thinker" is worthless on its own, because you cannot check it. So no relation in this archive exists without the words that prove it. Each one records what kind of link it is, how confident the reading was, and the passage it came from.</p>
    </div>

    <div class="fig">
      <div>
        <div class="edge">
          <span class="ent">A 1990 booklet on India's economy</span>
          <span class="rel">cites</span>
          <span class="ent">a classical economist</span>
          <span class="ev">Evidence held with the link: the sentence warning that India must act to avoid “the disaster which Malthus had forecast for a nation multiplying itself unchecked.”</span>
        </div>
        <div class="edge">
          <span class="ent">The same booklet</span>
          <span class="rel">invokes</span>
          <span class="ent">the founder of a free-enterprise forum</span>
          <span class="ev">Evidence held with the link: the epigraph printed inside the front matter, attributed to him by name and dates.</span>
        </div>
      </div>
      <p class="fig-cap"><b>The rule that makes this trustworthy is mechanical.</b> Every quotation attached to a relation must appear verbatim in the text of the work it is drawn from. The pipeline checks each one as a substring, and any relation whose quotation fails that check is discarded rather than kept with a warning. A fabricated quotation cannot survive the step that stores it.</p>
    </div>

    <h2>Positions, on axes that stay separate</h2>
    <div class="sec body-w">
      <p>The interesting question about a tradition is not who is in it, but how. So each writer is placed on several independent axes rather than given one label: how central they are to the collection, which strand of thinking they belong to, and what they actually did for a living. Keeping the axes separate matters, because a person can be peripheral to the archive and central to the century, and a single tag would force us to pick.</p>
      <p>Each placement is recorded with the confidence behind it, and anything uncertain is flagged for a curator instead of being quietly published as fact.</p>
    </div>

    <div class="fig">
      <div class="two">
        <div class="box"><span class="box-k">Held per writer</span><span class="box-t">Three separate readings</span>
          <ul>
            <li>How central to this collection</li>
            <li>Which strand of thinking</li>
            <li>What they did: economist, editor, parliamentarian, industrialist</li>
          </ul>
        </div>
        <div class="box"><span class="box-k">Held alongside</span><span class="box-t">The audit trail</span>
          <ul>
            <li>A confidence level per axis</li>
            <li>The reasoning, in a sentence or two</li>
            <li>A review flag when any axis is uncertain</li>
          </ul>
        </div>
      </div>
      <p class="fig-cap"><b>Roughly three quarters of the writers came out of the first pass flagged for human review.</b> That is the system working. A classifier that returned confident answers for all of them would be lying about a corpus this uneven.</p>
    </div>

    <h2>The moment the method proved itself</h2>
    <div class="sec body-w">
      <p>Before running the classification across the whole collection, we tested it against a set of answers written by hand. It disagreed on several writers. When we examined the disagreements, the software was right and the hand-written answers were wrong: it had counted how often each writer was actually written about in the collection, and we had gone on reputation.</p>
      <p>We corrected our own answer key and let the run proceed. That is the argument for building the ontology from the corpus rather than from what everyone already believes.</p>
    </div>

    <h2>Two tiers, because pretending is worse than admitting</h2>
    <div class="sec body-w">
      <p>Old scans do not all read cleanly, and a confident quotation drawn from a badly read page is more damaging than no quotation at all. So the archive is explicitly split, and says which tier it is answering from.</p>
    </div>

    <div class="fig">
      <div class="two">
        <div class="box"><span class="box-k">Tier A</span><span class="box-t">Trusted text</span><p>Clean material with stable paragraph addresses. Searchable, quotable, and linkable down to the paragraph. Software may quote it directly.</p></div>
        <div class="box"><span class="box-k">Tier B</span><span class="box-t">Scanned works</span><p>Full catalogue record, a summary and its main arguments, and the original document. Software may describe it and must link out for the underlying claim rather than quote it.</p></div>
      </div>
      <p class="fig-cap"><b>The tier is part of the data, not a disclaimer in a footer.</b> Anything reading the archive can tell what it is allowed to assert, and the promotion path from Tier B to Tier A is already in the schema, so improving a scan later is a data update rather than a rebuild.</p>
    </div>

    <h2>What the researcher gets</h2>
    <div class="sec body-w">
      <p>A fast library, searchable in five languages, where a name resolves to a person rather than a spelling, where every answer points back to the page it came from, and where a question like <em>who argued with whom about free enterprise in the 1960s</em> has an answer you can follow to the paragraph.</p>
      <p>The same structure is readable by software, so a researcher's AI assistant can work from the archive directly, under the same tier rules a human gets, without a copy of the collection being handed to anyone.</p>
    </div>
""",
))

# ─────────────────────────────────────────────── 3. comic production
PAGES.append(dict(
    slug="comic-production", url="/case-studies/comic-production/",
    title="Hundreds of comic books, every line sourced",
    description="A research corpus of roughly ten million words turned into finished comic scripts where every beat points to an exact line in an exact file, and a gate refuses the script if a pointer does not resolve.",
    jsonld=ARTICLE_LD % ("Hundreds of comic books, every line sourced",
                         "A ten-million-word research corpus turned into finished comic scripts where every beat is traceable to a source line.",
                         "/case-studies/comic-production/"),
    body=crumb() + """
    <h1>Hundreds of comic books, <em>every line traced to a source.</em></h1>

    <p class="lede">One of India's largest publishers wanted comic biographies of real people, made at a pace no research team could match, and accurate enough to put a living subject's words in a speech bubble. Those two requirements pull in opposite directions. The resolution was to make provenance a mechanical gate rather than an editorial promise.</p>

    <div class="stats">
      <div><b>~10M</b><span>words of research in the corpus</span></div>
      <div><b>70+</b><span>books converted and chaptered</span></div>
      <div><b>220+</b><span>interviews transcribed</span></div>
      <div><b>48</b><span>pages, the fixed canvas per title</span></div>
    </div>

    <h2>The ontology, top to bottom</h2>
    <div class="sec body-w">
      <p>Everything in the system is one of five things, and every line the pipeline produces knows where it sits. This is what lets a new product line be added without touching the machinery.</p>
    </div>

    <div class="fig">
      <div class="layers">
        <div class="box"><span class="box-k">Level 1</span><span class="box-t">Line</span><p>A product family. Comic biographies. Classical epics. Social-awareness titles. Early-reader books.</p></div>
        <div class="up">▼ contains ▼</div>
        <div class="box"><span class="box-k">Level 2</span><span class="box-t">Program</span><p>A series inside the line. Business figures. Science figures. One epic. One awareness category.</p></div>
        <div class="up">▼ contains ▼</div>
        <div class="box"><span class="box-k">Level 3</span><span class="box-t">Subject</span><p>The person or character a book is about. One subject can spawn several books, an early-years title and a later-career title.</p></div>
        <div class="up">▼ splits into ▼</div>
        <div class="two" style="margin-top:0">
          <div class="box"><span class="box-k">Level 4 · input</span><span class="box-t">Dossier</span><p>The research. Sources, each carrying its own provenance record, and an index regenerated from the files so it can never drift from what is actually there.</p></div>
          <div class="box inv"><span class="box-k">Level 5 · output</span><span class="box-t">Comic</span><p>One script file per book, with its own metadata at the top, in a grammar a parser reads.</p></div>
        </div>
      </div>
      <p class="fig-cap"><b>The contract is uniform even where the shape is not.</b> A dossier built from converted books looks different inside from one built from authored topic notes, but both present the same three things to the tooling, so one publishing path handles every line.</p>
    </div>

    <h2>How the research gets in</h2>
    <div class="sec body-w">
      <p>Books, long interviews and video all arrive as something a machine cannot read straight: a scanned page, an audio file, a video. Each is converted to text, then split so that it can be pointed at precisely.</p>
    </div>

    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">Step 1</span><span class="box-t">Convert</span><p>Books to text. Audio and video to transcripts, marked with who is speaking and when, and tagged honestly by language including mixed-language speech.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Step 2</span><span class="box-t">Split by chapter</span><p>One file per chapter, under a chapter map that summarises each in a line. This is what makes an exact pointer possible.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Step 3</span><span class="box-t">Record provenance</span><p>Per source: where it came from, who made it, what year, and the licence position.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Step 4</span><span class="box-t">Rebuild the index</span><p>Generated from the files themselves, never hand-maintained, so the index cannot describe a library that no longer exists.</p></div>
      </div>
      <p class="fig-cap"><b>Chapter-per-file is not tidiness, it is the enabling decision.</b> Because a claim can point at a file and a line number, a script can check the pointer. Without that granularity, "cite your source" stays a slogan instead of becoming a gate.</p>
    </div>

    <h2>Finding what the subject's own books never mention</h2>
    <div class="sec body-w">
      <p>This is the part that surprises people. An authorised biography is a careful document. The vivid, candid material about someone is usually in <em>other people's</em> accounts: a rival describing them, a colleague recalling a bad decision, a mentor talking about them at nineteen.</p>
      <p>Because every subject's research sits in one corpus rather than in a separate folder, the library holds those passages already. The work is finding them, and a plain text search is not good enough to do it.</p>
    </div>

    <div class="fig">
      <div class="flow flow-3">
        <div class="box"><span class="box-k">The problem</span><span class="box-t">Names are unreliable</span><p>Transcripts mangle surnames. Speakers refer to people by their company, their team, their role, or the one event everyone remembers, and never by name. Speaker labels are sometimes simply wrong.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">The method</span><span class="box-t">Anchor on entities, read in full</span><p>Search on the name, its likely mangled forms, and the companies, teams and signature events attached to the person. Then read the passages rather than pattern-match them.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">The check</span><span class="box-t">Confirm the speaker from content</span><p>Only the person's own words count as that person speaking. Who is talking is decided from what is said, not from the label on the line. Each find is stored with its exact location and a confidence mark.</p></div>
      </div>
      <p class="fig-cap"><b>The first full sweep proved the point.</b> It surfaced a strong passage that a plain text search had missed completely, because the subject's name appeared only in the interviewer's question and never in the answer that mattered.</p>
    </div>

    <h2>The gate, and the day it taught us something</h2>
    <div class="sec body-w">
      <p>Every line of dialogue, narration and caption in a script carries a pointer to the source line behind it. Before a script moves on, a checker resolves every pointer against the actual file. If a pointer does not resolve, the script does not proceed.</p>
    </div>

    <div class="fig">
      <div class="two">
        <div class="box"><span class="box-k">What the checker does</span><span class="box-t">Resolve, or refuse</span>
          <ul>
            <li>Read every pointer in the script</li>
            <li>Open the file and the line</li>
            <li>Confirm the claim is supported there</li>
            <li>Refuse the script if any pointer fails</li>
          </ul>
        </div>
        <div class="box"><span class="box-k">What it cannot do</span><span class="box-t">Notice what is absent</span>
          <ul>
            <li>A draft with no pointers at all</li>
            <li>passes, because there is nothing to fail</li>
            <li>It reports success</li>
            <li>while guarding nothing</li>
          </ul>
        </div>
      </div>
      <p class="fig-cap"><b>This actually happened, and it is the most useful thing we learned.</b> One draft arrived with no citations in it whatsoever. The gate passed it, truthfully and uselessly. Structure that is merely present is not the same as structure that is complete, so the checker now tests for coverage as well as correctness.</p>
    </div>

    <h2>A second lesson: preparation is not a scratchpad</h2>
    <div class="sec body-w">
      <p>The quote bank assembled during research is an intermediate file, so it was treated more casually than a script. Wording that had been smoothed while making notes was later inherited into finished scripts as though it were sourced material, and one subject's words had to be un-quoted after the fact.</p>
      <p>The rule that came out of it: a preparation artefact carries the same truth burden as the final page, because the final page will trust it without asking.</p>
    </div>

    <h2>Why the page count is a creative device</h2>
    <div class="sec body-w">
      <p>A title is a fixed number of pages, and the machine enforces that the script contains exactly that many. A whole life has to fit on a canvas that cannot stretch. That constraint is what forces the narrator to compress what will not be dramatised, and it is the reason the books have a voice at all. The limit is the craft, not a restriction on it.</p>
    </div>

    <h2>What comes out</h2>
    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-t">Script</span><p>One file, fixed grammar, every beat sourced.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-t">Art</span><p>Characters and style held consistent from page to page against a locked visual specification per figure.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-t">Editorial review</span><p>A private application where the publisher's team reads each script with the source link live on every beat.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-t">Print</span><p>Print-ready files, editable text versions, and translated editions.</p></div>
      </div>
      <p class="fig-cap"><b>One grammar, one parser, three consumers.</b> The validator, the renderer and the provenance checker all read the same structure, so the editor can never be shown something different from what was checked.</p>
    </div>
""",
))

# ─────────────────────────────────────────────── 4. cricket content engine
PAGES.append(dict(
    slug="cricket-content-engine", url="/case-studies/cricket-content-engine/",
    title="A newsroom that runs unattended",
    description="An engine that reads live sport, news and forum signals, plans its own slate, writes in a publisher's voice, checks itself against fetched sources, and stops at a human editor. Its taxonomy is a declared ontology that fails the build when broken.",
    jsonld=ARTICLE_LD % ("A newsroom that runs unattended",
                         "An autonomous content engine for a sports media publisher, with a declared content ontology and a human editor as the last gate.",
                         "/case-studies/cricket-content-engine/"),
    body=crumb() + """
    <h1>A newsroom that runs <em>without anyone in it.</em></h1>

    <p class="lede">A sports media publisher needed continuous coverage: match reports within the hour, previews before play, the story a fan base is arguing about today. Hiring for that clock is expensive and still leaves the small hours uncovered. So we built an engine that works the clock, and left exactly one human decision in place.</p>

    <h2>What one cycle does</h2>

    <div class="fig">
      <ol class="steps">
        <li><span class="m">1</span><div><h3>Read the signals</h3><p>Live match data, the news wire, and where a fan base actually talks. The engine starts from what is happening rather than from a content calendar written last week.</p></div></li>
        <li><span class="m">2</span><div><h3>Plan a slate</h3><p>It decides what is worth writing right now and what kind of piece each one should be: a match report, a preview, a fan-reaction piece, a short news item. It also decides what to skip.</p></div></li>
        <li><span class="m">3</span><div><h3>Write in the house voice</h3><p>Against a written style specification rather than a general sense of tone, so a hundred articles read as one publication instead of a hundred different ones.</p></div></li>
        <li><span class="m">4</span><div><h3>Check itself</h3><p>Claims are corroborated against sources the engine actually fetches, not against memory. A piece that cannot be supported does not get emitted.</p></div></li>
        <li><span class="m">5</span><div><h3>Publish to a review portal, not to the public</h3><p>Everything lands in a private editorial portal. An editor reads it and decides. Nothing reaches readers on the engine's own authority.</p></div></li>
        <li><span class="m">6</span><div><h3>Prove it ran</h3><p>Every firing stamps a record, whatever the outcome. If the engine goes quiet, that silence raises an alarm on its own rather than being noticed a week later.</p></div></li>
      </ol>
      <p class="fig-cap"><b>Step 5 is the design decision that matters.</b> An autonomous writer with publish rights is a liability. An autonomous writer that fills an editor's queue multiplies what one editor can get out. The engine is fast; the judgement stays human.</p>
    </div>

    <h2>The taxonomy is an ontology, and it is enforced</h2>
    <div class="sec body-w">
      <p>Most publishing systems accumulate tags until nobody knows which are real. Here, how content may be categorised is declared in one manifest, and everything else in the system reads from it: the thing that resolves a writer's raw tag into a canonical one, the dashboard's filters, and the check that runs before anything ships.</p>
      <p>Each dimension declares what kind of thing it is, whether an item can have one value or several, and what should happen when a value has never been seen before. That last column is the interesting one.</p>
    </div>

    <div class="fig">
      <div class="tbl-scroll">
      <table class="tbl">
        <tr><th>Policy</th><th>When an unfamiliar value appears</th><th>Why</th></tr>
        <tr><td>Closed</td><td>The build fails</td><td>Some sets are genuinely finite. A match format is one of a known list. An invented one is a mistake, not a discovery.</td></tr>
        <tr><td>Curated</td><td>Accepted, and flagged for a human to confirm</td><td>Competitions and teams are real-world things somebody should name properly, but a story should never be blocked waiting for that.</td></tr>
        <tr><td>Auto-grow</td><td>Accepted and queued, never blocked</td><td>New players appear constantly. Refusing an unknown name would stop coverage of a debut, which is exactly the story worth having.</td></tr>
      </table>
      </div>
      <p class="fig-cap"><b>Unknown values are always accepted and always surfaced.</b> Content is never held hostage to bookkeeping, and bookkeeping never silently rots. One command reports what needs a human, and the strict dimensions fail loudly.</p>
    </div>

    <div class="fig">
      <div class="two">
        <div class="box"><span class="box-k">The problem it solves</span><span class="box-t">The same thing, six names</span><p>A writer types a team's short code, its nickname, or its full name. Left alone, one team becomes six categories and every count is wrong.</p></div>
        <div class="box inv"><span class="box-k">How</span><span class="box-t">Aliases live in the registry</span><p>Every known form of a name resolves to one identity before it is stored. The variants never fragment, so a coverage report is a real number.</p></div>
      </div>
      <p class="fig-cap"><b>This is the ontology doing ordinary, load-bearing work.</b> Nothing clever is happening. It simply cannot be skipped without every downstream count becoming fiction.</p>
    </div>

    <h2>The engine is not trusted with the keys</h2>
    <div class="sec body-w">
      <p>The machine that writes runs unattended, which means it is the least trustworthy thing in the system. It holds exactly two credentials: read access to the sport data, and permission to push its work into one repository. It holds no credential that can publish anything to the public site.</p>
      <p>Publication happens in a separate, audited step. Tests and checks run there, and a failing check stops a bad batch before an editor ever sees it. If the writing machine were fully compromised, the worst it could do is fill a queue.</p>
    </div>

    <div class="fig">
      <div class="flow flow-3">
        <div class="box"><span class="box-k">Least trusted</span><span class="box-t">The engine</span><p>Two keys: read the sport data, push to one repository. Nothing else.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Gate</span><span class="box-t">Automated checks</span><p>Tests, type checks and content validation. Holds the publishing credential. A failure stops here.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">Decides</span><span class="box-t">The editor</span><p>Reads the queue in a private portal and chooses what runs.</p></div>
      </div>
      <p class="fig-cap"><b>Blast radius is a design input, not an afterthought.</b> Autonomy is safe in proportion to how little the autonomous part is allowed to do.</p>
    </div>
""",
))

# ─────────────────────────────────────────────── 5. olympiad forms
PAGES.append(dict(
    slug="olympiad-forms", url="/case-studies/olympiad-forms/",
    title="Handwritten registers into verified rows",
    description="School registration sheets filled in by hand, read at scale and reconciled against the paper's own arithmetic. The guarantee is not perfect accuracy; it is that nothing wrong ships silently.",
    jsonld=ARTICLE_LD % ("Handwritten registers into verified rows",
                         "Handwritten school registration sheets read at scale, with deterministic verification and an explicit unverified state.",
                         "/case-studies/olympiad-forms/"),
    body=crumb() + """
    <h1>Handwritten registers into rows <em>nobody has to re-check.</em></h1>

    <p class="lede">An academic olympiad receives its registrations on paper. Schools fill in pre-printed grids and hand-ruled registers: a row per student, a tick per subject, often a handwritten total at the bottom. Thousands of sheets arrive in a season, and every one used to be typed up by a person, then checked by another person, because the data becomes a child's exam entry.</p>

    <p class="note">This is real personal information about children. The system is invite-only, source documents are stored separately from results, and deletion of stored documents is a deliberate, restricted action.</p>

    <h2>The doctrine the whole system is built on</h2>

    <div class="fig">
      <div class="two">
        <div class="box"><span class="box-k">The model does</span><span class="box-t">Perception</span><p>Look at the page. Read what is written in each cell. Report the marks, the names, the numbers as they appear. That is all it is asked to do.</p></div>
        <div class="box inv"><span class="box-k">The code does</span><span class="box-t">Arithmetic</span><p>Every sum, every reconciliation, every comparison against the sheet's own totals, every verdict. Deterministic, repeatable, inspectable.</p></div>
      </div>
      <p class="fig-cap"><b>The split exists because the two failure modes are different.</b> Misreading a smudged digit is a perception error a human would also make. Adding up wrongly is not something software should ever do, so software that can reason its way to a wrong sum is not given the job.</p>
    </div>

    <h2>The rule that makes verification mean something</h2>
    <div class="sec body-w">
      <p>Here is the subtle trap. If the same reading pass produces both the individual marks and the handwritten total, and they agree, that agreement proves nothing: a single confused reading of the page can produce a consistent, wrong answer that verifies itself.</p>
      <p>So evidence that confirms a reading has to come from somewhere independent of it. A total read in the same pass may <em>contradict</em> the marks, which is useful. It may never <em>confirm</em> them.</p>
    </div>

    <div class="fig">
      <div class="flow flow-3">
        <div class="box"><span class="box-k">Not allowed</span><span class="box-t">Self-confirmation</span><p>One pass reads the marks and the total together, they agree, the row is called verified. A coordinated misreading passes.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Allowed</span><span class="box-t">Independent corroboration</span><p>The total is read again separately, several times, and the readings are voted on. Once settled it is pinned, and later corrections are not permitted to rewrite it.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">Verdict</span><span class="box-t">Match, or say so</span><p>Agreement from an independent source is a match. No independent source is not a match; it is reported as unverified.</p></div>
      </div>
      <p class="fig-cap"><b>Absence of evidence is never green.</b> A sheet with no usable checksum and nothing to corroborate it comes back marked unverified, not marked correct. This single rule is the difference between a system that reports what it knows and one that flatters itself.</p>
    </div>

    <h2>What happens to one sheet</h2>
    <div class="fig">
      <ol class="steps">
        <li><span class="m">1</span><div><h3>Prepare the page</h3><p>The scan is straightened using the table's own printed gridlines as the reference, then reduced to a working copy. The original is kept exactly as received, byte for byte, so the source of truth is never the processed version.</p></div></li>
        <li><span class="m">2</span><div><h3>Read it</h3><p>Every row, every subject column, the names, and the handwritten total. The total gets its own separate reading and a vote across attempts.</p></div></li>
        <li><span class="m">3</span><div><h3>Reconcile</h3><p>Code recomputes each class from the marks and compares against the independently read total. Registers that continue across sheets are handled by subtracting the running figures rather than assuming each page stands alone.</p></div></li>
        <li><span class="m">4</span><div><h3>Target repairs</h3><p>Where a class does not reconcile, only the disputed part is re-read. The pinned total is not up for revision, so a repair cannot quietly move the goalposts to make itself agree.</p></div></li>
        <li><span class="m">5</span><div><h3>Deliver with verdicts</h3><p>Spreadsheet and data files out, every group carrying its verdict. Matches are usable immediately; anything flagged or unverified arrives with the reason attached.</p></div></li>
      </ol>
      <p class="fig-cap"><b>Step 4 is where most systems cheat.</b> If a correction pass is allowed to rewrite the number it is being measured against, every sheet eventually reconciles and the reconciliation is meaningless.</p>
    </div>

    <h2>Conflicts are reported, never repaired</h2>
    <div class="sec body-w">
      <p>Sometimes the paper contradicts itself: a free entry credited in one place and written somewhere else, a total that cannot be produced from any reading of the rows. The system does not choose the interpretation that makes the sheet balance. It flags the conflict and describes it, because a school's paperwork is evidence and the software is not entitled to overrule it.</p>
    </div>

    <h2>The promise we actually make</h2>
    <div class="sec body-w">
      <p>Not that the reading is perfect. Handwriting on a photocopied grid does not permit that promise, and any vendor who makes it is describing a demo.</p>
      <p>The promise is that <span class="hl">nothing wrong ships silently</span>. Every uncertain row arrives flagged, with a reason a person can act on in seconds. The work that remains for a human is triage of a short list, instead of re-typing and re-checking every sheet that came in.</p>
    </div>

    <h2>The ontology, in one sentence</h2>
    <div class="sec body-w">
      <p>Pages belong to sheets, sheets belong to register runs that can continue across pages, rows group into classes, and every group carries a verdict with the evidence behind it. Once that structure is written down, verification stops being a judgement call and becomes arithmetic, which is the only kind of check that holds up when the volume is thousands of sheets a season.</p>
    </div>
""",
))


def main():
    for p in PAGES:
        out = ROOT / "case-studies" / p["slug"] / "index.html" if p["slug"] else ROOT / "case-studies" / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        html = SHELL.format(
            title=p["title"], description=p["description"], url=p["url"],
            v=V, jsonld=p["jsonld"], body=p["body"].rstrip() + "\n",
        )
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}  ({len(html.splitlines())} lines)")


if __name__ == "__main__":
    main()
