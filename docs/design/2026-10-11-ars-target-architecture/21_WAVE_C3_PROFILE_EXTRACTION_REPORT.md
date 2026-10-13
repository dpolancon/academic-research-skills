# ARS — Wave C3: Minimal Scholar / Advisor Profile System Extraction Report

**Date:** 2026-10-13
**Status:** COMPLETE
**Commit Target:** `feat(profiles): extract committee scholar calibrations`
**Governing Baseline:** `617f982` (`feat(governance): add lightweight revision control contract`)
**Architecture Consolidation:** `C4_PROFILE_EXTRACTION_ABSORBED_BY_C3`

---

## 1. Baseline

* **Parent Commit:** `617f982` (Wave C2 lightweight editorial governance & revision guard implementation).
* **Git Status:** Working tree clean prior to C3 file additions; protected untracked directories (`docs/design/2026-10-10-editorial-governance/`, `econ-slides/slide_deck_Fondecyt/`, `econ-slides/tests/`) fully preserved untouched.
* **Architecture Lock:** Conforms strictly to decisions locked in `14_WAVE_C_DECOMPOSITION_DESIGN_REVIEW.md`, `15_WAVE_C_EXECUTION_PLAN.md`, and `16_WAVE_C_HUMAN_DECISION_LOCK.md`.

---

## 2. Scope Lock

The execution of Wave C3 was strictly constrained to:
* Extracting durable calibration knowledge from legacy skills `advisor-reviewer/` and `PE-phd-committee/` into modular profile records.
* Establishing the ARS Profile Contract (`profiles/PROFILE_CONTRACT.md`).
* Populating concrete scholar profiles for **exactly three** authorized scholars:
  1. `Michael Ash` (`profiles/scholars/michael-ash.md`)
  2. `Deepankar Basu` (`profiles/scholars/deepankar-basu.md`)
  3. `Kevin Young` (`profiles/scholars/kevin-young.md`)
* Creating a thin, referential active advisor role wrapper:
  * `Michael Ash` (`profiles/advisors/michael-ash.md`)
* Creating the declarative UMass Political Economy committee composition:
  * `profiles/committees/umass-pe.md`
* Providing three reusable future templates:
  * `profiles/templates/scholar-profile.md`
  * `profiles/templates/advisor-role.md`
  * `profiles/templates/committee-composition.md`
* Developing a deterministic profile validation test suite:
  * `scripts/test_profile_contract.py`
* **Forbidden Scope Respected:**
  * Zero web searches, automated corpus collection, or web browsing.
  * Zero automated persona inference or psychological speculation.
  * Zero new profiles for outside scholars, editors, referees, or candidates.
  * Zero migration of project-specific Chapter 1 payloads or dissertation drafts.
  * Zero modification of legacy skills (`advisor-reviewer/`, `PE-phd-committee/`, `academic-paper-reviewer/`, etc.).
  * Zero modification of runtime governance registries (`docs/governance/ars_registry.yaml`, routing).

---

## 3. Legacy Sources Inspected

The extraction process fully audited the following local repositories and design records:
1. `advisor-reviewer/SKILL.md`:
   * Section 1: Advisor (Michael Ash) Core Directives & Concerns (Econometric Simplification, Theoretical Definitions, Institutional Transmission Mechanisms, Descriptive Grounding).
   * Section 2: Literature Section Tone & Clarity ("Bring it down to earth").
   * Section 3: Numerical Examples & Pedagogical Counterfactuals ("Punchline Principle", stylized round numbers).
   * Section 4: Applied Econometrics in Political Economy (UMass Benchmark: forensic transparency, data-first visualization, balanced critique).
   * Section 5: Writing Structure & Clarity (IZA-UMass synthesis, active voice, BLUF).
   * Section 6: Preserving the Candidate's Marxist-Heterodox Style (Candidate-specific, isolated).
   * Section 7: Diagnostic Review Protocol (Dissertation draft references, spreadsheet matrix, isolated).
2. `PE-phd-committee/SKILL.md`:
   * Section 1: Committee Personas (Michael Ash Chair/Advisor; Deepankar Basu Internal Econometrics/Marxian; Kevin Young External History).
   * Section 2: Operational Modes (`pre-defense` written reports, `defense` verbal Socratic dialogue).
   * Section 3: Pre-Defense Workflow (Report structuring).
   * Section 4: Defense Mode Workflow (3-phase committee questioning, dialogue, verdict).
   * Section 5: Hardening Guidelines (Ban placeholder responses, adversarial Socratic follow-up, technical ODE/econometrics rigor, interdisciplinary historical grounding).
