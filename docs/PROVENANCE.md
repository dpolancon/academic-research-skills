# Academic Research Skills (ARS) — Provenance & Upstream Lineage Record

**Status:** Wave A Provenance Audit Baseline  
**Date:** 2026-10-11  
**Repository:** `dpolancon/academic-research-skills` (Fork maintained by Diego Polanco)  
**License Decision Status:** **HOLD** (Awaiting explicit human decision)  

---

## 1. Executive Summary & Repository Identity

This repository serves as **Diego Polanco's maintained research copilot and computational infrastructure** for economics, applied econometrics, and political economy.

The repository is **not** a monolithic single-origin project. It is a multi-lineage distribution uniting:
1. **The ARS General Academic Research Core:** Inherited from Cheng-I Wu (`Imbad0202/academic-research-skills`), licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
2. **The Economics Writing & Presentation Suite:** Inherited and adapted from Lu Han (`hanlulong/econ-writing-skill` and `hanlulong/econ-slides-skill`), licensed under the permissive MIT License.
3. **Political Economy, Heterodox Modeling & Applied Econometrics Extensions:** Independently researched and authored by Diego Polanco (`dpolancon`).

---

## 2. Upstream Lineage Foundations

### Upstream 1: `Imbad0202/academic-research-skills`
- **Original Author:** Cheng-I Wu (Imbad0202)
- **Repository URL:** `https://github.com/Imbad0202/academic-research-skills`
- **License:** CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International)
- **Base Version in Fork:** v3.12.0
- **Scope Inherited:** Core research state machine (`academic-pipeline`), systematic literature research (`deep-research`), multi-perspective peer review (`academic-paper-reviewer`), general academic drafting (`academic-paper`), shared contracts, and execution harnesses.

### Upstream 2: `hanlulong/econ-writing-skill` & `hanlulong/econ-slides-skill`
- **Original Author:** Lu Han (hanlulong)
- **Repository URLs:**
  - `https://github.com/hanlulong/econ-writing-skill`
  - `https://github.com/hanlulong/econ-slides-skill`
  - `https://github.com/hanlulong/econ-paper-review-skill`
- **License:** MIT License
- **Base Tracking Evidence:** Fork integration commit `42f27ee` ("Integration with Econ-Writting Skills")
- **Scope Inherited:** Flagship economics writing guide synthesizing 50+ economists (`econ-write`), and academic Beamer slide deck architecture and themes (`econ-slides`).

### Local Maintainer & Author: `dpolancon/academic-research-skills`
- **Maintainer & Author:** Diego Polanco (dpolancon)
- **Repository URL:** `https://github.com/dpolancon/academic-research-skills`
- **Scope Authored:** UMass Amherst forensic applied econometrics (`umass-applied-econometrics`), heterodox dynamical model checks (`heterodox-economics-review`), dissertation review & committee profiles (`advisor-reviewer`, `PE-phd-committee`), public scholarship editorial guidelines (`editor-jacobin-lat`), prose register and AI-trace discipline protocol (`prose-register-critic`), specialized time-series plotting tools (`irf-plotting`), and LaTeX workspace tools (`latex-compilation`).

---

## 3. Component-by-Component Provenance Audit (14 Skills)

