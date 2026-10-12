# ARS Update & Learning Registry

Single source of truth for tracking local and remote updates, prompt calibrations, domain learnings, and feature enhancements across the Academic Research Skills (ARS) monorepo.

This registry is designed to prevent synchronization conflicts when switching between local workstations (`desktop-bsb5hhv-swift-void`) and remote environments (laptops, cloud runners, remote terminals).

---

## Conflict Avoidance & Remote Sync Protocol

### 1. Before Leaving This Workstation (Push Local Learnings)
When you modify or learn new rules in any skill (e.g. `econ-slides`, `econ-write`), commit and broadcast before switching to another machine:
```powershell
# From C:\ReposGitHub\academic-research-skills:
.\sync.ps1 -Push -Skill "econ-slides" -Description "Your update or learning summary"
```
This script will:
1. Append your change to this registry table.
2. Stage and commit changes with `feat(<skill>): <description> [host: <machine>]`.
3. Fetch remote `origin/main` and rebase linearly.
4. Push to GitHub (`origin/main`).

### 2. When Working Remotely (Remote Machine)
1. Pull latest `main`: `git pull --rebase origin main`
2. Make your edits and commit them cleanly.
3. Push back to `origin/main`.

### 3. When Returning to This Workstation (Ingest Remote Updates)
Before starting new local work:
```powershell
# Check status and differences:
.\sync.ps1 -Check

# Safe pull and ingest:
.\sync.ps1 -Pull
```
If there are uncommitted local modifications, `sync.ps1` safely stashes them (`git stash`), pulls remote commits with rebase (`git pull --rebase origin main`), and applies your stash (`git stash pop`), alerting you if any manual conflict resolution is needed.

---

## Live Wiring (NTFS Directory Junctions)

Skills are installed into the AI agent's "local brain" (`~/.gemini/config/skills/`) and project workspaces (`.agents/skills/`) via **NTFS Directory Junctions**.
- **Two-way transparency**: Any edit, prompt improvement, or template added by the agent or user inside the local brain immediately updates `C:\ReposGitHub\academic-research-skills` on disk.
- **Zero duplication**: No drift between installed skills and the canonical git repository.

---

## Update Log (Historical Sync Entries)

| Entry ID | Date (UTC/Local) | Host / Machine | Component / Skill | Type | Description | Git Reference / Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `REG-001` | 2026-10-01 18:50 | `desktop-bsb5hhv-swift-void` | `infra / skills` | `ARCHITECTURE` | Installed 14-skill suite in Antigravity global brain (`~/.gemini/config/skills`) & LitVault workspace via NTFS Directory Junctions. Registered `~/.gemini/config/skills.json`. | Local configured |
| `REG-002` | 2026-10-01 18:52 | `desktop-bsb5hhv-swift-void` | `econ-slides` | `LEARNING` | Added specialized working session & research grant talk reference (`references/working-session-grant-talks.md`) for unclosed theoretical models (Fondecyt PK land-rent benchmark). | Local configured |
| `REG-003` | 2026-10-01 18:55 | `desktop-bsb5hhv-swift-void` | `sync-tools` | `TOOLING` | Created `scripts/sync-skills.ps1` and root `sync.ps1` conflict-prevention sync harness; upgraded `install-local.ps1` to support live junctions. | Local configured |

---

## Governance & Learning Protocol (Wave B0+)

Starting with Wave B0, `UPDATE_REGISTRY.md` serves as the authoritative human-readable governance surface for recording:
- Upstream synchronizations and upstream-derived updates
- Local prompt calibrations, domain heuristics, and empirical learnings
- Evaluation findings and regression test evidence
- Capability migrations, reassignments, and decompositions
- Accepted vs rejected architectural lessons
- Security and provenance updates

### Prospective Schema Specification

Every prospective governance or learning record should capture:

| Field | Description | Allowed Values / Format |
| :--- | :--- | :--- |
| `date` | Date of recorded event | `YYYY-MM-DD` |
| `component` | Affected component or subsystem | Component ID in `docs/governance/ars_registry.yaml` or subsystem name |
| `change_type` | Type of governance/learning change | `UPSTREAM_SYNC`, `LOCAL_IMPROVEMENT`, `EVAL_FINDING`, `MIGRATION`, `CAPABILITY_REASSIGNMENT`, `PROFILE_LEARNING`, `REJECTED_CHANGE`, `SECURITY_OR_PROVENANCE` |
| `source` | Upstream commit, paper, advisor interaction, or eval case | Reference path or commit |
| `provenance` | Entity or author proposing/originating change | Author handle / name |
| `lesson_or_change` | Core technical lesson or modification | Concise summary |
| `evidence` | Supporting evaluation runs, tests, or documentation | Path to test, report, or diff |
| `decision` | Action taken | `ACCEPTED`, `REJECTED`, `DEFERRED`, `MIGRATED` |
| `status` | Operational status | `COMMITTED`, `STAGED`, `PLANNED` |
| `affected_capabilities` | Capabilities impacted | Capability IDs from `ars_registry.yaml` |
| `follow_up` | Required next step or pending wave | Next action description |

### Governance & Architecture Log

| Entry ID | Date | Component | Change Type | Provenance | Lesson / Change | Evidence | Decision | Status | Affected Capabilities |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GOV-001` | 2026-10-11 | `repo-hygiene` | `SECURITY_OR_PROVENANCE` | Diego Polanco | Untrack root `.env`, establish `.env.example`, remove 458 tracked client mirror files from index, audit upstream licenses. | `08_WAVE_A_EXECUTION_REPORT.md` | `ACCEPTED` | `COMMITTED` (63f7b33) | `G01`-`G05` hygiene |
| `GOV-002` | 2026-10-12 | `governance` | `MIGRATION` | Diego Polanco | Establish machine-readable `docs/governance/ars_registry.yaml`, reconcile `MODE_REGISTRY.md` to mode-bearing components, add prospective learning schema. | `11_WAVE_B0_GOVERNANCE_REPORT.md` | `ACCEPTED` | `COMMITTED` | All 20 capabilities |

