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

## Update Log

| Entry ID | Date (UTC/Local) | Host / Machine | Component / Skill | Type | Description | Git Reference / Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `REG-001` | 2026-10-01 18:50 | `desktop-bsb5hhv-swift-void` | `infra / skills` | `ARCHITECTURE` | Installed 14-skill suite in Antigravity global brain (`~/.gemini/config/skills`) & LitVault workspace via NTFS Directory Junctions. Registered `~/.gemini/config/skills.json`. | Local configured |
| `REG-002` | 2026-10-01 18:52 | `desktop-bsb5hhv-swift-void` | `econ-slides` | `LEARNING` | Added specialized working session & research grant talk reference (`references/working-session-grant-talks.md`) for unclosed theoretical models (Fondecyt PK land-rent benchmark). | Local configured |
| `REG-003` | 2026-10-01 18:55 | `desktop-bsb5hhv-swift-void` | `sync-tools` | `TOOLING` | Created `scripts/sync-skills.ps1` and root `sync.ps1` conflict-prevention sync harness; upgraded `install-local.ps1` to support live junctions. | Local configured |
