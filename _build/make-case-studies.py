#!/usr/bin/env python3
"""Stamp the case-study pages from one shared shell.

There is no build step on this site: the generated HTML is committed and served
directly. This script exists so the head, nav and footer cannot drift across
pages. Edit the body content here and re-run it; never hand-edit the output.

    python3 _build/make-case-studies.py
"""
import pathlib

import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from shell import SHELL, ARTICLE_LD, INDEX_LD, V, write, write_redirect  # noqa: E402


def crumb():
    return ('    <p class="crumb"><a href="/case-studies/">Case studies</a></p>\n')


PAGES = []

# ─────────────────────────────────────────────────────────── index
PAGES.append(dict(
    slug="", url="/case-studies/",
    title="Case studies",
    description="Five systems Thothica has built: an AI layer over five live government portals, a century-old archive mapped into a citable graph, a graphic-stories production line where every panel is sourced, an unattended newsroom, and handwritten registers turned into verified rows.",
    jsonld=INDEX_LD % ("Case studies", "Five systems Thothica has built, across government, publishing, research and events.", "/case-studies/"),
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
      <li><a href="/case-studies/graphic-stories/">
        <span class="m">3</span>
        <span>
          <span class="idx-k">Publishing · graphic stories at scale</span>
          <span class="idx-t">Graphic stories at scale, with every line traced to a source</span>
          <p>Research turned into a navigable corpus, then into finished books: script, characters, backgrounds and print-ready pages. Every beat points at an exact line in an exact file, and a gate refuses the script if a pointer does not resolve.</p>
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
      <p class="fig-cap"><b>The arrows only point up.</b> The layer holds read permission and nothing else, so it cannot alter a record even if it is asked to. For a government system, that permission boundary is why the work could be approved at all.</p>
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

    <h2>What the catalogue actually looks like</h2>
    <div class="sec body-w">
      <p>The catalogue is a grid. Down one side are the things a department counts. Across the top are the ways each of those can legitimately be cut. A filled cell means that combination is defined and answerable; an empty one means it is not, and the system says so rather than inventing a number.</p>
    </div>

    <div class="fig">
      <div class="tbl-scroll">
      <table class="mx">
        <thead><tr><th></th><th>By district</th><th>By scheme</th><th>By month</th><th>By status</th><th>By officer</th></tr></thead>
        <tbody>
          <tr><th>Applications received</th><td class="on">•</td><td class="on">•</td><td class="on">•</td><td class="on">•</td><td class="off"></td></tr>
          <tr><th>Pending beyond limit</th><td class="on">•</td><td class="on">•</td><td class="on">•</td><td class="on">•</td><td class="on">•</td></tr>
          <tr><th>Amount disbursed</th><td class="on">•</td><td class="on">•</td><td class="on">•</td><td class="off"></td><td class="off"></td></tr>
          <tr><th>Complaints raised</th><td class="on">•</td><td class="off"></td><td class="on">•</td><td class="on">•</td><td class="off"></td></tr>
        </tbody>
      </table>
      </div>
      <p class="scroll-note">Scroll the table sideways →</p>
      <p class="fig-cap"><b>A filled cell is a promise.</b> The layer will answer that question from the portal's own rows. The empty cells matter just as much, because they are where the department's data genuinely cannot support a breakdown, and saying so is more useful than producing a figure nobody can defend. This grid is small here for the example; on the largest portal it runs to more than fifty measures.</p>
    </div>

    <h2>What happens when somebody asks</h2>
    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">Asked</span><span class="box-t">In plain language</span><p>"How many applications in this district are waiting on one document?"</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Resolved</span><span class="box-t">Against the catalogue</span><p>The question maps to a defined measure and two defined cuts. If it maps to nothing, the layer says the question cannot be answered rather than guessing.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Read</span><span class="box-t">From the portal's rows</span><p>A read-only query against the department's own database. No copy, no separate warehouse, no stale figure.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">Returned</span><span class="box-t">With the receipt</span><p>The number, and the rows it was computed from, so the officer can open the underlying files.</p></div>
      </div>
      <p class="fig-cap"><b>The second step is the one that makes this safe.</b> A layer that maps every question onto something will always produce an answer, including for questions its data cannot support. Refusing is a feature that has to be designed in.</p>
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

    <h2>Why one person is the hardest part</h2>
    <div class="sec body-w">
      <p>A hundred years of printing produces a dozen spellings of the same name. Initials expand and contract, transliteration conventions change, a periodical drops a middle name, and the same writer appears in Devanagari in one work and Latin script in another. Until those collapse into one identity, every count in the archive is wrong.</p>
    </div>

    <div class="fig">
      <div class="mapto">
        <ul>
          <li>The name as printed on a 1954 pamphlet</li>
          <li>The initials-only form used by a periodical</li>
          <li>The same name in a different script</li>
          <li>A transliteration with different vowels</li>
          <li>A byline with the middle name dropped</li>
        </ul>
        <div class="arw"></div>
        <div class="box inv"><span class="box-k">Resolved to</span><span class="box-t">One writer</span><p>One identity, carrying every form it has ever been printed under, so a search on any of them finds all of the work.</p></div>
      </div>
      <p class="fig-cap"><b>Where the software cannot make the match with confidence, it does not.</b> The name is kept exactly as printed and marked unresolved, which leaves a curator a real queue to work through. Forcing an uncertain match would quietly merge two people, and nobody would ever find the error.</p>
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
      <p class="fig-cap"><b>The tier travels with every record.</b> Anything reading the archive can tell what it is allowed to say about a given work. The route from Tier B up to Tier A is already in the schema, so if a scan is cleaned up later, that is a change to the data rather than a rebuild.</p>
    </div>

    <h2>What the researcher gets</h2>
    <div class="sec body-w">
      <p>A fast library, searchable in five languages. A name resolves to a person rather than a spelling. Every answer points back to the page it came from. And a question like <em>who argued with whom about free enterprise in the 1960s</em> has an answer you can follow down to the paragraph.</p>
      <p>Software can read the same structure. A researcher's AI assistant works from the archive directly, under the same tier rules a person gets, and nobody has to hand over a copy of the collection.</p>
    </div>
""",
))

# ─────────────────────────────────────────────── 3. comic production
PAGES.append(dict(
    slug="graphic-stories", url="/case-studies/graphic-stories/",
    title="Graphic stories at scale, every line sourced",
    description="An ongoing production line for graphic stories across several publishing lines: research corpus, sourced scripts, generated characters and backgrounds, and print-ready and editable output.",
    jsonld=ARTICLE_LD % ("Graphic stories at scale, every line sourced",
                         "An ongoing production line for graphic stories: sourced scripts, generated art, and print-ready and editable output.",
                         "/case-studies/graphic-stories/"),
    body=crumb() + """
    <h1>Graphic stories at scale, <em>every line traced to a source.</em></h1>

    <p class="lede">One of India's largest publishers wanted graphic stories made at a pace no studio could match, and accurate enough to put a living person's words in a speech bubble. Those two requirements pull in opposite directions. The resolution was to make provenance a mechanical gate rather than an editorial promise, and then to build the rest of the production line around it.</p>

    <p class="note">The pipeline is deployed and running. Titles come off it continuously across five publishing lines, and each new line we add extends the same machinery instead of needing its own.</p>

    <div class="stats">
      <div><b>~10M</b><span>words in the research corpus</span></div>
      <div><b>70+</b><span>books converted and chaptered</span></div>
      <div><b>220+</b><span>interviews transcribed</span></div>
      <div><b>5</b><span>publishing lines on one pipeline</span></div>
    </div>

    <h2>The ontology, top to bottom</h2>
    <div class="sec body-w">
      <p>Everything in the system is one of five things, and every line the pipeline produces knows where it sits. A new product line can then be added without touching the machinery.</p>
    </div>

    <div class="fig">
      <div class="layers">
        <div class="box"><span class="box-k">Level 1</span><span class="box-t">Line</span><p>A product family, and they are not alike. Illustrated biographies. India's classical epics and traditional knowledge. Health and social-awareness titles for children and teenagers. An original character universe for early readers. Activity and early-learning books. Each has its own format, length and voice.</p></div>
        <div class="up">▼ contains ▼</div>
        <div class="box"><span class="box-k">Level 2</span><span class="box-t">Program</span><p>A series inside the line. Business figures. Science figures. One epic. One awareness category such as road safety or mental health.</p></div>
        <div class="up">▼ contains ▼</div>
        <div class="box"><span class="box-k">Level 3</span><span class="box-t">Subject</span><p>The person, character or topic a book is about. One subject can spawn several books, an early-years title and a later-career title, or one story told for two different age groups.</p></div>
        <div class="up">▼ splits into ▼</div>
        <div class="two" style="margin-top:0">
          <div class="box"><span class="box-k">Level 4 · input</span><span class="box-t">Dossier</span><p>The research. Sources, each carrying its own provenance record, and an index regenerated from the files so it can never drift from what is actually there.</p></div>
          <div class="box inv"><span class="box-k">Level 5 · output</span><span class="box-t">Book</span><p>One script file per title, with its own metadata at the top, in a grammar a parser reads. Length, format and narrator are declared here, per title.</p></div>
        </div>
      </div>
      <p class="fig-cap"><b>The contract is uniform even where the shape is not.</b> A dossier built from converted books looks different inside from one built from authored topic notes, but both present the same three things to the tooling. That is why an entire new line was added by extending one list of permitted values, inheriting the grammar, the gates and the deliverables unchanged.</p>
    </div>

    <h2>How the research gets in</h2>
    <div class="sec body-w">
      <p>Books, long interviews and video all arrive as something a machine cannot read straight: a scanned page, an audio file, a video. Each is converted to text, then split so that it can be pointed at precisely.</p>
    </div>

    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-k">Step 1</span><span class="box-t">Convert</span><p>Books to text. Audio and video to transcripts, marked with who is speaking and when, and tagged honestly by language including mixed-language speech.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-k">Step 2</span><span class="box-t">Split by chapter</span><p>One file per chapter, under a chapter map that summarises each in a line. Only then can a claim point at an exact line.</p></div>
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
      <p class="fig-cap"><b>This actually happened, and we learned more from it than from anything that worked.</b> One draft arrived with no citations in it at all. The gate passed it, truthfully and uselessly, because there was nothing to check. The checker now counts how much of the script is cited as well as checking the citations it finds.</p>
    </div>

    <div class="fig">
      <div class="branch">
        <div class="box"><span class="box-k">Every line of the script</span><span class="box-t">Carries a pointer to a file and a line number</span><p>The checker opens each one against the real file in the research corpus.</p></div>
        <div class="branch-arms">
          <div class="arm"><span class="arm-l">Every pointer opens</span>
            <div class="box"><span class="box-t">The script moves on</span><p>To art direction, then to the editorial review application, where the source link stays live on every beat so a reviewer can check the same thing by hand.</p></div>
          </div>
          <div class="arm"><span class="arm-l">One pointer fails</span>
            <div class="box inv"><span class="box-t">The script stops here</span><p>It is returned. There is no option to record the failure and continue, because a warning nobody has to clear is a warning nobody clears.</p></div>
          </div>
        </div>
      </div>
      <p class="fig-cap"><b>The gate is binary on purpose.</b> Most quality tooling produces a report, and reports get skimmed under deadline. A stage that simply refuses to hand the work onward cannot be skimmed.</p>
    </div>

    <h2>A second lesson: preparation is not a scratchpad</h2>
    <div class="sec body-w">
      <p>The quote bank assembled during research is an intermediate file, so it was treated more casually than a script. Wording that had been smoothed while making notes was later inherited into finished scripts as though it were sourced material, and one subject's words had to be un-quoted after the fact.</p>
      <p>The rule that came out of it: a preparation artefact carries the same truth burden as the final page, because the final page will trust it without asking.</p>
    </div>

    <h2>Why a declared length is a creative device</h2>
    <div class="sec body-w">
      <p>Lengths differ by line and by title. What does not differ is that each title <em>declares</em> its length up front, and the machine then enforces that the script contains exactly that many pages, no more and no fewer.</p>
      <p>A whole life, or a whole epic, then has to fit a canvas that cannot stretch, and that pressure is where the narrator's voice comes from. Declaring the length per title is also what lets a 48-page biography and a short awareness title run through one pipeline without either being bent into the other's shape.</p>
    </div>

    <h2>The art is generated too, against a locked look</h2>
    <div class="sec body-w">
      <p>The pipeline does not stop at a script for someone else to draw. Frontier image models generate the characters, the backgrounds and the finished pages. The hard part is not making one good picture; it is making the four hundredth picture of the same character still look like that character.</p>
      <p>So every recurring figure carries a locked visual specification with reference art, and a figure belongs to exactly one place that owns its look even when the character appears across several programs. Props and settings are locked the same way. Generation happens against those locks rather than against a fresh description each time.</p>
      <p>One deliberate exception: for gods and legendary figures, what a reader already recognises outranks what a text technically describes. A textually defensible figure a child cannot recognise is a failed design. The sourcing contract still governs every word they say and everything they do.</p>
    </div>

    <h2>What comes out, and the part nobody sells you</h2>
    <div class="fig">
      <div class="flow flow-4">
        <div class="box"><span class="box-t">Script</span><p>One file, fixed grammar, declared length, every beat sourced.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-t">Pages</span><p>Characters, backgrounds and finished pages generated against the locked specifications.</p></div>
        <div class="arw"></div>
        <div class="box"><span class="box-t">Editorial review</span><p>A private application where the publisher's team reads each title with the source link live on every beat.</p></div>
        <div class="arw"></div>
        <div class="box inv"><span class="box-t">Production</span><p>Print-ready colour files, editable text versions, and translated editions.</p></div>
      </div>
      <p class="fig-cap"><b>Everything reads the same structure.</b> The validator, the renderer and the citation checker all use one parser, so an editor can never be shown a page different from the one that was checked.</p>
    </div>

    <div class="sec body-w">
      <p>The last box is where most generated-art pipelines quietly fail, because the tools stop once there is a picture. A printer does not want a picture. A printer wants colour separated for the press it is actually running, with black text that is genuinely one ink rather than a muddy mix of four, at a resolution the paper can hold.</p>
      <p>An editor, meanwhile, wants to change a word without regenerating a page. An image model produces neither, so we built both. One converts the colour so it survives uncoated paper. The other turns a rendered page back into a document you can edit, in the same lettering as the printed book.</p>
    </div>

    <div class="fig">
      <div class="two">
        <div class="box"><span class="box-k">Ships to the printer</span><span class="box-t">Press-ready colour</span><p>Separated for the press, with text held to a single black ink so it stays crisp instead of blurring across plates, at print resolution throughout.</p></div>
        <div class="box"><span class="box-k">Ships to the editor</span><span class="box-t">Editable pages</span><p>Rendered pages converted back into an editable document in the book's own lettering, so a correction is a text edit rather than a regeneration.</p></div>
      </div>
      <p class="fig-cap"><b>This is the dull half of the work, and it is the half that decides whether a book gets printed.</b> Generating a good-looking page is the easier part. Getting that page through a press and past an editor is what turns it into a book.</p>
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
      <p>Most publishing systems accumulate tags until nobody knows which are real. Here, one manifest declares how content may be categorised. Everything else reads from it: the resolver that turns a writer's raw tag into a canonical one, the dashboard filters, and the check that runs before anything ships.</p>
      <p>Each dimension declares what kind of thing it is, whether an item can have one value or several, and what should happen when a value has never been seen before. That last column is the interesting one.</p>
    </div>

    <div class="fig">
      <div class="tbl-scroll">
      <table class="tbl">
        <tr><th>Policy</th><th>When an unfamiliar value appears</th><th>Why</th></tr>
        <tr><td>Closed</td><td>The build fails</td><td>Some sets really are finite. A match format is one of a known list, so a value outside that list means something went wrong upstream and the build should stop.</td></tr>
        <tr><td>Curated</td><td>Accepted, and flagged for a human to confirm</td><td>Competitions and teams are real-world things somebody should name properly, but a story should never be blocked waiting for that.</td></tr>
        <tr><td>Auto-grow</td><td>Accepted and queued, never blocked</td><td>New players appear constantly. Refusing an unknown name would stop coverage of a debut, which is exactly the story worth having.</td></tr>
      </table>
      </div>
      <p class="scroll-note">Scroll the table sideways →</p>
      <p class="fig-cap"><b>Unknown values are always accepted and always surfaced.</b> Content is never held hostage to bookkeeping, and bookkeeping never silently rots. One command reports what needs a human, and the strict dimensions fail loudly.</p>
    </div>

    <h2>The manifest, and what each dimension declares</h2>
    <div class="fig">
      <div class="tbl-scroll">
      <table class="mx">
        <thead><tr><th>Dimension</th><th>Kind</th><th>Values per article</th><th>Unknown value</th><th>Role</th></tr></thead>
        <tbody>
          <tr><th>Competition</th><td>Named entity</td><td>One</td><td>Warns</td><td class="on">The spine</td></tr>
          <tr><th>Teams</th><td>Named entity</td><td>Several</td><td>Warns</td><td class="off"></td></tr>
          <tr><th>Players</th><td>Named entity</td><td>Several</td><td>Queued</td><td class="off"></td></tr>
          <tr><th>Format</th><td>Fixed list</td><td>One</td><td class="on">Fails</td><td class="off"></td></tr>
          <tr><th>Themes</th><td>Fixed list</td><td>Several</td><td class="on">Fails</td><td class="off"></td></tr>
        </tbody>
      </table>
      </div>
      <p class="scroll-note">Scroll the table sideways →</p>
      <p class="fig-cap"><b>One dimension is marked as the spine.</b> That is the one the coverage view groups by, so the newsroom sees its output organised the way it actually thinks about the season. Everything else is a filter. Declaring which is which in the manifest means the dashboard never has to guess.</p>
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
      <p class="fig-cap"><b>We decide how much damage each part could do before deciding what it may touch.</b> The engine writes well and is trusted with almost nothing. That is why running it unattended is reasonable.</p>
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

    <h2>Three verdicts, and only one of them is silent</h2>
    <div class="fig">
      <div class="flow flow-3">
        <div class="box"><span class="box-k">Verdict 1</span><span class="box-t">Match</span><p>The rows add up to a total that was read independently. Usable straight away, and nobody needs to look at the paper again.</p></div>
        <div class="arw" style="visibility:hidden"></div>
        <div class="box"><span class="box-k">Verdict 2</span><span class="box-t">Flagged</span><p>The sheet contradicts itself, or a class will not reconcile however it is read. Comes back with the specific disagreement described.</p></div>
        <div class="arw" style="visibility:hidden"></div>
        <div class="box inv"><span class="box-k">Verdict 3</span><span class="box-t">Unverified</span><p>Nothing independent to check the reading against. The figures are there and are probably right, and the system refuses to say so.</p></div>
      </div>
      <p class="fig-cap"><b>The third verdict is the one that makes the other two worth anything.</b> A system without it reports everything it managed to read as correct, and the school finds out at the exam hall. Roughly speaking, the work left for a person is the second and third piles, which is a short list rather than every sheet that arrived.</p>
    </div>

    <div class="fig">
      <div class="bars">
        <div class="bar-row"><span>Reconciled against an independent total</span><span class="bar-track"><span class="bar-fill" style="width:78%"></span></span><b>usable now</b></div>
        <div class="bar-row"><span>Flagged with a described conflict</span><span class="bar-track"><span class="bar-fill hatch" style="width:14%"></span></span><b>needs a person</b></div>
        <div class="bar-row"><span>No independent evidence available</span><span class="bar-track"><span class="bar-fill" style="width:8%;background:#fff"></span></span><b>reported as unverified</b></div>
      </div>
      <div class="key"><span><i class="solid"></i>Verified</span><span><i class="hatched"></i>Needs a person</span><span><i></i>Not claimed either way</span></div>
      <p class="fig-cap"><b>Proportions vary by batch and by how the school filled the sheet in.</b> The shape is what matters: most of a batch clears on its own, and the part that does not arrives already sorted into "we found a problem" and "we could not check".</p>
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
        out = write("case-studies", p["slug"], p["title"], p["description"],
                    p["url"], p["jsonld"], p["body"])
        print(f"wrote {out}")
    # the page was published briefly under its old name; keep that URL alive
    print(f"redirect {write_redirect('case-studies/comic-production', '/case-studies/graphic-stories/')}")


if __name__ == "__main__":
    main()
