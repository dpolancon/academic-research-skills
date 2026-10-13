# ARS Wave C1.1 — Prose Protocol Domain-Boundary Repair Report

**Date:** 2026-10-12
**Baseline Commit:** `42cf628` (`feat(prose): extract shared prose discipline protocol`)
**Mode:** Bounded Domain-Boundary Repair
**Target:** [`shared/protocols/prose_discipline_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/prose_discipline_protocol.md)
**Status:** COMPLETE — READY FOR WAVE C2

---

## 1. Baseline

Wave C1 extracted the shared prose discipline protocol and deterministic offline tool at commit `42cf628` (`feat(prose): extract shared prose discipline protocol`), resting on architecture lock baseline `a433dcf`.

---

## 2. Independent Audit Finding

An independent adversarial audit of Wave C1 evaluated commit `42cf628` across 26 verification checkpoints. The audit returned:

```
PROTOCOL ROLE:
CROSS_DOMAIN_SHARED_PROTOCOL

ECON-WRITE LEAKAGE:
MINOR_WORDING

C2 FOUNDATION:
READY_AFTER_BOUNDED_REPAIR

FINAL DECISION:
C1_REQUIRES_BOUNDED_REPAIR
```

The sole finding requiring repair was **`ECON-WRITE LEAKAGE: MINOR_WORDING`**, localized entirely within Section 8 of [`shared/protocols/prose_discipline_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/prose_discipline_protocol.md).

---

## 3. Exact Ownership Leak

In the original C1 extraction, Section 8 (*Claim-Strength Discipline*) structured its claim-verb calibration table around specific econometrics research designs and methodologies:
- Granger Causality / VAR / Predictive (`predicts`, `precedes conditionally`)
- Cointegration / Long-Run Relations (`identifies a long-run relation`, `rejects the zero-rank null hypothesis`)
- Impulse Responses (IRF / GIRF) (`conditional dynamic response`)
- Quasi-Experimental / Identification (`local average effect`, `parallel trends`)

While Section 5 affirmed that `econ-write` is the domain owner of economics writing, structuring the claim-strength table of a generic `CROSS_DOMAIN_SHARED_PROTOCOL` exclusively around econometric time-series and quasi-experimental techniques constituted a minor ownership leak into `econ-write`'s jurisdictional territory.

---

## 4. Repair Applied

Section 8 was completely rewritten to replace method-specific econometric terminology with generic, discipline-agnostic scientific research designs and evidentiary categories.

Specifically:
1. Removed all method-specific econometric designs (`VAR`, `cointegration`, `IRF`, `parallel trends`, `local average effect`, `zero-rank null hypothesis`).
2. Expanded research designs into six domain-agnostic foundations spanning quantitative, formal, archival, and observational scholarship.
3. Added an explicit **Domain-Delegation Boundary** sub-section formalizing the separation between linguistic claim calibration and substantive evidentiary entitlement.

---

## 5. Domain-Agnostic Claim-Strength Rule

The repaired protocol establishes the following universal principle:

> **The strength of a claim verb must not exceed the evidentiary entitlement provided by the research design, source base, formal derivation, or other discipline-appropriate warrant.**

### Evidentiary Entitlement and Calibrated Verb Hierarchy

| Research Design / Evidentiary Foundation | Calibrated Permissible Verbs | Forbidden Over-Claims |
| :--- | :--- | :--- |
| **Descriptive / Stylized Trends** | `documents`, `records`, `traces`, `summarizes`, `describes` | `proves`, `demonstrates conclusively`, `confirms truth of` |
| **Observational / Correlational Associations** | `is associated with`, `co-occurs with`, `covaries with`, `corresponds to` | `causes`, `drives directly`, `forces`, `proves causality` |
| **Predictive / Conditional Forecasting** | `predicts`, `forecasts`, `precedes conditionally`, `contains predictive information` | `causes`, `governs mechanistic outcome`, `dictates` |
| **Identified Causal / Quasi-Experimental Designs** | `estimates the causal effect of`, `identifies the conditional impact of`, `supports the hypothesis that` | `proves universal law`, `eradicates all alternative mechanisms` |
| **Formal / Theoretical Deduction** | `establishes by construction`, `proves (under stated axioms)`, `derives`, `entails` | `empirically demonstrates`, `empirically confirms` (without data) |
| **Historical / Archival / Qualitative Evidence** | `indicates`, `suggests`, `substantiates`, `is consistent with`, `supports the interpretation that` | `conclusively proves`, `rules out all rival accounts` |

