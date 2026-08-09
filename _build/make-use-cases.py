#!/usr/bin/env python3
"""Stamp the use-case pages from the shared shell.

Use cases are what we can build for a kind of institution. They are not case
studies and must never read as delivered work: no client, no engagement, no
past tense claiming something shipped. Where a capability is already proven,
link to the case study instead of implying it here.

    python3 _build/make-use-cases.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from shell import ARTICLE_LD, INDEX_LD, write  # noqa: E402

PAGES = []


def crumb():
    return '    <p class="crumb"><a href="/use-cases/">Use cases</a></p>\n'


# ───────────────────────────────────────────────────────────── index
PAGES.append(dict(
    slug="", url="/use-cases/",
    title="Use cases",
    description="What Thothica can build, by the kind of institution asking: archives and libraries, government departments, media companies, legal practices, defence, and AI companies that need structured data.",
    jsonld=INDEX_LD % ("Use cases", "What Thothica can build, by kind of institution.", "/use-cases/"),
    body="""    <p class="eyebrow">Use cases</p>

    <h1>What we can build, <em>by who is asking.</em></h1>

    <p class="lede">The discipline does not change between these. An archive, a revenue department and a defence unit all have the same underlying problem: the meaning of their data lives in people rather than in the system. What changes is what that costs them, and what a solution has to survive.</p>

    <p class="note">These are capabilities, not completed engagements. Where we have already built something of this kind, the page links to the case study.</p>

    <ol class="idx">
      <li><a href="/use-cases/archives/">
        <span class="m">1</span>
        <span><span class="idx-k">Archives, libraries, museums</span>
        <span class="idx-t">Collections that answer questions instead of storing files</span>
        <p>Manuscripts and oral history captured properly, a public platform over the collection, an open interface so any AI can read it under your rules, and the citation record that tells you who is actually using your holdings.</p></span>
      </a></li>
      <li><a href="/use-cases/government/">
        <span class="m">2</span>
        <span><span class="idx-k">Government · department by department</span>
        <span class="idx-t">Not one use case, a different one per department</span>
        <p>Industry, revenue, procurement, legislative drafting, disaster management, local bodies, constituency offices, public sector oversight. Each has a distinct problem, and the pages say which.</p></span>
      </a></li>
      <li><a href="/use-cases/media/">
        <span class="m">3</span>
        <span><span class="idx-k">Media and publishing</span>
        <span class="idx-t">From research to a story that is ready to run</span>
        <p>Continuous coverage that stops at an editor, a research desk that turns documents into publishable angles, honest analytics, and discourse measured at a scale a newsroom cannot read by hand.</p></span>
      </a></li>
      <li><a href="/use-cases/legal/">
        <span class="m">4</span>
        <span><span class="idx-k">Legal practices and chambers</span>
        <span class="idx-t">The office keeps its judgement, the machine keeps the record</span>
        <p>Judgments turned into filing-ready translations under a controlled glossary, case files structured into positions and authorities, and contradictions surfaced across a body of law.</p></span>
      </a></li>
      <li><a href="/use-cases/defence/">
        <span class="m">5</span>
        <span><span class="idx-k">Defence and security</span>
        <span class="idx-t">Systems that run where nothing may leave the building</span>
        <p>Doctrine and standing orders made queryable, multi-source pictures assembled with provenance, and every component able to run fully disconnected on hardware you control.</p></span>
      </a></li>
      <li><a href="/use-cases/ai-companies/">
        <span class="m">6</span>
        <span><span class="idx-k">AI companies and labs</span>
        <span class="idx-t">Unstructured material turned into training-grade structure</span>
        <p>Domain corpora converted into typed, provenanced datasets with the licence position recorded, plus evaluation sets a model cannot have memorised.</p></span>
      </a></li>
    </ol>
