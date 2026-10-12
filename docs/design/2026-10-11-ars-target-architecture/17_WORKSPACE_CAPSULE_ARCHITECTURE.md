# ARS Workspace Capsule Conceptual Architecture

**Document ID:** `17_WORKSPACE_CAPSULE_ARCHITECTURE.md`
**Status:** CONCEPTUAL ARCHITECTURAL SPECIFICATION (Wave C0.1 Lock)
**Date:** 2026-10-12
**Governing Baseline Commit:** `1b94bfb`
**Scope:** Conceptual design of the ARS Workspace abstraction, defining research boundaries, source-of-truth invariants, mutation controls, lifecycle states, and Material Passport integration.
**Implementation State:** DESIGN ONLY. Runtime folder creation and code implementation strictly deferred to a dedicated future wave.

---

## 1. Why ARS Needs Workspaces

The Academic Research Skills (ARS) repository is an intellectual and methodological toolkit consisting of generic paper lifecycles, disciplinary writing policies, simulated referee panels, and deterministic verification tools. However, scholarly research is never conducted in the abstract; it is executed upon concrete, bounded research objects—such as a working paper, an empirical article, a dissertation chapter, or a revise-and-resubmit package.

Without a formal **`WORKSPACE`** abstraction, two serious failure modes emerge:
1. **Repository Contamination:** Project-specific data, empirical regression outputs, dissertation constants, and private advisor annotations leak into canonical skill code (as observed in legacy `advisor-reviewer`).
2. **Contextual Ambiguity:** Multi-agent workflows lack an authoritative definition of the manuscript's source-of-truth, leading to race conditions, untracked overwrites, and unanchored revisions across external directories.

The Workspace abstraction provides an explicit, bounded container that decouples **what is being researched** (the manuscript artifact) from **how research is conducted** (ARS skills, tools, profiles, and protocols).

---

## 2. Workspace vs. Skill vs. Tool vs. Profile vs. Protocol

To maintain absolute architectural clarity, the repository enforces strict taxonomy across its core concepts:

| Entity Type | Definition & Operational Responsibility | Canonical Example | Does It Own Capabilities? |
| :--- | :--- | :--- | :--- |
| **`WORKSPACE`** | The bounded research object and working environment upon which ARS operations act. | `workspaces/macro-capacity-wp/` | **NO.** Container and research subject only. |
| **`CORE_SKILL`** | Canonical owner of a broad, generic research lifecycle or evaluation capability. | `academic-paper`, `academic-paper-reviewer` | **YES.** Sole owner of declared lifecycle. |
| **`DOMAIN_SKILL`** | Canonical owner of field-specific disciplinary policies and formatting standards. | `econ-write`, `econ-slides` | **YES.** Sole owner of domain policies. |
| **`TOOL`** | Deterministic, non-agentic utility executing single-purpose computation or verification. | `revision_guard.py`, `check_jargon_leakage.py` | **YES.** Deterministic execution owner. |
| **`PROFILE`** | Declarative calibration data encapsulating scholar priors, advisor heuristics, or committee rosters. | `profiles/scholars/michael-ash.md`, `profiles/committees/umass-pe.md` | **NO.** Input parameters to skills only. |
| **`SHARED_PROTOCOL`** | Cross-cutting behavioral standard or evaluation rubric consumed across multiple skills. | `shared/protocols/prose_discipline_protocol.md` | **NO.** Standard consumed by skills. |
| **`ORCHESTRATOR`** | Control plane sequencing workflow stages and managing Material Passport lineage. | `academic-pipeline` | **NO.** Sequences without owning substance. |

---

## 3. Source-of-Truth Model

A workspace must declare **exactly ONE canonical source-of-truth** in its metadata manifest:

> **The Single Source Invariant:** There must never be two simultaneously canonical manuscript sources for a workspace.

When a workspace is initialized, its `workspace.yaml` manifest defines the authoritative source origin. All drafting, compiling, and verification steps branch directionally from this declared origin. Ambiguous multi-master configurations are strictly invalid.

---

## 4. Supported Conceptual Source Modes

The workspace abstraction conceptually supports four source modes:

