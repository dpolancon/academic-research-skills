# ARS WAVE E EXECUTION PLAN: DISSEMINATION ARCHITECTURE & PUBLIC SCHOLARSHIP

**Status:** IMPLEMENTATION AUTHORIZED BY DIEGO POLANCO (2026-10-19)  
**Date:** 2026-10-19  
**Human Architect:** Diego Polanco  
**Repository:** `academic-research-skills` (`dpolancon/academic-research-skills`)  
**Working Branch:** `main`  
**Governing Checkpoint Baseline:** `27fbfd60255fe6c3cd99e7298c43a5189869163b` (Wave D human-closed & ratified)  

> [!NOTE]
> **Implementation Authorization Note (2026-10-19):**  
> On 2026-10-19, human architect Diego Polanco reviewed this revised execution plan and the plan review response record, and formally authorized Wave E implementation under the following ratified decisions:
> - **E-1 (Sequence):** Implement Wave E logical decomposition before Wave F physical migration, explicitly superseding the earlier timing deferral recorded in D0/D1. Wave F requires separate authorization.
> - **E-2 (Personalization):** Keep `profiles/author/diego-public.md` deferred in the Personalization Backlog.
> - **E-3 (Compatibility):** Convert `editor-jacobin-lat/SKILL.md` into a deprecated compatibility entry point delegating to `public-scholarship` with the Jacobin venue profile.
> - **E-4 (Protection):** Preserve existing project files, slide tests, and editorial-governance material. Work on `econ-slides` is verification-only.
> - **E-5 (Standards):** Adopt the revised provenance classifications and bounded auditor model, keeping assignment-specific requirements distinct from venue preferences.
>
> Earlier statements in this document marked as "awaiting authorization" are preserved as historical design context.

---

## 1. Plain-Language Value Proposition & Research Responsibilities

### 1.1 The Division of Intellectual Responsibility in Research
In academic political economy and heterodox economics, research communicates across three distinct tiers of responsibility:

1. **Substantive Analytical Investigation (Domain Skills):**
   - *Owners:* [`political-economy-research`](../../../political-economy-research/SKILL.md), [`umass-applied-econometrics`](../../../umass-applied-econometrics/SKILL.md), [`heterodox-economics-review`](../../../heterodox-economics-review/SKILL.md).
   - *Responsibility:* Establishing empirical facts, deriving mathematical stability conditions, estimating time-series specifications, tracing historical processes, and respecting statistical non-findings. Narrative cannot overturn evidence; theoretical priors cannot dictate econometric results.
2. **Scholarly Manuscript Production (Core Authoring):**
   - *Owners:* [`academic-paper`](../../../academic-paper/SKILL.md), [`econ-write`](../../../econ-write/SKILL.md).
   - *Responsibility:* Formal scholarly communication addressed to peer reviewers, advisors, and discipline specialists. Governed by academic paper structures, Bottom Line Up Front (BLUF), triangular paragraphs, explicit identification strategies, and formal caveats.
3. **Public Dissemination & Policy Intervention (Dissemination Skills):**
   - *Owners:* [`public-scholarship`](../../../public-scholarship/SKILL.md) (canonical skill), [`econ-slides`](../../../econ-slides/SKILL.md).
   - *Responsibility:* Communicating research findings to non-specialist audiences, including students, trade unionists, policy analysts, journalists, and civic organizations.

### 1.2 The Core Problem: Incomprehensibility vs. Vulgarization
When academic research enters the public sphere, it routinely falls into one of two destructive failure modes:
- **The Hermetic Failure:** The writing remains trapped in academic endogamy—dense econometric terminology, mathematical notation, and internal literature disputes that render the findings unintelligible to anyone without a PhD.
- **The Vulgarization Failure:** In attempting to be accessible, the writing abandons analytical rigor, substituting moralizing adjectives (*"rapaz"*, *"siniestro"*), partisan catchphrases (*"la derecha"*, *"el modelo neoliberal"*), or sweeping geographical generalities (*"desde Buenos Aires a Brasilia"*) for concrete material mechanisms. Crucially, empirical uncertainty is often discarded, converting tentative findings into dogmatic certainties.

