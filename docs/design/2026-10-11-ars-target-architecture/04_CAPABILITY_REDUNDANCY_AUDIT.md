# ARS Capability Redundancy & Intellectual Gap Audit

**Status:** Target Architecture Baseline v0.1  
**Date:** 2026-10-11  
**Repository:** `c:\ReposGitHub\academic-research-skills` (`dpolancon/academic-research-skills`)  
**Scope:** Complete capability ownership, duplication audit, and intellectual gap analysis  

---

## 1. Overview & Four Duplication Dimensions

This audit organizes repository analysis by **CAPABILITY** rather than individual component folders. It identifies where the live working tree violates the primary architectural principle:

> **One capability, one canonical owner.**

The audit categorizes duplication across four distinct dimensions:
1. **Physical Duplication:** The same skill or documentation tree exists at multiple file paths (e.g., committed client mirror directories).
2. **Functional Duplication:** Two independent skills or tools implement the same intellectual workflow or state machine.
3. **Prompt Duplication:** Identical substantive instructions, heuristics, or checklists copied verbatim across multiple `SKILL.md` files.
4. **Governance Duplication:** Multiple registries, schemas, or status files claim canonical authority without synchronization.

---

## 2. Capability Redundancy & Ownership Matrix

| # | Capability | Current Implementers | Canonical Target Owner | Consumers | Type of Duplication | Severity | Recommended Consolidation | Migration Risk |
|---|---|---|---|---|---|---|---|---|
| C01 | **Client Installation & Discovery** | Root folders, `.agents/skills/*`, `.claude/skills/*`, `install-local.ps1` | `clients/` + thin installer/generator | All agent runners | PHYSICAL | **CRITICAL** | Untrack `.agents` and `.claude` full skill blobs in git. Rely on root as single canonical source tree, generating client links/views via `install-local.ps1`. | Low (requires testing agent discovery paths). |
| C02 | **Academic Paper Authoring Lifecycle** | `academic-paper`, `econ-write` | `skills/core/academic-paper` | `academic-pipeline`, users | FUNCTIONAL | **CRITICAL** | `academic-paper` owns the multi-agent writing lifecycle, state machine, and document assembly. `econ-write` supplies disciplinary policy and bounded section drafting. | Low (clarifies intent and slash commands). |
| C03 | **Economics Prose & Section Standards** | `econ-write`, `umass-applied-econometrics`, `advisor-reviewer` | `skills/domain/econ-write` | `academic-paper`, `econ-slides`, users | PROMPT + FUNCTIONAL | **HIGH** | Consolidate all economics writing advice (BLUF, intro formula, model presentation, active voice) in `econ-write`. Remove copied style rules from econometrics and advisor skills. | Low. |
| C04 | **Simulated External Peer Review** | `academic-paper-reviewer`, `PE-phd-committee`, `advisor-reviewer` | `skills/core/academic-paper-reviewer` | `academic-pipeline`, users | FUNCTIONAL | **CRITICAL** | `academic-paper-reviewer` is the sole owner of multi-perspective peer review, editorial decisions, and revision roadmaps. Committee members and advisors become profiles consumed by the reviewer. | Medium (must preserve specialized reviewer personas). |
| C05 | **Internal Author Pre-Submission Review** | `academic-paper` (`peer_reviewer_agent`), `econ-write` (review checklist) | `skills/core/academic-paper` (internal check) | `academic-paper` | FUNCTIONAL | **MEDIUM** | Strict boundary: `academic-paper` internal review is an author self-check before export; it never issues formal journal verdicts or R&R roadmaps. | Low. |
| C06 | **Dissertation Committee Simulation** | `PE-phd-committee` (embedded review workflow) | `skills/core/academic-paper-reviewer` (defense mode) + `profiles/committees/umass-pe` | Doctoral candidate | FUNCTIONAL + PROMPT | **HIGH** | Decompose `PE-phd-committee`. Committee personas (Ash, Basu, Young) become declarative profiles in `profiles/committees/umass-pe`. The defense dialogue and review package route through `academic-paper-reviewer`. | Low. |
| C07 | **Advisor Calibration** | `advisor-reviewer` | `profiles/advisors/michael-ash` | `academic-paper-reviewer`, `academic-paper` | PROMPT + PROJECT | **HIGH** | Decompose `advisor-reviewer`. Reusable feedback standards (econometric simplicity, cointegration honesty, Marglin grounding) become `profiles/advisors/michael-ash`. Chapter 1 specifics offloaded to project overlay. | Low. |
| C08 | **Prose Discipline & AI-Trace Auditing** | `prose-register-critic`, `econ-write`, `academic-paper` (writing quality check) | `shared/protocols/prose_discipline_protocol` + `tools/prose/*` | `academic-paper`, `econ-write`, `public-scholarship` | FUNCTIONAL + PROMPT | **HIGH** | Convert `prose-register-critic` from a top-level skill into a shared protocol (Category A/B/C definitions, claim-strength verbs) and deterministic regex tools (`check_jargon_leakage.py`). | Low. |
| C09 | **Scholarly Slide Production** | `econ-slides`, `econ-write` (presentations section) | `skills/dissemination/econ-slides` | Academic presenters | FUNCTIONAL + PROMPT | **MEDIUM** | `econ-slides` is the sole canonical owner of Beamer presentation workflows. Remove presentation subsections from `econ-write`. Sanitize local `slide_deck_Fondecyt/` from the skill folder. | Low. |
| C10 | **Public Scholarship Translation** | `editor-jacobin-lat`, `econ-write` (policy/op-ed notes) | `skills/dissemination/public-scholarship` | Public writers | FUNCTIONAL + PROMPT | **HIGH** | Separate generic public scholarship translation (de-specialization, hooks, structural arguments) into a reusable skill `public-scholarship`. Isolate Jacobin América Latina rules into `profiles/venues/jacobin-lat`. | Low. |
| C11 | **Applied Political Economy Econometrics** | `umass-applied-econometrics`, `advisor-reviewer` | `skills/domain/applied-econometrics-pe` | `academic-paper`, researcher | PROMPT + PROJECT | **HIGH** | Consolidate forensic replication, integration order governance, and Toda–Yamamoto rules into `applied-econometrics-pe`. Purge rules that force empirical conclusions. | Medium (requires epistemic refactoring). |
| C12 | **Cointegration Specification Audit** | `umass-applied-econometrics/tools/cointegration_specification_audit.md` | `tools/econometrics/cointegration_audit` | `applied-econometrics-pe`, `academic-paper-reviewer` | PROMPT | **MEDIUM** | Move embedded markdown protocol into a standalone, deterministic diagnostic tool under `tools/econometrics/`. | Low. |
| C13 | **Toda–Yamamoto Causality Mapping** | `umass-applied-econometrics/tools/toda_yamamoto_specification_mapping.md` | `tools/econometrics/toda_yamamoto` | `applied-econometrics-pe`, `academic-paper-reviewer` | PROMPT | **MEDIUM** | Move embedded markdown protocol into a standalone, deterministic diagnostic tool under `tools/econometrics/`. | Low. |
| C14 | **IRF / GIRF Plotting & Reporting** | `irf-plotting` (top-level skill) | `tools/plotting/irf_plotting` | Econometrics skills, researcher | TAXONOMY | **LOW** | Retype `irf-plotting` from core skill to specialized tool interface. | Low. |
| C15 | **LaTeX Compilation & Workspace Setup** | `latex-compilation` (top-level skill) | `tools/latex/compile_workspace` | `academic-paper`, `econ-slides`, users | TAXONOMY | **LOW** | Retype `latex-compilation` from core skill to shared deterministic build tool. | Low. |
| C16 | **Editorial Decision Persistence & Verification** | Candidate `editorial-governance Phase 1` (`scripts/revision_guard.py`), `passport.yaml` | `shared/contracts/editorial_governance` + `tools/verification/revision_guard` | `academic-pipeline`, `academic-paper-reviewer` | GOVERNANCE | **MEDIUM** | Absorb the 3-axis decision model and source-contract into the Material Passport as an optional extension; simplify away overengineered cryptographic DAG machinery. | Low. |
| C17 | **Mode & Capabilities Governance** | `MODE_REGISTRY.md` (4 skills, 25 modes), `README.md` (14 skills), `UPDATE_REGISTRY.md` | `CAPABILITY_REGISTRY.yaml` + updated `MODE_REGISTRY.md` | All skills and contributors | GOVERNANCE | **HIGH** | Expand governance to cover the entire suite. Create authoritative `CAPABILITY_REGISTRY.yaml` mapping all capabilities to owners. Update `MODE_REGISTRY.md` to reflect true operational modes across all components. | Low. |
| C18 | **Author Voice Calibration** | `academic-paper` (style calibration), `advisor-reviewer` (Diego style notes) | `profiles/author/diego-academic` | `academic-paper`, `econ-write` | PROMPT + FRAGMENT | **MEDIUM** | Formalize author preferences into versioned profile `profiles/author/diego-academic`, separating durable style preferences from project data. | Low. |

