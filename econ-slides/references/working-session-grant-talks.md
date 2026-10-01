# Working Session Presentations for Research Grants (Obsidian Notes → Beamer)

Guidelines for turning ongoing research notes, theoretical blueprints, and vault notes (such as Obsidian Markdown files) into Beamer slide decks for research team working sessions and research grant milestones (e.g., Fondecyt, NSF, ERC).

---

## 1. Core Genre Distinction: Seminar Talk vs. Working Session

A standard seminar talk presents a finished paper to convince an outside audience of a completed result. 
A **grant working session talk** has a different purpose:
1. **Report stabilized architecture**: What parts of the model or empirical design are settled and mutually agreed upon.
2. **Stress-test open closures**: What analytical equations, parameter calibrations, or theoretical bridges remain open.
3. **Align team roles**: Define the exact derivation path, empirical tasks, and grant deadlines for co-investigators.

Never present speculative conjectures as proven results. Explicitly guard the presentation boundary.

---

## 2. Epistemological Tagging Protocol (From Vault Notes to Slides)

When migrating notes containing active modeling (e.g., Post-Keynesian financial fragility, land rent, DSGE, or econometric specifications), preserve three explicit labels:

- **`[SOURCE]`**: Relations taken directly from established literature (e.g., Foley 2001, 2003; Stiglitz, Hirano & Toda 2021). Always comment or cite the exact equation/proposition.
- **`[PROJECT ADAPTATION]`**: Bridges, reinterpretations, or parameterizations introduced by the project team.
- **`[TO BE DERIVED]`**: Relations, stability conditions, or theorems that must emerge from formalization.

### Beamer Implementation Pattern
Use colored tags or dedicated boxes in LaTeX/Beamer:
```latex
\newcommand{\TagSource}{\textcolor{teal}{\textbf{\footnotesize [SOURCE]}}}
\newcommand{\TagAdapt}{\textcolor{blue}{\textbf{\footnotesize [ADAPTATION]}}}
\newcommand{\TagOpen}{\textcolor{magenta}{\textbf{\footnotesize [TO BE DERIVED]}}}

\begin{frame}{Estructura de balances y compromisos financieros}
  \framesubtitle{Integración de deuda bancaria y renta del suelo}
  \begin{itemize}
    \item \TagSource Activos y pasivos de las firmas siguen la contabilidad de Foley (2001).
    \item \TagAdapt Se añade el colateral de tierra valorizado a precio de mercado $p_L L$.
    \item \TagOpen Condición de transición a régimen Ponzi en presencia de renta diferencial.
  \end{itemize}
  \Takeaway{La arquitectura contable está cerrada; la dinámica de bifurcación permanece abierta a discusión.}
\end{frame}
```

---

## 3. The 30–45 Minute Team Working Session Budget

| Block | Focus | Slide Budget | Time Target |
| :--- | :--- | :--- | :--- |
| **I. Agenda & Contract** | What is stabilized vs. what is open for discussion today | 1–2 slides | 3 min |
| **II. Core Framework** | Baseline accounting, environment, agents, balance sheets | 3–5 slides | 8–10 min |
| **III. Analytical Blocks** | Equations of investment, land valuation, banking loans | 4–6 slides | 12–15 min |
| **IV. Open Closures** | Competing closures, stability conditions, team debate | 3–4 slides | 10–12 min |
| **V. Grant Road-map** | Fondecyt/grant deliverables, tasks, calendar | 1–2 slides | 3–5 min |
| **Total** | | **12–19 slides** | **35–45 min** |

---

## 4. Converting Obsidian Markdown Notes to LaTeX/Beamer

1. **Vault Note Ingestion**:
   - Locate the target note (e.g. `Notas_Modelacion/N03_Beamer.md`).
   - Extract the frontmatter (`status`, `contract`, `questions`).
   - Map each `# Slide X` or H2/H3 block to a distinct Beamer `frame`.
2. **Formula Discipline**:
   - Convert standard Markdown LaTeX math `$...$` and `$$...$$` to clean Beamer equations.
   - Use `\begin{align*}` with precise alignment markers (`&`) for systems of equations.
   - Avoid shrinking text with `\tiny` or `\scriptsize`; if a system doesn't fit, split into progressive frames (e.g., `Firmas`, `Bancos`, `Rentas`).
3. **Team Discussion Prompts**:
   - Conclude key frames with an explicit `\Takeaway{...}` or `\textbf{Discusión para el equipo:}` to focus the room's attention on the exact technical decision needed.

---

## 5. Multilingual & Grant-Specific Requirements (e.g., Fondecyt)

- When drafting in Spanish, use UTF-8 and proper babel/polyglossia settings:
  ```latex
  \usepackage[spanish,es-nodecimaldot]{babel}
  ```
- Keep technical economic nomenclature consistent (e.g. *stock-flow consistent*, *rollover*, *fragilidad financiera*, *hedge/speculative/Ponzi*).
- Align slide titles with grant objectives stated in the proposal (Objetivo General, Objetivos Específicos).