### 1.3 The Governing Standard: Des-specialization Without Banalization
Wave E establishes a disciplined **Dissemination Architecture** governed by the standard of **des-specialization without banalization**:
- Explaining complex institutional and structural mechanisms in clear, lucid language that connects with everyday material life.
- Strictly preserving the causal ceilings, evidentiary limits, and empirical qualifications established by underlying domain research.
- **Fidelity in Simplification:** Simplification must preserve the specific mechanism and qualifications of the source argument. It must never substitute inaccurate universal shorthands, ideological slogans, or ungrounded claims of certainty.

### 1.4 Reusability Across Diverse Public Genres
Public scholarship is not a single rigid template. Wave E designs `public-scholarship` to serve multiple public-facing genres:
- **Contemporary Op-Eds (800–1,200 words):** Rapid, timely interventions addressing a breaking news event or policy debate, leading with a sharp thesis and supported by 1–2 key mechanisms.
- **Explanatory Public Essays (1,500–2,500 words):** In-depth, accessible investigations of structural economic problems (e.g., inflation, industrial policy, exchange-rate crises) that educate readers on underlying institutional forces.
- **Historical Perspectives (1,500–3,000 words):** Public essays that revisit historical episodes to extract structural lessons for current debates, without reading like academic historiography papers.
- **Policy Briefs & Memoranda (1,200–2,000 words):** Actionable, evidence-grounded syntheses designed for legislative aides, labor federations, or civic campaigns, highlighting concrete trade-offs and implementation considerations.

---

## 2. Sequencing Reconciliation: Wave E Logical Decomposition vs. Wave F Physical Migration

### 2.1 The Conflicting Recorded Instructions
The repository contains two conflicting recorded instructions regarding the sequencing of public-scholarship decomposition:

1. **The Target Migration Roadmap ([`docs/design/2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md`](../2026-10-11-ars-target-architecture/05_TARGET_MIGRATION_ROADMAP.md)):**
   - Authored 2026-10-11 as the foundational sequence blueprint:
     $$\text{Wave D (P2)} \longrightarrow \text{Wave E (P2)} \longrightarrow \text{Wave F (P3)}$$
   - Formulates **Strategic Principle 2**: *"Decouple logical ownership from physical file moves: Client runners depend on current paths. Reclassify logically first through registries and routing rules. Physical moves occur only in the final wave with automated discovery tests."*
   - Explicitly specifies that Wave F depends on Waves A through E being completed and tested.
2. **The Wave D Deferral Records ([`docs/design/wave-d/D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md`](../wave-d/D0_DOMAIN_CAPABILITY_RECONNAISSANCE.md) §0 item 6 & [`docs/design/wave-d/D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md`](../wave-d/D1_POLITICAL_ECONOMY_CAPABILITY_CONTRACT.md) §0 item G3):**
   - Authored 2026-10-14 during Wave D initialization.
   - States: *"Public scholarship decomposition deferred beyond Wave D/F: In accordance with the post-Wave-C restart handoff, execution of this decomposition is `DEFERRED — FUTURE AUTHORIZATION REQUIRED` (beyond Wave D/F). A governing-document timing inconsistency is recorded between the target blueprint and the restart handoff."*
   - D0 explicitly noted this inconsistency between the target blueprint and the post-Wave-C instructions and recorded it as an alignment item requiring human resolution.

### 2.2 Comparative Assessment of Sequences

| Approach | Sequence | Practical Advantages | Risks & Disadvantages |
|:---|:---|:---|:---|
| **Approach 1: Wave E Logical First (Recommended)** | Wave E (logical decomposition at root runtime paths) $\longrightarrow$ Human review/closure $\longrightarrow$ Wave F (physical migration) | • Stabilizes capability boundaries and venue profiles before moving folders.<br>• Follows the proven pattern from Wave C (where `advisor-reviewer` and `PE-phd-committee` were decomposed into profiles and compatibility stubs while remaining at root).<br>• Enables Wave F to execute a single, comprehensive directory reorganization on an already-stable ontology. | • Requires maintaining compatibility stubs at the repository root during Wave E. |
| **Approach 2: Wave F Physical First** | Wave F (physical directory migration) $\longrightarrow$ Wave E (subsequent decomposition) | • Cleans the physical directory tree into `skills/core/`, `skills/domain/`, `skills/dissemination/` earlier. | • Moves `editor-jacobin-lat/` into `skills/dissemination/` before its decomposition into `public-scholarship` and `profiles/venues/` is designed.<br>• Requires updating client runner configurations and discovery tests twice.<br>• Blurs the boundary between physical movement and substantive capability decomposition. |