3. Design Foundations:
   * `docs/design/2026-10-11-ars-target-architecture/14_WAVE_C_DECOMPOSITION_DESIGN_REVIEW.md`
   * `docs/design/2026-10-11-ars-target-architecture/15_WAVE_C_EXECUTION_PLAN.md`
   * `docs/design/2026-10-11-ars-target-architecture/16_WAVE_C_HUMAN_DECISION_LOCK.md`

---

## 4. Evidence Classification Methodology

In accordance with Step 1 and Step 2 of the C3 specification, source material was decomposed using a formal evidentiary taxonomy:

| Classification | Definition | Target Artifact | Handling in C3 |
|:---------------|:-----------|:----------------|:---------------|
| `SCHOLAR_DURABLE` | Enduring empirical priors, modeling standards, and writing principles independent of project context. | `profiles/scholars/<person>.md` | Extracted and preserved with explicit confidence ratings. |
| `ADVISOR_ROLE_SPECIFIC` | Active supervisory relationship context, dissertation lifecycle boundaries, and role bindings. | `profiles/advisors/<person>.md` | Encapsulated in thin wrapper; references scholar profile. |
| `COMMITTEE_COMPOSITION` | Declarative multi-member panel roster, affiliations, and institutional roles. | `profiles/committees/umass-pe.md` | Encapsulated in declarative composition record; references scholar profiles. |
| `DIRECT_FEEDBACK_EVIDENCE` | Attributed supervisory directives documented in legacy guidance. | `profiles/scholars/michael-ash.md` | Preserved under Evidence Base / Durable Calibration. |
| `INFERRED_CALIBRATION` | Bounded methodological inference supported by repeated observations across sources. | `profiles/scholars/<person>.md` | Preserved under explicit Inferred Calibration sections. |
| `GENERIC_REVIEW_DUPLICATE` | Referee report formatting, Socratic dialogue simulation, verdict letters, review roadmaps. | Canonical `academic-paper-reviewer` | Excluded from profiles; delegated to canonical review owner. |
| `GENERIC_WRITING_DUPLICATE` | Active voice, BLUF, brevity, transition discipline. | Shared Prose Protocol (`shared/protocols/prose_discipline_protocol.md`) | Referenced generally; excluded from profile ownership. |
| `PROJECT_SPECIFIC` | Chapter 1 replication parameters, Shaikh ARDL specifications, 68-item feedback matrix, candidate draft paths. | External project workspace | Strictly excluded from durable profiles. |
| `UNSUPPORTED_PERSONA_SPECULATION` | Speculation regarding personality types, psychological traits, political affiliations, grading odds. | N/A | Strictly prohibited and rejected. |

---

## 5. Michael Ash Scholar Extraction

* **Target File:** [`profiles/scholars/michael-ash.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/scholars/michael-ash.md)
* **Status:** `CREATED`
* **Evidence Base:** Published empirical political economy research (Ash, Basu, & Dube 2017; Herndon, Ash, & Pollin 2014) and explicit supervisory directives from `advisor-reviewer/SKILL.md`.
* **Durable Principles Extracted:**
  1. *Forensic Transparency:* Explicit disclosure of data cleaning, sample exclusions, sample boundaries, weights, and outlier sensitivity.
  2. *Data-First Visualization (Marglin Emulation):* Inspection of raw trends and non-parametric plots (GDP, employment, capital stock) before parametric regressions.
  3. *Econometric Simplification & Cointegration Discipline:* Explicit definition of admissibility in accessible terms; economic meaning over specification counts; unvarnished reporting of residual nonstationarity (never hidden behind model selection criteria); awareness of attenuation bias from RHS measurement error.
  4. *Demystifying Workplace Micro-Mechanisms:* Breaking down the macro "black box" into concrete workplace conversions of capital to potential capacity, technical change, labor intensity, and class struggle. Dynamic second derivatives (acceleration terms) must be bounded by institutional rate limits.
  5. *Pedagogical Numerical Grounding:* Stylized round numbers, the "Punchline Principle" (demonstrating what is at stake with parameter shifts), and pedagogical counterfactuals.
  6. *Grounded Prose:* Removing academic posturing, adopting BLUF structure, active voice, and immediate technical definitions.

---

## 6. Michael Ash Advisor-Role Extraction

* **Target File:** [`profiles/advisors/michael-ash.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/advisors/michael-ash.md)
* **Status:** `CREATED`
* **Role Status:** `active`
* **Lifecycle Boundary:** `valid_until_event: dissertation_completion`
* **Design Execution:** Deliberately thin wrapper.
  * Imports canonical identity via `scholar_ref: ../scholars/michael-ash.md`.
  * Contains zero duplication of Michael Ash's intellectual profile.
  * Contains zero embedded review engines (`review_engine: academic-paper-reviewer`).
  * Enforces `calibration_only: true`.
  * Outlines transition policy upon dissertation completion (role archives, scholar profile remains permanently active).

