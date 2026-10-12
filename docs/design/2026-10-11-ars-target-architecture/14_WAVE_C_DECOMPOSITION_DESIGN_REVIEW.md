# ARS Wave C Legacy Component Decomposition Design Review

**Document ID:** `14_WAVE_C_DECOMPOSITION_DESIGN_REVIEW.md`
**Status:** PROPOSED ARCHITECTURAL DESIGN (Wave C0 Review)
**Date:** 2026-10-12
**Baseline Git Commit:** `a797db9`
**Scope:** Structural decomposition design for legacy persona and governance candidates: `advisor-reviewer`, `PE-phd-committee`, `prose-register-critic`, and `editorial-governance Phase 1`
**Execution Authority:** Design specification only. No runtime modifications, physical migrations, or skill deletions authorized during Wave C0.

---

## 1. Executive Decision

The Academic Research Skills (ARS) suite requires an explicit architectural decomposition of legacy and candidate components before physical restructuring (Wave F). Under the governing architectural rule:

> **One capability, one canonical owner (`forbidden_duplicate_owners: true`).**

All review machinery, manuscript lifecycle logic, and disciplinary standards have already been bound to their canonical owners (`academic-paper-reviewer`, `academic-paper`, and `econ-write`). Consequently, the four candidate areas reviewed here are resolved as follows:

1. **`advisor-reviewer`:** Decompose into a reusable static scholar calibration profile (`profiles/advisors/michael-ash.md`) and a project-specific overlay (`projects/dissertation-ch1/`). Strip all duplicated generic peer-review and manuscript advice.
2. **`PE-phd-committee`:** Decompose into individual scholar calibration profiles (`profiles/scholars/deepankar-basu.md`, `profiles/scholars/kevin-young.md`, shared `profiles/advisors/michael-ash.md`) and a declarative committee composition profile (`profiles/committees/umass-pe.md`). Route all defense dialogue and referee simulation through canonical `academic-paper-reviewer`.
3. **`prose-register-critic`:** Reclassify from an independent top-level skill into a shared disciplinary protocol (`shared/protocols/prose_discipline_protocol.md`) and deterministic lexical lint tools (`tools/prose_checks/`). Eliminate AI-detector false positives while protecting domain technical terminology (Category A).
4. **`editorial-governance Phase 1`:** Absorb into a lightweight shared protocol (`shared/contracts/passport/editorial_governance.schema.json`) paired with a deterministic verification engine (`scripts/revision_guard.py`) integrated as an optional sidecar port in the Material Passport architecture. Reject heavy cryptographic DAG machinery and multi-party distributed consensus.

---

## 2. Baseline & Invariants

### 2.1 Frozen Commit Sequence
The design review is anchored strictly to commit `a797db9`:
- `63f7b33`: Freeze ARS target architecture and Wave A repository baseline
- `06b46b3`: feat(governance): establish integrated ARS registry (Wave B0)
- `8bdc0df`: docs(econ-write): add evaluation examples and ranked sources
- `a87e8b2`: feat(routing): enforce ARS capability precedence (Wave B1)
- `a797db9`: test(routing): add adversarial precedence cases (Wave B1.1)

### 2.2 Invariant Architectural Bounds
The following architectural decisions are locked and non-negotiable:
- **Canonical Manuscript Lifecycle:** Owned exclusively by `academic-paper`.
- **Economics Disciplinary Writing Policy:** Owned exclusively by `econ-write`.
- **Simulated External Peer Review:** Owned exclusively by `academic-paper-reviewer`.
- **Workflow Orchestration Control Plane:** Owned exclusively by `academic-pipeline`.
- **Evidence & Citation Lineage:** Owned by `deep-research` and `shared/contracts/passport/`.
- **Advisor & Committee Operational Role:** Strictly `CALIBRATION_ONLY` inputs to `academic-paper-reviewer`; never competing review engines.
- **Current-Path Execution Rule:** All runtime dispatch contracts continue resolving to live root directories until Wave F physical repository migration.

---

## 3. Legacy Component Inventory

