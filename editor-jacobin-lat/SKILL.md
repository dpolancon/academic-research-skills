---
name: editor-jacobin-lat
description: "DEPRECATED: Compatibility redirect for Jacobin América Latina editorial calibration. Canonical dissemination skill is public-scholarship consuming profiles/venues/jacobin-lat.md."
metadata:
  version: "2.0.0-deprecated"
  status: deprecated
  lifecycle: DEPRECATED_COMPATIBILITY_REDIRECT
  canonical_dissemination_skill: public-scholarship
  venue_profile: profiles/venues/jacobin-lat.md
---

# Editor Jacobin América Latina (Deprecated Compatibility Redirect)

> **STATUS: DEPRECATED**<br>
> This skill surface is deprecated as of ARS Wave E. It no longer operates as a standalone monolithic skill bundling generic public scholarship with venue-specific editorial mandates.
> Generic public translation across multiple public genres is canonically owned by `public-scholarship`.
> Editorial calibration for *Jacobin América Latina* (Martín Arboleda criteria, headline constraints, anti-agitprop blacklist) is maintained in the modular profile system at `profiles/venues/jacobin-lat.md`.

---

## Canonical Replacements

* **Canonical Dissemination Skill:** [`skills/dissemination/public-scholarship`](file:///c:/ReposGitHub/academic-research-skills/skills/dissemination/public-scholarship)
* **Venue Profile (Jacobin AL):** [`profiles/venues/jacobin-lat.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/venues/jacobin-lat.md)
* **Deterministic Auditor Tool:** [`tools/audit_columna/audit_columna.py`](file:///c:/ReposGitHub/academic-research-skills/tools/audit_columna/audit_columna.py) (legacy wrapper: [`editor-jacobin-lat/scripts/audit_columna.py`](file:///c:/ReposGitHub/academic-research-skills/editor-jacobin-lat/scripts/audit_columna.py))

---

## Compatibility Routing Behavior

When an agent or user invokes `editor-jacobin-lat`, execute the following compatibility workflow:

1. **Do NOT Execute an Independent Dissemination Engine:** `editor-jacobin-lat` does not own standalone public scholarship rules separate from `public-scholarship`.
2. **Delegate to Canonical Dissemination Skill:** Route all public translation, op-ed drafting, essay writing, and des-specialization tasks to `public-scholarship`.
3. **Inject Venue Profile Calibration:** Supply [`profiles/venues/jacobin-lat.md`](file:///c:/ReposGitHub/academic-research-skills/profiles/venues/jacobin-lat.md) as the calibration input to `public-scholarship`.
4. **Preserve Substantive Research Invariants:**
   > **Boundary Principle:** The venue profile calibrates presentation, headline format (declarative thesis $\le 12$ words, no subtitles), and style. It acquires zero authority over underlying research findings, econometric validity, or empirical non-findings.