---

## 7. Deepankar Basu Scholar Extraction

* **Target File:** [`profiles/scholars/deepankar-basu.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/scholars/deepankar-basu.md)
* **Status:** `CREATED`
* **Evidence Base:** Published scholarship in classical/Marxian political economy (Basu & Manolakos 2013; Ash, Basu, & Dube 2017) and committee evaluation standards in `PE-phd-committee/SKILL.md`.
* **Durable Principles Extracted:**
  1. *Classical & Marxian Foundations:* Surplus approach, capital accumulation, reproduction schemas, and Leontief fixed-coefficient production functions ($Y_t = \min \{ A_t L_t, \mu_t B_t K_t \}$) to prevent neoclassical smooth substitution and respect the Cambridge capital controversy.
  2. *Mathematical Consistency & Stability:* Rigorous derivation of ordinary differential equations (ODEs), dynamic stability conditions, trend-stabilized closures (supermultiplier dynamics), and boundary/singularity audits.
  3. *Dimensional Analysis:* Purging "log-dollars" errors by requiring logarithmic and transcendental functions to operate strictly on dimensionless ratios.
  4. *System-Level Cointegration Restrictions:* Johansen reduced-rank vector error-correction restrictions ($r=1$) and dynamic consistency between theoretical models and econometric time-series specifications.

---

## 8. Kevin Young Scholar Extraction

* **Target File:** [`profiles/scholars/kevin-young.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/scholars/kevin-young.md)
* **Status:** `CREATED`
* **Evidence Base:** Modern US political economy, Latin American political economy, and social movements scholarship; committee directives in `PE-phd-committee/SKILL.md`.
* **Durable Principles Extracted:**
  1. *Active History vs. Passive Backdrop:* Rejection of history as cosmetic narrative or ex-post curve-fitting; institutional shocks, social movements, and state policies operate as active regulators of macroeconomic dynamics.
  2. *Contextualization of Structural Breaks:* Mapping statistical step-shifts and dummy controls to concrete historical turning points:
     * Mid-1950s: post-Korean War defense budget adjustments, corporate planning consolidation, bureaucratic labor management.
     * 1970s: Bretton Woods collapse, OPEC oil shocks, global stagflation, corporate counter-offensives.
     * 1980s: Volcker interest-rate shock, deindustrialization, Reagan administration anti-labor policies, neoliberal wage repression.
  3. *Class Struggle & Elite Mobilization:* Power asymmetries between capital, organized labor, and the state as fundamental drivers of macroeconomic trajectories.
  4. *Interdisciplinary Engagement:* Integrating historical and archival records with quantitative empirical models.

---

## 9. Committee Composition