| Component Path | Current Structural Form | Declared Purpose | Size / Files | Target Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| `advisor-reviewer/` | Root Skill (`SKILL.md`) | Reviewer calibrated for Michael Ash & UMass PE econometrics | 99 lines (1 file) | `PROFILE` + `PROJECT_OVERLAY` |
| `PE-phd-committee/` | Root Skill (`SKILL.md`) | Doctoral defense simulator with 3 UMass PE committee personas | 117 lines (1 file) | `PROFILE` (Composition + Member Personas) |
| `prose-register-critic/` | Root Skill (`SKILL.md`) | AI-trace lexical discipline auditor & jargon checker | 148 lines (1 file) | `SHARED_PROTOCOL` + `TOOL` |
| `docs/design/2026-10-10-editorial-governance/` | Design bundle + untracked candidate code | Append-only human editorial decision & revision verification engine | 8 design docs, 2 schemas, 2 test suites, 1 CLI | `SHARED_PROTOCOL` + `TOOL` (Material Passport Port) |

---

## 4. `advisor-reviewer` Decomposition

### 4.1 Granular Capability Dissection
`advisor-reviewer` contains a mixture of reusable advisor heuristics, duplicated generic review mechanics, duplicated writing rules, and narrow dissertation chapter refutations.

```
advisor-reviewer/SKILL.md
 ├── [A] Reusable Advisor Calibration ───────────► profiles/advisors/michael-ash.md
 ├── [B] Generic Peer Review Machinery ──────────► DUPLICATE (academic-paper-reviewer)
 ├── [C] Generic Writing Guidance (BLUF/Voice) ──► DUPLICATE (academic-paper / econ-write)
 ├── [D] Chapter 1 / Shaikh Project Logic ───────► PROJECT_OVERLAY (projects/dissertation-ch1/)
 ├── [E] Inferred Personality Speculation ───────► REJECT
 └── [F] Phantom Skill References ───────────────► REJECT / CLEANSE
```

### 4.2 Detailed Categorization & Action Plan
1. **Advisor-Specific Calibration (`EXTRACT_TO_PROFILE`):**
   - *Econometric Simplicity & Cointegration Basics:* Demystifying admissibility via counterfactuals; requiring explicit discussion of residual nonstationarity rather than concealing it under specification search criteria.
   - *Descriptive Grounding (Marglin Emulation):* Supplementing parametric regressions with casual, non-parametric, descriptive data trends (GDP, employment, capital stock growth) to keep econometric abstractions grounded in physical realities.
   - *Workplace Transmission Mechanisms:* Deconstructing macroeconomic black boxes into institutional workplace dynamics (labor-capital conversion, technical change, distributional conflict).
   - *Tone & Clarity:* Demanding that theoretical literature reviews be brought "down to earth," free from academic posturing, defensive heterodox jargon, or snobbish tone.
   - *Pedagogical Numerical Punchlines:* Concrete, intuitive round numbers (e.g. $g_k = 3\%, \theta = 0.8$) illustrating what is dynamically at stake.
   - *Target:* `profiles/advisors/michael-ash.md`.
2. **Duplicated Generic Review Machinery (`DUPLICATE_REMOVE_AFTER_MIGRATION`):**
   - Diagnostic Review Protocol (Section 7), 10-point checklists, prioritized revision matrix generation.
   - Already owned canonically by `academic-paper-reviewer`.
3. **Duplicated Manuscript Advice (`DUPLICATE_REMOVE_AFTER_MIGRATION`):**
   - Active voice, avoiding passive AI phrasing ("Furthermore", "Moreover"), BLUF introduction formula, and immediate variable definitions.
   - Already owned canonically by `econ-write` and `academic-paper`.
4. **Project-Specific Material (`PROJECT_OVERLAY`):**
   - Explicit references to Chapter 1 ("Critical Replication of Shaikh's capacity utilization chapter", `CH1_CriticalReplication.pdf`).
   - Diego Polanco candidate writing profile (`profit_rate_chile.pdf`).
   - Specific section and table references (Section 2.3, Section 3, Section 4.3 Stage S1, Section 4.6 Stage S2, Table 1).
   - Specific dataset and model specifications (US 1947–2011 Shaikh database, restriction counterfactual $\theta=1$, no-dummy cointegration check).
   - The 68-item `Feedback_Matrix.xlsx` (Page 17 labor vs latent capacity; Page 7 VECM specification space).
   - *Target:* Isolated to external dissertation workspace overlay `projects/dissertation-ch1/` (outside canonical ARS core).
5. **Inferred Personality Speculation (`REJECT`):**
   - Speculative psychological assertions (e.g., "The advisor is confused by this second derivative of capital"). Must be reformulated into objective methodological guidance: "Clarify the second derivative $d\hat{k}/dt$ as an acceleration term and analyze its dynamic boundary conditions."
