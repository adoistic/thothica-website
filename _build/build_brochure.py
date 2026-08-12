#!/usr/bin/env python3
"""Builds the Thothica capability brochure in two forms from one source of truth:

  thothica-brochure.html  ->  printed to thothica-brochure.pdf (for people)
  thothica-brochure.md    ->  the same content as text (for AI agents)

Run from the repo root:  python3 _build/build_brochure.py
Then print the PDF with the command printed at the end.
"""
import base64, os, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
b64 = lambda p: 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
LB, LW = b64('assets/thothica-logo-black.png'), b64('assets/thothica-logo-white.png')

# ── content, written once, rendered twice ───────────────────────────────────
LAYERS = [
 ('L1', 'Ontology', 'We write down what your data means',
  'Our software reads the systems you already run and writes the first draft: what each record is, how it '
  'links to the others, and who has to sign off. We set the rules it follows and check what it produces. '
  'You end up with one document your staff can read and your software can execute.',
  ['SAP','Oracle','PostgreSQL','SQL Server','SharePoint','Excel','Tally','Scanned PDFs','Legacy portals','Paper registers']),
 ('L2', 'Agents and engineers', 'We sit with your experts, in software or in person',
  'Much of what decides an outcome was never written down anywhere. It is in the head of the officer who '
  'has done the job for eleven years. Forward deployed agents are software that works through the systems '
  'your people already use. Forward deployed engineers are our own people, in your building, writing the '
  'same structure by hand where software cannot reach. Which of the two we send depends on the engagement, '
  'and on some it is both.',
  ['Revenue officers','Archivists','Procurement staff','Draftsmen','Editors','Examiners','Registrars','Curators']),
 ('L3', 'Application', 'We build the system your staff work in',
  'Either we build it, or we put the layer inside the software you already use. Either way your staff get '
  'an answer they can act on, with the source record attached to it.',
  ['A single-window portal','A case file system','An editorial queue','An officer dashboard','An open API','A layer inside your ERP']),
 ('L4', 'Operation', 'We run it, and we keep running it',
  'Five government portals, a hundred-year-old archive, a publishing line and a newsroom engine are live on '
  'this stack right now, and we operate them. We do not hand over the code and leave.',
  ['5 government portals','115,652 records classified','2,000+ works catalogued','10M words of research']),
]

