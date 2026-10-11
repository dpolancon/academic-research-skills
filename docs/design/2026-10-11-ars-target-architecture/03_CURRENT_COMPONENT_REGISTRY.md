# ARS Current Component Registry & Classification Baseline

**Status:** Current-State Baseline & Classification Pass  
**Date:** 2026-10-11  
**Repository:** `c:\ReposGitHub\academic-research-skills` (`dpolancon/academic-research-skills`)  
**Scope:** Complete component audit across live working tree  

---

## 1. Ontology & Disposition Vocabulary

### 1.1 Component Ontology (Primary Type)
Every component in the repository is classified into exactly one primary type:
- `CORE_SKILL`: Reusable, domain-general scholarly reasoning or synthesis engine.
- `DOMAIN_SKILL`: Specialized disciplinary knowledge, methodological rules, or domain writing conventions.
- `DISSEMINATION_SKILL`: Translation of academic research into presentation or public-facing artifacts.
- `ORCHESTRATOR`: State machine and control plane governing transitions, gates, and handoffs without owning disciplinary reasoning.
- `PROFILE`: Declarative configuration layer containing author voice, advisor preferences, committee personas, or venue constraints.
- `TOOL`: Bounded, deterministic execution or verification script.
- `SHARED_PROTOCOL`: Cross-cutting invariant, contract, or schema governing multiple skills.
- `CLIENT_ADAPTER`: Discovery, installation, or environment mapping layer for external agent runners (Antigravity, Claude, Codex).
- `PROJECT_OVERLAY`: Manuscript-specific, dissertation-specific, or grant-specific data, models, or notes.
- `LEGACY_OR_DEPRECATION_CANDIDATE`: Outdated, redundant, or orphaned components proposed for retirement.

### 1.2 Disposition Vocabulary
- `KEEP_AS_IS`: Retained without structural modification.
- `KEEP_AND_EVOLVE`: Retained as canonical owner; evolved with upstream updates and hardening.
- `REFACTOR`: Substantive internal restructuring to isolate responsibilities or remove contaminants.
- `DECOMPOSE`: Broken down into multiple distinct components (e.g. separating profile from generic workflow).
- `MERGE`: Merged into another canonical component that already owns the capability.
- `DEMOTE_TO_PROFILE`: Converted into a declarative configuration profile.
- `DEMOTE_TO_TOOL`: Converted into a deterministic command-line script or verification utility.
- `DEMOTE_TO_PROTOCOL`: Converted into a shared invariant or contract under `shared/`.
- `MIGRATE_TO_SHARED`: Relocated to shared infrastructure.
- `DEPRECATE`: Marked for sunset; replaced by canonical owner.
- `REMOVE_AFTER_MIGRATION`: Deleted once consumers have migrated to canonical owners.
- `CANDIDATE_NEW_CAPABILITY`: Gap candidate proposed only after non-redundancy proof.

---

## 2. Top-Level Skill Registry (14 Components)

### 01. `deep-research`
- **Current Path(s):** `deep-research/`, `.agents/skills/deep-research/`, `.claude/skills/deep-research/`
- **Primary Type:** `CORE_SKILL`
- **Primary Capability:** Systematic literature discovery, multi-agent research synthesis, evidence mapping, and PRISMA reporting.
- **Secondary Capabilities:** Socratic research question mentoring, citation verification via APIs (Crossref, Semantic Scholar, arXiv, OpenAlex), risk of bias analysis, meta-analysis protocol.
- **Upstream Origin:** `Imbad0202/academic-research-skills` (v2.9.4)
- **Personalization Level:** None (pure upstream core).
- **Project-Specific Contamination:** None.
- **Overlap Risk:** Low. Bounded overlap with `academic-paper` literature strategist (which performs paper-specific gap fills).
- **Proposed Target Owner:** `skills/core/deep-research`
- **Disposition:** `KEEP_AND_EVOLVE`
- **Migration Priority:** P1
- **Evidence:** `deep-research/SKILL.md` (v2.9.4), 13 agents, 7 declared modes in `MODE_REGISTRY.md`. Pure methodological core.

---

