# WAVE D6 — GOVERNANCE RECONCILIATION REPORT

**Date:** 2026-10-19
**Status:** IMPLEMENTED — AWAITING HUMAN REVIEW (Diego Polanco)
**Governing Baseline Checkpoint:** `aa5283ecd4cf49c377a3a96ba8d57c3c0257ab65`
**Repository:** `C:\ReposGitHub\academic-research-skills`
**Working Branch:** `main`
**Commit / Push Authorization:** None. Strict no-commit / no-push discipline enforced.

> [!NOTE]
> **Post-Implementation Closure Note (2026-10-19):**
> Following validation of this report and completion of dynamic regression checks, human architect Diego Polanco authorized the local commit and normal push of the D6 governance reconciliation at checkpoint `27fbfd60255fe6c3cd99e7298c43a5189869163b` (`Reconcile Wave D6 governance and verify capability boundaries`).
> Wave D is now explicitly **HUMAN-CLOSED**. See the formal [Wave D Human Closure Record](WAVE_D_HUMAN_CLOSURE_2026-10-19.md) and the governing [Restart Handoff](ARS_SESSION_HANDOFF_POST_WAVE_D_2026-10-19.md).
> The historical metadata and "NO COMMIT / NO PUSH" footer below describe the pre-publication review state prior to the authorized commit and push.

---

## 1. Plain-Language Before/After Table of Research Responsibilities

Wave D6 reconciles the repository's governance foundation (`docs/governance/ars_registry.yaml`, `docs/governance/ROUTING_AND_PRECEDENCE.md`, and canonical routing tests) with the domain capabilities developed and accepted across Waves D1 through D5.1.

The table below summarizes the exact intellectual division of labour across all substantive research domains:

| Substantive Research Domain / Task | Pre-D6 Baseline State | Post-D6 Reconciled Governance State | Canonical Owner & Runtime Path | Governing Architectural Principle |
|:---|:---|:---|:---|:---|
| **Comparative-Historical Political Economy** | Capability listed as `CANDIDATE` with `current_owner: null`. Component unregistered. | Canonically registered as active `DOMAIN_SKILL`. Sole owner of comparative research designs, periodization, qualitative mechanism reasoning, and institutional analysis. | `political-economy-research`<br>(`political-economy-research/`) | `ONE CAPABILITY → ONE CANONICAL OWNER`<br>`INFERENTIAL-TASK JURISDICTION` |
| **Applied Time-Series Econometrics** | Notes in registry referenced obsolete forced regime-switching rule H.4 and embedded tool extraction. Scope ambiguous. | Canonically registered as active `DOMAIN_SKILL` bounded strictly to implemented PE time-series methods (ADF/KPSS integration order, Toda-Yamamoto lag selection, cointegration rank audits, linear VAR/VECM). Does not claim micro causal inference. | `umass-applied-econometrics`<br>(`umass-applied-econometrics/`) | `NO CROSS-METHOD OVERRIDE`<br>`CONSTRUCTION PROVENANCE ≠ STOCHASTIC ADMISSIBILITY` |
| **Heterodox Macroeconomic Modeling** | Notes in registry described a narrow 29-line check for Sraffian Supermultiplier singularities. | Canonically registered as active `DOMAIN_SKILL` owning formal growth and distribution modeling (Goodwin baseline, 2D Jacobian local stability, phase diagrams, and SFC accounting closures). Derives testable restrictions; does not select empirical estimators. | `heterodox-economics-review`<br>(`heterodox-economics-review/`) | `THEORETICAL MODEL ≠ AUTOMATIC ESTIMATOR`<br>`THEORY → EMPIRICAL METHOD → INTERPRETATION` |
| **Historical Source Criticism Standard** | Unregistered in governance registry. Status ambiguous between skill and protocol. | Canonically registered as active `SHARED_PROTOCOL` (`shared/protocols/historical_source_criticism_protocol.md`). Governs claim-relative warrant assessment (14 diagnostic dimensions, 4 canonical verdicts: SUPPORTS, UNDERMINES, SILENT, INDETERMINATE; no universal hierarchy; no causal inference leak). Consumed conditionally within requesting workflows. | `historical-source-criticism`<br>(`shared/protocols/historical_source_criticism_protocol.md`) | `BEHAVIOR, NOT PATH, DETERMINES COMPONENT TYPE`<br>`CAPABILITY SUPPORT ≠ UNIVERSAL APPLICATION REQUIREMENT` |
| **Micro-econometric Causal Inference (DID / IV / RDD / Synthetic Control)** | Unrepresented in registry capabilities; causal-method ownership leak to `econ-write` previously removed in D4.1. | Explicitly codified as unassigned capability gap `causal_inference_microeconometrics` (`migration_status: CANDIDATE`, `current_owner: null`). Acknowledged absence; forbidden from routing to `econ-write` or `umass-applied-econometrics`. | `UNASSIGNED_CAPABILITY_GAP`<br>(`NO CURRENT CANONICAL OWNER`) | `UNRESOLVED CAPABILITY OWNERSHIP ≠ LICENSE TO ASSIGN TO NEAREST SKILL` |
| **Systematic Literature Discovery & Archival Retrieval** | Owned by `deep-research`. Boundary with PE search uncodified. | Explicitly reaffirmed: `deep-research` owns external search and archival retrieval. `political-economy-research` analyzes sources provided to it; PE never searches or fabricates sources. | `deep-research`<br>(`deep-research/`) | `INFERENTIAL-TASK JURISDICTION` |
| **Manuscript Section Drafting & Composition** | Owned by `academic-paper` consuming `econ-write` for economics disciplinary style. | Reaffirmed and bounded: Political-economy methodology, econometrics, and macro modeling supply analytical outputs and claim ceilings. `econ-write` owns bounded economics drafting and disciplinary writing standards, while `academic-paper` owns the generic manuscript lifecycle and consumes economics writing standards. | `academic-paper`<br>(`academic-paper/`) | `ORCHESTRATION IS NOT OWNERSHIP` |
| **Multi-Step Cross-Domain Research Orchestration** | Owned by `academic-pipeline`. | Reaffirmed: compound multi-step workflows sequence through `academic-pipeline`. The orchestrator delegates each substantive inferential step to its respective canonical owner and claims no substantive methodology. | `academic-pipeline`<br>(`academic-pipeline/`) | `ORCHESTRATION IS NOT OWNERSHIP` |

---

## 2. Exact Changed Files and Architectural Rationale

Wave D6 modifications were strictly confined to the authorized governance and routing surfaces:

```text
docs/governance/ars_registry.yaml
docs/governance/ROUTING_AND_PRECEDENCE.md
evals/gold/routing/cases.yaml
scripts/test_routing_contract.py
scripts/validate_ars_registry.py
docs/design/wave-d/D6_GOVERNANCE_RECONCILIATION.md
```

### Detailed File Changes:

1. [`docs/governance/ars_registry.yaml`](../../governance/ars_registry.yaml)
   - **Version:** Bumped to `1.2.0` (Last Updated: `2026-10-19`).
   - **Component Registration (`components:`):**
     - Registered `political-economy-research` (`runtime_path: political-economy-research`, `semantic_role: DOMAIN_SKILL`, `lifecycle_status: ACTIVE`).
     - Registered `historical-source-criticism` (`runtime_path: shared/protocols/historical_source_criticism_protocol.md`, `semantic_role: SHARED_PROTOCOL`, `lifecycle_status: ACTIVE`).
     - Updated `umass-applied-econometrics` notes to reflect Wave D2 refactor (elimination of forced regime-switching rule H.4, modular tool references, strict time-series bounding).
     - Updated `heterodox-economics-review` notes to reflect Wave D3 expansion (Goodwin baseline, Jacobian stability, SFC closures).
     - *Total components validated:* Increased from 18 to 20.
   - **Capability Registration (`capabilities:`):**
     - Updated `political_economy_research_methodology`: `migration_status: CURRENT`, `current_owner: political-economy-research`, `current_owner_type: DOMAIN_SKILL`.
     - Registered `claim_relative_source_criticism`: `migration_status: CURRENT`, `current_owner: historical-source-criticism`, `current_owner_type: SHARED_PROTOCOL`.
     - Registered `causal_inference_microeconometrics`: `migration_status: CANDIDATE`, `current_owner: null`, `notes: NO CURRENT CANONICAL OWNER`.
     - Updated `applied_econometrics_political_economy`: `migration_status: CURRENT`, updated description and notes.
     - Updated `heterodox_macro_modeling`: `migration_status: CURRENT`, updated description and notes.
     - Updated `cointegration_specification_audit` and `toda_yamamoto_specification_mapping`: updated notes decoupling empirical admissibility from theoretical mechanism plausibility.
     - *Total capabilities validated:* Increased from 20 to 22.