CASES = [
 ('Government', 'Five Portals, One Read-Only AI Layer',
  'A state government ran five portals on different technology, each with its own idea of how to store the '
  'same facts. Officials could see their own screens. Nobody could ask a question across the records.',
  'A question goes to the officer who knows. They export a spreadsheet, clean it by hand, and produce a '
  'figure nobody else can reproduce.',
  'A question goes to the layer. It answers from that portal’s own rows, and every figure opens the '
  'records it was built from.',
  [('115,652','records classified on one portal'), ('5','live portals carrying the layer'),
   ('4','different technologies underneath'), ('0','writes back into any source system')],
  'For each portal we first wrote down what its data measures and every way it can legitimately be broken '
  'down, then classified the free-text fields into a fixed set so they could be counted. The layer holds '
  'read permission only. It cannot alter a record even if it is asked to.'),
 ('Think tank', 'A Century of Writing, Searchable by Who Said What',
  'A think tank held the written record of a tradition going back to the 1850s: more than two thousand PDFs, '
  'most of them photographs of printed pages, on a site that was slow to load and impossible to search.',
  'Two thousand PDFs of photographed pages. The collection existed; the knowledge in it did not.',
  'Ask who wrote about whom, on what subject and in what words. Every relation carries the passage that '
  'proves it.',
  [('1,000+','historical works catalogued'), ('506','writers resolved to one identity each'),
   ('5','languages read across several scripts'), ('2','declared trust tiers')],
  'Every relation carries the verbatim passage that proves it, checked as a substring of the source text. A '
  'relation whose quotation fails that check is discarded rather than kept with a warning, so a fabricated '
  'quotation cannot survive storage.'),
 ('Publishing', 'Graphic Stories at Scale, Every Line Traced to a Source',
  'One of India’s largest publishers wanted graphic stories faster than any studio could make them, and '
  'accurate enough to put a living person’s words in a speech bubble.',
  'Pace and accuracy pull against each other, and provenance is a promise somebody has to keep by hand.',
  'Provenance is a mechanical gate. Every beat points at a source line, and the gate resolves each pointer '
  'before the script proceeds.',
  [('10M','words in the research corpus'), ('70+','books converted and chaptered'),
   ('220+','interviews transcribed'), ('5','publishing lines on one pipeline')],
  'Sources are split chapter per file so a claim can point at an exact file and line. Art is generated '
  'against locked visual specifications per figure, and ships both as press-ready separated colour and as '
  'editable pages in the book’s own lettering.'),
 ('Media', 'A Newsroom That Runs Unattended and Publishes Nothing',
  'A sports publisher needed coverage on a clock that never stops. Hiring for that clock is expensive and '
  'still leaves the small hours uncovered.',
  'Continuous coverage means hiring for a clock that never stops, and the small hours stay uncovered anyway.',
  'The engine works the clock and stops at an editorial queue. It holds no credential that can publish.',
  [('0','credentials that can publish'), ('1','manifest every consumer reads from'),
   ('3','kinds of taxonomy dimension'), ('1','human decision left in place')],
  'The engine reads live signals, plans its own slate, writes against a written style specification and '
  'corroborates its claims against sources it actually fetches. Then it stops. On its worst day it fills a '
  'queue rather than embarrassing the masthead.'),
 ('Education', 'Handwritten Registers Turned Into Verified Rows',
  'An academic olympiad receives registrations on paper: a row per student, a tick per subject, a handwritten '
  'total at the bottom. Thousands of sheets a season, every one typed up and checked by hand.',
  'Every sheet typed up by one person, then checked by a second, because the data becomes a child’s exam entry.',
  'A model reads the page and code does every sum. Anything it cannot verify comes back marked unverified, '
  'never marked correct.',
  [('2','independent readings of each total'), ('3','verdicts, one of them silent'),
   ('0','sums done by the model'), ('100%','of conflicts reported, never repaired')],
  'The doctrine is that the model does perception and the code does arithmetic. Evidence that confirms a '
  'reading must come from a source independent of it, so the same reading is never used to check itself.'),
]

USES = [
 ('Archives, libraries, museums', 'Collections That Answer Questions',
  'Manuscripts and oral history captured properly, a public platform over the collection, an open interface '
  'any AI can read under your rules, and a picture of who actually cites you.'),
 ('Government', 'A Different Use Case per Department',
  'Industry, revenue, procurement, drafting, disaster management, local bodies, constituency offices and '
  'public sector oversight. Each has its own problem, and each gets its own first deliverable.'),
 ('Media and publishing', 'From Research to a Story Ready to Run',
  'Coverage that stops at an editor, a research desk that turns documents into angles, analytics that answer '
  'editorial questions, and discourse measured claim by claim.'),
 ('Legal practices', 'The Office Keeps Its Judgement',
  'Judgments translated to filing standard under a glossary that is binding, case files structured into '
  'positions and authorities, and conflicting authority surfaced across a body of law.'),
 ('Defence and security', 'Runs Where Nothing May Leave the Building',
  'Doctrine and standing orders made answerable, assessment that keeps source reliability separate from what '
  'was reported, and every part able to run fully disconnected.'),
 ('AI companies and labs', 'Messy Material Turned Into Training-Grade Structure',
  'Domain corpora typed and given provenance with the licence position recorded, plus evaluation sets a model '
  'cannot already have memorised.'),
]

