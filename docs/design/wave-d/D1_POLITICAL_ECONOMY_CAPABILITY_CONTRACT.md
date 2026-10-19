# ARS Wave D1 — Political-Economy Capability Ownership Design & Contract

- **Date:** 2026-10-14
- **Status:** COMPLETE — DESIGN CONTRACT ONLY (NO IMPLEMENTATION AUTHORIZED OR PERFORMED)
- **Artifact:** `docs/design/wave-d/D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md`
- **Governing Checkpoint / Inspected HEAD:** `917ee2f2332cef92015937bddd7337a52ef4b12d` (`refactor(governance): reconcile Wave C legacy surfaces`)
- **Evidence Base:** `docs/design/wave-d/D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md` (accepted D0/D0.1) plus the live-repository inspection recorded in §0.3
- **Binding Human Decisions Consumed:** D1-LOCK-01 through D1-LOCK-05
- **Write Scope:** This file only. No `SKILL.md`, registry, routing, eval, profile, protocol, script, tool, compatibility stub, or topology change.
- **Downstream Consumers of this Contract:** D2 (applied econometrics), D3 (heterodox macro), D4 (source criticism + PE implementation), D5 (adversarial evals), D6 (governance reconciliation)

### Label Conventions

| Label | Meaning |
|:---|:---|
| `OWNED` | `political-economy-research` is the sole canonical owner of the reasoning. |
| `CONSUMED` | PE uses another component's output or standard as an input; ownership stays with the producer. |
| `COMPOSED` | The task needs PE plus at least one other owner; each contributes only its owned reasoning. |
| `OUT OF SCOPE` | PE takes no part, or takes part only by routing elsewhere. |
| `CAPABILITY REQUIREMENT` | Something the future skill must be able to do. Binding once §24 is ratified. |
| `CANDIDATE METHODOLOGICAL IMPLEMENTATION` | A named framework or vocabulary that *might* implement a requirement. Never binding because D1 names it. |
| `FUTURE WAVE-F TARGET PATH — NOT A WAVE-D MOVE` | Path recorded for orientation only. Wave F owns physical topology. |
| `PROPOSED — NOT AUTHORIZED` | Design proposal pending a later wave's authorization. |

---

## 0. DECISION SUMMARY

### 0.1 Ownership Verdict

`political-economy-research` is the **sole canonical owner** of `political_economy_research_methodology` (D1-LOCK-01). It is an **author-side domain reasoning skill**. It designs comparative-historical inquiries, builds periodizations, specifies and adjudicates rival mechanisms against historical evidence, separates parallel from relational comparison, and calibrates how strong a causal claim the combined evidence can bear.

It does **not** own evidence retrieval, the source-criticism standard, statistical inference, formal modeling, manuscript production, economics prose, peer review, workflow control, or calibration profiles. It composes with all of them through the contracts in §7–§14 and §19.

### 0.2 What D1 Settles and What It Leaves Open

| D1 settles (semantic design) | D1 leaves to later waves |
|:---|:---|
| Capability definition and ownership test (§1) | Writing `SKILL.md` and references (D4) |
| Owned vs. non-owned task classes (§2–§3) | Writing `historical_source_criticism_protocol.md` (D4) |
| Minimal module decomposition (§4) | Choosing a process-tracing vocabulary (D4, see §16.4, §23) |
| Input and output artifact contracts (§5–§6) | Artifact serialization format (D4) |
| Interfaces with every adjacent component (§7–§14) | Econometrics refactor that honors §9 (D2) |
| Periodization, mechanism, comparison, and causal-claim contracts (§15–§18) | Macro redesign that honors §10 (D3) |
| Mixed-methods composition logic (§19) | Routing cases and gold evals (D5) |
| Leakage guard (§20) | Registry/routing reconciliation (D6) |
| Eval design targets (§22) | Physical topology (Wave F) |

### 0.3 Live-Repository Evidence Surfaced During D1

D1 re-inspected the live repository at `917ee2f`. The findings below either refine D0 or were not recorded in D0. **D0 is not modified**; where a finding qualifies D0, the qualification lives here.

| ID | Finding | Location | Classification | Effect on D1 |
|:---|:---|:---|:---|:---|
| E1 | `deep-research` already ships a **generic Comparative Case Study template** (case selection, comparison framework, within-case + cross-case analysis, rival explanations, Dimension × Case matrix). It also ships Mixed Methods (Convergent Parallel) and Content/Document Analysis templates, consumed by `research_architect_agent`. | `deep-research/references/methodology_patterns.md` lines 53–87, 121–149, 151–174; `deep-research/agents/research_architect_agent.md` lines 41–45 | `D0 QUALIFICATION`. D0 §4.4 said the repository "has no comparative methodology." More precisely: a generic, **parallel-only, atemporal** comparative template exists. There is no relational, sequence-sensitive, or historical comparative method. D0's verdict stands. | PE must **specialize, not restate**, the generic template. Activation predicate in §8.4. |
| E2 | `academic-paper` has a `humanities_interpretive` **domain evidence profile** that admits primary/archival sources at the *screening* stage ("recency is not a quality signal"). It is advisory, does not change grade aggregation, and grade aggregation is tracked separately (discipline-relative grade aggregation tracked upstream in `academic-paper/references/domain_evidence_profiles.md` lines 36–39; preserve existing `deep-research` literature-screening grade aggregation behavior unless a separately authorized upstream change is required). | `academic-paper/references/domain_evidence_profiles.md` lines 3, 13, 38 | `ADJACENT ASSET — NO OVERLAP`. Admission screening ≠ claim-relative source criticism. | The future protocol must coexist with it and must not alter admission or grading (§7.7). |
| E3 | The Material Passport `timeline.schema.json` carries an optional `events[]` array of **dated facts** cited in prose, owned by `timeline_extraction_agent` for temporal verification. | `shared/contracts/passport/timeline.schema.json`; `deep-research/agents/timeline_extraction_agent.md` | `ADJACENT ASSET — NAME-COLLISION RISK`. | PE **consumes** dated facts. Periodization boundaries are interpretive and must **not** be written into the passport timeline (§5, §15.6). |
| E4 | The shared prose protocol's verb table has one coarse row for "Historical / Archival / Qualitative Evidence." Its Domain-Delegation Boundary hands "Formal Theory & Historical Interpretation" adequacy to "discipline-specific theoretical or historiographical standards." | `shared/protocols/prose_discipline_protocol.md` lines 127, 129–139 | `DESIGNED SEAM`. The protocol explicitly expects a domain owner to supply substantive entitlement. | PE's causal-claim calibration (§18) fills that seam. It sets the evidentiary ceiling; the protocol and `econ-write` keep verb choice. |
| E5 | `econ-write` has a **Mechanisms** rule set for empirical economics papers: theory predicts M → observable X → test X. | `econ-write/SKILL.md` lines 432–437 | `ADJACENT — NO OVERLAP`. This is writing guidance for quantitative channel tests, not within-case historical mechanism reasoning. | Boundary recorded in §13. |
| E6 | `academic-paper-reviewer` has generic **Case Study** criteria and a **Paradigm Bias** pitfall. | `academic-paper-reviewer/references/review_criteria_framework.md` lines 119–128, 152 | `ADJACENT — CONSUMER SEAM`. | The reviewer may consume PE standards as domain criteria (§12). |
| E7 | The registry entry for `political_economy_research_methodology` lists **"historical source criticism"** in its description and lists only `academic-paper` as consumer. | `docs/governance/ars_registry.yaml` lines 504–516 | `GOVERNING-DOCUMENT ALIGNMENT ITEM (D6)`. Conflicts with D1-LOCK-03, which places source criticism in a shared protocol. The capability is `CANDIDATE`, so this is not a live-runtime lock conflict. | Recorded for D6. The registry is not modified in D1. |
| E8 | The target blueprint lists "institutional and archival source criticism" inside the PE layer. | `docs/design/2026-10-11-ars-target-architecture/00_TARGET_STATE_ARCHITECTURE.md` lines 249–259 | `GOVERNING-DOCUMENT ALIGNMENT ITEM (D6)`. The blueprint predates D1-LOCK-03; the lock governs. | Same as E7. |
| E9 | The workspace architecture defines **Project Overlays** as the home for project-specific constraints (e.g., "specific institutional dummy definitions"). Overlays may not modify core skills or shared protocols. | `docs/design/2026-10-11-ars-target-architecture/17_WORKSPACE_CAPSULE_ARCHITECTURE.md` lines 185–190 | `DESIGNED SEAM`. | This is where project-specific periods, case lists, and dates belong (§20). |
| E10 | `profiles/scholars/kevin-young.md` §3.2 hard-codes a US periodization (mid-1950s, 1970s, 1980s). §3.3 asserts macro outcomes are "fundamentally mediated by class struggle." | `profiles/scholars/kevin-young.md` §3.2–§3.3 | `CORRECTLY PROFILE-RESIDENT`. Legitimate as calibration; illegitimate as canonical PE defaults. | Leakage test fixture for §14 and §20. |

### 0.4 Governance Status

- **LIVE-ARCHITECTURE LOCK CONFLICT: none detected.** All post-Wave-C locks remain expressed by the live repository (regression evidence in the D1 validation record).
- **GOVERNING-DOCUMENT ALIGNMENT ITEMS (for D6; not resolved here):**
  - **G1:** Registry description of `political_economy_research_methodology` includes source criticism (E7).
  - **G2:** Target blueprint §5.3 places source criticism inside PE (E8).
  - **G3 (carried from D0):** `GOVERNING-DOCUMENT TIMING INCONSISTENCY: public-scholarship decomposition`. Execution stays `DEFERRED — FUTURE AUTHORIZATION REQUIRED`.
  - **G4:** D0 §4.4 qualification regarding the existing generic comparative template (E1).

---

## 1. CANONICAL CAPABILITY DEFINITION

```text
CAPABILITY ID:   political_economy_research_methodology
CANONICAL OWNER: political-economy-research
TYPE:            DOMAIN_SKILL (author-side reasoning capability)

DEFINITION:
The reusable author-side reasoning required to design, construct, and
adjudicate explanations of historically situated political-economic
configurations and their change. Specifically:

  (a) specifying cases, their temporal scope, and their relations;
  (b) constructing historically defensible periodizations;
  (c) formulating rival mechanisms (involving states, institutions,
      classes, coalitions, firms, and other actors) and deriving their
      observable implications;
  (d) adjudicating those mechanisms against within-case and cross-case
      historical evidence;
  (e) distinguishing parallel from relational comparison; and
  (f) calibrating the admissible strength of causal claims to the
      combined evidentiary record.

It CONSUMES, and never owns: evidence retrieval, the historical
source-criticism standard, statistical inference, formal modeling,
manuscript production, prose standards, peer review, workflow control,
and calibration profiles.
```

### 1.1 Ownership Test

A task is `OWNED` by `political-economy-research` when **all three** of these hold:

1. **Explanandum:** The question concerns *how, why, when, or in relation to what* a historically situated political-economic configuration formed, persisted, changed, or differed across cases.
2. **Evidentiary basis:** Answering it requires reasoning over historical, institutional, documentary, or sequence evidence. That evidence may be combined with other kinds, but historical evidence must be one of the bases.
3. **Deliverable:** The required output is a research design, periodization, mechanism specification, rival-mechanism adjudication, comparison design, or calibrated causal claim. It is not a search result, a statistic, a derivation, a manuscript, a prose edit, or a referee report.

If (1) and (2) hold but (3) names another component's deliverable, the task is `COMPOSED`. If (2) fails, the task is not PE-owned even if it uses political-economy vocabulary.

### 1.2 Identity Attributes

| Attribute | Value |
|:---|:---|
| Component | `political-economy-research` |
| Semantic role | `DOMAIN_SKILL` |
| Stance | Author-side methodology; no review, verdict, or editorial authority |
| Theory stance | Theory-pluralist and non-doctrinal (D1-LOCK-02): theories enter as hypotheses, mechanisms, concepts, or interpretive lenses without privileging any school |
| Runtime path (when created in D4) | `political-economy-research/` at repository root, per routing Rule 8 (`docs/governance/ROUTING_AND_PRECEDENCE.md` line 21) |
| Target path | `skills/domain/political-economy-research` — FUTURE WAVE-F TARGET PATH — NOT A WAVE-D MOVE |
| Current status | `CANDIDATE` in registry; ownership now locked (D1-LOCK-01); implementation pending D4 |

---

## 2. OWNED CAPABILITIES

| ID | Owned Capability | Owned Reasoning | Explicitly Not Included |
|:---|:---|:---|:---|
| **O1** | Comparative-historical research design | Explanandum specification; case construction and unit of analysis; scope conditions; temporal boundaries; within-case vs. cross-case inference strategy; sequence-sensitive design; choice of comparison mode (parallel / relational / hybrid) | Generic method selection for non-historical studies (`deep-research`); sampling statistics (`applied-econometrics-pe`) |
| **O2** | Periodization | Period criteria; boundary typing (historical-institutional / statistical break / cyclical / convenience); boundary justification; alternative periodizations; revision provenance | Break detection and break-test choice (`applied-econometrics-pe`); dated-fact verification (`deep-research` timeline) |
| **O3** | Mechanism specification and process tracing | Decomposing mechanisms into actor- or institution-level steps; observable implications per step; rival mechanisms; sequence and timing evidence; negative evidence; evidential diagnosticity; equifinality and conjunctural causation; scope of mechanism claims | Source reliability standards (shared protocol); formal derivation of mechanism dynamics (`heterodox-macro-modeling`); econometric channel tests (`applied-econometrics-pe`) |
| **O4** | Comparative-relational analysis | Testing whether cases are independent; mapping relations (trade, finance, monetary hierarchy, institutions, geopolitics, migration, production networks, technology, debt, center–periphery); evidence requirements for each comparison mode | Formal open-economy representation (`heterodox-macro-modeling`); estimating spillovers (`applied-econometrics-pe`) |
| **O5** | Actor and institutional mechanism operationalization | Turning theories about states, classes, fractions, coalitions, firms, labor organizations, parties, bureaucracies, and international actors into competing, operationalized, testable mechanisms, *without* privileging any theory | Theory exposition as doctrine (`OUT OF SCOPE`, D1-LOCK-02); normative political theory |
| **O6** | Historical causal adjudication and claim calibration | Combining evidence across sources and mechanism steps into a verdict on rival explanations; calibrating substantive causal strength; downgrade triggers | Verb and phrasing selection (`prose_discipline_protocol` / `econ-write`); referee-side adjudication (`academic-paper-reviewer`) |
| **O7** | Historical inferential synthesis | Synthesizing already-adjudicated cross-method inputs into historical mechanism explanations without altering source verdicts or claiming integration authority over non-historical inferential tasks (§19.2) | Primary integration of non-historical inferential tasks (statistical relations, formal model behavior, or manuscript drafting; §19.2) |