2. [`docs/governance/ROUTING_AND_PRECEDENCE.md`](../../governance/ROUTING_AND_PRECEDENCE.md)
   - **Version:** Bumped to `1.2.0` (Baseline Parent: `aa5283e`).
   - **Ownership Principles:** Added Principles 9 through 12 codifying inferential-task jurisdiction, `THEORY → EMPIRICAL METHOD → INTERPRETATION`, protocol standard vs. workflow owner distinction, and unassigned causal inference gap preservation.
   - **Routing Decision Tree:** Added explicit routing branches for political-economy research, heterodox macro modeling, applied time-series econometrics, historical source assessment via shared protocol, archival retrieval, and unassigned causal inference gap.
   - **Core Precedence Rules:** Added Rules R12 (`political-economy-research`), R13 (`heterodox-economics-review`), R14 (`umass-applied-econometrics`), R15 (`historical-source-criticism`), and R16 (`UNASSIGNED_CAPABILITY_GAP`).
   - **Adversarial Rules:** Added Section 4 detailing Rules ADV-D1 through ADV-D6.
   - **Runtime Warning:** Added `political-economy-research`, `umass-applied-econometrics`, and `heterodox-economics-review` to the mandatory live runtime path allowlist.

3. [`evals/gold/routing/cases.yaml`](../../../evals/gold/routing/cases.yaml)
   - **Version:** Bumped to `1.2.0` (Schema: `ars-routing-eval-v1.2`).
   - **Cases:** Added Part 3 containing 9 new canonical evaluation fixtures (`ROUTE-018` through `ROUTE-026`) mapping all D5 E6 and E7 behavioral scenarios into the canonical routing benchmark. Total cases increased from 17 to 26 (12 positive, 14 adversarial).

4. [`scripts/test_routing_contract.py`](../../../scripts/test_routing_contract.py)
   - **D5 Conceptual Name Mapping:** Added `D5_CONCEPTUAL_TO_REGISTERED` dictionary mapping `applied-econometrics-pe` → `umass-applied-econometrics`, `heterodox-macro-modeling` → `heterodox-economics-review`, and `historical_source_criticism_protocol` → `historical-source-criticism`. Added programmatic check ensuring all conceptual names resolve to active registered components without creating duplicate components.
   - **Unassigned Capability Gap Handling:** Supported `primary_owner: UNASSIGNED_CAPABILITY_GAP`, asserting that it does not exist as a registered component and verifying that the underlying capability has `current_owner: null`.
   - **Shared Protocol Typing Enforcement:** Enforced that components with `semantic_role: SHARED_PROTOCOL` cannot be selected as primary executable owners, preventing protocol-as-skill errors.
   - **Governing Protocol Verification:** Added `governing_protocol` check ensuring requesting workflows consume valid `SHARED_PROTOCOL` components.
   - **Rule Verification:** Implemented rule-specific checks for R12, R13, R14, and ADV-D1 through ADV-D6.

5. [`scripts/validate_ars_registry.py`](../../../scripts/validate_ars_registry.py)
   - Added Section 4 enforcing Wave D6 Invariants D6-1 through D6-5 (active political economy skill, active historical source protocol, active applied econometrics, active heterodox macro modeling, and unassigned causal inference gap preservation).