1. **`local_copy`:**
   - The manuscript and associated project files reside entirely inside the workspace boundary (under `working/`).
   - Standard mode for self-contained, greenfield drafting within ARS.
2. **`external_repository`:**
   - The manuscript lives in an external Git repository (e.g. `C:\ReposGitHub\my-dissertation-project`).
   - The workspace references the external path and relative manuscript entrypoint (e.g. `chapters/ch1_replication.tex`).
   - ARS treats the external repository as read-only by default.
3. **`external_folder`:**
   - The manuscript lives in a designated local or network filesystem directory without Git tracking.
   - Operated via immutable snapshot intake.
4. **`future_connector_backed_source`:**
   - Remote, cloud-hosted document services (Overleaf Git bridge, Google Docs API, OSF repositories).
   - Read/write access governed by dedicated adapter connectors (deferred to future roadmap).

---

## 5. Mutation Boundary & Directory Roles

Workspaces enforce strict structural separation between intake snapshots, active drafting, generated outputs, and revision ledgers:

```
┌────────────────────────────────────────────────────────┐
│ WORKSPACE MUTATION BOUNDARY                            │
├────────────────────────────────────────────────────────┤
│ source/   ──► Immutable intake snapshot (READ-ONLY)    │
│ working/  ──► Active mutable author draft (WRITABLE)   │
│ evidence/ ──► Retained data tables & regression logs   │
│ editorial/──► Append-only revision decisions & reviews │
│ outputs/  ──► Compiled PDFs, diffs, release bundles    │
│ .ars/     ──► Workspace state, passport, revision digests│
└────────────────────────────────────────────────────────┘
```

### External Repository Safety Invariant
> **Critical Safety Invariant:** When interacting with an `external_repository` or `external_folder`, ARS must **NEVER** silently mutate the external source. All edits occur within the local `working/` boundary. Pushing or syncing mutations back to an external source requires an explicit human-authorized export action.

---

## 6. Conceptual Directory Anatomy

```
workspace/
├── workspace.yaml              # Authoritative manifest: source mode, entrypoint, capabilities
├── source/                     # Immutable intake snapshot or baseline commit reference
├── working/                    # Mutable workspace drafting tree (LaTeX sources, figures)
│   ├── main.tex
│   ├── sections/
│   └── figures/
├── evidence/                   # Retained empirical data, replication tables, citation logs
├── editorial/                  # Editorial governance decision ledger and referee comments
│   ├── editorial_governance.yaml
│   └── referee_reports/
├── outputs/                    # Compiled LaTeX artifacts, visual diffs, camera-ready PDFs
│   ├── main.pdf
│   └── diff_highlighted.pdf
└── .ars/                       # Internal ARS metadata and lineage tracking
    ├── passport.yaml           # Material Passport summary port
    ├── workspace_state.yaml    # Lifecycle state, active stage, and timestamp
    └── revision_ledger.yaml    # Deterministic verification digests
```

> ⚠️ **IMPORTANT ARCHITECTURAL NOTICE:**
> This directory structure is **CONCEPTUAL**. These folders are **NOT** created during Wave C0.1. Physical folder scaffolding and tooling are deferred to a dedicated future workspace implementation wave.

---

## 7. Workspace Lifecycle

Workspaces progress through seven semantic lifecycle states:

```
┌──────────┐     ┌────────┐     ┌──────────────┐     ┌──────────┐
│ IMPORTED │ ──► │ ACTIVE │ ──► │ UNDER_REVIEW │ ──► │ REVISION │
└──────────┘     └────────┘     └──────────────┘     └────┬─────┘
                                                          │
   ┌──────────┐     ┌───────────────┐     ┌─────────────────▼┐
   │ ARCHIVED │ ◄── │ RELEASE_READY │ ◄── │ RELEASE_CANDIDATE │
   └──────────┘     └───────────────┘     └──────────────────┘
```