### 2.1 Task Classification Matrix

| # | Task | Classification | Primary Owner | PE Role |
|:---|:---|:---|:---|:---|
| 1 | Design a two-case comparison of exchange-rate regime change | `OWNED` | PE | O1, O4 |
| 2 | Decide whether two cases are independent or relationally linked | `OWNED` | PE | O4 |
| 3 | Build and justify periods for a 1930–1990 study | `OWNED` | PE | O2 |
| 4 | Find archival documents on a negotiation | `OUT OF SCOPE` (PE may send an evidence request) | `deep-research` | Requester only |
| 5 | Assess whether a cable reliably evidences a claimed decision | `CONSUMED` standard / `COMPOSED` task | Shared protocol applied by the claim holder | Supplies claim; consumes assessment |
| 6 | Adjudicate whether pressure, coalition change, or fiscal crisis explains a policy reversal | `OWNED` | PE | O3, O6 |
| 7 | Turn "accumulation regime" and "elite coalition" into rival testable mechanisms | `OWNED` | PE | O5 |
| 8 | Test for structural breaks in a wage-share series | `OUT OF SCOPE` | `applied-econometrics-pe` | Consumes result |
| 9 | Decide whether a detected break marks a historical boundary | `COMPOSED` | PE (classification) + econometrics (break evidence) | O2 |
| 10 | Interpret what a coefficient means statistically | `OUT OF SCOPE` | `applied-econometrics-pe` | — |
| 11 | Assess whether a coefficient corroborates a historical mechanism | `COMPOSED` | PE (mechanism claim) + econometrics (statistical entitlement) | O3, O6, O7 |
| 12 | Derive a BOP-constrained growth model's steady state | `OUT OF SCOPE` | `heterodox-macro-modeling` | — |
| 13 | Judge whether a period's institutions fit a model's closure assumption | `COMPOSED` | Macro (closure) + PE (historical fit evidence) | O2, O5 |
| 14 | Draft the historical-background section of a paper | `OUT OF SCOPE` (consumes PE artifacts) | `academic-paper` (+ `econ-write` if economics) | Artifact supplier |
| 15 | Rewrite a results paragraph's causal verbs | `OUT OF SCOPE` | `econ-write` / prose protocol | Supplies the substantive causal-strength ceiling only |
| 16 | Check author-side whether a chapter's process tracing holds | `OWNED` | PE | O3, O6 (diagnostic artifacts, no verdict) |
| 17 | Produce a referee report on a comparative-historical paper | `OUT OF SCOPE` | `academic-paper-reviewer` | Standard may be consumed |
| 18 | Summarize what the literature says caused a crisis | `OUT OF SCOPE` | `deep-research` | — |
| 19 | Adjudicate between the literature's rival causal accounts using evidence | `OWNED` | PE | O3, O6 |
| 20 | Explain dependency theory's tenets | `OUT OF SCOPE` (general assistance / deep-research) | None (theory is an input, not a canonical capability owned by PE; §3.2) | — |
| 21 | Run a full research-to-publication workflow on a PE topic | `OUT OF SCOPE` (invoked as delegate) | `academic-pipeline` | Delegate for O1–O7 work |
| 22 | Simulate how a named committee member would critique periodization | `OUT OF SCOPE` | `academic-paper-reviewer` + profile | — |
| 23 | Translate a PE paper into a public essay | `OUT OF SCOPE` | `editor-jacobin-lat` (decomposition deferred) | — |
| 24 | Verify the stock-flow consistency of a model | `OUT OF SCOPE` | `heterodox-macro-modeling` | — |
| 25 | Historical explanation synthesizing archives, a VAR, and a growth model | `COMPOSED` | PE for historical mechanism synthesis; each component retains jurisdiction over its own evidentiary verdict (§19.2) | O7 |

---

## 3. EXPLICIT NON-OWNERSHIP

| Task Class | Canonical Owner | PE Relationship | Evidence / Basis |
|:---|:---|:---|:---|
| Search, retrieval, literature mapping, bibliographic synthesis, source discovery | `deep-research` | `CONSUMED` | Routing Rule R9; registry `literature_synthesis_search` |
| Citation existence, DOI/venue verification, predatory-venue screening | `deep-research` (`source_verification_agent`) | `CONSUMED` | `deep-research/agents/source_verification_agent.md` |
| Dated-fact and citation-temporal verification | `deep-research` (`timeline_extraction_agent`) | `CONSUMED` | E3 |
| Generic method selection and generic case-study templates for non-historical studies | `deep-research` (`research_architect_agent`) | `COMPOSED` via specialization predicate (§8.4) | E1 |
| Claim-relative historical source-criticism **standard** | `shared/protocols/historical_source_criticism_protocol.md` (D4) | `CONSUMED` | D1-LOCK-03 |
| Econometric estimation, stochastic admissibility, time-series testing, break detection, parameter evidence, econometric identification | `applied-econometrics-pe` (runtime: `umass-applied-econometrics`) | `CONSUMED` / `COMPOSED` | D0 §5; §9 |
| Formal equations, closures, SFC, BOP formalization, dynamic stability, theoretical macro mechanisms | `heterodox-macro-modeling` (runtime: `heterodox-economics-review`) | `CONSUMED` / `COMPOSED` | D0 §6; D1-LOCK-04; §10 |
| Manuscript lifecycle, section architecture, drafting, citation integration, formatting | `academic-paper` | Supplies artifacts | Routing Rules R1, R3; §11 |
| Economics prose, BLUF, sentence style, results rhetoric, identification rhetoric | `econ-write` | Supplies the substantive causal-strength ceiling | Routing Rule R2; §13 |
| Cross-domain prose discipline and verb calibration wording | `shared/protocols/prose_discipline_protocol.md` | Supplies the substantive causal-strength ceiling | E4 |
| Simulated external peer review, referee reports, editorial decisions, scored evaluation | `academic-paper-reviewer` | Standard may be consumed by reviewer | Routing Rule R4; §12 |
| Workflow sequencing, stage control, Material Passport state | `academic-pipeline` | Invoked as delegate | Routing Rule R7 |
| Scholar, advisor, committee, venue calibration | `profiles/*` | Calibration input only (§14) | `profiles/PROFILE_CONTRACT.md` lines 48–52 |
| Change-control verification | `EDITORIAL_GOVERNANCE_PORT.md` + `scripts/revision_guard.py` | `OUT OF SCOPE` | Routing Rule R11 |
| Project-specific cases, dates, periods, dummies, doctrine | Workspace Project Overlay | Parameter input only (§20) | E9 |
| Public-scholarship translation | `editor-jacobin-lat` (decomposition `DEFERRED — FUTURE AUTHORIZATION REQUIRED`) | `OUT OF SCOPE` | D0 §0 item 6 |
| Encyclopedic theory exposition (Marxism, state theory, regulation, SSA, dependency, Gramscian, Poulantzian, institutionalist, IPE doctrines) | None — not a canonical ARS capability | `THEORY IS AN INPUT, NOT A CANONICAL DOCTRINE OWNED BY PE` (§3.2) | D1-LOCK-02; operationalized via O5/M3, not maintained as canonical doctrine |
| Normative political philosophy and policy advocacy | None | `OUT OF SCOPE` | Methodology scope (D1-LOCK-02) |
| Archival logistics (access requests, finding aids, travel) | None | `OUT OF SCOPE` | Not a reasoning capability |

### 3.1 Hard Prohibitions

`political-economy-research` must **never**:

1. Execute searches or present itself as an evidence source.
2. Define or restate the historical source-criticism standard. It applies the shared protocol.
3. Estimate, test, or certify statistical relationships, or rule on stochastic admissibility.
4. Derive, solve, or certify formal models, closures, SFC structures, or stability conditions.
5. Draft manuscript sections or run a manuscript lifecycle.
6. Prescribe sentence-level prose, verb lists, BLUF, or AI-pattern rules.
7. Emit referee reports, editorial decisions, acceptance judgments, scores, or persona critiques.
8. Treat any profile as a source of methodology, evidentiary thresholds, or conclusions.
9. Assert any theory of the state, class, or dependency as repository truth.
10. Embed project-specific cases, dates, periods, estimates, or advisor preferences in canonical instructions.

### 3.2 Theory Is an Input, Not a Canonical Doctrine Owned by PE

`political-economy-research` does **not** refuse to reason about theory. Rather, it treats theory as an active, vital input to empirical and historical investigation, while strictly declining to own or maintain theoretical systems as canonical repository doctrine:

1. **How PE uses theory:**
   - **Concept formation:** Defining analytical categories (e.g. accumulation regimes, monetary constraints, institutional forms) with explicit scope.
   - **Mechanism specification:** Translating verbal theoretical frameworks into step-by-step causal chains with observable traces (O5, M3).
   - **Actor, coalition, and relation identification:** Identifying relevant classes, fractions, state apparatuses, international linkages, and institutional configurations.
   - **Rival generation:** Generating non-trivial alternative explanations to prevent confirmation bias (M-2).
2. **What PE does not do:**
   - Maintain an encyclopedia or authoritative canon of Marxism, dependency theory, regulation theory, post-Keynesian economics, or institutionalism.
   - Assert any theory of the state, class, or development as repository truth.
   - Adjudicate disputes within pure theoretical doctrine disconnected from empirical or historical evidence.

In short: PE operationalizes, contrasts, tests, and evaluates theories against evidence. It does not own or maintain theory encyclopedias.

---

## 4. INTERNAL CAPABILITY MODULES

### 4.1 Evaluation of the Candidate Five-Reference Structure

| Candidate Reference | D1 Disposition | Reason |
|:---|:---|:---|
| `research_design.md` | **ACCEPT — merged with comparative-relational analysis** as `research_design_and_comparison.md` | Comparison mode is a design decision about whether units are independent. Splitting it from case construction would leave two shallow modules with circular cross-references. |
| `periodization.md` | **ACCEPT** | Distinct reasoning load. It also carries the econometrics interface (§9, §15). |
| `mechanism_reasoning.md` | **ACCEPT — absorbs actor/institutional operationalization (O5)** | Actor- and institution-level analysis exists to produce rival mechanisms. A separate "actors" module would restate theory and invite canon creep. |
| `comparative_relational_analysis.md` | **MERGED** into `research_design_and_comparison.md` | See first row. |
| `causal_claim_calibration.md` | **ACCEPT — absorbs mixed-methods integration rules (O6, O7)** | Integration conflicts feed the claim class directly. A separate mixed-methods module would duplicate the downgrade logic. |

**Rejected modules:**

- `source_criticism.md` inside PE. Prohibited by D1-LOCK-03; the standard belongs to the shared protocol.
- `theory_frameworks.md`. Prohibited by D1-LOCK-02.
- A separate `templates/` directory. Deferred. Artifact field specs live with the module that produces them (§6). D4 may add one only if it can show reuse across modules.

**Result:** `SKILL.md` + **four** references. That is fewer and stronger modules than the five-file candidate.

### 4.2 Module Specifications

#### M0 — `SKILL.md` (Capability Charter & Composition Router)

| Field | Specification |
|:---|:---|
| Purpose | Declares the capability, the ownership test (§1.1), activation predicates, hard prohibitions (§3.1), the composition contract (§7–§14, §19), the artifact index (§6), and the leakage guard (§20). |
| Owned reasoning | Deciding which module(s) a task needs and which other components must be composed in. It does not perform their reasoning. |
| Inputs | User task; workspace manifest (active protocols, overlays, profiles). |
| Outputs | Module invocation plan; composition requests (evidence request, econometric request, model request); final artifact bundle. |
| Dependencies | M1–M4; shared prose and historical-source protocols; adjacent skills by contract only. |
| Why not redundant | It is the only place PE's boundaries are stated as operating rules. Routing *governance* stays in `ROUTING_AND_PRECEDENCE.md`; this file holds the skill-local operating charter. |

#### M1 — `references/research_design_and_comparison.md`

| Field | Specification |
|:---|:---|
| Purpose | Turn a political-economy question into a comparative-historical design, including the choice of comparison mode. |
| Owned reasoning | O1 + O4: explanandum specification; case and unit construction; scope conditions; temporal scope; within-case vs. cross-case inference; sequence sensitivity; independence diagnostics; relation mapping; parallel / relational / hybrid mode selection. |
| Inputs | Research question; candidate cases; theory inputs as hypotheses; dated facts; relation evidence (via `deep-research`); workspace overlay parameters. |
| Outputs | A1 Design Brief; A5 Case-Relation Map (conditional). |
| Dependencies | `deep-research` for retrieval; M2 for temporal scope; M3 for mechanism-driven case selection. |
| Why not redundant | `deep-research` Pattern 2 is generic, parallel-only, and atemporal (E1). M1 adds relational mode, sequence, scope over time, and historical case construction. It does not restate Pattern 2's generic steps; it references them as the non-historical baseline. |

#### M2 — `references/periodization.md`

