# Academic Research Skills (ARS)

[![Version](https://img.shields.io/badge/version-v3.12.0-blue)](CHANGELOG.md)

ARS is a set of agent skills for economics and political-economy research: framing questions, reviewing literature, running and reporting econometrics, writing papers, simulating peer review, building slides, and writing for public audiences. You load the skills into an AI coding agent (Google Antigravity or Claude Code) and work with them in conversation. A standalone Python pipeline is also included for running the full research → write → review cycle from the terminal.

This is Diego Polanco's maintained fork of Cheng-I Wu's [academic-research-skills](https://github.com/Imbad0202/academic-research-skills), extended with economics workflows from Lu Han and original political-economy, econometrics, and literature-review skills. It's used by Diego and collaborators; a public release is pending a licensing review (see [License](#license)).

ARS is a **copilot, not an autopilot**. It does not propose research questions for you, run experiments on its own, or carry a paper from idea to submission without your sign-off at each step. The scope boundaries are written down in [POSITIONING.md](POSITIONING.md).

---

## Two ways to use ARS

| | **A. Agent skills** (most users) | **B. Standalone pipeline** |
|---|---|---|
| What it is | Skill folders your agent reads (`SKILL.md` + references) | `scripts/run_pipeline.py`, a 10-stage state machine |
| You interact via | Chat in Antigravity or Claude Code | Terminal, or an Obsidian note that triggers runs on save |
| Models | Whatever your agent uses | Together AI or Google Gemini via API key |
| Start here | [Install the skills](#install-the-skills) | [Standalone pipeline](#standalone-pipeline) |

---

## Install the skills

### 1. Clone the repo

```powershell
git clone https://github.com/dpolancon/academic-research-skills.git
cd academic-research-skills
```

Clone it somewhere permanent. The install links point back into this folder, so moving or deleting it breaks them.

### 2. Link the skills into your agent

Each agent looks for skills in a specific folder. Every skill is a subfolder containing a `SKILL.md`.

| Agent | Skill folder | Scope |
|---|---|---|
| Google Antigravity | `%USERPROFILE%\.gemini\config\skills\` | All workspaces |
| Claude Code | `%USERPROFILE%\.claude\skills\` | All projects |
| Claude Code | `<your-project>\.claude\skills\` | That project only |

**Windows (PowerShell).** Run from the repo root. It creates directory junctions (links, not copies) and skips anything that already exists:

```powershell
$repo   = (Resolve-Path .).Path
$target = "$env:USERPROFILE\.gemini\config\skills"     # Antigravity
# $target = "$env:USERPROFILE\.claude\skills"          # Claude Code, all projects

$skills = 'deep-research','literature-review','political-economy-research',
          'umass-applied-econometrics','irf-plotting','heterodox-economics-review',
          'academic-paper','econ-write','latex-compilation',
          'academic-paper-reviewer','econ-slides','academic-pipeline',
          'skills\dissemination\public-scholarship'

New-Item -ItemType Directory -Force -Path $target | Out-Null
foreach ($s in $skills) {
    $name = Split-Path $s -Leaf
    $link = Join-Path $target $name
    if (Test-Path $link) { Write-Host "skip (exists): $name"; continue }
    New-Item -ItemType Junction -Path $link -Target (Join-Path $repo $s) | Out-Null
    Write-Host "linked: $name"
}
```

Install only the skills you need by trimming the `$skills` list.

**macOS / Linux:**

```bash
repo="$(pwd)"
target="$HOME/.claude/skills"        # or your agent's skill folder
mkdir -p "$target"
for s in deep-research literature-review political-economy-research \
         umass-applied-econometrics irf-plotting heterodox-economics-review \
         academic-paper econ-write latex-compilation academic-paper-reviewer \
         econ-slides academic-pipeline skills/dissemination/public-scholarship; do
  name="$(basename "$s")"
  [ -e "$target/$name" ] && { echo "skip (exists): $name"; continue; }
  ln -s "$repo/$s" "$target/$name" && echo "linked: $name"
done
```

**To remove one link** without touching the repo files (Windows):

```powershell
[System.IO.Directory]::Delete("$env:USERPROFILE\.gemini\config\skills\<skill-name>")
```

On macOS/Linux, use `rm "$target/<skill-name>"` (no trailing slash, no `-r`).

> **About the bundled installers.** `install-local.ps1` (repo root) is the original installer. It only works if the repo is cloned to `C:\ReposGitHub\academic-research-skills`, installs an older list that includes the deprecated names below, leaves out `literature-review` and `political-economy-research`, and also writes to `AppData\Local\Claude\skills`, a location Claude Code doesn't currently read. `scripts/install-local.ps1` is its replacement and currently handles only `public-scholarship` (`-DryRun` and `-Uninstall` supported). It will cover the remaining skills as the layout migration continues. Until then, use the snippet above.

### 3. Check that it worked

Start a **new** session after linking. Agents load skills at startup.

- **Antigravity:** open a new conversation; the skills should appear in the available-skills list.
- **Claude Code:** run `claude` in any folder, type `/`, and look for the skill names in the menu. Press `Esc` and exit with `/exit`. You don't need to send a prompt.

---

## Pick a skill

You don't usually need to name a skill. Describe the task and the agent picks one. Naming it explicitly ("use literature-review to…") helps when two could fit.

### Frame and research

| I want to… | Skill |
|---|---|
| Turn a vague idea into a research question, through guided questioning | `deep-research` (socratic mode) |
| Get a quick brief, an annotated bibliography, a fact-check, or a PRISMA systematic review | `deep-research` (quick / lit-review / fact-check / systematic-review modes) |
| Build a governed literature review: source notes → citation contracts → paragraph ledgers → staged prose → manuscript text | `literature-review` |
| Design comparative-historical political-economy research: periodization, mechanisms, process tracing, rival explanations | `political-economy-research` |

### Empirics and modeling

| I want to… | Skill |
|---|---|
| Plan or audit applied econometrics: replication, integration order, Toda–Yamamoto, small-sample bootstrap | `umass-applied-econometrics` |
| Produce publication-grade impulse response plots (VAR/SVAR/TVAR, IRF and GIRF) | `irf-plotting` |
| Work on formal heterodox macro models: closures, stability, stock-flow consistency | `heterodox-economics-review` |

### Write

| I want to… | Skill |
|---|---|
| Draft, plan, outline, or revise a paper; write an abstract; convert citation formats | `academic-paper` |
| Apply economics writing conventions (Cochrane, McCloskey, and others) | `econ-write` |
| Set up and compile LaTeX cleanly | `latex-compilation` |

### Review

| I want to… | Skill |
|---|---|
| Get a simulated referee panel (editor, three reviewers, devil's advocate) | `academic-paper-reviewer` |
| …calibrated to a specific advisor or committee | `academic-paper-reviewer` with a profile from [profiles/](profiles/) (for example `profiles/advisors/michael-ash.md`, `profiles/committees/umass-pe.md`) |

### Present and disseminate

| I want to… | Skill |
|---|---|
| Turn a paper into a Beamer talk, discussant slides, or a job-market deck | `econ-slides` |
| Write an op-ed, essay, policy brief, or explainer from research | `public-scholarship` (venue calibration via `profiles/venues/jacobin-lat.md`) |

### Run the whole cycle

| I want to… | Skill |
|---|---|
| Go research → write → integrity check → review → revise → finalize, with a checkpoint at every stage | `academic-pipeline` |

The full list of callable modes for `deep-research`, `academic-paper`, `academic-paper-reviewer`, and `academic-pipeline` is in [MODE_REGISTRY.md](MODE_REGISTRY.md). The authoritative component list is the governance registry, [docs/governance/ars_registry.yaml](docs/governance/ars_registry.yaml).

---

## Deprecated names

These names still work as redirects so old prompts don't break, but new work should use the replacement.

| Old name | Use instead |
|---|---|
| `advisor-reviewer` | `academic-paper-reviewer` + `profiles/advisors/michael-ash.md` |
| `PE-phd-committee` | `academic-paper-reviewer` + `profiles/committees/umass-pe.md` |
| `editor-jacobin-lat` | `public-scholarship` + `profiles/venues/jacobin-lat.md` |
| `prose-register-critic` | `shared/protocols/prose_discipline_protocol.md` and `tools/prose_checks/check_prose_patterns.py` |

---

## Standalone pipeline

### Install

Requires Python 3 (development and tests use 3.14).

```bash
pip install -r requirements.txt
```

### API keys

Set the key for the provider you'll use. `.env.example` lists the variables, but the scripts **do not load `.env` files automatically**; set them in your shell.

```powershell
# PowerShell
$env:TOGETHER_API_KEY = "your-together-key"
$env:GEMINI_API_KEY   = "your-gemini-key"
```

```bash
# bash / zsh
export TOGETHER_API_KEY="your-together-key"
export GEMINI_API_KEY="your-gemini-key"
```

If `TOGETHER_API_KEY` isn't set, the gateway falls back to `docs/together_AI_baseURL_APIKEY.txt` (gitignored) with lines `TOGETHER_API_KEY=...` and `TOGETHER_BASE_URL=https://api.together.ai/v1`.

### Configuration precedence

1. CLI flags: `--provider` (`together` or `gemini`), `--model`, `--base-url`, `--config`
2. Environment: `DEFAULT_PROVIDER`, `DEFAULT_MODEL`
3. `agent_config.yaml` in the repo root (or the file passed with `--config`)
4. Built-in defaults: provider `together`, model `Qwen/Qwen3.5-9B`, base URL `https://api.together.ai/v1`

### Run it

```bash
# Interactive dashboard against a project folder
python scripts/run_pipeline.py --target-dir "C:\path\to\your\project"

# Use Gemini instead of the default
python scripts/run_pipeline.py --target-dir "C:\path\to\your\project" --provider gemini --model <gemini-model-id>

# Obsidian mode: watch a vault and run a stage whenever the task note is saved
python scripts/run_pipeline.py --target-dir "C:\path\to\your\vault" --obsidian-vault
```

`--target-dir` also fences writes: the pipeline won't write outside that folder. Pipeline state is kept in `passport.yaml` inside the target folder.

**Obsidian task note.** Write your request in `ARS/ARS_Active_Task.md` inside the target folder:

```markdown
---
stage: 1
mode: socratic
run_on_save: true
---

I want to review the literature on AI-driven central banking tools and financial stability.
```

Saving with `run_on_save: true` triggers the stage. When it finishes, the runner advances `stage` and sets `run_on_save` back to `false` so it doesn't loop.

### Stages

```
1    RESEARCH      research question brief + methodology blueprint
2    WRITE         manuscript draft
2.5  INTEGRITY     citation, reference and claim checks (mandatory gate)
3    REVIEW        peer-review reports + editor decision
4    REVISE        revised draft + response to reviewers
3'   RE-REVIEW     editor verification (may route to 4')
4'   RE-REVISE     final round of revisions, if requested
4.5  FINAL CHECK   citation and reference integrity (mandatory gate)
5    FINALIZE      final manuscript layout
6    COMPLETED
```

Details: [academic-pipeline/references/pipeline_state_machine.md](academic-pipeline/references/pipeline_state_machine.md) and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

### Companion tools

```bash
# Check a reference against Crossref, OpenAlex, Semantic Scholar and arXiv
python scripts/cross_model_client.py verify --reference "Walters, W. H. (2023). Fabrication in ChatGPT citations. Scientific Reports, 13, 14045." --context "ChatGPT citations are often fabricated (Walters, 2023)."

# Devil's-advocate critique of a draft or outline
python scripts/cross_model_client.py critique --material "Your draft or outline text"
```

---

## Repository map

| Path | What it is |
|---|---|
| `deep-research/`, `literature-review/`, `academic-paper/`, … | **Skills.** One folder per skill, each with a `SKILL.md`. |
| `skills/` | New skill layout, being migrated in stages. `skills/dissemination/public-scholarship/` is the first skill moved; the other entries are compatibility links. |
| `profiles/` | Calibration profiles (advisors, committees, scholars, venues) used by the review and dissemination skills. |
| `shared/`, `agents/` | Protocols, contracts and agent definitions shared across skills. |
| `tools/` | Deterministic helper scripts (prose checks, column audit). |
| `commands/`, `.claude-plugin/`, `hooks/` | Claude Code slash commands and plugin packaging. |
| `scripts/` | Standalone pipeline, model gateway, installers, validators. |
| `docs/` | Setup, architecture, governance registry, design records. |
| `evals/`, `tests/`, `examples/` | Evaluation sets, tests, example artifacts (see [examples/showcase/](examples/showcase/)). |

**Status.** The repository is partway through a layout migration ("Wave F"). The first pilot (moving `public-scholarship` into `skills/dissemination/`) is complete; the remaining skills will move in later batches. Old paths keep working throughout.

---

## Further reading

- [QUICKSTART.md](QUICKSTART.md): the shortest path to a first session
- [POSITIONING.md](POSITIONING.md): what ARS will and won't do
- [MODE_REGISTRY.md](MODE_REGISTRY.md): callable modes
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md): pipeline architecture
- [CHANGELOG.md](CHANGELOG.md): release history
- [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md)

---

## License

Licensing and provenance vary by component. See [LICENSE](LICENSE) and [docs/PROVENANCE.md](docs/PROVENANCE.md). A repository-wide licensing reconciliation is currently on HOLD pending provenance review.
