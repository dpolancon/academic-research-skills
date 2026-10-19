# ARS Wave D0 — Read-Only Domain Capability Reconnaissance Report

- **Date:** 2026-10-14
- **Status:** COMPLETE — RECONNAISSANCE ONLY (NO IMPLEMENTATION AUTHORIZED)
- **Target Artifact:** `docs/design/wave-d/D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md`
- **Inspected Repository HEAD:** `917ee2f2332cef92015937bddd7337a52ef4b12d` (`refactor(governance): reconcile Wave C legacy surfaces`)
- **Post-Wave-C Synchronized Checkpoint:** `917ee2f` (reconciled Wave C legacy surfaces, stubs, and regression lock)
- **Pre-C5 Baseline Commit:** `38f31af` (`feat(profiles): extract committee scholar calibrations`)
- **Provenance Statement:** Commit `917ee2f` directly advances from `38f31af` by executing Wave C5 legacy reconciliation (`docs/design/2026-10-11-ars-target-architecture/22_WAVE_C5_LEGACY_DEPRECATION_AND_GOVERNANCE_RECONCILIATION.md`). Both commit references are legitimate; `38f31af` serves as the pre-C5 feature baseline, while `917ee2f` is the authoritative post-Wave-C synchronized HEAD inspected by this mission.
- **Authoritative Governance Reference:** `docs/governance/ars_registry.yaml` (v1.1.0) & `docs/governance/ROUTING_AND_PRECEDENCE.md` (v1.1.0)

---

## 0. EXECUTIVE VERDICT

This reconnaissance audit evaluates the live state of the `academic-research-skills` repository following the completion and regression lock of Waves A through C at synchronized checkpoint `917ee2f`. Its purpose is to resolve the canonical ownership, boundaries, and interfaces of remaining domain capabilities before any Wave D implementation work is authorized.

### Summary of Architectural Findings

1. **Comparative-Historical Political Economy Methodology is a Genuine Void:**
   The repository currently possesses zero canonical capability for qualitative, archival, or comparative-historical political economy methodology. Historical analysis is currently represented only through disparate fragments: brief calibration directives in a scholar profile (`profiles/scholars/kevin-young.md`), ad-hoc econometric dummy step-shifts (`umass-applied-econometrics/SKILL.md`), and journalistic house-style mandates (`editor-jacobin-lat/SKILL.md`). There is no operational capability for process tracing, causal-process observations (CPOs), rival mechanism adjudication, historical periodization, or comparative-relational explanation. A dedicated canonical domain skill—`political-economy-research`—is **architecturally justified and necessary**.

2. **Historical Source Criticism Requires Shared Evidential Protocol Substrate (Claim-Relative):**
   `deep-research` currently contains an evidence reference (`deep-research/references/source_quality_hierarchy.md`) based on a clinical/biomedical hierarchy that elevates randomized controlled trials and meta-analyses while demoting qualitative, documentary, and archival materials to "Level VI / VII (low weight / expert opinion)." Conversely, historical political economy relies heavily on archival, documentary, and institutional evidence. However, rather than replacing this with an inverted hierarchy that unconditionally privileges primary over secondary sources, historical source criticism must evaluate evidence **relative to the specific claim** (assessing provenance, institutional standpoint, intended audience, incentives for candor vs. concealment, access to events, contemporaneous vs. retrospective construction, and archival silence). It should be codified as a shared cross-domain protocol (`shared/protocols/historical_source_criticism_protocol.md`), conditionally activated when documentary/historical sources are present, and consumed by `political-economy-research`, `deep-research`, and `academic-paper-reviewer`.

3. **Applied Econometrics Contains High-Value Assets Marred by Critical Epistemic Leakage:**
   `umass-applied-econometrics` contains outstanding forensic and econometric assets: integration order governance (ADF + KPSS dual gates, collinearity filtering, $I(2)$ risk checks), levels-augmented Toda–Yamamoto $(k+d_{\max})$ specification mapping, small-sample bootstrapping ($N \le 30$), and data-first visualization. However, it suffers from two major defects:
   - **Critical Epistemic Violation (Rule 2.H.4):** Explicitly commands that *"For peripheral economies, interpret failures to cointegrate as evidence of structural regime-switching (e.g., FX-constrained accumulation) rather than data deficiency."* This forces an empirical failure of a statistical null/rank condition to mean substantive confirmation of a theoretical prior, violating the foundational epistemic invariant: **Theory proposes $\to$ Empirics tests $\to$ Interpretation follows evidence**.
   - **Heavy Prose Duplication:** Section 1 (lines 16–24) and Section 3 (Checklist items 1–3, 10) copy verbatim prose rules (BLUF, active voice, banned AI transitions) that belong canonically to `econ-write` and `shared/protocols/prose_discipline_protocol.md`.
   - **Methodological Protocol Classification:** The diagnostic protocols for cointegration audit and Toda–Yamamoto mapping are Markdown reasoning and specification protocols, not deterministic executable tools. Their methodological content belongs canonically to `applied-econometrics-pe`. Physical file relocation to future target directories (`tools/econometrics/`) belongs strictly to Wave F.

4. **Heterodox Macro-Modeling is Severely Under-Specified:**
   `heterodox-economics-review` currently consists of a 29-line fragment extracted from a single project-specific dispute concerning Sraffian Supermultiplier (SSM) singularities and variable capacity utilization. It completely lacks generalized coverage of macroeconomic closures (Keynesian, Kaleckian, Classical-Marxian), dynamic system stability (Jacobian trace-determinant criteria, Routh-Hurwitz conditions, Hopf bifurcations), balance-sheet stock-flow consistency (SFC), traverse dynamics, or center–periphery external constraints. It must be redesigned from a narrow 29-line paper checklist into a rigorous domain modeling capability: `heterodox-macro-modeling`.

5. **Stock-Flow Consistency (SFC) Ownership Belongs Under Macro-Modeling:**
   Sectoral balances, balance-sheet matrices, transaction-flow accounting, and dynamic stock accumulation are theoretical-accounting structures inherent to Post-Keynesian macroeconomics. They belong canonically inside `heterodox-macro-modeling`. Separate deterministic arithmetic tool creation is deferred pending demonstrated need in D3/D5.

6. **Public Scholarship Decomposition Deferred Beyond Wave D/F:**
   `editor-jacobin-lat` bundles generic public-scholarship translation (de-specialization, accessible non-academic prose, structural argument) with the house style of *Jacobin América Latina* (Martín Arboleda criteria, 12-word declarative titles without subtitles, Spanish editorial register). In accordance with the post-Wave-C restart handoff, execution of this decomposition is `DEFERRED — FUTURE AUTHORIZATION REQUIRED` (beyond Wave D/F). A governing-document timing inconsistency is recorded between the target blueprint and the restart handoff.

### Recommended Logical Domain Architecture After Wave D

```text
skills/domain/
├── econ-write/                          [ACTIVE — Disciplinary economics writing conventions]
├── applied-econometrics-pe/             [REFACTORED from umass-applied-econometrics; H.4 purged]
├── heterodox-macro-modeling/            [REDESIGNED from heterodox-economics-review; expanded scope]
└── political-economy-research/          [PROPOSED NEW — Comparative-historical PE & process tracing]

shared/protocols/
├── prose_discipline_protocol.md         [ACTIVE — Cross-domain prose discipline]
└── historical_source_criticism_protocol.md [PROPOSED NEW — Claim-relative archival & documentary evaluation]

references/econometrics/ (internal to applied-econometrics-pe; FUTURE WAVE-F TARGET: tools/econometrics/)
├── cointegration_audit.md               [Methodological cointegration specification protocol]
└── toda_yamamoto.md                     [Methodological Toda-Yamamoto lag grid mapping protocol]
```

*(Note: Per Wave C invariant, physical file migration of directories to `skills/domain/` or `tools/econometrics/` remains deferred to Wave F; runtime paths remain at repository root or existing extracted substrates).*

### Major Human Resolutions Recorded for Subsequent Decision Lock

1. **Protocol Packaging for Historical Source Criticism:** Provisionally approved as a cross-domain shared protocol (`shared/protocols/historical_source_criticism_protocol.md`) with **conditional activation** when documentary/archival evidence is present. It does not replace quantitative or experimental standards in unrelated domains.
2. **Epistemic Purge Authorization:** Authorize the deletion of `umass-applied-econometrics` Rule 2.H.4 and its replacement with an evidence-conditioned hypothesis protocol in D2.
3. **Formal Scope of `political-economy-research`:** Bound primarily as a **research methodology capability** (process tracing, periodization, relational comparison, source-based causal inference), not a universal theory encyclopedia. Formal mathematical modeling belongs to `heterodox-macro-modeling`.
4. **SFC Tooling Status:** `DEFER TOOL CREATION PENDING DEMONSTRATED NEED`. First establish the analytical SFC modeling capability in D3; create a deterministic arithmetic zero-sum matrix checker only if a recurring, specifiable operation demonstrates the need.
5. **Public Scholarship Status:** `DEFERRED — FUTURE AUTHORIZATION REQUIRED` (deferred beyond Wave D/F).

---

## 1. INSPECTION SCOPE

### 1.1 Files and Directories Inspected

