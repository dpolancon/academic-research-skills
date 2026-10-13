# Editorial Governance Material Passport Port Contract

**Specification ID:** `shared/contracts/passport/EDITORIAL_GOVERNANCE_PORT.md`
**Version:** 1.0.0
**Wave:** Wave C2 (Lightweight Editorial Governance + Material Passport Port)
**Status:** CANONICAL SHARED CONTRACT
**Role:** `CHANGE_CONTROL_ONLY`

---

## 1. Purpose & Sidecar Architecture

Editorial Governance provides a deterministic, offline change-control contract that answers a single bounded question:

> **"Did this revision obey the authorized change-control contract we established?"**

It explicitly does **not** evaluate whether a manuscript is scientifically valid, theoretically sound, or worthy of publication.

### Sidecar vs. Passport Separation
To avoid bloating the manuscript's primary manifest (`passport.yaml`) with sentence-level revision ledgers, the architecture enforces a strict separation of concerns:

- **Sidecar Revision Ledger (`governance.json`):**
  Maintains detailed decision records, three-axis classifications, bounded diff anchors, source contracts, and historical adjudication records. Lives in an external sidecar file.
- **Material Passport Summary Port (`passport.yaml`):**
  Consumes a lightweight, 5-field summary verifying that change control was observed without recording detailed editorial deliberations.

---

## 2. Material Passport Summary Port Fields

When a workspace or manuscript workflow integrates with Material Passport, the `passport.yaml` manifest embeds only the following five high-level summary fields:

```yaml
editorial_governance:
  governance_id: "gov-2026-fondecyt-ch1"
  verification_verdict: "PASS"
  active_decision_count: 5
  unresolved_decision_count: 0
  source_hash: "a1b2c3d4e5f6..."
```

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `governance_id` | `string` | Unique identifier linking this revision state to its sidecar governance ledger. |
| `verification_verdict` | `enum` | Overall deterministic verification verdict: `PASS`, `FAIL`, or `INDETERMINATE`. |
| `active_decision_count` | `integer` | Total number of decisions currently active in the governing sidecar ledger. |
| `unresolved_decision_count`| `integer` | Count of open decisions requiring human resolution (`resolution == UNRESOLVED`). |
| `source_hash` | `string` / `null` | SHA-256 fingerprint of the baseline source document at the inception of the revision. |

Sentence-level diffs, anchor positions, and authorial rationales are strictly prohibited from the passport manifest.

---

## 3. Three-Axis State Model

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

These axes are orthogonal descriptive fields, avoiding combinatorial state-machine fragility.

---

## 4. Verification Verdict Semantics

Deterministic verification via `scripts/revision_guard.py` produces one of three canonical verdicts:

| Verdict | Meaning | Scholarly Independence Invariant |
| :--- | :--- | :--- |
| `PASS` | Mechanically verifiable change-control obligations are satisfied. All changes fall within authorized regions; no forbidden text appears. | **Does NOT imply scholarly quality.** A paper with poor arguments or awkward prose receives `PASS` if change control was obeyed. |
| `FAIL` | At least one mechanically verifiable contract condition was violated (e.g., source edited outside authorized anchors, rejected text introduced). | **Means ONLY a change-control violation.** Does not mean the paper's claims are false. |
| `INDETERMINATE` | Compliance cannot be determined mechanically (e.g., anchor missing/moved, source hash mismatch, semantic ambiguity). | **Prevents false blocking.** Missing anchors prompt human review rather than causing false build breaks. |

---

## 5. Release-Policy Semantics

Future workspace capsules configure editorial governance release policy via three levels:

- **`optional` (Default):** Governance verification is available as a diagnostic check. A non-`PASS` verdict never blocks compilation, drafting, review, or release.
- **`recommended`:** Governance verification surfaces non-`PASS` verdicts as warnings during workflow progression, but does not prohibit transition to `RELEASE_READY`.
- **`required`:** Transition to `RELEASE_READY` requires a verified `PASS` verdict. Does **not** block ordinary drafting, editing, review, or experimental runs.

**Global Invariant:** Editorial governance is **never globally mandatory**. Default policy is always `optional`.

---

## 6. Ownership Boundaries

To preserve strict separation of capabilities across the ARS ecosystem:

1. **Editorial Governance vs. Peer Review (`academic-paper-reviewer`):**
   Editorial governance checks bounded change authorization. Peer review evaluates scholarly substance, contribution, and methodological adequacy. A governance `PASS` never implies reviewer approval.
2. **Editorial Governance vs. Disciplinary Writing (`econ-write`):**
   Editorial governance checks textual scope compliance. `econ-write` governs economics disciplinary conventions, identification language, and model presentation.
3. **Editorial Governance vs. Manuscript Lifecycle (`academic-paper`):**
   `academic-paper` owns drafting, section structuring, and compilation. Editorial governance verifies change control only when invoked.
4. **Editorial Governance vs. Prose Discipline Protocol:**
   Prose discipline provides stylistic cadence and scaffolding diagnostics. Editorial governance verifies change authorization. They operate independently.
5. **Editorial Governance vs. Git:**
   Git records repository commits and branching. Editorial governance records authorial intent, bounded change authorization, and deterministic revision compliance.

---

## 7. Future Workspace Integration Seam

When workspace runtime infrastructure is implemented in future waves:
- Workspaces declare sidecar ledgers in `workspace.yaml` via `editorial_governance: { path: "governance.json", release_policy: "optional" }`.
- Revision guard tooling runs during verification passes and updates `passport.yaml`'s 5-field summary port.
- No core skills are modified or burdened with governance execution machinery.