STEPS = {'Five Portals, One Read-Only AI Layer': [('Catalogue', 'For each portal, what its data measures and every legitimate way it can be broken down: by district, by scheme, by month, by status.'), ('Classify', 'Free-text fields sorted into a fixed set so they can be counted. On one portal that was 115,652 separate decisions about what a piece of text meant.'), ('Answer', 'An official asks in plain language. The answer is assembled from that portal’s own rows.'), ('Trace', 'Every figure opens the records it was built from, so a number can be defended in the room.')], 'A Century of Writing, Searchable by Who Said What': [('Read', 'Photographs of printed pages turned into text across five languages and several scripts.'), ('Resolve', '506 writers matched to one identity each, across scripts, spellings and initials.'), ('Relate', 'Who wrote what, who is the subject of what, who is mentioned inside what, who argued with whom.'), ('Prove', 'Every relation carries the verbatim passage, checked as a substring of the source text.')], 'Graphic Stories at Scale, Every Line Traced to a Source': [('Corpus', '70+ books and 220+ interviews, split chapter per file so a claim can point at an exact line.'), ('Script', 'Every beat in the finished script carries a pointer to the source line behind it.'), ('Gate', 'The gate resolves each pointer before the script proceeds. A broken pointer stops the book.'), ('Art', 'Characters and pages generated against locked visual specifications, shipped press-ready.')], 'A Newsroom That Runs Unattended and Publishes Nothing': [('Read', 'Live match data, the news wire and fan forums, on a clock that never stops.'), ('Plan', 'The engine plans its own slate against a taxonomy declared in one manifest.'), ('Write', 'In the publisher’s voice, against a written style specification, checked against sources it fetches.'), ('Stop', 'Everything lands in a private queue. An editor decides what runs.')], 'Handwritten Registers Turned Into Verified Rows': [('Transcribe', 'A vision model reads what is actually on the paper, and does nothing else.'), ('Recompute', 'Code recomputes each class from the marks. The model does no arithmetic at all.'), ('Reconcile', 'Compared against the handwritten total, read independently and pinned so a later repair cannot move it.'), ('Verdict', 'Verified, conflicted, or unverified. A sheet with nothing to check against is never called correct.')]}

GOVDEPTS = [
 ('Industry','What each scheme really requires, and in what order','Investors wait on officers who know','An eligibility model behind the single window'),
 ('Revenue','Which patterns in the register indicate a leak','The same leak is found again every year','Rules as code, each citing its statute'),
 ('Procurement','What a suspicious award looks like across a body of tenders','Only single files get read','A detection grid over published fields'),
 ('Drafting','Which instruments contradict which','Conflicts surface in litigation','Obligations typed and compared'),
 ('Disaster','Who must act on a given warning, and by when','The map lives with experienced officers','Warnings that produce an owned task list'),
 ('Local bodies','What is pending, and with whom','A diary and a chat thread','Nothing exists without an owner and a date'),
 ('PSU oversight','Which bodies overlap in mandate','Suspected, never evidenced','A roster where every value opens its source'),
]

# ── HTML rendering ──────────────────────────────────────────────────────────
def foot(inv=False):
    """Content pages only. The section name already sits in the header, so the
    footer carries just the mark and the page number."""
    return (f'<div class="foot"><img src="{LW if inv else LB}" alt="Thothica"/>'
            f'<span class="pg"></span></div>')

def slide(inner, label='', inv=False, bare=False):
    """bare=True for the front and back covers: no header rule, no footer."""
    tail = '' if bare else foot(inv)
    return f'<section class="slide{" inv" if inv else ""}{" bare" if bare else ""}">{inner}{tail}</section>'

def chips(xs):
    return '<div class="chips">' + ''.join(f'<span>{x}</span>' for x in xs) + '</div>'

def statgrid(pairs, cols=4):
    cells = ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in pairs)
    return f'<div class="stats" style="grid-template-columns:repeat({cols},1fr)">{cells}</div>'

pages = []

