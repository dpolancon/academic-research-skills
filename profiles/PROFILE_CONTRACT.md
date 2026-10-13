# Academic Research Skills — Profile Contract

## 1. Purpose & Scope

This document defines the architectural contract, evidentiary standards, and lifecycle rules governing scholar profiles, contextual advisor roles, and committee compositions in Academic Research Skills (ARS).

ARS profiles are designed to calibrate review engines (`academic-paper-reviewer`) with domain-specific, methodological, and evidentiary priors. They replace monolithic, legacy simulator skills with modular, reusable, evidence-grounded records.

---

## 2. Core Taxonomy & Decoupling

ARS establishes a strict three-tier taxonomy that separates durable scholarly identity from situational project relationships and multi-member bodies:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        CANONICAL SCHOLAR IDENTITIES                    │
│                      (profiles/scholars/<person>.md)                   │
│                                                                        │
│   • Durable intellectual orientation    • Methodological emphases      │
│   • Core empirical priors               • Documented feedback history  │
└───────────────────▲────────────────────────────────▲───────────────────┘
                    │                                │
                    │ references                     │ references
┌───────────────────┴───────────────┐  ┌─────────────┴──────────────────┐
│      CONTEXTUAL ADVISOR ROLE      │  │     COMMITTEE COMPOSITION      │
│   (profiles/advisors/<person>.md) │  │  (profiles/committees/<id>.md) │
│                                   │  │                                │
│   • Active project relationship   │  │   • Multi-member panel roster  │
│   • Bounded lifecycle status      │  │   • Institutional roles        │
│   • Calibration-only wrapper      │  │   • Composition status         │
└───────────────────────────────────┘  └────────────────────────────────┘
```

### 2.1 Scholar Profile (`profiles/scholars/<person>.md`)
A durable, evidence-grounded calibration record associated with an individual scholar. Scholar profiles capture permanent intellectual, empirical, and methodological priorities drawn from verified publications, curriculum guidelines, or documented supervisory feedback. They are independent of any single student, dissertation, or institutional panel.

### 2.2 Advisor Role Wrapper (`profiles/advisors/<person>.md`)
A lightweight contextual binding that links a specific scholar profile to an active advisory relationship. The wrapper defines relationship state, active lifecycle duration, and project context. It does not replicate intellectual calibration and contains no review engine.

### 2.3 Committee Composition (`profiles/committees/<committee>.md`)
A declarative record identifying the members, institutional affiliations, and committee roles for an academic evaluation body (e.g., doctoral dissertation committee). It references individual scholar profiles and specifies panel composition without embedding review mechanics or dialogue simulations.

---

## 3. Strict Architectural Guardrails

1. **Profiles Do Not Own Capabilities:** Profiles are passive calibration data. They do not own or execute agent capabilities, workflows, or tool invocations.
2. **Review Capabilities Belong to `academic-paper-reviewer`:** All peer review, diagnostic critique, Socratic questioning, and report generation belong canonically to `academic-paper-reviewer`. Profiles provide parameter calibration only.
3. **Profiles Do Not Authorize Manuscript Changes:** Profiles cannot approve, merge, or stamp document modifications. All editorial change control is governed by the Material Passport contract and editorial governance.
4. **No Personality or Persona Simulation:** Profiles do not simulate human personalities, conversational demeanors, emotional tones, or subjective temperaments.
5. **No Persona Inference:** Profiles must never extrapolate political party preferences, unstated theoretical beliefs, psychological traits, or subjective grading probabilities.
6. **Mandatory Epistemic Disclaimer:**
   > **Disclaimer:** Profile-guided review approximates evidence-grounded calibration and must not be represented as the actual scholar's opinion.

---

## 4. Evidence Classification Model

Every claim or calibration prior in an ARS profile must be explicitly categorized under one of the following evidentiary tiers:

| Tier | Category | Definition | Handling in Profiles |
|:-----|:---------|:-----------|:---------------------|
| **T1** | **Factual / Directly Supported** | Explicitly verified in source literature, syllabus, or departmental guidelines. | Included with explicit source citation. |
| **T2** | **Direct Feedback** | Verbatim or closely paraphrased directives from documented supervisory feedback. | Included with source attribution. |
| **T3** | **Inferred Calibration** | Bounded methodological inferences derived from multiple consistent observations. | Included only if bounded and marked as inferred. |
| **T4** | **Project Context** | Material specific to a single chapter, model parameter, or temporary draft. | **STRICTLY EXCLUDED** from durable scholar profiles. |
| **T5** | **Unsupported Speculation** | Guesses regarding personality, ideology, private views, or grading tendencies. | **STRICTLY PROHIBITED**. |

---

## 5. Confidence Model

ARS profiles enforce a minimal, standardized confidence vocabulary:

* **`HIGH`**: Supported by direct explicit source evidence, published papers, or repeated supervisory feedback.
* **`MEDIUM`**: Supported by bounded inferences consistent with multiple documented observations across sources.
* **`LOW`**: Context-specific, single-occurrence, or weak inferences.

**Rule of Parsimony:** Prefer omission over `LOW`-confidence speculation. If source material is insufficient to establish a clear methodological prior, the profile must leave the category blank or omit it entirely.

---

## 6. Prohibited Inferences & Persona Boundaries

To protect academic integrity and prevent model hallucination, profiles must never encode:
* Personality typology (e.g., Myers-Briggs, Big Five, emotional temperament).
* Political party registration or private political preferences.
* Psychological dispositions or interpersonal combativeness.
* Speculative unstated theoretical dogmas.
* Likely grading behavior or manuscript acceptance/rejection probabilities.
* Presumed personal motives, intentions, or private preferences.

---

## 7. Schema Contracts

### 7.1 Scholar Profile Frontmatter Schema
```yaml
---
profile_id: scholar-<slug>          # Unique identifier (e.g., scholar-michael-ash)
profile_type: scholar              # Must be 'scholar'
display_name: <Full Name>          # Human-readable name
profile_status: active | archived  # Current operational status
evidence_status: curated           # Evidence curation status
supported_roles:                   # List of roles this profile can calibrate
  - advisor
  - committee_member
  - committee_chair
