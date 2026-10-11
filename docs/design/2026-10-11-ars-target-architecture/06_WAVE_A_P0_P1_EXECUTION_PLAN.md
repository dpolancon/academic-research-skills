# ARS Wave A (P0/P1) First Safe Implementation Plan

**Status:** Proposed Execution Plan (Awaiting Human Approval)  
**Date:** 2026-10-11  
**Repository:** `c:\ReposGitHub\academic-research-skills` (`dpolancon/academic-research-skills`)  
**Scope:** Bounded repository identity, provenance audit, secret hygiene, and canonical-source stabilization (Gaps G01–G05)  
**Execution State:** **NOT EXECUTED** (Design Only)  

---

## 1. Safety Invariants & Pre-Conditions

1. **Strictly Bounded to Wave A (G01–G05):** Wave A contains exclusively repository identity, license provenance audit, secret hygiene, and canonical-source cleanup. Capability registry promotion and mode registry expansion are explicitly deferred to Wave B.
2. **No Substantive Skill Rewriting:** Wave A modifies zero academic writing rules, zero econometric methods, and zero theoretical models.
3. **Zero Involuntary Data Loss:** All operations that modify git tracking (`git rm --cached`) retain disk copies intact.
4. **No Breaking of Local Runner Paths:** Client junctions for Antigravity and Claude Code remain functioning locally on Windows.
5. **No Secret Inspection / Printing:** Secret values in `.env` must not be inspected, printed, or staged during design or execution.
6. **Explicit Rollback for Every Step:** Every action has an exact, copy-pasteable Git rollback command.
7. **Human Approval Gates:** Actions affecting public repository metadata, licensing decisions, or git tracking require explicit human sign-off before execution.

---

## 2. Itemized Change Specifications

### Action A.1 — Secret Hygiene: Current Tracking Untrack & Historical Exposure Assessment
- **Exact File(s):** `.env`, `.env.example`, `.gitignore`
- **Change Type:** Git index untracking + config update + conditional security branch
- **Reason:** The root working tree currently tracks `.env` in git (`git ls-files .env` returns `.env`), posing a configuration hygiene and credential exposure risk (Gap `G04`).
- **Detailed Operation:**
  - **Branch A: Current Tracking Hygiene:**
    1. Confirm `.env` is tracked in git index (`git ls-files .env`).
    2. Ensure `.env` is listed in `.gitignore` so local files are never automatically re-staged.
    3. Create `.env.example` documenting required variable names (`TOGETHER_API_KEY`, `GEMINI_API_KEY`, `DEFAULT_MODEL`, `DEFAULT_PROVIDER`) with placeholder values only.
    4. Run `git rm --cached .env` to untrack `.env` from git while preserving the local file on disk intact.
  - **Branch B: Possible Historical Exposure (Conditional):**
    5. Perform a safe commit-history audit to check when and where `.env` entered git history (e.g., `git log --oneline -- .env`), **WITHOUT printing or logging secret values**.
    6. **Conditional Action:** If live, valid API credentials entered Git history:
       - Require immediate credential revocation and rotation at provider consoles (Together AI, Google Gemini).
    7. **Separate Decision:** Determine whether Git history rewriting (e.g. `git filter-repo` / BFG) is warranted. History rewriting is **NOT** automatically authorized in Wave A; it is an independent, disruptive operational decision requiring explicit human sign-off.
- **Dependency:** None.
- **Verification Test:** 
  - `git ls-files .env` returns empty.
  - `Test-Path .env` returns `True` (file preserved locally on disk).
  - `Test-Path .env.example` returns `True`.
- **Rollback:** `git add .env`
- **Human Approval Required:** **YES**

---

### Action A.2 — Canonical Source Tree Hygiene & Narrow Client Mirror Cleanup
- **Exact File(s):** `.agents/skills/*`, `.claude/skills/*`, `.gitignore`, `install-local.ps1`
- **Change Type:** Git index untracking + ignore rules hardening
- **Reason:** Git currently tracks full duplicate copies of skills under `.agents/skills/*` and `.claude/skills/*` alongside the canonical root skills. Because these paths are wired as NTFS junctions on Windows, every single file edit produces triple modifications in `git status` (Gap `G05`, `C01`). The public repo must have **one canonical source tree**, with client paths generated or linked locally.
- **Invariant:** **No complete skill implementation is tracked more than once.** Thin client configuration files, adapters, or discovery config directly under `.agents` or `.claude` (such as `.claude/CLAUDE.md`, `.claude-plugin/`) remain permitted where justified.
- **Detailed Operation:**
  1. Add `.agents/skills/` and `.claude/skills/` to `.gitignore`.
  2. Run `git rm -r --cached .agents/skills .claude/skills` to remove duplicate skill blobs from git index tracking while preserving disk junctions and files.
  3. Verify `install-local.ps1` correctly creates or repairs directory junctions on demand without git re-staging them.
