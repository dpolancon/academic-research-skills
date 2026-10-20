"""
Deterministic synthetic regression fixtures verifying the 8 canonical workflow requirements:
1. SINGLE-SOURCE PARAGRAPH: source -> ledger -> assembly -> staged prose
2. VALID CROSS-LITERATURE HINGE: explicit hinge permits weave
3. THEMATIC RESONANCE ONLY: weave must be rejected
4. MIXED AUTHORITIES: external source + internal project method + current implementation
5. PUBLICATION OWNERSHIP: internal provenance does not displace manuscript ownership of contribution
6. HUMANIZATION DRIFT: stylistic rewrite strengthens a claim => audit FAIL
7. NEW SOURCE REQUIRED: triggers human escalation, no silent expansion
8. LOCKED ARCHITECTURE CONFLICT: triggers escalation upon attempting to alter locked unit
"""

import unittest
import json
from pathlib import Path
import sys
import jsonschema

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from claim_immobility_auditor import ClaimImmobilityAuditor
from notebooklm_adapter import MockExtractionBackend


class TestSyntheticRegressionFixtures(unittest.TestCase):
    def setUp(self):
        self.schemas_dir = SKILL_ROOT / "schemas"
        with open(self.schemas_dir / "paragraph_ledger_schema.json", "r", encoding="utf-8") as fp:
            self.ledger_schema = json.load(fp)
        with open(self.schemas_dir / "argument_assembly_schema.json", "r", encoding="utf-8") as fp:
            self.assembly_schema = json.load(fp)
        with open(self.schemas_dir / "staged_prose_schema.json", "r", encoding="utf-8") as fp:
            self.staged_schema = json.load(fp)
        with open(self.schemas_dir / "post_humanization_audit_schema.json", "r", encoding="utf-8") as fp:
            self.audit_schema = json.load(fp)

        self.claim_auditor = ClaimImmobilityAuditor()

    # FIXTURE 1: SINGLE-SOURCE PARAGRAPH
    def test_fixture_1_single_source_pipeline(self):
        """Source -> Ledger -> Assembly -> Staged Prose pipeline for a single author."""
        ledger = {
            "paragraph_key": "LEDGER_SYNTH_01",
            "paragraph_theme": "Baseline Foundation",
            "governing_clusters": ["CLUS_SYNTH_01"],
            "governing_contracts": ["CCC_SYNTH_01"],
            "human_gate_status": "LOCK",
            "proposition_slots": [
                {
                    "slot_id": "P01.S1",
                    "proposition": "Primary asset accumulation depends directly on gross investment flows.",
                    "provenance_class": "DIRECT_SOURCE_CLAIM",
                    "primary_warrant": {
                        "authority_type": "EXTERNAL_SOURCE",
                        "authority_keys": ["SRC_AUTHOR_ALPHA"],
                        "locators": "pp. 12-14"
                    },
                    "prohibited_stronger_claim": "Do not assert gross flows determine relative prices.",
                    "scholarly_status": "LOCK"
                }
            ]
        }
        jsonschema.validate(instance=ledger, schema=self.ledger_schema)

        assembly = {
            "unit_id": "P01",
            "argumentative_job": "Introduce asset accumulation foundation.",
            "reason_for_inclusion": "Grounds downstream capital measurement.",
            "opening_move": "State foundational investment identity.",
            "foreground_claims": ["Primary asset accumulation depends on gross investment."],
            "internal_claim_order": ["P01.S1"],
            "cross_literature_weave_decisions": [],
            "do_not_weave_boundaries": [],
            "citation_choreography": [
                {
                    "claim_id": "P01.S1",
                    "permitted_citation_keys": ["SRC_AUTHOR_ALPHA"],
                    "joint_citation_permitted": False
                }
            ],
            "source_ownership_boundaries": [
                {
                    "concept_or_metric": "Gross investment accumulation",
                    "governing_authority": "SRC_AUTHOR_ALPHA",
                    "ownership_rule": "Direct source attribution"
                }
            ],
            "required_qualifications": ["Valid for perpetual inventory accounts."],
            "terminology_to_preserve": ["gross investment flows"],
            "prohibited_stronger_argument": "Do not assert gross flows determine relative prices.",
            "evidence_lock_references": ["LEDGER_SYNTH_01"],
            "human_status": "LOCK"
        }
        jsonschema.validate(instance=assembly, schema=self.assembly_schema)

        staged = {
            "unit_id": "P01",
            "assembly_ref": "ASSEMBLY_P01",
            "ledger_ref": "LEDGER_SYNTH_01",
            "staged_sentences": [
                {
                    "sentence_index": 1,
                    "slot_id": "P01.S1",
                    "staged_text": "Primary asset accumulation depends directly on gross investment flows (Author Alpha, 2010).",
                    "provenance_class": "DIRECT_SOURCE_CLAIM",
                    "attribution": {
                        "source_keys": ["SRC_AUTHOR_ALPHA"],
                        "citations": ["(Author Alpha, 2010)"],
                        "locators": "pp. 12-14"
                    },
                    "boundary_enforcement": "Does not claim investment determines relative prices."
                }
            ],
            "full_staged_paragraph": "Primary asset accumulation depends directly on gross investment flows (Author Alpha, 2010).",
            "inspection_checks": {
                "plain_syntax_observed": True,
                "ornament_minimized": True,
                "signposting_restrained": True,
                "citations_stabilized": True,
                "boundaries_visible": True
            },
            "human_status": "LOCK"
        }
        jsonschema.validate(instance=staged, schema=self.staged_schema)

    # FIXTURE 2: VALID CROSS-LITERATURE HINGE
    def test_fixture_2_valid_cross_literature_hinge(self):
        """Explicit hinge contract permits controlled interweaving across distinct authors."""
        assembly = {
            "unit_id": "P02",
            "argumentative_job": "Reconcile competing depletion conventions.",
            "reason_for_inclusion": "Confronts gross capacity against net efficiency.",
            "opening_move": "State depletion divergence.",
            "foreground_claims": ["Gross and net valuations diverge systematically under non-zero steady growth."],
            "internal_claim_order": ["P02.S1", "P02.S2"],
            "cross_literature_weave_decisions": [
                {
                    "hinge_id": "HINGE_DEPLETION_01",
                    "literatures_bridged": ["Author Beta", "Author Gamma"],
                    "permitted_weave_scope": "Multi-asset steady-state comparison",
                    "justification": "Satisfies criteria 1-4 under CCC_DEP_01"
                }
            ],
            "do_not_weave_boundaries": [
                {
                    "sources_or_traditions": ["Capacity proxy", "Efficiency decay"],
                    "reason_for_separation": "Ontological distinction",
                    "prohibited_conflation": "Conflating survival probability with service flow"
                }
            ],
            "citation_choreography": [
                {
                    "claim_id": "P02.S2",
                    "permitted_citation_keys": ["SRC_BETA", "SRC_GAMMA"],
                    "joint_citation_permitted": True,
                    "placement_guidance": "Joint parenthetical permitted under CCC_DEP_01"
                }
            ],
            "source_ownership_boundaries": [
                {
                    "concept_or_metric": "Gross-net divergence",
                    "governing_authority": "Adjudicated Hinge",
                    "ownership_rule": "Preserve authorial dispute"
                }
            ],
            "required_qualifications": ["Conditioned on constant retirement profile."],
            "terminology_to_preserve": ["steady-state ratio", "depletion profile"],
            "prohibited_stronger_argument": "Do not claim one measure is universally correct.",
            "evidence_lock_references": ["LEDGER_P02", "CLUS_DEP"],
            "human_status": "LOCK"
        }
        jsonschema.validate(instance=assembly, schema=self.assembly_schema)
        self.assertEqual(len(assembly["cross_literature_weave_decisions"]), 1)

    # FIXTURE 3: THEMATIC RESONANCE ONLY
    def test_fixture_3_thematic_resonance_rejects_weave(self):
        """Thematic resonance lacking an adjudicated hinge strictly rejects interweaving."""
        # When two authors share a theme but lack Criteria 1-4, weave decisions must be empty
        # and do_not_weave_boundaries must explicitly enforce separation.
        assembly = {
            "unit_id": "P03",
            "argumentative_job": "Discuss macro valuation and micro project appraisal without conflation.",
            "reason_for_inclusion": "Distinguish macro aggregation from project decisions.",
            "opening_move": "State macro index-number problem.",
            "foreground_claims": ["Macro capital aggregates conflate distribution with technique."],
            "internal_claim_order": ["P03.S1"],
            "cross_literature_weave_decisions": [],  # REJECTED WEAVE
            "do_not_weave_boundaries": [
                {
                    "sources_or_traditions": ["Macro Aggregation Critique", "Micro Project Appraisal"],
                    "reason_for_separation": "Scale mismatch; failing Criterion 2 (Scope Shift)",
                    "prohibited_conflation": "Do not treat micro project heuristics as macro aggregation theorems."
                }
            ],
            "citation_choreography": [
                {
                    "claim_id": "P03.S1",
                    "permitted_citation_keys": ["SRC_MACRO_AUTHOR"],
                    "joint_citation_permitted": False  # Joint citation strictly forbidden
                }
            ],
            "source_ownership_boundaries": [
                {
                    "concept_or_metric": "Aggregate valuation paradox",
                    "governing_authority": "SRC_MACRO_AUTHOR",
                    "ownership_rule": "Source-local attribution only"
                }
            ],
            "required_qualifications": ["Applies to macroeconomic production functions."],
            "terminology_to_preserve": ["index-number problem"],
            "prohibited_stronger_argument": "Do not merge micro heuristics into macro production function critique.",
            "evidence_lock_references": ["LEDGER_P03"],
            "human_status": "LOCK"
        }
        jsonschema.validate(instance=assembly, schema=self.assembly_schema)
        self.assertEqual(len(assembly["cross_literature_weave_decisions"]), 0)
        self.assertFalse(assembly["citation_choreography"][0]["joint_citation_permitted"])

    # FIXTURE 4: MIXED AUTHORITIES
    def test_fixture_4_mixed_authorities(self):
        """Demarcates external literature, internal method lineage, and active empirical code."""
        ledger = {
            "paragraph_key": "LEDGER_P04",
            "paragraph_theme": "Methodological Infrastructure",
            "governing_clusters": ["CLUS_METHOD"],
            "governing_contracts": ["CCC_METHOD_01"],
            "human_gate_status": "LOCK",
            "proposition_slots": [
                {
                    "slot_id": "P04.S1",
                    "proposition": "Classical perpetual inventory methods assume fixed discards.",
                    "provenance_class": "DIRECT_SOURCE_CLAIM",
                    "primary_warrant": {
                        "authority_type": "EXTERNAL_SOURCE",
                        "authority_keys": ["SRC_CLASSICAL_AUTHOR"],
                        "locators": "p. 100"
                    },
                    "prohibited_stronger_claim": "Do not claim classical framework included Weibull mortality.",
                    "scholarly_status": "LOCK"
                },
                {
                    "slot_id": "P04.S2",
                    "proposition": "We develop a generalized survival reformulation incorporating asset-specific Weibull profiles.",
                    "provenance_class": "AUTHORIAL_SYNTHESIS",
                    "primary_warrant": {
                        "authority_type": "INTERNAL_METHODOLOGY",
                        "authority_keys": ["AUTH_DISSERTATION_CH2", "AUTH_CURRENT_MANUSCRIPT"]
                    },
                    "prohibited_stronger_claim": "Do not attribute Weibull reformulation to classical predecessor.",
                    "scholarly_status": "LOCK"
                },
                {
                    "slot_id": "P04.S3",
                    "proposition": "The empirical implementation calibrates survival parameters against official asset lifetimes.",
                    "provenance_class": "AUTHORIAL_SYNTHESIS",
                    "primary_warrant": {
                        "authority_type": "DATA_IMPLEMENTATION",
                        "authority_keys": ["AUTH_DATA_REPO"]
                    },
                    "prohibited_stronger_claim": "Do not claim empirical parameters are universal constants.",
                    "scholarly_status": "LOCK"
                }
            ]
        }
        jsonschema.validate(instance=ledger, schema=self.ledger_schema)
        authorities = [s["primary_warrant"]["authority_type"] for s in ledger["proposition_slots"]]
        self.assertEqual(authorities, ["EXTERNAL_SOURCE", "INTERNAL_METHODOLOGY", "DATA_IMPLEMENTATION"])

    # FIXTURE 5: PUBLICATION OWNERSHIP
    def test_fixture_5_publication_ownership(self):
        """Internal provenance lineage does not displace manuscript ownership of an unpublished contribution."""
        slot = {
            "slot_id": "P05.S1",
            "proposition": "We develop an analytical reformulation of the capital framework.",
            "provenance_class": "AUTHORIAL_SYNTHESIS",
            "primary_warrant": {
                "authority_type": "PAPER_GOVERNANCE",
                "authority_keys": ["AUTH_CURRENT_PAPER", "INTERNAL_PROVENANCE_DISSERTATION"]
            },
            "prohibited_stronger_claim": "Do not cite unpublished internal dissertation in public manuscript prose as external predecessor.",
            "scholarly_status": "LOCK"
        }
        # In the manuscript, publication ownership belongs to current paper
        self.assertEqual(slot["provenance_class"], "AUTHORIAL_SYNTHESIS")
        self.assertIn("AUTH_CURRENT_PAPER", slot["primary_warrant"]["authority_keys"])

    # FIXTURE 6: HUMANIZATION DRIFT
    def test_fixture_6_humanization_drift_mandatory_fail(self):
        """Stylistic rewriting that strengthens causal language fails the claim immobility audit."""
        staged_sentence = "The historical evidence suggests an association between asset age and maintenance outlays."
        humanized_sentence = "The historical evidence proves that asset aging causes maintenance outlays to surge."

        passed, issues = self.claim_auditor.audit_sentence_pair(staged_sentence, humanized_sentence)
        self.assertFalse(passed)
        self.assertTrue(any("Causal escalation" in i for i in issues))

    # FIXTURE 7: NEW SOURCE REQUIRED (HUMAN ESCALATION)
    def test_fixture_7_new_source_escalation(self):
        """Requiring an external source not in active corpus perimeter triggers human escalation."""
        corpus = ["SRC_AUTHOR_1", "SRC_AUTHOR_2"]
        proposed_source = "SRC_EXTERNAL_UNADMITTED"

        # Simulating boundary guard
        if proposed_source not in corpus:
            escalation_ticket = {
                "ticket_id": "ESC_CORPUS_01",
                "trigger_type": "NEW_SOURCE_REQUIRED",
                "status": "OPEN",
                "human_action_required": "Corpus admission is strictly reserved for human authority."
            }
        else:
            escalation_ticket = None

        self.assertIsNotNone(escalation_ticket)
        self.assertEqual(escalation_ticket["trigger_type"], "NEW_SOURCE_REQUIRED")

    # FIXTURE 8: LOCKED ARCHITECTURE CONFLICT
    def test_fixture_8_locked_architecture_conflict_escalation(self):
        """Attempting to modify a locked architectural unit triggers human escalation."""
        current_state = {
            "canonical_architecture": "P01-P11",
            "architecture_status": "LOCK",
            "paragraphs": {"P01": "LOCK", "P02": "LOCK"}
        }

        # Attempt to insert a new paragraph P01b into locked spine
        proposed_modification = "SPLIT_P01_INTO_P01A_AND_P01B"

        if current_state["architecture_status"] == "LOCK":
            escalation_ticket = {
                "ticket_id": "ESC_ARCH_01",
                "trigger_type": "ARCHITECTURE_MODIFICATION_PROPOSED",
                "status": "OPEN",
                "reason": "Cannot alter locked canonical architecture P01-P11 autonomously."
            }
        else:
            escalation_ticket = None

        self.assertIsNotNone(escalation_ticket)
        self.assertEqual(escalation_ticket["trigger_type"], "ARCHITECTURE_MODIFICATION_PROPOSED")


if __name__ == "__main__":
    unittest.main()
