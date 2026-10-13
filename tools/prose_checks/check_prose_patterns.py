#!/usr/bin/env python3
"""
tools/prose_checks/check_prose_patterns.py

Deterministic prose pattern diagnostic tool for academic manuscripts.
Implements mechanical checks defined in shared/protocols/prose_discipline_protocol.md.

Runs strictly offline using Python standard library.
Does NOT perform AI-detection or author intention inference.
Flags are emitted as REVIEW recommendations for human editors.
"""

import sys
import re
import json
import argparse
from typing import Dict, List, Any, Optional, Set, Tuple


# Default Category A protected technical terms (immune from replacement / jargon flags)
DEFAULT_CATEGORY_A_TERMS = {
    "rate of exploitation",
    "transformation elasticity",
    "balance-of-payments constraint",
    "companion matrix eigenvalues",
    "sraffa-kurz choice of technique",
    "reserve army of labor",
    "johansen trace test",
    "supermultiplier",
    "effective demand",
    "organic composition of capital",
    "cointegrating vector",
    "cointegration vector",
    "error correction model",
    "vector error correction",
    "heteroskedasticity",
    "autocorrelation",
    "eigenvalues",
    "null hypothesis",
    "parallel trends",
    "local average treatment effect",
    "instrumental variable",
    "regression discontinuity",
    "difference-in-differences",
    "asymptotic normality",
    "leontief",
    "bernoulli ode",
    "supermultipliers",
}

# Category C rhetorical scaffolding and branded metaphors
CATEGORY_C_PATTERNS: List[Tuple[str, str, str]] = [
    # (regex_pattern, pattern_label, replacement_advice)
    (r"\bempirical tournament\b", "branded_metaphor", "Replace branded metaphor with 'model comparison' or 'specification testing'."),
    (r"\badmissibility gates?\b", "branded_metaphor", "Replace with 'cointegration and stability criteria' or 'diagnostic benchmarks'."),
    (r"\bsystem-admissibility criteria\b", "branded_metaphor", "Replace with 'specification diagnostics'."),
    (r"\bblack-box screening protocol\b", "branded_metaphor", "Replace with 'diagnostic screening procedure'."),
    (r"\bdeliberately stress test\b", "branded_metaphor", "Replace with 'evaluate sensitivity' or 'assess robustness'."),
    (r"\bprofound institutional divergence\b", "inflated_scaffolding", "Replace with direct empirical description of institutional differences."),
    (r"\bauthorization gate\b", "workflow_leakage", "Remove workflow scaffolding; describe empirical criteria directly."),
    (r"\bretained criteria\b", "workflow_leakage", "Replace with 'selected specifications' or 'diagnostic criteria'."),
    (r"\bediting ledger\b", "workflow_leakage", "Remove internal editing apparatus reference."),
    (r"\binterpretive move\b", "metanarrative_tell", "Remove self-referential analytical narrations."),
    (r"\banalytical move\b", "metanarrative_tell", "Remove self-referential analytical narrations."),
    (r"\bselection filter\b", "workflow_leakage", "Replace with 'selection benchmark' or 'diagnostic filter'."),
    (r"\bempirical objects?\b", "inflated_scaffolding", "Replace with the actual empirical entity (e.g. 'relationship under test', 'data sample')."),
    (r"\btherapeutic\b", "inflated_scaffolding", "Remove emotional or moralizing rhetoric from technical description."),
]

# Pipeline and internal script path leaks in prose
PIPELINE_LEAK_PATTERNS: List[Tuple[str, str]] = [
    (r"\\texttt\{output/[^}]+\}", "LaTeX internal output file path leak in prose."),
    (r"\boutput/report_[a-zA-Z0-9_\.]+", "Internal pipeline report path leak in prose."),
    (r"\bcodes/[a-zA-Z0-9_\.]+\b", "Internal code directory path leak in prose."),
    (r"\bscripts/[a-zA-Z0-9_\.]+\.py\b", "Internal script reference in manuscript prose."),
]

# Canned transition words that become mechanical when repeated
CANNED_TRANSITION_WORDS = [
    "furthermore",
    "moreover",
    "additionally",
    "in addition",
    "importantly",
    "crucially",
]

# Contrast formulas
CONTRAST_TEMPLATE_REGEX = re.compile(
    r"\b(not\s+[^,;]+,\s+but\b|not\s+only\s+[^,;]+\s+but\s+also\b|rather\s+than\s+[^,;]+,|\bfar\s+from\s+[^,;]+,|\binstead\s+of\s+[^,;]+,)",
    re.IGNORECASE
)

# Evaluative intensifiers
EVALUATIVE_INTENSIFIERS = [
    "crucially",
    "decisive",
    "profound",
    "profoundly",
    "stark",
    "starkly",
    "striking",
    "strikingly",
    "dramatic",
    "dramatically",
    "remarkable",
    "remarkably",
]