### 02. `academic-paper`
- **Current Path(s):** `academic-paper/`, `.agents/skills/academic-paper/`, `.claude/skills/academic-paper/`
- **Primary Type:** `CORE_SKILL`
- **Primary Capability:** End-to-end academic manuscript authoring, structuring, and revision lifecycle.
- **Secondary Capabilities:** Style calibration, author voice adaptation, internal self-review (author pre-submission audit), bilingual abstract generation, LaTeX/PDF formatting.
- **Upstream Origin:** `Imbad0202/academic-research-skills` (v3.2.0)
- **Personalization Level:** None in core engine; contains hooks for local user style calibration.
- **Project-Specific Contamination:** None in skill definitions.
- **Overlap Risk:** **CRITICAL**. Overlaps heavily with `econ-write` (which also claims full economics paper drafting and section writing).
- **Proposed Target Owner:** `skills/core/academic-paper`
- **Disposition:** `KEEP_AND_EVOLVE` (established as the sole canonical owner of the academic manuscript authoring lifecycle; delegates economics disciplinary rules to `econ-write`).
- **Migration Priority:** P1
- **Evidence:** `academic-paper/SKILL.md` lines 18-25, 12-agent pipeline, 10 declared modes in `MODE_REGISTRY.md`.

---

### 03. `academic-paper-reviewer`
- **Current Path(s):** `academic-paper-reviewer/`, `.agents/skills/academic-paper-reviewer/`, `.claude/skills/academic-paper-reviewer/`
- **Primary Type:** `CORE_SKILL`
- **Primary Capability:** Simulated external, independent multi-perspective peer review and formal editorial adjudication.
- **Secondary Capabilities:** Re-review verification (R&R traceability matrix), reviewer calibration (AUC/FPR/FNR metrics), Socratic revision coaching, Devil's Advocate adversarial critique.
- **Upstream Origin:** `Imbad0202/academic-research-skills` (v1.10.0)
- **Personalization Level:** None.
- **Project-Specific Contamination:** None.
- **Overlap Risk:** **HIGH**. Overlaps with `PE-phd-committee` (which implements a parallel 3-referee review and memo workflow) and `advisor-reviewer` (which implements custom referee feedback).
- **Proposed Target Owner:** `skills/core/academic-paper-reviewer`
- **Disposition:** `KEEP_AND_EVOLVE` (established as the sole canonical owner of simulated external peer review; consumes committee and advisor profiles).
- **Migration Priority:** P1
- **Evidence:** `academic-paper-reviewer/SKILL.md`, 7 agents, 6 modes in `MODE_REGISTRY.md`, Schema 13 sprint contract hard gate.

---

### 04. `academic-pipeline`
- **Current Path(s):** `academic-pipeline/`, `.agents/skills/academic-pipeline/`, `.claude/skills/academic-pipeline/`
- **Primary Type:** `ORCHESTRATOR`
- **Primary Capability:** Full research-to-publication lifecycle state machine, checkpoint enforcement, and Material Passport tracking.
- **Secondary Capabilities:** Mandatory integrity gating (Stages 2.5 and 4.5), claim verification sampling, context-reset boundary persistence, process summary generation.
- **Upstream Origin:** `Imbad0202/academic-research-skills` (v3.12.0)
- **Personalization Level:** Low.
- **Project-Specific Contamination:** None.
- **Overlap Risk:** Medium. Must remain strictly an orchestrator; must not accumulate substantive writing, reviewing, or econometrics reasoning.
- **Proposed Target Owner:** `orchestrator/academic-pipeline` (or `skills/core/academic-pipeline` logically typed as ORCHESTRATOR).
- **Disposition:** `KEEP_AS_IS`
- **Migration Priority:** P0
- **Evidence:** `academic-pipeline/SKILL.md`, `docs/ARCHITECTURE.md` §2-§3, 10-stage state machine in `references/pipeline_state_machine.md`.

---