# 1 cover
pages.append(slide(f'''<div class="frame">
  <div class="head"><img class="cover-mark" src="{LW}" alt="Thothica"/>
    <p class="eb" style="margin-top:26px">An AI startup &middot; Data ontology</p></div>
  <div class="fill" style="justify-content:center">
    <h1>AI Systems for Institutions That Run on Records.</h1>
    <p class="lede" style="margin-top:26px;max-width:50ch">We write the ontology, send the agents that fill it,
      and build the system your staff work in. Then we run it.</p>
    <p class="narr" style="margin-top:32px">Four layers, one company.</p>
  </div>
  {statgrid([('5','government portals running our AI layer'),('115,652','records classified on one of those portals'),
             ('1,000+','historical works mapped and searchable'),('10M','words of research made usable')])}
</div>''', inv=True, bare=True))

# 2 the stack
rail = ''.join(
  f'<li><span class="n">{n}</span><div><span class="eb">{k}</span>'
  f'<h3 style="margin-top:3px">{h}</h3><p>{p}</p>{chips(c)}</div></li>'
  for n, k, h, p, c in LAYERS)
pages.append(slide(f'''<div class="frame">
  <div class="head"><p class="eb">01 &middot; The stack</p>
    <h2 style="margin-top:9px">Four Layers, All of Them Ours</h2>
    <p style="margin-top:11px;max-width:64ch">This is normally four separate suppliers, plus a systems
      integrator hired to connect them. We do all four parts ourselves.</p></div>
  <div class="fill" style="margin-top:18px"><ol class="rail">{rail}</ol></div>
</div>''', 'The stack'))

# 3 what an ontology is
pages.append(slide('''<div class="frame">
  <div class="head"><p class="eb">02 &middot; The discipline</p>
    <h2 style="margin-top:9px">What an Ontology Is</h2></div>
  <div class="fill" style="margin-top:16px">
    <p style="max-width:66ch">Ask two departments what a pending case is and you will get two answers. Both are
      right, because each was defined for a different purpose years ago, and neither definition was ever written
      down. So the two produce different numbers and nobody can say which one is correct.</p>
    <p style="max-width:66ch;margin-top:11px">An ontology closes it. It is a plain document that says what each
      thing is, which one is the real number, and who decides.</p>
    <div class="flow3" style="margin-top:24px">
      <div class="box"><span class="bk">Data sources</span><span class="bt">What you have</span>
        <p>Scanned PDFs. Spreadsheets. Databases. Old systems still in use. SAP and other enterprise software.
          Wherever your data sits, we write the connection to it. Nothing is moved or re-typed.</p></div>
      <div class="arw"></div>
      <div class="box"><span class="bk">Logic sources</span><span class="bt">What you know</span>
        <p>Formulas buried in spreadsheets. Code you already run. Written rules. Much of it is in no system at
          all: agents and engineers sit with your experts and write it down in the same structure.</p></div>
      <div class="arw"></div>
      <div class="box fillin"><span class="bk">Systems of action</span><span class="bt">What you do</span>
        <p>Your ERP. Your existing portals. A new system we build. An AI agent. The result is a step someone
          can actually carry out, with the record it came from attached.</p></div>
    </div>
    <p class="narr" style="margin-top:20px;max-width:54ch">Those three parts together are the ontology. It is kept
      in one place, in one structure, and both your staff and your software read it.</p>
    <div style="margin-top:auto">
      <p class="eb" style="margin-bottom:9px">Why the method repeats</p>
      <p style="max-width:66ch">Four unrelated industries. No two of them stored their data the same way. We
        rebuilt the same layer against each one, and the method did not change.</p>
    </div>
  </div>
</div>''', 'What an ontology is'))

