# Thothica: capability brochure

> AI systems for institutions that run on records. We write the ontology, send the agents that fill it, and build the system your staff work in. Then we run it.

Thothica Private Limited, New Delhi, India. Founded 2023. Contact: hello@thothica.com · https://thothica.com

This file is the same brochure the PDF contains, written as plain text so it can be handed to an assistant. Clients are described rather than named. Named evidence is available under a confidentiality undertaking.

## At a glance

- **5** government portals running our AI layer
- **115,652** records classified on one of those portals
- **1,000+** historical works mapped and searchable
- **10M** words of research made usable

## 01. The stack: four layers, all of them ours

This is normally four separate suppliers, plus a systems integrator hired to connect them. We do all four parts ourselves.

### L1. Ontology: We write down what your data means

Our software reads the systems you already run and writes the first draft: what each record is, how it links to the others, and who has to sign off. We set the rules it follows and check what it produces. You end up with one document your staff can read and your software can execute.

*Ontology works with:* SAP, Oracle, PostgreSQL, SQL Server, SharePoint, Excel, Tally, Scanned PDFs, Legacy portals, Paper registers

### L2. Agents and engineers: We sit with your experts, in software or in person

Much of what decides an outcome was never written down anywhere. It is in the head of the officer who has done the job for eleven years. Forward deployed agents are software that works through the systems your people already use. Forward deployed engineers are our own people, in your building, writing the same structure by hand where software cannot reach. Which of the two we send depends on the engagement, and on some it is both.

*Agents and engineers works with:* Revenue officers, Archivists, Procurement staff, Draftsmen, Editors, Examiners, Registrars, Curators

### L3. Application: We build the system your staff work in

Either we build it, or we put the layer inside the software you already use. Either way your staff get an answer they can act on, with the source record attached to it.

*Application works with:* A single-window portal, A case file system, An editorial queue, An officer dashboard, An open API, A layer inside your ERP

### L4. Operation: We run it, and we keep running it

Five government portals, a hundred-year-old archive, a publishing line and a newsroom engine are live on this stack right now, and we operate them. We do not hand over the code and leave.

*Operation works with:* 5 government portals, 115,652 records classified, 2,000+ works catalogued, 10M words of research

## 02. The discipline: what an ontology is

Ask two departments what a pending case is and you will get two answers. Both are right, because each was defined for a different purpose years ago, and neither definition was ever written down. So the two produce different numbers and nobody can say which one is correct.

An ontology closes it. It is a plain document that says what each thing is, which one is the real number, and who decides. It has three parts:

1. **Data sources, what you have.** Scanned PDFs, spreadsheets, databases, old systems still in use, SAP and other enterprise software. Wherever your data sits we write the connection to it. Nothing is moved or re-typed.
2. **Logic sources, what you know.** Formulas buried in spreadsheets, code you already run, written rules. Much of it is in no system at all: agents and engineers sit with your experts and write it down in the same structure.
3. **Systems of action, what you do.** Your ERP, your existing portals, a new system we build, or an AI agent. The result is a step someone can actually carry out, with the record it came from attached.

Those three parts together are the ontology. It is kept in one place, in one structure, and both your staff and your software read it.

**Why the method repeats.** Four unrelated industries. No two of them stored their data the same way. We rebuilt the same layer against each one, and the method did not change.

## 03. Case studies: five systems in production

### Five Portals, One Read-Only AI Layer

*Sector: Government*

A state government ran five portals on different technology, each with its own idea of how to store the same facts. Officials could see their own screens. Nobody could ask a question across the records.

- **115,652** records classified on one portal
- **5** live portals carrying the layer
- **4** different technologies underneath
- **0** writes back into any source system

**Before.** A question goes to the officer who knows. They export a spreadsheet, clean it by hand, and produce a figure nobody else can reproduce.

**After.** A question goes to the layer. It answers from that portal’s own rows, and every figure opens the records it was built from.

**How it runs.**

1. **Catalogue.** For each portal, what its data measures and every legitimate way it can be broken down: by district, by scheme, by month, by status.
2. **Classify.** Free-text fields sorted into a fixed set so they can be counted. On one portal that was 115,652 separate decisions about what a piece of text meant.
3. **Answer.** An official asks in plain language. The answer is assembled from that portal’s own rows.
4. **Trace.** Every figure opens the records it was built from, so a number can be defended in the room.