### 2.3 Proposed Decision E-1: Sequence Ratification
It is proposed that the human architect formally adopt **Approach 1**, explicitly superseding the timing deferral recorded in `D0` §0 item 6 and `D1` §0 item G3:
- Wave E will execute the logical decomposition of dissemination capabilities while retaining all runtime paths at the repository root per **Routing Contract Rule 8 (Runtime Path Rule)**.
- Wave F (physical directory harmonization) remains **strictly separately authorized work**. The completion of Wave E will not automatically launch Wave F.

---

## 3. Candidate Provenance & Rule Classification

To ensure that venue-specific editorial preferences or single-assignment instructions are not mistaken for universal standards of public writing, every rule candidate in the existing `editor-jacobin-lat` surface is classified below:

### 3.1 Candidate Provenance Table

| Candidate Rule | Exact Source / Location | Classification | Applicability | Evidence Status | Proposed Treatment |
|:---|:---|:---|:---|:---|:---|
| **Declarative headline (max 12 words, no colon, no subtitle)** | `editor-jacobin-lat/SKILL.md` l. 22–23;<br>`references/criterios_martin_arboleda.md` l. 39–43;<br>`checklists/rubrica_evaluacion_100.md` l. 14, 23;<br>`scripts/audit_columna.py` l. 86–112 | **Supported venue preference** | *Jacobin América Latina* | Supported by direct written editor guidance (Martín Arboleda feedback). | Extract to `profiles/venues/jacobin-lat.md` as venue formatting rule. In `public-scholarship`, recommend clear assertive headlines, but permit subtitles, colons, or question formats where appropriate for other venues. |
| **Word-count target (1,500–2,500 words; sweet spot 1,800–2,000)** | `SKILL.md` l. 28–29;<br>`criterios_martin_arboleda.md` l. 48;<br>`rubrica_evaluacion_100.md` l. 15, 26;<br>`audit_columna.py` l. 122–136 | **Supported venue preference** | *Jacobin América Latina* long-form essays | Supported by direct venue guidelines for standard essay slots. | Retain in `profiles/venues/jacobin-lat.md`. In `public-scholarship`, define flexible word-budget targets calibrated by genre (op-ed, policy brief, long essay). |
| **Mandatory dialogue with Isabella Weber & sellers' inflation** | `SKILL.md` l. 24–27;<br>`criterios_martin_arboleda.md` l. 22–32;<br>`rubrica_evaluacion_100.md` l. 16;<br>`audit_columna.py` l. 45–51, 196–210 | **Commission-specific instruction** | Inflation & Unidad Popular essay commission | Documented feedback for a specific essay commission on inflation and class power in Chile. Not a universal venue rule for unrelated topics. | Classify as commission-specific exemplar. In `profiles/venues/jacobin-lat.md`, cite as a thematic model for cost-shock and inflation topics, but do not mandate across all public essays. |
| **Framing on "Bourgeois Economics vs. Critique of Political Economy"** | `SKILL.md` l. 35–39;<br>`references/glosario_desespecializacion.md` l. 7–14;<br>`audit_columna.py` l. 166–180 | **Supported venue preference** | *Jacobin América Latina* & socialist PE | Supported by venue editorial manual and socialist intellectual tradition. | Include in `profiles/venues/jacobin-lat.md` as core editorial stance. In `public-scholarship`, offer class-relational and structural framing as an available approach, without making it an exclusionary gate for other research genres. |
| **Regional Latin American focus & dynamics** | `SKILL.md` l. 20–21;<br>`criterios_martin_arboleda.md` l. 33–38;<br>`rubrica_evaluacion_100.md` l. 13;<br>`audit_columna.py` l. 16–22 | **Supported venue preference** | *Jacobin América Latina* | Supported by publication mandate (Latin American edition). | Include in `profiles/venues/jacobin-lat.md` as regional scope guidance. Omit from generic `public-scholarship` (which must support global research). |
| **Mandatory comparative integration of $\ge 2$ other LatAm countries** | `rubrica_evaluacion_100.md` l. 13, 27;<br>`audit_columna.py` l. 212–234 | **Commission-specific instruction / Unresolved** | Chile UP essay draft review | Source text records a review note urging regional breadth on a single-country draft; unsupported as a standing policy across all *Jacobin* columns. | Demote from mandatory mechanical gate to an advisory review question when comparative regional scope is explicitly requested. |
| **Contemporary opening anchor (first 2–3 paragraphs)** | `SKILL.md` l. 18–19;<br>`criterios_martin_arboleda.md` l. 22–24;<br>`rubrica_evaluacion_100.md` l. 11;<br>`audit_columna.py` l. 45–51, 182–194 | **Generic public-writing standard** (contextual) / **Venue preference** | Op-eds & public essays | Widely supported in public journalism (connecting history to living dilemmas). | Adopt in `public-scholarship` as a recommended technique for op-eds, but permit historical explainers and policy briefs to open with institutional puzzles or policy questions. Retain in `profiles/venues/jacobin-lat.md` as priority guideline. |
| **Forensic mechanisms over moralizing adverbs / slogans** | `SKILL.md` l. 41–44;<br>`criterios_martin_arboleda.md` l. 12, 19;<br>`references/manual_estilo_jacobin.md` l. 14–20;<br>`references/glosario_desespecializacion.md` l. 33–37 | **Generic public-writing standard** | All serious research-grounded public writing | Universal craft standard for academic translation: data and mechanisms persuade; moral outrage without evidence does not. | Core requirement in `public-scholarship`. Reusable across all public writing. |
| **Anti-agitprop Spanish blacklist (*"burguesía rapaz"*, *"lacayos"*...)** | `manual_estilo_jacobin.md` l. 16–18;<br>`audit_columna.py` l. 38–43, 150–164 | **Supported venue preference** | *Jacobin América Latina* | Explicitly codified blacklist in Jacobin AL style guide to protect intellectual seriousness. | Retain in `profiles/venues/jacobin-lat.md`. The auditor checks this blacklist only when the Jacobin profile is active. |

