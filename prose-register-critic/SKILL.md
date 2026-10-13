---
name: prose-register-critic
description: "DEPRECATED: Compatibility redirect for ARS prose discipline. Reusable protocol is shared/protocols/prose_discipline_protocol.md; deterministic tool is tools/prose_checks/check_prose_patterns.py."
metadata:
  version: "3.0.0-deprecated"
  status: deprecated
  lifecycle: DEPRECATED_COMPATIBILITY_REDIRECT
  shared_protocol: shared/protocols/prose_discipline_protocol.md
  deterministic_tool: tools/prose_checks/check_prose_patterns.py
  generic_writing_owner: academic-paper
  economics_writing_owner: econ-write
---

# Prose Register Critic (Deprecated Compatibility Redirect)

> **STATUS: DEPRECATED**<br>
> This skill surface is deprecated as of ARS Wave C5. It no longer operates as an independent writing or critique skill.
> Reusable prose discipline is canonically codified in the Shared Prose Protocol and executed via deterministic offline tooling.
> Manuscript authoring and revision remain canonically owned by `academic-paper` and `econ-write`.

---

## Canonical Replacements

* **Shared Discipline Protocol:** [`shared/protocols/prose_discipline_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/prose_discipline_protocol.md)
* **Deterministic Diagnostic Tool:** [`tools/prose_checks/check_prose_patterns.py`](file:///c:/ReposGitHub/academic-research-skills/tools/prose_checks/check_prose_patterns.py)
* **Generic Manuscript Writing:** [`academic-paper`](file:///c:/ReposGitHub/academic-research-skills/academic-paper)
* **Economics Disciplinary Writing:** [`econ-write`](file:///c:/ReposGitHub/academic-research-skills/econ-write)

---

## Compatibility Routing Behavior

When an agent or user invokes `prose-register-critic`, route according to the task type:

1. **Diagnostic Pattern Scan / Prose Audit:**
   * Execute the offline deterministic checker:
     ```bash
     python tools/prose_checks/check_prose_patterns.py <file_or_dir>
     ```
2. **Generic Manuscript Revision:**
   * Invoke `academic-paper`, consuming the rules in [`shared/protocols/prose_discipline_protocol.md`](file:///c:/ReposGitHub/academic-research-skills/shared/protocols/prose_discipline_protocol.md) for Category A/B/C classification and lexical discipline.
3. **Economics Disciplinary Revision:**
   * Invoke `econ-write` for bounded economics prose, applying the shared prose discipline alongside BLUF, triangular style, and causal claim standards.
4. **No Independent Writing Ownership:**
   * `prose-register-critic` does not author or rewrite text independently.