- **Governance & Target Architecture:**
  - `docs/governance/ars_registry.yaml` (v1.1.0, 517 lines)
  - `docs/governance/ROUTING_AND_PRECEDENCE.md` (v1.1.0, 164 lines)
  - `docs/governance/MODE_REGISTRY.md` (v1.0.0, 48 lines)
  - `docs/design/2026-10-11-ars-target-architecture/00_TARGET_STATE_ARCHITECTURE.md`
  - `docs/design/2026-10-11-ars-target-architecture/01_CAPABILITY_OWNERSHIP_MAP.md`
  - `docs/design/2026-10-11-ars-target-architecture/02_CURRENT_TO_TARGET_GAP_MATRIX.md`
  - `docs/design/2026-10-11-ars-target-architecture/03_CURRENT_COMPONENT_REGISTRY.md`
  - `docs/design/2026-10-11-ars-target-architecture/04_CAPABILITY_REDUNDANCY_AUDIT.md`
  - `docs/design/2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md`
  - `docs/design/2026-10-11-ars-target-architecture/14_WAVE_C_DECOMPOSITION_DESIGN_REVIEW.md`
  - `docs/design/2026-10-11-ars-target-architecture/15_WAVE_C_EXECUTION_PLAN.md`
  - `docs/design/2026-10-11-ars-target-architecture/16_WAVE_C_HUMAN_DECISION_LOCK.md`
  - `docs/design/2026-10-11-ars-target-architecture/17_WORKSPACE_CAPSULE_ARCHITECTURE.md`
  - `docs/design/2026-10-11-ars-target-architecture/18_WAVE_C1_PROSE_DISCIPLINE_EXTRACTION_REPORT.md`
  - `docs/design/2026-10-11-ars-target-architecture/19_WAVE_C1_1_PROSE_BOUNDARY_REPAIR.md`
  - `docs/design/2026-10-11-ars-target-architecture/20_WAVE_C2_EDITORIAL_GOVERNANCE_IMPLEMENTATION_REPORT.md`
  - `docs/design/2026-10-11-ars-target-architecture/21_WAVE_C3_PROFILE_EXTRACTION_REPORT.md`
  - `docs/design/2026-10-11-ars-target-architecture/22_WAVE_C5_LEGACY_DEPRECATION_AND_GOVERNANCE_RECONCILIATION.md`
- **Core Reasoning Skills:**
  - `deep-research/SKILL.md` (v2.9.4, 508 lines)
  - `deep-research/agents/source_verification_agent.md` (220 lines)
  - `deep-research/agents/timeline_extraction_agent.md` (100 lines)
  - `deep-research/references/source_quality_hierarchy.md` (189 lines)
  - `deep-research/references/methodology_patterns.md`
  - `deep-research/templates/evidence_assessment_template.md`
  - `academic-paper/SKILL.md` (v3.2.0, 520 lines)
  - `academic-paper/references/domain_evidence_profiles.md`
  - `academic-paper-reviewer/SKILL.md` (v1.10.0, 480 lines)
  - `academic-paper-reviewer/references/review_criteria_framework.md`
- **Domain Skills:**
  - `econ-write/SKILL.md` (759 lines)
  - `econ-write/identification-strategies.md` (164 lines)
  - `econ-write/review-checklist.md`
  - `umass-applied-econometrics/SKILL.md` (111 lines)
  - `umass-applied-econometrics/tools/cointegration_specification_audit.md` (215 lines)
  - `umass-applied-econometrics/tools/toda_yamamoto_specification_mapping.md` (185 lines)
  - `heterodox-economics-review/SKILL.md` (29 lines)
- **Dissemination Skills:**
  - `econ-slides/SKILL.md` (145 lines)
  - `editor-jacobin-lat/SKILL.md` (65 lines)
  - `editor-jacobin-lat/references/criterios_martin_arboleda.md`
  - `editor-jacobin-lat/references/glosario_desespecializacion.md`
  - `editor-jacobin-lat/scripts/audit_columna.py`
- **Shared Substrates & Governance:**
  - `shared/protocols/prose_discipline_protocol.md` (v1.0.0, 285 lines)
  - `shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md`
  - `shared/contracts/passport/timeline.schema.json`
  - `shared/contracts/passport/citation_provenance.schema.json`
  - `shared/contracts/passport/version_records.schema.json`
  - `profiles/PROFILE_CONTRACT.md` (v1.0.0, 210 lines)
  - `profiles/scholars/michael-ash.md`, `deepankar-basu.md`, `kevin-young.md`
  - `profiles/advisors/michael-ash.md`
  - `profiles/committees/umass-pe.md`
- **Legacy Compatibility Stubs:**
  - `advisor-reviewer/SKILL.md` (deprecated redirect stub)
  - `PE-phd-committee/SKILL.md` (deprecated redirect stub)
  - `prose-register-critic/SKILL.md` (deprecated redirect stub)
- **Test & Validation Harnesses:**
  - `scripts/validate_ars_registry.py`
  - `scripts/test_routing_contract.py`
  - `scripts/test_prose_discipline.py`
  - `scripts/test_profile_contract.py`
  - `scripts/test_revision_guard.py`
  - `scripts/test_wave_c_reconciliation.py`
  - `evals/gold/routing/cases.yaml` (17 canonical cases)

### 1.2 Non-Inspected Areas and Rationale

- **Quarantined Legacy Project Directories:**
  - `paper_refutation_SSM/`, `user_testings/`, `editing_memos/`, `writings_testing/`, `slide_deck_Fondecyt/`.
  - *Rationale:* Explicitly locked as non-canonical project overlays in Waves B and C. They do not own reusable capabilities and are slated for offloading to external repositories in Wave F.
- **Client Junction Directories:**
  - `.agents/skills/`, `.claude/skills/`.
  - *Rationale:* Untracked symlink/junction views governed by `install-local.ps1`.
- **Note on Unverified Component `math-modeling`:**
  - An earlier draft of D0 referenced an upstream generic `math-modeling` skill. Repository inspection confirmed that `math-modeling` does not exist on disk and is not registered in `docs/governance/ars_registry.yaml`. That claim was unsupported by live evidence and has been purged from this reconnaissance.

---

## 2. CURRENT CAPABILITY OWNERSHIP MAP

The following table reflects the authoritative operational baseline established in `docs/governance/ars_registry.yaml` (v1.1.0) and confirmed by live code inspection.

| Capability ID | Canonical Current Owner | Current Runtime Path | Implementation Type | Semantic Role | Quality / Status | Overlap Risk | Recommended Disposition |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `literature_synthesis_search` | `deep-research` | `deep-research` | `SKILL` | `CORE_SKILL` | `ACTIVE` / High | None (sole search engine) | PRESERVE; track upstream |
| `academic_manuscript_lifecycle` | `academic-paper` | `academic-paper` | `SKILL` | `CORE_SKILL` | `ACTIVE` / High | Low (with `econ-write`) | PRESERVE; generic lifecycle owner |
| `simulated_external_peer_review` | `academic-paper-reviewer` | `academic-paper-reviewer` | `SKILL` | `CORE_SKILL` | `ACTIVE` / High | None (monopoly locked) | PRESERVE; sole review engine |
| `research_workflow_orchestration` | `academic-pipeline` | `academic-pipeline` | `ORCHESTRATOR` | `ORCHESTRATOR` | `ACTIVE` / High | None (control plane only) | PRESERVE; orchestration only |
| `economics_prose_and_section_standards` | `econ-write` | `econ-write` | `SKILL` | `DOMAIN_SKILL` | `ACTIVE` / High | Low (policy consumer) | PRESERVE; economics writing policy |
| `applied_econometrics_political_economy` | `umass-applied-econometrics` | `umass-applied-econometrics` | `SKILL` | `DOMAIN_SKILL` | `ACTIVE` / High with defects | High (prose duplication, Rule H.4) | REFACTOR in Wave D2; purge Rule H.4; deduplicate prose |
| `heterodox_macro_modeling` | `heterodox-economics-review` | `heterodox-economics-review` | `SKILL` | `DOMAIN_SKILL` | `ACTIVE` / Inadequate (29 lines) | High (name implies review; narrow SSM scope) | REDESIGN in Wave D3; expand to full modeling skill |
| `scholarly_slide_production` | `econ-slides` | `econ-slides` | `SKILL` | `DISSEMINATION_SKILL` | `ACTIVE` / High | Low | PRESERVE; quarantine Fondecyt files in Wave F |
| `public_scholarship_translation` | `editor-jacobin-lat` | `editor-jacobin-lat` | `SKILL` | `DISSEMINATION_SKILL` | `PLANNED_MIGRATION` | High (bundles generic + Jacobin) | DEFERRED — FUTURE AUTHORIZATION REQUIRED (beyond Wave D/F) |
| `prose_discipline_and_lexical_audit` | `prose-discipline` | `shared/protocols/prose_discipline_protocol.md` | `SHARED_PROTOCOL` | `SHARED_PROTOCOL` | `ACTIVE` / High | None (shared substrate) | PRESERVE; cross-domain protocol |
| `editorial_decision_persistence` | `editorial-governance` | `shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md` | `SHARED_PROTOCOL` | `SHARED_PROTOCOL` | `ACTIVE` / High | None (change control only) | PRESERVE; change control only |
| `cointegration_specification_audit` | `umass-applied-econometrics` | `umass-applied-econometrics/tools/cointegration_specification_audit.md` | `METHODOLOGICAL_PROTOCOL` (Markdown reference) | `METHODOLOGICAL_PROTOCOL` | `ACTIVE` / High | Medium (misclassified as tool) | Retain in `applied-econometrics-pe` as methodological protocol; FUTURE WAVE-F TARGET PATH — NOT A WAVE-D MOVE |
| `toda_yamamoto_specification_mapping` | `umass-applied-econometrics` | `umass-applied-econometrics/tools/toda_yamamoto_specification_mapping.md` | `METHODOLOGICAL_PROTOCOL` (Markdown reference) | `METHODOLOGICAL_PROTOCOL` | `ACTIVE` / High | Medium (misclassified as tool) | Retain in `applied-econometrics-pe` as methodological protocol; FUTURE WAVE-F TARGET PATH — NOT A WAVE-D MOVE |
| `irf_girf_generation` | `irf-plotting` | `irf-plotting` | `TOOL` | `TOOL` | `PLANNED_MIGRATION` | Low | PRESERVE; retyping and physical relocation deferred to Wave F |
| `latex_workspace_compilation` | `latex-compilation` | `latex-compilation` | `TOOL` | `TOOL` | `PLANNED_MIGRATION` | Low | PRESERVE; retyping and physical relocation deferred to Wave F |
| `advisor_michael_ash_calibration` | `advisor-michael-ash` | `profiles/advisors/michael-ash.md` | `PROFILE` | `PROFILE` | `ACTIVE` / High | None (calibration input) | PRESERVE; profile only |
| `committee_umass_pe_defense` | `committee-umass-pe` | `profiles/committees/umass-pe.md` | `PROFILE` | `PROFILE` | `ACTIVE` / High | None (calibration input) | PRESERVE; profile only |
| `venue_jacobin_lat_editorial` | `editor-jacobin-lat` | `editor-jacobin-lat` | `DISSEMINATION_SKILL` | `PROFILE` (embedded) | `PLANNED_MIGRATION` | High (embedded in skill) | DEFERRED — FUTURE AUTHORIZATION REQUIRED (beyond Wave D/F) |
| `author_diego_academic_voice` | `academic-paper` | `academic-paper` | `CORE_SKILL` | `PROFILE` (embedded) | `PLANNED` | Medium (ad-hoc across prompts) | DEFERRED — FUTURE AUTHORIZATION REQUIRED (beyond Wave D/F) |
| `political_economy_research_methodology` | *None (Unowned)* | *None* | `CANDIDATE` | `DOMAIN_SKILL` | `CANDIDATE` / Demonstrated Void | High (if improperly bounded) | DESIGN in Wave D1; canonical domain skill |