### 3.2 The Venue Profile Boundary Principle
> [!IMPORTANT]
> **Venue Calibration Boundary:**  
> A venue profile (`profiles/venues/jacobin-lat.md`) calibrates editorial framing, rhetorical emphasis, headline format, and stylistic register. **It acquires zero authority over underlying evidence, econometric methods, causal inferences, or substantive research conclusions.** If an empirical paper finds no evidence of cointegration or no statistically significant effect, a venue profile cannot command the writer to assert that the mechanism was historically decisive.

---

## 4. Proposed Component Architecture & Responsibility Allocation

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              CURRENT STATE (POST-WAVE D)                               │
├─────────────────────────────────────┬──────────────────────────────────────────────────┤
│ COMPONENT                           │ CURRENT ROLE & LIMITATIONS                       │
├─────────────────────────────────────┼──────────────────────────────────────────────────┤
│ editor-jacobin-lat/                 │ Bundles generic public translation with Jacobin  │
│                                     │ América Latina house style and UP commission.    │
├─────────────────────────────────────┼──────────────────────────────────────────────────┤
│ econ-slides/                        │ Owns Beamer presentations; contains unquarantined│
│                                     │ local grant project files (slide_deck_Fondecyt/).│
├─────────────────────────────────────┼──────────────────────────────────────────────────┤
│ editor-jacobin-lat/scripts/audit_columna.py │ Monolithic script checking both generic and│
│                                     │ Jacobin-specific rules with mixed authority.     │
└─────────────────────────────────────┴──────────────────────────────────────────────────┘
                                          │
                                          ▼ PROPOSED WAVE E DECOMPOSITION
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              TARGET STATE (POST-WAVE E)                                │
├─────────────────────────────────────┬──────────────────────────────────────────────────┤
│ COMPONENT                           │ TARGET RESPONSIBILITY                            │
├─────────────────────────────────────┼──────────────────────────────────────────────────┤
│ public-scholarship/                 │ CANONICAL OWNER: public_scholarship_translation  │
│ (proposed runtime path at root)     │ Multi-genre public scholarship translation,      │
│                                     │ des-specialization, everyday material stakes,    │
│                                     │ empirical claim discipline across outlets.       │
├─────────────────────────────────────┼──────────────────────────────────────────────────┤
│ profiles/venues/jacobin-lat.md      │ CANONICAL PROFILE: venue_jacobin_lat_editorial   │
│                                     │ Venue editorial profile (Arboleda criteria,      │
│                                     │ headline constraints, regional scope, blacklist).│
├─────────────────────────────────────┼──────────────────────────────────────────────────┤
│ editor-jacobin-lat/SKILL.md         │ DEPRECATED COMPATIBILITY STUB                    │
│                                     │ Redirects callers to public-scholarship with     │
│                                     │ profiles/venues/jacobin-lat.md calibration.      │
├─────────────────────────────────────┼──────────────────────────────────────────────────┤
│ econ-slides/                        │ CANONICAL OWNER: scholarly_slide_production      │
│ (verification-only in Wave E)       │ Generic academic Beamer deck generation;         │
│                                     │ slide_deck_Fondecyt/ quarantined & untouched.    │
├─────────────────────────────────────┼──────────────────────────────────────────────────┤
│ editor-jacobin-lat/scripts/audit_columna.py │ DETERMINISTIC DISSEMINATION TOOL                 │
│ (retained in current directory)     │ Parameterized auditor with 3 bounded output tiers│
│                                     │ (mechanical, heuristic, substantive review).     │
└─────────────────────────────────────┴──────────────────────────────────────────────────┘
```

### 4.1 Specification of Canonical `public-scholarship`
- **Component ID:** `public-scholarship`
- **Runtime Path:** `public-scholarship/` (retained at repository root during Wave E)
- **Role:** `DISSEMINATION_SKILL`
- **Owned Capability:** `public_scholarship_translation`
- **Core Design:**
  - **Des-specialization without Banalization:** Teaches the model how to explain complex institutional, historical, and econometric findings without condescension and without academic jargon.
  - **Fidelity to Underlying Mechanics:** Simplification must faithfully preserve the specific causal mechanism and empirical qualifications of the source argument. For example, explaining balance-of-payments constraints as a chronic shortage of foreign exchange needed for vital imports, or explaining endogenous money through the specific mechanisms of bank credit creation and central bank settlement, must reflect the source paper's analytical framework rather than applying rigid, inaccurate universal synonyms.
  - **Empirical Ceilings:** Strictly prohibits strengthening causal claims, transforming correlation into causation, or suppressing empirical non-findings to create a more compelling narrative.

### 4.2 Specification of Venue Profile: `profiles/venues/jacobin-lat.md`
- **Component ID:** `venue-jacobin-lat`
- **File Location:** `profiles/venues/jacobin-lat.md`
- **Contract:** Conforms to [`profiles/PROFILE_CONTRACT.md`](../../../profiles/PROFILE_CONTRACT.md).
- **Contents:**
  - *Editorial Director Reference:* Martín Arboleda.
  - *Core Framing:* Bourgeois economics vs. critique of political economy.
  - *Headline Constraints:* Max 12 words, declarative sentence stating central thesis, strictly no colons or subtitles.
  - *Style Blacklist:* Anti-agitprop blacklist of moralizing clichés.
  - *Word-Budget Range:* 1,500–2,500 words for long-form essays.
  - *Thematic Exemplars:* Isabella Weber sellers' inflation cited as a model for cost-shock pieces.

### 4.3 Specification of Legacy Redirect: `editor-jacobin-lat/SKILL.md`
- **Lifecycle Status:** `DEPRECATED`
- **Implementation Type:** `LEGACY_SKILL`
- **Behavior:** Standard compatibility stub declaring deprecation and directing callers and agents to `public-scholarship` with `profiles/venues/jacobin-lat.md` calibration (matching the exact pattern of `advisor-reviewer` and `PE-phd-committee` in Wave C5).

### 4.4 Slide Presentation Boundary: `econ-slides` (Verification-Only)
- **Inspection Finding:** Detailed inspection of `econ-slides/SKILL.md`, `econ-slides/references/`, and `econ-slides/themes/` confirms that the skill is already project-agnostic and references generic benchmarks (`references/working-session-grant-talks.md` cites Fondecyt alongside NSF and ERC as general examples).
- **Edit Scope in Wave E:** **Zero source edits required.** The slide presentation component requires verification-only in Wave E:
  - Verifying that existing automated tests (`econ-slides/tests/run-tests.sh` or Python verification tools) pass cleanly against self-contained sample talk fixtures.
  - **Strict Preservation:** `econ-slides/slide_deck_Fondecyt/` and `econ-slides/tests/` remain completely untouched and preserved in the local working directory. Protection during Wave E does not imply permanent retention at this path; relocation to an external project repository is deferred to Wave F or human direction.

### 4.5 Bounded Column Auditor Authority: `audit_columna.py`
- **Canonical Location for Wave E:** Retained at its existing physical location: `editor-jacobin-lat/scripts/audit_columna.py`.
  - *Rationale:* Avoids premature directory moves or symlinks before Wave F. Existing invocation commands continue to function.
- **Three Bounded Output Tiers:**
  1. **Mechanical Failures (Hard Gates):** Demonstrable, deterministic violations of explicit formal criteria:
     - Title word count exceeding 12 words (when venue profile requires $\le 12$).
     - Presence of colon (`:`) or subtitle markup (when venue profile bans subtitles).
     - Text length outside target word budget (e.g. $< 1,400$ or $> 2,600$ words for Jacobin).
  2. **Heuristic Warnings (Review Prompts):** Pattern matches that suggest potential writing issues but require human or editorial judgment:
     - Exact matches against the anti-agitprop blacklist (distinguishing original author prose from direct quotations or critical discussion of the phrase).
     - Academic meta-phrases (*"este artículo analiza"*, *"la literatura económica ha debatido"*).
     - High density of passive voice or nominalizations.
  3. **Substantive Review Questions (Informational Prompts):** Items that static scripts cannot verify:
     - Is the empirical mechanism faithful to the underlying study?
     - Is the opening hook genuinely connected to the central thesis?
     - Are historical claims warranted by the cited evidence?
- **Prohibition on Keyword Proxies:** The auditor must NOT describe keyword matches as verifying causal warrant, evidentiary adequacy, theoretical fidelity, or the substantive presence of a contemporary anchor.

---

## 5. Implementation File Surface & Governance Accounting

### 5.1 Comprehensive File Surface Inventory

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              WAVE E FILE SURFACE CLASSIFICATION                        │
├───────────────────────────────────┬────────────────────────────────────────────────────┤
│ CATEGORY                          │ FILES / PATHS                                      │
├───────────────────────────────────┼────────────────────────────────────────────────────┤
│ Proposed New Files                │ • public-scholarship/SKILL.md                      │
│                                   │ • public-scholarship/references/craft.md           │
│                                   │ • profiles/venues/jacobin-lat.md                   │
│                                   │ • evals/gold/wave_e_dissemination/cases.yaml       │
│                                   │ • scripts/test_wave_e_dissemination.py             │
│                                   │ • tests/test_audit_columna.py                      │
├───────────────────────────────────┼────────────────────────────────────────────────────┤
│ Existing Files to Modify          │ • editor-jacobin-lat/SKILL.md (retyped to stub)    │
│                                   │ • editor-jacobin-lat/scripts/audit_columna.py      │
│                                   │ • docs/governance/ars_registry.yaml                │
│                                   │ • docs/governance/ROUTING_AND_PRECEDENCE.md        │
│                                   │ • evals/gold/routing/cases.yaml (add ROUTE-027–30) │
├───────────────────────────────────┼────────────────────────────────────────────────────┤
│ Read-Only Dependencies            │ • profiles/PROFILE_CONTRACT.md                     │
│                                   │ • shared/protocols/prose_discipline_protocol.md    │
│                                   │ • scripts/validate_ars_registry.py                 │
│                                   │ • scripts/test_routing_contract.py                 │
├───────────────────────────────────┼────────────────────────────────────────────────────┤
│ Protected Preserved Surfaces      │ • econ-slides/slide_deck_Fondecyt/ (UNTOUCHED)     │
│ (No edits, moves, or deletes)     │ • econ-slides/tests/ (UNTOUCHED)                   │
│                                   │ • docs/design/2026-10-10-editorial-governance/     │
│                                   │ • All Wave D domain skills & protocols             │
├───────────────────────────────────┼────────────────────────────────────────────────────┤
│ Deferred Work                     │ • profiles/author/diego-public.md (Backlog)        │
│ (Explicitly excluded)             │ • Physical folder moves to skills/ (Wave F)        │
│                                   │ • Causal inference microeconometrics capability    │
└───────────────────────────────────┴────────────────────────────────────────────────────┘
```