- **Dependency:** Action A.1.
- **Verification Test:**
  - `git ls-files .agents/skills .claude/skills` returns empty (narrow acceptance criterion).
  - Canonical root skills remain fully tracked (`git ls-files econ-write/SKILL.md` returns path).
  - `Get-Item .agents/skills/econ-write` verifies junction still points to root.
- **Rollback:** `git checkout HEAD -- .agents/skills .claude/skills`
- **Human Approval Required:** **YES**

---

### Action A.3 — License and Provenance Audit
- **Exact File(s):** `docs/design/2026-10-11-ars-target-architecture/08_LICENSE_AND_PROVENANCE_AUDIT.md` (audit report), `README.md`, `POSITIONING.md`, `NOTICE.md`, `LICENSE`
- **Change Type:** Provenance audit & documentation alignment (NO automatic license reassignment)
- **Reason:** Public documentation exhibits contradictory license statements (Gap `G02`). `README.md` lines 192–194 states: *"This project is licensed under the Apache 2.0 License."* In contrast, `POSITIONING.md` lines 7, 45 states: *"It is licensed under CC BY-NC 4.0... not an open source license."* Automatic dual-licensing cannot be assumed without formal provenance tracing.
- **Audit Classification of Repository Materials:**
  1. **Inherited from Imbad0202 upstream:**
     - Components: `deep-research`, `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`, `shared/`, `scripts/run_pipeline.py`, `scripts/cross_model_client.py`, `docs/ARCHITECTURE.md`, `MODE_REGISTRY.md`, `POSITIONING.md`, `LICENSE`, `NOTICE.md`.
     - Source repository: `https://github.com/Imbad0202/academic-research-skills`
     - Upstream Author: **Cheng-I Wu** (Imbad0202)
     - Source License: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
     - Known base version: v3.12.0
     - Local status: Unmodified or minimal wrapper integration.
     - License implication: Governed by CC BY-NC 4.0 (restricts commercial use).
     - Confidence: HIGH.
     - Required human decision: Confirm that all inherited upstream components remain under CC BY-NC 4.0 with explicit attribution to Cheng-I Wu.
  2. **Inherited / adapted from hanlulong upstream:**
     - Components: `econ-write`, `econ-slides`.
     - Source repositories: `https://github.com/hanlulong/econ-writing-skill`, `https://github.com/hanlulong/econ-slides-skill`, `https://github.com/hanlulong/econ-paper-review-skill`.
     - Upstream Author: **Han Lulong** (hanlulong).
     - Source License: MIT License.
     - Known base: Commit `42f27ee` integration.
     - Local status: Adapted with local extensions and presentation references.
     - License implication: Permissive MIT license allows reuse and adaptation provided the original MIT copyright notice is preserved.
     - Confidence: HIGH.
     - Required human decision: Determine how to preserve Han Lulong MIT copyright notices when distributing alongside CC BY-NC 4.0 materials.
  3. **Independently authored locally:**
     - Components: `umass-applied-econometrics`, `advisor-reviewer`, `PE-phd-committee`, `heterodox-economics-review`, `prose-register-critic`, `editor-jacobin-lat`, `irf-plotting`, `latex-compilation`, `editorial-governance Phase 1`, project overlays (`paper_refutation_SSM`, `user_testings`, `editing_memos`, `writings_testing`).
     - Source repository: `https://github.com/dpolancon/academic-research-skills`
     - Author: **Diego Polanco** (dpolancon).
     - Source License: Author-owned.
     - Local status: Original intellectual and empirical works.
     - License implication: The author possesses full copyright authority to license these works under CC BY-NC 4.0, MIT, Apache 2.0, or dual terms.
     - Confidence: HIGH.
     - Required human decision: The author must explicitly choose the desired licensing terms for local components.
  4. **Mixed / Derived infrastructure:**
     - Components: Root `README.md`, `install-local.ps1`, `sync.ps1`, `UPDATE_REGISTRY.md`.
     - Confidence: HIGH.
     - Required human decision: Reconcile contradictory public metadata (remove inaccurate Apache 2.0 claim in `README.md` or clearly scope it to build scripts only after human sign-off).
