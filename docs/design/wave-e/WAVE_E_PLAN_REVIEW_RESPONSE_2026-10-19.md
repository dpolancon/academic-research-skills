# ARS WAVE E PLAN REVIEW RESPONSE RECORD

**Date:** 2026-10-19  
**Human Architect:** Diego Polanco  
**Repository:** `academic-research-skills` (`dpolancon/academic-research-skills`)  
**Working Branch:** `main`  
**Governing Implementation Checkpoint:** `27fbfd60255fe6c3cd99e7298c43a5189869163b`  
**Governing Plan Document:** [`docs/design/wave-e/WAVE_E_EXECUTION_PLAN.md`](WAVE_E_EXECUTION_PLAN.md)  
**Status:** REVISED PLAN DELIVERED — PENDING ARCHITECT RATIFICATION (NO IMPLEMENTATION AUTHORIZED)  

---

## 1. Context and Revision Purpose

Following the submission of the initial Wave E scope review, human architect Diego Polanco reviewed the proposed dissemination architecture and issued launcher instructions identifying nine specific corrections (A through I) required before implementation can be considered.

This record documents the exact disposition of each correction in the revised [`docs/design/wave-e/WAVE_E_EXECUTION_PLAN.md`](WAVE_E_EXECUTION_PLAN.md). In accordance with the governing boundaries:
- **No implementation, physical migration, commit, or push was authorized or performed.**
- **No historical Wave D records, executable skills, scripts, tests, profiles, registry, or routing files were modified.**
- **Untracked local user project files (`econ-slides/slide_deck_Fondecyt/`, `econ-slides/tests/`, `docs/design/2026-10-10-editorial-governance/`) remain completely intact and preserved.**

---

## 2. Correction-Resolution Mapping Table