* **Target File:** [`profiles/committees/umass-pe.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/committees/umass-pe.md)
* **Status:** `CREATED`
* **Committee Roster:**
  * Chair and Primary Advisor: `Michael Ash` (`../scholars/michael-ash.md`) — `role: chair_and_advisor`, `status: active`.
  * Internal Economics Member: `Deepankar Basu` (`../scholars/deepankar-basu.md`) — `role: internal_member`, `status: active`.
  * External Member: `Kevin Young` (`../scholars/kevin-young.md`) — `role: external_member`, `status: active`.
* **Design Execution:** Declarative composition record.
  * Contains no embedded Socratic dialogue transcripts or defense state machines.
  * Delegates all review execution to `academic-paper-reviewer`.
  * Decoupled from editorial governance (Material Passport protocol).

---

## 10. Profile Contract

* **Target File:** [`profiles/PROFILE_CONTRACT.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/PROFILE_CONTRACT.md)
* **Status:** `CREATED`
* **Core Provisions:**
  * Defines the formal three-tier taxonomy (Scholar Identity, Contextual Advisor Role, Committee Composition).
  * Establishes strict architectural guardrails: profiles do not own capabilities, do not replace `academic-paper-reviewer`, do not authorize manuscript changes, and do not simulate human personalities.
  * Formulates the mandatory epistemic disclaimer:
    > "Profile-guided review approximates evidence-grounded calibration and must not be represented as the actual scholar's opinion."
  * Codifies the 5-tier Evidence Model (T1 Factual, T2 Direct Feedback, T3 Inferred Calibration, T4 Project Context, T5 Unsupported Speculation).
  * Codifies the Confidence Model (`HIGH`, `MEDIUM`, `LOW`) and the rule of parsimony (prefer omission over speculation).
  * Defines canonical YAML frontmatter schemas for Scholar, Advisor, and Committee entities.
  * Formalizes lifecycle and transition rules for active doctoral supervision.

---

## 11. Template / Shell System

