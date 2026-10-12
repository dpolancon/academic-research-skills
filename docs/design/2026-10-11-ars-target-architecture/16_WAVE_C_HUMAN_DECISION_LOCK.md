# ARS Wave C Human Decision Lock & Governance Reconciliation

**Document ID:** `16_WAVE_C_HUMAN_DECISION_LOCK.md`
**Status:** BINDING ARCHITECTURAL SPECIFICATION (Wave C0.1 Lock)
**Date:** 2026-10-12
**Governing Baseline Commit:** `1b94bfb`
**Scope:** Formal record and architectural lock of binding human decisions resolving the Wave C0 design review, introducing the Workspace abstraction, and preparing the foundation for Subwave C1 execution.

---

## 1. Baseline

This specification locks decisions strictly on top of baseline commit `1b94bfb`:
- `63f7b33`: Freeze ARS target architecture and Wave A repository baseline
- `06b46b3`: feat(governance): establish integrated ARS registry (Wave B0)
- `8bdc0df`: docs(econ-write): add evaluation examples and ranked sources
- `a87e8b2`: feat(routing): enforce ARS capability precedence (Wave B1)
- `a797db9`: test(routing): add adversarial precedence cases (Wave B1.1)
- `1b94bfb`: docs(architecture): design Wave C legacy decomposition (Wave C0)

All decisions recorded herein are binding and must not be reopened during subsequent implementation subwaves.

---

## 2. Purpose

The Wave C0 architectural design review identified three operational alternatives and uncovered the need for a formal research boundary abstraction. Following interactive human review, all open architectural questions have been resolved.

This document serves as the authoritative, permanent lock for these decisions. It establishes:
1. The dual representation model for scholar identities versus contextual role wrappers;
2. The active status and lifecycle policy for advisor Michael Ash;
3. Epistemic provenance requirements for extracted scholar profiles;
4. The formal definition and operational invariants of the `WORKSPACE` abstraction;
5. The strict exclusion of substantive Chapter 1 dissertation copies from ARS;
6. The workspace-scoped release policy for lightweight editorial governance;
7. The preservation of frozen Wave B1/B1.1 routing contracts;
8. The final green light for Subwave C1 implementation.

---

## 3. Locked Canonical Ownership

The core capability monopolies established in Waves A through B1 remain inviolate (`forbidden_duplicate_owners: true`):

| Capability Domain | Sole Canonical Operational Owner | Architectural Role | Invariant Precedence Rule |
| :--- | :--- | :--- | :--- |
| **Generic Manuscript Lifecycle** | `academic-paper` | `CORE_SKILL` | Owns complete paper structure, multi-agent writing workflow, formatting, and author-side quality gates. |
| **Economics Disciplinary Writing Policy** | `econ-write` | `DOMAIN_SKILL` | Owns economics prose style (BLUF, triangular structure, concrete magnitudes, identification exposition). Consumed by `academic-paper`. |
| **Simulated External Peer Review** | `academic-paper-reviewer` | `CORE_SKILL` | Sole owner of independent referee panel simulation, Devil's Advocate stress-testing, editorial decision letters, and revision roadmaps. |
| **Workflow Orchestration** | `academic-pipeline` | `ORCHESTRATOR` | Control plane managing stage transitions and Material Passport lineage. Does not duplicate substantive disciplinary rules. |
| **Evidence & Citation Integrity** | `deep-research` | `CORE_SKILL` | Owns literature search, citation verification, and corpus entry extraction. |
| **Presentation Slide Production** | `econ-slides` | `DOMAIN_SKILL` | Sole owner of Beamer presentation deck generation and slide validation. |

---

## 4. Scholar Identity and Contextual Roles

ARS adopts a **dual representation model** that decouples permanent intellectual identity from contextual advisory and committee roles:

```
┌─────────────────────────────────────────────────────────────┐
│ Canonical Durable Intellectual Identity                     │
│ Target: profiles/scholars/<person>.md                       │
│ Content: Methodological priors, published evidence,         │
│          epistemic standards, theoretical lens              │
└──────────────────────────────┬──────────────────────────────┘
                               │ Referenced by
                ┌──────────────┴──────────────┐
                ▼                             ▼
┌──────────────────────────────┐ ┌──────────────────────────────┐
│ Contextual Active Advisor    │ │ Declarative Committee        │
│ Target: profiles/advisors/   │ │ Target: profiles/committees/ │
│         <person>.md          │ │         <committee>.md       │
│ Content: Active supervisory  │ │ Content: Multi-scholar roster│
│          review constraints  │ │          synthesis & defense │
└──────────────────────────────┘ └──────────────────────────────┘
```

1. **Canonical Scholar Identity (`profiles/scholars/<person>.md`):**
   - Represents the durable, scholar-level profile grounded in verified publications, public lectures, and pedagogical writings.
   - Independent of any specific student, dissertation, or institutional committee.
2. **Contextual Role Wrappers:**
   - **Advisor Profile (`profiles/advisors/<person>.md`):** A lightweight role binding that references the canonical scholar profile and defines active supervisory review heuristics and constraints.
   - **Committee Profile (`profiles/committees/<committee>.md`):** A declarative composition profile defining the panel roster (referencing individual scholar profiles) and chair synthesis rules.
3. **No Redundant Profiles:** The advisor profile does not duplicate the scholar profile; it imports or points to the canonical scholar identity.

---

## 5. Michael Ash Active-Role Policy

Michael Ash plays a central role as primary doctoral supervisor in the candidate's active dissertation workflow:

1. **Active During Dissertation Lifecycle:**
   - Michael Ash remains an **ACTIVE** advisor (`profiles/advisors/michael-ash.md`) and committee chair (`profiles/committees/umass-pe.md`) throughout all dissertation drafting, review, and defense cycles.
2. **Post-Dissertation Lifecycle Transition:**
   - Upon successful completion and defense of the doctoral dissertation:
     - The advisor role binding (`profiles/advisors/michael-ash.md`) may be marked inactive or archived;
     - The committee membership in `umass-pe.md` may transition to archived;
     - The canonical scholar profile (`profiles/scholars/michael-ash.md`) remains permanent, durable, and reusable across future applied econometrics and political economy research.

---

## 6. Profile Provenance Requirements

Profiles must not synthesize or extrapolate personal scholarly opinions without explicit evidentiary grounding. Every extracted profile must classify its contents across six distinct epistemic tiers:

| Metadata Field | Classification Level | Description / Permitted Application |
| :--- | :--- | :--- |
| `evidence_status` | `SOURCED_FACTUAL` | Verifiable institutional affiliations, degrees, official course syllabi, and software packages. |
| `evidence_status` | `PUBLISHED_EVIDENCE` | Methodological positions, identification strategies, and theoretical frameworks documented in peer-reviewed publications. |
| `evidence_status` | `DIRECT_FEEDBACK` | Explicit supervisory annotations, dissertation memos, and marked draft comments authorized for private research use. |
| `evidence_status` | `CONTEXTUAL_ROLE` | Departmental committee norms, defense procedural guidelines, and seminar conventions. |
| `evidence_status` | `INFERRED_CALIBRATION` | Analytical extrapolations from co-authorship networks or theoretical tradition (must be explicitly flagged as advisory). |
| `confidence` | Numeric `[0.0 - 1.0]` | Explicit calibration confidence metric reflecting empirical support density. |

> **Hard Guardrail:** No generalized automated persona-inference or corpus-scraping engine may be implemented. All Wave C profiles are hand-curated and evidence-backed.

---

## 7. Workspace Definition

ARS formally establishes the concept of a **`WORKSPACE`**:

> **Definition:** A Workspace is the bounded research object on which ARS skills, tools, profiles, and protocols operate.

