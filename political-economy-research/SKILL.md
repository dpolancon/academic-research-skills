---
name: political-economy-research
description: Canonical author-side domain capability for comparative-historical political-economy research design, historical periodization, mechanism and process-tracing reasoning, rival-mechanism adjudication, comparative-relational analysis, non-doctrinal actor/institution operationalization, historical causal-strength calibration, and historical inferential synthesis. Does NOT own literature search/retrieval, historical source-criticism standard definition, econometric estimation/stochastic admissibility, formal macroeconomic modeling, manuscript drafting, prose editing, or peer-review refereeing.
---

# Political-Economy Research Methodology (`political-economy-research`)

## 1. Capability Charter & Canonical Ownership (`M0`)

`political-economy-research` is the **sole canonical owner** of `political_economy_research_methodology` (`DOMAIN_SKILL` — author-side methodological reasoning).
- **Current Runtime Path:** `political-economy-research/`
- **Future Wave-F Target Path:** `skills/domain/political-economy-research/` *(FUTURE WAVE-F TARGET PATH — NOT A WAVE-D MOVE)*

### 1.1 Three-Part Ownership Test
A task is **OWNED** by `political-economy-research` when **all three** conditions hold:
1. **Explanandum:** The inquiry asks *how, why, when, or in relation to what* a historically situated political-economic configuration formed, persisted, transformed, or varied across cases.
2. **Evidentiary Basis:** Answering the inquiry requires reasoning over historical, institutional, documentary, archival, or sequence evidence (alone or in composition with quantitative/formal inputs).
3. **Deliverable:** The output is an author-side comparative-historical research design, periodization, mechanism specification, rival-mechanism adjudication, relational comparison assessment, or calibrated historical causal claim.

If (1) and (2) hold but (3) requests another component's deliverable (e.g., an econometric test, a formal ODE proof, a manuscript section, or a referee report), the task is **COMPOSED** under `INFERENTIAL-TASK JURISDICTION` (§4).

### 1.2 Owned Capabilities (`O1`–`O7`)
- **`O1` Comparative-Historical Research Design:** Explanandum specification, case and unit-of-analysis construction, temporal scope, scope conditions, within-case vs. cross-case inference strategy, and comparison mode selection.
- **`O2` Historical Periodization:** Explicit period criteria, boundary typing (`HISTORICAL_INSTITUTIONAL`, `STATISTICAL_BREAK`, `CYCLICAL_FLUCTUATION`, `CONVENIENCE`, `CONTESTED`), transition intervals, alternative periodizations, and anti-reverse-engineering discipline.
- **`O3` Mechanism Specification & Process Tracing:** Decomposing causal chains (`ANTECEDENT → MECHANISM → INTERMEDIATE PROCESS → ACTOR / INSTITUTIONAL RESPONSE → CONSEQUENCE`), deriving step-level observable implications, evaluating sequence and negative evidence, and adjudicating rival mechanisms via qualitative diagnosticity, equifinality, and conjunctural causation.
- **`O4` Comparative-Relational Analysis:** Distinguishing `PARALLEL COMPARISON` from `RELATIONAL EXPLANATION` and `HYBRID` designs using substantive structural evidence of cross-case linkages (trade, finance, ownership, policy transmission, institutional dependence, geopolitical hierarchy, migration, technology transfer, monetary relations, commodity-chain dependence) without universal numeric thresholds.
- **`O5` Non-Doctrinal Actor & Institution Operationalization:** Translating theoretical frameworks about states, classes, class fractions, coalitions, firms, labor organizations, parties, bureaucracies, and international actors into competing, operationalized, testable mechanisms.
- **`O6` Historical Causal-Strength Calibration:** Calibrating every substantive historical causal conclusion against step-level evidence, rival mechanisms, negative evidence, downgrade triggers, and scope conditions to set the **substantive causal-strength ceiling** for downstream writing.
- **`O7` Historical Inferential Synthesis:** Synthesizing already-adjudicated historical, econometric, and formal-model inputs into historical mechanism explanations without overriding any method's jurisdiction.

