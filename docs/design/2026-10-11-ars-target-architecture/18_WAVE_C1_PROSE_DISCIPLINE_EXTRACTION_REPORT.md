# ARS Wave C1 Prose Discipline Extraction Report

**Document ID:** `18_WAVE_C1_PROSE_DISCIPLINE_EXTRACTION_REPORT.md`
**Status:** IMPLEMENTED SPECIFICATION & EXTRACTION REPORT (Wave C1)
**Date:** 2026-10-12
**Baseline Git Commit:** `a433dcf`
**Subwave:** Wave C1 (Shared Prose Discipline Protocol & Deterministic Tool Extraction)
**Execution Authority:** Implementation pass authorized by Wave C0.1 decision lock.

---

## 1. Baseline

Wave C1 extraction is anchored strictly to baseline commit `a433dcf`:
- `63f7b33`: Freeze ARS target architecture and Wave A repository baseline
- `06b46b3`: feat(governance): establish integrated ARS registry (Wave B0)
- `8bdc0df`: docs(econ-write): add evaluation examples and ranked sources
- `a87e8b2`: feat(routing): enforce ARS capability precedence (Wave B1)
- `a797db9`: test(routing): add adversarial precedence cases (Wave B1.1)
- `1b94bfb`: docs(architecture): design Wave C legacy decomposition (Wave C0)
- `a433dcf`: docs(architecture): lock Wave C decisions and workspace model (Wave C0.1)

---

## 2. Legacy Source Inspected

The extraction process fully audited the legacy component:
- **Component Path:** `prose-register-critic/`
- **Core File:** `prose-register-critic/SKILL.md` (148 lines)
- **Declared Legacy Scope:** AI-trace lexical discipline auditor, jargon checker, 11 pattern families, 3-tier classification, and phantom script references (`check_jargon_leakage.py`).
- **Legacy Preservation Status:** In accordance with the `MIGRATE_FIRST` rule, `prose-register-critic/` remains 100% unchanged during Wave C1. Formal deprecation is scheduled for Subwave C5.

---

## 3. Extraction Methodology

The extraction decoupled substantive editorial value from AI-detector heuristics using a strict functional classification ledger:

1. **`SHARED_PROTOCOL`:** Cross-domain editorial standards, Category A/B/C definitions, claim-strength verb discipline, and diagnostic pattern families extracted to `shared/protocols/prose_discipline_protocol.md`.
2. **`DETERMINISTIC_TOOL`:** Mechanical, reproducible pattern checks extracted to `tools/prose_checks/check_prose_patterns.py`.
3. **`DOMAIN_RESERVATION`:** Economics-specific conventions and causal identification standards explicitly reserved to `econ-write`.
4. **`LIFECYCLE_RESERVATION`:** Universal manuscript structure and authoring state machines reserved to `academic-paper`.
5. **`REVIEW_RESERVATION`:** Referee simulation and editorial decision letters reserved to `academic-paper-reviewer`.
6. **`REJECTED_HEURISTIC`:** AI-authorship classification, machine cadence probability scoring, and uncalibrated dynamic blacklists purged.

---

## 4. Preserved Shared Capabilities