6. **Phantom Skill References (`REJECT / CLEANSE`):**
   - References to non-existent skills `umass-applied-econometrics` and `heterodox-economics-review` must be purged.

---

## 5. `PE-phd-committee` Decomposition

### 5.1 Persona Decoupling: Scholar Profiles vs. Committee Composition
`PE-phd-committee` couples three distinct academic scholar personas with doctoral defense execution mechanics and specific dissertation chapter proofs. The target architecture separates individual scholar evidence from committee composition logic.

```
PE-phd-committee/SKILL.md
 ├── Member 1: Michael Ash ──────────────────────► profiles/advisors/michael-ash.md
 ├── Member 2: Deepankar Basu ───────────────────► profiles/scholars/deepankar-basu.md
 ├── Member 3: Kevin Young ──────────────────────► profiles/scholars/kevin-young.md
 ├── Committee Composition & Roles ──────────────► profiles/committees/umass-pe.md
 ├── Pre-Defense & Defense Review Engine ────────► DUPLICATE (academic-paper-reviewer)
 └── Specific Chapter Proofs (ODE/Dummies) ──────► PROJECT_OVERLAY (projects/dissertation-ch1/)
```

### 5.2 Individual Member Profiles (`EXTRACT_TO_PROFILE`)
1. **Michael Ash (Chair / Applied Econometrics):**
   - Focuses on econometric transparency, PSS bounds test sensitivity, descriptive data grounding, and workplace microfoundations.
   - Unified with the profile extracted from `advisor-reviewer`.
2. **Deepankar Basu (Internal Member / Marxian Theory & Mathematical Econometrics):**
   - *Theoretical Lens:* Marxian reproduction schemas, growth theory, supermultiplier dynamics, and Cambridge capital controversy boundaries.
   - *Mathematical Auditing:* Leontief production function microfoundations ($Y_t = \min\{A_t L_t, \mu_t B_t K_t\}$), dimensional analysis (enforcing transcendental operations only on dimensionless ratios; eliminating "log-dollars"), and dynamic system ODE stability.
   - *Target:* `profiles/scholars/deepankar-basu.md`.
3. **Kevin Young (External Member / History & Social Movements):**
   - *Historical Lens:* Modern US and Latin American political economy, class struggle, and institutional shocks.
   - *Methodological Stance:* Rejects treating history as a passive statistical backdrop; views institutional shocks as active regulators of capacity utilization and econometric stationarity.
   - *Historical Event Mapping:* Connecting statistical step-shifts to structural ruptures (1956 post-Korean War defense budget stabilizers; 1974 Bretton Woods collapse and OPEC price shock; 1980 Volcker interest-rate shock and neoliberal wage repression).
   - *Target:* `profiles/scholars/kevin-young.md`.