### 05. `econ-write`
- **Current Path(s):** `econ-write/`, `.agents/skills/econ-write/`, `.claude/skills/econ-write/`
- **Primary Type:** `DOMAIN_SKILL`
- **Primary Capability:** Authoritative economics disciplinary writing rules, section architecture (Introduction formula, Model, Data, Results), and prose standards (Cochrane, McCloskey, Shapiro).
- **Secondary Capabilities:** Bounded economics drafting/editing, LaTeX typography for economics, empirical identification reporting standards, referee response guidelines.
- **Upstream Origin:** `hanlulong/econ-writing-skill` + local enhancements.
- **Personalization Level:** Domain-adapted.
- **Project-Specific Contamination:** Minor (contains presentation tips that belong in `econ-slides` and referee response tips that duplicate review workflows).
- **Overlap Risk:** **CRITICAL**. Overlaps with `academic-paper` (creates ambiguity about who writes an economics paper), `econ-slides` (contains presentation guidance), and `prose-register-critic` (contains style/banned phrase rules).
- **Proposed Target Owner:** `skills/domain/econ-write`
- **Disposition:** `REFACTOR` (narrow to economics disciplinary policy, section architecture, and bounded prose editing; remove duplicated slide and peer-review workflows; integrate as domain dependency of `academic-paper`).
- **Migration Priority:** P1
- **Evidence:** `econ-write/SKILL.md` (745 lines), frontmatter line 3 claiming it handles all paper writing, thesis writing, presentations, and audits.

---

### 06. `umass-applied-econometrics`
- **Current Path(s):** `umass-applied-econometrics/`, `.agents/skills/umass-applied-econometrics/`, `.claude/skills/umass-applied-econometrics/`
- **Primary Type:** `DOMAIN_SKILL`
- **Primary Capability:** Applied time-series econometrics in political economy (forensic replication, integration-order governance, specification space mapping, Toda–Yamamoto VAR).
- **Secondary Capabilities:** Embedded Toda–Yamamoto protocol, embedded cointegration audit protocol, Marglin descriptive macro grounding, small-sample macro bootstrapping.
- **Upstream Origin:** Local creation (Diego Polanco).
- **Personalization Level:** Highly personalized to UMass Amherst economics department traditions.
- **Project-Specific Contamination:** **HIGH**. 
  - Rule H.2 hardcodes specific historical regime signatures ($\hat{\gamma} \approx 1$ balanced Fordist mechanization, $\hat{\gamma} \gg 1$ post-Fordist machinery acceleration).
  - Rule H.4 hardcodes an empirical interpretation: *"For peripheral economies, interpret failures to cointegrate as evidence of structural regime-switching (e.g. FX-constrained accumulation) rather than data deficiency."*
  - References `09_papers_PDF` folder, `AshBasuDube2017.pdf`, `HAP2014.pdf`.
- **Overlap Risk:** **HIGH**. Embedded tools (`tools/cointegration_specification_audit.md`, `tools/toda_yamamoto_specification_mapping.md`) duplicate deterministic scripts; writing rules duplicate `econ-write` and `prose-register-critic`.
- **Proposed Target Owner:** `skills/domain/applied-econometrics-pe` + `tools/econometrics/*`
- **Disposition:** `REFACTOR` (extract embedded protocols into `tools/econometrics/`; purge epistemically biased rules that force empirical verdicts; generalize regime analysis; decouple from dissertation corpus paths).
- **Migration Priority:** P1
- **Evidence:** `umass-applied-econometrics/SKILL.md` lines 55-89, embedded tools paths lines 17-23.

---

### 07. `advisor-reviewer`
- **Current Path(s):** `advisor-reviewer/`, `.agents/skills/advisor-reviewer/`, `.claude/skills/advisor-reviewer/`
- **Primary Type:** `PROFILE` (currently misclassified as a standalone skill).
- **Primary Capability:** Durable advisor preferences of Michael Ash (econometric simplicity, cointegration residual honesty, Marglin descriptive grounding, workplace micro-mechanisms).
- **Secondary Capabilities:** Diagnostic review against dissertation feedback matrix.
- **Upstream Origin:** Local creation (Diego Polanco).
- **Personalization Level:** Highly personalized.
- **Project-Specific Contamination:** **CRITICAL**.
  - Explicitly states in line 8: *"This skill calibrates... for the Critical Replication of Shaikh's capacity utilization chapter."*
  - Hardcodes `CH1_CriticalReplication.pdf`, `Feedback_Matrix.xlsx` with 68 items, Page 17 ("labor capacity" $\to$ "latent capacity"), Page 7 VECM comments (lines 88-90).
  - Hardcodes US economy 1947–2011, Section 3 and Section 4.3/4.6, Table 1 overaccumulation regime classification (lines 23, 33, 52-53, 97).