### 5.2 Reconciled Governance Registry Arithmetic
The proposed Wave E modifications require exact governance accounting in `docs/governance/ars_registry.yaml`:

- **Component Accounting:**
  The baseline repository comprises 17 active (or planned active) components and 3 deprecated compatibility stubs:

| Status | Baseline | Change | Result |
|---|---:|---:|---:|
| **Active** | 17 | −1 legacy conversion (`editor-jacobin-lat`) + 2 additions (`public-scholarship`, `venue-jacobin-lat`) | **18** |
| **Deprecated** | 3 | +1 legacy conversion (`editor-jacobin-lat`) | **4** |
| **Total Components** | **20** | +2 additions | **22** |

- **Capability Accounting:**
  Capabilities are verified strictly from operational ownership records, completely decoupled from component arithmetic:
  - *Current Capability Count:* 22 capabilities.
  - *Ownership Reassignments in Wave E:*
    1. Capability `public_scholarship_translation` (Capability ID 9): `current_owner` reallocated from `"editor-jacobin-lat"` to `"public-scholarship"`. Migration status $\to$ `CURRENT`.
    2. Capability `venue_jacobin_lat_editorial` (Capability ID 18): `current_owner` reallocated from `"editor-jacobin-lat"` to `"venue-jacobin-lat"`. Migration status $\to$ `CURRENT`.
    3. `editor-jacobin-lat` retains zero substantive capabilities (Invariant D6-4 / Principle 5).
    4. Capability `causal_inference_microeconometrics` remains preserved as an unassigned gap (`current_owner: null`, `migration_status: CANDIDATE`).
  - *Resulting Expected Capability Count:* Exactly $\mathbf{22}$ **capabilities** (no capabilities added or deleted).