""",
))

# ───────────────────────────────────────────────────────────── archives
PAGES.append(dict(
    slug="archives", url="/use-cases/archives/",
    title="Archives, libraries and museums",
    description="What Thothica can build for a collection: manuscript and oral-history capture, a public platform, an open machine interface so any AI can read the holdings under the institution's own rules, physical media tracking, and citation intelligence.",
    jsonld=ARTICLE_LD % ("Archives, libraries and museums",
                         "Capabilities for collections: capture, structure, public platform, an open machine interface, and citation intelligence.",
                         "/use-cases/archives/"),
    body=crumb() + """
    <h1>Collections that answer questions <em>instead of storing files.</em></h1>

    <p class="lede">An archive already holds the knowledge. What it usually lacks is any way for that knowledge to be asked a question, by a researcher or by anything else. The work below runs from the physical shelf to an interface a machine can read.</p>

    <p class="note">We have done work of this kind. See <a href="/case-studies/think-tank-archive/">the think tank archive</a> for how the mapping works in practice, and the open library at <a href="https://falsafa.ai">Falsafa.ai</a> for the method in public.</p>

    <h2>The path a collection takes</h2>
    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">1</span><span class="box-t">Capture</span><p>Scanning, photography of bound and fragile material, and recording. What exists only on paper or only in someone's memory becomes a file that can be worked with.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">2</span><span class="box-t">Make readable</span><p>Pictures of pages become text, including old typesetting, many scripts and handwriting. Recordings become transcripts with speakers and timings.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">3</span><span class="box-t">Structure</span><p>The ontology: what each item is, who made it, what it is about, who is named inside it, and how items relate. Every relation carries the passage that proves it.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">4</span><span class="box-t">Publish</span><p>To people as a fast public platform, and to machines as an open interface. Both read the same structure.</p></div>
      </div>
      <p class="fig-cap"><b>Most digitisation stops after step 2.</b> That produces a searchable pile, which is better than a cupboard and still not a knowledge system. Steps 3 and 4 are where a collection becomes something you can ask a real question of.</p>
    </div>

    <h2>Oral history, treated as a first-class source</h2>
    <div class="sec body-w">
      <p>Testimony is the most perishable holding any institution has, and the least well handled. We record it, transcribe it with speakers separated and timings kept, and translate where the interview is in a language the catalogue is not. Mixed-language speech is tagged honestly as mixed rather than forced into one language, because that tag decides how strictly a later quotation can be trusted.</p>
      <p>Then the transcript is treated exactly like a manuscript: the people and places named in it become entities, the passages become citable at a fixed address, and what the speaker said about a subject becomes a relation with the words attached.</p>
    </div>

    <h2>Manuscripts and material the machine finds hard</h2>
    <div class="sec body-w">
      <p>Older holdings break ordinary pipelines: unusual scripts, marginalia, damaged pages, mixed languages on one leaf, and layouts no modern reader expects. Two commitments make this survivable. The original stays untouched and byte-exact, so every later pass can be rerun from the source rather than from a processed copy. And the catalogue declares how confident it is in each reading rather than presenting a shaky transcription as fact.</p>
    </div>

    <h2>An open interface, so any AI can read your holdings on your terms</h2>
    <div class="sec body-w">
      <p>Researchers now arrive with an assistant. The question is whether your collection is something that assistant can consult properly, or something it will guess about. The answer is a small server that exposes your holdings as a set of defined operations: list the works, fetch a specific record, retrieve an exact passage, search the text, find related items.</p>
      <p>The design decision that matters is that no language model sits inside it. It reads from your published structure and returns text and records. The reasoning happens in whatever assistant the researcher brought, which means every improvement in those tools lifts your archive without you paying for it or rebuilding anything.</p>
    </div>

    <div class="fig">
      <div class="flow flow-3">
        <div class="box"><span class="box-k">The researcher brings</span><span class="box-t">Their own assistant</span><p>Whatever they already use. You do not choose it, host it, or pay for it.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">You publish</span><span class="box-t">A defined set of operations</span><p>List, fetch, get an exact passage, search, find related. No model inside. It serves your structure and nothing else.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Your rules travel with it</span><span class="box-t">Tiers and citation duties</span><p>Material you trust may be quoted with an address. Material you do not may only be described, with a link out. The interface applies those rules itself, so they hold even when nobody is watching.</p></div>
      </div>
      <p class="fig-cap"><b>This is how the think tank archive is published, and it is open.</b> An institution that does this stops being a place assistants hallucinate about and becomes a place they cite.</p>
    </div>

    <h2>Knowing how your collection is actually cited</h2>
    <div class="sec body-w">
      <p>Most archives cannot answer a simple question from their own board: who used us this year, and for what. Reader registers record visits, not influence. So we build the citation picture from the outside in.</p>
    </div>

    <div class="tbl-scroll">
    <table class="tbl">
      <tr><th>Question</th><th>How it gets answered</th></tr>
      <tr><td>Who cites us</td><td>Scholarly databases and open citation indexes are matched against your holdings, so a work in your collection carries the papers that cite it.</td></tr>
      <tr><td>Which holdings matter</td><td>Citation counts attach to items, so acquisition and conservation budgets can follow demonstrated use rather than intuition.</td></tr>
      <tr><td>Are we cited correctly</td><td>Malformed and broken references to your material are found and reported, and stable addresses are published so future citations resolve.</td></tr>
      <tr><td>Where are we invisible</td><td>Fields that should be citing you and do not, which is a collections and outreach finding rather than a technical one.</td></tr>
      <tr><td>Who uses us without saying so</td><td>Passages from your holdings appearing in published work without attribution, found by matching text rather than by trusting a bibliography.</td></tr>
    </table>
    </div>

    <h2>The physical layer, tracked</h2>
    <div class="sec body-w">
      <p>Digitisation does not remove the object. Boxes still move, tapes still degrade, and a loan still has to come back. We model the physical item alongside the digital one: where it is, what condition it was last recorded in, what carrier it lives on, which digital surrogate came from it, and what the retention or conservation clock says. Obsolete carriers are surfaced by risk rather than discovered when a machine to read them no longer exists.</p>
    </div>

    <h2>Turning the backlist into things people can read</h2>
    <div class="sec body-w">
      <p>Institutions sit on out-of-print books, journal runs and reports whose only form is a PDF nobody reads on a phone. Once the text is structured, the same source can be issued as a web edition with stable addresses for citation, as a reflowable electronic book, and as a fresh print-ready file. One structured source, several editions, rather than three separate retyping projects.</p>
    </div>