1. **`IMPORTED`:** Source manuscript ingested, entrypoint verified, and initial snapshot hashed.
2. **`ACTIVE`:** Author drafting, section expansion, and iterative revisions underway.
3. **`UNDER_REVIEW`:** Simulated peer review panel (`academic-paper-reviewer`) or committee defense active.
4. **`REVISION`:** Revising draft in response to referee reports under bounded-diff change control.
5. **`RELEASE_CANDIDATE`:** Final polishing, prose discipline audits, citation compliance verification.
6. **`RELEASE_READY`:** Passed all configured workspace release gates; verified and compiled for submission.
7. **`ARCHIVED`:** Research published, defense concluded, or project permanently frozen.

These states represent non-blocking semantic milestones. Workspaces are not required to follow every state sequentially.

---

## 8. Capability and Profile Activation

A workspace declares its required toolchain and scholar calibrations via its manifest without duplicating skill logic:

```yaml
# workspace.yaml (Conceptual)
workspace_id: "capacities-replication-2026"
version: "1.0.0"

source:
  mode: external_repository
  path: "C:\\ReposGitHub\\dissertation-econometrics"
  entrypoint: "chapters/chapter1_capacity.tex"

capabilities:
  enabled:
    - academic-paper
    - econ-write
    - deep-research
    - academic-paper-reviewer

profiles:
  active:
    - michael-ash
    - deepankar-basu

protocols:
  active:
    - prose_discipline_protocol

editorial_governance:
  release_gate: optional
```

- **No Ownership Transfer:** The workspace does not own or modify `academic-paper` or `econ-write`.
- **Precedence Compliance:** Runtime tool dispatch adheres strictly to established Wave B1/B1.1 routing contracts.

---

## 9. Project Overlays

A Project Overlay provides declarative, domain-specific or project-specific constraints (e.g. customized econometric notation, specific institutional dummy definitions) consumed by a workspace.

- **Workspace vs. Overlay:** The workspace is the *active environment*; the overlay is the *parameterized policy*.
- **Isolation:** Project overlays live within the workspace boundary or an external configuration file; they are strictly forbidden from modifying ARS core skills or shared protocols.

---

## 10. Editorial Governance Policy

Editorial governance provides change control and bounded-diff verification:

1. **Workspace-Scoped Enforcement:**
   - The release gate policy is declared per workspace: `optional`, `recommended`, or `required`.
   - The system-wide default is **`optional`**.
2. **Boundary of 'Required':**
   - When configured as `required`, failure of `revision_guard.py` blocks **ONLY** the transition from `RELEASE_CANDIDATE` to `RELEASE_READY`.
   - It never blocks drafting, compiling, exploratory editing, or reviewing.

---

## 11. Material Passport Relationship

The Material Passport integrates with the workspace via a clean separation of concerns:

- **Material Passport Summary (`.ars/passport.yaml`):** Tracks high-level artifact provenance, literature corpus digests, citation verification verdicts, and the `editorial_governance_summary` port (`PASS`/`FAIL`/`INDETERMINATE`).
- **Granular Revision Ledger (`editorial/editorial_governance.yaml`):** Retains fine-grained sentence-level diff anchors, author rationales, and reviewer comment links.

---

## 12. External Repository Safety

To protect external user repositories from destructive automated edits:

1. **Intake Immutability:** External files are read into `source/` as an immutable snapshot.
2. **Local Working Copies:** All multi-agent drafting and surgical edits occur on local working copies in `working/`.
3. **Explicit Export Gate:** Changes are written back to the external repository only when the user explicitly triggers an export or sync command.
4. **Path Traversal Protection:** Workspaces reject any attempt to reference paths outside the declared workspace boundary.

---

## 13. Git Worktree as Optional Backend

The abstract workspace model remains backend-agnostic. When operating on an external Git repository, ARS may optionally instantiate the workspace using a **Git Worktree**:

- **Advantages:** Provides lightweight, isolated branch drafting sharing the parent repository's object store without risking uncommitted work in the user's primary working tree.
- **Abstract Independence:** Git worktree is strictly an implementation mechanism; the workspace concept remains fully compatible with plain filesystem folders, cloud drives, or LaTeX bundles.

---

## 14. Concrete Walkthrough Examples

### Example 1: Working Paper (`local_copy`)
- **Use Case:** Drafting a new working paper on inflation regimes from scratch.
- **Manifest:** `mode: local_copy`, `capabilities: [academic-paper, econ-write]`.
- **Workflow:** `academic-paper` scaffolds manuscript architecture in `working/main.tex`, consuming `econ-write` for triangular introduction and model exposition. Compiles outputs into `outputs/main.pdf`.

