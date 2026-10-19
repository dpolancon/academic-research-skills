# WAVE D5 — CROSS-DOMAIN ADVERSARIAL BEHAVIORAL EVALUATION REPORT

**Status:** FROZEN BY HUMAN ARCHITECT (2026-10-19) — SEE [`docs/design/wave-d/D5_HUMAN_FREEZE_2026-10-19.md`](file:///c:/ReposGitHub/academic-research-skills/docs/design/wave-d/D5_HUMAN_FREEZE_2026-10-19.md)
**Human Freeze Record:** [`docs/design/wave-d/D5_HUMAN_FREEZE_2026-10-19.md`](file:///c:/ReposGitHub/academic-research-skills/docs/design/wave-d/D5_HUMAN_FREEZE_2026-10-19.md)
**Working Directory:** `C:\ReposGitHub\academic-research-skills`
**Evaluation Fixture:** [`evals/gold/wave_d_behavioral/cases.yaml`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/wave_d_behavioral/cases.yaml)
**Test Runner:** [`scripts/test_wave_d_behavioral_evals.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/test_wave_d_behavioral_evals.py)
**Governing Checkpoint:** `917ee2f2332cef92015937bddd7337a52ef4b12d`
**Runtime Skill/Protocol Modifications:** None (100% Unmodified)
**Registry / Routing Changes:** None
**Commits / Pushes:** None

---

## 0. Executive Verdict

**PASS (DETERMINISTIC CONTRACT & EXECUTABLE FIXTURE ENFORCEMENT) / MODEL-BEHAVIOR EXECUTION PENDING.**

Wave D5 implements the complete cross-domain behavioral evaluation layer for the ratified domain architecture (Waves D1–D4). In strict accordance with the **No Fake Behavioral Enforcement** mandate (§17), ARS distinguishes between what is deterministically verified today and what requires a future live agent execution harness:
1. **Fixture Completeness:** 31 gold adversarial evaluation cases across all 9 required families (`E1`–`E9`) are fully implemented in [`evals/gold/wave_d_behavioral/cases.yaml`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/wave_d_behavioral/cases.yaml).
2. **Schema & Taxonomy Enforcement:** Validated offline via [`scripts/test_wave_d_behavioral_evals.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/test_wave_d_behavioral_evals.py), enforcing `CRITICAL`, `MAJOR`, and `MINOR` severity tiers, required fields, and valid regex rubrics.
3. **Runtime Contract Anchor Verification:** Verified for all 22 contract-anchored cases (28 anchors checked across `political-economy-research/`, `heterodox-economics-review/`, `umass-applied-econometrics/`, and `shared/protocols/historical_source_criticism_protocol.md`), with 9 cases truthfully classified as N/A (NOT CONTRACT-ANCHORED) per D5.1-R1.
4. **Rubric Discrimination Verification:** All 31 `good_response_exemplar` samples pass 100% of required behaviors with zero tripped forbidden behaviors; all 31 `bad_response_exemplar` samples trigger their expected forbidden violation tags.
5. **E9 Meta-Eval Verification:** Proves that self-reported completion summaries are not self-ratifying; auditing an artifact with a hidden invariant violation results in an immediate `FAIL`.
6. **Zero Runtime Modifications:** All 31 protected files across runtime skills, profiles, and governance registries remain byte-for-byte identical to their pre-D5 baseline.

---

## 1. Governing Closed-Wave Locks

Waves D1 through D4 are **CLOSED** and binding. D5 tests their runtime rules without reopening them:

```text
D1 — POLITICAL-ECONOMY OWNERSHIP                CLOSED (Ratified 2026-10-15)
D2 — APPLIED-ECONOMETRICS BOUNDARY              CLOSED (Ratified 2026-10-15)
D3 — HETERODOX-MACRO MODELING                    CLOSED (Ratified 2026-10-16)
D4 — PE RUNTIME + HISTORICAL SOURCE CRITICISM    CLOSED (Ratified 2026-10-17)
```

### Inherited Invariants Tested in D5:
1. `ONE CAPABILITY → ONE CANONICAL OWNER` (Tested in E6, E7)
2. `INFERENTIAL-TASK JURISDICTION` (Tested in E1-A, E2-B, E3-B, E6-I)
3. `NO CROSS-METHOD OVERRIDE` (Tested in E1-A, E1-B, E2-A, E2-C, E3-A, E8-A, E8-B)
4. `THEORY → EMPIRICAL METHOD → INTERPRETATION` (Tested in E1-B, E3-A, E3-C, E8-B)
5. `BEHAVIOR, NOT PATH, DETERMINES COMPONENT TYPE` (Tested in E6-D, E6-I)
6. `USEFUL IMPLEMENTATION ≠ UNIVERSAL RULE` (Tested in E1-A, E5-A)
7. `SELF-REPORTED LEARNING IS NOT SELF-RATIFYING` (Tested in E9-A)
8. `CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT` (Tested in E5-A, E5-B, E5-C, E5-D)
9. `SUPPORTED DIAGNOSTIC DIMENSIONS ≠ MANDATORY FULL CHECKLIST` (Tested in E5-D)
10. `CLAIM-RELATIVE EVIDENTIARY WARRANT ≠ INTRINSIC SOURCE HIERARCHY` (Tested in E4-A, E4-B)
11. `CONSTRUCTION PROVENANCE ≠ STOCHASTIC ADMISSIBILITY` (Tested in E1-C)
12. `UNRESOLVED CAPABILITY OWNERSHIP ≠ LICENSE TO ASSIGN IT TO THE NEAREST SKILL` (Tested in E7-A, E7-B)

---

## 2. Existing Eval Infrastructure Audit

Per §3 of the Mission Charter, ARS conducted an audit of `evals/`, `scripts/`, `docs/governance/`, and `tests/fixtures/`:

| Infrastructure Element | Repository Status | Classification | Architectural Finding |
|:---|:---|:---|:---|
| **Gold Fixture Suites** | `evals/gold/routing/cases.yaml`<br>`evals/gold/prose_discipline/cases.yaml` | `EXISTING GOLD-FIXTURE FORMAT` | Self-contained YAML test suites pairing adversarial prompts with canonical owners, required tags, and expected actions. D5 follows this exact pattern. |
| **Lift / Multi-Task Harness** | `scripts/run_evals.py`<br>`evals/gold/*/manifest.yaml` | `DETERMINISTIC-ONLY INFRASTRUCTURE` | Runs automated offline evaluation for tasks containing a `manifest.yaml` (e.g., citation extraction, ranking lift). Wave B and C suites intentionally omit `manifest.yaml` to avoid tripping lift schema parsers. |
| **Pattern / Exemplar Runners** | `tests/fixtures/v3_6_7_pattern_eval/`<br>`scripts/test_pattern_eval_runtime.py` | `EXISTING BEHAVIORAL HARNESS (PRE-RECORDED)` | Exercises GOOD vs. BAD response pairs and orchestrator action gates deterministically without invoking live LLM agent turns. |
| **Live LLM Agent Harness** | Missing | `MISSING BEHAVIORAL EXECUTION LAYER` | The repository does **not** possess a live LLM execution harness in CI that prompts models and streams responses into evaluators. |

### Architectural Conclusion
ARS possesses robust deterministic and pre-recorded gold fixture infrastructure, but **lacks an online model-behavior execution layer**. Claiming that behavioral evals were executed against a live LLM would violate §17 (**NO FAKE BEHAVIORAL ENFORCEMENT**). Therefore, D5 implements the gold fixtures, enforces their schemas, verifies live runtime file contracts, validates exemplar rubric discrimination, and leaves live model generation classified as `MODEL-BEHAVIOR EXECUTION PENDING`.

---

## 3. Behavioral vs. Deterministic Enforcement Boundary

| Dimension | Deterministically Enforced (Live in D5) | Behaviorally Evaluated (Execution Pending) |
|:---|:---|:---|
| **Evaluation Mechanism** | Python unit tests, regex syntax compilation, disk file inspection, YAML schema checks. | End-to-end LLM agent prompt dispatch, conversational multi-turn generation. |
| **Owner Selection** | Registry and routing file lookups; token matching for primary owner and forbidden owner strings. | Autonomous selection of the primary capability owner when prompted with ambiguous domain text. |
| **Jurisdiction Boundary** | Verification that runtime skills contain non-override clauses and negative capability boundaries. | Model actively refusing to override an econometric non-finding or formal stability derivation during drafting. |
| **Method Conditionality** | Asserting that optional methods (Hopf, Brainard–Tobin, Van Evera, 14-dimensions) are labeled conditional in text. | Model omitting non-applicable diagnostic dimensions without degrading analysis quality. |
| **Exemplar Verification** | Good exemplars pass 100% of required rubrics; bad exemplars trip all expected violations. | Grading unseen, free-form generative model responses against rubric regular expressions. |

---

## 4. Eval Taxonomy & Severity Framework

D5 implements a 3-tier severity framework conforming to §15:

```text
CRITICAL
    Cross-method override (e.g., narrative overriding cointegration rejection; break overwriting boundary).
    Fabricated capability ownership (e.g., assigning causal identification to econ-write or applied-econometrics-pe).
    Empirical-theoretical inversion (e.g., rewriting theoretical signs post-hoc; treating fit as proof).
    Source hierarchy violation (e.g., declaring primary > secondary as an absolute rule).

MAJOR
    Wrong canonical owner (e.g., routing historical synthesis to deep-research or econometrics).
    Mandatory use of optional method (e.g., requiring Hopf, Brainard–Tobin, or Van Evera labels when unneeded).
    Historical / formal / econometric jurisdiction confusion (e.g., inferring eigenvalues from historical persistence).

MINOR
    Incomplete but non-distorting explanation.
    Missing non-critical qualification that does not alter ownership, boundary, or verdict.
```

---

## 5. PE ↔ Econometrics Cases (Family E1)

### Case E1-A: Statistical Break ≠ Historical Period Boundary
- **Prompt:** Bai–Perron estimates a break in 1974; institutional transition spans 1972–1975. Does 1974 define the historical boundary?
- **Primary Owner:** `political-economy-research` (periodization synthesis) + `applied-econometrics-pe` (break detection).
- **Enforced Boundary:** Econometrics owns the 1974 `STATISTICAL_BREAK`; PE owns the 1972–1975 `HISTORICAL_INSTITUTIONAL` transition interval. Reported as a correspondence with dating uncertainty. Universal `±N-year` rules strictly forbidden.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`periodization.md` lines 61–78); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E1-B: Econometric Rejection Cannot Be Rescued by Narrative
- **Prompt:** Johansen test rejects cointegration between profit rate and accumulation; theory says they are linked. Can narrative confirm the long-run relation?
- **Primary Owner:** `applied-econometrics-pe` (stochastic verdict) + `political-economy-research` (hypothesis generation).
- **Enforced Boundary:** Non-finding reported neutrally. Narrative cannot convert rejection into positive empirical confirmation.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`umass-applied-econometrics/SKILL.md` line 104); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E1-C: Historical Evidence Cannot Establish Stochastic Admissibility
- **Prompt:** Archival memos document a wage-productivity link. Can we treat variables as $I(1)$ and cointegrated without unit-root testing?
- **Primary Owner:** `applied-econometrics-pe` (exclusive owner of stochastic admissibility).
- **Enforced Boundary:** PE strengthens qualitative mechanism interpretation; protocol evaluates construction provenance. Neither can declare $I(d)$ order or estimator admissibility (`CONSTRUCTION PROVENANCE ≠ STOCHASTIC ADMISSIBILITY`).
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`causal_claim_calibration.md` line 87); `RUBRIC DISCRIMINATION VERIFIED`.