""",
))

# ───────────────────────────────────────────────────────────── government
PAGES.append(dict(
    slug="government", url="/use-cases/government/",
    title="Government, department by department",
    description="Government is not one use case. Industry, revenue, procurement, legislative drafting, disaster management, local bodies, constituency offices and public sector oversight each have a distinct problem an ontology solves.",
    jsonld=ARTICLE_LD % ("Government, department by department",
                         "Distinct ontology use cases across industry, revenue, procurement, legislation, disaster management, local bodies and constituency offices.",
                         "/use-cases/government/"),
    body=crumb() + """
    <h1>Government is not one use case. <em>It is a different one per department.</em></h1>

    <p class="lede">A revenue department and a disaster management authority have nothing in common in subject matter, and exactly one thing in common underneath: the rules that decide an outcome are written down somewhere no software can read. Below, department by department, is what that costs and what we would build.</p>

    <p class="note">We already run an AI layer across five live state government portals. See <a href="/case-studies/government-portals/">that case study</a> for how the layer behaves on a system in production.</p>

    <h2>One rule we apply before any of it</h2>
    <div class="fig">
      <div class="two">
        <div class="box inv"><span class="box-k">Start here</span><span class="box-t">Records you already own</span><p>Anything the department in the room holds itself. No permission to negotiate, no other agency's cooperation, no waiting. Work that can begin on Monday.</p></div>
        <div class="box"><span class="box-k">Last, and marked optional</span><span class="box-t">Records someone else owns</span><p>Anything needing another department's data sharing agreement. Valuable, slower, and never the thing a first phase depends on.</p></div>
      </div>
      <p class="fig-cap"><b>Who already holds the data decides what we do first.</b> Most government data projects stall in a memorandum between two agencies. Starting with registers the department already owns is what keeps a first phase deliverable inside one financial year.</p>
    </div>

    <h2>Industry and investment promotion</h2>
    <div class="sec body-w">
      <p><b>The problem.</b> An investor asks what land, what incentive, what clearance, and in what order. The answer exists across a dozen schemes, several agencies and a stack of orders, and lives in the memory of a few officers. Single-window portals often route the paperwork without ever encoding what each scheme actually requires.</p>
      <p><b>What we build.</b> The eligibility ontology: every scheme, the conditions it imposes, the document that proves each condition, the officer who signs each stage, and what makes a file complete. On top of that, a single window that can tell an applicant what is missing on day one, and tell an officer which files are decision-ready and which are stuck and why.</p>
    </div>

    <h2>Revenue and arrears</h2>
    <div class="sec body-w">
      <p><b>The problem.</b> Auditors report large arrears every year. The underlying detail sits in registers that were designed for collection, not for analysis, so the same leak is rediscovered annually rather than prevented.</p>
      <p><b>What we build.</b> Public registers normalised into a typed model with provenance on every record, then detection written as plain deterministic rules rather than a model. Every finding cites the statute or rule it rests on and carries its own derivation, step by step, with the figure and the source quote at each step.</p>
    </div>

    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">1</span><span class="box-t">Harvest</span><p>Published registers pulled and stored raw first, so every later pass re-runs from the same bytes.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">2</span><span class="box-t">Normalise</span><p>One typed model, provenance per record, and the gaps written down rather than hidden.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">3</span><span class="box-t">Detect</span><p>Rules as code, no model anywhere in detection, so any finding re-derives live in front of whoever is challenging it.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">4</span><span class="box-t">Answer</span><p>An assistant that may only quote the sources it was handed, verified word for word, and refuses when it cannot.</p></div>
      </div>
      <p class="fig-cap"><b>Detection must be deterministic in government work.</b> A finding that cannot be reproduced in a meeting is a finding that will be dismissed in that meeting. Rules as code re-derive; a score does not.</p>
    </div>

    <h2>Procurement integrity</h2>
    <div class="sec body-w">
      <p><b>The problem.</b> Tender data is published and almost never read as a body. Patterns that only appear across thousands of awards stay invisible to the officer looking at one file.</p>
      <p><b>What we build.</b> A grid of tests computable from published fields alone: single-bid awards, bid windows shorter than the prescribed minimum, repeated awards just under a delegation limit, vendor concentration per buyer, repeat buyer-and-vendor pairings, corrigenda that keep extending deadlines, award values drifting from estimates, clustering at the end of a financial year, bidders sharing an address, and set-aside shortfalls against policy. Each hit becomes a finding citing the exact rule, with its working shown.</p>
    </div>

    <h2>Legislative and regulatory drafting</h2>
    <div class="sec body-w">
      <p><b>The problem.</b> Rules accumulate for decades. Amendments overlay orders, orders overlay acts, and departments issue clarifications that quietly contradict each other. Nobody holds the whole body in their head, so contradictions are discovered in litigation.</p>
      <p><b>What we build.</b> The corpus of instruments modelled as things rather than documents: obligations, thresholds, definitions, exemptions, commencement dates and repeals, each anchored to the clause it comes from. Once obligations are typed, contradiction detection becomes mechanical.</p>
    </div>

    <div class="fig">
      <div>
        <div class="edge"><span class="ent">A threshold in one rule</span><span class="rel">conflicts with</span><span class="ent">the same threshold in a later order</span><span class="ev">Both clauses are shown side by side, verbatim, with their dates and their issuing authority. The system reports the conflict; it never picks a winner.</span></div>
        <div class="edge"><span class="ent">A defined term</span><span class="rel">is redefined by</span><span class="ent">a subordinate instrument</span><span class="ev">Every downstream clause relying on the original definition is listed, so the blast radius of a redefinition is visible before it is signed.</span></div>
        <div class="edge"><span class="ent">An obligation</span><span class="rel">survives</span><span class="ent">the repeal that was meant to end it</span><span class="ev">Repeal and savings clauses are modelled, so an obligation that outlived its parent act surfaces instead of lying dormant until someone is prosecuted under it.</span></div>
      </div>
      <p class="fig-cap"><b>The system's job is to find and show, never to decide.</b> Which rule prevails is a legal judgement belonging to the department. Presenting both clauses with their provenance is what lets that judgement be made in an afternoon instead of in a courtroom.</p>
    </div>

    <h2>Disaster management and weather</h2>
    <div class="sec body-w">
      <p><b>The problem.</b> A warning is not an instruction. A forecast arrives, and the question nobody can answer fast enough is who must do what, where, by when, and under whose authority. That mapping exists, in a standing order and in the experience of officers who have handled the last three events.</p>
      <p><b>What we build.</b> An ontology that connects the physical world to the administrative one: gauges, reservoirs, rivers, wards and villages on one side; officers, standing orders, thresholds and escalation ladders on the other. A warning crossing a threshold then produces a task list rather than a notification, with an owner and a deadline against every line, and escalation that fires on silence rather than waiting to be triggered.</p>
    </div>

    <div class="fig">
      <div class="layers">
        <div class="box"><span class="box-k">Action</span><span class="box-t">A task list, owned and dated</span><p>Which officer, which ward, what action, by when, under which clause of the standing order. Silence escalates by itself.</p></div>
        <div class="up">▲ derived from ▲</div>
        <div class="box inv"><span class="box-k">The ontology</span><span class="box-t">Physical world joined to the administrative one</span><p>A gauge reading is tied to the settlements downstream of it, the officers responsible for those settlements, and the threshold in the standing order that makes the reading actionable.</p></div>
        <div class="up">▲ reads ▲</div>
        <div class="box"><span class="box-k">Sources</span><span class="box-t">Forecasts, gauges, standing orders, rosters</span><p>Feeds you already receive, and documents you already have, most of which have never been machine-readable.</p></div>
      </div>
      <p class="fig-cap"><b>This is why a weather system is an ontology problem rather than a data problem.</b> The forecast is already good. What is missing is the written map from a number to a duty.</p>
    </div>

    <h2>Local bodies and constituency offices</h2>
    <div class="sec body-w">
      <p><b>The problem.</b> A ward office or a legislator's office runs on requests: a grievance, a certificate, a works demand, a recommendation. They arrive by every channel, and the record of what happened lives in a diary and a WhatsApp thread. Nobody can say what is pending and with whom.</p>
      <p><b>What we build.</b> Case operations where nothing can exist without an owner and a next date. Every request typed, routed and aged, with the standing rule that silence escalates rather than sleeps. For a constituency office, that becomes an honest picture of what was asked, what was done, and what is stuck, which is also the only defensible answer at the end of a term.</p>
    </div>

    <h2>Public sector oversight</h2>
    <div class="sec body-w">
      <p><b>The problem.</b> A state may hold hundreds of public sector undertakings, boards, corporations, societies and authorities. Their mandates were written across decades. Overlapping objects clauses, dormant bodies and duplicated functions are widely suspected and rarely evidenced.</p>
      <p><b>What we build.</b> A verified roster where every value opens the document it came from, and nothing is invented to fill a gap. Where a value cannot be sourced it stays empty and the gap is reported, because an empty cell is itself a finding. Overlap is then shown as evidence, with the objects clauses of two bodies set side by side verbatim, never as an assertion that they duplicate one another. Bodies mandated once per district or per university are marked as structurally required so they are never mistaken for duplication.</p>
    </div>
