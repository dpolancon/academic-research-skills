---
name: advisor-reviewer
description: "DEPRECATED: Compatibility redirect for Michael Ash advisor calibration. Canonical review engine is academic-paper-reviewer consuming profiles/advisors/michael-ash.md."
metadata:
  version: "3.0.0-deprecated"
  status: deprecated
  lifecycle: DEPRECATED_COMPATIBILITY_REDIRECT
  canonical_review_engine: academic-paper-reviewer
  calibration_profile: profiles/advisors/michael-ash.md
  scholar_identity: profiles/scholars/michael-ash.md
---

# Advisor Reviewer (Deprecated Compatibility Redirect)

> **STATUS: DEPRECATED**<br>
> This skill surface is deprecated as of ARS Wave C5. It no longer operates as an independent peer-review engine.
> Substantive manuscript review and evaluation are canonically owned by `academic-paper-reviewer`.
> Supervisory calibration is maintained in the modular profile system.

---

## Canonical Replacements

* **Canonical Review Engine:** [`academic-paper-reviewer`](file:///c:/ReposGitHub/academic-research-skills/academic-paper-reviewer)
* **Advisor Calibration Wrapper:** [`profiles/advisors/michael-ash.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/advisors/michael-ash.md)
* **Canonical Scholar Identity:** [`profiles/scholars/michael-ash.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/scholars/michael-ash.md)

---

## Compatibility Routing Behavior

When an agent or user invokes `advisor-reviewer`, execute the following compatibility workflow:

1. **Do NOT Execute an Independent Review Engine:** `advisor-reviewer` contains no standalone review state machine, scoring rubrics, or decision letters.
2. **Delegate to Canonical Reviewer:** Dispatch all manuscript evaluation, section critiques, and revision roadmaps to `academic-paper-reviewer`.
3. **Inject Advisor Calibration:** Supply [`profiles/advisors/michael-ash.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/advisors/michael-ash.md) as contextual calibration input to `academic-paper-reviewer`.
4. **Enforce Epistemic Boundary:**
   > **Disclaimer:** Profile-guided review approximates evidence-grounded supervisory calibration and must not be represented as the actual scholar's opinion.
