# LITERATURE-REVIEW WORKFLOW SPECIFICATION (v1.1.0 — FIVE-LOOP ARCHITECTURE)

## 1. Purpose & Design Philosophy
This specification defines the operational protocol for executing an evidence-grounded, pass-efficient academic literature review. Rather than querying an extraction backend repeatedly on a paragraph-by-paragraph basis (`P_j → backend → paragraph`), the workflow executes extraction at the **Source Level** and **Cluster Level**, locking durable vault notes (`EXTRACTION-SATURATED` and `ADJUDICATION-SATURATED`) that downstream paragraph ledgers consume.

---

## 2. Operational Sequence Across the Five Loops

### Loop A: Project Governance & Authority Map (`00_contract/`)
1. **Define Authority Hierarchy:** Separate external literature claims from internal methodological texts, executable data repositories, and paper-level analytical governance.
2. **Enforce Citation-Admission Controls:** No source may be cited as a primary authority unless cataloged with a SHA-256 hash, ingested/verified locally, and normalized into `SRC_<KEY>.md`. Secondary references cited within primary texts must be logged in `01_corpus/candidate_references_ledger.md` and cited only with explicit mediating attribution (`AuthorA, Year, cited in AuthorB, Year`).

### Loop B: Corpus Tiering, Iterative Question Bank & Query Packs (`01_corpus/`, `02_questions/`)
1. **Assign Source Tiers (`01_corpus/`):**
   - `TIER_A_CORE`: Multi-theme anchors (1–2 comprehensive Query Pack passes).
   - `TIER_B_SUPPORTING`: Single-theme or cluster contributors (1 targeted Query Pack pass).
   - `TIER_C_CONTEXTUAL`: Bounded historical/contextual support (1 lightweight pass).
   - `TIER_D_INTERNAL_AUTHORITY`: Internal project authorities (0 external validation passes).
2. **Maintain Iterative Question Bank (`02_questions/QUESTION_BANK.md`):**
   - Synthesize atomic questions from $Q_{\text{project}} \cup Q_{\text{legacy}} \cup Q_{\text{source}}$.
   - Preserve unique Atomic Question IDs (`Q_XXX_NNN`).
   - Apply mandatory 5-state adjudication (`CONFIRMED`, `NARROWED`, `EXPANDED`, `CONFLICT`, `OUT OF SCOPE`) to all legacy discovery claims.
3. **Bundle Atomic Questions into Query Packs (`QP_<FAMILY>`):**
   - Group related atomic questions into reusable execution bundles.
   - Ensure every backend response is unpacked back into individual Atomic Question IDs during normalization.

### Loop C: Bounded Source Passes & Extraction Saturation (`03_source_notes/`)
1. **Execute Scoped Source Pass:**
   - Invoke backend adapter with explicit single-source scoping (`source_ids=[source_id]`) and consolidated Query Pack prompt.
   - Persist raw structured JSON output (preserving verbatim text, chunk IDs, and character offsets).
2. **Normalize into `SRC_<KEY>.md`:**
   - Record `EXPLICIT`, `PARTIAL`, or `NOT LOCATED` for each assigned atomic question.
   - Record exact author terminology, page/section/equation anchors, and explicit negative guardrails (`Does NOT Establish`).
   - Feed any newly discovered source-specific distinctions ($Q_{\text{source}}$) back into `QUESTION_BANK.md`.
3. **Evaluate `EXTRACTION-SATURATED` Gate:**
   - Mark `EXTRACTION_SATURATED` when all assigned atomic questions have terminal statuses, complete provenance, preserved terminology, recorded negative boundaries, and zero unresolved contradictions.
   - Lock source against routine re-querying.

### Loop D: Cluster Passes, Comparative Matrices, Citation-Chunk Contracts & Synthesis Hinges (`04_cluster_notes/`, `05_synthesis_notes/`)
1. **Construct Comparative Evidence Matrix:**
   - Cross-tabulate saturated `SRC_<KEY>.md` notes across shared atomic questions.
   - Execute a bounded multi-source comparative query (`source_ids=[id1, id2, ...]`) only when direct cross-text disambiguation is required.
2. **Lock `CITATION_CHUNK_CONTRACT` in `CLUS_<KEY>.md`:**
   - Enforce `Cluster Membership ≠ Common Claim Membership`.
   - Document candidate proposition, source-by-source support, common denominator, meaningful internal differences, permitted citation chunk, excluded members for narrowed claims, and prohibited overclaims.
   - Mark cluster `ADJUDICATION_SATURATED`.
3. **Adjudicate Cross-Literature Synthesis Hinges (`SYNTH_<KEY>.md`):**
   - Verify all 4 Hinge Criteria: (1) Conceptual Proximity, (2) Interpretive Value, (3) Non-Inflationary Boundary, and (4) Paragraph Necessity.

### Loop E: Downstream Paragraph Ledgers, Exception Queries & Prose (`06_paragraph_ledgers/`)
1. **Assemble Paragraph Ledgers (`LEDGER_P<XX>.md`):**
   - Construct sentence-by-sentence plans consuming saturated `SRC_*`, `CLUS_*`, `SYNTH_*`, and Loop A authorities.
   - Tag every sentence (`DIRECT SOURCE CLAIM`, `CLUSTER CITATION CHUNK`, `ADJUDICATED CROSS-LITERATURE HINGE`, `AUTHORIAL SYNTHESIS`, `TRANSITION`).
2. **Handle Exception Queries (If Required):**
   - Re-entry to the extraction backend is permitted **only** if one of six triggers is tripped:
     - `A: REQUIRED_CLAIM_NOT_LOCATED`
     - `B: CONFLICT`
     - `C: PROVENANCE_GAP`
     - `D: CLAIM_EXCEEDS_NOTE`
     - `E: ATTRIBUTION_AMBIGUITY`
     - `F: NEW_QUESTION`
   - *Rule:* Moving to a new paragraph $P_{j+1}$ is never a valid trigger. Exception outputs must update `SRC_<KEY>.md` or `CLUS_<KEY>.md` before ledger consumption.
3. **Human Ratification Gates:**
   - Pause for explicit human approval at: (1) Consequential Cluster Adjudications, (2) Novel Synthesis Hinges, (3) Paragraph Ledgers, (4) Manuscript Prose Insertion, and (5) Contribution/Novelty Claims.
4. **Prose Drafting & Sentence-Level Provenance Audit:**
   - After human ratification of `LEDGER_P<XX>.md`, draft prose strictly within the ratified perimeter and audit every sentence against its source/cluster/hinge pointer.

---

## 3. Regression Fixture & Optimization Metrics

1. **Regression Fixture Requirement:**
   - Gold-standard calibrated paragraphs (such as `P01`) serve as permanent regression fixtures. Any workflow refactor must reproduce the fixture's paragraph ledger from existing canonical source and synthesis notes with zero evidence loss, zero attribution weakening, and zero claim inflation.
2. **Efficiency & Quality Metrics:**
   - **Source Reuse ($R_{\text{source}}$):** Downstream themes/ledgers served per source pass.
   - **Query Reuse ($R_{\text{query}}$):** Downstream claims/matrix cells populated per query pack execution.
   - **Cluster Reuse ($R_{\text{cluster}}$):** Citation chunks/hinges/ledgers served per cluster pass.
   - **Exception Rate ($E_{\text{rate}}$):** Exception queries per paragraph ledger.
   - **Requery Rate ($Q_{\text{re}}$):** Re-queried saturated sources per total saturated sources.