""",
))

# ───────────────────────────────────────────────────────────── media
PAGES.append(dict(
    slug="media", url="/use-cases/media/",
    title="Media and publishing",
    description="Continuous coverage that stops at an editor, a research desk that turns documents into publishable angles, honest analytics, and discourse measured at a scale a newsroom cannot read by hand.",
    jsonld=ARTICLE_LD % ("Media and publishing",
                         "Content engines, research desks, analytics and discourse measurement for media companies.",
                         "/use-cases/media/"),
    body=crumb() + """
    <h1>From research to <em>a story that is ready to run.</em></h1>

    <p class="lede">A newsroom's constraint is not ideas. It is that the work of finding, checking and shaping is done by the same people who write, on a clock that never stops. Each capability below removes one of those loads without moving the editorial decision.</p>

    <p class="note">We run an engine of this kind in production. See <a href="/case-studies/cricket-content-engine/">the unattended newsroom</a>.</p>

    <h2>Continuous coverage with a human gate</h2>
    <div class="sec body-w">
      <p>An engine that reads live signals in your subject area, decides what is worth covering now, writes it against your written style specification, corroborates its claims against sources it actually fetches, and files everything into a private queue. An editor decides what runs. The engine holds no credential that can publish, so its worst day fills a queue rather than embarrasses the masthead.</p>
    </div>

    <h2>The research desk</h2>
    <div class="sec body-w">
      <p>Reporters lose hours to documents: a budget, an annual report, a court order, a tender, a transcript. The desk turns those into a structured corpus, then surfaces the publishable angle: what changed against last year, which figure contradicts the press release, who is named and in what context, and which passage is worth quoting.</p>
    </div>

    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">1</span><span class="box-t">Ingest</span><p>Reports, filings, orders, transcripts, whatever arrives, including material that is only a scan.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">2</span><span class="box-t">Structure</span><p>Entities, figures, dates and claims typed and addressed, so a number can be pointed at rather than retyped.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">3</span><span class="box-t">Compare</span><p>Against last year, against the stated position, against what the same body said elsewhere. Contradiction is the story.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">4</span><span class="box-t">Hand over</span><p>A brief with the angle, the supporting passages, and a link to the exact page behind each one.</p></div>
      </div>
      <p class="fig-cap"><b>The desk hands over a brief.</b> A reporter given an angle and the passages behind it still writes the piece themselves, which is what keeps the byline honest.</p>
    </div>

    <h2>Analytics that answer editorial questions</h2>
    <div class="sec body-w">
      <p>Standard dashboards report traffic. Editors need to know which subjects earn attention that lasts, which formats work for which desks, where coverage is thin against demonstrated demand, and what a piece is worth beyond its first day. That requires your content to be typed against a real taxonomy rather than tagged loosely, so a coverage figure is a fact instead of an artefact of inconsistent labels.</p>
    </div>

    <h2>Discourse, measured rather than sensed</h2>
    <div class="sec body-w">
      <p>Newsrooms and researchers both want to say what a public conversation is doing. Sentiment scores are too crude to be worth printing. What can be defended is structure: which claims are circulating, who introduced them, how they mutate as they spread, which communities carry which framing, and when a subject crosses from one community into another.</p>
      <p>The unit of analysis is a claim rather than a post, so the same assertion in ten thousand different wordings counts once. Every figure resolves back to the posts behind it, because a study that cannot show its underlying material cannot be published.</p>
    </div>

    <div class="fig">
      <div class="two">
        <div class="box"><span class="box-k">What we do not do</span><span class="box-t">A mood score</span><p>One number for a nation's feeling. Impossible to defend, impossible to act on, and wrong in ways nobody can audit.</p></div>
        <div class="box inv"><span class="box-k">What we build</span><span class="box-t">A claim-level map</span><p>Which assertions exist, where each first appeared, how the wording drifts, which groups carry which version, and where they overlap. Every count opens the posts beneath it.</p></div>
      </div>
      <p class="fig-cap"><b>Built for a study that has to survive review.</b> If a finding cannot be traced to material a reader can inspect, it is an opinion with a chart attached.</p>
    </div>

    <h2>Publishing operations</h2>
    <div class="sec body-w">
      <p>For book and comic publishers the same discipline produces finished artefacts rather than articles: a research corpus, sourced scripts, generated art held consistent across a title, and output that a press and an editor can both actually use. That work is described in full in <a href="/case-studies/graphic-stories/">the graphic stories case study</a>.</p>
    </div>
