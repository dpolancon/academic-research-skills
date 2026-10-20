#!/usr/bin/env python3
"""
style_risk_auditor.py — Structural No-AI-Trace Style-Risk Auditor

Evaluates academic manuscript prose against 18 structural style-risk pattern
families to detect repetitive rhetorical formulas, syntactic monotony, and
workflow metadata leakage without attempting pseudo-scientific "AI detection".

Specification: literature-review/references/structural_style_risk_guidelines.md
Consumes: shared/protocols/prose_discipline_protocol.md
"""

import re
import sys
import argparse
from typing import List, Dict, Any, Tuple


class StyleRiskAuditor:
    """Deterministic structural style-risk auditor."""

    WORKFLOW_LEAK_PATTERNS = [
        r"\bledger\b", r"\bproposition\s+slot\b", r"\bcluster\s+note\b",
        r"\bquery\s+pack\b", r"\bCCC_[A-Z0-9_]+\b", r"\bSRC_[A-Z0-9_]+\b",
        r"\bCLUS_[A-Z0-9_]+\b", r"\bprovenance\s+tag\b", r"\bsaturation\s+lock\b",
        r"\bextraction\s+pass\b", r"\bexception\s+query\b"
    ]

    GENERIC_BUZZWORDS = [
        r"\bframework\b", r"\barchitecture\b", r"\bdimension\b",
        r"\blens\b", r"\bnexus\b", r"\bintervention\b", r"\btapestry\b",
        r"\bmosaic\b", r"\bparadigm\b"
    ]

    INFLATED_NOVELTY_PATTERNS = [
        r"\bgroundbreaking\b", r"\bunprecedented\b", r"\bvital\s+lacuna\b",
        r"\bcrucial\s+breakthrough\b", r"\bnovel\s+nexus\b", r"\bfirst\s+to\s+ever\b"
    ]

    METADISCOURSE_PATTERNS = [
        r"\bin\s+this\s+section\s+we\b", r"\bit\s+is\s+important\s+to\s+note\s+that\b",
        r"\bhaving\s+established\b", r"\bit\s+is\s+worth\s+emphasizing\b",
        r"\bwe\s+now\s+turn\s+our\s+attention\s+to\b", r"\bas\s+discussed\s+above\b",
        r"\bit\s+should\s+be\s+observed\s+that\b"
    ]

    MECHANICAL_SYNTHESIS_PATTERNS = [
        r"\btaken\s+together\b", r"\bin\s+summary\b", r"\bcollectively,\s+these\b",
        r"\bultimately,\s+this\s+literature\b", r"\bin\s+sum,\b"
    ]

    HOLLOW_CONNECTIVES = [
        r"\bimportantly,\s+this\b", r"\bcrucially,\s+the\b",
        r"\binterestingly,\s+this\b", r"\bnotably,\s+these\b"
    ]

    PROSPECTIVE_PATTERNS = [
        r"\bthe\s+following\s+(section|paragraph|chapter)\s+turns\b",
        r"\bin\s+the\s+next\s+(section|paragraph)\b",
        r"\bwill\s+be\s+addressed\s+in\s+subsequent\b"
    ]

    BINARY_SYMMETRY_PATTERNS = [
        r"\bwhile\s+[^,]+argues?[^,]+,\s+[^,]+contends?\b",
        r"\bon\s+the\s+one\s+hand[^,]+,\s+on\s+the\s+other\s+hand\b",
        r"\bwhereas\s+[^,]+asserts?[^,]+,\s+[^,]+maintains?\b"
    ]

    def split_paragraphs(self, text: str) -> List[str]:
        paras = re.split(r"\n\s*\n", text.strip())
        return [p.strip() for p in paras if p.strip()]

    def split_sentences(self, paragraph: str) -> List[str]:
        # Simple sentence splitter preserving citations
        raw = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'\(])", paragraph)
        return [s.strip() for s in raw if s.strip()]

    def audit_text(self, text: str) -> Dict[str, Any]:
        paragraphs = self.split_paragraphs(text)
        total_paragraphs = len(paragraphs)
        flags: List[Dict[str, Any]] = []

        para_lengths = [len(p.split()) for p in paragraphs]
        all_sentence_lengths: List[int] = []

        consecutive_topic_openers = 0
        annotated_bib_count = 0
        binary_symmetry_count = 0
        colon_list_count = 0
        em_dash_count = 0
        citation_dump_count = 0

        for p_idx, p in enumerate(paragraphs, 1):
            sentences = self.split_sentences(p)
            for s in sentences:
                all_sentence_lengths.append(len(s.split()))

            # Check Paragraph Opener (Abstract topic sentence monotony)
            if sentences:
                opener = sentences[0]
                if re.match(r"^(The|A|An|This|Scholarly|Recent)\s+[A-Za-z\s]+(plays|represents|constitutes|is\s+central|has\s+long\s+been)", opener):
                    consecutive_topic_openers += 1
                else:
                    consecutive_topic_openers = 0
                if consecutive_topic_openers >= 3:
                    flags.append({
                        "family": "RISK_TOPIC_SENTENCE_MONOTONY",
                        "paragraph": p_idx,
                        "description": "Repeated formulaic abstract topic sentence opening paragraph.",
                        "matched_text": opener[:80] + "..."
                    })

                # Check Paragraph Ending Announcement
                closer = sentences[-1]
                for pat in self.PROSPECTIVE_PATTERNS:
                    if re.search(pat, closer, re.IGNORECASE):
                        flags.append({
                            "family": "RISK_PROSPECTIVE_ANNOUNCEMENTS",
                            "paragraph": p_idx,
                            "description": "Paragraph ends with a procedural announcement of what follows.",
                            "matched_text": closer
                        })

            # Check Annotated-Bibliography sequencing in paragraph
            author_seq_in_p = 0
            for s in sentences:
                if re.match(r"^[A-Z][a-zA-Z\s]+(\(\d{4}\)|\sand\s+[A-Z][a-zA-Z\s]+\(\d{4}\))\s+(argues|finds|shows|demonstrates|suggests|examines)", s):
                    author_seq_in_p += 1
            if author_seq_in_p >= 2:
                flags.append({
                    "family": "RISK_ANNOTATED_BIB_SEQUENCING",
                    "paragraph": p_idx,
                    "description": f"Paragraph contains {author_seq_in_p} consecutive 'Author (Year) verb' sentence openings.",
                    "matched_text": f"Found {author_seq_in_p} instances in paragraph {p_idx}"
                })

            # Check individual sentence patterns
            for s_idx, s in enumerate(sentences, 1):
                # 1. Workflow vocabulary leaks
                for pat in self.WORKFLOW_LEAK_PATTERNS:
                    m = re.search(pat, s, re.IGNORECASE)
                    if m:
                        flags.append({
                            "family": "RISK_WORKFLOW_VOCABULARY_LEAK",
                            "paragraph": p_idx,
                            "sentence": s_idx,
                            "description": f"Internal pipeline term leaked into prose: '{m.group(0)}'",
                            "matched_text": s
                        })

                # 2. Inflated novelty
                for pat in self.INFLATED_NOVELTY_PATTERNS:
                    m = re.search(pat, s, re.IGNORECASE)
                    if m:
                        flags.append({
                            "family": "RISK_INFLATED_NOVELTY",
                            "paragraph": p_idx,
                            "sentence": s_idx,
                            "description": f"Inflated gap/novelty rhetoric detected: '{m.group(0)}'",
                            "matched_text": s
                        })

                # 3. Metadiscourse
                for pat in self.METADISCOURSE_PATTERNS:
                    m = re.search(pat, s, re.IGNORECASE)
                    if m:
                        flags.append({
                            "family": "RISK_EXCESSIVE_METADISCOURSE",
                            "paragraph": p_idx,
                            "sentence": s_idx,
                            "description": f"Excessive procedural metadiscourse: '{m.group(0)}'",
                            "matched_text": s
                        })

                # 4. Mechanical synthesis
                for pat in self.MECHANICAL_SYNTHESIS_PATTERNS:
                    m = re.search(pat, s, re.IGNORECASE)
                    if m:
                        flags.append({
                            "family": "RISK_MECHANICAL_SYNTHESIS",
                            "paragraph": p_idx,
                            "sentence": s_idx,
                            "description": f"Mechanical synthesis trigger: '{m.group(0)}'",
                            "matched_text": s
                        })

                # 5. Hollow connectives
                for pat in self.HOLLOW_CONNECTIVES:
                    m = re.search(pat, s, re.IGNORECASE)
                    if m:
                        flags.append({
                            "family": "RISK_HOLLOW_CONNECTIVES",
                            "paragraph": p_idx,
                            "sentence": s_idx,
                            "description": f"Polished but hollow connective phrase: '{m.group(0)}'",
                            "matched_text": s
                        })

                # 6. Binary symmetry
                for pat in self.BINARY_SYMMETRY_PATTERNS:
                    m = re.search(pat, s, re.IGNORECASE)
                    if m:
                        flags.append({
                            "family": "RISK_BINARY_SYMMETRY",
                            "paragraph": p_idx,
                            "sentence": s_idx,
                            "description": "Repetitive antithetical sentence symmetry ('While X..., Y...').",
                            "matched_text": s
                        })

                # 7. Triadic lists (three-part enumerations: X, Y, and Z)
                triad_match = re.search(r"\b([a-z\s]+),\s+([a-z\s]+),\s+and\s+([a-z\s]+)\b", s)
                if triad_match and len(s.split()) < 35:
                    flags.append({
                        "family": "RISK_TRIADIC_ENUMERATION",
                        "paragraph": p_idx,
                        "sentence": s_idx,
                        "description": f"Formulaic three-part list: '{triad_match.group(0)}'",
                        "matched_text": s
                    })

                # 8. Colon list construction
                if re.search(r":\s+[a-z0-9]", s):
                    colon_list_count += 1

                # 9. Em-dash scaffolding
                if s.count("—") >= 2 or s.count("--") >= 2:
                    em_dash_count += 1

                # 10. Citation dumping (4+ citations in one parenthetical)
                for dump in re.findall(r"\(([^\)]+)\)", s):
                    citations = [c.strip() for c in dump.split(";") if re.search(r"\d{4}", c)]
                    if len(citations) >= 4:
                        flags.append({
                            "family": "RISK_CITATION_DUMPING",
                            "paragraph": p_idx,
                            "sentence": s_idx,
                            "description": f"Citation dumping detected ({len(citations)} citations in single parenthesis).",
                            "matched_text": dump
                        })

                # 11. Generic buzzwords clustering
                buzz_count = sum(1 for b in self.GENERIC_BUZZWORDS if re.search(b, s, re.IGNORECASE))
                if buzz_count >= 3:
                    flags.append({
                        "family": "RISK_GENERIC_BUZZWORD_CLUSTER",
                        "paragraph": p_idx,
                        "sentence": s_idx,
                        "description": f"Density of generic academic buzzwords is excessive ({buzz_count} in sentence).",
                        "matched_text": s
                    })

        # Global metric checks
        if colon_list_count >= 3:
            flags.append({
                "family": "RISK_COLON_LIST_CONSTRUCTION",
                "description": f"High frequency of colon-scaffolded lists across text ({colon_list_count} occurrences)."
            })

        if em_dash_count >= 3:
            flags.append({
                "family": "RISK_EM_DASH_SCAFFOLDING",
                "description": f"High frequency of paired em-dash scaffolding ({em_dash_count} sentences)."
            })

        # Sentence length uniformity check
        if len(all_sentence_lengths) >= 5:
            mean_len = sum(all_sentence_lengths) / len(all_sentence_lengths)
            variance = sum((l - mean_len) ** 2 for l in all_sentence_lengths) / len(all_sentence_lengths)
            std_dev = variance ** 0.5
            if std_dev < 3.5 and mean_len > 15:
                flags.append({
                    "family": "RISK_UNIFORM_SENTENCE_LENGTH",
                    "description": f"Monotonous sentence length distribution (std_dev = {std_dev:.2f}, mean = {mean_len:.1f} words)."
                })

        return {
            "total_paragraphs": total_paragraphs,
            "total_sentences": len(all_sentence_lengths),
            "flags_detected": len(flags),
            "flags": flags,
            "overall_style_risk_score": "LOW" if len(flags) <= 2 else ("MODERATE" if len(flags) <= 5 else "HIGH")
        }

    def format_markdown_report(self, results: Dict[str, Any]) -> str:
        lines = [
            "# STRUCTURAL STYLE-RISK AUDIT REPORT",
            "",
            f"- **Total Paragraphs Audited:** {results['total_paragraphs']}",
            f"- **Total Sentences Audited:** {results['total_sentences']}",
            f"- **Total Style Risk Flags:** {results['flags_detected']}",
            f"- **Overall Style Risk Level:** `{results['overall_style_risk_score']}`",
            "",
            "---",
            "",
            "## Detected Flags and Editorial Diagnostics",
            ""
        ]

        if not results["flags"]:
            lines.append("No structural style-risk flags detected. Prose exhibits natural cadence and variation.")
        else:
            lines.append("| # | Family | Paragraph | Sentence | Description |")
            lines.append("|---|---|---|---|---|")
            for idx, f in enumerate(results["flags"], 1):
                p = f.get("paragraph", "—")
                s = f.get("sentence", "—")
                lines.append(f"| **{idx}** | `{f['family']}` | {p} | {s} | {f['description']} |")

            lines.append("")
            lines.append("### Flagged Passages Detail")
            lines.append("")
            for idx, f in enumerate(results["flags"], 1):
                if "matched_text" in f:
                    lines.append(f"**Flag {idx} (`{f['family']}`):**")
                    lines.append(f"> \"{f['matched_text']}\"")
                    lines.append("")

        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Audit manuscript prose for structural style risks.")
    parser.add_argument("input_file", help="Path to manuscript markdown or text file.")
    parser.add_argument("--json", action="store_true", help="Output raw JSON format.")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as fp:
        text = fp.read()

    auditor = StyleRiskAuditor()
    results = auditor.audit_text(text)

    if args.json:
        import json
        print(json.dumps(results, indent=2))
    else:
        print(auditor.format_markdown_report(results))


if __name__ == "__main__":
    main()
