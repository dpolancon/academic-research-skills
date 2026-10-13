---
profile_id: advisor-<slug>
profile_type: advisor_role
scholar_ref: ../scholars/<slug>.md
role_status: active # active | archived
valid_until_event: dissertation_completion
calibration_only: true
review_engine: academic-paper-reviewer
---

# Advisor Role Wrapper Template: <Scholar Name>

> **Epistemic Notice & Disclaimer:**
> This wrapper establishes a contextual advisory relationship. It provides calibration parameters only.
> Review mechanics, diagnostic audits, and report generation are executed exclusively by the canonical review engine `academic-paper-reviewer`.

---

## 1. Role Context & Purpose
<!--
Describe the advisory relationship, institutional context, and supervisory scope.
-->
* **Supervisor:** <Scholar Full Name>
* **Institutional Affiliation:** <Department / University>
* **Supervisory Relationship:** Active doctoral advisor / master's supervisor.

---

## 2. Canonical Scholar Reference
<!--
Link to the canonical scholar profile.
DO NOT duplicate the scholar's intellectual priors, publications, or methodological standards here.
-->
* **Canonical Profile Path:** `../scholars/<slug>.md`
* **Calibration Inheritance:** All durable methodological, empirical, and writing priors are inherited from the canonical profile.

---

## 3. Relationship Lifecycle & Transition Rules
<!--
Define the active period and transition triggers for this wrapper.
-->
* **Status:** `active`
* **Lifecycle Boundary:** `dissertation_completion` (or other formal milestone)
* **Post-Milestone Transition:** Transitions to `role_status: archived` upon project completion, while the canonical scholar profile remains permanently active.

---

## 4. Operational Boundaries
<!--
Enforce capability separation.
-->
* **Calibration Only:** Contains no standalone review engine or scoring automation.
* **Review Engine Delegation:** All evaluation passes dispatch to `academic-paper-reviewer`.
* **Change Authorization:** Does not authorize manuscript changes; editorial governance remains separate.