class ProsePatternChecker:
    def __init__(self, protected_terms: Optional[Set[str]] = None):
        self.protected_terms = set(DEFAULT_CATEGORY_A_TERMS)
        if protected_terms:
            self.protected_terms.update(t.lower() for t in protected_terms)

    def analyze_text(self, text: str) -> Dict[str, Any]:
        """Analyzes text deterministically and returns structured diagnostic report."""
        lines = text.splitlines()
        flags: List[Dict[str, Any]] = []
        protected_found: Set[str] = set()

        # Track protected terms present in the text
        lower_text = text.lower()
        for term in self.protected_terms:
            if re.search(r"\b" + re.escape(term) + r"\b", lower_text):
                protected_found.add(term)

        # 1. Check Category C Scaffolding and Branded Metaphors
        for line_num, line in enumerate(lines, start=1):
            for pat, label, advice in CATEGORY_C_PATTERNS:
                matches = list(re.finditer(pat, line, re.IGNORECASE))
                for match in matches:
                    matched_str = match.group(0)
                    # Check if part of a protected term
                    if self._is_protected(matched_str, line):
                        continue
                    flags.append({
                        "family": "category_c_scaffolding",
                        "severity": "REVIEW",
                        "line": line_num,
                        "matched_text": matched_str,
                        "pattern_label": label,
                        "message": advice,
                    })

            # Check pipeline metadata leaks
            for pat, advice in PIPELINE_LEAK_PATTERNS:
                matches = list(re.finditer(pat, line, re.IGNORECASE))
                for match in matches:
                    flags.append({
                        "family": "pipeline_metadata_leakage",
                        "severity": "REVIEW",
                        "line": line_num,
                        "matched_text": match.group(0),
                        "pattern_label": "internal_path_leak",
                        "message": advice,
                    })

        # Paragraph-level analyses
        paragraphs = self._split_paragraphs(text)
        for p_idx, (p_text, start_line) in enumerate(paragraphs, start=1):
            p_flags = self._analyze_paragraph(p_text, start_line)
            flags.extend(p_flags)

        # Multi-sentence opening repetitions across entire text
        start_flags = self._check_sentence_start_repetitions(lines)
        flags.extend(start_flags)

        # Summarize counts
        flag_counts: Dict[str, int] = {}
        for f in flags:
            fam = f["family"]
            flag_counts[fam] = flag_counts.get(fam, 0) + 1

        status = "REVIEW" if flags else "PASS"

        return {
            "status": status,
            "summary": {
                "total_flags": len(flags),
                "flag_counts": flag_counts,
                "protected_terms_identified": len(protected_found),
            },
            "flags": flags,
            "protected_terms": sorted(list(protected_found)),
        }

    def _is_protected(self, matched_str: str, context_line: str) -> bool:
        """Verifies if the matched string is part of a declared Category A protected term."""
        matched_lower = matched_str.lower()
        context_lower = context_line.lower()
        for term in self.protected_terms:
            if matched_lower in term and term in context_lower:
                return True
        return False

    def _split_paragraphs(self, text: str) -> List[Tuple[str, int]]:
        """Splits text into paragraphs with starting line numbers."""
        paragraphs = []
        current_lines = []
        start_line = 1
        current_start = 1

        lines = text.splitlines()
        for idx, line in enumerate(lines, start=1):
            if not line.strip():
                if current_lines:
                    paragraphs.append(("\n".join(current_lines), current_start))
                    current_lines = []
            else:
                if not current_lines:
                    current_start = idx
                current_lines.append(line)

        if current_lines:
            paragraphs.append(("\n".join(current_lines), current_start))

        return paragraphs

    def _analyze_paragraph(self, p_text: str, start_line: int) -> List[Dict[str, Any]]:
        """Analyzes a single paragraph for clustering and density issues."""
        p_flags = []

        # Check canned transitions count in paragraph
        transition_matches = []
        for word in CANNED_TRANSITION_WORDS:
            matches = list(re.finditer(r"\b" + re.escape(word) + r"\b", p_text, re.IGNORECASE))
            for m in matches:
                transition_matches.append((word, m.start()))

        if len(transition_matches) >= 2:
            matched_words = [m[0] for m in transition_matches]
            p_flags.append({
                "family": "canned_transitions",
                "severity": "REVIEW",
                "line": start_line,
                "matched_text": ", ".join(matched_words),
                "pattern_label": "canned_transition_cluster",
                "message": (
                    f"Clustered canned transition adverbs ({len(transition_matches)} found in paragraph). "
                    "Vary transitions or rely on thematic progression."
                ),
            })

        # Check contrast template repetition in paragraph (>= 2)
        contrast_matches = list(CONTRAST_TEMPLATE_REGEX.finditer(p_text))
        if len(contrast_matches) >= 2:
            matched_snippets = [m.group(0) for m in contrast_matches]
            p_flags.append({
                "family": "contrast_template_repetition",
                "severity": "REVIEW",
                "line": start_line,
                "matched_text": "; ".join(matched_snippets),
                "pattern_label": "contrast_formula_cluster",
                "message": (
                    f"Multiple contrast formulas ({len(contrast_matches)} found in paragraph). "
                    "Convert secondary contrasts into direct declarative assertions."
                ),
            })

        # Check evaluative intensifier density in paragraph (>= 3)
        intensifier_matches = []
        for word in EVALUATIVE_INTENSIFIERS:
            matches = list(re.finditer(r"\b" + re.escape(word) + r"\b", p_text, re.IGNORECASE))
            for m in matches:
                intensifier_matches.append(m.group(0))

        if len(intensifier_matches) >= 3:
            p_flags.append({
                "family": "evaluative_intensifiers",
                "severity": "REVIEW",
                "line": start_line,
                "matched_text": ", ".join(intensifier_matches),
                "pattern_label": "intensifier_cluster",
                "message": (
                    f"Dense cluster of evaluative intensifiers ({len(intensifier_matches)} found in paragraph). "
                    "Let point estimates and test statistics convey significance."
                ),
            })

        return p_flags

    def _check_sentence_start_repetitions(self, lines: List[str]) -> List[Dict[str, Any]]:
        """Identifies mechanical repetition of sentence beginnings (3+ consecutive)."""
        full_text = "\n".join(lines)
        # Approximate sentence boundaries: period, question mark, or exclamation mark followed by space/newline
        raw_sentences = re.split(r"(?<=[.!?])\s+", full_text)
        clean_sentences = [s.strip() for s in raw_sentences if s.strip()]

        flags = []
        if len(clean_sentences) < 3:
            return flags

        def get_first_token(s: str) -> str:
            # Strip markdown formatting or punctuation at start
            clean = re.sub(r"^[^a-zA-Z0-9]+", "", s)
            tokens = clean.split()
            return tokens[0].lower() if tokens else ""

        consecutive_count = 1
        current_token = get_first_token(clean_sentences[0])
        start_idx = 0

        for i in range(1, len(clean_sentences)):
            token = get_first_token(clean_sentences[i])
            # Skip very short or empty tokens
            if token and token == current_token and len(token) > 1:
                consecutive_count += 1
            else:
                if consecutive_count >= 3:
                    flags.append({
                        "family": "sentence_start_repetition",
                        "severity": "REVIEW",
                        "line": 1,  # approximate
                        "matched_text": f"'{current_token.capitalize()}' repeated {consecutive_count} times",
                        "pattern_label": "mechanical_sentence_openings",
                        "message": (
                            f"{consecutive_count} consecutive sentences start with '{current_token.capitalize()}'. "
                            "Vary sentence openings using conditional clauses or substantive nouns."
                        ),
                    })
                current_token = token
                consecutive_count = 1
                start_idx = i

        if consecutive_count >= 3:
            flags.append({
                "family": "sentence_start_repetition",
                "severity": "REVIEW",
                "line": 1,
                "matched_text": f"'{current_token.capitalize()}' repeated {consecutive_count} times",
                "pattern_label": "mechanical_sentence_openings",
                "message": (
                    f"{consecutive_count} consecutive sentences start with '{current_token.capitalize()}'. "
                    "Vary sentence openings using conditional clauses or substantive nouns."
                ),
            })

        return flags