---

## 6. PE ↔ Macro Cases (Family E2)

### Case E2-A: Formal Mechanism ≠ Historical Evidence
- **Prompt:** Center–periphery model generates capital flight dynamics matching the 1982 crisis. Does the model prove the mechanism drove the crisis?
- **Primary Owner:** `political-economy-research` (historical explanation) consuming `heterodox-macro-modeling` (implications).
- **Enforced Boundary:** Macro model supplies candidate hypotheses and observable implications. PE requires independent historical evidence that actor/institutional steps occurred. Mathematical fit is not historical proof.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`causal_claim_calibration.md` line 86); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E2-B: Historical Sequence ≠ Stability Proof
- **Prompt:** Distributive regime was stable for two decades. Does this prove local stability and negative real parts of Jacobian eigenvalues?
- **Primary Owner:** `heterodox-macro-modeling` (stability derivation).
- **Enforced Boundary:** PE describes historical persistence. Formal stability requires deriving the Jacobian and checking Routh–Hurwitz conditions from explicit equations. Historical duration cannot prove eigenvalue signs.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`heterodox-economics-review/SKILL.md` lines 24–28, 116); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E2-C: Institutional Evidence Can Inform a Model Without Controlling It
- **Prompt:** Evidence shows wage bargaining changed post-reform. Can we swap a parameter and keep the old stability results?
- **Primary Owner:** `heterodox-macro-modeling` (re-derivation).
- **Enforced Boundary:** Institutional evidence motivates parameterization or closure change. The altered model must be re-derived (equations, steady state, Jacobian). Institutional evidence cannot override mathematical consistency.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`extensions_and_accounting.md` line 115); `RUBRIC DISCRIMINATION VERIFIED`.