### Example 2: Dissertation Chapter (`external_repository`)
- **Use Case:** Refining a dissertation chapter hosted in an external Git repository.
- **Manifest:** `mode: external_repository`, `path: C:\ReposGitHub\dissertation`, `profiles: [michael-ash, deepankar-basu]`.
- **Workflow:** Evaluated via `academic-paper-reviewer` calibrated with Michael Ash simplicity directives and Deepankar Basu mathematical ODE stability checks. Edits staged locally in `working/`. Chapter 1 historical replication constants remain quarantined to external project notes.

### Example 3: Revise-and-Resubmit Package (`local_copy` / `external_folder`)
- **Use Case:** Addressing journal referee reports with strict change control.
- **Manifest:** `editorial_governance: { release_gate: required }`.
- **Workflow:** Referee comments ingested into `editorial/`. Changes bounded to authorized string anchors in `working/`. `revision_guard.py` verifies zero collateral edits before certifying `RELEASE_READY`.

---

## 15. Non-Goals

The Workspace abstraction explicitly disclaims the following:
- **Not a Workflow Engine:** Workspaces do not replace `academic-pipeline` orchestration logic.
- **Not a Secret Store:** Workspaces must never store API tokens, SSH keys, or private credentials in metadata files.
- **Not a Distributed Storage System:** Workspaces do not implement peer-to-peer synchronization or cloud storage backends.
- **Not an Alternative Capability Owner:** Workspaces never define or override core skill behaviors.

---

## 16. Future Connector Seam

The workspace specification provides an extensible interface for future cloud document connectors:

- **Overleaf Connector:** Bidirectional git-sync or API integration with Overleaf cloud projects.
- **Google Docs Connector:** Markdown-to-Docs export adapter for co-authoring.
- **OSF / Zenodo Connector:** Automated deposit of final release packages and replication evidence.

All connector implementations are deferred to the post-target roadmap.

---

## 17. Security and Privacy Considerations

1. **Credential Hygiene:** `.ars/` and `workspace.yaml` must never contain authentication secrets. Environment variables (`.env`) remain the sole provider for credentials.
2. **Gitignore Defaults:** `.ars/` workspace state and local `working/` scratch files must include standardized `.gitignore` rules to prevent accidental repository pollution.
3. **Data Isolation:** Private student supervisory feedback memos or confidential referee reports must reside in private workspace directories and never be committed to shared ARS profiles.

---

## 18. Implementation Deferral

> **Binding Governance Constraint:**
> The Workspace Capsule Architecture is formally **LOCKED** as a conceptual model. No physical runtime directories, CLI runner scripts, or file scaffolding are created in Wave C0.1. Physical implementation will occur in a separate, dedicated future wave following completion of Wave C decomposition.

---

## 19. The 10 Workspace Safety Rules (Locked Invariants)

The following ten safety rules are permanently locked and binding upon all future implementations:

1. **Single Source-of-Truth:** A workspace must declare exactly ONE canonical source-of-truth.
2. **External Read-Only Default:** External repositories and folders are read-only; mutations require explicit human authorization.
3. **Separation of Intake and Drafting:** Source intake (`source/`) and editable working state (`working/`) are strictly distinguishable.
4. **Non-Destructive Outputs:** Generated outputs (`outputs/`) must never silently overwrite source intake files.
5. **No Capability Ownership:** Workspace metadata must never define, own, or duplicate substantive capability logic.
6. **No Ownership Transfer via Activation:** Activating profiles or skills in a workspace does not alter global capability precedence.
7. **Explicit Overlays:** Project overlays must be explicitly declared and isolated from core skills.
8. **Workspace-Scoped Release Gating:** Editorial governance release gating is a workspace policy (`optional` by default), not a global mandate.
9. **Connectors Are Deferred:** Cloud and connector-backed sources remain future work; no mock connectors are authorized now.
10. **Zero Credential Storage:** Metadata manifests and workspace ledgers must never store passwords, API keys, or private tokens.