**The rule underneath.** For each portal we first wrote down what its data measures and every way it can legitimately be broken down, then classified the free-text fields into a fixed set so they could be counted. The layer holds read permission only. It cannot alter a record even if it is asked to.

### A Century of Writing, Searchable by Who Said What

*Sector: Think tank*

A think tank held the written record of a tradition going back to the 1850s: more than two thousand PDFs, most of them photographs of printed pages, on a site that was slow to load and impossible to search.

- **1,000+** historical works catalogued
- **506** writers resolved to one identity each
- **5** languages read across several scripts
- **2** declared trust tiers

**Before.** Two thousand PDFs of photographed pages. The collection existed; the knowledge in it did not.

**After.** Ask who wrote about whom, on what subject and in what words. Every relation carries the passage that proves it.

**How it runs.**

1. **Read.** Photographs of printed pages turned into text across five languages and several scripts.
2. **Resolve.** 506 writers matched to one identity each, across scripts, spellings and initials.
3. **Relate.** Who wrote what, who is the subject of what, who is mentioned inside what, who argued with whom.
4. **Prove.** Every relation carries the verbatim passage, checked as a substring of the source text.

**The rule underneath.** Every relation carries the verbatim passage that proves it, checked as a substring of the source text. A relation whose quotation fails that check is discarded rather than kept with a warning, so a fabricated quotation cannot survive storage.

### Graphic Stories at Scale, Every Line Traced to a Source

*Sector: Publishing*

One of India’s largest publishers wanted graphic stories faster than any studio could make them, and accurate enough to put a living person’s words in a speech bubble.

- **10M** words in the research corpus
- **70+** books converted and chaptered
- **220+** interviews transcribed
- **5** publishing lines on one pipeline

**Before.** Pace and accuracy pull against each other, and provenance is a promise somebody has to keep by hand.

**After.** Provenance is a mechanical gate. Every beat points at a source line, and the gate resolves each pointer before the script proceeds.

**How it runs.**

1. **Corpus.** 70+ books and 220+ interviews, split chapter per file so a claim can point at an exact line.
2. **Script.** Every beat in the finished script carries a pointer to the source line behind it.
3. **Gate.** The gate resolves each pointer before the script proceeds. A broken pointer stops the book.
4. **Art.** Characters and pages generated against locked visual specifications, shipped press-ready.

**The rule underneath.** Sources are split chapter per file so a claim can point at an exact file and line. Art is generated against locked visual specifications per figure, and ships both as press-ready separated colour and as editable pages in the book’s own lettering.

### A Newsroom That Runs Unattended and Publishes Nothing

*Sector: Media*

A sports publisher needed coverage on a clock that never stops. Hiring for that clock is expensive and still leaves the small hours uncovered.

- **0** credentials that can publish
- **1** manifest every consumer reads from
- **3** kinds of taxonomy dimension
- **1** human decision left in place

**Before.** Continuous coverage means hiring for a clock that never stops, and the small hours stay uncovered anyway.

**After.** The engine works the clock and stops at an editorial queue. It holds no credential that can publish.

**How it runs.**

1. **Read.** Live match data, the news wire and fan forums, on a clock that never stops.
2. **Plan.** The engine plans its own slate against a taxonomy declared in one manifest.
3. **Write.** In the publisher’s voice, against a written style specification, checked against sources it fetches.
4. **Stop.** Everything lands in a private queue. An editor decides what runs.

**The rule underneath.** The engine reads live signals, plans its own slate, writes against a written style specification and corroborates its claims against sources it actually fetches. Then it stops. On its worst day it fills a queue rather than embarrassing the masthead.

### Handwritten Registers Turned Into Verified Rows

*Sector: Education*

An academic olympiad receives registrations on paper: a row per student, a tick per subject, a handwritten total at the bottom. Thousands of sheets a season, every one typed up and checked by hand.

- **2** independent readings of each total
- **3** verdicts, one of them silent
- **0** sums done by the model
- **100%** of conflicts reported, never repaired