| Component | Path | Provenance Classification | Origin Repository | Upstream Author | Upstream License | Tracking Policy | Modification Status | Confidence |
|---|---|---|---|---|---|---|---|---|
| `deep-research` | `deep-research/` | `IMBAD_UPSTREAM` | `Imbad0202/academic-research-skills` | Cheng-I Wu | CC BY-NC 4.0 | `track-core` | Unmodified | HIGH |
| `academic-paper` | `academic-paper/` | `IMBAD_UPSTREAM` | `Imbad0202/academic-research-skills` | Cheng-I Wu | CC BY-NC 4.0 | `track-core` | Unmodified | HIGH |
| `academic-paper-reviewer` | `academic-paper-reviewer/` | `IMBAD_UPSTREAM` | `Imbad0202/academic-research-skills` | Cheng-I Wu | CC BY-NC 4.0 | `track-core` | Unmodified | HIGH |
| `academic-pipeline` | `academic-pipeline/` | `IMBAD_UPSTREAM` | `Imbad0202/academic-research-skills` | Cheng-I Wu | CC BY-NC 4.0 | `track-core` | Unmodified | HIGH |
| `econ-write` | `econ-write/` | `HANLULONG_UPSTREAM` | `hanlulong/econ-writing-skill` | Lu Han | MIT | `track-selectively` | Locally adapted | HIGH |
| `econ-slides` | `econ-slides/` | `HANLULONG_UPSTREAM` | `hanlulong/econ-slides-skill` | Lu Han | MIT | `track-selectively` | Locally adapted | HIGH |
| `umass-applied-econometrics` | `umass-applied-econometrics/` | `LOCAL_ORIGINAL` | Local creation | Diego Polanco | Author-owned | `local-only` | Original work | HIGH |
| `heterodox-economics-review` | `heterodox-economics-review/` | `LOCAL_ORIGINAL` | Local creation | Diego Polanco | Author-owned | `local-only` | Original work | HIGH |
| `advisor-reviewer` | `advisor-reviewer/` | `LOCAL_ORIGINAL` | Local creation | Diego Polanco | Author-owned | `local-only` | Original work | HIGH |
| `PE-phd-committee` | `PE-phd-committee/` | `LOCAL_ORIGINAL` | Local creation | Diego Polanco | Author-owned | `local-only` | Original work | HIGH |
| `editor-jacobin-lat` | `editor-jacobin-lat/` | `LOCAL_ORIGINAL` | Local creation | Diego Polanco | Author-owned | `local-only` | Original work | HIGH |
| `prose-register-critic` | `prose-register-critic/` | `LOCAL_ORIGINAL` | Local creation | Diego Polanco | Author-owned | `local-only` | Original work | HIGH |
| `irf-plotting` | `irf-plotting/` | `LOCAL_ORIGINAL` | Local creation | Diego Polanco | Author-owned | `local-only` | Original work | HIGH |
| `latex-compilation` | `latex-compilation/` | `LOCAL_ORIGINAL` | Local creation | Diego Polanco | Author-owned | `local-only` | Original work | HIGH |

---

## 4. Supporting Infrastructure & Tools Provenance

| Component / File | Provenance Classification | Primary Origin | Primary Author | License Status |
|---|---|---|---|---|
| `scripts/run_pipeline.py` | `IMBAD_UPSTREAM` | `Imbad0202/academic-research-skills` | Cheng-I Wu | CC BY-NC 4.0 |
| `scripts/cross_model_client.py` | `IMBAD_UPSTREAM` | `Imbad0202/academic-research-skills` | Cheng-I Wu | CC BY-NC 4.0 |
| `shared/*` (schemas & contracts) | `IMBAD_UPSTREAM` | `Imbad0202/academic-research-skills` | Cheng-I Wu | CC BY-NC 4.0 |
| `docs/ARCHITECTURE.md` | `IMBAD_UPSTREAM` | `Imbad0202/academic-research-skills` | Cheng-I Wu | CC BY-NC 4.0 |
| `scripts/revision_guard.py` | `LOCAL_ORIGINAL` | Local creation (Phase 1) | Diego Polanco | Author-owned |
| `install-local.ps1` | `MIXED_DERIVATION` | Adapted from local wiring | Diego Polanco | Author-owned / permissive |
| `sync.ps1` | `MIXED_DERIVATION` | Local conflict-avoidance tool | Diego Polanco | Author-owned / permissive |
| Root `README.md` | `MIXED_DERIVATION` | Upstream text + fork updates | Mixed | Textual contradiction present |

---

## 5. License Decision Status: HOLD

### Current Factual Situation:
1. **Root LICENSE File:** States `Copyright (c) 2026 Cheng-I Wu` under `CC BY-NC 4.0`.
2. **POSITIONING.md:** Declares `CC BY-NC 4.0` as the authoritative framework license, restricting commercial use to safeguard academic access.
3. **README.md (Line 192):** Contradictorily claims the project is licensed under `Apache 2.0`.
4. **hanlulong Material:** Governed by the `MIT License`, which requires preserving Lu Han's copyright notice.
5. **Diego Polanco Material:** Original works created by Diego Polanco, currently held without an explicit separate sub-license declaration.

### Explicit Decision:
**No license changes are executed in Wave A.** The root `LICENSE` file remains untouched.

### Questions Reserved for Human / Legal Determination:
- **Decision 1:** Does the repository maintain a unified **CC BY-NC 4.0** distribution license (per upstream ARS positioning) with explicit third-party MIT notices for Lu Han's components?
- **Decision 2:** Or does the repository adopt an explicit dual-licensing schema (e.g. CC BY-NC 4.0 for workflow content and prompts, Apache 2.0 / MIT for Python scripts and execution tools)?
- **Interim Action:** Update `README.md` and `POSITIONING.md` to remove the unqualified Apache 2.0 claim, stating truthfully that licensing varies by component and is currently on **HOLD** pending human determination.
