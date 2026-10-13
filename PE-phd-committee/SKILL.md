---
name: PE-phd-committee
description: "DEPRECATED: Compatibility redirect for UMass Amherst PE dissertation committee calibration. Canonical review and defense engine is academic-paper-reviewer consuming profiles/committees/umass-pe.md."
metadata:
  version: "3.0.0-deprecated"
  status: deprecated
  lifecycle: DEPRECATED_COMPATIBILITY_REDIRECT
  canonical_review_engine: academic-paper-reviewer
  committee_profile: profiles/committees/umass-pe.md
---

# PE PhD Committee (Deprecated Compatibility Redirect)

> **STATUS: DEPRECATED**<br>
> This skill surface is deprecated as of ARS Wave C5. It no longer operates as an independent dissertation defense simulator or review engine.
> Substantive doctoral manuscript evaluation and defense questioning are canonically owned by `academic-paper-reviewer`.
> Panel composition is maintained in the modular profile system.

---

## Canonical Replacements

* **Canonical Review / Defense Engine:** [`academic-paper-reviewer`](file:///c:/ReposGitHub/academic-research-skills/academic-paper-reviewer)
* **Committee Composition Profile:** [`profiles/committees/umass-pe.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/committees/umass-pe.md)
* **Member Scholar Profiles:**
  * Michael Ash (Chair/Advisor): [`profiles/scholars/michael-ash.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/scholars/michael-ash.md)
  * Deepankar Basu (Internal Member): [`profiles/scholars/deepankar-basu.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/scholars/deepankar-basu.md)
  * Kevin Young (External Member): [`profiles/scholars/kevin-young.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/scholars/kevin-young.md)

---

## Compatibility Routing Behavior

When an agent or user invokes `PE-phd-committee`, execute the following compatibility workflow:

1. **Do NOT Execute an Independent Simulation Engine:** `PE-phd-committee` contains no standalone Socratic questioning state machines or deliberation verdict routines.
2. **Delegate to Canonical Reviewer:** Dispatch all dissertation defense simulations, pre-defense reviews, and referee reports to `academic-paper-reviewer`.
3. **Inject Committee Composition:** Supply [`profiles/committees/umass-pe.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/committees/umass-pe.md) as declarative panel calibration to `academic-paper-reviewer`.
4. **Calibrate via Member Profiles:** Let the referenced member profiles inform theoretical, empirical, and historical questioning angles.
5. **Enforce Epistemic Boundary:**
   > **Disclaimer:** Profile-guided simulation approximates evidence-grounded academic calibration and must never be represented as actual committee-member opinions.
