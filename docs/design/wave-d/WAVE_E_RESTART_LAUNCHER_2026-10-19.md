# AG LAUNCHER — WAVE E SCOPE RECONCILIATION & EXECUTION PLANNING

Work in:

`C:\ReposGitHub\academic-research-skills`

## 1. MISSION AND GOVERNING BOUNDARIES

Execute a **read-only assessment and scoping plan for Wave E (Dissemination Architecture & Public Scholarship)**.

Wave D is **CLOSED and RATIFIED** at checkpoint:

`27fbfd60255fe6c3cd99e7298c43a5189869163b`

### Proposed Purpose of Wave E
In plain language, Wave E organizes how academic research becomes public-facing writing and presentations while strictly preserving analytical rigor and evidence standards. It addresses:
1. Translating dense academic research into accessible public essays without vulgarizing theoretical mechanisms or fabricating empirical claims.
2. Decoupling generic public-scholarship prose translation from venue-specific editorial profiles (e.g., *Jacobin América Latina*).
3. Sanitizing and solidifying academic slide presentation production (`econ-slides`) while protecting active research presentations.

### Strict Scope Limits
- **READ-ONLY ASSESSMENT & WRITTEN PLAN ONLY.**
- **NO IMPLEMENTATION AUTHORIZED.**
- **NO DIRECTORY MOVES OR PHYSICAL MIGRATION (Wave F).**
- **NO DELETION OR MODIFICATION OF USER PROJECT FILES.**
- **NO NEW COMMIT OR PUSH.**

---

## 2. REQUIRED READING & BASELINE VERIFICATION

Read first:

1. [`docs/design/wave-d/ARS_SESSION_HANDOFF_POST_WAVE_D_2026-10-19.md`](ARS_SESSION_HANDOFF_POST_WAVE_D_2026-10-19.md) *(Authoritative restart context)*
2. [`docs/design/wave-d/WAVE_D_HUMAN_CLOSURE_2026-10-19.md`](WAVE_D_HUMAN_CLOSURE_2026-10-19.md) *(Wave D ratified closure record)*
3. [`docs/governance/ars_registry.yaml`](../../governance/ars_registry.yaml) *(Components and capability ontology)*
4. [`docs/governance/ROUTING_AND_PRECEDENCE.md`](../../governance/ROUTING_AND_PRECEDENCE.md) *(Capability routing precedence)*
5. [`docs/design/2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md`](../2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md) *(Original Wave E and Wave F roadmap specifications)*
6. Relevant deferral records:
   - [`docs/design/wave-d/D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md`](D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md) §0 item 6
   - [`docs/design/wave-d/D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md`](D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md) §0 item G3

Run read-only inspection:
- Verify branch is `main` and HEAD is `27fbfd60255fe6c3cd99e7298c43a5189869163b`.
- Verify `git status --short`. Confirm that untracked areas (`docs/design/2026-10-10-editorial-governance/`, `econ-slides/slide_deck_Fondecyt/`, `econ-slides/tests/`) remain intact.
- Inspect current dissemination surfaces:
  - `editor-jacobin-lat/SKILL.md` and `editor-jacobin-lat/references/`
  - `econ-slides/SKILL.md` and `econ-slides/references/`

---

## 3. CORE TASKS FOR THIS SESSION

### Task 1: Reconcile the Sequencing Conflict (Wave E vs. Wave F)
The incoming session must investigate and resolve the explicit timing contradiction across governing records:
1. **The Roadmap Specification:** [`05_TARGET_MIGRATION_ROADMAP.md`](../2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md) defines Wave E (P2) as preceding Wave F (P3), and states that Wave F depends on Waves A through E being completed and tested.
2. **The Deferral Statements:** Wave D records ([`D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md`](D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md) §0 item 6 and [`D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md`](D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md) §0 item G3) state that decomposing `editor-jacobin-lat` into generic public-scholarship is `DEFERRED — FUTURE AUTHORIZATION REQUIRED (beyond Wave D/F)`.
3. **The Authority & Source Analysis:** Identify the exact origin, rationale, and authority of each statement. Did the post-Wave-C handoff intentionally defer public scholarship until after physical tree cleanup, or was it an informal scope-limiter for Wave D?
4. **Sequencing Recommendation:** Recommend a coherent path forward:
   - *Option 1 (Roadmap Strict):* Plan and execute Wave E logical decomposition first (retaining root runtime paths per Rule 8), followed by Wave F physical migration.
   - *Option 2 (Wave F First):* Execute Wave F physical directory harmonization first, keeping `editor-jacobin-lat` intact as a dissemination skill, and perform public-scholarship decomposition subsequently.
   - *Option 3 (Partial Wave E):* Address `econ-slides` presentation boundaries and column auditing now, while keeping `editor-jacobin-lat` decomposition deferred.
   *Do not silently overturn any prior deferral without human approval.*

### Task 2: Differentiate Candidate Topics vs. Authorized Scope
Treat the following candidate topics as subjects for architectural analysis, NOT automatically authorized work:
- **Public-Scholarship Generalization:** Extracting generic public-writing translation rules from `editor-jacobin-lat`.
- **Venue-Profile Extraction:** Isolating Martín Arboleda editorial rules into `profiles/venues/jacobin-lat.md`.
- **Author-Style Calibration:** Formalizing `profiles/author/diego-public.md` (distinguishing it from academic voice).
- **Presentation Sanitization:** Quarantining project-specific slides (`slide_deck_Fondecyt/`) while maintaining working Beamer builds.
- **Column Audit Integration:** Integrating `scripts/audit_columna.py` into shared tool suites.

### Task 3: Produce the Wave E Execution Plan
Create `docs/design/wave-e/WAVE_E_EXECUTION_PLAN.md` containing:
1. **Plain-Language Value Proposition:** Practical benefit to scholarly and public dissemination.
2. **Included vs. Excluded Activities:** Crisp boundaries protecting core domain skills and research projects.
3. **Existing Components & Proposed Responsibility Changes:** Component-by-component analysis (`editor-jacobin-lat`, `econ-slides`).
4. **Target File Surfaces:** Planned file modifications, new files, and tests.
5. **Deterministic Verification Criteria:** Schemas, routing tests, and fixtures.
6. **Required Human Decisions:** Explicit list of decisions requiring human architect approval before any code or documentation edit is executed.

---

## 4. PRESERVATION OF INVARIANTS

- **No Domain Changes:** Waves D1–D4 are closed; do not touch `political-economy-research`, `heterodox-economics-review`, `umass-applied-econometrics`, or `historical_source_criticism_protocol.md`.
- **Preserve User Projects:** Do not delete, move, or rename `econ-slides/slide_deck_Fondecyt/`.
- **No Path Moves:** Client discoverability at live root paths remains binding until Wave F.
- **Deterministic Evaluation:** All planned checks must be offline and deterministic.

---

WAVE E SCOPE REVIEW ONLY — IMPLEMENTATION REQUIRES HUMAN AUTHORIZATION