A Workspace is **NOT**:
- A skill or sub-agent;
- A capability owner;
- An orchestrator control plane;
- A scholar profile or persona;
- A permanent home for reusable ARS logic or tools.

### Conceptual Layering:
```
WORKSPACE (The Research Object: paper, chapter, draft, R&R)
    │
    ▼
academic-pipeline (Workflow Orchestration & Stage Gating)
    │
    ▼
Skills + Tools + Profiles + Protocols (The Methodological Engine)
```

The workspace model natively accommodates working papers, dissertation chapters, draft journal submissions, revise-and-resubmit revisions, first-pass manuscript diagnoses, and release verification.

---

## 8. Workspace Source-of-Truth Rule

Every workspace must explicitly declare **exactly ONE canonical source-of-truth** in its metadata manifest:

```yaml
# Conceptual Manifest Snippet:
source:
  mode: external_repository | local_copy | external_folder | future_connector
  path: "..."
  entrypoint: "manuscript.tex"
```

1. **Strict Singularity:** There must never be two simultaneously canonical manuscript sources.
2. **Supported Conceptual Modes:**
   - `local_copy`: Manuscript files reside directly inside the workspace boundary.
   - `external_repository`: Manuscript resides in a separate external Git repository.
   - `external_folder`: Manuscript resides in a designated local or network filesystem folder.
   - `future_connector_backed_source`: Remote document services (Overleaf, Google Docs, OSF).
3. **No Ambiguous Overwrites:** Synchronizations must be deterministic and directional.

---

## 9. Workspace Mutation Boundary

Workspaces enforce strict structural separation between intake snapshots, active drafting, generated outputs, and revision ledgers:

- `source/`: Immutable intake snapshot or read-only reference to original inputs.
- `working/`: Mutable drafting tree where revisions and edits occur.
- `evidence/`: Retained data tables, regression logs, and citation dossiers.
- `editorial/`: Append-only revision decisions, author rationales, and referee comments.
- `outputs/`: Compiled LaTeX PDFs, diff outputs, and distribution packages.
- `.ars/`: Local workspace metadata, Material Passport state, and revision digests.

### External Repository Safety Invariant:
> **Hard Invariant:** For workspaces referencing `external_repository` or `external_folder`, ARS must **NEVER** silently mutate the external source. External mutations require explicit human confirmation.

---

## 10. Workspace Lifecycle

Workspaces follow a semantic, non-blocking lifecycle progression:

```
IMPORTED ──► ACTIVE ──► UNDER_REVIEW ──► REVISION ──► RELEASE_CANDIDATE ──► RELEASE_READY ──► ARCHIVED
```

- `IMPORTED`: Intake snapshot initialized and verified.
- `ACTIVE`: Author-side drafting and iterative editing underway.
- `UNDER_REVIEW`: Simulated external peer review or committee evaluation in progress.
- `REVISION`: Addressing review critiques under bounded-diff change control.
- `RELEASE_CANDIDATE`: Draft finalized; undergoing formatting and verification checks.
- `RELEASE_READY`: Passed all configured release gates; certified for submission.
- `ARCHIVED`: Research project completed, published, or permanently frozen.

Workspaces are not required to traverse every state; these represent semantic milestones rather than a rigid state machine.

---

## 11. Workspace Capability Activation

A workspace declares its required tools, domain policies, and calibration profiles via declarative configuration:

```yaml
capabilities:
  enabled:
    - academic-paper
    - econ-write
    - deep-research
    - academic-paper-reviewer
profiles:
  active:
    - michael-ash
protocols:
  active:
    - prose_discipline_protocol
```

- **Activation Is Not Ownership:** Activating a capability within a workspace does not transfer ownership or fork skill code.
- **Strict Precedence:** All operations within the workspace strictly obey B1/B1.1 capability routing contracts.

---

## 12. Project-Overlay Distinction

ARS enforces a rigorous conceptual distinction between a Workspace and a Project Overlay:

