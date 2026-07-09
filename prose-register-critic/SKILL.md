---
name: prose-register-critic
description: "Audits academic drafts for internal LLM-scaffolding terminology, meta-commentary, and passive register. Triggers: audit register, check jargon, check prose register, find metadata leaks, style audit."
metadata:
  version: "1.0.0"
  status: active
---

# Prose Register Critic — Academic Editing Auditor

This skill prevents internal workflow commands, agent-routing labels, and pipeline scaffolding terms from leaking into the final visible prose of a manuscript.

## Core Directives

1. **Purge Metadata Leakage:** Scrutinize the text for terms that sound like an editing ledger (e.g., "retained criteria", "empirical object", "system-admissibility gates").
2. **Enforce Direct Empirical Naming:** The author must write about the *empirical* system, not the *editing* system.
   - *Bad:* "The empirical object is the cointegration vector."
   - *Good:* "The cointegration vector is the relationship under test."
3. **Scan for Meta-Commentary:** Remove throat-clearing statements where the AI describes its own process (e.g., "This interpretive move reads...").

## Integrated Tools
- Run `python scripts/check_jargon_leakage.py <file>` to automatically scan for standard blocklist terms.