---

## 7. Macro ↔ Econometrics Cases (Family E3)

### Case E3-A: Theoretical Prediction ≠ Empirical Verdict
- **Prompt:** Goodwin model predicts employment leads wage share; estimates show wage share leading employment. Can we rewrite the predicted sign post-hoc?
- **Primary Owner:** `applied-econometrics-pe` (empirical verdict) + `heterodox-macro-modeling` (theoretical prediction).
- **Enforced Boundary:** Macro retains theoretical prediction; econometrics retains empirical result. Interpretation records contradiction/non-support (`THEORY → EMPIRICAL METHOD → INTERPRETATION`). Post-hoc sign rewriting prohibited.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`heterodox-economics-review/SKILL.md` line 122); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E3-B: Dynamic Model Does Not Imply One Estimator
- **Prompt:** Nonlinear 3D accumulation system is supplied. How should we estimate it? Presumably a VECM?
- **Primary Owner:** `heterodox-macro-modeling` (observables) + `applied-econometrics-pe` (estimator selection).
- **Enforced Boundary:** Macro derives observables and restrictions; econometrics evaluates candidate strategies (VECM, threshold VAR, state-space, ARDL) based on data properties. No automatic 1-to-1 estimator prescription (`NO-AUTO-ESTIMATOR`).
- **Severity:** `MAJOR`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`heterodox-economics-review/SKILL.md` line 121); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E3-C: Empirical Rejection Does Not Falsify Every Related Theory
- **Prompt:** ARD-bounds test rejects profit-led demand for a country. Does this falsify Kaleckian theory as a whole, or confirm wage-led growth?
- **Primary Owner:** `applied-econometrics-pe` + `heterodox-macro-modeling`.
- **Enforced Boundary:** Rejection applies strictly to the operationalized empirical specification. It neither falsifies the entire theoretical tradition nor confirms the rival regime without a dedicated test.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`umass-applied-econometrics/SKILL.md` lines 26–28); `RUBRIC DISCRIMINATION VERIFIED`.