- **`WORKSPACE`:** The active, bounded research environment and mutable files for a specific paper or chapter.
- **`PROJECT_OVERLAY`:** A declarative, reusable set of project-specific constraints, model assumptions, or custom terminology consumed by a workspace.

Project overlays must remain explicit, external to ARS core skills, and consumed strictly on an opt-in basis. They must never pollute canonical skills or shared protocols.

---

## 13. Chapter 1 Exclusion Rule

Dissertation Chapter 1 (Critical Replication of Shaikh's capacity utilization chapter) is **frozen and complete**:

1. **No ARS Project Copy:** Do **NOT** create `projects/dissertation-ch1/` inside ARS.
2. **Strict File Quarantine:** The following materials must **NEVER** be copied into ARS runtime directories or canonical design trees:
   - Chapter 1 LaTeX manuscript sources (`CH1_CriticalReplication.pdf`);
   - The 68-item feedback matrix (`Feedback_Matrix.xlsx`);
   - Dissertation empirical datasets, regression scripts, or Stata/R outputs;
   - Paper-specific model refutation parameters ($\theta=1$ constraint, no-dummy VECM checks).
3. **Documentation-Only Provenance:** Reusable lessons and historical supervisory feedback extracted from Chapter 1 reside exclusively as migration provenance notes in documentation artifacts.

---

## 14. Prose-Discipline Boundary

The prose discipline capability extracted from `prose-register-critic` is established as:

> **Semantic Role:** `CROSS-DOMAIN SHARED_PROTOCOL`
> **Canonical Destination:** `shared/protocols/prose_discipline_protocol.md`

1. **Protocol Contents:**
   - Category A technical vocabulary protection (immune from deletion);
   - Category B legitimate phrase review;
   - Category C rhetorical scaffolding rewrite rules;
   - Evidential claim-strength verb calibration;
   - 11 auditing pattern families.
2. **Deterministic Tooling:**
   - Deterministic linting scripts reside in `tools/prose_checks/check_jargon_leakage.py`.
   - Checks are strictly limited to mechanically defensible Category C pattern matches.
3. **No Competing Writing Engine:**
   - Economics writing policy remains exclusively owned by `econ-write`.
   - General academic paper writing remains exclusively owned by `academic-paper`.
   - The prose protocol is consumed by writing and review skills; it does not draft or rewrite manuscripts independently.
4. **Anti-AI False Positive Guard:** Generic, naive n-gram blacklists and stylistic flattening are explicitly rejected.

---

## 15. Editorial-Governance Scope

Editorial governance governs **CHANGE CONTROL ONLY**:

```
Editorial Governance VERIFIES:
  [✔] Revision authorization state (AUTHORIZED / HELD / BLOCKED)
  [✔] Modification scope and regional string anchors
  [✔] Decision provenance and reviewer comment binding
  [✔] Source-role attribution (SOURCE_CONTRIBUTION vs AUTHORIAL_DERIVATION)
  [✔] Bounded-diff compliance (zero collateral edits outside anchors)
  [✔] Resolution status of reviewer critiques

Editorial Governance DOES NOT JUDGE:
  [✘] Scientific or theoretical validity
  [✘] Econometric identification credibility
  [✘] Historical interpretation correctness
  [✘] Journal publication probability or merit
```

Scientific, empirical, and stylistic evaluations belong exclusively to canonical domain and review skills (`econ-write`, `academic-paper-reviewer`, `academic-paper`).

---

## 16. Release-Gate Policy

There is **NO globally mandatory ARS release gate**.

1. **Workspace-Scoped Policy:**
   - Each workspace manifest declares its desired editorial governance enforcement level:
   ```yaml
   editorial_governance:
     release_gate: optional | recommended | required
   ```
2. **Default Setting:** `optional`.
3. **Scope of 'Required':**
   - When set to `required`, validation failure blocks **ONLY** the transition to `RELEASE_READY`.
   - It **NEVER** blocks drafting, exploratory editing, compiling, reviewing, or intermediate commits.

---

## 17. Material Passport Decision

Wave C0 **Option C** is formally locked:

> **Option C:** Lightweight Shared Editorial Contract + Material Passport Summary Port + Sidecar Revision Ledger + Deterministic Verification Tooling.

1. **Contracts:**
   - `shared/contracts/passport/editorial_governance.schema.json`
   - `shared/contracts/passport/revision_verification.schema.json`
2. **Material Passport Summary (`passport.yaml`):**
   - Tracks high-level revision integrity: `governance_id`, `verification_verdict` (`PASS`/`FAIL`/`INDETERMINATE`), `active_decision_count`, `source_hash`.
3. **Sidecar Ledger (`editorial/editorial_governance.yaml`):**
   - Retains granular per-decision rationales, anchor strings, and invariant retirement records.
4. **Verification Core:**
   - Deterministic verification engine `scripts/revision_guard.py`.

---

## 18. Future-Personalization Seam

All generalized personalization systems remain **DEFERRED** per `10_FUTURE_PERSONALIZATION_BACKLOG.md`:

- **In Scope for Wave C:** Hand-curated markdown profiles (`profiles/scholars/`, `profiles/advisors/`, `profiles/committees/`).
- **Deferred Systems:**
  - Automated corpus-based profile extraction tools (`ars-profile-builder`);
  - Algorithmic persona inference from author writing samples;
  - Automated referee and editor profile generators;
  - Multi-tenant profile isolation harnesses.
- **Extension Seam:** Wave C static profiles utilize standardized YAML frontmatter metadata, providing a clean compatibility seam for future automated generators without modifying core skill architectures.

---

## 19. Physical Migration Deferral

Physical repository directory restructuring remains strictly scheduled for **Wave F**:

- All live runtime paths continue resolving to live root directories:
  - `academic-paper`
  - `econ-write`
  - `academic-paper-reviewer`
  - `academic-pipeline`
  - `deep-research`
  - `econ-slides`
- Physical target paths (`skills/core/`, `skills/domain/`, `orchestrator/`) are architectural designations only and must not be created during Wave C.

---

## 20. Human Decisions Now Closed

The three operational choices from Wave C0 and the workspace abstraction are now formally **RESOLVED**:

| Item ID | Human Decision Topic | Final Binding Resolution | Status |
| :--- | :--- | :--- | :--- |
| **HD-01** | **Scholar/Advisor Taxonomy** | Adopt dual model: canonical scholar identity (`profiles/scholars/`) + contextual role wrappers (`profiles/advisors/`, `profiles/committees/`). Michael Ash active until dissertation completion. | **RESOLVED & LOCKED** |
| **HD-02** | **Chapter 1 Quarantine** | Documentation-only migration provenance and extraction notes; no substantive `projects/dissertation-ch1/` folder created in ARS. | **RESOLVED & LOCKED** |
| **HD-03** | **Editorial Release Gate** | Workspace-scoped policy (`optional | recommended | required`, default `optional`); gates only `RELEASE_READY`. | **RESOLVED & LOCKED** |
| **HD-04** | **Workspace Model** | Formalized `WORKSPACE` abstraction as the bounded research object with strict source-of-truth and mutation boundaries. | **RESOLVED & LOCKED** |

---

## 21. Remaining Unresolved Issues

There are **zero remaining unresolved architectural issues** blocking Wave C implementation.

All capability owners, profile relationships, protocol boundaries, and verification gates are unambiguous, non-duplicative, and mathematically consistent with the established ARS governance foundation.

---

## 22. Final Lock Statement

```
============================================================
WAVE C ARCHITECTURAL DECISION STATUS:
WAVE_C_HUMAN_DECISIONS_LOCKED
============================================================
```

All human decisions are locked. Subwave C1 implementation (Shared Prose Discipline Protocol & Tool Extraction) is authorized to proceed upon final confirmation.