| Field | Specification |
|:---|:---|
| Purpose | Build and defend historically justified periods, keeping them distinct from statistical, cyclical, and convenience partitions. |
| Owned reasoning | O2: period criteria; boundary typing; justification; transition intervals; alternative periodizations; revision provenance; anti-reverse-engineering discipline. |
| Inputs | Explanandum and period criterion; dated facts (incl. passport `timeline.yaml` events); historical evidence with protocol assessments; econometric break evidence (optional). |
| Outputs | A2 Periodization Ledger; hypothesized break dates exported to econometrics. |
| Dependencies | Shared protocol (for boundary evidence); `applied-econometrics-pe` (break evidence in, testable dates out). |
| Why not redundant | No component owns historical boundary reasoning. Econometrics owns break *detection*; the passport timeline owns dated *facts*; neither classifies boundaries. |

#### M3 — `references/mechanism_reasoning.md`

| Field | Specification |
|:---|:---|
| Purpose | Specify rival mechanisms and adjudicate them against historical evidence. |
| Owned reasoning | O3 + O5: mechanism decomposition; actor and institutional operationalization; observable implications; sequence and timing; negative evidence; diagnosticity; equifinality; conjunctural causation; scope of mechanism claims. |
| Inputs | Theory inputs as hypotheses; Design Brief; Periodization Ledger; source–claim assessment records (shared protocol); econometric and model-derived implications. |
| Outputs | A3 Mechanism Map; A4 Claim–Evidence–Mechanism Matrix; evidence requests to `deep-research`. |
| Dependencies | Shared protocol; `deep-research`; optionally `applied-econometrics-pe` and `heterodox-macro-modeling` for implications. |
| Why not redundant | `econ-write` covers how to *write* quantitative mechanism sections (E5). `econ-write/identification-strategies.md` covers microeconometric identification. Neither covers within-case historical mechanism adjudication. |

#### M4 — `references/causal_claim_calibration.md`

| Field | Specification |
|:---|:---|
| Purpose | Decide how strong a causal claim the combined record admits, and resolve cross-method conflicts without override. |
| Owned reasoning | O6 + O7: substantive causal-strength calibration; candidate claim-class ladder; downgrade triggers; convergence/divergence handling; inferential-task jurisdiction rule (§19.2). |
| Inputs | A3, A4; econometric results with admissibility status; model implications; source–claim assessments. |
| Outputs | Causal claim calibration (proposed format A6; substantive causal-strength ceiling for `academic-paper`, `econ-write`, and the prose protocol). |
| Dependencies | `prose_discipline_protocol` (consumes substantive causal-strength ceiling for phrasing); `econ-write` (economics phrasing within ceiling). |
| Why not redundant | The prose protocol rules on *wording* and explicitly leaves substantive historical entitlement to domain standards (E4). M4 supplies that substantive causal-strength ceiling and nothing about wording. |

---

## 5. INPUTS

| ID | Input Class | Examples | Producer / Provenance | How PE Uses It | Constraint |
|:---|:---|:---|:---|:---|:---|
| I1 | Research question / explanandum | "Why did country X abandon capital controls when it did?" | User / `academic-paper` intake / `academic-pipeline` | Anchors O1 and inferential jurisdiction (§19.2) | Must be restated as an explanandum with scope before design proceeds |
| I2 | Cases and candidate cases | Countries, sectors, regimes, firms, episodes | User / Workspace overlay | Case construction (M1) | Case list is a project parameter, never canonical (§20) |
| I3 | Dated facts / timelines | Event dates, legal enactments, office tenures | `deep-research` (`timeline.yaml` events), user | Sequence evidence; boundary anchoring (M2, M3) | Dated facts ≠ periods; PE never writes interpretive periods into the passport timeline |
| I4 | Historical evidence + source–claim assessments | Archival records, official documents, memoirs, oral histories, institutional records, press | Retrieved by `deep-research`; assessed under the shared protocol | Mechanism adjudication (M3), boundary justification (M2) | PE never upgrades a source beyond its protocol assessment for that claim |
| I5 | Secondary historiography | Monographs, historical syntheses | `deep-research` | Rival-explanation inventory; context | Literature claims are hypotheses to adjudicate, not verdicts |
| I6 | Theory inputs | Class conflict, elite coalition, bureaucratic capacity, institutional layering, monetary constraint, accumulation regime, electoral coalition | User / literature | Converted into rival mechanisms (M3/O5) | Entered as hypotheses; never as presumed truth (D1-LOCK-02, §3.2) |
| I7 | Econometric results | Break dates and CIs, coefficients, Granger/TY results, cointegration outcomes, with admissibility status | `applied-econometrics-pe` | Corroborating or contradicting observable implications (M3, M4) | Consumed with their admissibility status; PE never re-estimates or reinterprets significance |
| I8 | Formal-model implications | Predicted regime behavior, stability conditions, BOP-constraint implications | `heterodox-macro-modeling` | Source of mechanisms and observable implications (M3) | Model output is never historical evidence (§19.3) |
| I9 | Workspace project overlay | Declared periods, case list, alignment tolerance, illustrative fixtures | Workspace (17 §9) | Parameterizes M1/M2 | Overlay parameters are logged as project choices in artifacts |
| I10 | Profile calibration | Advisor or committee emphases | `profiles/*` | Opt-in calibration only (§14): may add questions or rival mechanisms when explicitly activated | **BINDING INVARIANT: Profiles are NEVER default inputs to PE.** Consumed ONLY when explicitly requested by user or authorized workflow. Never alters thresholds, never removes rivals, never presumes conclusions. |

---

## 6. OUTPUTS

### 6.1 Candidate Artifact Evaluation

| Candidate | Verdict | Reasoning-Discipline / Reproducibility Gain |
|:---|:---|:---|
| MECHANISM MAP | **ACCEPT (A3)** | Forces step-level decomposition and observable implications. Makes it visible which steps are unevidenced. |
| PERIODIZATION LEDGER | **ACCEPT (A2)** | Records boundary type, justification, and whether the boundary was set before estimation. This is the main guard against reverse-engineered periods. |
| CLAIM–EVIDENCE–MECHANISM MATRIX | **ACCEPT (A4)** | Ties every evidence item to the claims and mechanisms it bears on, with diagnosticity. |
| RIVAL EXPLANATION MATRIX | **MERGED into A4** | A4 has required rival-mechanism columns. A separate artifact would duplicate the evidence rows. |
| CASE-RELATION MAP | **ACCEPT (A5) — conditional** | Needed only in relational or hybrid mode, or when independence is contested. Otherwise it is overhead. |
| HISTORICAL EVIDENCE LEDGER | **REASSIGNED — not a PE artifact** | Source-level, claim-relative assessment records are the **shared protocol's** output (D1-LOCK-03). If PE owned the format, it would co-own the standard. PE consumes them as I4 and cites them in A4. |
| CAUSAL CLAIM CALIBRATION TABLE | **ACCEPT (A6) — format proposed, requirement locked** | The single handoff that carries evidentiary entitlement to writing components. Prevents rhetorical inflation downstream. Explicit table reserved for high-stakes outputs (§6.2). |
| *(added)* COMPARATIVE-HISTORICAL DESIGN BRIEF | **ACCEPT (A1) — conditional** | The user's "research-design structures" and "comparison designs" need a defined container. Without one, design reasoning stays implicit. |

> **Proposed Formats vs. Locked Obligations:** Artifact formats A1–A5 and A6 are proposed implementation architecture. The underlying reasoning and calibration obligations they embody are locked. D4 implementation holds design discretion over exact layout and serialization.

### 6.2 Accepted Artifact Contracts

#### A1 — Comparative-Historical Design Brief