### 5.3 Proposed Governance Identifiers & Version Increments
- **Registry Schema Version:** Propose increment from `1.2.0` to `1.3.0`.
- **Routing Precedence Contract Version:** Propose increment from `1.2.0` to `1.3.0`.
- **Proposed Precedence Rules:**
  - `Rule R17`: Generic Public Scholarship (`public-scholarship`).
  - `Rule R18`: Venue-Calibrated Public Scholarship / Jacobin AL (`public-scholarship` + `profiles/venues/jacobin-lat.md`).
- **Proposed Adversarial Disambiguation Rules:**
  - `ADV-E1`: Public Scholarship vs. Economics Disciplinary Writing (`public-scholarship` vs. `econ-write`).
  - `ADV-E2`: Venue Profile vs. Autonomous Review Engine (`venue-jacobin-lat` vs. `academic-paper-reviewer`).
  - `ADV-E3`: Legacy Jacobin Call (`editor-jacobin-lat` redirect to `public-scholarship` + profile).
  - `ADV-E4`: Simplification vs. Causal Overclaiming (`public-scholarship` bounded by domain evidence ceilings).
- **Proposed Routing Fixtures:** `ROUTE-027`, `ROUTE-028`, `ROUTE-029`, `ROUTE-030` added to `evals/gold/routing/cases.yaml` (bringing total from 26 to 30 cases).

