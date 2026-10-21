# Quick Start

From zero to a first ARS session in about five minutes. For details, see the [README](README.md).

## 1. Clone and link

```powershell
git clone https://github.com/dpolancon/academic-research-skills.git
cd academic-research-skills
```

Then link the skills into your agent using the snippet in [README → Install the skills](README.md#install-the-skills). Antigravity reads `%USERPROFILE%\.gemini\config\skills\`; Claude Code reads `%USERPROFILE%\.claude\skills\` or `<project>\.claude\skills\`.

## 2. Start a new session

Open a new Antigravity conversation, or run `claude` in your project folder. Skills are loaded when a session starts.

## 3. Ask for what you need

Describe the task. The agent picks the skill. Some starting points:

**Find a research question**
> "I'm interested in why Chile's capital stock series diverge after 1973, but I don't have a sharp question yet. Help me think it through."

`deep-research` asks questions instead of giving answers, and ends with a research plan you wrote.

**Build a literature review**
> "Use literature-review to set up a control bundle for a section on capital measurement debates."

**Audit an econometric strategy**
> "Here's my VAR specification and unit-root results. Check integration order and whether Toda–Yamamoto applies."

`umass-applied-econometrics`; add `irf-plotting` for the figures.

**Get a referee report**
> "Review this draft as a five-person referee panel." (attach the paper)

`academic-paper-reviewer`. Add "calibrated to my committee" to use `profiles/committees/umass-pe.md`.

**Make slides**
> "Turn this paper into a 20-minute seminar talk in Beamer."

**Write for the public**
> "Turn section 3 into a 1,200-word op-ed for a general audience."

`public-scholarship`.

**Run the full cycle**
> "I want to take this project from research question to a finished, reviewed paper."

`academic-pipeline` runs ten stages and stops for your confirmation after each one.

## Which skill when?

| I want to… | Skill |
|---|---|
| Explore a vague idea | `deep-research` (socratic) |
| Quick literature summary or fact-check | `deep-research` (quick / fact-check) |
| Systematic review (PRISMA) | `deep-research` (systematic-review) |
| Governed literature-review section | `literature-review` |
| Political-economy research design | `political-economy-research` |
| Applied econometrics | `umass-applied-econometrics` |
| Write or revise a paper | `academic-paper` + `econ-write` |
| Referee report | `academic-paper-reviewer` |
| Slides | `econ-slides` |
| Op-ed, essay, policy brief | `public-scholarship` |
| Everything, end to end | `academic-pipeline` |

The full table, with deprecated names and the standalone Python pipeline, is in the [README](README.md#pick-a-skill).