# 4..8 case studies, one page each
for sector, title, lede, before, after, stats, note in CASES:
    chain = ''.join(f'<li><span class="n">{i+1}</span><div><h3>{a}</h3><p>{b}</p></div></li>'
                    for i, (a, b) in enumerate(STEPS[title]))
    pages.append(slide(f'''<div class="frame">
      <div class="head"><p class="eb">03 &middot; Case study &middot; {sector}</p>
        <h2 style="margin-top:9px">{title}</h2>
        <p class="lede" style="margin-top:12px;max-width:62ch">{lede}</p></div>
      <div class="fill" style="margin-top:20px">
        {statgrid(stats)}
        <div class="two" style="margin-top:24px">
          <div class="box"><span class="bk">Before</span><span class="bt">How it worked</span><p>{before}</p></div>
          <div class="box fillin"><span class="bk">After</span><span class="bt">How it works now</span><p>{after}</p></div>
        </div>
        <div style="margin-top:26px">
          <p class="eb" style="margin-bottom:10px">How it runs</p>
          <ol class="chain">{chain}</ol>
        </div>
        <div style="margin-top:auto">
          <p class="eb" style="margin-bottom:8px">The rule underneath</p>
          <p style="max-width:70ch">{note}</p>
        </div>
      </div>
    </div>''', f'Case study &middot; {sector}'))

# 9 use cases
cells = ''.join(
  f'<div class="box"><span class="bk">{k}</span><span class="bt">{t}</span><p>{d}</p></div>'
  for k, t, d in USES)
pages.append(slide(f'''<div class="frame">
  <div class="head"><p class="eb">04 &middot; Use cases</p>
    <h2 style="margin-top:9px">Built to Order, by Institution</h2>
    <p style="margin-top:11px;max-width:64ch">Grouped by the institution asking. These are capabilities, not
      finished projects.</p></div>
  <div class="fill" style="margin-top:20px">
    <div class="two" style="grid-auto-rows:1fr;gap:12px">{cells}</div>
  </div>
</div>''', 'Use cases'))

# 10 government detail
rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in GOVDEPTS)
pages.append(slide(f'''<div class="frame">
  <div class="head"><p class="eb">04 &middot; Use cases &middot; Government</p>
    <h2 style="margin-top:9px">A Different Use Case per Department</h2>
    <p style="margin-top:11px;max-width:66ch">A revenue department and a disaster management authority share
      nothing in subject matter and one thing underneath: the rules that decide an outcome are written
      somewhere no software can read.</p></div>
  <div class="fill" style="margin-top:20px">
    <table><thead><tr><th>Department</th><th>Written down nowhere</th><th>What that costs today</th>
      <th>First deliverable</th></tr></thead><tbody>{rows}</tbody></table>
    <div style="margin-top:auto">
      <p class="eb" style="margin-bottom:8px">Sequencing</p>
      <p style="max-width:66ch">Start with registers the department already owns. Anything that needs another
        agency’s cooperation comes last and is marked optional, because most government data projects stall in
        a memorandum between two agencies.</p>
    </div>
  </div>
</div>''', 'Use cases &middot; Government'))

# 11 open source
pages.append(slide('''<div class="frame">
  <div class="head"><p class="eb">05 &middot; Open source</p>
    <h2 style="margin-top:9px">The Method, in Public</h2>
    <p style="margin-top:11px;max-width:64ch">We publish the method where anyone can inspect it.</p></div>
  <div class="fill" style="margin-top:22px">
    <div class="three">
      <div class="box"><span class="bk">Open library</span><span class="bt">Falsafa.ai</span>
        <p>Our open library of the world’s philosophical, classical and religious texts: more than 2,000 works
          split into more than 1.3 million passages that can each be quoted and cited exactly.</p></div>
      <div class="box"><span class="bk">Built on top of it</span><span class="bt">The Atlas</span>
        <p>A map of the collection drawn from the texts themselves: the people, ideas, places, groups and events
          across twenty-five centuries, and every time one text cites another, including whether the later
          author agreed or argued back.</p></div>
      <div class="box fillin"><span class="bk">The rule underneath</span><span class="bt">It cannot invent a quotation</span>
        <p>The software that builds the Atlas is not allowed to write quotations. It can only point at
          paragraphs, and the words are attached afterwards from the source text.</p></div>
    </div>
    <div style="margin-top:26px">
      <p class="eb" style="margin-bottom:10px">What is in it today</p>
      ''' + statgrid([('2,018','works in the library'), ('1.3M','passages addressable'),
                      ('36,472','entities in the Atlas'), ('363,042','verbatim quotations')]) + '''
    </div>
    <p class="narr" style="margin-top:auto;max-width:52ch">Thothica works with some of India’s largest publishers,
      with state governments, and with leading think tanks and small businesses.</p>
  </div>
</div>''', 'Open source'))