---

## 3. Resolution of Mandatory Component Questions

### 3.1 `econ-write` vs. `academic-paper`
- **Contradiction:** Both skills currently claim to write and rewrite academic economics papers. `academic-paper/SKILL.md` offers a 12-agent pipeline for all academic papers, while `econ-write/SKILL.md` states: *"USE THIS SKILL whenever the user writes, edits, reviews, rewrites, or structures any economics paper... Covers all paper types and all sections."*
- **Resolution:**
  1. **Economics Prose Standards:** Strictly owned by `econ-write` (synthesizing Cochrane, McCloskey, Shapiro, Bellemare).
  2. **Paper Workflow Lifecycle:** Strictly owned by `academic-paper` (12-agent pipeline: intake, structure, drafting, citations, format conversion).
  3. **Revision Workflow:** Strictly owned by `academic-paper` revision modes (coaching, point-by-point response, delta tracking).
  4. **Literature Positioning:** `econ-write` owns the economics "Value Added / 5-10 closest papers / however-narrative" formula; `academic-paper` literature strategist executes the systematic search and gap-matrix assembly.
  5. **Citation Handling:** Owned by `shared/evidence` protocol and `academic-paper` citation compliance agent.
  6. **Internal Quality Review:** Writer-side self-check uses `econ-write` review checklist during drafting.
  7. **External Simulated Peer Review:** Strictly delegated to `academic-paper-reviewer`.
  8. **Operational Rule:** When writing an economics paper end-to-end, `academic-paper` invokes `econ-write` as its disciplinary domain layer. When performing bounded economics editing (e.g., rewriting an introduction, refining an abstract, or drafting a model section), `econ-write` can be invoked directly without launching the full 12-agent pipeline.