---

## 6. Domain-Delegation Boundary

Section 8 now contains an explicit, enforceable delegation clause:

- **Protocol Scope:** The Prose Discipline Protocol governs **linguistic and stylistic calibration only**. It does not evaluate the substantive validity, methodological rigor, or empirical credibility of research designs.
- **Economics & Econometrics (`econ-write`):** Substantive identification validity, specification testing, estimator properties, and disciplinary causal entitlement remain exclusively owned and evaluated by `econ-write`.
- **Manuscript Lifecycle & Section Architecture (`academic-paper`):** Structural placement and authorial narrative framing remain owned by `academic-paper`.
- **Peer Review & Evidentiary Adjudication (`academic-paper-reviewer`):** Assessing whether evidence justifies conclusions remains owned by `academic-paper-reviewer`.
- **Evidence Retrieval & Factual Grounding (`deep-research`):** Source provenance and evidence evaluation remain owned by `deep-research`.
- **Formal Theory & Historical Interpretation:** Methodological adequacy remains governed by discipline-specific theoretical or historiographical standards.

---

## 7. Regression Guard Added

A targeted structural test was added to [`scripts/test_prose_discipline.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/test_prose_discipline.py):

`test_claim_strength_domain_boundary()` verifies that:
1. Section 8 header and boundaries exist.
2. Section 8 contains **zero** occurrences of method-specific econometric terminology (`VAR`, `cointegration`, `IRF`, `parallel trends`).
3. Section 8 contains the required domain-delegation statements and explicitly recognizes `econ-write` as the substantive economics entitlement owner.

---

## 8. Files Deliberately Unchanged

In accordance with Wave C1.1 bounds, the following surfaces were kept untouched:
- [`tools/prose_checks/check_prose_patterns.py`](file:///c:/ReposGitHub/academic-research-skills/tools/prose_checks/check_prose_patterns.py) and [`tools/prose_checks/__init__.py`](file:///c:/ReposGitHub/academic-research-skills/tools/prose_checks/__init__.py): Tool passed independent audit without behavioral defect; no changes needed.
- [`evals/gold/prose_discipline/cases.yaml`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/prose_discipline/cases.yaml): Gold fixtures passed independent audit without defect.
- [`docs/design/2026-10-11-ars-target-architecture/18_WAVE_C1_PROSE_DISCIPLINE_EXTRACTION_REPORT.md`](file:///c:/ReposGitHub/academic-research-skills/docs/design/2026-10-11-ars-target-architecture/18_WAVE_C1_PROSE_DISCIPLINE_EXTRACTION_REPORT.md): Historical Wave C1 record preserved.
- `prose-register-critic/`: Preserved intact until Wave C5.
- `econ-write/`, `academic-paper/`, `academic-paper-reviewer/`, `academic-pipeline/`, `deep-research/`: Substantive skills untouched.
- `docs/governance/ars_registry.yaml`, `MODE_REGISTRY.md`, `UPDATE_REGISTRY.md`: Governance registries untouched.
- Protected untracked development (`docs/design/2026-10-10-editorial-governance/`, `econ-slides/`, etc.): Untouched.

---

## 9. Validation Results

All repository test suites executed and passed cleanly:

1. **ARS Registry Validation:**
   `python scripts/validate_ars_registry.py` -> `PASS: ars_registry.yaml is valid (14 components, 20 capabilities)`
2. **ARS Capability Precedence Contract:**
   `python scripts/test_routing_contract.py` -> `PASS: All 17 positive and adversarial routing fixtures conform to contract`
3. **Prose Discipline Regression Suite:**
   `python scripts/test_prose_discipline.py` -> `PASS: All tests passed (including new domain boundary regression guard and 11/11 gold fixtures)`

---

## 10. C2 Readiness

Wave C1.1 successfully repaired the minor wording leak without reopening C1 architecture, modifying the deterministic tool, or altering runtime routing.

The foundation is fully verified and ready to proceed to:
**Wave C2 — Lightweight Editorial Governance + Material Passport Integration**.
