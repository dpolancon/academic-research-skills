---
committee_id: committee-<slug>
profile_type: committee_composition
display_name: "<Panel / Committee Name>"
institution: "<University / Institution>"
department: "<Department>"
field: "<Subdiscipline / Field>"
composition_status: active # active | archived
members:
  - scholar_ref: ../scholars/<slug-1>.md
    role: chair_and_advisor # chair_and_advisor | internal_member | external_member
    status: active # active | archived
  - scholar_ref: ../scholars/<slug-2>.md
    role: internal_member
    status: active
  - scholar_ref: ../scholars/<slug-3>.md
    role: external_member
    status: active
review_engine: academic-paper-reviewer
---

# Committee Composition Template: <Committee Name>

> **Epistemic Notice & Disclaimer:**
> This document defines panel composition only. It does not contain simulation logic, Socratic questioning engines, or verbal dialogue transcripts.
> All multi-perspective evaluation and report generation is executed exclusively by `academic-paper-reviewer`.

---

## 1. Overview & Institutional Purpose
<!--
Specify the academic committee purpose (e.g., doctoral defense, qualifying exam, master's thesis).
-->
* **Institutional Context:** <University / Department>
* **Panel Function:** <Doctoral Dissertation Committee / Examination Board>
* **Composition Status:** `active`

---

## 2. Committee Roster & Member References
<!--
List the committee members, their institutional roles, and relative paths to canonical scholar profiles.
DO NOT duplicate scholarly calibration text in this roster.
-->

### 2.1 Committee Chair
* **Scholar Reference:** `../scholars/<slug-1>.md`
* **Role:** `chair_and_advisor`
* **Primary Evaluative Scope:** <Core methodological focus>

### 2.2 Internal Member
* **Scholar Reference:** `../scholars/<slug-2>.md`
* **Role:** `internal_member`
* **Primary Evaluative Scope:** <Disciplinary focus>

### 2.3 External Member
* **Scholar Reference:** `../scholars/<slug-3>.md`
* **Role:** `external_member`
* **Primary Evaluative Scope:** <Interdisciplinary focus>

---

## 3. Operational Boundaries & Capability Delegation
<!--
Maintain clear separation from review execution and editorial governance.
-->
* **Passive Roster Record:** This record provides panel composition metadata to review engines.
* **Review Execution Delegation:** Reviews dispatch through `academic-paper-reviewer`.
* **Editorial Governance:** Evaluation comments are advisory; document modifications remain governed by the Material Passport change-control protocol.
