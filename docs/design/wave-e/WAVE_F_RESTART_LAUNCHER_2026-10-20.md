# AG LAUNCHER — WAVE F PHYSICAL MIGRATION ASSESSMENT & PLANNING

Work in:

`C:\ReposGitHub\academic-research-skills`

## 1. Task and Authorization

Execute a **read-only inspection and written migration plan for Wave F (Physical Directory Harmonization)**.

Diego Polanco authorizes:
- Inspection of the published repository baseline, governance contracts, and existing directory layouts.
- Read-only analysis of client discoverability impacts across environments (Claude Code, Cursor, AG, CLI callers).
- Authoring the comprehensive Wave F execution plan in `docs/design/wave-f/WAVE_F_EXECUTION_PLAN.md`.

**Wave D is HUMAN-CLOSED** at checkpoint:
`27fbfd60255fe6c3cd99e7298c43a5189869163b`

**Wave E is HUMAN-CLOSED** at implementation checkpoint:
`bf81d8e9b1b9a90415ae2884388d3bfdfa62d24d`

**STRICT LIMITS FOR THIS SESSION:**
- **READ-ONLY ASSESSMENT & WRITTEN PLAN ONLY.**
- **NO PHYSICAL MIGRATION, DIRECTORY MOVING, OR RENAMING AUTHORIZED.**
- **NO CODE, REGISTRY, OR ROUTING CONTRACT MODIFICATIONS.**
- **NO COMMITS, PUSHES, OR ALTERATION OF UNTRACKED WORK.**
- **STOPPING TOKEN:** `WAVE F PLANNING ONLY — IMPLEMENTATION REQUIRES HUMAN AUTHORIZATION`

---

## 2. Establish Baseline & Required Reading

### Read in sequence:
1. [`docs/design/wave-e/ARS_SESSION_HANDOFF_POST_WAVE_E_2026-10-20.md`](ARS_SESSION_HANDOFF_POST_WAVE_E_2026-10-20.md) *(Governing restart context)*
2. [`docs/design/wave-e/WAVE_E_HUMAN_CLOSURE_2026-10-20.md`](WAVE_E_HUMAN_CLOSURE_2026-10-20.md) *(Ratified Wave E closure record)*
3. [`docs/governance/ars_registry.yaml`](../../governance/ars_registry.yaml) *(Authoritative machine-readable ontology v1.3.0)*
4. [`docs/governance/ROUTING_AND_PRECEDENCE.md`](../../governance/ROUTING_AND_PRECEDENCE.md) *(Authoritative capability routing contract v1.3.0)*
5. [`docs/design/2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md`](../2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md) *(Target architecture roadmap)*
6. [`docs/design/wave-e/WAVE_E_COMPLETION_REPORT.md`](WAVE_E_COMPLETION_REPORT.md) *(Accepted Wave E implementation report)*

### Read-Only Verification:
- Inspect `git rev-parse HEAD` and verify ancestry from Wave D (`27fbfd6`) and Wave E Checkpoint A (`bf81d8e`).
- Inspect `git status --short` to confirm that untracked directories (`docs/design/2026-10-10-editorial-governance/`, `econ-slides/slide_deck_Fondecyt/`, `econ-slides/tests/`) remain intact.

---

## 3. Core Planning Tasks for Wave F

Wave F is the final structural phase of the ARS target architecture migration. Its goal is to align physical repository directory layouts with the logical taxonomy established across Waves A through E:

```text
Root Runtime Layout (Current)              Target Harmonized Layout (Wave F)
├── academic-paper/                 ──►   ├── skills/core/academic-paper/
├── academic-paper-reviewer/        ──►   ├── skills/core/academic-paper-reviewer/
├── deep-research/                  ──►   ├── skills/core/deep-research/
├── research-rabbit/                ──►   ├── skills/core/research-rabbit/
├── literature-matrix/              ──►   ├── skills/core/literature-matrix/
├── source-criticism/               ──►   ├── skills/core/source-criticism/
├── academic-pipeline/              ──►   ├── skills/core/academic-pipeline/
├── econ-write/                     ──►   ├── skills/domain/econ-write/
├── econ-models/                    ──►   ├── skills/domain/econ-models/
├── heterodox-economics-review/     ──►   ├── skills/domain/heterodox-economics-review/
├── political-economy-research/     ──►   ├── skills/domain/political-economy-research/
├── umass-applied-econometrics/     ──►   ├── skills/domain/umass-applied-econometrics/
├── public-scholarship/             ──►   ├── skills/dissemination/public-scholarship/
├── econ-slides/                    ──►   ├── skills/dissemination/econ-slides/
├── editor-jacobin-lat/scripts/     ──►   ├── tools/audit_columna/
└── [tools & shared protocols]      ──►   └── tools/ & shared/
```

### Task 1: Client Discoverability and Compatibility Strategy
- Analyze how client agents discover skills (e.g. Claude Code scanning top-level `*/SKILL.md` vs subdirectories).
- Determine whether root-level compatibility redirection stubs or configuration paths (`skills/` search paths) are required.
- Formulate a clear deprecation and transition schedule for any root-level paths.

### Task 2: Physical Migration Mapping & Phasing
- Map all 22 components in `docs/governance/ars_registry.yaml` from their current `runtime_path` to `target_path`.
- Plan migration in atomic, logical batches (e.g., Core Skills -> Domain Skills -> Dissemination Skills -> Tools).
- Identify cross-component relative links in Markdown documents and references that will require path updating.

### Task 3: Tool and Script Harmonization
- Plan relocation of `editor-jacobin-lat/scripts/audit_columna.py` to `tools/audit_columna/`.
- Plan physical disposition of `editor-jacobin-lat/` root directory once compatibility redirects are finalized.
- Address migration of planned tools (`irf-plotting`, `latex-compilation`).

### Task 4: CI, Test Runners & Manifest Updates
- Plan updates to `scripts/_ci_pytest_manifest.toml` (45 entries) for new test and module paths.
- Plan updates to `scripts/validate_ars_registry.py` and `scripts/test_routing_contract.py` once `runtime_path` equals `target_path` (transitioning Rule 8).
- Ensure zero loss of test coverage across all test tiers.

### Task 5: User Research Asset Preservation
- Design strict preservation procedures to ensure `econ-slides/slide_deck_Fondecyt/` and associated slide tests are quarantined and preserved with 100.0% cryptographic byte-for-byte fidelity throughout the physical migration of `econ-slides`.

### Task 6: Produce Wave F Execution Plan
- Write `docs/design/wave-f/WAVE_F_EXECUTION_PLAN.md` detailing:
  1. Plain-language architectural objectives and risk mitigations.
  2. Inventory of target path relocations.
  3. Client discoverability and compatibility mechanisms.
  4. CI and test suite update plan.
  5. User project preservation safeguards.
  6. Explicit human decision gates required before implementation.

---

## 4. Preservation of Invariants

- **Zero Physical Moves During Planning:** All files must remain at current locations during this planning turn.
- **Wave D & E Immutability:** Wave D and Wave E are closed; their logical contracts and decisions are permanent.
- **Micro Causal Inference Gap:** Capability `causal_inference_microeconometrics` remains an unassigned gap (`current_owner: null`).
- **Personalization Backlog:** Author profile `diego-public.md` remains deferred.
- **Deterministic Testing:** All test plans must remain offline and deterministic.

---

WAVE F PLANNING ONLY — IMPLEMENTATION REQUIRES HUMAN AUTHORIZATION
