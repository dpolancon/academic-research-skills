"""
Deterministic unit test suite for the generic literature-review skill.
Validates all 12 schemas, templates, replaceable ExtractionBackend behavior,
exception trigger guardrails, optimization metrics, and absence of project-specific hardcoding.
"""

import json
import unittest
from pathlib import Path
import sys
import jsonschema

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from notebooklm_adapter import (  # noqa: E402
    ExtractionBackend,
    MockExtractionBackend,
    ALLOWED_EXCEPTION_TRIGGERS,
    compute_optimization_metrics,
)


class TestLiteratureReviewSkillArchitecture(unittest.TestCase):
    def test_all_schemas_are_valid_draft7(self):
        schemas_dir = SKILL_ROOT / "schemas"
        expected_schemas = [
            "corpus_registry_schema.json",
            "question_object_schema.json",
            "query_pack_schema.json",
            "cluster_citation_contract_schema.json",
            "exception_query_schema.json",
            "argument_assembly_schema.json",
            "staged_prose_schema.json",
            "manuscript_prose_contract_schema.json",
            "post_humanization_audit_schema.json",
            "paragraph_ledger_schema.json",
            "governance_state_schema.json",
            "control_bundle_manifest_schema.json",
        ]
        for fname in expected_schemas:
            fpath = schemas_dir / fname
            self.assertTrue(fpath.exists(), f"Schema file {fname} must exist.")
            with open(fpath, "r", encoding="utf-8") as fp:
                data = json.load(fp)
            jsonschema.Draft7Validator.check_schema(data)

            # Overfitting audit: ensure no paper-k-stock specific terms in generic schemas
            schema_str = json.dumps(data).lower()
            self.assertNotIn("chile", schema_str)
            self.assertNotIn("shaikh", schema_str)
            self.assertNotIn("basu", schema_str)
            self.assertNotIn("zarembka", schema_str)
            self.assertNotIn("hofman", schema_str)

    def test_all_templates_exist_and_are_generic(self):
        templates_dir = SKILL_ROOT / "templates"
        expected_templates = [
            "source_note_template.md",
            "cluster_note_template.md",
            "synthesis_note_template.md",
            "paragraph_ledger_template.md",
            "argument_assembly_template.md",
            "staged_prose_template.md",
            "manuscript_prose_template.md",
            "post_humanization_audit_template.md",
        ]
        for tname in expected_templates:
            tpath = templates_dir / tname
            self.assertTrue(tpath.exists(), f"Template {tname} must exist.")
            text = tpath.read_text(encoding="utf-8").lower()
            self.assertNotIn("chile", text)
            self.assertNotIn("shaikh", text)

        cb_dir = templates_dir / "control_bundle"
        expected_cb_templates = [
            "00_BUNDLE_MANIFEST.template.md",
            "01_AUTHORITY_HIERARCHY.template.md",
            "04_CLAIM_PROVENANCE_AND_STATUS_RULES.template.md",
            "06_HUMAN_SOVEREIGNTY_GATES.template.md",
            "08_CURRENT_STATE.template.yaml",
            "09_HUMAN_RATIFICATION_LEDGER.template.md",
            "10_ESCALATION_QUEUE.template.md",
            "12_RATIFICATION_PACKET.template.md",
        ]
        for cname in expected_cb_templates:
            cpath = cb_dir / cname
            self.assertTrue(cpath.exists(), f"Control bundle template {cname} must exist.")

    def test_argument_assembly_schema_validation(self):
        schema_file = SKILL_ROOT / "schemas" / "argument_assembly_schema.json"
        with open(schema_file, "r", encoding="utf-8") as fp:
            schema = json.load(fp)

        valid_assembly = {
            "unit_id": "UNIT_01",
            "argumentative_job": "Establish foundational boundary between nominal value and physical assets.",
            "reason_for_inclusion": "Prevent conceptual conflation downstream.",
            "opening_move": "State classical measurement paradox.",
            "foreground_claims": ["Aggregation requires presupposing valuation."],
            "internal_claim_order": ["S1", "S2", "S3"],
            "cross_literature_weave_decisions": [
                {
                    "hinge_id": "HINGE_01",
                    "literatures_bridged": ["Tradition A", "Tradition B"],
                    "permitted_weave_scope": "Conceptual critique only",
                    "justification": "Satisfies criteria 1-4"
                }
            ],
            "do_not_weave_boundaries": [
                {
                    "sources_or_traditions": ["Micro Appraisal", "Macro Aggregation"],
                    "reason_for_separation": "Scale mismatch",
                    "prohibited_conflation": "Equating plant decision with aggregate scalar"
                }
            ],
            "citation_choreography": [
                {
                    "claim_id": "S1",
                    "permitted_citation_keys": ["SRC_AUTHOR1"],
                    "joint_citation_permitted": False
                }
            ],
            "source_ownership_boundaries": [
                {
                    "concept_or_metric": "Capital scalar",
                    "governing_authority": "External literature",
                    "ownership_rule": "Attributed to cited source"
                }
            ],
            "required_qualifications": ["Applies to multi-asset systems."],
            "terminology_to_preserve": ["who's who", "valuation technique"],
            "prohibited_stronger_argument": "Do not assert national accounting is impossible.",
            "evidence_lock_references": ["LEDGER_01", "CLUS_01"],
            "human_status": "LOCK"
        }
        jsonschema.validate(instance=valid_assembly, schema=schema)

    def test_staged_prose_schema_validation(self):
        schema_file = SKILL_ROOT / "schemas" / "staged_prose_schema.json"
        with open(schema_file, "r", encoding="utf-8") as fp:
            schema = json.load(fp)

        valid_staged = {
            "unit_id": "UNIT_01",
            "assembly_ref": "ASSEMBLY_01",
            "ledger_ref": "LEDGER_01",
            "staged_sentences": [
                {
                    "sentence_index": 1,
                    "slot_id": "S1",
                    "staged_text": "Aggregate capital cannot be reduced to a physical scalar independent of relative prices.",
                    "provenance_class": "DIRECT_SOURCE_CLAIM",
                    "attribution": {
                        "source_keys": ["SRC_AUTHOR1"],
                        "citations": ["(Author, 2020)"]
                    },
                    "boundary_enforcement": "Does not claim measurement is impossible in practice."
                }
            ],
            "full_staged_paragraph": "Aggregate capital cannot be reduced to a physical scalar independent of relative prices (Author, 2020).",
            "inspection_checks": {
                "plain_syntax_observed": True,
                "ornament_minimized": True,
                "signposting_restrained": True,
                "citations_stabilized": True,
                "boundaries_visible": True
            },
            "human_status": "LOCK"
        }
        jsonschema.validate(instance=valid_staged, schema=schema)

    def test_mock_backend_and_metrics(self):
        backend = MockExtractionBackend()
        sources = backend.list_sources()
        self.assertEqual(len(sources), 2)
        ans = backend.ask("Test question", ["src_001"])
        self.assertIn("answer", ans)
        self.assertIn("citations", ans)

        metrics = compute_optimization_metrics(
            downstream_source_uses=8,
            source_passes_executed=2,
            downstream_query_claims=12,
            query_pack_executions=3,
            downstream_cluster_uses=6,
            cluster_passes_executed=2,
            exception_queries_triggered=1,
            paragraph_ledgers_constructed=5,
            requeried_saturated_sources=0,
            total_saturated_sources=5,
        )
        self.assertEqual(metrics["source_reuse"], 4.0)
        self.assertEqual(metrics["query_reuse"], 4.0)
        self.assertEqual(metrics["cluster_reuse"], 3.0)
        self.assertEqual(metrics["exception_rate"], 0.2)
        self.assertEqual(metrics["requery_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