- **Name Correction Mandate:** Correct the upstream author name in all documentation from *Ching-In Wu* to **Cheng-I Wu**.
- **Boundaries:** This action performs an audit and documents options. It does **not** provide legal advice and does **not** re-license files during this pass.
- **Dependency:** None.
- **Verification Test:** Audit document records provenance, upstream licenses, confidence levels, and explicit human decision points for all 14 components.
- **Rollback:** N/A (audit document).
- **Human Approval Required:** **YES** (human decision required before modifying any license text).

---

### Action A.4 — Correct Security Ownership Links
- **Exact File(s):** `SECURITY.md`
- **Change Type:** Text / link update
- **Reason:** `SECURITY.md` line 18 directs vulnerability reports to `https://github.com/Imbad0202/academic-research-skills/security/advisories` (upstream maintainer Cheng-I Wu), rather than to this fork or an explicit security contact (Gap `G03`).
- **Detailed Operation:**
  1. Update reporting instructions in `SECURITY.md` to point to `https://github.com/dpolancon/academic-research-skills/security/advisories` (or maintainer contact email).
- **Dependency:** Action A.3.
- **Verification Test:**
  - Verify link points to `dpolancon` repository advisories.
- **Rollback:** `git checkout HEAD -- SECURITY.md`
- **Human Approval Required:** **NO** (mechanical link correction).

---

### Action A.5 — Record Provenance & Upstream Lineage
- **Exact File(s):** `docs/PROVENANCE.md`, `docs/UPSTREAMS.yaml`
- **Change Type:** New documentation and machine-readable upstream registry creation
- **Reason:** The repository lacks explicit tracking of which components derive from `Imbad0202/academic-research-skills`, which derive from `hanlulong/econ-writing-skill`, and which are local creations (Gap `G01`, `G15`).
- **Detailed Operation:**
  1. Create `docs/PROVENANCE.md` detailing the architectural ancestry of all 14 skills, explicitly attributing Cheng-I Wu (Imbad0202) and Han Lulong (hanlulong).
  2. Create `docs/UPSTREAMS.yaml` specifying base upstream repositories, tracking policies (`track-core`, `track-selectively`, `local-only`), and divergence notes.
- **Dependency:** Action A.3.
- **Verification Test:**
  - Validate `docs/UPSTREAMS.yaml` parses cleanly with `yaml.safe_load()`.
  - Confirm every skill in `README.md` has an entry in `docs/UPSTREAMS.yaml`.
- **Rollback:** Remove `docs/PROVENANCE.md` and `docs/UPSTREAMS.yaml`.
- **Human Approval Required:** **NO** (additive architectural documentation).

---

## 3. Wave A Execution Schedule & Gates

| Step | Action ID | Action Summary | Risk | Human Approval | Ready to Execute? |
|---|---|---|---|---|---|
| 1 | **A.1** | Secret hygiene (untrack `.env`, `.env.example`, check history branch) | Low | YES | Awaiting Approval |
| 2 | **A.2** | Untrack `.agents/skills` & `.claude/skills` mirrors (narrow criteria) | Medium | YES | Awaiting Approval |
| 3 | **A.3** | License and provenance audit (categorize sources, correct Cheng-I Wu) | Low | YES | Awaiting Approval |
| 4 | **A.4** | Fix `SECURITY.md` upstream advisory link | Low | NO | Ready (After A.3) |
| 5 | **A.5** | Create `PROVENANCE.md` & `UPSTREAMS.yaml` | Low | NO | Ready (After A.3) |

*(Note: Action A.6 for capability registry promotion and MODE_REGISTRY expansion has been removed from Wave A and transferred to Wave B.)*

---

## 4. Execution Command Reference (Dry Run Only — DO NOT EXECUTE)

```powershell
# ============================================================
# DRY RUN REFERENCE ONLY — DO NOT EXECUTE WITHOUT HUMAN APPROVAL
# ============================================================

# Step 1: Secret hygiene
# git rm --cached .env

# Step 2: Untrack client mirrors (narrow skill directories only)
# git rm -r --cached .agents/skills .claude/skills

# Step 3: Verify git status reflects only untracked cache removals
# git status --short
```