| Item | Finding from Architect Review | Revised Plan Section | Supporting Local Evidence | Resolution Status | Remaining Uncertainty |
|:---:|:---|:---|:---|:---:|:---|
| **A** | Unsupported claim that "beyond Wave D/F" was merely colloquial; need explicit proposed human decision superseding earlier recorded deferral. | §2.1, §2.2, §2.3, §7 (Decision E-1) | [`05_TARGET_MIGRATION_ROADMAP.md`](../2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md);<br>[`D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md`](../wave-d/D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md) §0 item 6;<br>[`D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md`](../wave-d/D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md) §0 item G3 | **RESOLVED** | None. Roadmap and D0/D1 are presented as conflicting recorded instructions. Proposed Decision E-1 explicitly supersedes earlier deferral. Wave F remains separately authorized. |
| **B** | Lack of explicit provenance table separating generic craft, venue preferences, and commission-specific instructions; venue profile must not gain authority over substantive methods/evidence. | §3.1, §3.2 | [`editor-jacobin-lat/SKILL.md`](../../../editor-jacobin-lat/SKILL.md);<br>[`editor-jacobin-lat/references/criterios_martin_arboleda.md`](../../../editor-jacobin-lat/references/criterios_martin_arboleda.md);<br>[`editor-jacobin-lat/references/manual_estilo_jacobin.md`](../../../editor-jacobin-lat/references/manual_estilo_jacobin.md);<br>[`editor-jacobin-lat/checklists/rubrica_evaluacion_100.md`](../../../editor-jacobin-lat/checklists/rubrica_evaluacion_100.md);<br>[`editor-jacobin-lat/scripts/audit_columna.py`](../../../editor-jacobin-lat/scripts/audit_columna.py) | **RESOLVED** | None. Complete 6-column provenance table classifies all 7 candidate areas. The Venue Profile Boundary Principle (§3.2) explicitly bars venue profiles from overriding research findings. |
| **C** | Generic public skill was over-constrained to a single op-ed pattern; erroneous illustrative equivalence (`endogenous money → central bank accommodation`) must be removed and mechanisms faithfully simplified. | §1.3, §1.4, §4.1 | [`editor-jacobin-lat/references/glosario_desespecializacion.md`](../../../editor-jacobin-lat/references/glosario_desespecializacion.md) | **RESOLVED** | None. Generic skill now supports 4 distinct public genres. Contemporary anchors and class-relational framing are defined as available approaches, not mandatory gates. Erroneous shorthand removed; mechanism-faithful simplification mandated. |
| **D** | Auditor lacked bounded authority tiers; keyword matches were treated as proxies for substantive/causal validity; distinction needed between author prose and quotations. | §4.5 | [`editor-jacobin-lat/scripts/audit_columna.py`](../../../editor-jacobin-lat/scripts/audit_columna.py) | **RESOLVED** | None. Auditor bounded into 3 output tiers (mechanical failures, heuristic warnings, substantive review questions). Static scripts prohibited from claiming verification of causal warrant or evidence. |
| **E** | Arithmetic contradiction in component count ($20 + 2 = 22$, not 21); capability counts must not be inferred from component counts; routing identifiers and rules must be labeled as proposed. | §5.2, §5.3 | [`docs/governance/ars_registry.yaml`](../../governance/ars_registry.yaml);<br>[`docs/governance/ROUTING_AND_PRECEDENCE.md`](../../governance/ROUTING_AND_PRECEDENCE.md) | **RESOLVED** | None. Reconciled arithmetic: 20 $\to$ 22 components (17 active + 1 new skill + 1 new profile + 4 deprecated [including retyped `editor-jacobin-lat`]); exactly 22 capabilities. All rules (R17–18, ADV-E1–E4) and fixtures (ROUTE-027–030) marked as proposed. |
| **F** | Inconsistent auditor paths proposed (`scripts/`, `editor-jacobin-lat/scripts/`, symlinks); need single settled physical location. | §4.5, §5.1 | [`editor-jacobin-lat/scripts/audit_columna.py`](../../../editor-jacobin-lat/scripts/audit_columna.py) | **RESOLVED** | None. Settled canonical location for Wave E is `editor-jacobin-lat/scripts/audit_columna.py`, preserving existing invocations and avoiding premature file moves or symlinks before Wave F. |
| **G** | Slide presentation edit boundary was vague; need exact files inspected; preserve untracked grant files without implying permanent location. | §4.4, §5.1, §7 (Decision E-4) | [`econ-slides/SKILL.md`](../../../econ-slides/SKILL.md);<br>[`econ-slides/references/working-session-grant-talks.md`](../../../econ-slides/references/working-session-grant-talks.md);<br>`econ-slides/slide_deck_Fondecyt/`;<br>`econ-slides/tests/` | **RESOLVED** | None. Inspection confirmed `econ-slides` source and references are already project-agnostic. Wave E work is explicitly classified as verification-only. `slide_deck_Fondecyt/` and `tests/` preserved untouched. |
| **H** | Evaluation claims conflated static contract validation with live generative testing; need explicit negative fixtures. | §6.1, §6.2 | [`evals/gold/wave_d_behavioral/cases.yaml`](../../../evals/gold/wave_d_behavioral/cases.yaml);<br>[`scripts/test_routing_contract.py`](../../../scripts/test_routing_contract.py) | **RESOLVED** | None. Four distinct evaluation tiers defined. Live generative evaluation explicitly acknowledged as untested offline. Four concrete negative evaluation fixtures specified. |
| **I** | File inventory conflated existing and new files (e.g. `evals/gold/routing/cases.yaml` listed as new); unclear separation of protected and deferred surfaces. | §5.1 | Repository filesystem inspection | **RESOLVED** | None. File inventory structured into 5 unambiguous categories: Proposed New Files, Existing Files to Modify, Read-Only Dependencies, Protected Preserved Surfaces, and Deferred Work. |

---

## 3. Detailed Summary of Corrections

### Correction A: Sequencing Conflict Resolution
The revised plan (§2) removes any characterization of the Wave D deferral as "informal" or "colloquial." Both `05_TARGET_MIGRATION_ROADMAP.md` and the Wave D reconnaissance records (`D0` §0.6, `D1` §0.G3) are treated with equal textual authority as conflicting recorded instructions. The plan recommends Approach 1 (logical decomposition at root runtime paths first) and provides a concrete human decision (**Decision E-1**) to formally supersede the earlier deferral. Furthermore, it explicitly clarifies that Wave F remains independently authorized work and that closing Wave E does not automatically launch Wave F.

### Correction B: Candidate Provenance & Rule Classification
The revised plan (§3.1) adds a comprehensive provenance table tracing candidate rules from `editor-jacobin-lat` to their exact file and line origins. Candidates are strictly classified into generic standards, supported venue preferences, and commission-specific instructions:
- **Declarative headlines (max 12 words, no subtitles/colons):** Classified as a supported venue preference for *Jacobin AL* based on Martín Arboleda's direct feedback; generalized writing permits subtitles, colons, or questions.
- **Weber and sellers' inflation:** Classified as a commission-specific instruction stemming from the Unidad Popular / inflation essay commission; retained as an exemplar for inflation topics, but rejected as a mandatory gate for all articles.
- **Latin American country quotas ($\ge 2$ countries):** Demoted from a mechanical gate to an advisory review prompt for regional comparative pieces.
- **Venue Profile Boundary Principle (§3.2):** Explicitly codified that venue profiles govern rhetorical framing and style, possessing zero authority over empirical evidence, econometric admissibility, or substantive research conclusions.