- **Overlap Risk:** **CRITICAL**. Duplicates peer-review workflow from `academic-paper-reviewer`; duplicates writing rules from `econ-write` and `umass-applied-econometrics`.
- **Proposed Target Owner:** `profiles/advisors/michael-ash` + project overlay in dissertation repository.
- **Disposition:** `DECOMPOSE` / `DEMOTE_TO_PROFILE` (extract reusable Michael Ash preferences into `profiles/advisors/michael-ash`; quarantine Chapter 1 dissertation specifics into project overlay; decommission standalone skill).
- **Migration Priority:** P1
- **Evidence:** `advisor-reviewer/SKILL.md` lines 8, 33, 52-53, 89-98.

---

### 08. `PE-phd-committee`
- **Current Path(s):** `PE-phd-committee/`, `.agents/skills/PE-phd-committee/`, `.claude/skills/PE-phd-committee/`
- **Primary Type:** `PROFILE` (currently misclassified as a standalone skill with an embedded review workflow).
- **Primary Capability:** Multi-member dissertation defense committee personas (Michael Ash, Deepankar Basu, Kevin Young).
- **Secondary Capabilities:** Pre-defense written referee reports simulation, verbal Socratic defense simulation.
- **Upstream Origin:** Local creation (Diego Polanco).
- **Personalization Level:** Highly personalized.
- **Project-Specific Contamination:** **HIGH**.
  - Hardcodes Kevin Young directives for specific step-shift dummies ($s_1, s_2, s_3$ for 1956, 1974, 1980) from Diego's Chapter 1 (lines 34-39, 112-115).
  - Hardcodes Deepankar Basu directives for Bernoulli ODE linearization ($v = \hat{k}^{-1}$) and Appendix derivations from Chapter 1 (lines 27, 108).
- **Overlap Risk:** **CRITICAL**. Duplicates the entire peer-review panel workflow, EIC synthesis, referee reports, and Socratic coaching from `academic-paper-reviewer`.
- **Proposed Target Owner:** `profiles/committees/umass-pe` (consumed by a generic defense mode in `academic-paper-reviewer`).
- **Disposition:** `DECOMPOSE` / `DEMOTE_TO_PROFILE` (extract committee member profiles into `profiles/committees/umass-pe`; route defense simulation through `academic-paper-reviewer`; purge dissertation-specific ODE/dummy rules).
- **Migration Priority:** P1
- **Evidence:** `PE-phd-committee/SKILL.md` lines 34-39, 45-51, 56-58, 108-115.

---

### 09. `heterodox-economics-review`
- **Current Path(s):** `heterodox-economics-review/`, `.agents/skills/heterodox-economics-review/`
- **Primary Type:** `DOMAIN_SKILL`
- **Primary Capability:** Mathematical and dynamical systems consistency checks for Post-Keynesian and Sraffian macro models.
- **Secondary Capabilities:** Singularity checks ($\mu \to 1$), boundary conditions, Harrodian instability vs Smithian investment functions.
- **Upstream Origin:** Local creation (Diego Polanco).
- **Personalization Level:** Highly personalized to Diego's working paper on Sraffian Supermultiplier refutation.
- **Project-Specific Contamination:** **HIGH**. 
  - Entire 29-line file is tailored to Diego's specific paper refuting Shaikh's/SSM capacity utilization models (`paper_refutation_SSM`).
  - Lacks general Post-Keynesian, Kaleckian, Marxian, or stock-flow consistent modeling frameworks.
- **Overlap Risk:** Medium. Narrow fragment that should be part of a comprehensive heterodox macro modeling domain layer.
- **Proposed Target Owner:** `skills/domain/heterodox-macro-modeling`
- **Disposition:** `REFACTOR` / `KEEP_AND_EVOLVE` (redesign and broaden into a full heterodox macro modeling domain skill covering growth, distribution, Marxian reproduction, Sraffian pricing, dynamic systems, and SFC principles).
- **Migration Priority:** P2
- **Evidence:** `heterodox-economics-review/SKILL.md` lines 8-24.