# 12 the ask
pages.append(slide(f'''<div class="frame">
  <div class="head"><img class="cover-mark" src="{LW}" alt="Thothica"/></div>
  <div class="fill" style="justify-content:center">
    <p class="eb">Get in touch</p>
    <h1 style="margin-top:18px;max-width:16ch">Tell us your hardest problem.</h1>
    <p class="lede" style="margin-top:24px;max-width:52ch">If the rules that decide an outcome in your
      organisation are written somewhere no software can read, that is the problem we solve. Send us a
      description of it and we will tell you what it would take.</p>
    <div style="margin-top:38px">
      <p class="eb" style="margin-bottom:9px">Thothica Private Limited</p>
      <p style="font-size:20px;font-weight:700">hello@thothica.com</p>
      <p style="margin-top:6px">thothica.com &nbsp;&middot;&nbsp; New Delhi, India</p>
    </div>
    <p style="margin-top:34px;max-width:60ch;font-size:12px">Clients are described rather than named in this
      document. Named evidence is available under a confidentiality undertaking.</p>
  </div>
</div>''', inv=True, bare=True))

html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<title>Thothica &middot; capability brochure</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500'
        '&family=Teachers:ital,wght@0,400;0,500;0,600;0,700&display=block" rel="stylesheet">'
        '<link rel="stylesheet" href="brochure.css">'
        '<style>body{counter-reset:pg}.slide{counter-increment:pg}.pg:after{content:counter(pg)}</style>'
        '</head><body>' + '\n'.join(pages) + '</body></html>')
open('_build/brochure.html', 'w').write(html)
print('brochure.html:', len(pages), 'pages')

# ── Markdown rendering, same content, for agents ────────────────────────────
def md_stats(pairs):
    return '\n'.join(f'- **{a}** {b}' for a, b in pairs)

M = []
M.append('# Thothica: capability brochure\n')
M.append('> AI systems for institutions that run on records. We write the ontology, send the agents that '
         'fill it, and build the system your staff work in. Then we run it.\n')
M.append('Thothica Private Limited, New Delhi, India. Founded 2023. Contact: hello@thothica.com · '
         'https://thothica.com\n')
M.append('This file is the same brochure the PDF contains, written as plain text so it can be handed to an '
         'assistant. Clients are described rather than named. Named evidence is available under a '
         'confidentiality undertaking.\n')
M.append('## At a glance\n')
M.append(md_stats([('5','government portals running our AI layer'),
                   ('115,652','records classified on one of those portals'),
                   ('1,000+','historical works mapped and searchable'),
                   ('10M','words of research made usable')]) + '\n')

M.append('## 01. The stack: four layers, all of them ours\n')
M.append('This is normally four separate suppliers, plus a systems integrator hired to connect them. '
         'We do all four parts ourselves.\n')
for n, k, h, p, c in LAYERS:
    M.append(f'### {n}. {k}: {h}\n\n{p}\n\n*{k} works with:* ' + ', '.join(c) + '\n')

M.append('## 02. The discipline: what an ontology is\n')
M.append('Ask two departments what a pending case is and you will get two answers. Both are right, because '
         'each was defined for a different purpose years ago, and neither definition was ever written down. '
         'So the two produce different numbers and nobody can say which one is correct.\n')