### 3.2 `academic-paper-reviewer` vs. `academic-paper` Internal Review
- **Contradiction:** `academic-paper` contains an internal `peer_reviewer_agent`, while `academic-paper-reviewer` runs a 5-reviewer panel. Users may receive conflicting feedback or duplicate review loops.
- **Resolution:**
  - **Writer Self-Evaluation (`academic-paper.peer_reviewer_agent`):** An author-side pre-submission diagnostic run within Stage 2. It checks for logical coherence, unsupported claims, and tone. It **never** issues an Editorial Decision (Accept/Minor/Major/Reject) and **never** produces a formal Revision Roadmap.
  - **Independent Simulated Peer Review (`academic-paper-reviewer`):** An external, adversarial panel run at Stage 3. It enforces rubric secrecy (the drafting agent never sees the private rubric beforehand), executes the Schema 13 sprint contract hard gate, and issues formal journal-style decision packages.

### 3.3 `advisor-reviewer`
- **Contradiction:** Presents itself as an academic reviewer skill, but line 8 declares it is a dissertation rewrite guide for Chapter 1 (Shaikh critical replication), citing `CH1_CriticalReplication.pdf`, `Feedback_Matrix.xlsx` (68 items), and page-specific comments.
- **Resolution:**
  - **Reusable Advisor Profile (`profiles/advisors/michael-ash`):** Durable expectations of Michael Ash (preference for econometric simplicity, cointegration residual honesty, Marglin-style casual descriptive data grounding, deconstructing the workplace "black box", active voice, avoiding condescending heterodox rhetoric).
  - **Generic Review Behavior:** Already owned by `academic-paper-reviewer`.
  - **Chapter-1 Project Legacy:** Exact section numbers (4.3, 4.6), dummy years, ODE derivations, and the 68-item feedback matrix are quarantined to the dissertation project overlay. Standalone `advisor-reviewer` skill is decommissioned.