**Before.** Every sheet typed up by one person, then checked by a second, because the data becomes a child’s exam entry.

**After.** A model reads the page and code does every sum. Anything it cannot verify comes back marked unverified, never marked correct.

**How it runs.**

1. **Transcribe.** A vision model reads what is actually on the paper, and does nothing else.
2. **Recompute.** Code recomputes each class from the marks. The model does no arithmetic at all.
3. **Reconcile.** Compared against the handwritten total, read independently and pinned so a later repair cannot move it.
4. **Verdict.** Verified, conflicted, or unverified. A sheet with nothing to check against is never called correct.

**The rule underneath.** The doctrine is that the model does perception and the code does arithmetic. Evidence that confirms a reading must come from a source independent of it, so the same reading is never used to check itself.

## 04. Use cases: built to order, by institution

Grouped by the institution asking. These are capabilities, not finished projects.

### Collections That Answer Questions

*For: Archives, libraries, museums*

Manuscripts and oral history captured properly, a public platform over the collection, an open interface any AI can read under your rules, and a picture of who actually cites you.

### A Different Use Case per Department

*For: Government*

Industry, revenue, procurement, drafting, disaster management, local bodies, constituency offices and public sector oversight. Each has its own problem, and each gets its own first deliverable.

### From Research to a Story Ready to Run

*For: Media and publishing*

Coverage that stops at an editor, a research desk that turns documents into angles, analytics that answer editorial questions, and discourse measured claim by claim.

### The Office Keeps Its Judgement

*For: Legal practices*

Judgments translated to filing standard under a glossary that is binding, case files structured into positions and authorities, and conflicting authority surfaced across a body of law.

### Runs Where Nothing May Leave the Building

*For: Defence and security*

Doctrine and standing orders made answerable, assessment that keeps source reliability separate from what was reported, and every part able to run fully disconnected.

### Messy Material Turned Into Training-Grade Structure

*For: AI companies and labs*

Domain corpora typed and given provenance with the licence position recorded, plus evaluation sets a model cannot already have memorised.

### Government, department by department

| Department | Written down nowhere | What that costs today | First deliverable |
| --- | --- | --- | --- |
| Industry | What each scheme really requires, and in what order | Investors wait on officers who know | An eligibility model behind the single window |
| Revenue | Which patterns in the register indicate a leak | The same leak is found again every year | Rules as code, each citing its statute |
| Procurement | What a suspicious award looks like across a body of tenders | Only single files get read | A detection grid over published fields |
| Drafting | Which instruments contradict which | Conflicts surface in litigation | Obligations typed and compared |
| Disaster | Who must act on a given warning, and by when | The map lives with experienced officers | Warnings that produce an owned task list |
| Local bodies | What is pending, and with whom | A diary and a chat thread | Nothing exists without an owner and a date |
| PSU oversight | Which bodies overlap in mandate | Suspected, never evidenced | A roster where every value opens its source |

**Sequencing.** Start with registers the department already owns. Anything that needs another agency’s cooperation comes last and is marked optional, because most government data projects stall in a memorandum between two agencies.

## 05. Open source: the method, in public

- **Falsafa.ai.** Our open library of the world’s philosophical, classical and religious texts: more than 2,000 works split into more than 1.3 million passages that can each be quoted and cited exactly.
- **The Atlas.** A map of the collection drawn from the texts themselves: the people, ideas, places, groups and events across twenty-five centuries, and every time one text cites another, including whether the later author agreed or argued back.
- **It cannot invent a quotation.** The software that builds the Atlas is not allowed to write quotations. It can only point at paragraphs, and the words are attached afterwards from the source text.

- **2,018** works in the library
- **1.3M** passages addressable
- **36,472** entities in the Atlas
- **363,042** verbatim quotations

Thothica works with some of India’s largest publishers, with state governments, and with leading think tanks and small businesses.

## Get in touch

If the rules that decide an outcome in your organisation are written somewhere no software can read, that is the problem we solve. Send us a description of it and we will tell you what it would take.

- Email: hello@thothica.com
- Web: https://thothica.com
- Thothica Private Limited, New Delhi, India