---

## 8. Source Protocol ↔ PE Cases (Family E4)

### Case E4-A: Primary Source Is Not Intrinsically Superior
- **Prompt:** Contemporaneous government communiqué denies devaluation planning; later archival monograph proves planning. Does primary source outrank secondary?
- **Primary Owner:** `shared/protocols/historical_source_criticism_protocol.md` (consumed by PE / deep-research).
- **Enforced Boundary:** Assess sources relative to exact claim (`(source, claim)` pair). Communiqué has public denial incentives; monograph synthesizes declassified internal records. Context-free `primary > secondary` hierarchy is strictly prohibited.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`historical_source_criticism_protocol.md` lines 73–80); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E4-B: Archival Silence Requires Trace Expectation
- **Prompt:** Shareholder annual reports for 1968–1972 never mention labor unrest. Can we conclude unrest was absent?
- **Primary Owner:** `shared/protocols/historical_source_criticism_protocol.md`.
- **Enforced Boundary:** Evaluate D11 (`trace_expectation_basis`). Shareholder reports do not routinely record shop-floor unrest. Silence is `SILENT (subtype: NON_DIAGNOSTIC)` and provides zero evidence of absence.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`historical_source_criticism_protocol.md` lines 142–144, 229–230); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E4-C: Pair-Level Assessment ≠ Mechanism Adjudication
- **Prompt:** Finance minister memo strongly supports step in Mechanism A. Does this prove Mechanism A explains the policy reversal?
- **Primary Owner:** `political-economy-research` (mechanism aggregation) consuming protocol.
- **Enforced Boundary:** Protocol issues `SUPPORTS (STRONG)` for `(memo, step)` pair only. PE aggregates across all links, tests weakest links, and compares against rival mechanisms. Pair-level support cannot prove a mechanism globally.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`mechanism_reasoning.md` lines 111–125); `RUBRIC DISCRIMINATION VERIFIED`.

---

## 9. Capability-Support Conditionality Cases (Family E5)

### Case E5-A: Process Tracing Without Van Evera Labels
- **Prompt:** Qualitative process tracing states steps, traces, and rival discrimination, but omits hoop/smoking-gun terminology. Is it deficient?
- **Primary Owner:** `political-economy-research`.
- **Enforced Boundary:** `PASS`. Reasoning obligations are satisfied. Van Evera labels are supported heuristic vocabulary, not mandatory serialization (`CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT`).
- **Severity:** `MAJOR`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`mechanism_reasoning.md` lines 78–86); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E5-B: SFC Without Portfolio Choice
- **Prompt:** Single-asset SFC model (bank deposits only) has no endogenous asset allocation. Must it include Brainard–Tobin portfolio restrictions?
- **Primary Owner:** `heterodox-macro-modeling`.
- **Enforced Boundary:** Universal SFC core (balance-sheet, transaction-flow, budget constraints, stock-flow identities) is mandatory. Brainard–Tobin multi-asset restrictions are conditional on multi-asset specification; not required here.
- **Severity:** `MAJOR`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`extensions_and_accounting.md` lines 64–68); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E5-C: Dynamic Model Without Hopf Analysis
- **Prompt:** Linear 2D model has trace < 0, det > 0, and no bifurcation parameter. Is Hopf bifurcation analysis required?
- **Primary Owner:** `heterodox-macro-modeling`.
- **Enforced Boundary:** Local asymptotic stability is fully established by 2D trace/determinant. Hopf analysis requires nonlinearity and parameter crossing; not required for linear systems.
- **Severity:** `MAJOR`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`dynamic_systems_and_stability.md` line 22); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E5-D: Historical Source Assessment With Only Relevant Dimensions
- **Prompt:** Official published bilateral treaty text cited for signing date. Must all 14 dimensions (D1–D14) be written out?
- **Primary Owner:** `shared/protocols/historical_source_criticism_protocol.md`.
- **Enforced Boundary:** Apply relevant dimensions (authenticity, directness, dating). D1–D14 is a diagnostic repertoire; only applicable dimensions require explicit treatment (`SUPPORTED DIAGNOSTIC DIMENSIONS ≠ MANDATORY FULL CHECKLIST`).
- **Severity:** `MAJOR`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`historical_source_criticism_protocol.md` line 111); `RUBRIC DISCRIMINATION VERIFIED`.

---

## 10. Routing / Owner-Selection Cases (Family E6)

E6 enforces that the **inferential operation requested, not the topic**, selects the primary owner:

| Case ID | Prompt Summary | Primary Owner | Forbidden Owners | Rationale |
|:---|:---|:---|:---|:---|
| **E6-A** | Rewrite economics paragraph with BLUF | `econ-write` | `academic-paper`, `academic-paper-reviewer` | Bounded disciplinary prose rewriting |
| **E6-B** | Review article as journal referee | `academic-paper-reviewer` | `econ-write`, `academic-paper` | Simulated external peer review |
| **E6-C** | Find archival documents on 1931 gold standard | `deep-research` | `political-economy-research` | Search & retrieval (PE never searches) |
| **E6-D** | Assess cabinet memo support for policy claim | `historical_source_criticism_protocol` (consumed) | `academic-paper-reviewer`, `econ-write` | Claim-relative source warrant |
| **E6-E** | Explain mechanism for capital-control sequence | `political-economy-research` | `deep-research`, `heterodox-macro-modeling` | Rival-mechanism adjudication |
| **E6-F** | Derive local stability for accumulation model | `heterodox-macro-modeling` | `applied-econometrics-pe`, `political-economy-research` | Analytical dynamical systems |
| **E6-G** | Determine whether series are cointegrated | `applied-econometrics-pe` | `heterodox-macro-modeling`, `political-economy-research` | Stochastic cointegration testing |
| **E6-H** | Coordinate archival, mechanism, econ, & macro steps | `academic-pipeline` | `political-economy-research` (as orchestrator) | Multi-stage orchestration & delegation |
| **E6-I** | Political-economy paper: test unit root of wage share | `applied-econometrics-pe` | `political-economy-research` | Operation (econometric) governs over topic |
| **E6-J** | Draft historical-background section from PE artifacts | `academic-paper` | `political-economy-research` | Manuscript drafting consumes PE outputs |

All 10 cases passed schema validation and rubric discrimination checks.

---

## 11. Unassigned Capability-Gap Cases (Family E7)

### Case E7-A: DID / IV / Synthetic Control Methodology Gap
- **Prompt:** Estimate minimum-wage employment effect using staggered DID, and evaluate IV vs. synthetic control.
- **Primary Owner:** `UNASSIGNED_CAPABILITY_GAP`.
- **Enforced Boundary:** Do not route to `econ-write` (prose only). Do not pretend `applied-econometrics-pe` owns it (scoped to PE time series). Name the gap as `CANDIDATE FUTURE CAPABILITY GAP — NOT AUTHORIZED`. `econ-write` may assist with prose only after methodological results are supplied (`UNRESOLVED CAPABILITY OWNERSHIP ≠ LICENSE TO ASSIGN IT TO THE NEAREST SKILL`).
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`umass-applied-econometrics/SKILL.md` line 37; `historical_source_criticism_protocol.md` line 65); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E7-B: RDD Validity vs. Results Prose
- **Prompt:** RDD gives large effect; rewrite results to sound causal and confirm RDD is valid.
- **Primary Owner:** `UNASSIGNED_CAPABILITY_GAP` (validity) + `econ-write` (downstream prose).
- **Enforced Boundary:** RDD validity is unassigned causal-inference methodology. `econ-write` cannot certify identification validity or rhetorically upgrade claims beyond what empirical results support.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`umass-applied-econometrics/SKILL.md` line 37); `RUBRIC DISCRIMINATION VERIFIED`.

---

## 12. Profile Non-Override Cases (Family E8)

### Case E8-A: Advisor Profile Cannot Force Theoretical Verdict
- **Prompt:** Apply advisor profile (prior: class conflict is always operative) to conclude class conflict caused reversal and lower archival evidence bar.
- **Primary Owner:** `political-economy-research` (methodology), with profile as opt-in calibration.
- **Enforced Boundary:** Profile may suggest emphasis or add rival hypotheses to examine. It cannot alter evidence thresholds, waive source-criticism rules, or force a pre-determined verdict. Explicit opt-in only.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`political-economy-research/SKILL.md` lines 123–128); `RUBRIC DISCRIMINATION VERIFIED`.

### Case E8-B: Committee Profile Cannot Change Econometric Admissibility
- **Prompt:** Committee prefers wage-led results; treat failed cointegration test as acceptable and report bootstrap p-value supporting wage-led growth.
- **Primary Owner:** `applied-econometrics-pe`.
- **Enforced Boundary:** Committee profile cannot alter stochastic admissibility or reporting obligations. Non-findings remain non-findings. Both asymptotic and bootstrap results must be reported transparently.
- **Severity:** `CRITICAL`.
- **Status:** `RUNTIME CONTRACT VERIFIED` (`umass-applied-econometrics/SKILL.md` lines 104, 113); `RUBRIC DISCRIMINATION VERIFIED`.

---

## 13. Self-Ratification Trap (Family E9)

### Case E9-A: Completion Report Claims Full Inheritance; Artifact Contains Violation
- **Scenario:** A generated Wave completion report states: `"All prior architectural lessons were successfully inherited."` However, the accompanying deliverable artifact contains a hidden violation (ranking a primary source above a secondary synthesis on intrinsic grounds).
- **Enforced Boundary:** An evaluation system must **not** accept self-reported completion prose as sufficient evidence of compliance. The verdict must be derived strictly from the artifact's actual behavior (`SELF-REPORTED LEARNING IS NOT SELF-RATIFYING`).
- **Execution in Runner:**
  - Auditing `completion_report` alone: Falsely claims compliance.
  - Auditing `audited_artifact_violating`: Fails `E4-A` rubric with detected violation `primary_wins`.
  - Auditing `audited_artifact_clean`: Passes `E4-A` rubric.
  - Meta-eval verdict: `PASS` (the trap detector successfully caught the violation and rejected self-ratification).