""",
))

# ───────────────────────────────────────────────────────────── legal
PAGES.append(dict(
    slug="legal", url="/use-cases/legal/",
    title="Legal practices and chambers",
    description="Judgments turned into filing-ready translations under a controlled glossary, case files structured into positions and authorities, and contradictions surfaced across a body of law. Deployable inside the office.",
    jsonld=ARTICLE_LD % ("Legal practices and chambers",
                         "Translation under a controlled glossary, structured case files, and contradiction analysis, deployable inside a legal office.",
                         "/use-cases/legal/"),
    body=crumb() + """
    <h1>The office keeps its judgement. <em>The machine keeps the record.</em></h1>

    <p class="lede">Legal work is unusually well suited to an ontology and unusually unforgiving of a wrong one. Terms are defined, authority is hierarchical, and a document either says something or it does not. What breaks ordinary tools is that being approximately right is worthless here.</p>

    <h2>Judgments and orders, translated to filing standard</h2>
    <div class="sec body-w">
      <p>Courts in India work across languages, and a translation that reads well but renders a term of art loosely is not usable in a filing. So the terminology is not left to the translator's discretion. A controlled glossary of legal terms is mandatory input, and compliance with it is checked rather than hoped for.</p>
    </div>

    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">Stage 1</span><span class="box-t">Read the document</span><p>Scanned pages become text, with the structure of a judgment respected: cause title, parties, headnote, body, footnotes, and the running headers that must not be translated as if they were prose.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Stage 2</span><span class="box-t">Decide the approach first</span><p>The whole document is read before a word is translated, and a written strategy is fixed: how this judgment handles its terms, its register, its citations. Translating passage by passage without that produces a document that drifts.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">Stage 3</span><span class="box-t">Translate under the glossary</span><p>In passages, each carrying the strategy and what came before, so terminology stays identical from first page to last. The glossary is binding.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Stage 4</span><span class="box-t">Check, and redo what fails</span><p>Every passage is scored against the source and the glossary. Anything below the bar is translated again rather than shipped with a caveat.</p></div>
      </div>
      <p class="fig-cap"><b>The glossary is the ontology.</b> Several hundred terms with one binding rendering each is what makes two documents translated months apart consistent with one another, which is the difference between a convenience and a filing.</p>
    </div>

    <div class="sec body-w">
      <p>The output is a formatted document rather than a text file: the conventions of a legal document in the target language reproduced properly, party tables, footnote numbering, headers with page numbers, and the fonts a registry expects. A translation that has to be reformatted by a clerk has not saved the office anything.</p>
    </div>

    <h2>Case files, structured</h2>
    <div class="sec body-w">
      <p>A matter is a pile of documents and one lawyer's understanding of it. The ontology makes the understanding explicit: parties and their roles, the issues in dispute, each side's position on each issue, the authorities relied on for each position, the facts asserted with the document that evidences them, and the procedural history with its dates.</p>
      <p>Once that exists, a junior joining a matter reads a structure rather than a shelf, and a question like <em>what is our answer on limitation and what supports it</em> has an answer that opens the document behind it.</p>
    </div>

    <h2>Contradiction across a body of law</h2>
    <div class="sec body-w">
      <p>The same analysis described for <a href="/use-cases/government/">legislative drafting</a> serves a practice differently: conflicting authority on a point, a line of cases that has quietly diverged between benches, a statutory definition that changed under a body of precedent built on the old one, or an instrument still being cited after amendment. Each is surfaced with both texts side by side, never with a verdict, because the verdict is the practice's work.</p>
    </div>

    <h2>How it sits in the office</h2>
    <div class="fig">
      <div class="two">
        <div class="box"><span class="box-k">Control</span><span class="box-t">The firm decides everything</span>
          <ul>
            <li>Access is by invitation, per person</li>
            <li>Work is metered, so cost is visible per matter</li>
            <li>Every action is logged and auditable</li>
            <li>Deletion of stored material is deliberate and restricted</li>
          </ul>
        </div>
        <div class="box inv"><span class="box-k">Customisation</span><span class="box-t">Fitted to the practice</span>
          <ul>
            <li>The glossary is yours and you extend it</li>
            <li>Formatting matches the registries you file in</li>
            <li>The case ontology follows your areas of work</li>
            <li>It can run entirely on infrastructure you control</li>
          </ul>
        </div>
      </div>
      <p class="fig-cap"><b>Privilege is the constraint that shapes the architecture.</b> Client material is not a corpus to be pooled. Each practice gets its own instance, its own glossary and its own store, and nothing crosses between them.</p>
    </div>
