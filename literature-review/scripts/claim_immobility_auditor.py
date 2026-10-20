#!/usr/bin/env python3
"""
claim_immobility_auditor.py — Post-Humanization Claim-Immobility Auditor

Enforces the Claim-Immobility Law: stylistic humanization/polishing may vary
syntax, rhythm, and cadence, but may NEVER alter evidentiary bounds or strengthen claims.

Specification: literature-review/references/humanization_and_claim_immobility_protocol.md
Governing Schema: literature-review/schemas/post_humanization_audit_schema.json
"""

import re
import sys
import json
import argparse
from typing import List, Dict, Any, Tuple


class ClaimImmobilityAuditor:
    """Verifies that humanized sentences maintain unbroken provenance and unchanged claims."""

    CAUSAL_ESCALATION_PAIRS = [
        (r"\b(suggests?|indicates?|points?\s+to)\b", r"\b(proves?|demonstrates?|establishes?|determines?)\b"),
        (r"\b(correlated\s+with|associated\s+with)\b", r"\b(causes?|drives?|determines?|produces?)\b"),
        (r"\b(consistent\s+with)\b", r"\b(validates?|proves?|confirms?\s+that)\b")
    ]

    QUANTIFIER_INFLATION_PAIRS = [
        (r"\b(some|certain|specific)\b", r"\b(all|every|universal)\b"),
        (r"\b(often|frequently|sometimes)\b", r"\b(always|invariably|consistently)\b"),
        (r"\b(can|may|could)\b", r"\b(will|must|necessarily)\b")
    ]

    def audit_sentence_pair(
        self,
        staged_text: str,
        manuscript_text: str,
        prohibited_claim: str = ""
    ) -> Tuple[bool, List[str]]:
        """Compares staged sentence against manuscript sentence for unearned strengthening."""
        issues = []

        # 1. Check causal escalation
        for weak_pat, strong_pat in self.CAUSAL_ESCALATION_PAIRS:
            if re.search(weak_pat, staged_text, re.IGNORECASE) and not re.search(strong_pat, staged_text, re.IGNORECASE):
                if re.search(strong_pat, manuscript_text, re.IGNORECASE):
                    issues.append(f"Causal escalation detected: verb strengthened to match '{strong_pat}'")

        # 2. Check quantifier inflation
        for weak_pat, strong_pat in self.QUANTIFIER_INFLATION_PAIRS:
            if re.search(weak_pat, staged_text, re.IGNORECASE) and not re.search(strong_pat, staged_text, re.IGNORECASE):
                if re.search(strong_pat, manuscript_text, re.IGNORECASE):
                    issues.append(f"Quantifier inflation detected: scope broadened to match '{strong_pat}'")

        # 3. Check prohibited stronger claim
        if prohibited_claim and len(prohibited_claim) > 10:
            key_terms = [w.lower() for w in re.findall(r"\b[A-Za-z]{4,}\b", prohibited_claim) if w.lower() not in {"not", "that", "this", "have", "with", "from"}]
            if key_terms:
                matches = sum(1 for w in key_terms if w in manuscript_text.lower())
                if matches >= len(key_terms) * 0.75:
                    issues.append(f"Sentence approaches prohibited claim boundary: '{prohibited_claim[:60]}...'")

        return len(issues) == 0, issues

    def audit_unit(self, audit_data: Dict[str, Any]) -> Dict[str, Any]:
        """Audits a complete post-humanization audit payload against schema rules."""
        sentences = audit_data.get("sentences_audited", [])
        total = len(sentences)
        supported = 0
        transitions = 0
        rhetorical = 0
        unsupported = 0
        strengthening_found = False

        for s in sentences:
            cls = s.get("classification")
            if cls == "SUPPORTED":
                supported += 1
                if not s.get("mapped_ledger_slot"):
                    unsupported += 1
                    s["classification"] = "UNSUPPORTED"
                    s["audit_issue"] = "Marked SUPPORTED but lacks mapped_ledger_slot"
            elif cls == "TRANSITION":
                transitions += 1
            elif cls == "PURE_RHETORICAL_CONNECTIVE":
                rhetorical += 1
            elif cls == "UNSUPPORTED":
                unsupported += 1
            else:
                unsupported += 1
                s["classification"] = "UNSUPPORTED"
                s["audit_issue"] = f"Unknown classification '{cls}'"

            checks = s.get("claim_immobility_check", {})
            if not all(checks.values()):
                strengthening_found = True

        audit_verdict = "PASS" if (unsupported == 0 and not strengthening_found) else "FAIL"

        return {
            "unit_id": audit_data.get("unit_id", "UNKNOWN"),
            "manuscript_ref": audit_data.get("manuscript_ref", "UNKNOWN"),
            "audit_verdict": audit_verdict,
            "sentences_audited": sentences,
            "summary_metrics": {
                "total_sentences": total,
                "supported_count": supported,
                "transition_count": transitions,
                "rhetorical_count": rhetorical,
                "unsupported_count": unsupported,
                "claim_strengthening_detected": strengthening_found
            },
            "auditor": audit_data.get("auditor", "ClaimImmobilityAuditor"),
            "timestamp": audit_data.get("timestamp", "2026-10-20T00:00:00Z")
        }


def main():
    parser = argparse.ArgumentParser(description="Audit manuscript sentences for post-humanization claim immobility.")
    parser.add_argument("audit_json", help="Path to JSON file containing post-humanization audit payload.")
    args = parser.parse_args()

    with open(args.audit_json, "r", encoding="utf-8") as fp:
        data = json.load(fp)

    auditor = ClaimImmobilityAuditor()
    result = auditor.audit_unit(data)

    print(json.dumps(result, indent=2))
    sys.exit(0 if result["audit_verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