### 1.3 Explicit Non-Ownership & Hard Prohibitions
`political-economy-research` **never** owns or performs the following:
- **Search, Retrieval & Fact Verification:** Literature search, archival discovery, citation verification, and dated-fact extraction (`timeline.yaml`) belong exclusively to [`deep-research`](file:///c:/ReposGitHub/academic-research-skills/deep-research/SKILL.md). When evidence is missing, PE issues structured **Evidence Requests** rather than fabricating or searching.
- **Historical Source-Criticism Standard:** The claim-relative standard for evaluating `(source, claim)` pairs belongs exclusively to [`shared/protocols/historical_source_criticism_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/historical_source_criticism_protocol.md). PE consumes and applies that protocol; it never encodes a universal `PRIMARY SOURCE > SECONDARY SOURCE` hierarchy.
- **Stochastic Admissibility & Econometric Estimation:** Integration order ($I(d)$), unit-root testing, cointegration, structural break detection, estimator selection, and parameter inference belong exclusively to `applied-econometrics-pe`.
- **Formal Macroeconomic Modeling:** Formal equations, closures, Stock-Flow Consistent (SFC) matrices, BOP formalization, and dynamical stability proofs belong exclusively to `heterodox-macro-modeling`.
- **Manuscript Lifecycle & Drafting:** Section architecture, prose drafting, and citation formatting belong to [`academic-paper`](file:///c:/ReposGitHub/academic-research-skills/academic-paper/SKILL.md).
- **Prose Style & Verb Selection:** Economics rhetoric, BLUF, and sentence-level verb phrasing within the calibrated causal ceiling belong to [`econ-write`](file:///c:/ReposGitHub/academic-research-skills/econ-write/SKILL.md) and [`shared/protocols/prose_discipline_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/prose_discipline_protocol.md).
- **Simulated External Peer Review:** Referee reports, editorial decisions, and scored critiques belong exclusively to [`academic-paper-reviewer`](file:///c:/ReposGitHub/academic-research-skills/academic-paper-reviewer/SKILL.md).
- **Workflow Orchestration:** Multi-stage pipeline execution and Material Passport state belong to [`academic-pipeline`](file:///c:/ReposGitHub/academic-research-skills/academic-pipeline/SKILL.md).
- **Profile Calibration Doctrine:** Scholar, advisor, and committee calibration profiles are **explicit opt-in calibration only** (§5.1).
- **Doctrinal Theory Encyclopedias:** Theory is an active input used to generate concepts and rival testable mechanisms (`O5`); PE does not maintain doctrinal encyclopedias or privilege any school as repository truth.

---

## 2. Canonical Reasoning Workflow & Module Routing

Every substantive political-economy inquiry executes a disciplined 5-stage reasoning sequence routed across four reference modules:

```text
[1. EXPLANANDUM, SCOPE & COMPARISON MODE]  (M1: research_design_and_comparison.md)
    Define outcome to explain, unit of analysis, temporal/case scope, and evaluate
    independence vs. relational linkage predicates (PARALLEL / RELATIONAL / HYBRID).
          ↓
[2. HISTORICAL PERIODIZATION & BOUNDARY TYPING]  (M2: periodization.md)
    Declare explicit period criterion, type boundaries (HISTORICAL_INSTITUTIONAL,
    STATISTICAL_BREAK, CYCLICAL_FLUCTUATION, CONVENIENCE, CONTESTED), and check
    econometric break alignment without universal ±N-year tolerances.
          ↓
[3. RIVAL MECHANISM SPECIFICATION & PROCESS TRACING]  (M3: mechanism_reasoning.md)
    Operationalize theories into >=2 rival mechanisms:
    ANTECEDENT → MECHANISM → INTERMEDIATE PROCESS → ACTOR/INSTITUTIONAL RESPONSE → CONSEQUENCE.
    Specify step-level expected observable traces and trace-expectation bases.
          ↓
[4. CLAIM-RELATIVE EVIDENCE ADJUDICATION]  (M3 + historical_source_criticism_protocol.md)
    Evaluate documentary/historical evidence per (source, claim) pair via the shared
    protocol. Adjudicate rival mechanisms across sequence, diagnosticity, negative
    evidence, equifinality, and conjunctural causation.
          ↓
[5. CAUSAL-STRENGTH CALIBRATION & SYNTHESIS]  (M4: causal_claim_calibration.md)
    Calibrate causal conclusions against weakest critical links, rivals, negative
    evidence, downgrade conditions, and cross-method status (CONVERGENT, COMPLEMENTARY,
    DIVERGENT, ABSENT) to export the substantive causal-strength ceiling.
```

### Reference Module Routing Table

| Module ID | Reference Path | Owned Capabilities & Core Reasoning Load | When to Route |
|:---|:---|:---|:---|
| **M1** | [`references/research_design_and_comparison.md`](file:///c:/ReposGitHub/academic-research-skills/political-economy-research/references/research_design_and_comparison.md) | `O1` + `O4`: Comparative-historical design; specialization over generic `deep-research` Pattern 2; case/unit construction; Galton's problem; `PARALLEL` vs. `RELATIONAL` vs. `HYBRID` mode selection; substantive relational evidence predicates. | Designing comparative-historical studies, selecting cases, testing case independence, or evaluating transnational/center–periphery linkages. |
| **M2** | [`references/periodization.md`](file:///c:/ReposGitHub/academic-research-skills/political-economy-research/references/periodization.md) | `O2`: Period criteria; 5-type boundary classification; transition intervals; alternative periodizations; PE ↔ Econometrics break reconciliation (`EI-2`, `EI-3`, `EI-6`); anti-reverse-engineering guard. | Constructing historical periods, typing regime boundaries, or reconciling institutional turning points with econometric structural breaks. |
| **M3** | [`references/mechanism_reasoning.md`](file:///c:/ReposGitHub/academic-research-skills/political-economy-research/references/mechanism_reasoning.md) | `O3` + `O5`: 5-link process-tracing grammar; non-doctrinal actor/institution operationalization; rival mechanisms; expected traces; sequence and negative evidence; diagnosticity; equifinality; conjunctural causation; causal-process observations (`CPOs`). | Formulating competing causal mechanisms, tracing within-case decision processes, evaluating archival silences, or discriminating between rival theories. |
| **M4** | [`references/causal_claim_calibration.md`](file:///c:/ReposGitHub/academic-research-skills/political-economy-research/references/causal_claim_calibration.md) | `O6` + `O7`: Substantive causal-strength calibration; downgrade triggers; weakest-link rule; optional `C0`–`C8` calibration spectrum; mixed-methods synthesis (`INFERENTIAL-TASK JURISDICTION` and `NO CROSS-METHOD OVERRIDE`). | Determining how strong a causal claim the evidence supports, resolving conflicts between archival, econometric, and formal-model findings, or preparing claims for drafting. |
| **Shared Protocol** | [`../shared/protocols/historical_source_criticism_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/historical_source_criticism_protocol.md) | Claim-relative `(source, claim)` evaluation via the `D1`–`D14` diagnostic repertoire (applied where relevant, not as a mandatory 14-item checklist per `D4-L3`); prohibition of universal `primary > secondary` hierarchies; historical statistics `CONSTRUCTION PROVENANCE` vs. `STOCHASTIC ADMISSIBILITY`. | Whenever archival, documentary, institutional, testimonial, or reconstructed statistical sources materially bear on a claim. |
---

## 3. Supported vs. Mandatory Distinction (`CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT`)

In accordance with the repository governance invariant **`CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT`**, this skill strictly separates **mandatory reasoning obligations** from **supported (optional) vocabularies, taxonomies, and serialization formats**:

| Analytical Layer | `MANDATORY` (Binding Reasoning Obligation) | `SUPPORTED` (Optional Vocabulary / Serialization / Project Parameter) |
|:---|:---|:---|
| **Historical Source Assessment** | Evaluate sources relative to the specific claim (`(source, claim)` pair); assess access, proximity, strategic incentives, corroboration, and archival silence; never apply `PRIMARY > SECONDARY` universally. | Structured `Source–Claim Assessment Record` table serialization (`shared/protocols/historical_source_criticism_protocol.md` §8); explicit treatment of non-applicable repertoire dimensions (`D1`–`D14` are evaluated only where relevant per `D4-L3`). |
| **Process Tracing & Diagnosticity** | Trace `ANTECEDENT → MECHANISM → INTERMEDIATE PROCESS → ACTOR/INSTITUTIONAL RESPONSE → CONSEQUENCE`; specify rival mechanisms, expected observable implications, sequence evidence, negative evidence (`trace_expectation_basis`), diagnosticity, equifinality, conjunctural causation, and `CPOs`. | Van Evera test labels (`straw-in-the-wind`, `hoop`, `smoking-gun`, `doubly-decisive`); Beach & Pedersen variants; Mahoney & Thelen institutional change labels (`layering`, `drift`, `conversion`); Bayesian likelihood ratios (supported **only** when a project explicitly supplies a justified probabilistic design). |
| **Periodization & Break Alignment** | Declare period criterion; classify boundaries (`HISTORICAL_INSTITUTIONAL`, `STATISTICAL_BREAK`, `CYCLICAL_FLUCTUATION`, `CONVENIENCE`, `CONTESTED`); justify break alignment via granularity, lag, or transition duration; flag post-estimation revisions. | Explicit numerical alignment windows (e.g., `±k` years/quarters — valid **only** as a project-declared, method-justified parameter, never a universal constant). |
| **Comparative-Relational Mode** | Distinguish `PARALLEL COMPARISON` from `RELATIONAL EXPLANATION` and `HYBRID`; substantiate relational claims with concrete evidence of cross-case transmission channels. | Tilly (`individualizing`, `encompassing`) or Skocpol & Somers comparative labels; McMichael `incorporated comparison` terminology. (Universal numeric flow thresholds are **prohibited**.) |
| **Causal-Strength Calibration** | Calibrate every substantive historical causal conclusion against evidence, rivals, negative evidence, downgrade triggers, and scope conditions; enforce weakest-link and non-override rules. | Discrete class codes `C0`–`C8` (`M4` §2) and explicit `A1`–`A6` Markdown/YAML artifact tables (required only when high-stakes deliverables or formal evaluations warrant full tabular serialization). |

---

## 4. Cross-Domain Composition & Non-Override Contract

### 4.1 Inferential-Task Jurisdiction
> **PRIMARY ANALYTIC OWNER = the component owning the requested inferential operation, not merely the substantive object being studied.**

Studying a historical episode does not grant `political-economy-research` jurisdiction over statistical testing or formal mathematical derivation:
- **Historical mechanism & causal process questions** $\to$ Primary owner: `political-economy-research`.
- **Statistical relationship, integration/cointegration, or structural break detection questions** $\to$ Primary owner: `applied-econometrics-pe`.
- **Formal model equilibrium, closure consistency, or dynamic stability questions** $\to$ Primary owner: `heterodox-macro-modeling`.

### 4.2 Unbreachable Non-Override Rules (`NO CROSS-METHOD OVERRIDE`)
1. **`NO-1` (No Narrative Override of Econometrics):** Qualitative historical mechanisms never override or invalidate an econometric verdict or non-finding.
2. **`NO-2` / `EI-1` (Coefficient $\neq$ Historical Mechanism):** An econometric parameter estimate can corroborate or contradict an observable implication of a mechanism, but cannot by itself establish that a historical mechanism operated without within-case process evidence.
3. **`NO-3` / `MI-1` (Formal Model $\neq$ Historical Evidence):** A formal macroeconomic model generates candidate mechanisms and testable implications; mathematical consistency with a period supports at most `Institutional Compatibility` until historical evidence traces the mechanism's operation.
4. **`NO-4` / `EI-4` (No Narrative Rescue of Statistical Non-Findings):** PE must never invent post-hoc historical regime shifts to rescue failed cointegration tests or insignificant coefficients. Any regime-change hypothesis requires independent historical evidence in `M2`.
5. **`EI-2` & `EI-3` (Break $\neq$ Boundary & Boundary $\neq$ Break):** A statistical break (`STATISTICAL_BREAK`) is promoted to `HISTORICAL_INSTITUTIONAL` only with independent historical evidence of criterion change. Conversely, a historically documented institutional boundary without a detected statistical break remains a valid historical boundary while the statistical non-finding is reported truthfully.
6. **Historical Statistics Split:** Historical source criticism evaluates `CONSTRUCTION PROVENANCE` (archival compilation, coverage, definitional changes, interpolation); `applied-econometrics-pe` evaluates `STOCHASTIC ADMISSIBILITY` (unit roots, cointegration, break significance, estimator validity).

---

## 5. Profile Isolation & Project-Specific Leakage Guard

### 5.1 Profiles Are Explicit Opt-In Calibration Only
`political-economy-research` operates in theory-pluralist, non-doctrinal mode by default. Scholar, advisor, and committee calibration profiles are **never** default inputs:
- When explicitly activated by the user or workflow, a profile may **change inquiry emphasis**, **suggest additional rival questions**, or **foreground specific analytical concepts**.
- A profile may **NEVER** alter evidentiary standards, modify causal-strength calibration thresholds, remove rival explanations, supply default periodizations or mechanisms, or act as a hidden methodology provider.

### 5.2 Project-Specific Leakage Prohibition
Canonical instructions in `SKILL.md` and `references/*.md` must remain universal across regions, eras, and theoretical traditions. Project-specific case lists, country names, historical dates, alignment tolerances, and regime labels belong exclusively in Workspace Project Overlays or in explicitly tagged `ILLUSTRATION — NON-CANONICAL` examples rotated across $\ge 3$ distinct regions and eras.