---

## 3. POLITICAL-ECONOMY METHODOLOGY GAP MATRIX

The central object of Wave D0 reconnaissance is the unowned candidate capability: `political_economy_research_methodology`. This matrix evaluates each proposed sub-capability against live repository evidence.

| Candidate Capability | Existing Coverage in Live Repo | Existing Owner / Artifact | Quality & Limitations | Missing Behavior | Proposed Architectural Owner | Component Type | Repository Evidence | Confidence |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **Historical Periodization** | Partial | `umass-applied-econometrics/SKILL.md` §2.H.2; `profiles/scholars/kevin-young.md` §3.2 | Low. Encodes hardcoded Fordist thresholds ($\hat{\gamma} \approx 1$) or historic narrative dates without analytical methodology. | Rules for identifying endogenous crisis points, structural breaks vs. cyclical fluctuations, social structures of accumulation (SSA) shifts, and institutional boundaries. | `political-economy-research` | Domain Skill | `umass-applied-econometrics/SKILL.md` line 68; `profiles/scholars/kevin-young.md` lines 36–42 | OBSERVED |
| **Historical Source Criticism** | Absent | None. `deep-research` covers only bibliographic databases; `prose-discipline` lines 127, 137 disclaims source evaluation. | Inadequate. `deep-research/references/source_quality_hierarchy.md` uses a biomedical pyramid that treats archival records as "low quality descriptive studies." | Claim-relative evaluation of archival provenance, institutional standpoint/bias, contemporaneous vs. retrospective records, archival silence, and triangulation across documentary sources. | `shared/protocols/historical_source_criticism_protocol.md` (consumed by PE skill, `deep-research`, reviewer) | Shared Protocol | `deep-research/references/source_quality_hierarchy.md` lines 6–24, 91–100 | OBSERVED |
| **Process Tracing** | Absent | None. `econ-write/identification-strategies.md` covers only microeconometric identification (DiD, IV, RDD). | Absent. Zero protocols for mechanism-based qualitative explanation or causal-process observations. | Event $\to$ mechanism $\to$ intermediate process $\to$ response $\to$ outcome mapping; discriminating causal mechanisms within a single historical case. (*CANDIDATE IMPLEMENTATION CONTENT — TO BE VALIDATED IN D1/D4*). | `political-economy-research` | Domain Skill | `econ-write/identification-strategies.md` lines 1–164; `docs/design/.../04_...` line 159 | OBSERVED |
| **Causal-Process Observations (CPOs)** | Absent | None. | Absent. Econometric skills recognize only data-set observations (DSOs). | Protocol for identifying diagnostic pieces of data that provide evidence of context, process, or mechanism, distinct from statistical sample points. (*CANDIDATE IMPLEMENTATION CONTENT — TO BE VALIDATED IN D1/D4*). | `political-economy-research` | Domain Skill | Live repository search returned 0 matches for "causal process observation" | OBSERVED |
| **Rival Mechanism Discrimination** | Absent | None. `deep-research/agents/devils_advocate_agent.md` tests rhetorical logic, not empirical historical mechanisms. | Absent. | Systematic generation of competing institutional hypotheses and testing their observable implications against historical traces. (*CANDIDATE IMPLEMENTATION CONTENT — TO BE VALIDATED IN D1/D4*). | `political-economy-research` | Domain Skill | `deep-research/agents/devils_advocate_agent.md` | OBSERVED |
| **Negative Evidence Evaluation** | Absent | None. | Absent. | Rules for assessing "absence of evidence": inferring causal status from the non-occurrence of an expected trace where a mechanism predicts it must exist. (*CANDIDATE IMPLEMENTATION CONTENT — TO BE VALIDATED IN D1/D4*). | `political-economy-research` | Domain Skill | Live repository contains zero negative evidence protocols | OBSERVED |
| **Necessary vs. Sufficient Conditions** | Absent | None. Econometric skills use linear regression which implicitly assumes average additive effects. | Absent. | Qualitative logic tests (hoop tests, smoking-gun tests, doubly decisive tests; Van Evera / Bennett & George framework). (*CANDIDATE IMPLEMENTATION CONTENT — TO BE VALIDATED IN D1/D4*). | `political-economy-research` | Domain Skill | `docs/design/.../04_...` line 159 | OBSERVED |
| **Comparative-Relational Reasoning** | Absent | None. `editor-jacobin-lat` mentions regional dynamics but bans "invented parallels" without a constructive method. | Absent. The repository is strictly single-case / single-manuscript focused. | Distinguishing parallel case comparison (Mill's methods) from relational historical explanation (cases mutually constituted in global division of labor). (*CANDIDATE IMPLEMENTATION CONTENT — TO BE VALIDATED IN D1/D4*). | `political-economy-research` | Domain Skill | `editor-jacobin-lat/SKILL.md` line 21; `docs/design/.../00_...` line 259 | OBSERVED |
| **Center–Periphery Relations** | Fragmented | `editor-jacobin-lat/SKILL.md` line 43; `umass-applied-econometrics/SKILL.md` §2.H.4 | Defective. Present as rhetorical anti-imperialist framing or forced econometric rule H.4. | Methodological framework for analyzing foreign exchange constraints, balance-of-payments dominance, monetary hierarchy, and structural dependency. | `political-economy-research` | Domain Skill | `editor-jacobin-lat/SKILL.md` line 43; `umass-applied-econometrics/SKILL.md` line 70 | OBSERVED |
| **Institutional Transformation** | Fragmented | `profiles/scholars/michael-ash.md` §3.4 ("workplace black box"); `kevin-young.md` §3.1 | Calibration only. Scholar profiles raise questions during review but do not execute research workflows. | Step-by-step guidance for tracking institutional conversion, layering, drift, exhaustion, and displacement (Thelen/Streeck framework). (*CANDIDATE IMPLEMENTATION CONTENT — TO BE VALIDATED IN D1/D4*). | `political-economy-research` | Domain Skill | `profiles/scholars/michael-ash.md` lines 49–56 | OBSERVED |
| **State Transformation & Coalitions** | Fragmented | `editor-jacobin-lat` ("pugna distributiva"); `kevin-young.md` §3.3 ("elite mobilization") | Partial. Exists only as thematic review reminders or op-ed talking points. | Analytical framework for analyzing bureaucratic state capacity, ruling class fractions, social pacts, and distributional coalitions. | `political-economy-research` | Domain Skill | `profiles/scholars/kevin-young.md` lines 43–46 | OBSERVED |

---

## 4. HISTORICAL-METHODOLOGY DECOMPOSITION

A primary architectural task of Wave D0 is to determine whether the constituent elements of historical research methodology belong inside a single domain skill or require shared protocols.

### 4.1 Periodization

- **Nature of the Capability:** Periodization is an active analytical operation in comparative-historical research. It is the act of dividing continuous historical time into structurally distinct regimes governed by specific institutional logics, accumulation regimes, or power balances.
- **Repository Audit:** In the live repository, periodization is treated either as an econometric nuisance requiring dummy step-shifts (`umass-applied-econometrics/SKILL.md` §2.D, §2.H) or as pre-packaged historical narrative dates (`profiles/scholars/kevin-young.md` §3.2). There is no methodology for establishing *why* a boundary is drawn at a given juncture.
- **Epistemic Invariant:** Periodization must not be derived post-hoc solely to clean up econometric residuals (which amounts to data-mining under the guise of history). It requires historical-institutional justification based on documented regulatory and legal shifts, class reconfigurations, or external shocks.
- **Ownership Recommendation:** **Internal to `political-economy-research`**. It is a core reasoning capability of historical political economy, not a generic cross-domain tool.

### 4.2 Historical Source Criticism (Claim-Relative Evidence Assessment)

- **Nature of the Capability:** Historical source criticism is an evidential discipline governing the evaluation, authentication, and interpretation of documentary and archival records.
- **Repository Audit:**
  - `deep-research` is the repository's sole evidence-retrieval engine. However, its evidentiary reference hierarchy (`deep-research/references/source_quality_hierarchy.md`) is structured around clinical and quantitative standards (meta-analyses, RCTs, quasi-experiments), treating qualitative and descriptive studies as "Level VI/VII" (low weight).
  - When historical, institutional, or documentary claims are evaluated, this clinical hierarchy represents a clear **coverage gap / domain-mismatch risk**.
  - Conversely, replacing a clinical hierarchy with an inverted universal hierarchy ("primary archival sources > secondary literature") would be equally flawed. A primary source (e.g. an internal diplomatic cable) is not inherently "more true" than a secondary synthesis; it reflects the perceptions, mandates, and biases of its creator.
- **Required Claim-Relative Evidential Dimensions:**
  The protocol must assess evidence **strictly relative to the claim being asserted**, evaluating:
  1. *Provenance & Custodial Authenticity:* Verification of origin, transmission, and archival custody.
  2. *Producer & Institutional Standpoint:* Who produced the document, under what statutory mandate, for what intended audience, and representing what institutional interest?
  3. *Incentives for Candor vs. Concealment:* Assessing bureaucratic self-protection, diplomatic deception, propaganda, or domestic political posturing.
  4. *Temporal Proximity & Access:* Distinguishing eyewitness/contemporaneous records from retrospective memoirs, oral histories, or post-facto legal rationalizations.
  5. *Archival Survival & Silence:* Explicitly evaluating what is omitted or destroyed due to state secrecy, informal deals, or institutional censorship.
  6. *Corroboration & Contradiction:* Triangulating across independent documentary sources (e.g., cross-referencing diplomatic cables with corporate records and labor movement minutes).
  7. *Evidentiary Role for the Claim:* A diplomatic cable may be definitive evidence for *what an ambassador believed and reported*, but weak evidence that *the underlying event actually occurred as reported*.
- **Ownership Recommendation:** **Shared Cross-Domain Protocol (`shared/protocols/historical_source_criticism_protocol.md`)**.
  - *Rationale:* Multiple skills (`political-economy-research`, `deep-research` source verification agent, `academic-paper`, and `academic-paper-reviewer`) must evaluate historical and documentary sources. Codifying this as a shared protocol with **conditional activation** (activated only when documentary/historical sources are present) prevents duplicating evidential rules across components without interfering with quantitative evidence in other domains.

### 4.3 Process Tracing

- **Nature of the Capability:** Process tracing is an empirical method designed to identify, test, and verify causal mechanisms within a single historical trajectory or case.
- **Repository Audit:** `econ-write/identification-strategies.md` provides exhaustive guidance on microeconometric identification (RCT, DiD, IV, RDD, Synthetic Control, Bunching). However, econometric identification identifies *net average treatment effects* ($E[Y_1 - Y_0]$) across populations using statistical variance. It does **not** trace the operational sequence of intermediate mechanisms linking cause to outcome.
- **Architectural Scope (Capability Envelope):**
  - Specification of intermediate causal mechanisms: $\text{Antecedent Shock} \to M_1 \to M_2 \to \text{Outcome}$.
  - Causal-Process Observations (CPOs) as diagnostic evidentiary points.
  - Systematic rival mechanism discrimination.
  - Negative evidence evaluation (absence of expected traces).
  - *Candidate Implementation Content (to be validated in D1/D4):* Specific testing taxonomies such as Van Evera / Bennett & George hoop tests, smoking-gun tests, and doubly decisive tests.
- **Boundary with Econometric Identification:**
  - Econometrics asks: *Did $X$ statistically cause $Y$ across a sample of observations, holding covariates constant?*
  - Process tracing asks: *Did the specific sequence of mechanisms $M_1 \to M_2 \to M_3$ operate in this case to produce $Y$, and does empirical trace evidence eliminate alternative mechanisms $M_A$ or $M_B$?*
  - The two must never be conflated. A regression coefficient cannot substitute for process tracing, and a process trace cannot establish statistical exogeneity.
- **Ownership Recommendation:** **Internal to `political-economy-research`**. It represents an active, specialized reasoning workflow.

### 4.4 Comparative-Relational Reasoning

- **Nature of the Capability:** Comparative analysis in historical political economy must distinguish between two fundamentally different modes of inquiry:
  1. *Parallel Case Comparison (Millian / Variable-Oriented):* Treats cases as independent, isolated units ("billiard balls"). Compares variable values across cases, assuming independence of observations (ignoring Galton's problem).
  2. *Relational Historical Explanation (Systemic / Relational):* Treats cases as interconnected parts of a shared transnational system (global capitalism, monetary hierarchy, imperial networks, international supply chains). Explains divergent outcomes as the product of asymmetric structural relations rather than isolated domestic choices.
- **Repository Audit:** The repository currently has no comparative methodology. `editor-jacobin-lat` contains an ad-hoc warning against "invented geographic parallels" (line 21), but provides no positive method.
- **Ownership Recommendation:** **Internal to `political-economy-research`**.

---

## 5. APPLIED ECONOMETRICS AUDIT (`umass-applied-econometrics`)

`umass-applied-econometrics` represents an intellectually distinctive component combining rigorous time-series econometrics with the critical traditions of the UMass Amherst economics department. An itemized audit reveals both essential capabilities to preserve and serious defects requiring remediation.

### 5.1 Itemized Disposition Map

| Component / Section | Item Description | Disposition | Exact Repository Location | Architectural Justification |
|:---|:---|:---|:---|:---|
| **Section 1 (Lines 16–24)** | Prose & Tone Layer (BLUF, Simplicity, Banish AI-isms, Variable Definitions) | **DELETE / DEDUPLICATE** | `umass-applied-econometrics/SKILL.md` lines 16–24 | Pure duplication. Exactly duplicates `econ-write/SKILL.md` Core Principles and `shared/protocols/prose_discipline_protocol.md`. |
| **Section 2.A (Lines 31–34)** | Forensic Transparency (Herndon, Ash, & Pollin 2014) | **PRESERVE** | `umass-applied-econometrics/SKILL.md` lines 31–34 | Authoritative methodological standard. Demands transparency in data cleaning, sample cuts, and outlier exclusions. |
| **Section 2.B (Lines 35–38)** | Data-First Non-Parametric Visualization (Ash, Basu, & Dube 2017) | **PRESERVE** | `umass-applied-econometrics/SKILL.md` lines 35–38 | Methodological gate. Raw trends and non-parametric plots must anchor the analysis before parametric regressions are run. |
| **Section 2.C (Lines 39–42)** | Endogenous Class Struggle & Distribution | **PRESERVE (with refactor)** | `umass-applied-econometrics/SKILL.md` lines 39–42 | Treating distributional variables as endogenous drivers and testing bidirectional feedback via VECM is good econometric practice; must not force findings if feedback is rejected. |
| **Section 2.D (Lines 43–46)** | Specification-Space Mapping (Maziarz 2017) | **PRESERVE** | `umass-applied-econometrics/SKILL.md` lines 43–46 | Methodological standard. Demands full reporting of lag grids, boundary searches, and failed cointegration tests. |
| **Section 2.E (Lines 47–50)** | Descriptive Macro Grounding (Marglin) | **PRESERVE** | `umass-applied-econometrics/SKILL.md` lines 47–50 | Essential disciplinary standard. Simple, intuitive historical growth indicators must be integrated into the main text. |
| **Section 2.F (Lines 51–54)** | Institutional Deconstruction of Indicators (Pollin 1998) | **PRESERVE (with refactor)** | `umass-applied-econometrics/SKILL.md` lines 51–54 | Substantive critique of mainstream indicators (e.g. capacity utilization); must guide interpretation without overriding empirical data. |
| **Section 2.G (Lines 55–63)** | Integration Order Governance as Specification Gate | **PRESERVE** | `umass-applied-econometrics/SKILL.md` lines 55–63 | Gold standard of empirical discipline. Dual ADF+KPSS testing, collinearity screening ($r>0.99$, condition number $>30$), $I(2)$ risk checks, candidate disposition tables. |
| **Section 2.H.1, 2.H.3 (Lines 66–67, 69)** | Political Economy Interpretation of Parameters | **PRESERVE (with refactor)** | `umass-applied-econometrics/SKILL.md` lines 66–67, 69 | Framing parameters through economic theory; must be conditioned on empirical results rather than assumed ex-ante. |
| **Section 2.H.2 (Line 68)** | Hardcoded Historical Regime Signatures ($\hat{\gamma} \approx 1$ Fordist) | **REFACTOR** | `umass-applied-econometrics/SKILL.md` line 68 | Project-specific point estimates from Diego's dissertation chapter on machinery and structures. Demote to illustrative example; generalize rule to regime stability checks. |
| **Section 2.H.4 (Line 70)** | Forced Cointegration Failure Interpretation | **DELETE / PURGE** | `umass-applied-econometrics/SKILL.md` line 70 | **CRITICAL DEFECT.** Mandates interpreting failed cointegration as "structural regime-switching" rather than empirical rejection. |
| **Section 2.I (Lines 72–79)** | Small-Sample Bootstrap for Short Macro Panels | **PRESERVE** | `umass-applied-econometrics/SKILL.md` lines 72–79 | Methodological standard. Residual bootstrap resampling (300–1000 reps) for $N \le 30$ macro panels to guard against asymptotic size distortion. |
| **Section 2.J (Lines 80–89)** | Toda–Yamamoto Causality Mapping (Amiri & Ventelou 2012) | **PRESERVE** | `umass-applied-econometrics/SKILL.md` lines 80–89 | Benchmark $(k+d_{\max})$ levels VAR protocol with ex-ante openness, lag grids, SBIC/AIC markers ($^a$), dynamic sign tracking ($\sum\hat{\beta}_i$), and Lakatosian tournament tables. |
| **Section 3 (Lines 94–110)** | Diagnostic Checklist (Items 1–3, 10) | **DELETE / DEDUPLICATE** | `umass-applied-econometrics/SKILL.md` lines 96–98, 105 | Duplicate writing/prose checks; delegate to `econ-write`. Retain econometrics checklist items 4–9, 11–15. |
| **Protocol 1 (Embedded)** | Cointegration Specification Audit Protocol | **PRESERVE AS METHOD PROTOCOL** | `umass-applied-econometrics/tools/cointegration_specification_audit.md` | Methodological specification protocol owned by `applied-econometrics-pe`. Retain in place during Wave D; FUTURE WAVE-F TARGET PATH — NOT A WAVE-D MOVE. |
| **Protocol 2 (Embedded)** | Toda–Yamamoto Specification Mapping Protocol | **PRESERVE AS METHOD PROTOCOL** | `umass-applied-econometrics/tools/toda_yamamoto_specification_mapping.md` | Methodological specification protocol owned by `applied-econometrics-pe`. Retain in place during Wave D; FUTURE WAVE-F TARGET PATH — NOT A WAVE-D MOVE. |

### 5.2 Analysis of the Epistemic Ordering: Theory $\to$ Empirics $\to$ Interpretation

The target architecture enforces a strict epistemic hierarchy:
```text
THEORY
    proposes variables, mechanisms, hypotheses, and structural restrictions
        ↓
EMPIRICS
    tests stochastic admissibility, estimates parameters, and discriminates specifications
        ↓
INTERPRETATION
    evaluates findings conditioned strictly on the empirical result
```

#### Detailed Repository Evidence of Epistemic Inversion

In `umass-applied-econometrics/SKILL.md` Section 2.H, Rule 4 states:
```markdown
4. For peripheral economies, interpret failures to cointegrate as evidence of
   structural regime-switching (e.g., FX-constrained accumulation) rather
   than data deficiency.
```

**Epistemic Analysis:**
- In time-series econometrics, cointegration is an empirical test of whether a stationary linear combination of non-stationary series exists. If cointegration fails, the empirical finding is that the hypothesized long-run equilibrium relationship does not hold in the data.
- Rule 2.H.4 commands the researcher to convert an empirical rejection (no cointegration) into positive confirmation of a substantive theoretical concept ("structural regime-switching under foreign exchange constraints").
- This insulates the theoretical prior from empirical falsification. If cointegration holds, the theory is affirmed; if cointegration fails, the theory is also affirmed. This is an epistemic inversion.

**Remedy for Wave D2 Implementation:**
Refactor Rule 2.H.4 to enforce honest evidence conditioning:
> *"If candidate series fail to cointegrate in peripheral or volatile economies, researchers may formulate the hypothesis that parameter instability or structural regime-switching (e.g., balance-of-payments crises) disrupted the long-run relation. The researcher must then explicitly test for structural breaks or estimate sub-period/threshold systems. If structural break models also fail to find cointegration, the researcher must report the absence of cointegration as an empirical non-finding and reject the stable long-run relationship."*

---

## 6. HETERODOX MACRO AUDIT (`heterodox-economics-review`)

### 6.1 Current Capability vs. Target Modeling Scope

Inspection of `heterodox-economics-review/SKILL.md` confirms that it currently contains only **29 lines of text**.

```text
CURRENT CONTENT (29 lines):
§1. Mathematical Rigor & Dynamic Consistency Check:
    - Singularity checks at normal capacity utilization (\mu = 1)
    - Boundary conditions (\mu -> 0, \mu -> \infty)
    - Logarithmic derivatives of ratios (\nu = K / Y^p)
§2. Avoiding Specification Tautologies:
    - Behavioral vs. technological instability (\theta \neq 1 causing \nu -> \infty)
    - Induced technical change under unbalanced growth
§3. Literature & Conceptual Alignment:
    - Harrodian instability as behavioral/expectational (Smithian vs. Harrodian; Serrano, Freitas, Lavoie, Nikiforos)
§4. LaTeX Standards:
    - amsthm proposition/proof syntax
```

### 6.2 Nature of the Component: Modeling Capability vs. Ideological Reviewer

- **Naming Ambiguity:** The component is named `heterodox-economics-review`. This conflicts with `academic-paper-reviewer` by implying that it is an independent peer-review engine.
- **Substantive Role:** In reality, the skill owns zero peer-review workflow logic (no referee personas, no decision letters, no revision tracking). Its substantive content is exclusively **theoretical macro-modeling verification**.
- **Project Contamination:** The current 29 lines were extracted directly from Diego's specific research refuting Anwar Shaikh's Sraffian Supermultiplier formulation (`paper_refutation_SSM/`). It focuses obsessively on whether $\theta = 1$ causes capital-capacity elasticity divergences at $\mu = 1$.
- **Verdict:** The skill must be stripped of its "review" misnomer and redesigned into a canonical domain modeling skill: `heterodox-macro-modeling`.

### 6.3 Macro-Modeling Capability Envelope vs. Candidate Canon

The redesign in Wave D3 must lock the broad **capability envelope** while keeping specific mathematical traditions as candidate implementation content to be validated during D3.

#### Architectural Capability Envelope (Locked Scope)
1. **Accounting Consistency & Closures:** Formal mathematical specification of macroeconomic closures (distinguishing how saving, investment, capacity utilization, and distribution adjust across traditions).
2. **Dynamic Stability:** Analytical derivation of ODE systems, Jacobian matrices, local stability criteria, and bifurcation analyses.
3. **Equilibrium Concepts & The Traverse:** Distinguishing short-run adjustment, long-run normal positions, and the dynamic traverse between steady states.
4. **Demand-Led Growth & Distribution:** Analytics of distribution-growth interaction regimes and conflict inflation dynamics.
5. **Technical Change:** Direction of technical bias (Marx-biased, Harrod-neutral) and induced innovation.
6. **Stock-Flow Consistency (SFC):** Balance-sheet matrices, transaction-flow accounting, sectoral financial balances, and flow-stock integration.
7. **Center–Periphery & Open-Economy Extensions:** Balance-of-payments constrained growth, structuralist external debt dynamics, foreign exchange constraints.

*(Note: Specific models and theorems—e.g. Bhaduri–Marglin, Goodwin growth cycles, Thirlwall's law, Routh-Hurwitz conditions, Hopf bifurcations, Sraffian Supermultiplier formulations—represent **CANDIDATE IMPLEMENTATION CONTENT — TO BE VALIDATED IN D3** and are not frozen as a mandatory canon in D0).*

### 6.4 Stock-Flow Consistency (SFC) Ownership

- **Substantive Scope:** Balance sheets, transaction-flow matrices, sectoral balances ($\text{Private} + \text{Government} + \text{Foreign} \equiv 0$), and dynamic asset accumulation.
- **Architectural Owner:** **Canonical Domain Skill: `heterodox-macro-modeling`**.
  - *Rationale:* In modern Post-Keynesian macroeconomics (Godley & Lavoie 2007), SFC modeling is a foundational behavioral and structural modeling methodology. It belongs canonically inside `heterodox-macro-modeling`.
  - *Deterministic Tooling Disposition:* `DEFER TOOL CREATION PENDING DEMONSTRATED NEED`. First establish the analytical SFC modeling capability in D3. A deterministic arithmetic checker script (`tools/macro/sfc_consistency_check.py`) should be implemented only if D3/D5 demonstrates a recurring, specifiable arithmetic operation that benefits from extraction.

---

## 7. REDUNDANCY MATRIX

This matrix analyzes all potentially overlapping pairs across the repository to determine their correct architectural relationship.

Categories used:
- `NO OVERLAP`: Distinct intellectual capabilities with clear boundaries.
- `LEGITIMATE COMPOSITION`: Primary owner delegates or consumes supporting capability through explicit contract.
- `PARTIAL DUPLICATION`: Overlapping instructions or checks requiring extraction/consolidation.
- `OWNERSHIP CONFLICT`: Direct competition for canonical ownership requiring strict boundary enforcement.

| Component Pair | Evaluation Category | Repository Reality & Analysis | Correct Architectural Boundary |
|:---|:---|:---|:---|
| `deep-research` vs. `political-economy-research` | `NO OVERLAP` (with clear boundary) | `deep-research` conducts systematic literature searches, queries external academic databases (Crossref, OpenAlex, Semantic Scholar), and compiles PRISMA reports. It does not perform historical process tracing, construct periodizations, or evaluate comparative-relational mechanisms. | `deep-research` owns evidence retrieval and literature mapping. `political-economy-research` owns comparative-historical causal explanation. |
| `academic-paper` vs. `econ-write` | `LEGITIMATE COMPOSITION` | Locked in Wave B1. `academic-paper` is the sole owner of the multi-agent paper lifecycle and document state machine. `econ-write` owns economics disciplinary writing conventions (BLUF, triangular style, model exposition, identification rhetoric). | Bounded economics writing invokes `econ-write` directly. Full economics manuscripts invoke `academic-paper`, which consumes `econ-write` for disciplinary policy. |
| `academic-paper-reviewer` vs. `political-economy-research` | `NO OVERLAP` | `academic-paper-reviewer` is the sole owner of simulated external peer review, referee reports, and editorial decision letters. `political-economy-research` is an author-side research methodology skill. | `academic-paper-reviewer` evaluates manuscripts (including PE manuscripts, consuming domain standards); `political-economy-research` drafts or structures the qualitative research design. |
| `umass-applied-econometrics` vs. `heterodox-macro-modeling` | `NO OVERLAP` | `umass-applied-econometrics` owns empirical time-series econometrics (cointegration, VECM, Toda–Yamamoto, bootstrapping). `heterodox-macro-modeling` owns theoretical mathematical modeling (ODEs, closures, dynamic stability, SFC). | Econometrics tests empirical hypotheses and estimates time-series parameters; macro-modeling derives theoretical models and stability conditions. They compose when testing theoretical restrictions empirically. |
| `umass-applied-econometrics` vs. `political-economy-research` | `LEGITIMATE COMPOSITION` | `umass-applied-econometrics` handles quantitative time-series data. `political-economy-research` handles qualitative historical evidence and process tracing. They intersect at structural breaks and institutional periodization. | Econometrics provides statistical break diagnostics and time-series precedence; `political-economy-research` provides the institutional and historical mechanism explaining the break. |
| `heterodox-macro-modeling` vs. `political-economy-research` | `LEGITIMATE COMPOSITION` | `heterodox-macro-modeling` owns formal mathematical macro representation (equations, closures, dynamics, stability). `political-economy-research` owns comparative-historical and institutional explanation (historical sequences, state transformation, coalitions, relational dependence). | Macro-modeling formalizes the analytical dynamic system; `political-economy-research` explains the historical and institutional forces that generate, sustain, or disrupt the macroeconomic regime. They compose cleanly in mixed-methods projects. Neither absorbs the other. |
| `deep-research` vs. `historical-source-criticism` | `LEGITIMATE COMPOSITION` | `deep-research` currently uses a clinical/biomedical evidence hierarchy that misgrades historical archives. A shared source criticism protocol supplies the claim-relative evidential standard for non-biomedical historical records. | `shared/protocols/historical_source_criticism_protocol.md` sets the claim-relative evidential rules. `deep-research` applies them conditionally when verifying historical/documentary citations. |
| `heterodox-macro-modeling` vs. `process-tracing` | `NO OVERLAP` | Macro-modeling analyzes formal mathematical dynamic systems ($d\mu/dt$, Jacobian matrices). Process tracing analyzes empirical historical event sequences in political economy. | Formal mathematical deduction vs. qualitative empirical mechanism tracing. Complementary in mixed-methods projects; distinct canonical capabilities. |
| `editor-jacobin-lat` vs. `public-scholarship` | `PARTIAL DUPLICATION` | `editor-jacobin-lat` currently bundles generic public scholarship translation (de-specialization, accessible hooks) with Jacobin América Latina house style. | Generic public scholarship translation belongs in a reusable skill (`public-scholarship`); Jacobin house style belongs in a venue profile (`profiles/venues/jacobin-lat.md`). Decomposition deferred beyond Wave D/F (DEFERRED — FUTURE AUTHORIZATION REQUIRED). |

---

## 8. ROUTING BOUNDARY MATRIX & THOUGHT TESTS

To stress-test boundaries and expose ambiguities, the following 12 adversarial prompt scenarios were audited against repository evidence.

| # | Prompt Scenario | Primary Canonical Owner | Allowed Supporting Components | Forbidden Competing Owners | Rationale & Repository Evidence |
|:---|:---|:---|:---|:---|:---|
| 1 | *"Find archival evidence about copper negotiations."* | `deep-research` | `shared/protocols/historical_source_criticism_protocol.md` | `political-economy-research`, `academic-paper` | Evidence discovery and source retrieval belongs to `deep-research`. The candidate PE skill does not replace the search engine. |
| 2 | *"Assess whether these archival records support the proposed political mechanism."* | `political-economy-research` | `shared/protocols/historical_source_criticism_protocol.md`, `deep-research` (if search needed) | `academic-paper-reviewer`, `econ-write` | Evaluating whether qualitative archival evidence confirms a causal mechanism is the core task of qualitative process tracing. It is author-side research, not journal peer review. |
| 3 | *"Compare Chile and the United States as relationally connected accumulation regimes."* | `political-economy-research` | `heterodox-macro-modeling` (if formal open-economy equations are invoked) | `umass-applied-econometrics`, `academic-paper`, scholar profiles | Comparative-relational analysis and center–periphery external constraints belong to the PE methodology skill. Scholar profiles (`kevin-young.md`) are calibration inputs, not methodology providers. |
| 4 | *"Explain whether this historical sequence supports mechanism A rather than mechanism B."* | `political-economy-research` | `shared/protocols/historical_source_criticism_protocol.md` | `deep-research`, `academic-paper-reviewer`, `umass-applied-econometrics` | Discriminating between rival mechanisms using historical sequence evidence and CPOs is the exact definition of process tracing. |
| 5 | *"Derive the stability conditions of this demand-led growth model."* | `heterodox-macro-modeling` | None (pure domain skill derivation) | `umass-applied-econometrics`, `econ-write`, `heterodox-economics-review`, scholar profiles | Formal mathematical derivation of ODE stability, Jacobian matrices, and equilibrium conditions belongs to macro modeling. Scholar profiles (`deepankar-basu.md`) do not own derivation. |
| 6 | *"Check whether this stock-flow model closes consistently."* | `heterodox-macro-modeling` | None (analytical check; tool deferred) | `academic-paper-reviewer`, `umass-applied-econometrics` | Sectoral balance sheets, transaction-flow accounting, and stock-flow consistency are theoretical macro modeling capabilities. |
| 7 | *"Determine whether these series are admissible in an I(1) cointegration system."* | `umass-applied-econometrics` (future: `applied-econometrics-pe`) | Internal cointegration specification protocol | `heterodox-macro-modeling`, `political-economy-research` | Empirical time-series integration order governance (ADF/KPSS gates, collinearity screening) is owned by applied econometrics. |
| 8 | *"Run the Toda–Yamamoto specification audit."* | `umass-applied-econometrics` (future: `applied-econometrics-pe`) | Internal Toda-Yamamoto specification protocol | `econ-write`, `academic-paper` | Toda–Yamamoto $(k+d_{\max})$ specification mapping is a methodological protocol owned by applied econometrics. |
| 9 | *"Interpret this estimated coefficient through dependency theory."* | `political-economy-research` | `umass-applied-econometrics`, `econ-write` | `academic-paper-reviewer` | Conditioning the substantive interpretation of an empirical parameter on center–periphery structural relations belongs to political economy reasoning. |
| 10 | *"Rewrite this economics results section."* | `econ-write` | `shared/protocols/prose_discipline_protocol.md` | `academic-paper`, `umass-applied-econometrics` | Bounded economics prose and section drafting belongs directly to `econ-write`. |
| 11 | *"Review this paper as if for a journal."* | `academic-paper-reviewer` | Relevant domain profiles (`profiles/scholars/*`, `profiles/committees/*`) | `academic-paper`, `econ-write`, `heterodox-economics-review` | Simulated external peer review, referee reports, and editorial decision letters are the strict monopoly of `academic-paper-reviewer`. |
| 12 | *"Turn this economics paper into a Jacobin-style public article."* | `editor-jacobin-lat` (deferred beyond Wave D/F: `public-scholarship` + `profiles/venues/jacobin-lat.md`) | `econ-write` | `academic-paper`, `academic-pipeline` | Public scholarship translation and venue-specific op-ed editing. |

---

## 9. CANDIDATE WAVE-D ARCHITECTURE (LOGICAL TARGET)

The following diagram depicts the **logical target architecture** for the domain layer following Wave D.

> ⚠️ **CRITICAL RUNTIME REMINDER:**<br>
> This tree represents logical ownership and future Wave F organization. During Wave D, runtime execution remains strictly bound to root directories and existing extracted substrates per the locked runtime path rule. Physical moves into `skills/domain/` or `tools/econometrics/` are strictly deferred to Wave F.

```text
===============================================================================
                     LOGICAL TARGET ARCHITECTURE (WAVE D)
===============================================================================

CORE REASONING (Locked - Waves A-C)
├── deep-research                     [Universal literature search & PRISMA synthesis]
├── academic-paper                    [Generic manuscript lifecycle & drafting state machine]
└── academic-paper-reviewer           [Sole canonical owner of simulated external peer review]

CONTROL PLANE (Locked - Waves A-C)
└── academic-pipeline                 [Orchestrator only; workflow state & Material Passport]

DOMAIN INTELLECTUAL CAPABILITIES (Wave D Focus)
├── econ-write                        [Economics prose standards, BLUF, model/results rhetoric]
├── applied-econometrics-pe           [Applied time-series econometrics in PE; forensic rigor;
│                                      integration order governance; Toda-Yamamoto; bootstrap]
├── heterodox-macro-modeling          [Mathematical & dynamical macro consistency; Keynesian/
│                                      Kaleckian/Marxian/Sraffian closures; stability; SFC]
└── political-economy-research        [Comparative-historical PE methodology; periodization;
                                       process tracing; CPOs; comparative-relational analysis]

DISSEMINATION (DEFERRED — FUTURE AUTHORIZATION REQUIRED)
├── econ-slides                       [Scholarly Beamer presentation slide decks]
└── public-scholarship                [Generic public translation; decomposes editor-jacobin-lat]

SHARED PROTOCOLS & CONTRACTS
├── shared/protocols/
│   ├── prose_discipline_protocol.md  [Category A/B/C prose discipline & verb calibration]
│   └── historical_source_criticism_protocol.md [Claim-relative archival & documentary evaluation]
└── shared/contracts/passport/
    └── EDITORIAL_GOVERNANCE_PORT.md  [Change-control verification port; revision_guard.py]

METHODOLOGICAL SPECIFICATION PROTOCOLS (Internal to applied-econometrics-pe; FUTURE WAVE-F TARGET: tools/econometrics/)
├── cointegration_audit.md            [Methodological cointegration specification protocol]
└── toda_yamamoto.md                  [Methodological Toda-Yamamoto lag grid mapping protocol]

DETERMINISTIC TOOLS (Locked / Pre-existing)
└── tools/prose_checks/
    └── check_prose_patterns.py       [Deterministic regex prose scanning]

PROFILE CALIBRATION LAYER (Locked - Wave C)
├── profiles/scholars/                [Durable scholar priors: Michael Ash, Basu, Young]
├── profiles/advisors/                [Active advisor roles: Michael Ash]
└── profiles/committees/              [Committee compositions: UMass PE]
```

---

## 10. CANDIDATE COMPONENTS (PROPOSED — NOT AUTHORIZED)

In strict compliance with Operating Doctrine §10, every proposed component is documented below. None are authorized for creation during Wave D0.

```text
CANDIDATE COMPONENT:
skills/domain/political-economy-research (runtime: political-economy-research)

PROPOSED TYPE:
skill (Domain Skill)

PROPOSED OWNER / ROLE:
Canonical domain owner of comparative-historical political economy methodology, process tracing, historical periodization, causal-process observation (CPO) analysis, rival mechanism discrimination, and comparative-relational explanation.

EVIDENCE OF NEED:
Completely absent from the live repository. Audited in docs/design/2026-10-11-ars-target-architecture/04_CAPABILITY_REDUNDANCY_AUDIT.md lines 156-162 (G01, G03, G04, G06, G07). Current repository has zero capability to guide qualitative research, trace historical mechanisms, or conduct relational comparisons.

CURRENT DUPLICATION:
No current owner exists. Capability is registered as unowned candidate in docs/governance/ars_registry.yaml line 504. Dispersed fragments exist only as review comments in profiles/scholars/kevin-young.md and op-ed rhetoric in editor-jacobin-lat.

WHY EXISTING COMPONENTS CANNOT OWN THIS CLEANLY:
- academic-paper owns manuscript structuring, not qualitative causal inference.
- deep-research owns bibliographic search, not historical process tracing.
- econ-write owns prose standards and microeconometric causal language, not historical methodology.
- umass-applied-econometrics owns quantitative time-series models, not qualitative process tracing.
Forcing this into any existing skill violates the single capability ownership invariant.

EXPECTED CONSUMERS:
- academic-paper (when drafting historical or political economy sections)
- academic-paper-reviewer (when evaluating comparative-historical qualitative papers)
- academic-pipeline (during Stage 1/2 of political economy workflows)

STATUS:
PROPOSED — NOT AUTHORIZED
```

```text
CANDIDATE COMPONENT:
shared/protocols/historical_source_criticism_protocol.md

PROPOSED TYPE:
protocol (Shared Cross-Domain Protocol)

PROPOSED OWNER / ROLE:
Canonical cross-domain standard for evaluating historical, archival, documentary, and institutional evidence relative to specific asserted claims (provenance, institutional standpoint, incentives for candor vs concealment, temporal proximity, contemporaneous vs retrospective construction, archival silence, and triangulation).

EVIDENCE OF NEED:
deep-research/references/source_quality_hierarchy.md relies on a biomedical/clinical pyramid that represents a coverage gap and domain mismatch for archival sources. prose_discipline_protocol.md lines 127 and 137 recognizes historical evidence but explicitly disclaims substantive evaluation.

CURRENT DUPLICATION:
None. Currently completely missing.

WHY EXISTING COMPONENTS CANNOT OWN THIS CLEANLY:
Multiple skills (deep-research, political-economy-research, academic-paper, academic-paper-reviewer) must evaluate historical sources. If placed inside political-economy-research, deep-research would have to import domain-specific logic to verify archival citations. A shared protocol with conditional activation provides a decoupled, neutral standard.

EXPECTED CONSUMERS:
- political-economy-research
- deep-research (source_verification_agent)
- academic-paper-reviewer
- academic-paper

STATUS:
PROPOSED — NOT AUTHORIZED
```

```text
CANDIDATE COMPONENT:
skills/domain/applied-econometrics-pe (runtime: umass-applied-econometrics refactored)

PROPOSED TYPE:
skill (Domain Skill Refactor)

PROPOSED OWNER / ROLE:
Authoritative domain skill for applied time-series econometrics in political economy, forensic replication, integration order governance, small-sample bootstrapping, and data-first visualization.

EVIDENCE OF NEED:
Live umass-applied-econometrics/SKILL.md contains high-value econometrics but suffers from critical epistemic defect in Rule 2.H.4 (forcing failed cointegration to mean regime switching) and heavy prose duplication with econ-write in Section 1.

CURRENT DUPLICATION:
Duplicated prose in lines 16-24 with econ-write and prose_discipline_protocol.

WHY EXISTING COMPONENTS CANNOT OWN THIS CLEANLY:
econ-write owns general economics writing, not advanced time-series VECM and cointegration diagnostics.

EXPECTED CONSUMERS:
- academic-paper
- academic-paper-reviewer
- doctoral researchers

STATUS:
PROPOSED — NOT AUTHORIZED
```

```text
CANDIDATE COMPONENT:
skills/domain/heterodox-macro-modeling (runtime: heterodox-economics-review redesigned)

PROPOSED TYPE:
skill (Domain Skill Redesign)

PROPOSED OWNER / ROLE:
Canonical domain skill for mathematical and dynamical macroeconomics in Post-Keynesian, Marxian, Sraffian, and structuralist traditions; macroeconomic closures; dynamic stability; stock-flow consistency.

EVIDENCE OF NEED:
heterodox-economics-review/SKILL.md is a 29-line project fragment for SSM singularities. It lacks coverage of closures, general ODE stability, SFC, and distribution-growth regimes.

CURRENT DUPLICATION:
Name conflicts with academic-paper-reviewer. Content is modeling, not review.

WHY EXISTING COMPONENTS CANNOT OWN THIS CLEANLY:
academic-paper-reviewer owns peer review, not mathematical modeling. No other component owns theoretical macroeconomic systems.

EXPECTED CONSUMERS:
- academic-paper
- academic-paper-reviewer

STATUS:
PROPOSED — NOT AUTHORIZED
```

```text
CANDIDATE COMPONENT:
references/econometrics/cointegration_audit.md (FUTURE WAVE-F TARGET PATH: tools/econometrics/cointegration_audit.md)

PROPOSED TYPE:
protocol (Methodological Specification Protocol)

PROPOSED OWNER / ROLE:
Methodological diagnostic protocol for testing stochastic vs theoretical admissibility of candidate regressors, collinearity filtering, and VECM rank. Owned canonically by applied-econometrics-pe.

EVIDENCE OF NEED:
Currently located at umass-applied-econometrics/tools/cointegration_specification_audit.md. Requires clarification that it is a methodological reasoning protocol, not an executable deterministic tool.

CURRENT DUPLICATION:
Embedded in skill directory.

WHY EXISTING COMPONENTS CANNOT OWN THIS CLEANLY:
Belongs canonically to applied-econometrics-pe as a domain methodological reference. Physical file relocation to tools/ is deferred to Wave F.

EXPECTED CONSUMERS:
- applied-econometrics-pe
- academic-paper-reviewer

STATUS:
PROPOSED — NOT AUTHORIZED
```

```text
CANDIDATE COMPONENT:
references/econometrics/toda_yamamoto.md (FUTURE WAVE-F TARGET PATH: tools/econometrics/toda_yamamoto.md)

PROPOSED TYPE:
protocol (Methodological Specification Protocol)

PROPOSED OWNER / ROLE:
Methodological diagnostic protocol for Toda–Yamamoto (1995) levels-augmented (k + d_max) VAR lag selection grid mapping and Modified Wald test reporting. Owned canonically by applied-econometrics-pe.

EVIDENCE OF NEED:
Currently located at umass-applied-econometrics/tools/toda_yamamoto_specification_mapping.md. Requires clarification that it is a methodological reasoning protocol, not an executable deterministic tool.

CURRENT DUPLICATION:
Embedded in skill directory.

WHY EXISTING COMPONENTS CANNOT OWN THIS CLEANLY:
Belongs canonically to applied-econometrics-pe as a domain methodological reference. Physical file relocation to tools/ is deferred to Wave F.

EXPECTED CONSUMERS:
- applied-econometrics-pe
- academic-paper-reviewer

STATUS:
PROPOSED — NOT AUTHORIZED
```

---

## 11. RESTORED GOVERNING D1–D6 IMPLEMENTATION SEQUENCE

To implement the target domain architecture cleanly without regressions, epistemic leakage, or topology violations, the governing sequence established post-Wave-C is restored.

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ D1: Political-Economy Ownership & Capability Design                     │
│     - Define precise capability contract for political-economy-research │
│     - Scope boundaries with deep-research, econometrics, macro, review  │
│     - Establish capability envelope (periodization, process tracing,    │
│       CPOs, rival mechanisms, negative evidence, relational comparison) │
│     - Validate candidate implementation content boundaries              │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ D2: Applied-Econometrics Decomposition / Theory -> Empirics Boundary   │
│     - Epistemic purge of forced regime-switching rule H.4               │
│     - Demote hardcoded Fordist thresholds (H.2) to illustrative examples│
│     - Deduplicate prose rules (Section 1) and writing checklist items   │
│     - Clarify specification protocols as methodological references      │
│       (no physical relocation; Wave F preserves topology)               │
│     - Retain all forensic methods, integration order, and bootstrap     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ D3: Heterodox Macro-Modeling Architecture                              │
│     - Redesign heterodox-economics-review -> heterodox-macro-modeling   │
│     - Expand from 29 lines to formal modeling capability envelope       │
│     - Codify closures (Keynesian, Kaleckian, Marxian, Sraffian)         │
│     - Codify dynamic ODE stability (Jacobian, Routh-Hurwitz, Hopf)      │
│     - Codify Stock-Flow Consistency (SFC) principles & balance sheets   │
│     - Preserve valid singularity & boundary checks                      │
│     - Defer deterministic SFC tool creation pending demonstrated need   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ D4: Historical Source Criticism Protocol & PE Implementation            │
│     - Author shared/protocols/historical_source_criticism_protocol.md   │
│     - Codify claim-relative evaluation (provenance, standpoint, bias,   │
│       temporal proximity, candor incentives, archival silence)          │
│     - Implement political-economy-research skill                        │
│     - Connect protocol to deep-research via conditional activation      │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ D5: Adversarial Integration & Evals                                     │
│     - Add routing cases to evals/gold/routing/cases.yaml                │
│     - Add epistemic neutrality gold eval case                           │
│     - Add claim-relative historical source criticism gold eval cases    │
│     - Verify non-overlap and correct cross-skill composition            │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ D6: Domain Governance Reconciliation & Regression Lock                 │
│     - Update docs/governance/ars_registry.yaml to v1.2.0                │
│     - Update docs/governance/ROUTING_AND_PRECEDENCE.md                  │
│     - Implement scripts/test_wave_d_reconciliation.py                   │
│     - Lock Wave D state with full CI and regression suite pass          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 12. ADVERSARIAL EVAL PLAN

To verify the integrity of the proposed Wave D architecture and ensure that new components do not cause regressions, the following evaluation harness must be implemented during Wave D.

### 12.1 Non-Overlap & Routing Evals

Add 6 new adversarial cases to `evals/gold/routing/cases.yaml`:

1. `ROUTE-018 (ADV-D1: Process Tracing vs. Econometrics):`
   - *Prompt:* "Trace the political and institutional sequence of events that led to the 1982 debt crisis in Mexico."
   - *Target:* `political-economy-research`.
   - *Forbidden:* `umass-applied-econometrics`, `academic-paper`.
2. `ROUTE-019 (ADV-D2: Macro Stability vs. Peer Review):`
   - *Prompt:* "Check whether this 3-equation Post-Keynesian growth model satisfies the Routh-Hurwitz stability conditions."
   - *Target:* `heterodox-macro-modeling`.
   - *Forbidden:* `academic-paper-reviewer`, `umass-applied-econometrics`.
3. `ROUTE-020 (ADV-D3: Archival Fact-Check vs. Process Tracing):`
   - *Prompt:* "Find and verify the official minutes of the 1971 Bretton Woods suspension meeting."
   - *Target:* `deep-research` consuming `shared/protocols/historical_source_criticism_protocol.md`.
   - *Forbidden:* `political-economy-research`.
4. `ROUTE-021 (ADV-D4: Toda-Yamamoto Specification vs. Writing):`
   - *Prompt:* "Generate the (k + d_max) Toda-Yamamoto lag specification grid for GDP and wage share."
   - *Target:* `umass-applied-econometrics` (future: `applied-econometrics-pe`).
   - *Forbidden:* `econ-write`.
5. `ROUTE-022 (ADV-D5: SFC Matrix Consistency vs. Review):`
   - *Prompt:* "Verify that the sectoral transaction-flow matrix of this macro model satisfies accounting closure."
   - *Target:* `heterodox-macro-modeling`.
   - *Forbidden:* `academic-paper-reviewer`.
6. `ROUTE-023 (ADV-D6: Relational Comparison vs. Parallel Description):`
   - *Prompt:* "Analyze how US interest rate hikes relationally constrain industrial policy in Brazil."
   - *Target:* `political-economy-research`.
   - *Forbidden:* `academic-paper`, `econ-write`.

### 12.2 Epistemic Safeguard Evals (Layer Distinction Enforced)

1. **Deterministic Static Regression Check (Unit Test in `scripts/test_wave_d_reconciliation.py`):**
   - Scans `umass-applied-econometrics/SKILL.md` (and future `applied-econometrics-pe/SKILL.md`) to verify that the prohibited Rule 2.H.4 string *"interpret failures to cointegrate as evidence of structural regime-switching"* is completely absent.
2. **Model-Behavior Eval Case (`evals/gold/econometrics/cointegration_nonfinding.yaml`):**
   - Feeds a synthetic dataset with confirmed non-cointegration ($p > 0.50$ across all rank and residual tests).
   - Verifies that the model outputs an empirical non-finding and does not assert that the rejection proves FX-constrained regime-switching.

### 12.3 Claim-Relative Historical Source Criticism Evals

Implement in `evals/gold/historical_sources/`:
- **Case 1 (Contemporaneous Diplomatic Cable vs. Retrospective Memoir):**
  - *Setup:* A 1973 diplomatic cable from an embassy stating "Ministers are reportedly divided over currency policy" versus a 1995 memoir by the Finance Minister stating "I was completely unified with the President on currency policy."
  - *Evaluation Criteria:* The evaluator must **not** assign a crude categorical grade ("cable > memoir"). Instead, it must identify the claim each source can support:
    - The cable is strong evidence for *what outside observers and diplomats believed and reported at the time*, but weak evidence for internal cabinet unity.
    - The memoir is evidence of *the minister's retrospective public framing*, but subject to retrospective justification bias regarding contemporaneous division.
    - The evaluator must assess source-specific risks and calibrate claim strength accordingly.
- **Case 2 (Archival Silence in Corporate Board Records):**
  - *Setup:* Board minutes containing zero discussion of union organizing during a major strike wave.
  - *Evaluation Criteria:* The evaluator identifies the archival silence, noting that absence of record in official minutes does not support a claim that leadership was unconcerned; rather, it indicates informal decision-making or deliberate exclusion from official records.

---

## 13. LOCK CONFLICTS AND UNRESOLVED QUESTIONS

### 13.1 Confirmed Defects & Coverage Gaps

1. **Epistemic Inversion in `umass-applied-econometrics` §2.H.4:**
   - *Classification:* `CONFIRMED DEFECT`.
   - *Evidence:* Line 70 mandates interpreting cointegration failures as regime-switching, violating the locked invariant that theory expands hypotheses but does not dictate empirical outcomes.
2. **Prose Duplication in `umass-applied-econometrics` §1 and §3:**
   - *Classification:* `CONFIRMED DEFECT`.
   - *Evidence:* Lines 16–24 and lines 96–98 duplicate `econ-write` prose rules.
3. **Severe Under-Specification of `heterodox-economics-review`:**
   - *Classification:* `CONFIRMED DEFECT`.
   - *Evidence:* 29 lines focused exclusively on one paper's SSM singularity, misnamed as a "review" skill.
4. **Coverage Gap / Domain-Mismatch Risk in `deep-research`:**
   - *Classification:* `CONFIRMED COVERAGE GAP / DOMAIN-MISMATCH RISK`.
   - *Evidence:* `deep-research/references/source_quality_hierarchy.md` is structured for clinical/biomedical trials and lacks an evidential model for primary historical and documentary sources.

### 13.2 Architecture Status & Document Inconsistencies

- **LIVE-ARCHITECTURE LOCK CONFLICT: none detected.**
  All existing locked post-Wave-C structures (`academic-paper-reviewer` sole peer review monopoly, `academic-pipeline` orchestration only, `prose-discipline` shared protocol, `editorial-governance` change-control only, profile extractions, and deprecated compatibility stubs) are completely respected by the live repository. The 11/11 assertions in `scripts/test_wave_c_reconciliation.py` continue to pass cleanly.
- **GOVERNING-DOCUMENT TIMING INCONSISTENCY: public-scholarship decomposition.**
  - *The Inconsistency:* The target blueprint (`00_TARGET_STATE_ARCHITECTURE.md` §6, `05_TARGET_MIGRATION_ROADMAP.md` Wave E) classifies public-scholarship decomposition as a target condition / Wave E milestone. However, the post-Wave-C restart handoff places public-scholarship decomposition under work deferred beyond Wave D/F.
  - *Resolution for D0:* Public-scholarship decomposition is treated as `DEFERRED — FUTURE AUTHORIZATION REQUIRED`. No unauthorized Wave E ontology is created. The target-completion documentation will require reconciliation in a future governance update.

### 13.3 Architectural Decisions Recorded

1. **Packaging of Historical Source Criticism:** Provisionally approve Option A with conditional activation (`shared/protocols/historical_source_criticism_protocol.md` activated when documentary/archival sources are present).
2. **Scope of `political-economy-research`:** Approved as Option A (primarily a research methodology capability, not an exhaustive encyclopedia of political economy doctrines).
3. **SFC Tooling:** `DEFER TOOL CREATION PENDING DEMONSTRATED NEED`. First implement the analytical modeling capability in D3; create a deterministic arithmetic checker only if a recurring specifiable operation demonstrates need.
4. **Public Scholarship Decomposition:** Deferred beyond Wave D/F per restart handoff.

---

## 14. REVISED D1 AUTHORIZATION RECOMMENDATION

To authorize the commencement of Wave D implementation, the following concise decision package is recommended for human decision lock:

1. **Authorize Wave D1 Execution Exclusively:**
   Authorize the execution of **Wave D1: Political-Economy Capability Ownership Design**.
2. **Bind Core Architectural Constraints for D1:**
   - Confirm the four-domain logical target:
     - `econ-write`
     - `applied-econometrics-pe`
     - `heterodox-macro-modeling`
     - `political-economy-research`
   - Confirm that `political-economy-research` is justified as the canonical owner of comparative-historical PE methodology.
   - Confirm that its scope is primarily methodological (process tracing, periodization, relational comparison, source-based causal inference) rather than a universal theory encyclopedia.
   - Enforce strict boundaries keeping `political-economy-research` distinct from `deep-research` (literature search), econometric identification, formal macro-modeling, manuscript writing, and external peer review.
   - Provisionally approve `shared/protocols/historical_source_criticism_protocol.md` as a cross-domain shared protocol with conditional activation, subject to claim-relative evidentiary design.
   - Reaffirm that physical repository migration remains Wave F work; no directory moves will occur in Wave D.
3. **Withhold Wave D2–D6 Execution Authority:**
   Explicitly withhold implementation authority for D2 econometrics edits, D2 protocol extractions, D3 macro modeling expansion, D4 protocol coding, and D5/D6 evals/locks until D1 is complete and approved.