---

## 3. Mapping from D5 E6/E7 Cases to Canonical Routing Tests

Every behavioral evaluation scenario in D5 Family E6 (Routing & Owner Selection) and Family E7 (Unassigned Capability Gap) maps directly to a permanent canonical routing test fixture:

| D5 Case ID | Canonical Routing ID | Rule ID | Prompt Excerpt | Primary Owner | Excluded Owners (`must_not_primary_owner`) | Architectural Enforcement Point |
|:---|:---|:---|:---|:---|:---|:---|
| **E6-A** | `ROUTE-002`<br>`ROUTE-013` | `R2`<br>`ADV-A4` | `"Rewrite this economics paragraph so it leads with the result."` | `econ-write` | `academic-paper`, `academic-pipeline` | Bounded economics section drafting belongs directly to domain skill `econ-write`. |
| **E6-B** | `ROUTE-004`<br>`ROUTE-015` | `R4`<br>`ADV-A6` | `"Review this article as a journal referee and give a recommendation."` | `academic-paper-reviewer` | `academic-paper`, `econ-write` | Journal referee reports and simulated external peer review belong solely to `academic-paper-reviewer`. |
| **E6-C** | `ROUTE-021` | `ADV-D1` | `"Find archival documents about the 1931 suspension of the gold standard."` | `deep-research` | `political-economy-research`, `historical-source-criticism` | Source search and retrieval belong to `deep-research`; `political-economy-research` analyzes sources and never searches. |
| **E6-D** | `ROUTE-022` | `ADV-D2` | `"Assess whether this cabinet memo supports the claim that policy X was considered."` | `political-economy-research`<br>*(requesting workflow)* | `academic-paper-reviewer`, `umass-applied-econometrics`, `historical-source-criticism` | Claim-relative documentary assessment is governed by shared protocol (`historical-source-criticism`) and executed in requesting workflow; protocol is not an autonomous skill. |
| **E6-E** | `ROUTE-018` | `R12` | `"Explain which mechanism best explains this historical sequence of capital-control abandonment."` | `political-economy-research` | `deep-research`, `heterodox-economics-review` | Comparative-historical mechanism adjudication and institutional explanation belong to `political-economy-research`. |
| **E6-F** | `ROUTE-019` | `R13` | `"Derive local stability conditions for this accumulation model."` | `heterodox-economics-review` | `umass-applied-econometrics`, `political-economy-research` | Formal mathematical modeling, Jacobian derivation, and stability conditions belong to `heterodox-economics-review`. |
| **E6-G** | `ROUTE-020` | `R14` | `"Determine whether these variables are cointegrated."` | `umass-applied-econometrics` | `heterodox-economics-review`, `political-economy-research` | Stochastic admissibility, integration order testing, and cointegration testing belong to `umass-applied-econometrics`. |
| **E6-H** | `ROUTE-023` | `ADV-D3` | `"Coordinate all of these steps — archival retrieval, mechanism adjudication, cointegration tests, and a stability derivation — into one research workflow."` | `academic-pipeline` | `political-economy-research`, `umass-applied-econometrics` | Multi-step research orchestration belongs to `academic-pipeline`; orchestrator sequences and delegates, owning no substantive method. |
| **E6-I** | `ROUTE-024` | `ADV-D4` | `"This is a political-economy paper on the wage share. Please test whether the wage share has a unit root."` | `umass-applied-econometrics` | `political-economy-research` | Inferential operation, not topical framing, selects the owner; unit root testing is an econometric operation owned by `umass-applied-econometrics`. |
| **E6-J** | `ROUTE-025` | `ADV-D5` | `"Our model predicts a profit squeeze and the archives describe a strike wave in the late 1960s. Write the historical-background section of the paper."` | `academic-paper`<br>*(consuming `econ-write`)* | `political-economy-research`, `heterodox-economics-review` | Manuscript lifecycle belongs to `academic-paper` consuming `econ-write`; political economy, econometrics, and macro modeling supply analytical outputs and claim ceilings but do not draft manuscript sections. |
| **E7-A** | `ROUTE-026` | `ADV-D6` | `"Estimate the employment effect of the 2015 minimum-wage reform using a difference-in-differences design with staggered adoption, and tell me whether IV or synthetic control would be better."` | `UNASSIGNED_CAPABILITY_GAP` | All 20 registered components (dynamically enumerated and verified from registry) | Causal inference methodologies (DID/IV/RDD/synthetic controls) have no implemented canonical owner in ARS; requests must reject assignment to any existing component and report the capability gap. |

