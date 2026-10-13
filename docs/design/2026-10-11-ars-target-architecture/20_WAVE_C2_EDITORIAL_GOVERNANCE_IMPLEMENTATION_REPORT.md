# ARS Wave C2 — Lightweight Editorial Governance & Material Passport Port Report

**Date:** 2026-10-13
**Baseline Commit:** `bdcd832` (`fix(prose): restore cross-domain claim boundary`)
**Mode:** Bounded Implementation / Candidate Simplification
**Role:** `CHANGE_CONTROL_ONLY`
**Status:** COMPLETE — READY FOR INDEPENDENT AUDIT

---

## 1. Baseline

Wave C2 builds upon baseline commit `bdcd832`, which finalized the cross-domain prose discipline protocol repair in Wave C1.1. Working tree preflight verified no dirty tracked changes and preservation of protected local work.

---

## 2. Candidate Sources Inspected

The following Phase 1 candidate artifacts were inspected and analyzed as authorized source material:
- Historical candidate design documents: [`docs/design/2026-10-10-editorial-governance/`](file:///c:/ReposGitHub/academic-research-skills/docs/design/2026-10-10-editorial-governance/) (00 through 07)
- Candidate sidecar schema: [`shared/contracts/passport/editorial_governance.schema.json`](file:///c:/ReposGitHub/academic-research-skills/shared/contracts/passport/editorial_governance.schema.json)
- Candidate verification report schema: [`shared/contracts/passport/revision_verification.schema.json`](file:///c:/ReposGitHub/academic-research-skills/shared/contracts/passport/revision_verification.schema.json)
- Candidate verification script: [`scripts/revision_guard.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/revision_guard.py)
- Candidate evaluation suite: [`evals/gold/editorial_governance/cases.json`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/editorial_governance/cases.json) and [`manifest.yaml`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/editorial_governance/manifest.yaml)
- Candidate test runners: [`scripts/test_editorial_governance_schema.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/test_editorial_governance_schema.py) and [`scripts/test_revision_guard.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/test_revision_guard.py)

---

## 3. Preserved Mechanisms

The durable core identified in the C0/C0.1 architecture review was retained and solidified:
1. **Three-Axis State Model:** Orthogonal separation of Resolution, Authorization, and Action.
2. **Bounded-Diff Verification:** Explicit location anchors (`start`, `end`) bounding permissible edits.
3. **Canonical Verdict Model:** Strict tripartite `PASS`, `FAIL`, `INDETERMINATE` semantics.
4. **Source Identity Verification:** Standard SHA-256 document hashing for identity checks.
5. **Unresolved Decision Tracking:** Explicit accounting of open or pending decisions without silent build failure.
6. **Scoped Source Contracts:** Conceptual roles (`DIRECT_EVIDENCE`, `HISTORICAL_CONTEXT`, etc.) bounding citations.

---

## 4. Simplified Mechanisms

Excessive procedural overhead from the candidate design was stripped away:
1. **Simplified Schema Definitions:** Removed mandatory nested event structures; flattened decisions into clear, human-readable objects while preserving backward compatibility.
2. **Clean Anchor Model:** Simplified anchor declarations into lightweight location objects.
3. **Consolidated Evaluation Suite:** Structured the gold evaluation fixtures into 12 canonical benchmark cases (`EG-01` through `EG-12`).
4. **Standalone Test Runners:** Equipped test scripts with standalone CLI execution blocks as well as standard pytest discovery.

---

## 5. Rejected Overengineering

The following candidate mechanisms were deliberately removed or rejected in accordance with C0.1 architecture locks:
1. **Cryptographic DAG Machinery:** Predecessor trees, cycle detection algorithms, forking bans, and DAG supersession checks were eliminated.
2. **Immutable Prefix History Graphs:** Removed mandatory prefix-matching validation against historical ledgers. Git handles version control and commit history; editorial governance does not duplicate Git.
3. **Distributed Receipt Networks:** Multi-party signature receipts (`trusted_approvals`, `payload_digest`, external actor proofs) were removed as premature product-level infrastructure.
4. **Runtime Schema Self-Pinning:** Removed runtime requirements that hashed the schema files and Python scripts into cryptographic bindings.
5. **Multi-Layer Raster Evidence:** Removed requirements for rendered visual screenshot hashing and PDF raster evidence.
6. **False Blocking on Anchor Evolution:** Missing or shifted anchors now evaluate conservatively to `INDETERMINATE` rather than causing false build breaks (`FAIL`).

---

## 6. Three-Axis State Model

Decisions in the governing sidecar ledger are evaluated across three orthogonal descriptive axes:

```
┌────────────────────────────────────────────────────────┐
│ 1. RESOLUTION: What has been decided?                  │
│    • ACCEPT: Decision is approved for execution.       │
│    • REJECT: Proposed change is formally rejected.     │
│    • DEFER: Decision is deferred to a future pass.     │
│    • UNRESOLVED: Decision is pending human input.      │
├────────────────────────────────────────────────────────┤
│ 2. AUTHORIZATION: What modification is permitted?      │
│    • ALLOWED: Textual replacement permitted in scope.  │
│    • FORBIDDEN: Textual modification barred.           │
│    • CONDITIONAL: Permitted only under stated proviso. │
│    • NOT_SPECIFIED: Scope has not been authorized.     │
├────────────────────────────────────────────────────────┤
│ 3. ACTION: What was actually executed in the revision? │
│    • IMPLEMENTED: Authorized change is present.        │
│    • NOT_IMPLEMENTED: Change has not been executed.    │
│    • PARTIAL: Change is only partially applied.        │
│    • OUT_OF_SCOPE_CHANGE: Unapproved edit detected.    │
└────────────────────────────────────────────────────────┘
```

The three axes are stored as independent descriptive attributes, eliminating brittle state-machine transitions.

---

## 7. Source Contract

The shared source contract specifies:
- `governance_id`: Unique identifier linking the revision state to its sidecar ledger.
- `source_hash`: Optional SHA-256 fingerprint of the baseline source document.
- `source_role`: Disciplinary role bounding citation claims (`DIRECT_EVIDENCE`, `HISTORICAL_CONTEXT`, `THEORETICAL_MOTIVATION`, `METHOD_SOURCE`, `INTERPRETIVE_FRAMEWORK`, `COUNTERARGUMENT`, `DATA_SOURCE`).
- Attribution strength bounds (`allowed_attribution_strength`, `forbidden_attribution_strength`).

Ordinary hashing is used strictly for identity confirmation, not as a trust protocol.

---

## 8. Bounded-Diff Model

The bounded-diff engine operates via text anchors:
1. Decisions specify `start` and `end` delimiter strings bounding an authorized section.
2. `scripts/revision_guard.py` locates these anchors in both baseline and revised texts.
3. Text inside authorized spans is permitted to change.
4. Outside text is masked and compared: if text outside authorized spans was altered, `unauthorized_change_outside_scope` produces `FAIL`.
5. If a decision specifies `whole_document: true`, full-text authorial revisions are permitted.

---

## 9. PASS / FAIL / INDETERMINATE Semantics

| Verdict | Meaning | Scholarly Independence Invariant |
| :--- | :--- | :--- |
| `PASS` | All mechanically verifiable change-control obligations are satisfied. | **Does NOT imply scholarly quality.** A paper with poor arguments or awkward prose receives `PASS` if change control was obeyed. |
| `FAIL` | At least one verifiable contract condition was violated (e.g. edits outside authorized anchors, forbidden text introduced). | **Means ONLY a change-control violation.** Does not mean the paper's scientific claims are false. |
| `INDETERMINATE` | Compliance cannot be verified mechanically (e.g. anchor missing/moved, source hash mismatch, conditional/semantic proviso). | **Prevents false blocking.** Missing anchors prompt human inspection rather than halting workflow execution. |

---

## 10. Sidecar Architecture

Detailed editorial records are housed in an external sidecar file (`governance.json`):
- Keeps detailed deliberations, reviewer comment mappings, anchor lists, and rationale logs out of manuscript source files.
- Prevents bloat in version control manifests and release passports.
- Can be inspected offline by human authors or deterministic tools.

---

## 11. Material Passport Port

Defined in [`shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md`](file:///c:/ReposGitHub/academic-research-skills/shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md), the Material Passport summary port embeds exactly five high-level fields into `passport.yaml`:

```yaml
editorial_governance:
  governance_id: "gov-sample-01"
  verification_verdict: "PASS"
  active_decision_count: 5
  unresolved_decision_count: 0
  source_hash: "a1b2c3d4e5f6..."
```

Sentence-level diffs, anchor positions, and authorial rationales are strictly prohibited from the passport manifest.

---

## 12. Release-Policy Semantics

Future workspace capsules configure editorial governance release policy via three levels:
- **`optional` (Default):** Governance verification is available as a diagnostic check. A non-`PASS` verdict never blocks compilation, drafting, review, or release.
- **`recommended`:** Governance verification surfaces non-`PASS` verdicts as warnings during workflow progression, but does not prohibit transition to `RELEASE_READY`.
- **`required`:** Transition to `RELEASE_READY` requires a verified `PASS` verdict. Does **not** block ordinary drafting, editing, review, or experimental runs.

**Global Invariant:** Editorial governance is **never globally mandatory**. Default policy across all repositories and workspaces is always `optional`.

---

## 13. Revision Guard Behavior

[`scripts/revision_guard.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/revision_guard.py) is implemented as a deterministic, offline verification CLI and Python module:
- Standard library + `jsonschema` only (zero network requests, zero LLM dependencies).
- Strictly deterministic output with stable JSON sorting and format checkers.
- Safely reports `INDETERMINATE` when anchors are missing or moved, avoiding false blocking.
- Computes `passport_summary` matching the 5-field contract.

---

## 14. Gold Evaluation Coverage

The evaluation suite ([`evals/gold/editorial_governance/cases.json`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/editorial_governance/cases.json)) formalizes 12 gold benchmark test cases:
- `EG-01`: Exact authorized bounded edit -> `PASS`
- `EG-02`: Unauthorized change outside allowed region -> `FAIL`
- `EG-03`: Missing or moved anchor -> `INDETERMINATE`
- `EG-04`: Source hash mismatch -> `INDETERMINATE`
- `EG-05`: Accepted decision implemented -> `PASS`
- `EG-06`: Accepted mandatory decision not implemented -> `FAIL`
- `EG-07`: Rejected change absent -> `PASS`
- `EG-08`: Rejected change appears -> `FAIL`
- `EG-09`: Unresolved decision remains -> `INDETERMINATE` with `unresolved_count > 0`
- `EG-10`: Scholarly-quality independence -> `PASS`
- `EG-11`: Semantic ambiguity -> `INDETERMINATE`
- `EG-12`: Deterministic reproducibility -> `PASS`

All 12 cases execute and pass deterministically.

---

## 15. Schema Tests

[`scripts/test_editorial_governance_schema.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/test_editorial_governance_schema.py) exercises 10 comprehensive schema assertions:
1. `test_schemas_well_formed`: Valid Draft 2020-12 syntax.
2. `test_valid_sidecar_accepted`: Conforming lightweight sidecar passes.
3. `test_malformed_sidecar_rejected`: Bad version, missing decisions, extra properties rejected.
4. `test_required_fields_enforced`: `schema_version`, `governance_id`, `decisions` enforced.
5. `test_three_axis_enum_semantics`: Resolution, Authorization, Action enums verified.
6. `test_release_policy_enum`: `optional`, `recommended`, `required` verified.
7. `test_verdict_enum`: `PASS`, `FAIL`, `INDETERMINATE` strictly enforced.
8. `test_material_passport_summary_structure`: 5-field passport summary contract enforced.
9. `test_sidecar_passport_separation`: Detailed records barred from passport summary.
10. `test_no_dag_or_self_pinning_mandatory`: DAG and receipt networks are optional.

---

## 16. Determinism & Offline Verification

- Zero network calls: Verified absence of `requests`, `urllib`, `openai`, `httpx`, or socket calls.
- Zero AI inference: No machine-authorship classification or hallucination scoring.
- Deterministic reproducibility: Byte-equivalent JSON verification output verified across repeated executions.
- Clean compilation: All Python scripts compile cleanly via `python -m py_compile`.

---

## 17. Ownership Boundaries

To preserve strict separation of capabilities across the ARS ecosystem:
1. **Editorial Governance vs. Peer Review (`academic-paper-reviewer`):** Editorial governance checks bounded change authorization. Peer review evaluates scholarly substance, contribution, and methodological adequacy. A governance `PASS` never implies reviewer approval.
2. **Editorial Governance vs. Disciplinary Writing (`econ-write`):** Editorial governance checks textual scope compliance. `econ-write` governs economics disciplinary conventions, identification language, and model presentation.
3. **Editorial Governance vs. Manuscript Lifecycle (`academic-paper`):** `academic-paper` owns drafting, section structuring, and compilation. Editorial governance verifies change control only when invoked.
4. **Editorial Governance vs. Prose Discipline Protocol:** Prose discipline provides stylistic cadence and scaffolding diagnostics. Editorial governance verifies change authorization. They operate independently.
5. **Editorial Governance vs. Git:** Git records repository commits and branching. Editorial governance records authorial intent, bounded change authorization, and deterministic revision compliance.

---

## 18. Workspace Implementation Status

Runtime workspace implementation remains **deferred** in accordance with Wave C0.1 architecture locks:
- No `workspaces/` directories were created.
- No `workspace.yaml` runtime engine was built.
- C2 created the shared contract interfaces that future workspaces can consume cleanly.

---

## 19. Legacy / Candidate Migration Status

The Phase 1 candidate work has been successfully refactored and stabilized into:
- Simplified canonical schemas in [`shared/contracts/passport/`](file:///c:/ReposGitHub/academic-research-skills/shared/contracts/passport/)
- Material Passport port specification [`EDITORIAL_GOVERNANCE_PORT.md`](file:///c:/ReposGitHub/academic-research-skills/shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md)
- Deterministic verification engine [`scripts/revision_guard.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/revision_guard.py)
- Regression test suites in [`scripts/`](file:///c:/ReposGitHub/academic-research-skills/scripts/)
- Canonical gold evaluation cases in [`evals/gold/editorial_governance/`](file:///c:/ReposGitHub/academic-research-skills/evals/gold/editorial_governance/)

Historical candidate design documents in [`docs/design/2026-10-10-editorial-governance/`](file:///c:/ReposGitHub/academic-research-skills/docs/design/2026-10-10-editorial-governance/) were preserved unmodified.

---

## 20. C3 Readiness

All C2 objectives are fully achieved:
- Change control contract and Material Passport port established.
- All candidate tests pass (18/18 via pytest, 100% via standalone runners).
- All repository regressions pass (registry validator, routing contract, prose discipline).
- Zero modifications to runtime skills, routing, or registry.
- Protected `econ-slides/` development remains untouched.

The repository is fully ready for Wave C2 independent adversarial audit before initiating Wave C3.
