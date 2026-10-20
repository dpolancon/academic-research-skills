# ARS SESSION RESTART HANDOFF — POST-WAVE E CLOSURE

- **Date:** 2026-10-20
- **Repository:** `academic-research-skills` (`dpolancon/academic-research-skills`)
- **Working Branch:** `main`
- **Wave D Governing Checkpoint:** `27fbfd60255fe6c3cd99e7298c43a5189869163b`
- **Wave E Implementation Checkpoint (Checkpoint A):** `bf81d8e9b1b9a90415ae2884388d3bfdfa62d24d`
- **Commit Message (Checkpoint A):** `Complete Wave E dissemination architecture and acceptance verification`
- **Remote Publication State:** Pushed and verified on `origin/main` (`bf81d8e9b1b9a90415ae2884388d3bfdfa62d24d`)
- **Status:** WAVE E HUMAN-CLOSED — READY FOR WAVE F PHYSICAL MIGRATION PLANNING

---

## 1. Purpose and Governing Status

This handoff document establishes the authoritative restart context for any fresh AI session (ChatGPT or Antigravity) continuing work on the `academic-research-skills` (ARS) repository.

### Governing Status
- **Wave D Remains Formally Closed:** Wave D remains permanently human-closed and ratified at baseline checkpoint `27fbfd60255fe6c3cd99e7298c43a5189869163b`.
- **Wave E is Formally Closed:** On 2026-10-20, human architect Diego Polanco reviewed the implementation, completion report, and independent acceptance verification report, and ratified the closure of Wave E (Dissemination Architecture & Public Scholarship Logical Decomposition).
- **Published Implementation Baseline:** The accepted Wave E implementation and governance records are published on `origin/main` at commit [`bf81d8e9b1b9a90415ae2884388d3bfdfa62d24d`](https://github.com/dpolancon/academic-research-skills/commit/bf81d8e9b1b9a90415ae2884388d3bfdfa62d24d).
- **Next Session Objective:** The next session will focus exclusively on **Wave F physical directory harmonization scoping and planning**. Wave F physical directory relocation is **not** authorized. Code edits, file moving, and physical migrations are strictly forbidden.
- **Supersession Notice:** This handoff supersedes the post-Wave-D restart handoff ([`docs/design/wave-d/ARS_SESSION_HANDOFF_POST_WAVE_D_2026-10-19.md`](../wave-d/ARS_SESSION_HANDOFF_POST_WAVE_D_2026-10-19.md)) regarding active repository state.

---

## 2. Checkpoint Chain of Provenance

The repository's architectural evolution across Waves C, D, and E is anchored by verified Git commits on branch `main`:

```text
38f31af (feat(profiles): extract committee scholar calibrations)
   ↓
917ee2f (refactor(governance): reconcile Wave C legacy surfaces)
   ↓ [Wave D1–D5 implementation & D5.1 evaluation micro-repairs]
aa5283e (Freeze Wave D1–D5 baseline after D5.1 evaluation repairs)
   ↓ [Wave D6 governance reconciliation & dynamic capability regressions]
27fbfd6 (Reconcile Wave D6 governance and verify capability boundaries)  <-- Wave D Human Closure
   ↓ [Wave E logical decomposition, acceptance verification & gold fixtures]
bf81d8e (Complete Wave E dissemination architecture and acceptance verification)  <-- Wave E Implementation (Checkpoint A)
   ↓ [Wave E closure record, restart handoff, and Wave F planning launcher]
[HANDOFF_SHA] (Record Wave E human closure and Wave F restart handoff)  <-- Checkpoint B (HEAD)
```

1. **`27fbfd60255fe6c3cd99e7298c43a5189869163b`:** The final Wave D6 checkpoint closing Wave D, establishing capability monopoly boundaries and dynamic negative regressions.
2. **`bf81d8e9b1b9a90415ae2884388d3bfdfa62d24d`:** Checkpoint A containing the complete accepted Wave E implementation, registry v1.3.0, routing rules v1.3.0, column auditor, public scholarship skill, venue profile, and verification suites.
3. **`[HANDOFF_SHA]`:** Checkpoint B containing the human closure record, this restart handoff, annotated reports, and the Wave F planning launcher.

> [!NOTE]
> **Dynamic Self-Commit SHA Resolution:**
> In accordance with Git DAG invariants, a commit cannot record its own SHA prior to its creation. Checkpoint B's commit SHA (`HANDOFF_SHA`) can be resolved dynamically in any environment via:
> ```bash
> git log -1 --format=%H -- docs/design/wave-e/ARS_SESSION_HANDOFF_POST_WAVE_E_2026-10-20.md
> ```

---

## 3. Component and Capability Accounting

Against the authoritative registry [`docs/governance/ars_registry.yaml`](../../governance/ars_registry.yaml) (v1.3.0):

| Component / Capability Metric | Baseline (Post-Wave-D) | Wave E Changes | Accepted State (v1.3.0) |
|:---|:---:|:---:|:---:|
| **Operational Components** | 17 | −1 legacy retyping (`editor-jacobin-lat`)<br>+2 additions (`public-scholarship`, `venue-jacobin-lat`) | **18** |
| — *ACTIVE Lifecycle Status* | 15 | −1 retyping + 2 additions | **16** |
| — *PLANNED_MIGRATION (Tools)* | 2 | 0 changes (`irf-plotting`, `latex-compilation`) | **2** |
| **Deprecated Components** | 3 | +1 legacy retyping (`editor-jacobin-lat`) | **4** |
| **Total Components** | **20** | +2 net additions | **22** |
| **Total Capabilities** | **22** | 0 additions/deletions (reallocated Capabilities 9 & 18) | **22** |

### Accounting Breakdown:
- **16 Active Components:** `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`, `deep-research`, `econ-models`, `econ-slides`, `econ-write`, `heterodox-economics-review`, `literature-matrix`, `political-economy-research`, `public-scholarship`, `research-rabbit`, `source-criticism`, `umass-applied-econometrics`, `author-default` (profile), `committee-umass` (profile), `reviewer-standard` (profile), `venue-jacobin-lat` (profile).
- **2 Planned-Migration Tools:** `irf-plotting`, `latex-compilation`.
- **4 Deprecated Components:** `editor-jacobin-lat`, `advisor-reviewer`, `PE-phd-committee`, `prose-register-critic`.
- **22 Capabilities:** Exactly 21 capabilities owned by operational components. Exactly 1 capability remains an unassigned gap: `causal_inference_microeconometrics` (`current_owner: null`, `migration_status: CANDIDATE`).
- **Zero-Capability Deprecation Invariant:** All 4 deprecated components own exactly 0 capabilities.

---

## 4. Canonical Responsibilities and Root Runtime Paths

In accordance with Rule 8 (Client Discoverability & Runtime Paths), all components remain at live root runtime paths until Wave F physical harmonization:

1. **`public-scholarship` (DISSEMINATION_SKILL):**
   - **Runtime Path:** `public-scholarship/`
   - **Owned Capability:** `public_scholarship_translation`
   - **Scope:** Author-side translation of technical academic research into four non-academic public genres:
     1. *Contemporary Op-Ed:* 800–1,200 words, single thesis peg, hook-driven, rapid turnaround.
     2. *Explanatory Public Essay:* 1,500–3,000 words, deep conceptual mechanism unpacking, concrete everyday analogies.
     3. *Historical Perspective:* 1,200–2,500 words, archival and periodization context for contemporary debates.
     4. *Policy Brief:* 1,000–2,000 words, structured problem definition, institutional trade-offs, actionable options.
   - **Core References:**
     - [`despecialization_craft.md`](../../../public-scholarship/references/despecialization_craft.md): Ladder of abstraction, jargon elimination, concrete grounding.
     - [`public_genres.md`](../../../public-scholarship/references/public_genres.md): Structural contracts for the four non-academic genres.
     - [`epistemic_integrity.md`](../../../public-scholarship/references/epistemic_integrity.md): Claim ceilings, correlation vs. causation, non-findings discipline.

2. **Epistemic Integrity Core Principles:**
   - *Des-specialization Without Banalization:* Eliminating jargon does not mean flattening explanatory mechanisms.
   - *Faithful Mechanism Simplification:* Explaining the concrete institutional and material transmission path rather than replacing it with vague universal shorthand.
   - *Claim Ceilings:* The public essay cannot claim stronger epistemic certainty than the underlying academic paper. Empirical non-findings remain non-findings. Statistical association is never phrased as demonstrated causal intervention.

---

## 5. Modular Venue Profile, Legacy Stub & Retained Auditor

1. **Modular Venue Profile (`venue-jacobin-lat`):**
   - **Runtime Path:** `profiles/venues/jacobin-lat.md`
   - **Owned Capability:** `venue_jacobin_lat_editorial`
   - **Scope:** Calibrated to Martín Arboleda's editorial directives:
     - Analytical framing situated on class terrain (*bourgeois economics vs. critique of political economy*).
     - Declarative thesis headlines: $\le 12$ words, strictly no subtitles, no colons.
     - Anti-agitprop vocabulary discipline: arguments grounded in structural mechanisms rather than sloganized moral outrage.
     - Commission-specific flags: multi-country comparisons and Weber seller's inflation are commission-specific options disabled by default.

2. **Deprecated Compatibility Redirect Stub (`editor-jacobin-lat`):**
   - **Runtime Path:** `editor-jacobin-lat/SKILL.md`
   - **Status:** `DEPRECATED` (owns 0 capabilities).
   - **Behavior:** Issues a deprecation notice and delegates directly to `public-scholarship` calibrated with `profiles/venues/jacobin-lat.md`.

3. **Retained Auditor Tool (`editor-jacobin-lat/scripts/audit_columna.py`):**
   - **Runtime Path:** Retained at `editor-jacobin-lat/scripts/audit_columna.py` until Wave F.
   - **Three-Tier Output Model:**
     1. *Mechanical Failures (Hard Gates):* Formatting errors, missing title, subtitle in Jacobin mode, title word count $> 12$, text length underflow/overflow.
     2. *Heuristic Warnings (Review Prompts):* Academic cliché meta-phrases, technical jargon, quoted agitprop (`in_quote: True`), authorial slogans (`REVIEW_REQUIRED`).
     3. *Substantive Review Questions:* Qualitative prompts on empirical warrant, traceability, and class framing for human review.

---

## 6. Rule Boundaries and Architectural Invariants

- **Venue Profile Boundary Principle:** The venue profile calibrates rhetorical tone, structural framing, and presentation formatting. It has **zero authority** over underlying empirical evidence, quantitative methods, or scientific findings. A venue profile cannot force confirmation of rejected empirical hypotheses or invent historical facts.
- **Dissemination vs. Academic Writing Boundary:** `public-scholarship` translates completed academic findings into public genres. It does not replace manuscript drafting (`academic-paper`), economics disciplinary writing (`econ-write`), or academic peer review (`academic-paper-reviewer`).
- **Registry Invariants E-1 to E-3:** Enforced deterministically by [`scripts/validate_ars_registry.py`](../../../scripts/validate_ars_registry.py):
  - *Invariant E-1:* Exactly one active canonical dissemination skill (`public-scholarship`).
  - *Invariant E-2:* `editor-jacobin-lat` is deprecated, owns zero capabilities, and points to its canonical replacement.
  - *Invariant E-3:* Exactly one venue profile for Jacobin América Latina (`venue-jacobin-lat`), registered with valid schema and target consumer.

---

## 7. Verification Evidence & Reported Limitations

### Deterministic Verification Suite:
- **Registry Validator ([`scripts/validate_ars_registry.py`](../../../scripts/validate_ars_registry.py)):** All 22 components and 22 capabilities validated; Invariants E-1 through E-3 confirmed (exit code `0`).
- **Routing Contract Runner ([`scripts/test_routing_contract.py`](../../../scripts/test_routing_contract.py)):** 30/30 canonical cases pass (14 positive, 16 adversarial) with active dynamic rejection of invalid owners and unassigned gap (exit code `0`).
- **Column Auditor Unit Tests ([`tests/test_audit_columna.py`](../../../tests/test_audit_columna.py)):** 6/6 pytest unit tests pass covering generic and Jacobin modes, hard gates, and heuristic warnings (exit code `0`).
- **Dissemination Evals ([`scripts/test_wave_e_dissemination.py`](../../../scripts/test_wave_e_dissemination.py)):** 3/3 pytest items pass; 11 runtime anchors verified; rubric discrimination confirmed across 5 gold cases in [`evals/gold/wave_e_dissemination/cases.yaml`](../../../evals/gold/wave_e_dissemination/cases.yaml) (exit code `0`).
- **Slide Tooling Verification:** CLI smoke check (`check_deck.py --help`), theoretical template contract check (`theory-template-contract.py`), generic sample talk deck check (score 100 — ship), and sample talk script timing audit (22.5/30 min) pass cleanly.
- **CI Test Manifest Integration:** 45 manifest entries in [`scripts/_ci_pytest_manifest.toml`](../../../scripts/_ci_pytest_manifest.toml) validated and executed via [`scripts/run_ci_pytest_manifest.py`](../../../scripts/run_ci_pytest_manifest.py).

### Explicitly Declared Limitations:
1. **Live Generative Model Behavior Untested (`MODEL_BEHAVIOR_EXECUTION_PENDING`):** All evaluations are offline deterministic checks verifying schemas, anchor references, and rubric discrimination. Live conversational LLM output adheres to contracts only when run through an active execution harness.
2. **Slide Compilation & Visual Render Not Performed:** Offline checks verified sample talk artifacts; TeX toolchain compilation and 200 DPI visual rendering of slide decks were not performed.
3. **CI Execution Local Only:** Local runner execution is certified; hosted GitHub Actions status must be inspected via remote tools.

---

## 8. Protected Local Work & Privacy Boundary

- **Cryptographic Preservation:** All 142 untracked files across `econ-slides/slide_deck_Fondecyt/` (100 files), `econ-slides/tests/` (34 files), and `docs/design/2026-10-10-editorial-governance/` (8 files) were audited before and after Wave E implementation, confirming **100.0% SHA-256 byte-for-byte hash parity**.
- **Privacy Sanitization:** Raw JSON preservation audit files (`WAVE_E_PRESERVATION_MANIFEST_PRE_PASS.json` and `POST_PASS.json`) contain private filenames of the author's research grant. They remain untracked locally as audit evidence and are strictly excluded from public Git commits.
- **Grant Files Not Used as Inputs:** Zero files in `slide_deck_Fondecyt/` were modified or used as test inputs.

---

## 9. Deferred Capabilities & Invariants

- **Author-Style Profile Deferred:** `profiles/author/diego-public.md` was deliberately **not created** and remains deferred in the Personalization Backlog (Ratified Decision E-2).
- **Micro Causal Inference Gap Preserved:** Capability `causal_inference_microeconometrics` strictly retains `current_owner: null` and `migration_status: CANDIDATE`. Requests for micro causal identification (DID, IV, RDD, synthetic control) must reject all 22 components.

---

## 10. Authoritative Reading Order

To understand the repository state without reading redundant transcripts, read these documents in exact sequence:

1. [`docs/design/wave-e/ARS_SESSION_HANDOFF_POST_WAVE_E_2026-10-20.md`](ARS_SESSION_HANDOFF_POST_WAVE_E_2026-10-20.md) *(This restart handoff)*
2. [`docs/design/wave-e/WAVE_E_HUMAN_CLOSURE_2026-10-20.md`](WAVE_E_HUMAN_CLOSURE_2026-10-20.md) *(Ratified human closure record)*
3. [`docs/design/wave-e/WAVE_F_RESTART_LAUNCHER_2026-10-20.md`](WAVE_F_RESTART_LAUNCHER_2026-10-20.md) *(Wave F planning launcher)*
4. [`docs/governance/ars_registry.yaml`](../../governance/ars_registry.yaml) *(v1.3.0 machine-readable ontology)*
5. [`docs/governance/ROUTING_AND_PRECEDENCE.md`](../../governance/ROUTING_AND_PRECEDENCE.md) *(v1.3.0 routing contract)*
6. [`docs/design/wave-e/WAVE_E_COMPLETION_REPORT.md`](WAVE_E_COMPLETION_REPORT.md) *(Wave E implementation details)*
7. [`docs/design/wave-e/WAVE_E_ACCEPTANCE_VERIFICATION_2026-10-20.md`](WAVE_E_ACCEPTANCE_VERIFICATION_2026-10-20.md) *(Independent acceptance findings)*
8. [`docs/design/2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md`](../2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md) *(Target architecture roadmap for Wave F)*

---

## 11. Next-Session Perimeter: Wave F Initial Task and Strict Boundaries

### Initial Task for Fresh Session:
The incoming session must perform **read-only inspection and written migration planning for Wave F (Physical Directory Harmonization)**.

### Scope Boundaries for Wave F Planning:
1. **Physical Tree Analysis:** Audit the target layout specified in [`05_TARGET_MIGRATION_ROADMAP.md`](../2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md) (`skills/core/`, `skills/domain/`, `skills/dissemination/`, `tools/`).
2. **Client Compatibility Strategy:** Plan how client environments (Claude Code, Cursor, AG, human CLI) will discover skills post-migration (e.g., transition stubs, symlinks, or updated documentation).
3. **Tool Harmonization:** Plan relocation of tools (`editor-jacobin-lat/scripts/audit_columna.py`, `irf-plotting`, `latex-compilation`) to canonical `tools/` locations.
4. **CI & Verification Update Plan:** Plan the update of test runners, CI manifests, and anchors once paths change.

### Strict Prohibition:
- **NO PHYSICAL FILE MOVES OR DIRECTORY RENAMES.**
- **NO CODE OR REGISTRY MODIFICATIONS.**
- **NO COMMITS OR PUSHES.**
- **STOPPING TOKEN:** `WAVE F PLANNING ONLY — IMPLEMENTATION REQUIRES HUMAN AUTHORIZATION`.
