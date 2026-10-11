# Security Policy

## Supported versions

Only the latest release on the `main` branch receives security fixes.

| Version | Supported |
|---------|-----------|
| Latest (`main`) | Yes |
| Older releases | No |

## Reporting a vulnerability

If you find a security issue (e.g. prompt injection, credential exposure, unintended data exfiltration through API calls), **do not open a public issue**.

If GitHub's **"Report a vulnerability"** option is available under the repository's [Security Advisories](https://github.com/dpolancon/academic-research-skills/security/advisories) page, use that private reporting channel:

1. Go to the [Security Advisories](https://github.com/dpolancon/academic-research-skills/security/advisories) page.
2. Click **"Report a vulnerability"**.
3. Fill in the details — what you found, how to reproduce it, and the potential impact.

If private vulnerability reporting is not available, do not disclose sensitive security details in a public issue. Contact the repository maintainer privately before sharing reproduction details.

For ordinary non-sensitive bugs and feature requests, use the repository's [Issues](https://github.com/dpolancon/academic-research-skills/issues) page instead.

You will receive a response within 7 days. If the report is accepted, a fix will be issued and credited in the release notes. If declined, you will receive an explanation.

## Scope

The following are in scope for security reports:

- **Prompt injection** — inputs that cause agents to bypass IRON RULE constraints, integrity gates, or ethics protocols
- **Credential leakage** — configurations or agent behaviors that expose API keys (`ARS_CROSS_MODEL`, Semantic Scholar API key, etc.)
- **Data exfiltration** — agent behaviors that send user research data to unintended external services
- **Integrity gate bypass** — inputs that skip Stage 2.5 or Stage 4.5 blocking checks

The following are **out of scope**:

- AI output quality issues (hallucinations, weak arguments) — these are research limitations, not security vulnerabilities
- Feature requests or general bugs — use [Issues](https://github.com/dpolancon/academic-research-skills/issues) instead