confidence_overall: HIGH | MEDIUM  # Aggregate confidence rating
---
```

### 7.2 Advisor Role Wrapper Frontmatter Schema
```yaml
---
profile_id: advisor-<slug>                 # Unique identifier (e.g., advisor-michael-ash)
profile_type: advisor_role                 # Must be 'advisor_role'
scholar_ref: ../scholars/<slug>.md         # Relative path to canonical scholar profile
role_status: active | archived             # Status of the advisory relationship
valid_until_event: dissertation_completion # Event triggering role review/transition
calibration_only: true                     # Enforces calibration-only constraint
review_engine: academic-paper-reviewer     # Canonical review engine
---
```

### 7.3 Committee Composition Frontmatter Schema
```yaml
---
committee_id: committee-<slug>             # Unique identifier (e.g., committee-umass-pe)
profile_type: committee_composition        # Must be 'committee_composition'
display_name: <Panel Name>                 # Human-readable panel name
institution: <University/Institution>      # Institutional affiliation
department: <Department>                  # Primary department
field: <Academic Field>                    # Academic subdiscipline
composition_status: active | archived      # Status of committee composition
members:                                   # Roster of committee members
  - scholar_ref: ../scholars/<slug>.md
    role: chair_and_advisor | internal_member | external_member
    status: active | archived
review_engine: academic-paper-reviewer     # Canonical review engine
---
```

---

## 8. Lifecycle & Transition Rules

1. **Active Doctoral Supervision:** During active dissertation work, the advisor role remains `role_status: active`. The scholar profile remains `profile_status: active`.
2. **Dissertation Completion Transition:** Upon dissertation completion (`valid_until_event: dissertation_completion`), the advisor wrapper and committee composition transition to `archived` or `alumni` status.
3. **Scholar Profile Permanence:** Scholar profiles are permanent institutional assets. They persist unchanged across student cohort completions and remain available for future research calibration.
