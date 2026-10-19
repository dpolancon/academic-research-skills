# Wave D Cross-Domain Adversarial Behavioral Eval Suite

## Overview

This directory contains the canonical behavioral evaluation fixtures for the Wave-D cross-domain architecture ratified in Waves D1–D4:
- `political-economy-research` (runtime: `political-economy-research/`)
- `applied-econometrics-pe` (runtime: `umass-applied-econometrics/`)
- `heterodox-macro-modeling` (runtime: `heterodox-economics-review/`)
- `historical_source_criticism_protocol` (runtime: `shared/protocols/historical_source_criticism_protocol.md`)

## Specification & Governance

- **Specification:** Wave D5 Mission Charter
- **Design Record:** `docs/design/wave-d/D5_CROSS_DOMAIN_BEHAVIORAL_EVALS.md`
- **Test Runner:** `scripts/test_wave_d_behavioral_evals.py`

## Suite Inventory

The suite contains **31 cases** across 9 families:
- **E1: PE ↔ Econometrics** (`E1-A`, `E1-B`, `E1-C`)
- **E2: PE ↔ Macro Modeling** (`E2-A`, `E2-B`, `E2-C`)
- **E3: Macro ↔ Econometrics** (`E3-A`, `E3-B`, `E3-C`)
- **E4: Historical Source Protocol ↔ PE** (`E4-A`, `E4-B`, `E4-C`)
- **E5: Capability Support vs. Universal Requirement** (`E5-A`, `E5-B`, `E5-C`, `E5-D`)
- **E6: Routing & Precedence Disambiguation** (`E6-A` through `E6-J`, 10 cases)
- **E7: Unassigned Capability Gap** (`E7-A`, `E7-B`)
- **E8: Profile Non-Override** (`E8-A`, `E8-B`)
- **E9: Self-Ratification Trap** (`E9-A` meta-eval)

## Enforcement Status (D5 §17)

In strict compliance with the **No Fake Behavioral Enforcement** rule (§17), this suite distinguishes:
1. `FIXTURE IMPLEMENTED` — Gold prompts, boundaries, required/forbidden patterns, and good/bad exemplars are defined.
2. `SCHEMA ENFORCED` — Validated offline via `scripts/test_wave_d_behavioral_evals.py`.
3. `RUNTIME CONTRACT VERIFIED` — Domain boundary anchors confirmed against live runtime skills/protocols.
4. `RUBRIC DISCRIMINATION VERIFIED` — Good exemplars pass all required criteria; bad exemplars trip expected violations.
5. `MODEL-BEHAVIOR EXECUTION PENDING` — Live LLM agent turn evaluation is deferred to future harness execution.