### Correction C: Multi-Genre Reusability & Mechanism Simplification
The revised plan (§1.3, §1.4, §4.1) broadens `public-scholarship` beyond a single op-ed formula to support four distinct public genres (op-eds, explanatory essays, historical perspectives, and policy briefs). Contemporary hooks, structural thesis leads, and class-relational framing are repositioned as available techniques rather than universal obligations. The flawed shorthand `endogenous money → central bank accommodation` was completely eliminated; the standard now commands that simplification must faithfully preserve the specific causal mechanism and empirical qualifications of the source argument.

### Correction D: Bounded Column Auditor Authority
The revised plan (§4.5) defines three bounded output categories for `audit_columna.py`:
1. *Mechanical Failures:* Deterministic violations of explicit venue criteria (e.g., word count exceeding 12 words or presence of colons when Jacobin profile is active).
2. *Heuristic Warnings:* Review prompts for inspection (e.g., academic meta-phrases, anti-agitprop blacklist matches), explicitly distinguishing author prose from quoted material.
3. *Substantive Review Questions:* Prompts directing human or editorial review to matters static code cannot assess. Static scripts are explicitly prohibited from claiming verification of causal warrant or empirical validity.

### Correction E: Governance Registry Arithmetic Reconciliation
The revised plan (§5.2, §5.3) rectifies the component arithmetic:
- **Starting Components:** 20.
- **Additions:** `public-scholarship` (+1) and `venue-jacobin-lat` (+1).
- **Retyped:** `editor-jacobin-lat` is retained as a deprecated legacy stub (matching `advisor-reviewer` and `PE-phd-committee`).
- **Resulting Component Count:** Exactly $\mathbf{22}$ components ($20 + 2 = 22$).
- **Capability Count:** Exactly $\mathbf{22}$ capabilities (Capability 9 and 18 reallocated; zero new capabilities; causal inference gap preserved).
- Proposed rules (`R17`, `R18`, `ADV-E1`–`ADV-E4`) and routing fixtures (`ROUTE-027`–`ROUTE-030`) are explicitly labeled as proposed.

### Correction F: Settled Physical Location of Column Auditor
The revised plan (§4.5, §5.1) settles the physical location of `audit_columna.py` at its current location: `editor-jacobin-lat/scripts/audit_columna.py`. This avoids premature physical file reorganization prior to Wave F and prevents platform-dependent symlink issues on Windows.

### Correction G: Slide Presentation Scope Precision
The revised plan (§4.4, §5.1) records that direct inspection of `econ-slides/SKILL.md` and `econ-slides/references/` revealed zero project-specific dependencies. Consequently, Wave E work on slides is classified as **verification-only** (running existing tests against sample decks). Untracked directories (`econ-slides/slide_deck_Fondecyt/`, `econ-slides/tests/`) remain preserved and untouched in the local working tree.

### Correction H: Evaluation Limits & Negative Fixtures
The revised plan (§6.1, §6.2) establishes a four-tier evaluation model and explicitly notes that offline deterministic checks cannot evaluate live generative model adherence. Four concrete negative evaluation fixtures are specified: venue-rule leakage, commission-specific leakage, unsupported causal strengthening, and legacy redirection.

### Correction I: Consolidated Implementation Surface
The revised plan (§5.1) structures all repository surfaces into five mutually exclusive categories: Proposed New Files, Existing Files to Modify, Read-Only Dependencies, Protected Preserved Surfaces, and Deferred Work. Existing routing fixtures were moved from "new files" to "existing files to modify."

---

## 4. Overall Readiness of the Revised Plan

The revised execution plan in [`docs/design/wave-e/WAVE_E_EXECUTION_PLAN.md`](WAVE_E_EXECUTION_PLAN.md) is complete, methodologically sound, and aligned with all repository governance invariants. It provides a crisp, bounded roadmap for Wave E dissemination architecture while strictly insulating core domain methodology and user research files.

**Next Step:** The implementation package remains completely unstarted, awaiting formal review and ratification of the Proposed Human Decision Package (Decisions E-1 through E-5) by human architect Diego Polanco.

---

*REVIEW RESPONSE COMPLETE — PLAN REVISION DELIVERED — IMPLEMENTATION AWAITS AUTHORIZATION.*
