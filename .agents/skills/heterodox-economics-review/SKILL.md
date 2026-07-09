---
name: heterodox-economics-review
description: Guidelines and checklists for writing, formatting, and reviewing heterodox economics papers (e.g., Metroeconomica, JPKE) focusing on post-Keynesian and Sraffian growth models.
---

# Heterodox Economics Review & Drafting Guidelines

Use this skill when drafting, reviewing, or revising theoretical macroeconomics papers, particularly Sraffian Supermultiplier (SSM) models and Harrodian instability dynamics.

## 1. Mathematical Rigor & Dynamic Consistency Check
* **Singularity Checks**: Always verify if equations contain singularities at normal values (e.g., capacity utilization $\mu = 1$). If time derivatives are evaluated as $\mu \to 1$, check if term coefficients diverge (such as $\frac{1}{\mu - 1}\hat{\mu}$) and handle them using proper dynamical systems limits (like L'Hôpital's rule or phase-plane analyses).
* **Boundary Conditions**: Ensure proofs of stability or divergence do not simply assume limits, but rigorously check vector fields near boundary conditions ($\mu \to 0$ or $\mu \to \infty$).
* **Logarithmic Derivatives**: Double-check time derivatives of ratios (e.g., investment share $\phi = I/Y$). Ensure variables like capital-capacity ratio $\nu = K/Y^p$ are mapped correctly from accounting identities rather than assumed constant.

## 2. Avoiding Specification Tautologies
* **Behavioral vs. Technological Instability**: Do not model instability by fixing the capacity-to-capital elasticity $\theta \neq 1$ in a way that forces the capital-output ratio to grow to infinity ($\nu \to \infty$). That creates a technological tautology.
* **Induced Technical Change**: Under unbalanced growth, model changes in the capital-output ratio as the result of induced technical change or factor substitution (e.g., letting $\nu_n$ evolve endogenously relative to distribution) rather than using an exogenous constant $\theta$.

## 3. Literature & Conceptual Alignment
* **Harrodian Instability**: Ensure Harrodian instability is defined as a behavioral/expectational phenomenon (such as animal spirits and investment responsiveness in capital accumulation) rather than a technological discrepancy.
* **Core Debates**: Actively engage with:
  - The distinction between Smithian and Harrodian investment functions.
  - The taming of Harrodian instability via expected growth rate adjustments (e.g., Serrano, Freitas, Lavoie, Nikiforos).

## 4. LaTeX Standards
* Statically structure theorems and proofs using `amsthm` package environments: `\begin{proposition}` and `\begin{proof}`.
* Position `\begin{proof}` immediately after `\begin{proposition}`.
* Use `align` and `equation` for numbered derivations.