---

### 10. `prose-register-critic`
- **Current Path(s):** `prose-register-critic/`, `.agents/skills/prose-register-critic/`, `.claude/skills/prose-register-critic/`
- **Primary Type:** `SHARED_PROTOCOL` + `TOOL` (currently misclassified as a standalone core skill).
- **Primary Capability:** Cross-cutting prose discipline protocol (protecting Category A technical vocabulary, reviewing Category B, rewriting Category C rhetorical scaffolding).
- **Secondary Capabilities:** Evidential claim-strength verb calibration (matching verbs to empirical designs: descriptive, Granger causality, VECM, GIRF); detection of internal pipeline metadata leakage.
- **Upstream Origin:** Local creation (Diego Polanco, v2.1.0).
- **Personalization Level:** Medium (contains Diego's Spanish-to-English translation calques and preferred political economy terms).
- **Project-Specific Contamination:** Low to Medium (contains specific terms from Chapter 1 such as "admissibility gates", "empirical object").
- **Overlap Risk:** **HIGH**. Overlaps with `econ-write` prose rules and `academic-paper` writing quality check (`references/writing_quality_check.md`).
- **Proposed Target Owner:** `shared/protocols/prose_discipline_protocol.md` + `tools/prose/*` + `profiles/author/diego-academic`
- **Disposition:** `DECOMPOSE` / `DEMOTE_TO_PROTOCOL` (protocol lives in `shared/protocols/`; regex/scanners live in `tools/prose/`; author calques live in `profiles/author/`; consumed by `econ-write` and `academic-paper`).
- **Migration Priority:** P1
- **Evidence:** `prose-register-critic/SKILL.md` lines 15-32, 78-84, 114-116, 147.

---

### 11. `editor-jacobin-lat`
- **Current Path(s):** `editor-jacobin-lat/`, `.agents/skills/editor-jacobin-lat/`, `.claude/skills/editor-jacobin-lat/`
- **Primary Type:** `DISSEMINATION_SKILL` (with an embedded venue profile).
- **Primary Capability:** Public scholarship translation (de-specialization of dense academic arguments, contemporary hooking, institutional mechanism explanation).
- **Secondary Capabilities:** Jacobin América Latina editorial formatting (declarative thesis headlines without subtitles, 1,500-2,500 words, Martín Arboleda criteria).
- **Upstream Origin:** Local creation (Diego Polanco).
- **Personalization Level:** Highly personalized to Jacobin América Latina and Martín Arboleda.
- **Project-Specific Contamination:** Medium (hardcodes specific citations like Isabella Weber 2024 interview, Polanco 2022 input-output, Barredo-Zuriarrain).
- **Overlap Risk:** High risk of genre conflation (equating general public scholarship with one specific venue's style guide).
- **Proposed Target Owner:** `skills/dissemination/public-scholarship` (skill) + `profiles/venues/jacobin-lat` (profile).
- **Disposition:** `DECOMPOSE` (extract generic public scholarship translation into `public-scholarship`; isolate Jacobin rules and Martín Arboleda criteria into `profiles/venues/jacobin-lat`).
- **Migration Priority:** P2
- **Evidence:** `editor-jacobin-lat/SKILL.md` lines 15-30, 35-44.

---

### 12. `econ-slides`
- **Current Path(s):** `econ-slides/`, `.agents/skills/econ-slides/`, `.claude/skills/econ-slides/`
- **Primary Type:** `DISSEMINATION_SKILL`
- **Primary Capability:** Production and verification of academic economics Beamer presentation slide decks (seminars, conferences, job talks, discussants).
- **Secondary Capabilities:** Slide structure planning, exhibit surgery (cropping/refining tables/figures), speaker scripts, LaTeX compile checking (`check_deck.py`, `compile_deck.py`).
- **Upstream Origin:** `hanlulong/econ-writing-skill` (slide component) + local adaptation.
- **Personalization Level:** Medium.
- **Project-Specific Contamination:** **HIGH in subdirectories**.
  - Contains `slide_deck_Fondecyt/` (committed local grant project presentation files).
  - Contains `references/working-session-grant-talks.md` calibrated for Fondecyt PK land-rent benchmark.
- **Overlap Risk:** Medium. Minor overlap with `econ-write` presentation section.
- **Proposed Target Owner:** `skills/dissemination/econ-slides`
- **Disposition:** `KEEP_AND_EVOLVE` (establish as canonical owner of scholarly presentations; sanitize project-specific Fondecyt slides into project repo; absorb presentation advice from `econ-write`).
- **Migration Priority:** P1
- **Evidence:** `econ-slides/SKILL.md`, `econ-slides/slide_deck_Fondecyt/`, `UPDATE_REGISTRY.md` REG-002.

---

### 13. `irf-plotting`
- **Current Path(s):** `irf-plotting/`, `.agents/skills/irf-plotting/`, `.claude/skills/irf-plotting/`
- **Primary Type:** `TOOL` (currently misclassified as a top-level skill).
- **Primary Capability:** Publication-grade Impulse Response Function (IRF & GIRF) plotting and reporting for VAR, SVAR, and TVAR models.
- **Secondary Capabilities:** Formatting to CJE, JPKE, ROPE journal standards.
- **Upstream Origin:** Local creation (Diego Polanco).
- **Personalization Level:** Domain-adapted.
- **Project-Specific Contamination:** Low.
- **Overlap Risk:** Low. Can be called directly or invoked by econometrics skills.
- **Proposed Target Owner:** `tools/plotting/irf_plotting`
- **Disposition:** `DEMOTE_TO_TOOL` (reclassify as deterministic specialized tool interface; maintain CLI/Python wrapper callable by skills).
- **Migration Priority:** P2
- **Evidence:** `irf-plotting/SKILL.md` (bounded numerical/graphical utility; does not decide argument meaning).

---

### 14. `latex-compilation`
- **Current Path(s):** `latex-compilation/`, `.agents/skills/latex-compilation/`, `.claude/skills/latex-compilation/`
- **Primary Type:** `TOOL` (currently misclassified as a top-level skill).
- **Primary Capability:** Isolated LaTeX compilation workflow (latexmk/pdflatex), gitignoring auxiliary build artifacts, markdown backup generation.
- **Secondary Capabilities:** Build error diagnosis.
- **Upstream Origin:** Local creation.
- **Personalization Level:** Low.
- **Project-Specific Contamination:** Low.
- **Overlap Risk:** Low. Bounded utility consumed by `academic-paper`, `econ-write`, and `econ-slides`.
- **Proposed Target Owner:** `tools/latex/compile_workspace`
- **Disposition:** `DEMOTE_TO_TOOL` (reclassify as deterministic build tool; expose clean script interface).
- **Migration Priority:** P2
- **Evidence:** `latex-compilation/SKILL.md` (mechanical compilation utility).

---

## 3. Infrastructure, Shared Protocols & Candidate Components

### 15. `editorial-governance Phase 1`
- **Current Path(s):** 
  - `docs/design/2026-10-10-editorial-governance/` (8 design docs)
  - `shared/contracts/passport/editorial_governance.schema.json`
  - `shared/contracts/passport/revision_verification.schema.json`
  - `scripts/revision_guard.py`
  - `scripts/test_editorial_governance_schema.py`
  - `scripts/test_revision_guard.py`
  - `evals/gold/editorial_governance/`
- **Primary Type:** `SHARED_PROTOCOL` + `TOOL`
- **Primary Capability:** Durable persistence of human-adjudicated editorial decisions across multi-round revisions; authorization state gating (HELD/BLOCKED/PROPOSAL_ONLY/AUTHORIZED); source-role and intellectual ownership contract.
- **Secondary Capabilities:** Revision verification CLI (`revision_guard.py`), PASS/FAIL/INDETERMINATE semantics, regression evaluation fixtures.
- **Upstream Origin:** Local creation (Diego Polanco).
- **Personalization Level:** Abstracted from Chapter 1 editing lessons.
- **Project-Specific Contamination:** Low (generalized into abstract contracts).
- **Overlap Risk:** Moderate overlap with Material Passport schema and `academic-pipeline` integrity gates.
- **Proposed Target Owner:** `shared/contracts/editorial_governance/` + `tools/verification/revision_guard.py`
- **Disposition:** `REFACTOR` / `SIMPLIFY_AND_ABSORB` (preserve the 3-axis state model, source contract, and bounded diff authorization; simplify away the overengineered cryptographic DAG/receipt machinery; integrate into Material Passport as an optional extension).
- **Migration Priority:** P1
- **Evidence:** `docs/design/2026-10-10-editorial-governance/05_RECOMMENDED_ARCHITECTURE.md`, `scripts/revision_guard.py`.

---

### 16. Project Overlays & Experimental Artifacts
- **Current Path(s):**
  - `paper_refutation_SSM/` (Sraffian Supermultiplier paper draft, math proofs, review reports, style guides)
  - `user_testings/` (AK working paper, Obsidian vault configuration, cover letters, research statements)
  - `editing_memos/` (Doctoral writing memos, editorial laws, negative structural rules)
  - `writings_testing/` (POPGOV research statement)
  - `.env` (tracked configuration file)
- **Primary Type:** `PROJECT_OVERLAY`
- **Primary Capability:** Active and completed dissertation chapters, test cases, and candidate writings.
- **Secondary Capabilities:** Ad-hoc regression test grounds.
- **Upstream Origin:** Local researcher files.
- **Personalization Level:** 100% researcher-specific.
- **Project-Specific Contamination:** N/A (these are pure project files).
- **Overlap Risk:** Clutters canonical tool/skill repository; creates ambiguity about what is library infrastructure vs what is private dissertation data.
- **Proposed Target Owner:** Dedicated dissertation/research project repositories or quarantined `projects/` directory.
- **Disposition:** `QUARANTINE_AND_OFFLOAD` (maintain during Wave A-B; do not delete or modify in this pass; plan migration to external project repos or explicit test fixture directories).
- **Migration Priority:** P0 (for `.env` secret hygiene); P2 (for directory offloading).
- **Evidence:** `git ls-files paper_refutation_SSM user_testings editing_memos writings_testing .env`.

---

### 17. Client Adapter Mirrors
- **Current Path(s):**
  - `.agents/skills/*` (14 skill directories, Windows NTFS junctions to root)
  - `.claude/skills/*` (14 skill directories, Windows NTFS junctions to root)
  - `install-local.ps1`
  - `sync.ps1`
- **Primary Type:** `CLIENT_ADAPTER`
- **Primary Capability:** Multi-agent client discovery (Antigravity, Claude Code, Codex).
- **Secondary Capabilities:** Local workstation synchronization and conflict avoidance.
- **Upstream Origin:** Mixed (fork adapter setup).
- **Personalization Level:** Local workstation configuration (`desktop-bsb5hhv-swift-void`).
- **Project-Specific Contamination:** High (Git tracks all files inside `.agents` and `.claude` simultaneously, creating triple commits for every edit).
- **Overlap Risk:** **CRITICAL**. 3 physical copies of every skill file committed in git!
- **Proposed Target Owner:** `clients/antigravity/`, `clients/claude/`, `clients/codex/` (thin adapters/installers only).
- **Disposition:** `REFACTOR` (decouple public git tree from duplicated tracking; make junctions/mirrors generated by `install-local.ps1` and gitignored in the public repo).
- **Migration Priority:** P0
- **Evidence:** `git ls-files .agents .claude`, `install-local.ps1`, `UPDATE_REGISTRY.md` lines 41-46.

---

## 4. Component Classification Summary Matrix

| # | Current Component Name | Current Path(s) | Primary Type | Primary Capability | Upstream Origin | Personalization | Overlap Risk | Proposed Target Owner | Disposition | Priority |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | `deep-research` | `deep-research/` (+mirrors) | `CORE_SKILL` | Literature search & synthesis | Imbad0202 | None | Low | `skills/core/deep-research` | `KEEP_AND_EVOLVE` | P1 |
| 02 | `academic-paper` | `academic-paper/` (+mirrors) | `CORE_SKILL` | Manuscript authoring pipeline | Imbad0202 | None | Critical (`econ-write`) | `skills/core/academic-paper` | `KEEP_AND_EVOLVE` | P1 |
| 03 | `academic-paper-reviewer` | `academic-paper-reviewer/` (+mirrors) | `CORE_SKILL` | Simulated external peer review | Imbad0202 | None | High (`PE-phd-committee`) | `skills/core/academic-paper-reviewer` | `KEEP_AND_EVOLVE` | P1 |
| 04 | `academic-pipeline` | `academic-pipeline/` (+mirrors) | `ORCHESTRATOR` | 10-stage workflow control plane | Imbad0202 | Low | Medium | `orchestrator/academic-pipeline` | `KEEP_AS_IS` | P0 |
| 05 | `econ-write` | `econ-write/` (+mirrors) | `DOMAIN_SKILL` | Economics writing & section architecture | hanlulong + local | Domain-adapted | Critical (`academic-paper`) | `skills/domain/econ-write` | `REFACTOR` | P1 |
| 06 | `umass-applied-econometrics` | `umass-applied-econometrics/` (+mirrors) | `DOMAIN_SKILL` | PE applied econometrics & forensic replication | Local | High (UMass) | High (embedded tools) | `skills/domain/applied-econometrics-pe` | `REFACTOR` | P1 |
| 07 | `advisor-reviewer` | `advisor-reviewer/` (+mirrors) | `PROFILE` | Michael Ash advisor expectations | Local | Critical (Chapter 1) | Critical (reviewer/writer) | `profiles/advisors/michael-ash` | `DECOMPOSE` | P1 |
| 08 | `PE-phd-committee` | `PE-phd-committee/` (+mirrors) | `PROFILE` | Committee defense personas (Ash/Basu/Young) | Local | High (Chapter 1) | Critical (`academic-paper-reviewer`) | `profiles/committees/umass-pe` | `DECOMPOSE` | P1 |
| 09 | `heterodox-economics-review` | `heterodox-economics-review/` (+mirrors) | `DOMAIN_SKILL` | Heterodox macro dynamic consistency | Local | High (SSM paper) | Medium | `skills/domain/heterodox-macro-modeling` | `REFACTOR` | P2 |
| 10 | `prose-register-critic` | `prose-register-critic/` (+mirrors) | `SHARED_PROTOCOL` | Category A/B/C prose discipline & verb calibration | Local | Medium | High (`econ-write`, `academic-paper`) | `shared/protocols/prose_discipline_protocol` | `DEMOTE_TO_PROTOCOL` | P1 |
| 11 | `editor-jacobin-lat` | `editor-jacobin-lat/` (+mirrors) | `DISSEMINATION_SKILL` | Public scholarship de-specialization | Local | High (Jacobin AL) | High (venue lock-in) | `skills/dissemination/public-scholarship` | `DECOMPOSE` | P2 |
| 12 | `econ-slides` | `econ-slides/` (+mirrors) | `DISSEMINATION_SKILL` | Academic economics Beamer decks | hanlulong + local | Medium (Fondecyt) | Medium (`econ-write`) | `skills/dissemination/econ-slides` | `KEEP_AND_EVOLVE` | P1 |
| 13 | `irf-plotting` | `irf-plotting/` (+mirrors) | `TOOL` | Publication-grade IRF/GIRF generation | Local | Domain-adapted | Low | `tools/plotting/irf_plotting` | `DEMOTE_TO_TOOL` | P2 |
| 14 | `latex-compilation` | `latex-compilation/` (+mirrors) | `TOOL` | LaTeX build & md backup utility | Local | Low | Low | `tools/latex/compile_workspace` | `DEMOTE_TO_TOOL` | P2 |
| 15 | `editorial-governance Phase 1` | `shared/contracts/passport/*`, `scripts/*` | `SHARED_PROTOCOL` | Decision persistence & revision verification | Local | Abstracted | Moderate (Passport) | `shared/contracts/editorial_governance` | `REFACTOR` | P1 |
| 16 | Project Overlays | `paper_refutation_SSM/`, `user_testings/`, etc. | `PROJECT_OVERLAY` | Manuscript drafts, experimental runs, memos | Local | 100% | Medium (tree clutter) | External project repos / `projects/` | `QUARANTINE_AND_OFFLOAD` | P2 |
| 17 | Client Mirrors | `.agents/`, `.claude/`, `install-local.ps1` | `CLIENT_ADAPTER` | Multi-client discovery & local wiring | Local | Local workstation | Critical (triple tracking) | `clients/*` | `REFACTOR` | P0 |