### 5.3 Committee Composition Profile (`EXTRACT_TO_PROFILE`)
- A declarative specification file (`profiles/committees/umass-pe.md` or `.yaml`) detailing:
  - Committee roster: Chair (Michael Ash), Internal Economics (Deepankar Basu), External History (Kevin Young).
  - Role hierarchy and Chair synthesis protocol (synthesizing referee reports into a Chair's Memo & Roadmap).
  - Operational parameters for pre-defense review vs. oral defense Socratic dialogue.

### 5.4 Duplicated Generic Defense Engine (`DUPLICATE_REMOVE_AFTER_MIGRATION`)
- Pre-defense review generating 3 independent referee reports is identical to `academic-paper-reviewer` multi-referee panel execution.
- Defense deliberation issuing an Editorial Decision Letter (Pass, Minor Revision, Major Revision) + Prioritized Revision Roadmap duplicates `academic-paper-reviewer` decision synthesis.
- Hardening rules (banning evasive candidate answers, enforcing adversarial Socratic follow-up) belong to the `academic-paper-reviewer` defense mode protocol.

### 5.5 Project-Specific Assumptions (`PROJECT_OVERLAY`)
- Specific candidate identity ("Diego"), specific chapter equations (Bernoulli ODE linearization $v = \hat{k}^{-1}$, Johansen reduced-rank vector restriction $r=1$, and specific negative signs on 1956/1974/1980 dummy coefficients).
- Quarantined to `projects/dissertation-ch1/`.

---

## 6. `prose-register-critic` Decomposition

### 6.1 Semantic Reclassification
`prose-register-critic` was authored as a standalone skill, but intellectually it is a **shared disciplinary protocol** accompanied by **deterministic checking tools**. It must not remain a parallel writing engine or a conflicting editorial gate.

```
prose-register-critic/SKILL.md
 ├── Core Invariant & 3-Tier Classification ─────► shared/protocols/prose_discipline_protocol.md
 ├── 11 Auditing Pattern Families ───────────────► shared/protocols/prose_discipline_protocol.md
 ├── Evidential Claim-Strength Verb Rules ───────► shared/protocols/prose_discipline_protocol.md
 ├── Deterministic Lexical Scanner Tools ────────► tools/prose_checks/check_jargon_leakage.py
 ├── Standalone Skill Wrapper ───────────────────► DUPLICATE / RETIRE (after migration)
 └── AI-Detector Over-Censorship Risks ──────────► REJECT / CALIBRATE
```

### 6.2 Components to Extract to Shared Protocol (`EXTRACT_TO_SHARED_PROTOCOL`)
1. **Core Invariant:** "Technical language is not guilty by association."
2. **Three-Tier Taxonomy:**
   - **Category A: Technical / Conceptual (PROTECT/RETAIN):** Legitimate theoretical, empirical, mathematical, and historical vocabulary (`rate of exploitation`, `companion matrix eigenvalues`, `Johansen trace test`, `supermultiplier`, `effective demand`). Absolutely immune from generic deletion.
   - **Category B: Legitimate but Optional (REVIEW):** Defensible phrasing that becomes an AI tell when clustered locally (`under an unbalanced growth closure`, `transmission mechanism`).
   - **Category C: Rhetorical Scaffolding (REWRITE DIRECTLY):** Vacuous intensifiers, branded metaphors, and pipeline labels (`therapeutic`, `empirical tournament`, `admissibility gates`, `crucially`, `profound institutional divergence`).
3. **Evidential Claim-Strength Calibration:**
   - Strict mapping of verbs to research designs (Descriptive: `documents`, `shows`; VAR: `predicts`, `precedes conditionally`; VECM: `estimates a long-run relation`; GIRF: `conditional dynamic response`; NEVER: `proves`, `validates the true production law`).
4. **Metadata & Pipeline Leakage Filters:**
   - Purging table notes containing script paths, LaTeX internal labels, and prompt echoes.

### 6.3 Components to Extract to Tooling (`EXTRACT_TO_TOOL`)
- Python-based deterministic scanner `tools/prose_checks/check_jargon_leakage.py` (authoring the missing script to validate against Category C patterns without external dependencies).
- Verification test suite under `tools/prose_checks/tests/`.

### 6.4 Stylistic Traps and AI-Detector False Positives (`REJECT / GUARD`)
- **Indiscriminate Word Banning:** Reject naive blacklists that flag standard academic words like `vernacular`, `rubric`, or `plethora` when used in legitimate historical/institutional context.
- **Stateful Memory Snowball:** The proposed `prose_learning_ledger.json` dynamic blacklist risks accumulating false positives across chapters. It must remain strictly bounded to explicitly confirmed Category C terms.
- **Sentence Length Flattening:** Enforce sentence cadence variation (short punchy declarations interlocked with compound analytical sentences) rather than rigid mechanical word-count limits.

---

## 7. `editorial-governance Phase 1` Decomposition

### 7.1 Evaluation of Protected Candidate Bundle
The protected Phase 1 candidate bundle (`docs/design/2026-10-10-editorial-governance/`, `scripts/revision_guard.py`, schemas, evals) implements a rigorous revision verification system. However, parts of it reflect heavyweight product-level infrastructure disproportionate to academic research repository requirements.

```
editorial-governance Candidate Bundle
 ├── [A] Durable Core Principles ───────────────► PRESERVE & MIGRATE
 │    ├── 3-Axis Decision State Model
 │    ├── Scoped Source-Role Contract
 │    ├── Bounded-Diff Anchor Authorization
 │    └── Strict Verification Semantics (PASS/FAIL/INDETERMINATE)
 ├── [B] Heavyweight Cryptographic DAGs ─────────► SIMPLIFY / REJECT
 ├── [C] Multi-Party Trusted Receipt Servers ────► SIMPLIFY / REJECT
 └── [D] Schema Hash Pinning in Records ─────────► REJECT (prevents schema evolution)
```

### 7.2 Durable Ideas to Preserve (`EXTRACT_TO_SHARED_PROTOCOL` + `EXTRACT_TO_TOOL`)
1. **Three-Axis Decision State Model:**
   - *Concern Resolution:* `RESOLVED` / `DELIBERATE_LIMITATION` / `UNRESOLVABLE` / `REVIEWER_DISAGREE`.
   - *Authorization:* `AUTHORIZED` / `HELD` / `BLOCKED` / `PROPOSAL_ONLY`.
   - *Adjudicated Action:* `RETAIN` / `REWRITE` / `RELOCATE` / `REMOVE` (with mandatory `DO_NOT_RESTORE` invariant).
2. **Source-Role Contract:**
   - Scoped linking of specific claims to reference passages.
   - Distinguishing epistemic ownership: `SOURCE_CONTRIBUTION`, `AUTHORIAL_TRANSLATION`, `AUTHORIAL_DERIVATION`.
   - Functional roles: `DIRECT_EVIDENCE`, `HISTORICAL_CONTEXT`, `THEORETICAL_MOTIVATION`, `METHOD_SOURCE`, `INTERPRETIVE_FRAMEWORK`, `COUNTERARGUMENT`, `DATA_SOURCE`.
3. **Bounded-Diff Anchor Authorization:**
   - Enforcing that text modifications strictly respect approved start/end string anchors, preventing collateral edits across unauthorized manuscript sections.
4. **Deterministic Verification Semantics:**
   - Three-state verification: `PASS` (exit 0), `FAIL` (exit 1), `INDETERMINATE` (exit 2). Missing evidence or unanchored edits block release.

### 7.3 Heavyweight Machinery to Simplify or Reject (`REJECT`)
1. **Cryptographic DAGs & Merkle Proofs:** Tracking full SHA-256 parent-child ancestry chains for every minor wording proposal creates unnecessary overhead. Append-only ledger logs with stable IDs (`DEC-001`, `DEC-002`) are sufficient.
2. **External Trusted Receipt Servers:** Multi-signature cryptographic receipt acquisition requires external identity servers. In ARS, Git commit authorship and local Human-in-the-Loop approval events provide sufficient auditability.
3. **Internal Schema Hash Self-Pinning:** Storing SHA-256 hashes of schema files inside runtime verification records prevents non-breaking documentation improvements and schema maintenance.

---

## 8. Material Passport Decision

### 8.1 Evaluated Architecture Options
- **Option A (Passport Extension Monolith):** Merge editorial governance schemas directly into `shared/contracts/passport/passport.yaml` as mandatory top-level fields.
- **Option B (Independent Parallel Contract):** Maintain editorial governance as an entirely distinct contract system unconnected to Material Passport.
- **Option C (Lightweight Shared Contract + Optional Passport Port - RECOMMENDED):** Package editorial governance as a dedicated lightweight contract (`shared/contracts/passport/editorial_governance.schema.json`) that plugs into Material Passport as an optional sidecar port, validated by deterministic tool `scripts/revision_guard.py`.

### 8.2 Architectural Recommendation: Option C
**Rationale:**
1. **Separation of Concerns:** Material Passport tracks lifecycle artifact provenance (`literature_corpus[]`, `audit_artifact[]`, `rejection_log[]`, `reset_boundary[]`). Forcing fine-grained editorial sentence diffs into every routine pipeline pass would bloat passport files.
2. **Lineage Integration:** Maintaining editorial governance in complete isolation (Option B) creates duplicate verification tracking. Option C allows the Material Passport to record high-level revision verification summaries (`editorial_governance_summary` port) while referencing detailed decision records in `editorial_governance.yaml`.
3. **Avoidance of Overengineering:** Option C avoids distributed receipt servers while providing complete deterministic verification of bounded revisions.

### 8.3 Passport Boundary Definition
- **Belongs in Passport Summary (`passport.yaml`):**
  - `governance_id`: Identifier of the governing editorial ledger.
  - `verification_verdict`: `PASS`, `FAIL`, or `INDETERMINATE`.
  - `active_decision_count`: Total active authorized decisions.
  - `source_hash`: SHA-256 of the manuscript source verified.
- **Remains External (`editorial_governance.yaml`):**
  - Detailed per-decision rationale, author arguments, reviewer comment citations, start/end anchor strings, and invariant retirement history.

---

## 9. Cross-Component Duplication Matrix

| Capability | Current Source | Existing Canonical Owner | Proposed Target Role | Proposed Target Destination | Duplication Status | Migration Action | Risk if Removed | Risk if Retained | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Advisor Calibration (Ash)** | `advisor-reviewer` §1, §3 | `academic-paper-reviewer` (engine) | `PROFILE` | `profiles/advisors/michael-ash.md` | FUNCTIONAL_OVERLAY | `EXTRACT_TO_PROFILE` | Loss of Ash-specific research heuristics (simplicity, Marglin grounding) | Persona skill competes with `academic-paper-reviewer` | `advisor-reviewer/SKILL.md` L12-34 |
| **Dissertation Ch1 Overlays** | `advisor-reviewer` §2, §6, §7 | None (project specific) | `PROJECT_OVERLAY` | `projects/dissertation-ch1/` | PROJECT_CONTAMINATION | `PROJECT_OVERLAY` | None to ARS core; preserves dissertation work | Core skill polluted with Shaikh replication constants | `advisor-reviewer/SKILL.md` L8, L88-98 |
| **Committee Member: Basu** | `PE-phd-committee` §1.B | `academic-paper-reviewer` (engine) | `PROFILE` | `profiles/scholars/deepankar-basu.md` | FUNCTIONAL_OVERLAY | `EXTRACT_TO_PROFILE` | Loss of Marxian growth theory and ODE stability review lens | Fragmented reviewer personas in standalone skills | `PE-phd-committee/SKILL.md` L22-29 |
| **Committee Member: Young** | `PE-phd-committee` §1.C | `academic-paper-reviewer` (engine) | `PROFILE` | `profiles/scholars/kevin-young.md` | FUNCTIONAL_OVERLAY | `EXTRACT_TO_PROFILE` | Loss of historical institutional break auditing lens | Fragmented reviewer personas in standalone skills | `PE-phd-committee/SKILL.md` L30-40 |
| **Committee Composition (UMass PE)** | `PE-phd-committee` §1, §2 | `academic-paper-reviewer` (engine) | `PROFILE` | `profiles/committees/umass-pe.md` | FUNCTIONAL_OVERLAY | `EXTRACT_TO_PROFILE` | Loss of composite defense panel structure | Duplicate simulation logic | `PE-phd-committee/SKILL.md` L12-52 |
| **Referee Panel Simulation** | `PE-phd-committee` §3, `advisor-reviewer` §7 | `academic-paper-reviewer` | `CORE_SKILL` | `academic-paper-reviewer` | DIRECT_DUPLICATE | `DUPLICATE_REMOVE_AFTER_MIGRATION` | None; canonical reviewer owns multi-referee panels | Inconsistent scoring, duplicate review workflows | `PE-phd-committee/SKILL.md` L54-73 |
| **Defense Socratic Engine** | `PE-phd-committee` §4 | `academic-paper-reviewer` | `CORE_SKILL` | `academic-paper-reviewer` (defense mode) | DIRECT_DUPLICATE | `DUPLICATE_REMOVE_AFTER_MIGRATION` | Socratic defense mode lost if not added to reviewer | Standalone skill maintains unmaintained dialogue loop | `PE-phd-committee/SKILL.md` L75-94 |
| **Prose Category A/B/C Policy** | `prose-register-critic` §1 | `academic-paper` / `econ-write` (consumers) | `SHARED_PROTOCOL` | `shared/protocols/prose_discipline_protocol.md` | PROTOCOL_CONFLATION | `EXTRACT_TO_SHARED_PROTOCOL` | Loss of Category A technical vocabulary protection | Standalone skill acts as competing writing engine | `prose-register-critic/SKILL.md` L15-32 |
| **11 Auditing Pattern Families** | `prose-register-critic` §3 | `academic-paper` / `econ-write` (consumers) | `SHARED_PROTOCOL` | `shared/protocols/prose_discipline_protocol.md` | PROTOCOL_CONFLATION | `EXTRACT_TO_SHARED_PROTOCOL` | Inconsistent lexical standards across writing skills | Unsynchronized duplicate prompt heuristics | `prose-register-critic/SKILL.md` L51-98 |
| **Deterministic Jargon Scanner** | `prose-register-critic` §7 | None (phantom reference) | `TOOL` | `tools/prose_checks/check_jargon_leakage.py` | MISSING_IMPLEMENTATION | `EXTRACT_TO_TOOL` | Missing automated linting referenced in docs | Broken execution paths in runtime | `prose-register-critic/SKILL.md` L146-148 |
| **3-Axis Revision State Model** | Candidate bundle `05_RECOMMENDED_ARCHITECTURE.md` | `academic-pipeline` (consumer) | `SHARED_PROTOCOL` | `shared/contracts/passport/editorial_governance.schema.json` | CANDIDATE_ISOLATION | `EXTRACT_TO_SHARED_PROTOCOL` | Loss of structured authorization states for revisions | Untracked candidate work remains unintegrated | Candidate `05_RECOMMENDED_...` L9-14 |
| **Bounded-Diff Anchor Verification** | Candidate `scripts/revision_guard.py` | `academic-pipeline` (verifier) | `TOOL` | `scripts/revision_guard.py` (validated core) | CANDIDATE_ISOLATION | `EXTRACT_TO_TOOL` | Inability to prove that revisions stayed within bounds | High risk of unintended regression during rewriting | `scripts/revision_guard.py` |

---

## 10. Conceptual Target State

The target logical organization decouples profiles, protocols, and tools from core skills.

> ⚠️ **Current-Path Warning:** This tree illustrates the conceptual post-Wave-C semantic structure. Physical creation of new root directories is strictly deferred to Wave F.

```
academic-research-skills/
 ├── profiles/                                   [CALIBRATION PROFILES ONLY]
 │    ├── advisors/
 │    │    └── michael-ash.md                   <-- Extracted Ash research heuristics
 │    ├── scholars/
 │    │    ├── deepankar-basu.md                <-- Extracted Basu Marxian & ODE lens
 │    │    └── kevin-young.md                   <-- Extracted Young historical lens
 │    └── committees/
 │         └── umass-pe.md                      <-- Declarative UMass PE committee roster
 │
 ├── shared/                                     [SHARED PROTOCOLS & SCHEMAS]
 │    ├── protocols/
 │    │    └── prose_discipline_protocol.md     <-- Category A/B/C, verbs, pattern families
 │    └── contracts/
 │         └── passport/
 │              ├── editorial_governance.schema.json
 │              └── revision_verification.schema.json
 │
 ├── tools/                                      [DETERMINISTIC VERIFICATION TOOLS]
 │    ├── prose_checks/
 │    │    ├── check_jargon_leakage.py          <-- Category C regex scanner
 │    │    └── tests/test_jargon_leakage.py
 │    └── verification/
 │         └── revision_guard.py                <-- Bounded-diff verifier (promoted core)
 │
 ├── projects/                                   [EXTERNAL PROJECT OVERLAYS]
 │    └── dissertation-ch1/                     <-- Quarantined Shaikh replication data
 │
 └── [LIVE ROOT SKILLS (Executable Baseline)]
      ├── academic-paper/                       <-- Core manuscript lifecycle owner
      ├── econ-write/                           <-- Economics domain policy owner
      ├── academic-paper-reviewer/              <-- Sole canonical review engine (+ defense mode)
      └── academic-pipeline/                    <-- Orchestrator control plane
```

---

## 11. Migration Safety Rules & Anti-Loss Criteria

### 11.1 Tri-Stage Lifecycle Sequence
For every legacy component scheduled for retirement or extraction:
```
1. MIGRATE_FIRST ────────► 2. VERIFY ────────► 3. DEPRECATE_LEGACY_SURFACE
```
No legacy surface may be deprecated or deleted until its preserved content has a canonical destination, passing unit tests, and routing verification.

### 11.2 Explicit Anti-Loss Criteria
1. **Advisor-Specific Calibration:** All unique methodological guidance from Michael Ash (econometric simplicity, Marglin descriptive grounding, workplace microfoundations, cointegration honesty) must be verified verbatim in `profiles/advisors/michael-ash.md`.
2. **Committee Distinctiveness:** The specific intellectual contributions of Deepankar Basu (Marxian growth theory, Leontief microfoundations, ODE stability, dimensional analysis) and Kevin Young (institutional break contextualization, class struggle) must be preserved in distinct scholar profiles.
3. **Prose Protection Invariant:** Category A theoretical vocabulary must remain strictly protected; automated lint tools must be tested against false positives on heterodox and technical terms.
4. **Editorial Decision Provenance:** The 3-axis state model and bounded-diff anchor verification must pass 100% of synthetic gold test cases before candidate promotion.
5. **Review Engine Integrity:** Canonical `academic-paper-reviewer` must demonstrate successful execution of persona-calibrated reviews and defense modes before legacy skills are deprecated.

---

## 12. Proposed Wave C Subwaves

The implementation sequence inside Wave C is organized into five tightly scoped subwaves:

```
[Wave B Baseline: a797db9]
         │
         ▼
 ┌───────────────┐
 │ Subwave C1    │  Shared Prose Discipline Protocol & Tool Extraction
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │ Subwave C2    │  Lightweight Editorial Governance & Passport Integration
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │ Subwave C3    │  Advisor Profile Extraction (Ash) & Project Overlay
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │ Subwave C4    │  Committee Profiles Extraction (Basu, Young, UMass PE)
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │ Subwave C5    │  Legacy Surface Deprecation, Registry Update & Regression Lock
 └───────────────┘
```

- **Subwave C1 (Prose Discipline Protocol & Tooling):** Extract `prose-register-critic` content into `shared/protocols/prose_discipline_protocol.md` and author deterministic scanner `tools/prose_checks/check_jargon_leakage.py`.
- **Subwave C2 (Lightweight Editorial Governance):** Promote candidate schemas into `shared/contracts/passport/` and `scripts/revision_guard.py` with full synthetic test suite.
- **Subwave C3 (Advisor Profile Extraction):** Extract Michael Ash heuristics into `profiles/advisors/michael-ash.md`; isolate Chapter 1 project overlay.
- **Subwave C4 (Committee Profiles Extraction):** Extract Basu and Young profiles into `profiles/scholars/` and composition profile `profiles/committees/umass-pe.md`. Add `defense` mode calibration to `academic-paper-reviewer`.
- **Subwave C5 (Deprecation & Governance Update):** Update `docs/governance/ars_registry.yaml`, deprecate legacy skills (`advisor-reviewer`, `PE-phd-committee`, `prose-register-critic`), and lock routing tests.

---

## 13. Deferred Future Personalization Boundary

In accordance with `10_FUTURE_PERSONALIZATION_BACKLOG.md`:
- **In Scope for Wave C:** Static, hand-curated calibration markdown profiles derived from verified historical supervisory feedback and published papers (`profiles/advisors/michael-ash.md`, etc.).
- **Strictly Deferred to Future Architecture:**
  - Automated corpus-based profile extraction tools (`ars-profile-builder`).
  - Generalized author profile generators from PDF bibliographies.
  - Likely referee/editor persona inference engines.
  - Multi-tenant private profile isolation harnesses.
- **Clean Extension Seam:** Wave C static profiles use standard frontmatter (`profile_id`, `scholar_name`, `epistemic_status`, `methodological_priors`), ensuring future automated tools can generate identical schema profiles without modifying core skills.

---

## 14. Unresolved Human Decisions

The following architectural choices require human review and authorization before implementing Subwaves C1–C5:

1. **Scholar Profile Directory Topology:**
   - *Option 1A:* Unified directory `profiles/scholars/<scholar-name>.md` for all individuals (advisors and committee members alike).
   - *Option 1B (Recommended):* Hierarchical separation: `profiles/advisors/<advisor-name>.md` for primary dissertation supervisors, and `profiles/scholars/<scholar-name>.md` for specialized committee members and domain referees.
2. **Project Overlay Quarantine Location:**
   - *Option 2A (Recommended):* Move dissertation Chapter 1 specifics to an untracked/gitignored directory `projects/dissertation-ch1/` within the repository workspace.
   - *Option 2B:* Preserve dissertation Chapter 1 specifics in a dedicated documentation appendix `docs/legacy/dissertation_ch1_overlay.md`.
3. **Editorial Governance Release Gate Policy:**
   - *Option 3A (Recommended):* Editorial governance verification (`revision_guard.py`) is an opt-in quality gate during Wave C, becoming mandatory for release certification only in Wave D.
   - *Option 3B:* Make editorial governance verification strictly mandatory immediately upon promotion in Subwave C2.

---

## 15. Implementation Readiness Verdict

```
============================================================
WAVE C DECOMPOSITION DESIGN VERDICT:
WAVE_C_DESIGN_READY_FOR_HUMAN_REVIEW
============================================================
```

- **Architecture Alignment:** 100% compliant with ARS target architecture and capability monopoly invariant.
- **Duplication Status:** All legacy capabilities mapped to exactly one canonical owner or static profile.
- **Anti-Loss Guarantees:** All high-value advisor heuristics, theoretical lenses, and prose guidelines preserved.
- **Next Step:** Present design review and accompanying execution plan (`15_WAVE_C_EXECUTION_PLAN.md`) for human sign-off before executing Subwave C1.