""",
))

# ───────────────────────────────────────────────────────────── defence
PAGES.append(dict(
    slug="defence", url="/use-cases/defence/",
    title="Defence and security",
    description="Doctrine and standing orders made queryable, multi-source pictures assembled with provenance, and every component able to run fully disconnected on hardware the organisation controls.",
    jsonld=ARTICLE_LD % ("Defence and security",
                         "Queryable doctrine, provenance-carrying multi-source assessment, and fully disconnected deployment.",
                         "/use-cases/defence/"),
    body=crumb() + """
    <h1>Systems that run <em>where nothing may leave the building.</em></h1>

    <p class="lede">Defence organisations have the ontology problem in its severest form. The knowledge that decides an action is written in doctrine, standing orders and instructions accumulated over decades, and the people who can navigate it are few and are posted out every couple of years.</p>

    <p class="note">Everything here is designed for a disconnected environment. If a capability needs an external service to work, it is not offered.</p>

    <h2>The constraint that comes first</h2>
    <div class="fig">
      <div class="layers">
        <div class="box"><span class="box-k">Assumed</span><span class="box-t">No outbound network</span><p>The system is built to run with no connection to anything outside the enclave. Not "can be configured offline". Offline is the design point.</p></div>
        <div class="up">▲ built on ▲</div>
        <div class="box inv"><span class="box-k">Consequence</span><span class="box-t">The heavy work happens before deployment</span><p>Structuring, indexing and validation are done at build time. What is installed is data and deterministic code, so the running system needs no external call to answer a question.</p></div>
        <div class="up">▲ enables ▲</div>
        <div class="box"><span class="box-k">Result</span><span class="box-t">Your hardware, your control</span><p>Runs on infrastructure the organisation owns. Models, where used at all, are ones that run locally. Nothing phones home, because there is nothing to phone.</p></div>
      </div>
      <p class="fig-cap"><b>This is the same architecture we use elsewhere, for a different reason.</b> Doing the expensive work offline and shipping deterministic artefacts is how the government portals stay cheap to run. In a defence context the same choice is what makes deployment possible at all.</p>
    </div>

    <h2>Doctrine and standing orders, made answerable</h2>
    <div class="sec body-w">
      <p>Thousands of pages of doctrine, instructions, orders and amendments. The practical question is never "what does the manual say" but "which paragraph applies to this situation, in the current amendment state, and what does it require of me". We model instruments the way we model regulation: obligations, thresholds, conditions, authorities and amendment state, each anchored to its clause. Superseded material is marked superseded rather than deleted, so an officer can see both what applies now and what applied at the time of an incident under review.</p>
    </div>

    <h2>Assessment from many sources, with provenance intact</h2>
    <div class="sec body-w">
      <p>Assessment means combining reports of differing reliability. The failure mode is that confidence gets averaged into a single number and the reasoning becomes unrecoverable. The ontology keeps source reliability and information credibility as separate recorded properties, never merged, so an assessment can always be unwound to what each source actually said and how much that source has historically been worth.</p>
    </div>

    <div class="fig">
      <div>
        <div class="edge"><span class="ent">A reported observation</span><span class="rel">is asserted by</span><span class="ent">a source with its own reliability record</span><span class="ev">The claim and the source's track record are stored separately. A confident claim from an unreliable source never quietly becomes a confident fact.</span></div>
        <div class="edge"><span class="ent">Two reports</span><span class="rel">corroborate</span><span class="ent">each other, or do not</span><span class="ev">Corroboration is only recorded where the sources are genuinely independent. Two reports derived from the same origin are marked as one, not two.</span></div>
        <div class="edge"><span class="ent">An assessment</span><span class="rel">rests on</span><span class="ent">an ordered chain of evidence</span><span class="ev">Every conclusion can be unwound step by step to the reports beneath it, so a reviewer can see exactly where a judgement entered and who made it.</span></div>
      </div>
      <p class="fig-cap"><b>Independence is the rule doing the work here,</b> exactly as it does in <a href="/case-studies/olympiad-forms/">the verification work</a>. Evidence that confirms a reading must come from a source independent of it, or a single origin ends up confirming itself through three channels.</p>
    </div>

    <h2>Where else it applies</h2>
    <div class="tbl-scroll">
    <table class="tbl">
      <tr><th>Area</th><th>The ontology problem underneath</th></tr>
      <tr><td>Maintenance and fleet readiness</td><td>Platforms, subsystems, parts and their interchangeability, service life and inspection intervals, modelled so a readiness figure is derived from records rather than assembled by hand each week.</td></tr>
      <tr><td>Logistics and stores</td><td>The same physical item catalogued differently by different formations. Alias resolution is what turns several local names into one item with one true stock position.</td></tr>
      <tr><td>Procurement and qualification</td><td>Requirements written as conditions with the evidence that satisfies each, so trial outcomes and vendor claims can be checked against the specification rather than read against it.</td></tr>
      <tr><td>Training and lessons</td><td>After-action material structured so a recurring failure is countable across years and formations instead of being rediscovered by each new commander.</td></tr>
      <tr><td>Archives and history</td><td>Unit records, war diaries and photographic collections structured, described and preserved on the same basis as any other <a href="/use-cases/archives/">archive</a>, at the classification the material requires.</td></tr>
    </table>
    </div>

    <h2>What we will not claim</h2>
    <div class="sec body-w">
      <p>We build knowledge infrastructure. We do not build targeting systems, we do not offer autonomous decision-making in the use of force, and we do not present a machine's output as an assessment. Every system described here surfaces what the record says, with provenance, so a responsible officer decides faster on better evidence. Where the record is silent, the correct output is that it is silent.</p>
    </div>
