"""
Read-Only Compatibility Test Suite against paper-k-stock.

Verifies that the generalized literature-review schemas and control-bundle
validator can represent the parked paper-k-stock production state without
modifying any files in paper-k-stock and without embedding project-specific
logic into the generic ARS skill.
"""

import unittest
import json
import yaml
from pathlib import Path
import sys
import jsonschema

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from control_bundle_validator import ControlBundleValidator

PAPER_K_STOCK_ROOT = Path(r"C:\ReposGitHub\paper-k-stock")
VAULT_LIT_DIR = PAPER_K_STOCK_ROOT / "paper-k-stock_vault" / "10_Theory_and_Literature" / "literature_review"


class TestPaperKStockCompatibility(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schemas_dir = SKILL_ROOT / "schemas"
        with open(cls.schemas_dir / "paragraph_ledger_schema.json", "r", encoding="utf-8") as fp:
            cls.ledger_schema = json.load(fp)
        with open(cls.schemas_dir / "argument_assembly_schema.json", "r", encoding="utf-8") as fp:
            cls.assembly_schema = json.load(fp)
        with open(cls.schemas_dir / "staged_prose_schema.json", "r", encoding="utf-8") as fp:
            cls.staged_schema = json.load(fp)

    def test_paper_k_stock_control_bundle_passes_generic_validation(self):
        """Read-only check: paper-k-stock 00_control_bundle validates under ControlBundleValidator."""
        bundle_dir = VAULT_LIT_DIR / "00_control_bundle"
        if not bundle_dir.exists():
            self.skipTest("paper-k-stock control bundle not found on disk.")

        validator = ControlBundleValidator(bundle_dir, self.schemas_dir)
        passed, errors = validator.validate_all()
        self.assertTrue(passed, f"paper-k-stock control bundle failed generic validation: {errors}")

    def test_representability_of_paper_k_stock_simple_source_case(self):
        """Validates that a representative P01/P02 single-source proposition conforms to generic schema."""
        source_ledger_case = {
            "paragraph_key": "LEDGER_P02_REPRESENTATION",
            "paragraph_theme": "Heterogeneous Capital Valuation",
            "governing_clusters": ["CLUS_HETEROGENEOUS_CAPITAL_VALUATION_TECHNIQUE"],
            "governing_contracts": ["CCC_HET_01", "CCC_HET_02"],
            "human_gate_status": "LOCK",
            "proposition_slots": [
                {
                    "slot_id": "P02.S2",
                    "proposition": "Valuing heterogeneous capital requires presupposing the rate of profit or discount rate that aggregate theory seeks to explain.",
                    "provenance_class": "DIRECT_SOURCE_CLAIM",
                    "primary_warrant": {
                        "authority_type": "EXTERNAL_SOURCE",
                        "authority_keys": ["SRC_ROBINSON1953"],
                        "locators": "pp. 81-82, 89 note 2"
                    },
                    "prohibited_stronger_claim": "Do not expand into broad Cambridge controversy survey; keep terminology local.",
                    "scholarly_status": "LOCK"
                }
            ]
        }
        jsonschema.validate(instance=source_ledger_case, schema=self.ledger_schema)

    def test_representability_of_cross_literature_hinge_case(self):
        """Validates that a representative P03 Shaikh vs Zarembka hinge conforms to generic assembly schema."""
        hinge_assembly_case = {
            "unit_id": "P03",
            "argumentative_job": "Establish capital productivity as an accounting ratio conditional on denominator depletion conventions.",
            "reason_for_inclusion": "Confront gross capacity against net efficiency depletion.",
            "incoming_dependency": ["P02 (Capital Heterogeneity Valuation)"],
            "opening_move": "State that output-capital ratios are derived accounting aggregates.",
            "foreground_claims": [
                "Shaikh treats gross stock as a broad capacity indicator.",
                "Zarembka proves multi-asset steady-state Gross-to-Net stock ratio invariance."
            ],
            "internal_claim_order": ["P03.S1", "P03.S2", "P03.S3"],
            "cross_literature_weave_decisions": [
                {
                    "hinge_id": "CCC_PROD_02",
                    "literatures_bridged": ["Classical Competition (Shaikh)", "Steady-State Mathematical Aggregation (Zarembka)"],
                    "permitted_weave_scope": "Gross vs net stock divergence in capital productivity denominators",
                    "justification": "Satisfies Criteria 1-4 under ratified CCC_PROD_02 contract."
                }
            ],
            "do_not_weave_boundaries": [
                {
                    "sources_or_traditions": ["Shaikh Gross Capacity", "Zarembka Net Maintenance"],
                    "reason_for_separation": "Ontological divergence between survival tracking and efficiency decay",
                    "prohibited_conflation": "Do not treat steady-state invariance as holding across different growth regimes."
                }
            ],
            "citation_choreography": [
                {
                    "claim_id": "P03.S3",
                    "permitted_citation_keys": ["SRC_SHAIKH2016", "SRC_ZAREMBKA2019"],
                    "joint_citation_permitted": True,
                    "placement_guidance": "Joint parenthetical citation permitted under CCC_PROD_02."
                }
            ],
            "source_ownership_boundaries": [
                {
                    "concept_or_metric": "Gross-to-Net steady state invariance",
                    "governing_authority": "SRC_ZAREMBKA2019",
                    "ownership_rule": "Theorem owned by Zarembka; time-invariant within steady state."
                }
            ],
            "required_qualifications": [
                "Invariance holds time-invariantly within a given steady state / growth regime, NOT across different regimes.",
                "Aging maintenance hypothesis is suggestive, not proven."
            ],
            "terminology_to_preserve": ["u_K", "Y*/K", "Gross-to-Net ratio"],
            "prohibited_stronger_argument": "Do not claim net stock artificially depresses capital value categorically.",
            "evidence_lock_references": ["LEDGER_P03", "CCC_PROD_02"],
            "human_status": "LOCK"
        }
        jsonschema.validate(instance=hinge_assembly_case, schema=self.assembly_schema)

    def test_representability_of_mixed_authority_and_publication_ownership(self):
        """Validates that P10 method reformulation conforms to publication ownership rules."""
        p10_ledger_case = {
            "paragraph_key": "LEDGER_P10_REPRESENTATION",
            "paragraph_theme": "Methodological Reformulation and Dataset Contribution",
            "governing_clusters": ["CLUS_P10_DATASET_CONTRIBUTION"],
            "governing_contracts": ["CCC_DATA_01"],
            "human_gate_status": "LOCK",
            "proposition_slots": [
                {
                    "slot_id": "P10.S3",
                    "proposition": "We develop a reformulation of Shaikh's GPIM framework combining asset-specific Weibull survival profiles with historical calibration.",
                    "provenance_class": "AUTHORIAL_SYNTHESIS",
                    "primary_warrant": {
                        "authority_type": "INTERNAL_METHODOLOGY",
                        "authority_keys": ["AUTH_DISSERTATION_CH2", "AUTH_CURRENT_MANUSCRIPT"],
                        "locators": "Dissertation Ch. 2; Manuscript Section 2"
                    },
                    "prohibited_stronger_claim": "Do not cite dissertation in manuscript prose; ownership belongs to current paper.",
                    "scholarly_status": "LOCK"
                }
            ]
        }
        jsonschema.validate(instance=p10_ledger_case, schema=self.ledger_schema)
        slot = p10_ledger_case["proposition_slots"][0]
        self.assertEqual(slot["provenance_class"], "AUTHORIAL_SYNTHESIS")
        self.assertEqual(slot["primary_warrant"]["authority_type"], "INTERNAL_METHODOLOGY")


if __name__ == "__main__":
    unittest.main()