---

## 6. Deterministic Verification & Evaluation Limits

### 6.1 Stratified Verification Model
To maintain epistemic honesty, Wave E strictly distinguishes four tiers of verification:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   TIER 1: DETERMINISTIC GOVERNANCE CHECKS              │
│  • validate_ars_registry.py: verifies 22 components, 22 capabilities.  │
│  • test_routing_contract.py: verifies 30/30 routing cases.             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                   TIER 2: CONTROLLED AUDITOR SUITE                     │
│  • test_audit_columna.py: unit tests on controlled Markdown fixtures.  │
│  • Validates mechanical gates, heuristic warnings, and review prompts. │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                   TIER 3: STATIC BEHAVIORAL EVAL FIXTURES              │
│  • test_wave_e_dissemination.py: validates eval YAML schema & anchors. │
│  • Checks positive rubrics and negative regression catches.            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                   TIER 4: LIVE MODEL-GENERATIVE EVALUATION             │
│  • [EXPLICITLY UNTESTED IN OFFLINE PASSES]                             │
│  • Requires live LLM generation harness; offline checks do not prove   │
│    live model adherence.                                               │
└────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Proposed Negative Behavioral Evaluation Fixtures
The proposed evaluation suite (`evals/gold/wave_e_dissemination/cases.yaml`) will include explicit adversarial negative cases:

1. **Venue-Rule Leakage Negative Case:**
   - *Test:* A prompt requesting a generic public op-ed for an independent newspaper.
   - *Failure Catch:* Evaluator fails if the model imposes *Jacobin AL* constraints (e.g. banning subtitles, forcing Isabella Weber citations, or demanding Latin American country comparisons).