* **Target Files:**
  1. [`profiles/templates/scholar-profile.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/templates/scholar-profile.md)
  2. [`profiles/templates/advisor-role.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/templates/advisor-role.md)
  3. [`profiles/templates/committee-composition.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/templates/committee-composition.md)
* **Design Execution:**
  * Enforces evidence-grounded authoring for future scholars, advisors, and committees.
  * Contains explicit prohibitions against persona invention, psychological traits, and capability ownership.
  * Includes standardized placeholders for future evidence categories (`published_work`, `direct_feedback`, `institutional_context`).
  * Provides complete schema examples and instructional markdown comments.

---

## 12. Direct Evidence vs. Inferred Calibration

ARS Wave C3 strictly enforces boundary separation between verified facts and bounded inferences:
* **Direct Evidence:**
  * Specific empirical guidelines from Ash et al. (2014, 2017) and Basu & Manolakos (2013).
  * Verbatim supervisory constraints recorded in legacy `SKILL.md` files (Marglin descriptive grounding, Leontief production formulation, dimensional log checks, 1956/1974/1980 historical break mapping).
  * Marked as `HIGH` confidence.
* **Inferred Calibration:**
  * Generalization of Michael Ash's pedagogical counterfactuals and "punchline principle" across empirical sections.
  * Deepankar Basu's dynamic stability checks generalized across ODE specifications.
  * Kevin Young's structural shock mapping generalized across time-series dummy variables.
  * Kept bounded, disciplined, and explicitly marked.

---

## 13. Project-Specific Material Excluded

All candidate-specific and chapter-specific artifacts were quarantined and excluded from durable profiles:
* `CH1_CriticalReplication.pdf` and specific section draft paths.
* Shaikh ARDL capacity utilization replication equations and empirical parameters.
* The 68-item revision matrix in `Feedback_Matrix.xlsx`.
* Specific candidate voice emulation directives (`profit_rate_chile.pdf`).
* Temporary LaTeX modification roadmaps and defense verdicts.
* Zero `projects/` directory or project payload was introduced into the repository.

---

## 14. Generic Review Machinery Excluded

Generic peer-review workflows present in legacy simulator skills were rejected from profiles and retained exclusively under `academic-paper-reviewer`:
* Referee report formatting (Summary, Major Critiques, Minor Comments).
* Verbal Socratic dialogue simulation and deliberation transcripts.
* Editorial Decision Letter issuance (Pass, Minor Revision, Major Revision).
* Revision roadmap compilation.

---

## 15. Unsupported Persona Speculation Rejected

Strict prohibitions were enforced across all profile artifacts:
* **Zero Personality Typology:** No Myers-Briggs types, psychological profiles, or emotional traits.
* **Zero Ideological Labeling:** No political party preferences, private voting records, or unstated dogmas.
* **Zero Predictive Behavior:** No subjective grading likelihoods or paper acceptance/rejection probabilities.
* **Zero Conversational Tone Invention:** No simulation of interpersonal demeanor, combativeness, or colloquial speech.

---

## 16. Validator Coverage

A dedicated deterministic verification suite was authored in [`scripts/test_profile_contract.py`](file:///c:/ReposGitHub/academic-research-skills/scripts/test_profile_contract.py).

The suite verifies 19 assertions:
1. `Assertion 1 & 14`: Exactly three approved scholar profiles exist (`michael-ash.md`, `deepankar-basu.md`, `kevin-young.md`) with zero extraneous profiles.
2. `Assertion 2`: Michael Ash advisor wrapper exists.
3. `Assertion 3`: UMass PE committee composition exists.
4. `Assertion 4 & 5`: Advisor `scholar_ref` resolves to `michael-ash.md` on disk.
5. `Assertion 7`: Michael Ash advisor `role_status` is `active`.
6. `Assertion 8`: Advisor `valid_until_event` is `dissertation_completion`.
7. `Assertion 9`: Advisor wrapper is `calibration_only: true`.
8. `Assertion 10`: Advisor wrapper delegates `review_engine` to `academic-paper-reviewer`.
9. `Assertion 6`: All 3 committee member `scholar_ref` links resolve on disk.
10. `Assertion 15`: Committee composition delegates `review_engine` to `academic-paper-reviewer` without embedding simulation tokens.
11. `Assertion 11`: All 5 profile IDs are globally unique.
12. `Assertion 12`: All 3 reusable templates exist in `profiles/templates/`.
13. `Assertion 13`: Scholar profiles contain required sections (`Evidence Base`, `Evidence Confidence`, `Exclusions / Non-Inferences`, `Provenance`).
14. `Assertion 16`: No profile claims canonical capability ownership (`owns_capability`).
15. `Assertion 17`: No prohibited persona fields detected in frontmatter (`personality_type`, `political_preference`, etc.).
16. `Assertion 18`: Prohibited `projects/` directory does not exist.
17. `Assertion 19`: Scholar template includes explicit quality prompts and future evidence seams.

**Test Result:** `ALL PROFILE CONTRACT ASSERTIONS PASSED (19/19)`

---

## 17. Runtime Wiring Status

* **Status:** `NOT_STARTED` (Profiles operate as static calibration records only).
* In accordance with Step 15 and Step 20, runtime skills (`academic-paper-reviewer/SKILL.md`, `academic-paper/SKILL.md`) were **NOT** modified.
* Governance registry (`docs/governance/ars_registry.yaml`) was **NOT** modified.
* Routing contract (`docs/governance/ROUTING_AND_PRECEDENCE.md`) was **NOT** modified.
* Runtime consumption wiring is deferred to Wave C5 governance reconciliation.

---

## 18. Legacy Surface Status

* **Legacy Skills Preserved:**
  * `advisor-reviewer/` (`SKILL.md`): Unchanged, unmodified (99 lines intact).
  * `PE-phd-committee/` (`SKILL.md`): Unchanged, unmodified (117 lines intact).
* No legacy skill was deleted, redirected, stubbed, or modified during C3. Full deprecation and stubbing will occur in Wave C5.

---

## 19. Future Personalization Status

Wave C3 establishes the foundation for future profile extensions while strictly scoping current deliverables:
* **Completed in C3:** Curated, static markdown profile records, explicit evidence tiers, and standardized frontmatter.
* **Deferred to Backlog (`10_FUTURE_PERSONALIZATION_BACKLOG.md`):**
  * Automated corpus-based profile extraction tools (`ars-profile-builder`).
  * External publication retrieval / citation scrapers.
  * Automated referee and editor profile generators.
  * Multi-tenant profile isolation harnesses.

---

## 20. C5 Readiness & C4 Absorption Determination

### C4 Absorption Status:
```
C4_PROFILE_EXTRACTION_ABSORBED_BY_C3
```
* **Rationale:** As authorized by the human decision lock and the Wave C3 prompt, all three committee member scholar profiles (`Michael Ash`, `Deepankar Basu`, `Kevin Young`) and the declarative UMass PE committee composition (`profiles/committees/umass-pe.md`) were fully extracted, verified, and locked in this single coherent pass. No additional committee members exist or are needed. A standalone Wave C4 pass would be entirely redundant.

### Readiness for C5:
* Shared Prose Protocol extracted (Wave C1/C1.1).
* Lightweight Editorial Governance & Material Passport contract extracted (Wave C2).
* Scholar & Advisor Profile System extracted (Wave C3, absorbing C4).
* The target capability architecture is fully implemented. Following the independent adversarial audit of Wave C3, ARS is ready to proceed directly to **Wave C5: Legacy Deprecation, Redirection Stubs, and Governance Reconciliation**.