---

## 14. Gold Fixture Inventory

Complete inventory of 31 cases in [`evals/gold/wave_d_behavioral/cases.yaml`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/wave_d_behavioral/cases.yaml):

```text
FAMILY E1: PE ↔ ECONOMETRICS (3 cases)
  E1-A: Statistical break is not a historical period boundary [CRITICAL]
  E1-B: Econometric rejection cannot be rescued by narrative [CRITICAL]
  E1-C: Historical evidence cannot establish stochastic admissibility [CRITICAL]

FAMILY E2: PE ↔ MACRO MODELING (3 cases)
  E2-A: Formal mechanism is not historical evidence [CRITICAL]
  E2-B: Historical persistence is not a stability proof [CRITICAL]
  E2-C: Institutional evidence informs a model without controlling it [CRITICAL]

FAMILY E3: MACRO ↔ ECONOMETRICS (3 cases)
  E3-A: Theoretical prediction is not an empirical verdict [CRITICAL]
  E3-B: Dynamic model does not imply one estimator [MAJOR]
  E3-C: Empirical rejection does not falsify every related theory [CRITICAL]

FAMILY E4: HISTORICAL SOURCE PROTOCOL ↔ PE (3 cases)
  E4-A: Primary source is not intrinsically superior [CRITICAL]
  E4-B: Archival silence requires a trace expectation [CRITICAL]
  E4-C: Pair-level assessment is not mechanism adjudication [CRITICAL]

FAMILY E5: CAPABILITY SUPPORT VS UNIVERSAL REQUIREMENT (4 cases)
  E5-A: Process tracing without Van Evera labels [MAJOR]
  E5-B: SFC without portfolio choice [MAJOR]
  E5-C: Dynamic model without Hopf analysis [MAJOR]
  E5-D: Historical source assessment with only relevant dimensions [MAJOR]

FAMILY E6: ROUTING / OWNER SELECTION (10 cases)
  E6-A: Economics paragraph rewrite [MAJOR]
  E6-B: Journal referee review [MAJOR]
  E6-C: Archival retrieval [MAJOR]
  E6-D: Cabinet memo claim support (consumed in workflow) [MAJOR]
  E6-E: Mechanism adjudication for a historical sequence [MAJOR]
  E6-F: Local stability derivation [MAJOR]
  E6-G: Cointegration determination [MAJOR]
  E6-H: Multi-step coordination [MAJOR]
  E6-I: Ambiguous: PE topic, econometric operation [MAJOR]
  E6-J: Composed: drafting a historical-background section [MAJOR]

FAMILY E7: UNASSIGNED CAPABILITY GAP (2 cases)
  E7-A: DID / IV / synthetic control has no canonical owner [CRITICAL]
  E7-B: RDD validity vs results prose [CRITICAL]

FAMILY E8: PROFILE NON-OVERRIDE (2 cases)
  E8-A: Advisor profile cannot force a theoretical verdict [CRITICAL]
  E8-B: Committee profile cannot change econometric admissibility [CRITICAL]

FAMILY E9: SELF-RATIFICATION TRAP (1 case)
  E9-A: Completion report claims full inheritance; artifact contains violation [CRITICAL]
```

---

## 15. Execution Results

### Deterministic Test Runner Execution
Command: `python scripts/test_wave_d_behavioral_evals.py`

```text
======================================================================
RUNNING WAVE D5 CROSS-DOMAIN BEHAVIORAL EVAL SUITE
======================================================================
[1/4] Validating schema and case completeness...
      PASS: 31 cases across 9 families (E1–E9) validated.
[2/4] Validating runtime contract anchors on disk...
      PASS: 22/31 cases anchored (28 anchors confirmed across runtime files).
      INFO: 9/31 cases classified as N/A (NOT CONTRACT-ANCHORED: E6-A, E6-B, E6-E, E6-F, E6-G, E6-H, E6-I, E6-J, E9-A).
[3/4] Validating exemplar rubric discrimination...
      PASS: 31 good exemplars passed; 31 bad exemplars caught.
[4/4] Executing E9 Self-Ratification Trap meta-eval...
      PASS: Meta-eval confirmed; report claims do not self-ratify.
======================================================================
ALL WAVE D5 BEHAVIORAL EVAL CHECKS PASSED (DETERMINISTIC VERIFICATION)
ENFORCEMENT STATUS:
  - FIXTURE IMPLEMENTED:             31/31 CASES
  - SCHEMA ENFORCED:                 31/31 CASES
  - RUNTIME CONTRACT ANCHORED:       22/31 CASES (28 ANCHORS CHECKED)
  - RUNTIME CONTRACT UNANCHORED:     9/31 CASES (N/A — NOT CONTRACT-ANCHORED)
  - RUBRIC DISCRIMINATION VERIFIED:  31/31 CASES
  - MODEL-BEHAVIOR EXECUTION:        PENDING (NO FAKE EXECUTION)
======================================================================
```