2. **Commission-Specific Topic Leakage Negative Case:**
   - *Test:* A prompt requesting a public essay on a non-inflation topic (e.g., labor union organizing or environmental regulation).
   - *Failure Catch:* Evaluator fails if the model forces *sellers' inflation* or Isabella Weber into the text where substantive evidence does not warrant it.
3. **Unsupported Causal Strengthening Negative Case:**
   - *Test:* A prompt translating an econometric study with statistically non-significant cointegration or tentative correlation into a public essay.
   - *Failure Catch:* Evaluator fails if the model converts the tentative finding into definitive causation or claims the mechanism was empirically proven.
4. **Legacy Compatibility Redirection Negative Case:**
   - *Test:* A legacy invocation of `/editor-jacobin-lat`.
   - *Pass Criteria:* Model cleanly redirects to `public-scholarship` while applying `profiles/venues/jacobin-lat.md` calibration.

---

## 7. Revised Human Decision Package

Before any implementation, file creation, or code modification is authorized, the human architect (Diego Polanco) is invited to review and resolve the following five proposed decisions:

### Decision E-1: Sequencing Ratification (Wave E Logical First)
- **Proposed Action:** Formally ratify **Approach 1**, authorizing Wave E's logical decomposition to proceed at repository root runtime paths before Wave F physical migration, explicitly superseding earlier timing deferrals recorded in `D0` and `D1`.
- **Status:** `PROPOSED — PENDING ARCHITECT RATIFICATION`

### Decision E-2: Author-Style Calibration Disposition
- **Proposed Action:** Retain `profiles/author/diego-public.md` in the non-blocking Personalization Backlog ([`10_FUTURE_PERSONALIZATION_BACKLOG.md`](../2026-10-11-ars-target-architecture/10_FUTURE_PERSONALIZATION_BACKLOG.md)). Do not implement private author-voice calibration during Wave E.
- **Status:** `PROPOSED — PENDING ARCHITECT RATIFICATION`

### Decision E-3: Legacy Redirection Strategy for `editor-jacobin-lat`
- **Proposed Action:** Approve converting `editor-jacobin-lat/SKILL.md` into a deprecated compatibility redirection stub delegating to `public-scholarship` + `profiles/venues/jacobin-lat.md`.
- **Status:** `PROPOSED — PENDING ARCHITECT RATIFICATION`

### Decision E-4: Protection of Project Files & Existing Tests
- **Proposed Action:** Formally confirm that `econ-slides/slide_deck_Fondecyt/`, `econ-slides/tests/`, and `docs/design/2026-10-10-editorial-governance/` remain preserved and untouched throughout Wave E. Confirm that `econ-slides` work in Wave E is verification-only.
- **Status:** `PROPOSED — PENDING ARCHITECT RATIFICATION`

### Decision E-5: Candidate Classification & Bounded Auditor Authority
- **Proposed Action:** Formally adopt the Candidate Provenance Table classifications (§3.1) and the three-tiered bounded auditor authority model (§4.5), rejecting keyword proxies for substantive research validity.
- **Status:** `PROPOSED — PENDING ARCHITECT RATIFICATION`

---

## 8. Proposed Bounded Implementation Steps (When Authorized)

When the human architect ratifies the decision package, implementation should proceed in four strictly sequenced, deterministic steps:

1. **Step E-A: Venue Profile & Public Craft Formulation:**
   - Create `profiles/venues/jacobin-lat.md` and `public-scholarship/SKILL.md` + craft references.
2. **Step E-B: Column Auditor Parameterization & Unit Testing:**
   - Parameterize `editor-jacobin-lat/scripts/audit_columna.py` with 3 bounded output tiers; create `tests/test_audit_columna.py`.
3. **Step E-C: Legacy Stub Conversion & Governance Reconciliation:**
   - Convert `editor-jacobin-lat/SKILL.md` to redirect stub; update `ars_registry.yaml` (22 components, 22 capabilities) and `ROUTING_AND_PRECEDENCE.md`.
4. **Step E-D: Verification, Behavioral Evals, and Checkpoint Lock:**
   - Add `ROUTE-027`–`ROUTE-030` to routing fixtures; create `evals/gold/wave_e_dissemination/cases.yaml` and runner; verify complete test suite.

---

*WAVE E EXECUTION PLAN REVISED — HUMAN DECISION PACKAGE READY — IMPLEMENTATION NOT STARTED.*