---

## 4. Multi-Layer Validation Outcomes & Limitations

All validation suites across the standing regression baseline passed cleanly:

| Test Suite / Script | Verification Target | Status | Exit Code | Metrics / Assertions |
|:---|:---|:---:|:---:|:---|
| [`scripts/validate_ars_registry.py`](../../../scripts/validate_ars_registry.py) | Schema validity, component/capability uniqueness, Wave B1/C5/D6 invariants | **PASS** | `0` | 20 components, 22 capabilities validated; Invariants D6-1 to D6-5 confirmed |
| [`scripts/test_routing_contract.py`](../../../scripts/test_routing_contract.py) | Canonical routing precedence contract & D5 conceptual resolution | **PASS** | `0` | 26/26 cases passed (12 positive, 14 adversarial); conceptual mappings verified |
| [`scripts/test_wave_c_reconciliation.py`](../../../scripts/test_wave_c_reconciliation.py) | Wave C legacy stubs, profile routing, review ownership, Wave F deferral | **PASS** | `0` | 11/11 assertions passed |
| [`scripts/test_prose_discipline.py`](../../../scripts/test_prose_discipline.py) | Shared prose protocol, non-inference AI guard, gold fixtures | **PASS** | `0` | 11/11 fixtures passed; deterministic JSON output verified |
| [`scripts/test_profile_contract.py`](../../../scripts/test_profile_contract.py) | Scholar profiles, advisor/committee wrappers, templates | **PASS** | `0` | 19/19 assertions passed |
| [`scripts/test_revision_guard.py`](../../../scripts/test_revision_guard.py) | Change-control engine, deterministic sidecar validation | **PASS** | `0` | 12/12 cases passed |
| `pytest scripts/test_run_evals.py` | ARS core citation & lift evaluation harness | **PASS** | `0` | 24/24 passed in 0.58s |
| [`scripts/check_ci_pytest_manifest.py`](../../../scripts/check_ci_pytest_manifest.py) | CI pytest manifest drift guard | **PASS** | `0` | 43 entries verified clean |
| [`scripts/test_editorial_governance_schema.py`](../../../scripts/test_editorial_governance_schema.py) | Sidecar and Material Passport JSON draft schemas | **PASS** | `0` | 10/10 assertions passed |
| [`scripts/test_wave_d_behavioral_evals.py`](../../../scripts/test_wave_d_behavioral_evals.py) (CLI) | Frozen D5 cross-domain behavioral fixtures & anchors | **PASS** | `0` | 31/31 cases validated; 22 anchored (28 anchors), 9 unanchored N/A; rubric discrimination clean |
| [`scripts/test_wave_d_behavioral_evals.py`](../../../scripts/test_wave_d_behavioral_evals.py) (pytest) | Frozen D5 pytest test suite | **PASS** | `0` | 4/4 passed in 0.40s |
| `git diff --check` | Trailing whitespace and newline integrity | **PASS** | `0` | 0 errors |

### Demonstration of Negative Failure Modes

In accordance with the mission instructions, the routing test harness was subjected to three intentional failure mode probes to demonstrate active negative enforcement:

1. **Protocol-as-Skill Typing Violation:**
   - *Probe:* Setting `primary_owner: "historical-source-criticism"` in `ROUTE-022`.
   - *Outcome:* Test suite immediately failed with `primary_owner 'historical-source-criticism' has semantic_role 'SHARED_PROTOCOL'; shared protocols cannot be autonomous executable primary owners.`