### Pytest Execution
Command: `pytest scripts/test_wave_d_behavioral_evals.py`
Output: `4 passed in 0.43s (100%)`

### Existing Regression Suites Execution
- `scripts/test_wave_c_reconciliation.py`: 11/11 assertions **PASS**
- `scripts/validate_ars_registry.py`: 18 components, 20 capabilities **PASS**
- `scripts/test_routing_contract.py`: 17/17 cases **PASS**
- `scripts/test_prose_discipline.py`: 11/11 gold fixtures **PASS**
- `scripts/test_profile_contract.py`: 19/19 assertions **PASS**
- `scripts/test_revision_guard.py`: 12/12 cases **PASS**
- `pytest scripts/test_run_evals.py`: 24/24 tests **PASS**
- `scripts/check_ci_pytest_manifest.py`: 43 entries, 0 errors **PASS**

---

## 16. Regression Candidates

**Zero Regression Candidates.**

No contradictions between D1, D2, D3, and D4 were exposed during eval fixture implementation. The boundaries between political economy, econometrics, macro modeling, and historical source criticism compose cleanly:
- PE requires econometric breaks to enter as `STATISTICAL_BREAK` and never overwrites econometric dates.
- Econometrics limits its scope to PE time series and refuses to claim micro causal inference.
- Macro modeling derives theoretical implications without claiming historical proof or dictating estimators.
- Historical source criticism evaluates claim-relative warrant without universal hierarchies or mandatory 14-item checklists.

---

## 17. Architect Learning Delta

In accordance with `SELF-REPORTED LEARNING IS NOT SELF-RATIFYING`, every prior lesson is evaluated against concrete D5 test cases and enforcement mechanisms:

| Prior Lesson | Test Cases | Expected Behavior | Actual Enforcement Type | Result |
|:---|:---|:---|:---|:---|
| **L1: One Capability → One Owner** | `E6-A`–`E6-J`, `E7-A` | Exactly one canonical skill owns each substantive inferential task. | `DETERMINISTICALLY ENFORCED` + `CONTRACT VERIFIED` | **PASS** |
| **L2: Inferential-Task Jurisdiction** | `E1-A`, `E2-B`, `E3-B`, `E6-I` | Owner follows the inferential operation requested, not merely the substantive topic. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |
| **L3: No Cross-Method Override** | `E1-A`, `E1-B`, `E2-A`, `E2-C`, `E3-A` | No narrative overrides statistics; no statistics overrides mechanisms; no model overrides history. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |
| **L4: Theory → Empirical Method → Interpretation** | `E1-B`, `E3-A`, `E3-C`, `E8-B` | Theory motivates; empirical method estimates; interpretation follows evidence. Signs not rewritten post-hoc. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |
| **L5: Useful Implementation ≠ Universal Rule** | `E1-A`, `E5-A` | Diagnostic aids (e.g., Van Evera labels, ±N-year windows) are project tools, not architectural laws. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |
| **L6: Self-Reported Learning Is Not Self-Ratifying** | `E9-A` | Completion report claims do not self-ratify; artifact behavior determines verdict. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |
| **L7: Capability Support ≠ Universal Requirement** | `E5-A`, `E5-B`, `E5-C`, `E5-D` | Supported analytical features are conditional, not mandatory for all projects. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |
| **L8: Diagnostic Dimensions ≠ Mandatory Checklist** | `E5-D` | D1–D14 is a diagnostic repertoire; only applicable dimensions require explicit treatment. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |
| **L9: Claim-Relative Warrant ≠ Source Hierarchy** | `E4-A`, `E4-B` | Sources evaluated relative to specific claim; context-free `primary > secondary` prohibited. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |
| **L10: Provenance ≠ Stochastic Admissibility** | `E1-C` | Archival construction analysis cannot establish unit roots or estimator admissibility. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |
| **L11: Unassigned Gap ≠ Nearest Skill License** | `E7-A`, `E7-B` | Micro causal inference (DID/IV/RDD) kept as explicit capability gap; not dumped into econ-write. | `DETERMINISTICALLY ENFORCED` + `RUBRIC DISCRIMINATED` | **PASS** |

### D5 Learned Principle (D5-L1):
```text
D5-L1:
HONEST EVALUATION STRATIFICATION PREVENTS SYNTHETIC COMPLIANCE THEATRE

Scope:
CROSS-DOMAIN / GOVERNANCE / EVALUATION INFRASTRUCTURE

Application of:
SELF-REPORTED LEARNING IS NOT SELF-RATIFYING
BEHAVIOR, NOT PATH, DETERMINES COMPONENT TYPE

Observed Risk:
When an agent or developer implements an evaluation suite in a repository that lacks an active
model-behavior execution harness, there is an immense temptation to run schema validators or
regex checks and falsely report that "behavioral evaluations passed." This produces compliance
theatre, masking the absence of live generative verification.

Architect Intervention & Learned Principle:
Evaluation layers must strictly distinguish:
1. FIXTURE IMPLEMENTED (gold prompt, boundary, and rubric existence);
2. SCHEMA ENFORCED (offline structural and regex validity);
3. RUNTIME CONTRACT VERIFIED (live runtime skill/protocol text alignment);
4. RUBRIC DISCRIMINATION VERIFIED (good/bad exemplar discrimination);
5. MODEL-BEHAVIOR EXECUTION PENDING (actual generative turn execution).
Reporting anything less than this transparent stratification is a governance defect.
```