### 3.4 `PE-phd-committee`
- **Contradiction:** A standalone skill that reimplements the multi-agent review panel and Socratic coaching from `academic-paper-reviewer`, while hardcoding specific dissertation chapter parameters (Basu Appendix ODE, Young 1956/1974/1980 step-shifts).
- **Resolution:**
  - **Generic Defense Workflow:** Owned by `academic-paper-reviewer` via an operational mode `defense`.
  - **Committee Profile (`profiles/committees/umass-pe`):** Contains declarative personas for Michael Ash (Chair/econometrics), Deepankar Basu (Marxian/macro theory/dimensional analysis), and Kevin Young (history/social movements).
  - Standalone `PE-phd-committee` skill is decomposed into a profile and retired.

### 3.5 `prose-register-critic`
- **Contradiction:** Structured as a standalone core skill, but consists of a lexical discipline rulebook, Category A/B/C classification, and calls to Python scripts.
- **Resolution:**
  - **Shared Prose Protocol (`shared/protocols/prose_discipline_protocol.md`):** Owns the Category A (protect technical terms), Category B (review), Category C (rewrite) definitions, evidential claim-strength verbs, and the 11 auditing pattern families.
  - **Deterministic Audit Tools (`tools/prose/*`):** Owns `check_jargon_leakage.py` and `audit_prose_humanize.py`.
  - **Author Voice Profile (`profiles/author/diego-academic`):** Owns author-specific ES $\to$ EN translation calques ("renounce to", "accorded to").
  - `prose-register-critic` ceases to be an independent top-level skill and becomes a shared protocol and tool layer consumed by `academic-paper`, `econ-write`, and `public-scholarship`.

### 3.6 `heterodox-economics-review`
- **Contradiction:** Only 29 lines long; heavily contaminated with the mathematical details of Diego's specific paper refuting Shaikh's Sraffian Supermultiplier model (`paper_refutation_SSM`).
- **Resolution:**
  - Redesign and broaden into `skills/domain/heterodox-macro-modeling`.
  - Must cover general heterodox macro foundations: Post-Keynesian growth and distribution, Marxian reproduction schemes, Sraffian surplus approach, stock-flow consistency, Harrodian instability, and dynamic systems boundary analysis.
  - Purge paper-specific constants ($\theta=0.8, \mu=1$) and single-manuscript proofs.

### 3.7 `umass-applied-econometrics`
- **Contradiction:** Combines sound forensic econometric methods with political economy priors and advisor style preferences, but also contains rules that force empirical conclusions.
- **Resolution:**
  - **Forensic Econometrics:** ADF/KPSS integration-order testing, small-sample bootstrapping ($N \le 30$), $(k+d_{\max})$ Toda–Yamamoto specification mapping, non-parametric visualization. (Retained as core methodological rules and deterministic tools in `tools/econometrics/`).
  - **Political Economy Priors:** Hypotheses regarding endogenous distribution, workplace capacity extraction, and induced technical change. (Priors widen the candidate hypothesis space; they do not dictate results).
  - **Advisor/School Preferences:** Marglin descriptive macro grounding, BLUF principle. (Retained as UMass domain standards).
  - **Paper-Specific Rules:** Specific coefficient interpretations ($\hat{\gamma} \approx 1$ Fordist mechanization, US 1947–2011) quarantined to project overlays.
  - **Epistemic Bias Purge:** Remove Rule H.4 forcing failures to cointegrate to be interpreted as "FX-constrained accumulation regime-switching".

### 3.8 `editor-jacobin-lat`
- **Contradiction:** Conflates generic public scholarship writing with the specific house style of *Jacobin América Latina*.
- **Resolution:**
  - **Generic Public Scholarship (`skills/dissemination/public-scholarship`):** De-specialization without banalization, contemporary hooks, institutional mechanism translation, non-moralizing structural argument, accessible public prose.
  - **Venue Profile (`profiles/venues/jacobin-lat`):** Martín Arboleda criteria, headline conventions (declarative thesis, no subtitle, max 12 words), 1,500–2,500 word length, framing around "bourgeois economics vs critique of political economy", Spanish language register.