""",
))

# ───────────────────────────────────────────────────────────── AI companies
PAGES.append(dict(
    slug="ai-companies", url="/use-cases/ai-companies/",
    title="AI companies and labs",
    description="Domain corpora converted into typed, provenanced datasets with licence position recorded, plus evaluation sets a model cannot have memorised.",
    jsonld=ARTICLE_LD % ("AI companies and labs",
                         "Unstructured domain material turned into typed, provenanced training data and uncontaminated evaluation sets.",
                         "/use-cases/ai-companies/"),
    body=crumb() + """
    <h1>Unstructured material turned into <em>training-grade structure.</em></h1>

    <p class="lede">Frontier models are broadly capable and thin in exactly the places that matter to a specialist buyer: Indian legal procedure, a state's administrative practice, a classical corpus in its own language, a regulated industry's actual paperwork. That material exists. It is almost never in a form anyone can train on.</p>

    <h2>What we hand over</h2>
    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">1</span><span class="box-t">Acquire and preserve</span><p>Scans, filings, recordings, whatever the domain runs on. Originals kept byte-exact, so any later reprocessing starts from the source rather than from someone's cleaned copy.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">2</span><span class="box-t">Read and type</span><p>Text extracted, structure recovered, entities resolved, and every record given a stable address. Ground facts and anything inferred are kept in separate fields and never merged.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">3</span><span class="box-t">Provenance and rights</span><p>Per record: where it came from, when it was fetched, and its licence position. A dataset without this is not usable by anyone with a legal department.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">4</span><span class="box-t">Deliver</span><p>Typed records against a published schema, validated, with the gaps documented rather than quietly filled.</p></div>
      </div>
      <p class="fig-cap"><b>Step 3 is the one that decides whether a dataset can be used.</b> Most scraped corpora fail not on quality but on the fact that nobody can say where a given row came from or whether it was permitted.</p>
    </div>

    <h2>The rule that makes the data trustworthy</h2>
    <div class="sec body-w">
      <p>A model's output is never recorded as a fact. Anything normalised, classified or inferred is stored as a derived value carrying the method that produced it, the confidence, and what it was derived from. The ground fact stays exactly as printed in the source, in its own field.</p>
      <p>That separation is what lets a buyer decide for themselves how much of the interpretation to accept, and what stops a pipeline from laundering a guess into a training label.</p>
    </div>

    <div class="fig">
      <div class="two">
        <div class="box"><span class="box-k">Ground fact</span><span class="box-t">As printed</span><p>The verbatim value from the document, with source, exact location and the snippet that contains it. Never edited, never smoothed.</p></div>
        <div class="box inv"><span class="box-k">Derived value</span><span class="box-t">As interpreted</span><p>The normalised or classified form, with method, confidence and what it came from. Carries no source of its own, because it is not from a source.</p></div>
      </div>
      <p class="fig-cap"><b>They stay in two separate fields.</b> Once an interpretation is written into the same field as the record itself, nobody downstream can tell which parts came from the document and which were inferred.</p>
    </div>

    <h2>Evaluation sets that have not been memorised</h2>
    <div class="sec body-w">
      <p>Public benchmarks leak into training data, and a model that has seen the answers cannot be measured by them. We build evaluation sets from material that is genuinely held out: questions written against specific passages in a controlled corpus, with the answer verifiable as an exact quotation from a document rather than by an approximate match to an expected string.</p>
      <p>Because the corpus is structured, scoring can be deterministic. A citation either resolves to the right passage or it does not, which removes the judge model and the argument about whether it is fair.</p>
    </div>

    <h2>Retrieval that does not need a vector database</h2>
    <div class="sec body-w">
      <p>Where a lab or a product team wants grounded answering over a domain, the structure usually does the work that embeddings are reached for. A typed catalogue, exact-match search and authored relations give a model the shape of the domain, which similarity search flattens away. Citations resolve to a paragraph rather than to a chunk, so an answer can be followed back.</p>
      <p>Delivered as a defined set of operations any assistant can call, so the corpus is usable from whatever stack you already run. The same interface is described for <a href="/use-cases/archives/">archives</a>, and is running in public on our open library.</p>
    </div>
""",
))


def main():
    for p in PAGES:
        out = write("use-cases", p["slug"], p["title"], p["description"],
                    p["url"], p["jsonld"], p["body"])
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
