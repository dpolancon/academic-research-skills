"""
Unit tests for style_risk_auditor.py.
Verifies detection of structural style risks, metadiscourse, and workflow vocabulary leakage.
"""

import unittest
from pathlib import Path
import sys

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from style_risk_auditor import StyleRiskAuditor


class TestStyleRiskAuditor(unittest.TestCase):
    def setUp(self):
        self.auditor = StyleRiskAuditor()

    def test_clean_academic_prose_passes_with_zero_flags(self):
        clean_text = (
            "Capital measurement requires explicit aggregation assumptions across distinct durable assets. "
            "Because machine tools and non-residential structures depreciate at divergent physical rates, "
            "reconstructing national fixed wealth depends directly on mortality profiles and relative price indices. "
            "These empirical boundaries shape historical estimates of the output-capital ratio."
        )
        res = self.auditor.audit_text(clean_text)
        self.assertEqual(res["flags_detected"], 0)
        self.assertEqual(res["overall_style_risk_score"], "LOW")

    def test_workflow_vocabulary_leak_detected(self):
        leaked_text = "As shown in the proposition slot S1 and cluster note CLUS_01, the ledger confirms the result."
        res = self.auditor.audit_text(leaked_text)
        families = [f["family"] for f in res["flags"]]
        self.assertIn("RISK_WORKFLOW_VOCABULARY_LEAK", families)

    def test_inflated_novelty_detected(self):
        inflated_text = "This groundbreaking study fills a vital lacuna by establishing an unprecedented breakthrough."
        res = self.auditor.audit_text(inflated_text)
        families = [f["family"] for f in res["flags"]]
        self.assertIn("RISK_INFLATED_NOVELTY", families)

    def test_citation_dumping_detected(self):
        dump_text = "Multiple scholars have explored capital measurement (Smith, 2010; Jones, 2012; Brown, 2015; White, 2020)."
        res = self.auditor.audit_text(dump_text)
        families = [f["family"] for f in res["flags"]]
        self.assertIn("RISK_CITATION_DUMPING", families)

    def test_mechanical_synthesis_detected(self):
        synth_text = "Taken together, these empirical patterns demonstrate that relative valuation shifts matter."
        res = self.auditor.audit_text(synth_text)
        families = [f["family"] for f in res["flags"]]
        self.assertIn("RISK_MECHANICAL_SYNTHESIS", families)


if __name__ == "__main__":
    unittest.main()