### 3.9 `editorial-governance Phase 1`
- **Contradiction:** Created candidate schemas and a verification CLI (`revision_guard.py`), but risks duplicating Material Passport infrastructure and introducing unnecessary cryptographic complexity.
- **Resolution:**
  - **Target Capability Served:** Human editorial decision persistence, authorization state gating (HELD/BLOCKED/AUTHORIZED), claim/source role attribution contract, and revision regression protection.
  - **Generic Core to Preserve:** The 3-axis decision model (Resolution, Authorization, Action), the source contract (distinguishing source proposition vs author translation/derivation), and PASS/FAIL/INDETERMINATE semantics.
  - **Overengineered Parts to Simplify:** Full cryptographic SHA-256 DAGs with predecessor IDs, approval events with independent trusted receipts, complex ancestor chain invariant retirement validation, byte-level snapshot hashes, schema hash pinning inside the verification result.
  - **Consolidation:** Simplify into a lightweight shared contract (`shared/contracts/editorial_governance`) and absorb into the Material Passport / revision verification workflow. Do not expand as a separate distributed-ledger harness.

---

## 4. Epistemic Safeguard Audit: Rules Predetermining Empirical Verdicts

A foundational principle of the target architecture is:
> **Heterodox theory expands hypotheses and interpretive options. It does not predetermine empirical verdicts.**

The audit identified the following explicit violations in the current repository:

### 4.1 Cointegration Failure as Forced Regime-Switching
- **Location:** `umass-applied-econometrics/SKILL.md` Section 2.H, Rule 4:
  > *"For peripheral economies, interpret failures to cointegrate as evidence of structural regime-switching (e.g., FX-constrained accumulation) rather than data deficiency."*
- **Violation:** If an econometric model fails to find cointegration, the empirical result is that the long-run stationary linear combination does not exist in the sample. Ordering the researcher to interpret non-cointegration as proof of an "FX-constrained accumulation regime" forces a theoretical conclusion onto an empirical rejection.
- **Remedy:** Rephrase as an interpretive hypothesis: *"If cointegration fails in peripheral contexts, researchers should test whether structural breaks or balance-of-payments constraints account for parameter instability, rather than immediately assuming data error. However, if structural break models also fail, the absence of cointegration must be reported honestly as an empirical non-finding."*

### 4.2 Hardcoded Historical Regime Signatures
- **Location:** `umass-applied-econometrics/SKILL.md` Section 2.H, Rule 2:
  > *"Interpret sign and magnitude changes across historical sub-windows as regime signatures: $\hat{\gamma} \approx 1$ = balanced Fordist mechanization; $\hat{\gamma} \gg 1$ = decoupled post-Fordist machinery acceleration; $\hat{\gamma} < 0$ = institutional incoherence."*
- **Violation:** Encodes specific empirical point estimates from Diego's dissertation chapter on machinery and structures as universal, timeless theoretical signatures for all economies.
- **Remedy:** Demote specific numerical thresholds to project-specific examples; replace in the domain skill with general guidance on periodization and regime sensitivity.

### 4.3 History as "Active Regulator of Econometric Stationarity"
- **Location:** `PE-phd-committee/SKILL.md` Section 3.D, Rule 3:
  > *"The candidate explains how these shocks act as outlier filters to remove unit roots in VECM residuals, making history and class struggle active regulators of econometric stationarity."*
- **Violation:** Claims that institutional events and class struggle "regulate econometric stationarity," which risks encouraging researchers to add dummy variables post-hoc until residuals become stationary, justifying data-mining through political rhetoric.
- **Remedy:** Enforce standard econometric transparency (Ash): structural step-shift dummies must be justified ex-ante by historical events, and sensitivity to dummy placement must be reported in specification space maps. Dummies do not "cause stationarity"—they model discrete mean-shifts.

---

## 5. Intellectual Gap Test

Each proposed intellectual capability was evaluated against the live repository:

| # | Intellectual Capability | Current Status in Live Repo | Classification | Required Target Action |
|---|---|---|---|---|
| G01 | **Comparative-Historical Political Economy** | Dispersed fragments in `PE-phd-committee` (Kevin Young notes) and `editor-jacobin-lat`. No reusable research framework. | `GENUINE_GAP` | Design candidate domain skill `political-economy-research` once ownership stabilizes. |
| G02 | **Historical Source Criticism** | Absent. `deep-research` covers empirical/scientific databases (Crossref, Semantic Scholar) and PRISMA, but has no guidance for archival, documentary, or primary historical evidence. | `GENUINE_GAP` | Add historical evidence & source criticism protocol to `shared/protocols/` and `political-economy-research`. |
| G03 | **Periodization & Institutional Sequencing** | Mentioned in `umass-applied-econometrics` (regime signatures) and `PE-phd-committee` (step-shift dummies), but lacks rigorous methodological protocol. | `PARTIALLY_COVERED` | Generalize into periodization protocol within `political-economy-research`. |
| G04 | **Process Tracing & Causal Mechanisms** | Absent. No protocols for causal process observations (CPOs), hoop tests, smoking-gun tests, or doubly decisive tests. | `GENUINE_GAP` | Add process tracing guidance to `political-economy-research`. |
| G05 | **Institutional Analysis** | Present in `umass-applied-econometrics` (workplace extraction, Marglin grounding) and `advisor-reviewer` (black box). | `PARTIALLY_COVERED` | Consolidate institutional micro-foundations in `applied-econometrics-pe` and `political-economy-research`. |
| G06 | **Comparative-Relational Reasoning** | Absent. Current repository is strictly single-case / single-manuscript focused. No comparative design guidance. | `GENUINE_GAP` | Add comparative-relational method guidance to `political-economy-research`. |
| G07 | **Center–Periphery Analysis** | Dispersed mentions in `umass-applied-econometrics` and `editor-jacobin-lat`. | `PARTIALLY_COVERED` | Structure uneven development and external constraint methods in `political-economy-research`. |
| G08 | **Marxian / Post-Keynesian Macro Modeling** | Present in narrow 29-line `heterodox-economics-review` (SSM singularities) and `PE-phd-committee` (Basu Leontief notes). | `PARTIALLY_COVERED` | Redesign into full domain skill `skills/domain/heterodox-macro-modeling`. |
| G09 | **Stock-Flow Consistency (SFC)** | Only mentioned as an advisory note in slides references and user testing notes. No SFC matrices, transaction accounts, or balance-sheet checks exist. | `GENUINE_GAP` | Incorporate stock-flow consistency principles and diagnostics into `heterodox-macro-modeling`. |
| G10 | **Theory-to-Empirical Mapping** | Present in `umass-applied-econometrics` Rule G (Integration Order Governance), but limited to time-series cointegration. | `PARTIALLY_COVERED` | Broaden theory-to-empirical mapping across qualitative and historical evidence in `shared/protocols/`. |
| G11 | **Public Scholarship / Dissemination** | Present in `editor-jacobin-lat` (Jacobin columns) and `econ-slides` (Beamer decks), but generic public scholarship absent. | `PARTIALLY_COVERED` | Decompose `editor-jacobin-lat` into generic `public-scholarship` skill + venue profile. |

---

## 6. Desired Architecture Test

The proposed five-layer target architecture:
1. **Core Skills** (`deep-research`, `academic-paper`, `academic-paper-reviewer`)
2. **Domain Skills** (`econ-write`, `applied-econometrics-pe`, `heterodox-macro-modeling`, candidate `political-economy-research`)
3. **Profiles** (`profiles/author/*`, `profiles/advisors/*`, `profiles/committees/*`, `profiles/venues/*`, `profiles/journals/*`)
4. **Tools / Shared Protocols** (`tools/*`, `shared/protocols/*`, `shared/contracts/*`, `evals/*`)
5. **Dissemination Skills** (`econ-slides`, `public-scholarship`)

### Verdict: `CONFIRMED_WITH_REVISIONS`

### Required Architectural Revisions:
1. **Explicit Separation of the Orchestrator:** `academic-pipeline` must not be classified as a standard Core Skill. It is an **Orchestrator** (the control plane). It enforces state transitions, checkpoints, and passport verification, but does not own disciplinary reasoning.
2. **Decouple Logical Layering from Physical Paths:** Do not attempt an immediate physical re-organization into `skills/core/`, `skills/domain/`, etc. Doing so immediately breaks client discoverability (Antigravity slash commands, Claude Code, OpenAI Codex, Windows junctions). Maintain a **logical** classification via `CAPABILITY_REGISTRY.yaml` and client adapters before executing physical file moves.
3. **Quarantine Project Overlays:** The repository contains active and legacy project folders (`paper_refutation_SSM/`, `user_testings/`, `editing_memos/`, `writings_testing/`, `slide_deck_Fondecyt/`). These must be formally quarantined into project overlays or offloaded to project repositories, preventing them from contaminating core library infrastructure.
4. **Simplify Editorial Governance:** The candidate Phase 1 editorial governance framework must be simplified from an overengineered cryptographic DAG into a lightweight shared protocol (`shared/contracts/editorial_governance`) integrated into the Material Passport.