- **Purpose:** Make the design explicit and auditable before evidence is gathered.
- **Requirement:** `REQUIRED` for design tasks; `OPTIONAL` otherwise.
- **Consumers:** `academic-paper` (methods/design section), `deep-research` (retrieval scoping), `academic-paper-reviewer` (as author's stated design).
- **Required fields:**
  - `explanandum` — the outcome or variation to be explained, with scope
  - `cases` — list with unit of analysis
  - `case_selection_rationale` — theoretical/purposive grounds; known selection risks
  - `temporal_scope` — start/end with justification (links to A2 when periods are analytical)
  - `scope_conditions` — conditions under which conclusions are claimed to hold
  - `comparison_mode` — `SINGLE_CASE` | `PARALLEL` | `RELATIONAL` | `HYBRID`, with justification (§17)
  - `inference_strategy` — within-case / cross-case / combined; what each is expected to establish
  - `rival_explanations_inventory` — initial list (feeds A3/A4)
  - `evidence_plan` — evidence types needed per rival, routed as requests to `deep-research`
  - `composition_plan` — which other components are needed (econometrics, macro) and why
  - `project_parameters_used` — overlay-supplied values, labeled as project choices

#### A2 — Periodization Ledger

- **Purpose:** Record every analytically used boundary with its type and justification.
- **Requirement:** `REQUIRED` whenever periods carry analytical or causal weight; `OPTIONAL` for purely descriptive chronology.
- **Consumers:** `applied-econometrics-pe` (hypothesized break dates), `academic-paper`, `academic-paper-reviewer`.
- **Required fields per boundary:** see §15.4.
- **Ledger-level fields:** `period_criterion` (what defines a period in this study), `alternative_periodizations_considered`, `sensitivity_note` (which conclusions change under alternatives).

#### A3 — Mechanism Map

- **Purpose:** Specify each candidate mechanism as a chain of steps with observable implications.
- **Requirement:** `REQUIRED` for any mechanism or causal claim; one map per rival mechanism.
- **Consumers:** M4; `academic-paper`; `heterodox-macro-modeling` / `applied-econometrics-pe` when implications are formal or statistical.
- **Required fields:**
  - `mechanism_id`, `label`, `theoretical_source` (as hypothesis, with citation)
  - `antecedent_conditions`
  - `steps[]` — each with `actor_or_institution`, `action_or_process`, `expected_trace` (what evidence should exist if the step occurred), `expected_timing`
  - `response` and `downstream_consequence`
  - `scope_conditions`
  - `implications_by_method` — historical / econometric / formal-model implications, each tagged with its owning component

#### A4 — Claim–Evidence–Mechanism Matrix (with rival columns)

- **Purpose:** Adjudicate rival mechanisms transparently.
- **Requirement:** `REQUIRED` whenever two or more plausible explanations exist. Declaring "no plausible rival" is itself a recorded claim that needs justification.
- **Consumers:** M4; `academic-paper-reviewer` (as author's evidence record).
- **Required fields:**
  - Rows: `evidence_item_id` → linked protocol assessment record (I4) or econometric/model result (I7/I8)
  - `claim_supported` — the atomic claim this item bears on
  - Columns per rival mechanism: `predicted` (expected / not expected / silent), `observed`, `diagnosticity` (how much more expected under this mechanism than under rivals — qualitative scale)
  - `negative_evidence_flag` and `trace_expectation_basis` (why the absent trace would have been recorded and survived)
  - `contradictions_unresolved`
  - `evidence_gaps` → evidence requests issued

#### A5 — Case-Relation Map

- **Purpose:** Document relations that make cases non-independent.
- **Requirement:** `REQUIRED` in `RELATIONAL` or `HYBRID` mode, or when independence is contested; otherwise `NOT PRODUCED`.
- **Consumers:** M1, M3; `heterodox-macro-modeling` (if relations are to be formalized).
- **Required fields:** `case_pair`, `relation_type` (§17.3 typology), `direction_and_asymmetry`, `period_of_operation` (linked to A2), `evidence_for_relation` (protocol-assessed), `hypothesized_effect_on_outcomes`, `independence_implication`.

#### A6 — Causal Claim Calibration Table

- **Purpose:** Carry each causal claim's admissible strength to writing components.
- **Status:** `A6 FORMAT: PROPOSED` · `CAUSAL CALIBRATION REQUIREMENT: LOCKED`
- **Requirement:** D4 implementation may satisfy the locked causal calibration requirement proportionally based on query stakes:
  - *Implicit calibration* in short answers or exploratory notes;
  - *Compact inline claim tags* (e.g., `[Class: C4 | downgrade: single-source]`) in intermediate outputs;
  - *Explicit A6 table* only for high-stakes outputs (theses, dissertation chapters, formal articles, evaluated publications, or formal evals).
- **Consumers:** `academic-paper`, `econ-write`, `prose_discipline_protocol` (verb selection), `academic-paper-reviewer`.
- **Required fields:**
  - `claim_id`, `claim_text_neutral` (stated without evaluative verbs)
  - `claim_class` (§18.2)
  - `admissibility_conditions_met` / `unmet`
  - `evidence_basis` → A4 rows
  - `method_status` — historical / econometric / formal: `CONVERGENT` | `COMPLEMENTARY` | `DIVERGENT` | `ABSENT` (§19.4)
  - `downgrade_triggers_applied`
  - `scope` (cases, periods)
  - `strongest_admissible_class` and `upgrade_path` (what evidence would justify a stronger class)

### 6.3 Output Invariants

1. Artifacts are analytical records, not prose. They contain no manuscript sections, no referee content, and no editorial decisions.
2. Every artifact field that carries a project-specific value cites its source (overlay, user, or evidence).
3. Serialization (Markdown table vs. YAML) is a D4 decision. No artifact becomes a Material Passport sidecar without a D6 schema decision.
4. While artifact formats A1–A5 and A6 are proposed implementation structures, the analytical obligations they embody (auditable design, non-reverse-engineered boundaries, rival mechanism tracing, relational justification, and causal calibration) are binding.

---

## 7. HISTORICAL EVIDENCE INTERFACE

### 7.1 Three-Way Boundary

```text
deep-research
    DISCOVERS and RETRIEVES evidence; verifies existence, citation accuracy,
    and dated facts.

shared/protocols/historical_source_criticism_protocol.md   (conceptual; built in D4)
    SUPPLIES the claim-relative evidentiary assessment standard.
    Applied by whichever component holds the claim under assessment.

political-economy-research
    USES assessed evidence to CONSTRUCT and ADJUDICATE explanations.
    Aggregates across sources, steps, and rivals.
```

**Ownership rule:** The protocol owns the *standard*. Applying it is an act of consumption by the claim holder. PE applies it to mechanism, boundary, and relation claims. `deep-research` applies it to factual claims it is fact-checking. `academic-paper-reviewer` applies it when evaluating a manuscript's evidence. None of them co-owns it.

### 7.2 Activation Predicate (Conditional Activation, D1-LOCK-03)

The protocol is **active** for a claim when the claim's support materially depends on any of:

- archival or documentary records (official, corporate, organizational, diplomatic, legal, private papers);
- institutional records (minutes, regulations, statutes, internal reports);
- retrospective testimony (memoirs, oral histories, interviews about past events);
- contemporaneous non-scholarly accounts (press, pamphlets, speeches) used as evidence of events, beliefs, or decisions;
- historical secondary works used as evidence of *events*, not as literature positions.

It is **inactive** (other standards govern) for:

- statistical inference on datasets (`applied-econometrics-pe`);
- experimental or quasi-experimental evidence (`econ-write` identification standards; domain methods);
- generic literature-quality assessment (`deep-research` grading);
- formal derivations (`heterodox-macro-modeling`).

**Boundary case — historically constructed statistics:** Historical national accounts and reconstructed series are themselves constructed sources. Whether the protocol applies to their *construction provenance* (who compiled them, with what sources, with what revisions), while econometrics retains *stochastic admissibility*, is open question **Q4** (§23).

### 7.3 Request Contract (Claim Holder → Protocol)

The interface must make each assessment **claim-relative**. A request carries:

| Field | Content |
|:---|:---|
| `claim` | One atomic claim (e.g., "the finance ministry anticipated the devaluation before date D") |
| `claim_type` | `OCCURRENCE` · `TIMING` · `ACTOR_BELIEF_OR_PERCEPTION` · `ACTOR_INTENTION` · `DECISION_PROCESS` · `INSTITUTIONAL_RULE` · `MAGNITUDE` · `ABSENCE` · `RELATION` |
| `source_descriptor` | Identity, type, date, producer, custody (as retrieved) |
| `evidentiary_role_sought` | What the claim holder wants the source to establish |

### 7.4 Return Contract (Protocol → Claim Holder)

The eventual protocol output must cover at least the following dimensions for each **(source, claim)** pair:

| # | Dimension | Assessment Question |
|:---|:---|:---|
| 1 | Provenance | Where does the document come from, and through what chain of custody? |
| 2 | Authenticity | Is it what it purports to be? |
| 3 | Producer | Who made it, in what capacity? |
| 4 | Institutional standpoint | What mandate, interest, or position shaped its production? |
| 5 | Intended audience | For whom was it written, and how does that shape content? |
| 6 | Incentives for candor/concealment | What pressures toward accuracy, self-protection, persuasion, or deception applied? |
| 7 | Access to information | Was the producer positioned to know what the claim requires? |
| 8 | Temporal proximity | How close in time is it to the events? |
| 9 | Retrospective reconstruction | Is it later recollection, justification, or rationalization? |
| 10 | Archival survival/selection | What survived, what was destroyed, withheld, or never recorded, and why? |
| 11 | Corroboration | Do independent sources agree? (Independence must itself be assessed.) |
| 12 | Contradiction | Which sources disagree, and how can the disagreement be explained? |
| 13 | Conceptual fit | Do the source's categories match the claim's concepts, or is translation required? |
| 14 | Claim-specific evidentiary role | For *this* claim: strong / moderate / weak / none / undermining, with reasons |

**Return verdict per pair:** `SUPPORTS` · `UNDERMINES` · `SILENT` · `INDETERMINATE`, plus qualifiers. There is no source-level grade detached from a claim. That is the D1-LOCK-03 requirement that no universal source hierarchy be used.

### 7.5 Aggregation Belongs to PE

The protocol assesses **pairs**. PE aggregates pairs into step-level and mechanism-level judgments in A4, and then into claim classes in A6. The protocol never decides which mechanism wins. PE never overrides a pair-level assessment.

### 7.6 Boundary Stress Tests

| # | Scenario | Risk | Verdict |
|:---|:---|:---|:---|
| ST1 | PE finds an evidence gap mid-adjudication | PE starts searching | PE issues an **evidence request** (§8.2). `deep-research` retrieves. **PASS** if PE never emits retrieved content as its own finding. |
| ST2 | `deep-research` fact-checks "the minister met the ambassador on date D" | `deep-research` drifts into mechanism adjudication | `deep-research` applies the protocol to an `OCCURRENCE`/`TIMING` claim and stops. Asking *why* the meeting mattered routes to PE. **PASS** with this rule. |
| ST3 | The protocol output is rich enough to suggest a mechanism verdict | The protocol becomes an adjudicator | The return contract carries pair-level verdicts only. Cross-source and cross-rival aggregation is excluded from the protocol by design. **PASS.** |
| ST4 | `source_verification_agent` grades a diplomatic cable as "Level VII" under the biomedical pyramid | Pyramid misgrades archival evidence | When the protocol is active, the pyramid grade is not an input to PE adjudication; PE consumes the protocol assessment. How `deep-research` integrates this is **Q5** (D4). **PASS at the interface; implementation open.** |
| ST5 | A memoir is the only evidence for an actor's intention | Single retrospective source inflates the claim | Protocol flags retrospective reconstruction and candor incentives. M4 applies the single-source and retrospective-only downgrade triggers (§18.4). **PASS.** |
| ST6 | Official minutes are silent on an issue the mechanism says was decisive | Silence is read as absence | Negative evidence counts only when the trace would plausibly have been recorded *and* survived (protocol dimension 10 + A4 `trace_expectation_basis`). **PASS.** |
| ST7 | A secondary monograph asserts a causal account | The literature's verdict is imported as fact | Literature causal claims enter as rival hypotheses (I5). The monograph's *factual* reports may be assessed as evidence under the protocol. **PASS.** |
| ST8 | `academic-paper-reviewer` evaluates a paper's archival claims | Reviewer duplicates PE adjudication | The reviewer applies the protocol and may consume PE standards to *evaluate the author's reasoning*. It produces a referee assessment, not an author-side adjudication. **PASS.** |

### 7.7 Coexistence With Existing Assets

| Asset | Relationship to the Future Protocol |
|:---|:---|
| `deep-research/references/source_quality_hierarchy.md` | Stays in place for non-historical evidence. It is not edited or inverted. Its domain mismatch for archival claims (D0 §13.1 item 4) is handled by conditional activation, not by replacing it. |
| `academic-paper/references/domain_evidence_profiles.md` (`humanities_interpretive`) | Governs *admission* at literature screening. The protocol governs *claim-relative assessment* after admission. The protocol must not change admission or grade aggregation, preserving existing `deep-research` literature-screening grade aggregation behavior (referenced in `academic-paper/references/domain_evidence_profiles.md` lines 36–39) unless a separately authorized upstream change is required. |
| `shared/contracts/passport/timeline.schema.json` | Verifies dated facts. The protocol may assess the *sources* of dated facts. Interpretive periods never enter this schema. |
| `shared/protocols/prose_discipline_protocol.md` §8 | Line 136 ("Source provenance and factual grounding remain governed by `deep-research`") refers to retrieval-side provenance verification. Claim-relative assessment of historical sources is the new protocol's domain. D6 should reconcile this wording (Q13). |

---

## 8. DEEP-RESEARCH INTERFACE

### 8.1 Ownership Split

| `deep-research` OWNS | `political-economy-research` OWNS |
|:---|:---|
| Search and retrieval | Historical research design |
| Literature mapping and bibliographic synthesis | Mechanism construction |
| Source discovery | Process tracing |
| Source verification (existence, venue, citation accuracy) | Periodization |
| Dated-fact extraction (`timeline.yaml`) | Comparative-relational explanation |
| Generic method selection and generic design templates | Historical causal adjudication |
| Summarizing what the literature *claims* | Adjudicating *whether* those claims hold against evidence |

### 8.2 Evidence Request (PE → `deep-research`)

| Field | Content |
|:---|:---|
| `request_id` | Links back to A4 `evidence_gaps` |
| `discriminating_purpose` | Which rival mechanisms the evidence would discriminate between, and how |
| `expected_trace` | What the evidence would look like if mechanism M operated |
| `likely_locations` | Archive types, document classes, actors, periods (hints, not search execution) |
| `claim_type` | As §7.3, so retrieval can attach protocol-relevant metadata |

### 8.3 Retrieval Return (`deep-research` → PE)

Retrieved items with source descriptors, verification status, dated facts, and — when the protocol was applied to factual claims — pair-level assessment records. `deep-research` does **not** return mechanism verdicts.

### 8.4 Specialization Predicate for Research Design (resolves E1)

- **Default:** Non-historical comparative designs (e.g., comparing current programs across jurisdictions) stay with `deep-research` `research_architect_agent` using Pattern 2.
- **PE specialization applies** when the design needs any of: temporal scope as an analytical variable; sequence-sensitive inference; periodization; possible relational interdependence between cases; or historical evidence under the protocol.
- **Composition rule:** When `research_architect_agent` selects "comparative case study" and the specialization predicate holds, the historical design layer comes from PE's A1. Pattern 2 stays the generic baseline and is not duplicated in PE. Whether `research_architect_agent` gains an explicit delegation pointer is **Q6** (`deep-research` is an upstream-tracked core skill; any hook must be minimal).

### 8.5 Worked Composition: "Did US diplomatic pressure contribute to policy reversal in country X?"

```text
1. political-economy-research (M1/M3)
     - Restate the explanandum: reversal of policy P in country X, period T.
     - Specify rivals: M_pressure (external diplomatic pressure),
       M_coalition (domestic coalition shift), M_fiscal (fiscal/BOP crisis),
       M_ideational (technocratic learning), plus a timing-coincidence null.
     - For each, derive expected traces and timing (A3).
     - Issue evidence requests (A4 evidence_gaps → §8.2).

2. deep-research
     - Retrieve the diplomatic record, domestic cabinet/party records,
       fiscal data sources, press, memoirs; verify existence and dates.

3. historical_source_criticism_protocol (applied per source–claim pair)
     - e.g., embassy cable: strong for "the embassy reported pressure was
       applied," weaker for "pressure was received as decisive by the cabinet."
     - e.g., ex-minister memoir: retrospective; incentive to minimize or
       maximize external pressure depending on political position.

4. political-economy-research (M3/M4)
     - Fill A4: does the timing of pressure precede the decision process?
       Do internal records reference pressure? Do the coalition and fiscal
       rivals predict the same traces?
     - Assign claim class (A6): e.g., CONSTRAINT or CONTRIBUTION — or
       STRONG ATTRIBUTION only if rivals are discriminated and evidence
       is corroborated across independent sources.

5. If econometric (capital flows, reserves) or formal (BOP) inputs are
   used: applied-econometrics-pe / heterodox-macro-modeling supply
   them under §9–§10; PE integrates under §19.
```

### 8.6 Ambiguous-Prompt Disambiguation

| Prompt | Primary | Supporting | Rule |
|:---|:---|:---|:---|
| "What does the literature say caused the 1970s inflation in country X?" | `deep-research` | — | Literature summary, not adjudication |
| "Which of the literature's explanations of that inflation does the evidence support?" | PE | `deep-research`, protocol, possibly econometrics | Adjudication |
| "Find and verify the minutes of the meeting where the peg was abandoned." | `deep-research` | protocol | Retrieval + occurrence verification |
| "Use those minutes to assess whether the peg was abandoned because of reserve loss or political pressure." | PE | protocol, `deep-research` | Mechanism adjudication |
| "Design a study of how labor regimes changed across three countries since 1945." | PE | `deep-research` | Specialization predicate holds (temporal scope, sequence, possible relations) |
| "Design a study comparing current minimum-wage programs across three countries." | `deep-research` | `econ-write` (later writing) | Predicate fails: no historical/temporal/relational component |

---

## 9. APPLIED-ECONOMETRICS INTERFACE

### 9.1 Ownership Split

| `applied-econometrics-pe` OWNS | `political-economy-research` OWNS |
|:---|:---|
| Estimation, specification, stochastic admissibility | Historical meaning of boundaries and parameters as mechanism evidence |
| Unit-root, cointegration, VAR/VECM, Toda–Yamamoto, bootstrap | Periodization (historical side) |
| Break detection and break-test choice (known-date and unknown-date) | Classifying breaks within the Periodization Ledger |
| What a coefficient means statistically (sign, magnitude, uncertainty, identification) | Whether a statistical result corroborates or contradicts a mechanism's observable implication |

### 9.2 Bidirectional Flows

```text
PE → ECONOMETRICS
    - Hypothesized boundary dates (from A2) as ex-ante break hypotheses.
    - Mechanism-implied statistical predictions (from A3 implications_by_method),
      e.g., "if M operates, parameter β should change sign after boundary B."
    Econometrics decides whether and how these are testable.

ECONOMETRICS → PE
    - Break dates with uncertainty, test type, and whether dates were
      hypothesized ex ante or detected.
    - Estimates with admissibility status (passed/failed specification gates).
    - Non-findings, reported as non-findings.
```

### 9.3 Interface Rules

| Rule | Statement |
|:---|:---|
| **EI-1 Coefficient ≠ mechanism** | A coefficient can corroborate or contradict an observable implication of a mechanism. It cannot establish that the mechanism operated. Mechanism claims above `CONTRIBUTION` require process evidence (§18). |
| **EI-2 Break ≠ boundary** | A statistical break enters A2 as `STATISTICAL_BREAK`. It is promoted to `HISTORICAL_INSTITUTIONAL` only with independent historical evidence of institutional change within a declared alignment tolerance (§15.5). |
| **EI-3 Boundary ≠ break** | A historically justified boundary with no detected statistical break is kept as a historical boundary. The econometric non-finding is reported for that series. Neither result is suppressed or forced. |
| **EI-4 No narrative rescue** | PE must not supply post-hoc historical narratives to rescue failed statistical results. A "regime change explains non-cointegration" hypothesis must be stated with its own observable implications and assessed on evidence, consistent with the D2 purge of Rule 2.H.4 (D0 §5.2). |
| **EI-5 No statistical override** | PE never re-estimates, re-specifies, or reinterprets significance. Disagreements about specification route back to `applied-econometrics-pe`. |
| **EI-6 Revision provenance** | If periods are revised after seeing estimates, A2 records `set_before_estimation: false` and the reason. M4 applies the `DATA_INFORMED_PERIODIZATION` downgrade trigger to claims that depend on the revised boundary. |

### 9.4 Obligations Handed to D2

D2 must ensure `applied-econometrics-pe`:

1. Accepts PE boundary dates as ex-ante hypotheses without treating them as confirmed.
2. Reports break uncertainty and test provenance (hypothesized vs. detected) in a form A2 can consume.
3. Carries no historical interpretation rules of its own beyond statistical meaning. Rules like current §2.H.2 hard-coded regime signatures become illustrative only (D0 §5.1).
4. Routes historical-mechanism interpretation of parameters to PE rather than embedding it.

---

## 10. HETERODOX-MACRO INTERFACE

### 10.1 Center–Periphery Boundary (Three-Way)

| Concern | `political-economy-research` | `heterodox-macro-modeling` | `applied-econometrics-pe` |
|:---|:---|:---|:---|
| Dependency / center–periphery relations | Historical dependency relations; relational institutional mechanisms; mechanism-based interpretation | Formal representation of asymmetric structures | Empirical estimation of asymmetry indicators |
| External constraints | Transnational constraints as historically experienced and acted upon; state responses; coalition effects | BOP-constrained growth; open-economy closures | Testing constraint-implied relations (e.g., elasticities, thresholds) |
| Monetary relations | Historical monetary/political relations (e.g., reserve-currency politics, conditionality episodes) | Monetary hierarchy **when represented formally** | Estimating exchange-rate, reserve, or flow dynamics |
| Stocks and flows | Historical financing arrangements as institutions | Stock-flow structures, sectoral balances, SFC consistency | Measuring balances and flows; data admissibility |
| Dynamics | Sequence and timing of historical change | Dynamic stability, bifurcation, traverse | Parameter stability; break evidence |
| Mechanisms | Mechanism adjudication against historical evidence | Theoretical macro mechanisms derived formally | Stochastic evidence on mechanism implications |

**Composition rule:** A project may compose all three. Each contributes only its column. No component absorbs another's column, including when a single prompt mentions all three.

### 10.2 Interface Rules

| Rule | Statement |
|:---|:---|
| **MI-1 Model ≠ evidence** | A formal model is a source of mechanisms and observable implications (I8). Historical consistency with a model supports at most `INSTITUTIONAL_COMPATIBILITY` for the model's applicability. It is not evidence that the model's mechanism operated. |
| **MI-2 Closure justification** | Macro owns the closure's formal specification. Historical evidence that a period's institutions fit the closure's assumptions (e.g., wage-setting regime, capital mobility) is a PE input to macro, recorded with A2/A3 references. Macro decides how to use it. |
| **MI-3 Relational formalization** | When A5 relations are to be formalized (e.g., an asymmetric two-country structure), PE supplies the evidenced relation; macro owns the representation. |
| **MI-4 No historical doctrine in models** | Macro must not embed a historical interpretation as a modeling axiom without PE-traceable evidence. PE must not embed a model's conclusion as a historical finding. |

### 10.3 Obligations Handed to D3

D3 must ensure `heterodox-macro-modeling` exposes model-implied observable implications in a form A3 `implications_by_method` can reference. It must also keep SFC analysis inside the skill with no deterministic tool (D1-LOCK-04).

---

## 11. ACADEMIC-PAPER INTERFACE

| `academic-paper` OWNS | `political-economy-research` SUPPLIES |
|:---|:---|
| Manuscript lifecycle and state machine | A1 Design Brief → methods/design section content |
| Section architecture (incl. historical-background, methods, discussion sections) | A2 Periodization Ledger → period definitions and justification |
| Drafting, citation integration, formatting | A3/A4 → structured argument and evidence for mechanism sections |
| Revision cycles | A6 Calibration Table → admissible claim strength for every causal sentence |

**Rules:**

- **AP-1:** PE never drafts manuscript prose or sections. `academic-paper` turns artifacts into text.
- **AP-2:** `academic-paper` must not raise a causal claim above its A6 class during drafting or revision.
- **AP-3:** If drafting reveals a needed claim with no A6 row, `academic-paper` requests PE calibration rather than calibrating it itself.
- **AP-4:** Pipeline integration (e.g., whether `academic-pipeline` Stage 1/2 delegates to PE for PE topics) is orchestration and belongs to D6 (Q14).

---

## 12. REVIEWER INTERFACE

**Locked distinction:**

```text
political-economy-research   = AUTHOR-SIDE methodology
                               (designs, adjudicates, calibrates; produces artifacts)

academic-paper-reviewer      = SOLE OWNER of simulated external peer review
                               (referee reports, editorial decisions, scores,
                                revision roadmaps, persona critiques)
```

| Rule | Statement |
|:---|:---|
| **RV-1** | The reviewer may consume PE module standards (M1–M4) as domain criteria when evaluating comparative-historical work. This extends its existing Case Study criteria and Paradigm Bias guard (E6). |
| **RV-2** | PE never produces referee reports, accept/reject judgments, scored evaluations, decision letters, or persona-voiced critique. |
| **RV-3 Output-form disambiguation** | "Check whether my process tracing holds up" → PE: author-side diagnostic artifacts (A4 gaps, A6 downgrades), no verdict on publishability. "Review this paper as a referee" → reviewer. The deliverable form decides routing, not the subject matter. |
| **RV-4** | The reviewer, not PE, decides how profile calibration shapes critique (§14). |

---

## 13. ECON-WRITE INTERFACE

| `econ-write` OWNS | `political-economy-research` OWNS |
|:---|:---|
| Economics prose conventions, BLUF, triangular style, concrete magnitudes | Substantive historical-methodological reasoning |
| Sentence style, results-section rhetoric, identification rhetoric | Analytical structures (A1–A6) |
| Writing guidance for quantitative **Mechanisms** sections (`econ-write/SKILL.md` lines 432–437) | Within-case historical mechanism adjudication |
| Choosing verbs within the admissible ceiling (with prose protocol) | Setting the substantive causal-strength ceiling (A6) |

**Rules:**

- **EW-1:** PE contains no BLUF, compression, sentence-style, AI-pattern, or results-prose rules.
- **EW-2:** Writing tasks on PE material compose: PE artifacts → `econ-write` (economics) or `academic-paper` (generic) → prose protocol.
- **EW-3:** `econ-write` may not upgrade a claim's strength for rhetorical effect. If its identification-language rules and A6 disagree on a historical claim, A6 governs the substantive causal-strength ceiling. `econ-write` governs phrasing below it.

---

## 14. PROFILE INTERFACE

Profiles remain **calibration inputs** (`profiles/PROFILE_CONTRACT.md` lines 48–52). PE methodology is **never** routed through `profiles/scholars/*`, `profiles/advisors/*`, `profiles/committees/*`, or future `profiles/venues/*`.

| A profile MAY | A profile MAY NOT |
|:---|:---|
| Shift emphasis (which questions an advisor-facing summary foregrounds) | Supply missing canonical methodology |
| Add rival mechanisms or questions to *examine* | Remove a rival mechanism from consideration |
| Calibrate reviewer critique (in `academic-paper-reviewer`) | Lower or raise evidentiary thresholds or causal-strength conditions |
| Add perspective-specific prompts for author reflection | Presume a conclusion (e.g., that class conflict is the operative mechanism) |
| | Supply default periods, cases, or dates |

**Leakage fixture (E10):** `profiles/scholars/kevin-young.md` §3.2's US periods and §3.3's class-mediation prior are legitimate calibration. If they appeared in PE canonical instructions or as PE defaults, that would be a **profile-leakage defect**. D5 must test this (§22.3, EV-6).

### 14.1 Binding Invariant: Profiles Are Explicitly Opt-in

> **BINDING INVARIANT: PROFILES ARE NEVER DEFAULT INPUTS TO PE.**
> `political-economy-research` operates in canonical, theory-pluralist and non-doctrinal mode by default (no theoretical school is privileged by default; theories may actively structure concepts, mechanisms, scope conditions, and rival explanations, but the skill does not own doctrinal orthodoxy).
> Profiles are consumed ONLY when:
> 1. Explicitly requested by the user (e.g., "evaluate this chapter using the Brenner profile"); OR
> 2. Explicitly activated by an authorized workflow with user-declared calibration scope.
>
> A profile may NEVER:
> - supply default periodizations;
> - supply default mechanisms;
> - alter evidentiary thresholds or causal-strength conditions;
> - remove rival explanations;
> - predetermine conclusions.

---

## 15. PERIODIZATION CONTRACT

### 15.1 Capability Requirements

| ID | Requirement |
|:---|:---|
| P-1 | State a **period criterion** before dating boundaries: the dimension whose change defines a new period (e.g., institutional rule set, accumulation pattern, power configuration, external monetary regime, labor regime). |
| P-2 | Type every boundary using the typology in §15.2. |
| P-3 | Justify every `HISTORICAL_INSTITUTIONAL` boundary with protocol-assessed evidence of change in the stated criterion. |
| P-4 | Allow **transition intervals** where change is gradual. Point dates must not be forced on processual change. |
| P-5 | Record at least one **alternative periodization** when boundaries are contestable, and note which conclusions are sensitive to the choice. |
| P-6 | Record whether each boundary was set **before** econometric estimation, and log any revision with its reason (EI-6). |
| P-7 | Keep cyclical fluctuations from being promoted to period boundaries unless evidence shows regime-level change in the criterion. |
| P-8 | Permit convenience periods for description, labeled as such and **barred from causal-interpretive use**. |

### 15.2 Boundary Typology

| Type | Definition | Admissible Use |
|:---|:---|:---|
| `HISTORICAL_INSTITUTIONAL` | Change in the period criterion, documented by historical evidence | Causal and interpretive analysis |
| `STATISTICAL_BREAK` | Break in a series' statistical properties, detected or tested by econometrics | Statistical modeling. Interpretive use only after promotion (EI-2). |
| `CYCLICAL_FLUCTUATION` | Movement within a regime (expansion/contraction) with no criterion change | Describing within-period dynamics; never a period boundary |
| `CONVENIENCE` | Researcher-imposed partition (decades, data availability, presentation) | Description only; must be labeled |
| `CONTESTED` | Evidence conflicts on whether, or when, the criterion changed | Analysis with explicit sensitivity reporting |

### 15.3 Mixed Historical–Statistical Periodization (No Monopoly)

Neither component monopolizes mixed periodization:

- **Econometrics** is authoritative on *whether and when a statistical break exists* in a given series.
- **PE** is authoritative on *whether a boundary is historically justified* and on *its type in the ledger*.
- **Convergence** (break and historical boundary align within tolerance): recorded as mutually corroborating, each on its own terms.
- **Divergence:** handled by EI-2 and EI-3. Both findings are reported. Neither is overwritten.
- **Legitimate inspiration:** A detected break may prompt historical investigation. The resulting boundary is `HISTORICAL_INSTITUTIONAL` only if historical evidence independently supports it, and A2 records `prompted_by_statistical_break: true`.

### 15.4 Required Fields per Boundary (A2)

`boundary_id` · `date_or_interval` · `boundary_type` · `criterion_change_described` · `historical_evidence` (→ protocol records) · `statistical_evidence` (→ econometric results, if any) · `set_before_estimation` (true/false) · `prompted_by_statistical_break` (true/false) · `revision_log` · `alignment_tolerance_applied` · `confidence` · `alternatives`

### 15.5 Break Alignment and Evidentiary Reconciliation

A statistical break date and a historical period boundary need not be mathematically identical to corroborate each other. The periodization contract rejects pseudo-formal universal windows (such as hard-coded ±1 or ±2 year constants) that cannot be defended across disparate historical contexts.

Instead, break alignment and reconciliation are governed by four structural factors:

1. **Temporal Granularity:** Alignment must reflect series and historical frequency (decadal, annual, quarterly, or monthly).
2. **Dating Uncertainty:** Historical institutional change often spans an interval rather than a discrete point in time; point dates must not be forced onto processual transitions.
3. **Implementation Lag:** Institutional enactments, statutory reforms, and structural policy changes frequently take time to affect macroeconomic or behavioral series.
4. **Data Frequency & Aggregation:** Time-series breaks may lag or lead historical turning points due to reporting lags, annual averaging, or low-frequency measurements.

**Reconciliation Principles:**
- **Evidentiary justification required:** Aligning a statistical break with a historical boundary requires an explicit evidentiary justification grounded in data frequency, implementation lag, transition duration, or dating uncertainty.
- **Project-declared parameter:** Any numerical alignment window is a `PROJECT-DECLARED / METHOD-JUSTIFIED` parameter (supplied via the workspace overlay or Design Brief A1), not a hard-coded architectural constant.
- **Reporting:** When a break and a historical boundary diverge beyond justifiable lag or uncertainty, both are reported truthfully under §15.3 (EI-2/EI-3); neither is forced into artificial alignment.

### 15.6 Anti-Reverse-Engineering Invariant

> Periodization must not be reverse-engineered to rescue an econometric specification. Econometric break evidence may legitimately *inform* historical investigation, but a boundary's historical status rests on historical evidence. Boundaries revised after estimation carry a recorded downgrade (§18.4).

---

## 16. PROCESS-TRACING / MECHANISM CONTRACT

### 16.1 Capability Requirements (Vocabulary-Neutral)

| ID | Requirement |
|:---|:---|
| M-1 | Represent each candidate mechanism as **antecedent condition → actor/institutional mechanism → intermediate process → response → downstream consequence** (A3), at whatever granularity the evidence can support. |
| M-2 | Generate at least one **non-trivial rival** for every mechanism claim, including where relevant a timing-coincidence or common-cause alternative. |
| M-3 | Derive **observable implications** per step: what traces should exist, where, produced by whom, when. |
| M-4 | Use **sequence and timing** evidence: whether hypothesized causes precede effects, and whether intermediate steps occur in the predicted order. |
| M-5 | Treat **negative evidence** as informative only when the trace was expected to be produced, recorded, and preserved (linked to protocol dimension 10). |
| M-6 | Assess **diagnosticity**: how much more an evidence item is expected under one mechanism than under its rivals. Evidence that every rival predicts equally is non-discriminating, however abundant. |
| M-7 | Separate **within-case** evidence (process traces) from **cross-case** evidence (covariation), and state what each contributes. |
| M-8 | Recognize **equifinality** (different paths to the same outcome) and **conjunctural causation** (factors that matter only in combination). Do not force single-cause narratives. |
| M-9 | Scope mechanism claims to cases and periods (A2). Generalization beyond scope must be argued, not assumed. |
| M-10 | Keep mechanism claims **mechanism-specific**. Evidence that "something domestic changed" does not support a specific coalition mechanism. |
| M-11 | Admit **causal-process observations** (diagnostic pieces of within-case evidence about context, process, or mechanism) as a distinct evidence category from dataset observations, where methodologically appropriate. |

### 16.2 Actor and Institutional Mechanism Analysis (O5)

PE analyzes historically changing **institutions, states, firms, classes, class fractions, coalitions, labor organizations, political parties, bureaucracies, and international actors** through one general procedure. It hard-codes no theory:

1. **Formulate:** Express each candidate explanation as a mechanism with named actors or institutions, their interests or constraints as the theory specifies them, and their actions.
2. **Distinguish:** Identify where rival mechanisms make **different** predictions about traces, timing, actors, or outcomes. Where they make identical predictions, record that the evidence cannot discriminate.
3. **Operationalize:** Define what would count as evidence of each step (e.g., what documentary trace a coalition realignment would leave, versus a bureaucratic-capacity constraint, versus a monetary constraint).
4. **Assess:** Fill A4 and calibrate via A6.

**Illustrative rival set (non-canonical; any subset may be competing or complementary):** class conflict · elite coalition · bureaucratic capacity · institutional layering/conversion/drift · monetary or external constraint · accumulation-regime dynamics · electoral coalition · ideational/technocratic change. PE neither ranks these nor makes any one the default.

### 16.3 Non-Doctrinal Mechanism Evaluation Invariant

> PE helps formulate, distinguish, operationalize, and assess mechanisms. It operates in non-doctrinal mode: no theoretical school is privileged by default, and PE never predetermines which mechanism is correct. Theory actively structures which mechanisms and concepts are considered; evidence determines which are supported.

### 16.4 Candidate Methodological Implementations (Not Locked)

| Candidate | Capability Implemented | Already Covered Elsewhere? | Broadly Recognized? | Bias Risk | Needed Now? |
|:---|:---|:---|:---|:---|:---|
| Van Evera test typology (straw-in-the-wind, hoop, smoking-gun, doubly decisive) | M-6 diagnosticity, expressed as necessity/sufficiency of evidence | No | Yes. Widely taught in qualitative methods. | Low-moderate: can encourage false binary verdicts | **D4** — optional labeling layer over M-6 |
| Bayesian / likelihood-ratio process tracing (e.g., Bennett; Fairfield & Charman) | M-6 as explicit relative likelihood | No | Yes, growing | Moderate: false precision if numbers are forced | **D4** — qualitative likelihood logic recommended; numeric quantification optional |
| Causal-process observations vs. dataset observations (Brady & Collier) | M-7, M-11 | No | Yes | Low | **D4** — vocabulary candidate for M-11 |
| Mechanism-system tracing (e.g., Beach & Pedersen) | M-1 decomposition | No | Yes | Moderate: one school's variant taxonomy (theory-testing / building / explaining-outcome) | **D4** — consult, do not mandate |
| Historical-institutionalist sequence concepts (critical junctures, path dependence; layering, drift, conversion, displacement, exhaustion — Mahoney & Thelen; Streeck & Thelen) | M-1, M-4, O5 mechanism families | No | Yes within comparative politics/PE | **Moderate-high**: privileges institutionalist ontology over others | **D4** — include only as *one* family in a neutral list, never as the default frame |
| Set-theoretic / QCA logic | M-8 conjunctural causation, necessary/sufficient conditions | No | Yes, contested | Moderate | **D4 or defer** — mention as option; not required for core |

**Recommendation:** D4 should implement a **vocabulary-neutral core** (M-1 to M-11, with diagnosticity stated qualitatively) and may add optional mappings to recognized vocabularies. No framework becomes binding because D1 lists it.

---

## 17. COMPARATIVE-RELATIONAL CONTRACT

### 17.1 Definitions

```text
PARALLEL COMPARISON
    Cases treated as analytically independent units. Variation in
    outcomes is explained by variation in case-level conditions.
    Valid only if interdependence is absent, negligible, or controlled.

RELATIONAL COMPARISON
    Cases treated as mutually constituted through relations. Outcomes
    in one case are explained partly by the case's position in, and
    interaction through, relations with other cases or a shared system.

HYBRID
    Parallel comparison of case-level conditions with relational
    factors explicitly modeled as additional causes or controls.
```

### 17.2 Mode-Selection Procedure (Evidence Predicates for Relational Analysis)

> **CORE PRINCIPLE: RELATIONAL COMPARISON IS AN EVIDENCE-PREDICATE DESIGN PROBLEM, NOT A NUMERIC THRESHOLD.**

PE must not assume that comparative political economy is relational by default, nor that cases are independent observations. Mode selection is decided neither by theoretical assertion nor by arbitrary numerical counts of flows, but by structural evidence predicates:

1. **Constitutive or Causal Linkage Predicate:**
   - Are the cases connected through trade, finance, monetary hierarchy, international institutions, imperial/geopolitical ties, migration, production networks, technology transfer, or sovereign debt? AND
   - Would treating the cases as analytically independent omit a necessary constitutive or causal relation that shapes the observed outcomes?
2. **Common System Exposure Predicate (Galton's Problem):**
   - Are the cases exposed to a common external system or systemic shock, such that outcome similarities reflect systemic transmission rather than independent case-level causes?
3. **Asymmetric Interaction Predicate:**
   - Are relations structured hierarchically (e.g., center–periphery, currency hierarchy, structural adjustment conditionality) such that a case's structural position conditions its policy autonomy?

**Decision Rules:**
- **`PARALLEL` Mode:** Adopted when cases satisfy the independence predicate (or where systemic interdependencies are negligible or explicitly controlled). Requires a recorded independence justification.
- **`HYBRID` Mode:** Adopted when case-level causal processes operate alongside common systemic shocks or specific bilateral linkages that must be modeled as contextual conditions.
- **`RELATIONAL` Mode:** Adopted when the substantive outcome cannot be explained without modeling the relational ties and mutual constitution between cases (A5 required).

**Implementation Guidance for D4:** D4 must formulate qualitative and structural evidence predicates rather than mechanical counts, pseudo-numeric thresholds, or arbitrary flow volumes.

### 17.3 Relation Typology (A5 `relation_type`)

`TRADE` · `CAPITAL_FLOWS` · `MONETARY_HIERARCHY` · `INTERNATIONAL_INSTITUTIONS` · `IMPERIAL_OR_GEOPOLITICAL` · `MIGRATION` · `PRODUCTION_NETWORKS` · `TECHNOLOGY_TRANSFER` · `DEBT` · `CENTER_PERIPHERY_STRUCTURE` · `OTHER` (specified)

### 17.4 Evidence Requirements by Mode

| Mode | Must Demonstrate | Common Failure |
|:---|:---|:---|
| `PARALLEL` | Independence (or controlled interdependence); comparable measurement of conditions across cases; rival case-level explanations | Ignoring common shocks; treating linked cases as independent observations |
| `RELATIONAL` | **Evidence that the relation existed and operated** in the period (flows, institutional linkages, documented constraints or decisions referencing the other case); mechanism through which the relation affected outcomes | Asserting relations from theory alone (e.g., presuming center–periphery determination without evidencing the specific relation and its operation) |
| `HYBRID` | Both of the above for the respective components; explicit statement of how relational and case-level factors combine | Using relations as an unfalsifiable residual explanation |

### 17.5 Relational Evidence Invariant

> A relational explanation is a claim like any other. The relation must be evidenced, and its causal operation must be traced. Theoretical expectations of dependence, hierarchy, or imperial influence are hypotheses, not findings.

---

## 18. CAUSAL-CLAIM CALIBRATION

### 18.1 Principle

> Historical evidence, not rhetoric, determines the strength of a causal claim. PE calibrates each claim against evidence to establish its **substantive causal-strength ceiling**. Phrasing within that ceiling belongs to `econ-write` and `prose_discipline_protocol` (E4).

### 18.2 Claim Classes and Admissibility Conditions

> **STATUS: CANDIDATE IMPLEMENTATION CONTENT — D4 VALIDATION REQUIRED**
> The specific classification ladder C0–C8 below represents candidate implementation content subject to validation, refinement, simplification, or collapsing in Wave D4 based on operational need. It is not locked as binding repository architecture.
>
> **LOCKED ARCHITECTURAL INVARIANT:**
> ```text
> CAUSAL-STRENGTH CALIBRATION:
> BINDING
>
> DISCRETE CLASS SYSTEM:
> PROPOSED IMPLEMENTATION — D4 VALIDATION REQUIRED
> ```
> 1. Every substantive historical causal conclusion must undergo explicit causal-strength calibration against the available evidence, rival explanations, and downgrade conditions.
> 2. PE assigns the substantive causal-strength ceiling based on evidentiary warrant.
> 3. Phrasing within that ceiling is governed by shared prose discipline protocols and `econ-write`.
>
> D4 is explicitly authorized to validate, simplify, collapse, or refine the C0–C8 ladder or alternative representation based on operational need, provided this locked invariant is preserved.

Claim classes form two families. **Contribution-type classes** form an ordered ladder. **Logical-condition classes** are not points on that ladder; they have their own conditions.

**Contribution-type ladder (ascending candidate ladder):**

| Class | Claim Content | Minimum Admissibility Conditions |
|:---|:---|:---|
| `C0 CHRONOLOGICAL_ASSOCIATION` | A preceded or coincided with B | Reliable dating of A and B (protocol-assessed for `TIMING`). No causal content. |
| `C1 INSTITUTIONAL_COMPATIBILITY` | A's configuration was consistent with B | Documented features of A and B showing coherence. No direction or causal force asserted. |
| `C2 CONSTRAINT` | A narrowed the options available to actors producing B | Evidence that options were considered and foreclosed, or that actors perceived and referenced the limit; the timing fits. Does not claim A determined B. |
| `C3 FACILITATION` | A lowered the cost of, or enabled, B | Evidence that actors producing B used, invoked, or relied on A; the timing fits. |
| `C4 CONTRIBUTION` | A was one cause of B | A3 specified; step-level evidence for at least the critical link(s); at least one rival assessed and found not to fully account for B. |
| `C5 MECHANISM_SUPPORTED_CONTRIBUTION` | A contributed to B *through mechanism M* | C4 + protocol-assessed evidence for **each critical step** of M; rivals assessed with **discriminating** evidence (M-6); no unresolved contradiction from other methods on M's implications. |
| `C8 STRONG_CAUSAL_ATTRIBUTION` | A was the principal cause of B (in scope) | C5 + principal rivals **substantially eliminated** by discriminating evidence; corroboration across **independent** sources; claim survives source-reliability sensitivity (removing the most interested source); method status not `DIVERGENT`. |

**Logical-condition classes (scope-bound):**

| Class | Claim Content | Minimum Admissibility Conditions |
|:---|:---|:---|
| `C6 NECESSARY_CONDITION` | Without A, B would not have occurred (in scope) | Explicit counterfactual argument; evidence that the pathway to B ran through A, with no observed alternative path in scope; for multi-case claims, no in-scope case with B but without A; scope stated. |
| `C7 SUFFICIENT_CONDITION` | Given A (and stated background conditions), B follows (in scope) | For multi-case claims, all in-scope cases with A (and background conditions) show B; within-case, evidence that B followed independently of rival factors. **Rarely admissible from a single case**; single-case sufficiency claims default to `C5` at most. |

*(Class codes C6/C7 are kept for traceability with the prompt order; they are not ranks above C5.)*

### 18.3 Calibration Invariants

1. **No rhetorical upgrade:** Abundance of narrative detail is not diagnosticity. Many non-discriminating traces do not raise a class.
2. **Weakest critical link:** A mechanism-level claim is capped by the weakest evidenced critical step.
3. **Scope binding:** Every class is claimed for stated cases and periods only.
4. **Upgrade path required:** A6 records what evidence would justify the next class. This keeps calibration falsifiable and useful for further research.

### 18.4 Downgrade Triggers (Applied by M4)

| Trigger | Effect |
|:---|:---|
| `SINGLE_SOURCE_DEPENDENCE` — critical step rests on one source | Cap at `C4` |
| `INTERESTED_SOURCE_ONLY` — supporting sources share an incentive favoring the claim | Cap at `C4`; at most `C3` if the protocol flags strong concealment/persuasion incentives |
| `RETROSPECTIVE_ONLY` — critical step evidenced only by retrospective accounts | Cap at `C4` |
| `UNRESOLVED_CONTRADICTION` — protocol-assessed contradicting evidence is unexplained | Cap at `C3` |
| `METHOD_DIVERGENCE` — econometric or formal implications contradict the mechanism (§19.4) | Cap at `C4`; record divergence |
| `DATA_INFORMED_PERIODIZATION` — claim depends on a boundary revised after estimation | Cap at `C4`; flag |
| `IGNORED_INTERDEPENDENCE` — cases treated as independent despite independence-diagnostic evidence | Cap cross-case claims at `C1` until the mode is corrected |
| `NON_DISCRIMINATING_EVIDENCE` — all rivals predict the observed traces | Cap at `C2` for the contested link |

Specific caps are **D4-tunable defaults** (Q7). The trigger *set* is the D1 capability requirement.

### 18.5 Relationship to the Prose Protocol

- PE outputs `claim_class` and conditions. It does **not** output verb lists.
- The prose protocol's "Historical / Archival / Qualitative Evidence" row (line 127) becomes the default phrasing band. A6 tells writers where in that band, or above or below it, a given claim sits.
- Where a class→verb crosswalk should live (prose protocol vs. PE reference vs. `econ-write`) is **Q7**. D1 recommends it **not** live in PE, to avoid duplicating wording rules.

---

## 19. MIXED-METHODS COMPOSITION CONTRACT

### 19.1 Role Order

```text
THEORY
    proposes mechanisms and hypotheses
    (formal models via heterodox-macro-modeling; verbal theory via PE/O5)
        ↓
EVIDENCE
    evaluates them, each through its appropriate method:
      historical evidence → PE + shared protocol
      statistical evidence → applied-econometrics-pe
      (formal models generate implications; they are not evidence)
        ↓
INTERPRETATION
    follows the combined evidentiary record
```

### 19.2 Inferential-Task Jurisdiction Rule

Integration authority is governed by inferential-task jurisdiction rather than substantive-object primacy:

> **PRIMARY ANALYTIC OWNER = the component owning the requested inferential operation, not merely the substantive object being studied.**

Merely studying a historical object or episode does not grant `political-economy-research` integration authority over econometric estimation or formal macroeconomic modeling. Each component retains sole jurisdiction over its own evidentiary verdict.

| Inferential Question / Operation | Primary Analytic Owner | Supporting / Input Components | PE Role |
|:---|:---|:---|:---|
| Historical mechanism and causal process ("What historical mechanism explains this policy reversal?") | `political-economy-research` | `applied-econometrics-pe` (statistical implications); `heterodox-macro-modeling` (formal implications); `deep-research` | Primary owner of historical mechanism synthesis; cannot override source verdicts |
| Statistical relationship, parameter stability, or break detection ("Did these variables cointegrate or did β shift?") | `applied-econometrics-pe` | `political-economy-research` (historical boundary hypotheses, A2) | Supplies boundary hypotheses; cannot alter econometric verdict |
| Formal model behavior, closure consistency, or dynamic stability ("Is this growth model dynamically stable?") | `heterodox-macro-modeling` | `political-economy-research` (institutional closure-fit evidence) | Supplies historical fit evidence; cannot alter model derivation |
| Presentation and manuscript synthesis ("How should the manuscript present the combined result?") | `academic-paper` (+ `econ-write` if economics) | `political-economy-research`, `applied-econometrics-pe`, `heterodox-macro-modeling` | Supplies A6 substantive causal-strength ceiling |

For genuinely mixed-method questions, composition applies. Each component retains jurisdiction over its own evidentiary verdict.

A primary domain component may synthesize already-adjudicated inputs from other components for its own historical mechanism questions, but it cannot alter source verdicts or claim integration authority across the whole workflow merely because the substantive object is historical.

### 19.3 Non-Override Rules

#### Binding Lock: NO CROSS-METHOD OVERRIDE

```text
PE cannot revise an econometric verdict.
Econometrics cannot establish a historical mechanism.
Formal models cannot constitute historical evidence.
Historical evidence cannot establish stochastic admissibility.
```

| Rule | Statement |
|:---|:---|
| **NO-1** | No qualitative mechanism automatically overrides contradictory econometric results. |
| **NO-2** | No econometric coefficient automatically establishes a historical mechanism (EI-1). |
| **NO-3** | No formal model is treated as historical evidence (MI-1). |
| **NO-4** | No method's non-finding is converted into another method's positive finding (generalizes the D2 Rule 2.H.4 purge). |

### 19.4 Method-Status States and Handling

| State | Definition | Handling |
|:---|:---|:---|
| `CONVERGENT` | Methods' implications agree | Record mutual corroboration; each method's evidence counts on its own terms |
| `COMPLEMENTARY` | Methods address different aspects (e.g., econometrics on magnitude, history on process) | Combine within scope; no cross-substitution |
| `DIVERGENT` | Methods' implications conflict | **Report the conflict.** Diagnose candidate sources: measurement, scope mismatch, period misalignment, aggregation level, specification, source bias. Apply `METHOD_DIVERGENCE`. Never resolve by fiat. |
| `ABSENT` | A method was not applied | Record; no inference from absence of a method |

### 19.5 Integration Record

Integration results are recorded in A6 (`method_status`, `downgrade_triggers_applied`). No separate mixed-methods artifact is created (§4.1).

---

## 20. PROJECT-SPECIFIC LEAKAGE GUARD

### 20.1 Reusable-Domain Condition

The skill must work for research outside any single dissertation. Canonical instructions (`SKILL.md` and M1–M4 bodies) must **not** hard-code:

- specific countries or episodes (e.g., Chile, Unidad Popular, the nitrate crisis);
- specific regime labels as default periodization (e.g., Fordism);
- specific authors as doctrinal authorities (e.g., Shaikh);
- dissertation waves, chapters, or fixed historical dates;
- one center–periphery interpretation or one class configuration;
- one empirical model or estimate (e.g., hard-coded parameter signatures);
- any advisor's or committee member's preferences.

### 20.2 Where Project-Specific Content Goes

| Content | Home |
|:---|:---|
| Case lists, declared periods, alignment tolerance, dummy definitions | Workspace Project Overlay (17 §9) |
| Advisor/committee emphases | `profiles/*` (calibration only, §14) |
| Worked examples | Labeled `ILLUSTRATION — NON-CANONICAL` blocks, or eval fixtures |

### 20.3 Tests

| Test | Method |
|:---|:---|
| **Substitution test** (design-time and D5 model-behavior) | Replace every case name, date, and theory label in a task with another region/era/theory. Canonical instructions must apply unchanged. |
| **Illustration rotation** | Illustrations in canonical files must span **≥3 distinct regions or eras**, with no single project dominating (Q11). |
| **Static denylist scan** (D6 deterministic check) | Scan PE canonical files, outside labeled illustration blocks, for a configurable denylist (initial seed: `Chile`, `Unidad Popular`, `Allende`, `salitre`/`nitrate`, `Fordis*`, `Shaikh`, scholar profile names, `UMass`, four-digit years). Hits fail the check. The denylist lives in the test, not in the skill. |
| **Profile non-import check** | No PE canonical file references `profiles/` paths or reproduces profile calibration principles (E10). |

### 20.4 Audit of This Design

D1 itself names project-associated terms only in this guard, in E10, and in explicitly labeled illustrations. No contract, rule, artifact field, or claim-class condition in §1–§19 depends on a specific case, period, author, or advisor. **Result: PASS.**

---

## 21. CANDIDATE IMPLEMENTATION STRUCTURE

> **STATUS: PROPOSED — NOT AUTHORIZED.** Nothing in this section was created in D1. Creation requires D4 authorization.

### 21.1 Proposed Files

```text
political-economy-research/                      ← runtime path at repository root (created in D4),
│                                                  consistent with routing Rule 8
├── SKILL.md                                     ← M0 capability charter & composition router
└── references/
    ├── research_design_and_comparison.md        ← M1 (O1 + O4)  → A1, A5
    ├── periodization.md                         ← M2 (O2)       → A2
    ├── mechanism_reasoning.md                   ← M3 (O3 + O5)  → A3, A4
    └── causal_claim_calibration.md              ← M4 (O6 + O7)  → A6

shared/protocols/
└── historical_source_criticism_protocol.md      ← D4; existing live substrate directory (no move)
```

- `skills/domain/political-economy-research/` — **FUTURE WAVE-F TARGET PATH — NOT A WAVE-D MOVE.**
- No `tools/`, `scripts/`, `agents/`, or `templates/` subdirectory is proposed. PE's operations are reasoning, not deterministic computation. Agents and templates need demonstrated need in D4.

### 21.2 Implementation Guidance for D4

| Item | Guidance |
|:---|:---|
| `SKILL.md` frontmatter description | State the triggers (comparative-historical design, periodization, process tracing, rival-mechanism adjudication, relational comparison, historical causal calibration). Also state the **non-triggers** (search, statistics, formal models, drafting, prose, review), so routing can disambiguate. |
| Proportionality | Lightweight questions should get lightweight outputs. Artifacts are required only where §6.2 says so. Q8 settles minimum sets. |
| Illustrations | Labeled `ILLUSTRATION — NON-CANONICAL`, rotated across ≥3 regions/eras (§20.3). |
| Cross-references | Reference adjacent components by contract name. Never copy their rules (no BLUF, no econometric gates, no closure taxonomy, no source-criticism dimensions beyond pointing to the protocol). |
| Theory content | Theories appear only as examples of mechanism *inputs* (§16.2). There are no doctrinal exposition sections. |

### 21.3 Candidate Methodological Implementation Register (Design, Periodization, Comparison)

Process-tracing candidates are in §16.4. None of these is binding.

| Candidate | Capability Implemented | Covered Elsewhere? | Broadly Recognized? | Bias Risk | Needed Now? |
|:---|:---|:---|:---|:---|:---|
| Mill's methods of agreement/difference | Parallel-mode logic (O4) | Partially (generic Pattern 2, E1) | Yes | Low, but limits are well known (independence, small N) | D4 — as parallel-mode baseline with stated limits |
| Galton's problem (non-independence of cases) | Independence diagnostics (§17.2) | No | Yes | Low | D4 — core concept for mode selection |
| Skocpol & Somers' comparative logics (parallel demonstration, contrast of contexts, macro-causal analysis) | Design typology (O1) | No | Yes | Low-moderate | D4 — optional design vocabulary |
| Tilly's comparison types (individualizing, universalizing, variation-finding, encompassing) | Mode typology incl. encompassing/relational (O4) | No | Yes | Low-moderate | D4 — candidate vocabulary for relational mode |
| Incorporated comparison (McMichael) / relational comparison (Hart) | Relational mode (O4) | No | Recognized in historical sociology and PE | Moderate: world-systems / critical-geography lineage | D4 — consult; express requirements neutrally (§17) |
| Temporal-process concepts (e.g., Pierson; Sewell's eventful temporality) | Sequence, timing, critical-juncture reasoning (O1, O2, M-4) | No | Yes | Moderate: institutionalist vs. eventful ontologies differ | D4 — as alternative lenses, not defaults |
| Regulation-school / SSA periodizations | Theory-specific period criteria (O2 inputs) | No | Recognized within heterodox PE | **High**: school-specific; would hard-code one period criterion | **Not canonical.** Admissible only as user-supplied theory input (I6) or labeled illustration |

---

## 22. EVAL / ROUTING DESIGN (TARGET FOR D5/D6)

> Design only. No cases are added to `evals/gold/routing/cases.yaml` in D1. D5 assigns case IDs and must reconcile them with the D0 §12.1 proposals (ROUTE-018 to ROUTE-023). Fixtures must avoid any single project's cases (§20).

### 22.1 Adversarial Routing Cases

| # | Category | Prompt | Primary Owner | Supporting | Forbidden Owners | Expected Reasoning Boundary |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | Archival evidence search | "Locate archival records of the 1970s negotiations between country X's central bank and the IMF." | `deep-research` | historical-source protocol | PE (as primary), `academic-paper`, reviewer | Retrieval + existence/date verification only. No mechanism verdict. |
| 2 | Historical source evaluation | "An embassy cable says the cabinet was divided over devaluation. How much weight can it bear for the claim that the finance minister opposed it?" | `deep-research` (Rule R9 source-level claim assessment) applying the protocol | — | PE (unless mechanism adjudication is requested), reviewer, `econ-write` | Claim-relative assessment of one (source, claim) pair. No universal source grade. No mechanism aggregation. |
| 3 | Process tracing | "Does the evidence support that a business-coalition realignment, rather than a reserve crisis, drove the privatization program in country X?" | PE | protocol, `deep-research` | `applied-econometrics-pe` (primary), reviewer, `econ-write` | A3 per rival; A4 with diagnosticity; A6 class. Evidence requests for gaps; no searching. |
| 4 | Periodization | "Construct and justify periods for the labor regime in country X from 1940 to 2000." | PE | `deep-research`, protocol, `applied-econometrics-pe` (optional break evidence) | econometrics (primary), profiles | A2 with period criterion, boundary typing, alternatives, pre-/post-estimation flags. |
| 5 | Comparative case design | "Design a study of why industrial policy persisted in country A but collapsed in country B after the debt crisis." | PE | `deep-research` (generic baseline) | `academic-paper`, reviewer | A1 with independence diagnostics. Mode chosen from evidence, not assumed. |
| 6 | Relational historical explanation | "Explain how creditor-country interest-rate policy constrained industrial policy in debtor countries in the early 1980s." | PE | `heterodox-macro-modeling` (if formalized), `applied-econometrics-pe` (if estimated), `deep-research` | `academic-paper`, `econ-write` | `RELATIONAL` mode with an **evidenced** relation (A5). Constraint-type claim calibrated (C2 to C5). |
| 7 | Formal macro model | "Derive the stability conditions of this open-economy BOP-constrained growth model." | `heterodox-macro-modeling` | — | PE, `applied-econometrics-pe`, reviewer | Formal derivation only. No historical claims. |
| 8 | Econometric break test | "Test for structural breaks in the profit-share series and report break dates with confidence intervals." | `applied-econometrics-pe` | — | PE (primary), `heterodox-macro-modeling` | Statistical breaks only. No historical labeling of breaks (EI-2). |
| 9a | Coefficient interpretation (statistical) | "What does an elasticity of 0.4 mean here, and is it statistically distinguishable from zero?" | `applied-econometrics-pe` | — | PE | Statistical meaning only. |
| 9b | Coefficient interpretation (mechanism) | "Does this positive coefficient of capital inflows on the wage share support the claim that external financing loosened distributive conflict?" | PE | `applied-econometrics-pe` (mandatory, for statistical entitlement) | PE re-estimating; reviewer | EI-1: the coefficient corroborates an implication at most. Cap at `C4` without process evidence. |
| 10 | Manuscript drafting | "Draft the historical-context section of my paper from these period and mechanism notes." | `academic-paper` (+ `econ-write` if economics) | PE artifacts (consumed) | PE (as drafter) | AP-1/AP-2: prose built from A2/A3/A6. No claim upgrades. |
| 11 | Peer review | "Referee this comparative-historical article for a journal." | `academic-paper-reviewer` | PE standards (consumed); profiles if requested | PE (primary), `academic-paper` | Referee report from the reviewer. PE produces no verdict. |
| 12 | Mixed-method explanation | "Combine the archival record, our VAR results, and the growth model to explain why investment collapsed after the mid-1970s boundary." | PE (historical mechanism synthesis; no cross-method override, §19.2) | `applied-econometrics-pe`, `heterodox-macro-modeling`, protocol, `deep-research` | `academic-pipeline` (as substantive owner), PE revising econometric verdicts | §19: inferential jurisdiction, NO-1 to NO-4, method status, synthesis without override. |
| 13 | Author-side check vs. review | "Check whether my chapter's process tracing holds up before I send it to my advisor." | PE | protocol | reviewer (no referee report), profiles | RV-3: diagnostic artifacts (A4 gaps, A6 downgrades). No publishability verdict. |
| 14 | Profile-supplied periods | "Periodize my study of country X using the periods in my committee member's profile." | PE | — | profiles (as methodology source) | User-requested periods enter as **project parameters / hypotheses** and must still be typed and justified (§14, §15). |
| 15 | Theory exposition | "Explain the main tenets of structural dependency theory." | `deep-research` if literature synthesis is requested; otherwise general assistance | — | PE | D1-LOCK-02: theory exposition is not PE's capability. |
| 16 | Statistical-relation explanandum with history | "Did the long-run wage–output relation shift after the exchange-rate regime change?" | `applied-econometrics-pe` (statistical inferential task, §19.2) | PE (boundary hypothesis from A2) | PE (as integration owner) | Econometrics owns the test and its interpretation. PE supplies the boundary hypothesis only. |

### 22.2 Disambiguation Pairs (Must Route Differently)

| Pair | Distinguishing Feature |
|:---|:---|
| 2 vs. 3 | Single source–claim assessment vs. mechanism adjudication |
| 9a vs. 9b | Statistical meaning vs. mechanism corroboration |
| 12 vs. 16 | Historical mechanism inference vs. statistical relation inference (§19.2) |
| 13 vs. 11 | Author-side diagnostic vs. referee report |
| 5 vs. "compare current minimum-wage programs across three countries" | Specialization predicate (§8.4) holds vs. fails |

### 22.3 Model-Behavior Gold Evals (D5; proposed location `evals/gold/political_economy/`)

| ID | Target Behavior | Setup | Pass Criterion |
|:---|:---|:---|:---|
| EV-1 | No reverse-engineered periodization | Estimates fit best with a break at year Y; no historical evidence of criterion change | Boundary typed `STATISTICAL_BREAK`; not presented as a historical period |
| EV-2 | Relational claims need evidence | Prompt presumes center–periphery determination; no relation evidence supplied | Model flags the missing relation evidence, issues evidence requests, and does not assert `RELATIONAL` mode as established |
| EV-3 | No coefficient→mechanism overreach | Significant coefficient consistent with mechanism M; no process evidence | Claim capped at `C4` or below; EI-1 cited |
| EV-4 | Non-discriminating evidence does not upgrade | Abundant narrative consistent with all rivals | `NON_DISCRIMINATING_EVIDENCE` applied; no class increase |
| EV-5 | Archival silence handled correctly | Minutes silent on a supposedly decisive issue | Negative evidence used only with a stated trace-expectation basis |
| EV-6 | Profile non-leakage | Workspace with active scholar profile containing fixed periods and a class-mediation prior | Periods and priors not imported as defaults; rivals not removed |
| EV-7 | Substitution invariance | Same task across three different regions/eras | Structurally equivalent artifacts; no carry-over of case-specific content |
| EV-8 | Divergence handling | Archival evidence supports M; econometric implication contradicts M | `DIVERGENT` reported, candidate sources diagnosed, `METHOD_DIVERGENCE` applied; no resolution by fiat |
| EV-9 | Non-doctrinal theory evaluation | User strongly prefers mechanism A; evidence favors mechanism B | Conclusion follows evidence; preference recorded as hypothesis only |
| EV-10 | No fabricated evidence / no search | Adjudication requested with key evidence missing | Evidence requests issued; no invented sources or contents |
| EV-11 | Claim-relative source criticism (protocol, D4/D5) | Contemporaneous cable vs. retrospective memoir (as in D0 §12.3) | Each source assessed per claim; no categorical "primary > secondary" grading |

### 22.4 Deterministic Static Checks (D6; e.g., in a future `scripts/test_wave_d_reconciliation.py`)

| ID | Check |
|:---|:---|
| SC-1 | Registry: `political_economy_research_methodology` has owner `political-economy-research`, its description **excludes** source criticism (G1), and consumers are reconciled. |
| SC-2 | Routing: a PE rule exists and resolves to the root runtime path, never to `skills/domain/...`. |
| SC-3 | Denylist scan of PE canonical files outside illustration blocks (§20.3). |
| SC-4 | No `profiles/` path references in PE canonical files. |
| SC-5 | No prose-rule duplication in PE files (e.g., BLUF directives, banned-transition lists). |
| SC-6 | `historical_source_criticism_protocol.md` exists under `shared/protocols/`, and no source-criticism standard file exists inside `political-economy-research/`. |
| SC-7 | `tools/macro/sfc_consistency_check.py` is absent (D1-LOCK-04) unless a later authorization exists. |
| SC-8 | No Wave-D creation of `skills/domain/`, `tools/econometrics/`, or `orchestrator/` paths (D1-LOCK-05). |

---

## 23. OPEN IMPLEMENTATION QUESTIONS

| ID | Question | Resolving Wave | D1 Recommendation |
|:---|:---|:---|:---|
| Q1 | Which process-tracing vocabulary, if any, labels the M-6 diagnosticity core? | D4 | Vocabulary-neutral core; optional Van Evera / likelihood mappings; no forced numeric Bayesianism |
| Q2 | How is the protocol's (source, claim) assessment record serialized, and does it need a passport schema? | D4 (format), D6 (schema) | Start as a documented Markdown/YAML record; add a schema only if the pipeline must verify it |
| Q3 | How is protocol activation detected ("materially involved")? | D4 | Claim holder declares `claim_type` and source type; activation follows §7.2. No silent auto-activation inside unrelated domains. |
| Q4 | Does the protocol cover the construction provenance of historically reconstructed statistics? | D4 (with D2 consultation) | Yes for construction provenance; stochastic admissibility stays with econometrics |
| Q5 | How does `deep-research` (`source_verification_agent`) consume the protocol without editing the biomedical pyramid, and how does this relate to `humanities_interpretive` and upstream grade aggregation? | D4 | Minimal conditional hook; no pyramid inversion; preserve existing `deep-research` literature-screening grade aggregation behavior (referenced in `academic-paper/references/domain_evidence_profiles.md` lines 36–39) unless a separately authorized upstream change is required |
| Q6 | Should `research_architect_agent` get a delegation pointer to PE under the specialization predicate? | D4 (design), D6 (governance) | Minimal pointer only, mindful that `deep-research` is upstream-tracked |
| Q7 | Default caps for downgrade triggers; where a class→verb crosswalk lives | D4 (caps), D6 (crosswalk location) | Caps as tunable defaults in M4; crosswalk outside PE |
| Q8 | Minimum artifact sets for lightweight tasks | D4 | Proportional: A6 always for exported causal claims; others only per §6.2 conditions |
| Q9 | Default alignment tolerance vs. project-declared tolerance | D4 | Project-declared via overlay/Design Brief grounded in data granularity, lag, or uncertainty; no universal numerical constant |
| Q10 | Evidence predicates for adopting `RELATIONAL` mode | D4 | Qualitative/structural evidence predicates demonstrating that relations actively constituted or constrained outcomes; no pseudo-numeric flow thresholds |
| Q11 | Illustration rotation and fixture sourcing | D4/D5 | ≥3 regions/eras; fixtures drawn from varied, well-documented episodes |
| Q12 | Whether to include a neutral mechanism-family list, and how to stop canon creep | D4 | Short, explicitly illustrative list (§16.2); no ranking; no default |
| Q13 | Reconciling prose protocol §8 line 136 wording with the shared historical-source protocol | D6 | Clarify "provenance" as retrieval-side verification |
| Q14 | Registry consumers, new routing rule, `academic-pipeline` delegation for PE topics | D6 | Add PE rule; add reviewer and pipeline as consumers; pipeline delegates without owning |
| Q15 | Coordinating D2's Rule 2.H.4 replacement with PE (historical regime hypotheses) | D2/D4 | D2 text routes historical regime hypotheses to PE under EI-4 and NO-4 |

---

## 24. D1 FINAL LOCK

> **STATUS: HUMAN-RATIFIED BINDING ARCHITECTURE — WAVE D1 CLOSED.**

### 24.1 OWNERSHIP
`political-economy-research` is the canonical owner of `political_economy_research_methodology`, encompassing:
- Comparative-historical research design (case and unit construction, temporal scope, comparison mode selection);
- Historical periodization (criteria, boundary typing, justification, transition intervals, anti-reverse-engineering discipline);
- Process tracing and rival-mechanism adjudication (step decomposition, observable implications, negative evidence, diagnosticity);
- Comparative-relational analysis (independence diagnostics, relation mapping across trade, finance, monetary hierarchy, geopolitics, and debt);
- Historical causal claim calibration (substantive causal-strength ceiling, downgrade triggers, upgrade pathways).

### 24.2 CORE REASONING
The skill's core analytical reasoning consists of:
- **Non-dogmatic theory operationalization:** Translating theories into competing, testable mechanisms without privileging any theoretical school or asserting theory as repository doctrine (§3.2);
- **Within-case and cross-case evidence synthesis:** Combining causal-process observations with comparative structures;
- **Historical inferential synthesis:** Synthesizing already-adjudicated cross-method inputs into coherent historical mechanism explanations without altering source verdicts or claiming jurisdiction over non-historical operations (§19.2).

### 24.3 INPUTS / CONSUMPTION
`political-economy-research` consumes:
- Evidence retrieval, bibliographic verification, and dated timeline facts from `deep-research`;
- Claim-relative source assessment standards from `shared/protocols/historical_source_criticism_protocol.md` (applied to historical claims);
- Statistical estimates, structural break dates, and stochastic admissibility verdicts from `applied-econometrics-pe`;
- Formal equations, closure behaviors, and model-derived implications from `heterodox-macro-modeling`;
- Profile calibration from `profiles/*` on an **explicit opt-in basis only** (shifting inquiry emphasis or adding rival questions without altering standards, §14.1);
- Project-specific parameters (case lists, declared periods, alignment tolerances) from the Workspace Project Overlay.

### 24.4 NON-OWNERSHIP
`political-economy-research` explicitly does **not** own:
- Search, retrieval, bibliographic mapping, or venue verification (`deep-research`);
- Historical source-criticism standard definition (`shared/protocols/historical_source_criticism_protocol.md`);
- Econometric estimation, time-series testing, break detection, or stochastic admissibility (`applied-econometrics-pe`);
- Formal mathematical modeling, SFC balance sheets, or dynamic stability proofs (`heterodox-macro-modeling`);
- Manuscript drafting, section structure, citation formatting, or document lifecycle (`academic-paper`);
- Economics or generic prose style, BLUF, sentence rhythm, or verb selection (`econ-write`, `prose_discipline_protocol`);
- Referee reports, peer-review simulation, editorial decisions, or evaluative scoring (`academic-paper-reviewer`);
- Workflow orchestration, pipeline control, or Material Passport state management (`academic-pipeline`);
- Scholar, advisor, or committee calibration doctrine (`profiles/*`);
- Encyclopedic theoretical exposition or maintenance of doctrinal orthodoxies.

### 24.5 COMPOSITION
- **Inferential-Task Jurisdiction:** Integration authority belongs to the component owning the requested inferential operation, not merely the substantive object studied (§19.2). Merely studying a historical object does not grant PE integration monopoly over econometrics or formal models.
- **Binding Lock — NO CROSS-METHOD OVERRIDE:**
  - PE cannot revise an econometric verdict;
  - Econometrics cannot establish a historical mechanism;
  - Formal models cannot constitute historical evidence;
  - Historical evidence cannot establish stochastic admissibility.
- **Multi-Method Reconciliation Without Hierarchy:** Where historical and quantitative findings diverge, divergence is reported with candidate sources diagnosed; conflicts are never resolved by fiat.
- **Downstream Feeding:** PE exports substantive causal-strength ceilings (via proposed A6 calibration) to downstream writing (`academic-paper`, `econ-write`) and review (`academic-paper-reviewer`) components, which govern phrasing and evaluation within that ceiling.

### 24.6 IMPLEMENTATION STATUS
- **Design Lock, Not Code:** Wave D1 establishes a binding capability and ownership contract. It does not implement runtime code.
- **Proposed Architecture:** The candidate 4-reference module structure (M0–M4), the candidate C0–C8 causal-claim ladder, and the candidate artifact formats (A1–A6) represent proposed implementation architecture. Causal-strength calibration is locked as binding, while discrete class representations (such as C0–C8) and artifact formats remain proposed implementation subject to D4 validation.
- **Deferred Authorization:** Creation of runtime skill directories (`political-economy-research/`), shared protocol authoring, routing rule additions, registry updates, and eval fixtures are deferred to Waves D4, D5, and D6.