The following capabilities were extracted into the canonical shared protocol ([`prose_discipline_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/prose_discipline_protocol.md)):

- **The Core Invariant:** "Technical language is not guilty by association."
- **Three-Tier Terminology Taxonomy:**
  - *Category A (Protected Technical):* Theoretical and empirical concepts (`supermultiplier`, `eigenvalues`, `rate of exploitation`, `Johansen trace test`) immune from deletion or generic simplification.
  - *Category B (Review in Context):* Legitimate disciplinary terms (`under an unbalanced growth closure`, `transmission mechanism`) edited only when conspicuously clustered.
  - *Category C (Replaceable Scaffolding):* Vacuous intensifiers, branded metaphors, and pipeline labels (`empirical tournament`, `admissibility gates`, `crucially`) targeted for direct simplification.
- **Evidential Claim-Strength Verb Calibration:** Rigorous alignment of assertion verbs (`documents`, `shows`, `predicts`, `estimates cointegrating vector`) with empirical research designs.
- **11 Auditing Pattern Families:** Cross-domain diagnostics covering syntactic monotony, sentence openings, canned transitions, contrast templates, abstraction stacking, nominalizations, adjective loading, triads, narrative templates, and metadata leaks.

---

## 5. Deterministic Checks Extracted

The deterministic Python utility ([`check_prose_patterns.py`](file:///c:/ReposGitHub/academic-research-skills/tools/prose_checks/check_prose_patterns.py)) implements six reproducible, offline checks:

1. **Category C Scaffolding & Branded Metaphors:** Matches exact phrases (`empirical tournament`, `admissibility gates`, `black-box screening protocol`, `deliberately stress test`, `profound institutional divergence`).
2. **Pipeline Metadata Leakage:** Identifies unescaped internal file paths in prose (`\texttt{output/...}`, `codes/...`, `scripts/...`).
3. **Canned Transition Clustering:** Flags paragraphs containing 2 or more formulaic transition adverbs (`Furthermore`, `Moreover`, `Additionally`, `In addition`, `Importantly`, `Crucially`).
4. **Contrast Template Repetition:** Flags paragraphs containing 2 or more binary contrast templates (`not X, but Y`, `rather than X, Y`, `far from X, Y`, `instead of X, Y`).
5. **Sentence-Start Repetition:** Flags 3 or more consecutive sentences beginning with identical tokens (e.g. `This... This... This...`).
6. **Evaluative Intensifier Clustering:** Flags paragraphs overloaded with 3 or more unearned intensifiers (`crucially`, `decisive`, `profound`, `stark`, `striking`, `dramatic`).

---

## 6. Judgmental Rules Retained as Protocol Only

Certain qualitative aspects of the legacy skill cannot be reliably determined by regex or syntactic parsers without unacceptably high false-positive rates. These remain codified as guidelines for human editors and drafting agents in the protocol:

- Assessing whether an abstract theoretical paragraph lacks sufficient empirical grounding (Family 6).
- Evaluating whether nominalization clusters impede readability (Family 7).
- Determining whether a three-part triad represents essential distinct analytical categories (Family 9).
- Evaluating paragraph narrative staging and cadence variation (Family 10 & 11).

---

## 7. Econ-Write-Owned Material Excluded

Wave C1 strictly avoided absorbing or duplicating economics-specific writing rules:
- Economics-specific structure (BLUF, triangular newspaper style, Bellemare intro formula) remains owned by `econ-write`.
- Econometric causal claim rhetoric (DiD, IV, RDD, RCT, controls, cluster robust SEs) remains owned by `econ-write`.
- Regression table formatting and coefficient magnitude reporting remains owned by `econ-write`.

---

## 8. Academic-Paper-Owned Material Excluded

Universal manuscript authoring responsibilities remain untouched:
- Overall manuscript architecture (IMRaD) and section sequencing.
- Multi-agent authoring pipeline (12-agent writing state machine).
- Citation extraction and bibliographic compliance checking.

---

## 9. Reviewer-Owned Material Excluded

Simulated peer review mechanics remain untouched:
- Generating 5-referee panels and Devil's Advocate challenges.
- Synthesizing formal Editorial Decision Letters (Accept / Minor / Major / Reject).
- Generating prioritized LaTeX revision roadmaps.

---

## 10. Rejected AI-Detector Heuristics

The following problematic features of the legacy design and external AI-detector tools were explicitly **REJECTED**:

1. **AI Authorship Inference:** Any claim to detect "machine cadence", "LLM-generated prose", or calculate synthetic probability scores.
2. **Dynamic Blacklist Snowball:** The legacy `prose_learning_ledger.json` persistent blacklist loop was rejected to prevent cumulative over-censorship.
3. **Rigid Sentence-Length Limits:** Universal rules banning sentences over a specific word threshold.
4. **Indiscriminate Vocabulary Banning:** Naive blacklists flagging standard academic words (`vernacular`, `rubric`, `plethora`) used in legitimate scholarly context.

---

## 11. False-Positive Safeguards

To prevent stylistic tools from disrupting valid scholarship:
- **Category A Immunity:** Recognized technical and mathematical terms are explicitly exempted from jargon alerts.
- **Conservative Thresholds:** Patterns are flagged only when clustered (e.g. $\ge 2$ canned transitions, $\ge 3$ consecutive identical openings).
- **Non-Blocking Severity:** All flags are emitted with severity `REVIEW` or `INFO`. The tool status is `PASS` or `REVIEW`; it never emits build-breaking `FAIL` statuses on stylistic diagnostics.

---

## 12. Gold Fixture Coverage

The test suite in [`evals/gold/prose_discipline/cases.yaml`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/prose_discipline/cases.yaml) covers 11 comprehensive fixtures:

| Case ID | Category | Description | Result |
| :--- | :--- | :--- | :--- |
| `CASE_A` | Clean Technical | Direct econometric description with zero flags | `PASS` (0 flags) |
| `CASE_B` | Category A Protection | Heterodox theoretical terms (`supermultiplier`, `rate of exploitation`) | `PASS` (0 flags, protected) |
| `CASE_C` | Contrast Repetition | Overuse of binary antithesis templates ($\ge 2$) | `REVIEW` (1 flag) |
| `CASE_D` | Sentence Openings | 3 consecutive sentences starting with "This" | `REVIEW` (1 flag) |
| `CASE_E` | Canned Transitions | Clustered adverbs (`Furthermore`, `Moreover`, `Additionally`) | `REVIEW` (1 flag) |
| `CASE_F` | Rhetorical Repetition | Stylistic repetition flagged as `REVIEW` without error | `REVIEW` (1 flag) |
| `CASE_G` | Economics Domain | Econometrics terminology (`difference-in-differences`, `parallel trends`) | `PASS` (0 flags, protected) |
| `CASE_H` | Political Economy | Interdisciplinary terms (`reserve army of labor`, `balance-of-payments`) | `PASS` (0 flags, protected) |
| `CASE_I` | Category C Scaffolding | Draft laden with tournament metaphors and workflow leaks | `REVIEW` (7 flags) |
| `CASE_J` | False-Positive Guard | Complex, sophisticated prose passing cleanly | `PASS` (0 flags) |
| `CASE_K` | AI Non-Inference | Verifies zero AI scoring or synthetic authorship classifiers | `PASS` (0 flags) |

---

## 13. Test Results

Execution of [`scripts/test_prose_discipline.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/test_prose_discipline.py):
- Protocol structure: **17/17 sections verified**.
- Offline independence: **Zero external/network dependencies**.
- AI non-inference: **Zero forbidden classification terms**.
- Gold fixtures: **11/11 cases passed**.
- Determinism: **100% byte-identical outputs across repeated runs**.

Existing repository governance tests:
- `scripts/validate_ars_registry.py`: **PASS** (14 components, 20 capabilities).
- `scripts/test_routing_contract.py`: **PASS** (17/17 routing cases).

---

## 14. Legacy Surface Status

- `prose-register-critic/SKILL.md`: Preserved completely intact and operational.
- Legacy directory is untouched, preventing any premature breaking changes or workflow disruption.

---

## 15. Ownership Status

- `docs/governance/ars_registry.yaml`: Untouched in Wave C1. Formal registration and deprecation are scheduled for Subwave C5.
- `docs/governance/ROUTING_AND_PRECEDENCE.md`: Untouched. Capability monopolies remain strictly preserved.

---

## 16. C1 Limitations

- `check_prose_patterns.py` is a syntactic and lexical diagnostic tool; it does not parse complex multi-clause sentence semantics or evaluate argument logic.
- Complex Category B phrasing requires human editorial discretion.

---

## 17. C2 Readiness

With the shared prose discipline protocol and deterministic tooling extracted, tested, and validated:
- Subwave C1 is **COMPLETE**.
- The repository is fully prepared for **Subwave C2** (Lightweight Editorial Governance & Material Passport Integration).