2. **Unsupported-Method Reassignment Violation (Dynamic Invariant Regression):**
   - *Probe:* Reassigning `ROUTE-026` (staggered DID / synthetic control) to each registered component dynamically discovered from `docs/governance/ars_registry.yaml` (20 components evaluated).
   - *Outcome:* Every single registered component (20/20) was assertively rejected with routing errors (`ADV-D6 primary owner must be 'UNASSIGNED_CAPABILITY_GAP'` and negative assertion violation). No component was permitted to claim the unassigned causal-inference capability. In addition, an in-memory modification assigning an owner to `causal_inference_microeconometrics` in the registry immediately failed validation.
3. **Disciplinary Topic-over-Operation Violation:**
   - *Probe:* Assigning `ROUTE-024` (unit root test on wage share) to `political-economy-research` based on topic framing.
   - *Outcome:* Test suite immediately failed with `Negative assertion violated: primary_owner 'political-economy-research' is in must_not_primary_owner... ADV-D4 primary owner must be 'umass-applied-econometrics', got 'political-economy-research'.

### Testing Limitations
All routing contract and registry tests are deterministic offline verifications. They certify that routing policies, precedence rules, excluded owners, and capability boundaries are formally codified and enforceably discriminative. They do not simulate live generative LLM agent dialogue, which remains classified as `MODEL-BEHAVIOR EXECUTION PENDING`.

---

## 5. Preservation of Architectural Invariants and Boundaries

Wave D6 certifies full compliance with the following inherited repository constraints:

1. **Preservation of the Causal-Inference Gap:**
   - Micro causal inference (DID, IV, RDD, synthetic control) has `NO CURRENT CANONICAL OWNER`.
   - Codified as `causal_inference_microeconometrics` with `current_owner: null` and `migration_status: "CANDIDATE"`.
   - No new skill was authorized or created.
2. **Preservation of Domain Methodology Files:**
   - Zero modifications to `political-economy-research/` (runtime skill and 4 reference modules).
   - Zero modifications to `heterodox-economics-review/` (runtime skill and 4 reference modules).
   - Zero modifications to `umass-applied-econometrics/` (runtime skill and 2 tool reference protocols).
   - Zero modifications to `shared/protocols/historical_source_criticism_protocol.md`.
3. **Preservation of Profiles and Templates:**
   - Zero modifications to `profiles/advisors/`, `profiles/committees/`, `profiles/scholars/`, or `templates/`.
4. **Preservation of Frozen D5 Behavioral Evals:**
   - Zero modifications to `evals/gold/wave_d_behavioral/cases.yaml`, `evals/gold/wave_d_behavioral/README.md`, or `scripts/test_wave_d_behavioral_evals.py`.
5. **Preservation of Physical Path Topology:**
   - Core and domain skills remain at their live repository root locations (`academic-paper`, `econ-write`, `academic-paper-reviewer`, `academic-pipeline`, `deep-research`, `econ-slides`, `political-economy-research`, `umass-applied-econometrics`, `heterodox-economics-review`).
   - Physical migration to `skills/domain/` remains strictly deferred to Wave F.
6. **Preservation of Unrelated Work:**
   - `docs/design/2026-10-10-editorial-governance/` (8 files) and `econ-slides/` (slide deck and tests) remain 100% untracked and untouched.

---

## 6. Unresolved Architectural Questions & Wave Perimeter

1. **Future Wave F Directory Harmonization:**
   During Wave F physical migration, `umass-applied-econometrics` is targeted to migrate to `skills/domain/applied-econometrics-pe` and `heterodox-economics-review` to `skills/domain/heterodox-macro-modeling`. Wave D6 ensures that runtime truth remains anchored to current root directory names while the governance registry accurately records both current runtime paths and target paths without conflation.
2. **Next Steps:**
   With Wave D6 complete, all domain capabilities across Waves D1 through D5.1 are logically reconciled with repository governance and routing infrastructure.

---

D6 IMPLEMENTED — AWAITING HUMAN REVIEW — NO COMMIT / NO PUSH