def main():
    parser = argparse.ArgumentParser(
        description="ARS Deterministic Prose Pattern Diagnostic Tool (Offline)"
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Path to the academic text or LaTeX file to inspect. If omitted, reads stdin.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit output formatted as structured JSON.",
    )
    parser.add_argument(
        "--text",
        type=str,
        default=None,
        help="Direct text snippet to inspect instead of reading a file.",
    )
    parser.add_argument(
        "--protected-terms",
        nargs="*",
        default=[],
        help="Additional Category A protected terms to preserve.",
    )

    args = parser.parse_args()

    content = ""
    if args.text is not None:
        content = args.text
    elif args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            sys.stderr.write(f"Error reading file '{args.file}': {e}\n")
            sys.exit(1)
    else:
        if sys.stdin.isatty():
            parser.print_help()
            sys.exit(0)
        content = sys.stdin.read()

    checker = ProsePatternChecker(protected_terms=set(args.protected_terms))
    report = checker.analyze_text(content)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        status_label = "[PASS] Clean prose patterns" if report["status"] == "PASS" else "[REVIEW] Prose patterns recommended for inspection"
        print("=" * 60)
        print(f"ARS Prose Pattern Report: {status_label}")
        print("=" * 60)
        print(f"Total flags: {report['summary']['total_flags']}")
        print(f"Protected technical terms recognized: {report['summary']['protected_terms_identified']}")
        if report["protected_terms"]:
            print(f"  Terms: {', '.join(report['protected_terms'])}")
        print("-" * 60)

        if not report["flags"]:
            print("No mechanical scaffolding or repetitive pattern clusters detected.")
        else:
            for idx, flag in enumerate(report["flags"], start=1):
                print(f"#{idx} Line {flag['line']} [{flag['family'].upper()}] - {flag['severity']}")
                print(f"   Match: \"{flag['matched_text']}\"")
                print(f"   Action: {flag['message']}")
                print()

    # Always exit 0 unless execution error; review flags do not break build
    sys.exit(0)


if __name__ == "__main__":
    main()