M.append('An ontology closes it. It is a plain document that says what each thing is, which one is the real '
         'number, and who decides. It has three parts:\n')
M.append('1. **Data sources, what you have.** Scanned PDFs, spreadsheets, databases, old systems still in '
         'use, SAP and other enterprise software. Wherever your data sits we write the connection to it. '
         'Nothing is moved or re-typed.\n'
         '2. **Logic sources, what you know.** Formulas buried in spreadsheets, code you already run, '
         'written rules. Much of it is in no system at all: agents and engineers sit with your experts and '
         'write it down in the same structure.\n'
         '3. **Systems of action, what you do.** Your ERP, your existing portals, a new system we build, or '
         'an AI agent. The result is a step someone can actually carry out, with the record it came from '
         'attached.\n')
M.append('Those three parts together are the ontology. It is kept in one place, in one structure, and both '
         'your staff and your software read it.\n')
M.append('**Why the method repeats.** Four unrelated industries. No two of them stored their data the same '
         'way. We rebuilt the same layer against each one, and the method did not change.\n')

M.append('## 03. Case studies: five systems in production\n')
for sector, title, lede, before, after, stats, note in CASES:
    M.append(f'### {title}\n\n*Sector: {sector}*\n\n{lede}\n')
    M.append(md_stats(stats) + '\n')
    M.append(f'**Before.** {before}\n\n**After.** {after}\n')
    M.append('**How it runs.**\n\n' + '\n'.join(
        f'{i+1}. **{a}.** {b}' for i, (a, b) in enumerate(STEPS[title])) + '\n')
    M.append(f'**The rule underneath.** {note}\n')

M.append('## 04. Use cases: built to order, by institution\n')
M.append('Grouped by the institution asking. These are capabilities, not finished projects.\n')
for k, t, d in USES:
    M.append(f'### {t}\n\n*For: {k}*\n\n{d}\n')
M.append('### Government, department by department\n')
M.append('| Department | Written down nowhere | What that costs today | First deliverable |\n'
         '| --- | --- | --- | --- |\n' +
         '\n'.join(f'| {a} | {b} | {c} | {d} |' for a, b, c, d in GOVDEPTS) + '\n')
M.append('**Sequencing.** Start with registers the department already owns. Anything that needs another '
         'agency’s cooperation comes last and is marked optional, because most government data projects '
         'stall in a memorandum between two agencies.\n')

M.append('## 05. Open source: the method, in public\n')
M.append('- **Falsafa.ai.** Our open library of the world’s philosophical, classical and religious texts: '
         'more than 2,000 works split into more than 1.3 million passages that can each be quoted and cited '
         'exactly.\n'
         '- **The Atlas.** A map of the collection drawn from the texts themselves: the people, ideas, '
         'places, groups and events across twenty-five centuries, and every time one text cites another, '
         'including whether the later author agreed or argued back.\n'
         '- **It cannot invent a quotation.** The software that builds the Atlas is not allowed to write '
         'quotations. It can only point at paragraphs, and the words are attached afterwards from the '
         'source text.\n')
M.append(md_stats([('2,018','works in the library'), ('1.3M','passages addressable'),
                   ('36,472','entities in the Atlas'), ('363,042','verbatim quotations')]) + '\n')
M.append('Thothica works with some of India’s largest publishers, with state governments, and with leading '
         'think tanks and small businesses.\n')

M.append('## Get in touch\n')
M.append('If the rules that decide an outcome in your organisation are written somewhere no software can '
         'read, that is the problem we solve. Send us a description of it and we will tell you what it '
         'would take.\n')
M.append('- Email: hello@thothica.com\n- Web: https://thothica.com\n- Thothica Private Limited, New Delhi, India\n')

open('thothica-brochure.md', 'w').write('\n'.join(M))
print('thothica-brochure.md written')