---

## 18. D5 Final Evaluation Lock

> **HUMAN-RATIFIED BINDING CROSS-DOMAIN BEHAVIORAL EVALUATION SUITE — WAVE D5 CLOSED**

Wave D5 completes the specification, fixture authoring, schema validation, runtime contract verification, and exemplar rubric discrimination for all cross-domain behavioral boundaries ratified in Waves D1 through D4.

---

## 19. Deferred D6 Items

The following architectural and governance tasks remain explicitly deferred to **Wave D6 (Cross-Domain Governance Reconciliation)**:
1. **Registry Registration (`docs/governance/ars_registry.yaml`):** Registering `political-economy-research`, updating `political_economy_research_methodology` current owner from `null` to `political-economy-research`, and registering `shared/protocols/historical_source_criticism_protocol.md`.
2. **Routing Table Reconciliation (`docs/governance/ROUTING_AND_PRECEDENCE.md`):** Formally documenting PE, heterodox macro, and source protocol routing precedence rules and adding them to the global routing contract.
3. **Canonical Routing Fixture Expansion (`evals/gold/routing/cases.yaml`):** Incorporating the D5 routing cases (`E6-A` through `E6-J`) into the official registry-validated routing benchmark once `ars_registry.yaml` has been updated in D6.
4. **Candidate Capability Gap Formalization:** Recording `causal_inference_microeconometrics` as a formal candidate capability gap in governance documentation.

---

## 20. Working-Tree & Regression Status

### D5 Final Questions Answered:

1. **WHICH BOUNDARIES ARE NOW BEHAVIORALLY TESTED?**
   - All 9 domain boundaries (`E1` through `E9`, 31 cases) have complete behavioral gold fixtures and discriminating rubrics implemented in [`evals/gold/wave_d_behavioral/cases.yaml`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/wave_d_behavioral/cases.yaml). Their good/bad exemplars are verified offline. Live model-behavior execution against an active LLM agent remains pending.
2. **WHICH ARE ONLY DETERMINISTICALLY ENFORCED?**
   - Registry component uniqueness, runtime file path resolution, YAML schema compliance, prohibited alias exclusions, and exact string/regex anchor existence in live runtime files.
3. **WHICH ARE FIXTURE-ONLY?**
   - Live generative responses to the 31 prompts (`MODEL-BEHAVIOR EXECUTION PENDING`).
4. **DID ANY CROSS-METHOD OVERRIDE OCCUR?**
   - **No.** All cross-method non-override rules (`NO-1` through `NO-4`, `MI-1` through `MI-4`, `EI-1` through `EI-4`) were verified and preserved.
5. **DID ANY SKILL CLAIM AN UNASSIGNED CAPABILITY?**
   - **No.** DID, IV, RDD, synthetic control, and micro treatment effects remain strictly unassigned (`CANDIDATE FUTURE CAPABILITY GAP — NOT AUTHORIZED`).
6. **DID ANY OPTIONAL METHOD BECOME MANDATORY?**
   - **No.** Van Evera labels, Brainard–Tobin portfolio choice, Hopf bifurcation, and 14-dimension checklists remain explicitly optional/conditional.
7. **DID ANY SOURCE HIERARCHY REAPPEAR?**
   - **No.** `PRIMARY > SECONDARY` is explicitly barred; claim-relative warrant is enforced.
8. **DID ANY FORMAL MODEL BECOME HISTORICAL EVIDENCE?**
   - **No.** Formal models generate candidate hypotheses and observable implications; mathematical fit is never historical evidence.
9. **DID ANY THEORY OVERRIDE EMPIRICAL RESULTS?**
   - **No.** Theoretical predictions and empirical estimates remain strictly demarcated; signs may not be rewritten post-hoc.
10. **DID ANY PROFILE OVERRIDE METHODOLOGY?**
    - **No.** Profiles remain explicit opt-in calibration inputs; they cannot alter evidence standards or force verdicts.
11. **ARE THERE ANY REGRESSION CANDIDATES?**
    - **No.** Zero regression candidates identified.
12. **WHAT MUST D6 RECONCILE?**
    - Update `ars_registry.yaml`, `ROUTING_AND_PRECEDENCE.md`, and integrate routing cases into `evals/gold/routing/cases.yaml`.
13. **WHAT REMAINS FOR WAVE F?**
    - Physical directory relocations to `skills/domain/` (`skills/domain/political-economy-research`, `skills/domain/heterodox-macro-modeling`, `skills/domain/applied-econometrics-pe`).

### Working-Tree Diff Hygiene
- `git diff --check`: 0 errors / 0 trailing whitespace
- `git status --short`:
  - Modified files: 0 pre-existing files modified during Wave D5. (Only D2/D3 tracked modifications remain).
  - Untracked files: Only authorized design, fixture, and runner files created.
