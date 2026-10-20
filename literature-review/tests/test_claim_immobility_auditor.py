"""
Unit tests for claim_immobility_auditor.py.
Verifies enforcement of the Claim-Immobility Law across humanized manuscript prose.
"""

import unittest
from pathlib import Path
import sys

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from claim_immobility_auditor import ClaimImmobilityAuditor


class TestClaimImmobilityAuditor(unittest.TestCase):
    def setUp(self):
        self.auditor = ClaimImmobilityAuditor()

    def test_valid_supported_unit_passes(self):
        audit_payload = {
            "unit_id": "UNIT_01",
            "manuscript_ref": "sec02_p01",
            "sentences_audited": [
                {
                    "sentence_index": 1,
                    "sentence_text": "Aggregate capital measurement requires explicit aggregation assumptions.",
                    "classification": "SUPPORTED",
                    "mapped_ledger_slot": "P01.S1",
                    "mapped_argument_assembly_move": "Move 1",
                    "claim_immobility_check": {
                        "causal_direction_unchanged": True,
                        "quantifiers_not_amplified": True,
                        "prohibited_claim_avoided": True,
                        "attribution_unaltered": True,
                        "qualifications_intact": True
                    }
                },
                {
                    "sentence_index": 2,
                    "sentence_text": "This valuation contingency directly shapes observed productivity measures.",
                    "classification": "TRANSITION",
                    "claim_immobility_check": {
                        "causal_direction_unchanged": True,
                        "quantifiers_not_amplified": True,
                        "prohibited_claim_avoided": True,
                        "attribution_unaltered": True,
                        "qualifications_intact": True
                    }
                }
            ],
            "auditor": "TestHarness"
        }
        res = self.auditor.audit_unit(audit_payload)
        self.assertEqual(res["audit_verdict"], "PASS")
        self.assertEqual(res["summary_metrics"]["unsupported_count"], 0)
        self.assertFalse(res["summary_metrics"]["claim_strengthening_detected"])

    def test_unsupported_sentence_fails_audit(self):
        audit_payload = {
            "unit_id": "UNIT_02",
            "manuscript_ref": "sec02_p02",
            "sentences_audited": [
                {
                    "sentence_index": 1,
                    "sentence_text": "The entire national accounts series was fabricated in 1975.",
                    "classification": "UNSUPPORTED",
                    "claim_immobility_check": {
                        "causal_direction_unchanged": True,
                        "quantifiers_not_amplified": True,
                        "prohibited_claim_avoided": True,
                        "attribution_unaltered": True,
                        "qualifications_intact": True
                    }
                }
            ],
            "auditor": "TestHarness"
        }
        res = self.auditor.audit_unit(audit_payload)
        self.assertEqual(res["audit_verdict"], "FAIL")
        self.assertEqual(res["summary_metrics"]["unsupported_count"], 1)

    def test_causal_escalation_detection(self):
        staged = "The evidence suggests that asset composition shifts with relative prices."
        manuscript = "The evidence proves that asset composition shifts with relative prices."
        passed, issues = self.auditor.audit_sentence_pair(staged, manuscript)
        self.assertFalse(passed)
        self.assertTrue(any("Causal escalation" in i for i in issues))

    def test_quantifier_inflation_detection(self):
        staged = "Some capital series can diverge under high replacement costs."
        manuscript = "All capital series will diverge under high replacement costs."
        passed, issues = self.auditor.audit_sentence_pair(staged, manuscript)
        self.assertFalse(passed)
        self.assertTrue(any("Quantifier inflation" in i for i in issues))


if __name__ == "__main__":
    unittest.main()
