"""Adversarial tests for the sole candidate-owned definition route."""
import hashlib
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from allowed_value_evidence import validate_allowed_value_evidence  # noqa: E402
from review_evidence import _validate_resolved_mention  # noqa: E402


ROOT = Path(__file__).resolve().parents[6]


def binding(raw, *, atom_id="TEST-R-1", version=1, path="candidate.md"):
    return {"atom_id": atom_id, "version": version, "path": path,
            "sha256": hashlib.sha256(raw.encode()).hexdigest()}


def source(entity, claim, *, atom_id="TEST-R-1", version=1, role="Requirement", structured=False):
    body = ("# Define target\n\n## Scope\n\nTarget.\n\n## Claim\n\n" + claim
            if structured else "# Define target\n\n" + claim)
    return ("---\n"
            f"atom_id: {atom_id}\nversion: {version}\nstatus: Active\ncontent_role: {role}\n"
            "subjects:\n"
            f"  governs: \"{entity}\"\n"
            "---\n" + body + "\n")


def mention(entity, excerpt, *, kind="definition", components=None):
    return {
        "entity": entity, "resolution_basis": "meaning", "rationale": "The direct Claim owns this target.",
        "excerpt": excerpt, "definitions": [],
        "candidate_definition_evidence": {
            "entity": entity, "kind": kind, "excerpt": excerpt,
            "reason": "The candidate's complete primary Claim defines or classifies its exact target.",
            "component_definitions": [] if components is None else components,
        },
    }


def validate_candidate(raw, item, *, atom_id="TEST-R-1", version=1, authorities=None, targets=None):
    _validate_resolved_mention(
        item, authorities or {}, targets or {}, candidate_source=raw,
        candidate_binding=binding(raw, atom_id=atom_id, version=version),
    )


class CandidateDefinitionEvidenceTests(unittest.TestCase):
    def test_real_r1191_defines_its_own_exact_target(self):
        path = ROOT / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1191-CORE_META_MODEL-CORE-REQUIREMENT--define-primary-entity.md"
        raw = path.read_text()
        quote = "a Primary Entity **means** an Entity occurrence whose identity does **not** require another Entity occurrence as its bearer."
        validate_candidate(raw, mention("Primary Entity", quote), atom_id="CA-R-1191", version=13)

    def test_real_d414_positive_classification_defines_its_own_target(self):
        path = ROOT / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-414-CORE_META_MODEL-CORE--classify-carrier-as-a-primary-entity.md"
        raw = path.read_text()
        quote = "the Term Carrier **must** be **NARROWER_THAN** Primary Entity."
        validate_candidate(raw, mention("Carrier", quote, kind="classification"), atom_id="CA-D-414", version=14)

    def test_negative_delivery_constraint_does_not_self_define_d352_target(self):
        path = ROOT / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-352-CORE_META_MODEL-CORE--keep-status-subdirectories-outside-the-directory-carrier-type.md"
        raw = path.read_text()
        quote = "a Status subdirectory used for Artifact Carrier placement **must not** be a Directory Carrier."
        with self.assertRaisesRegex(ValueError, "positive classification"):
            validate_candidate(raw, mention("Artifact/Carrier Placement/Status Subdirectory", quote,
                                            kind="classification"), atom_id="CA-D-352", version=10)

    def test_candidate_exact_anchor_cannot_bypass_explicit_route(self):
        quote = "a Child **means** an independently defined target."
        raw = source("Child", quote)
        item = {"entity": "Child", "resolution_basis": "meaning", "rationale": "probe",
                "definitions": [{"authority": "SELF@1", "excerpt": quote}]}
        with self.assertRaisesRegex(ValueError, "cannot self-admit"):
            _validate_resolved_mention(item, {"SELF@1": raw}, {"SELF@1": "Child"},
                                        candidate_source=raw, candidate_binding=binding(raw))

    def test_candidate_allowed_value_cannot_bypass_owner_route(self):
        quote = "On **and** Off **must** be registered as internal values of `Widget/State`."
        raw = source("Widget/State", quote)
        item = {"entity": "Widget/State: On", "definitions": [{"authority": "SELF@1", "excerpt": quote}],
                "allowed_value_evidence": {"property": "Widget/State", "value": "On",
                                           "authority": "SELF@1", "excerpt": quote}}
        with self.assertRaisesRegex(ValueError, "cannot self-admit"):
            validate_allowed_value_evidence(item, {"SELF@1": raw}, {"SELF@1": "Widget/State"},
                                            candidate_source=raw)

    def test_other_entity_cannot_use_candidate_definition_proof(self):
        quote = "a Child **means** an independently defined target."
        raw = source("Child", quote)
        with self.assertRaisesRegex(ValueError, "exact GOVERNS"):
            validate_candidate(raw, mention("Parent", quote))

    def test_unrelated_definition_and_negative_classification_do_not_admit_target(self):
        raw = source("Target", "an Other **means** an independently defined target.")
        with self.assertRaisesRegex(ValueError, "explicit definition"):
            validate_candidate(raw, mention("Target", "an Other **means** an independently defined target."))

        raw = source("Target", "the Term Target **must not** be **NARROWER_THAN** Parent.")
        with self.assertRaisesRegex(ValueError, "positive classification"):
            validate_candidate(raw, mention("Target", "the Term Target **must not** be **NARROWER_THAN** Parent.",
                                            kind="classification"))

    def test_value_qualified_path_is_not_silently_truncated(self):
        quote = "a Child **means** an independently defined target."
        raw = source("Root/Child: Value", quote)
        with self.assertRaisesRegex(ValueError, "value-qualified"):
            validate_candidate(raw, mention("Root/Child: Value", quote))

    def test_negated_headings_do_not_admit_structured_or_legacy_claims(self):
        quote = "a Child **means** a target that is **not** its parent."
        for structured in (False, True):
            for heading in ("Not yet admitted", "Not a definition", "Without approval"):
                raw = source("Child", quote, structured=structured).replace("# Define target", "# " + heading)
                with self.subTest(structured=structured, heading=heading), self.assertRaises(ValueError):
                    validate_candidate(raw, mention("Child", quote))
        validate_candidate(source("Child", quote, structured=True), mention("Child", quote))

    def test_corrupt_binding_and_inactive_candidate_fail_closed(self):
        quote = "a Child **means** an independently defined target."
        raw = source("Child", quote)
        bad_binding = binding(raw)
        bad_binding["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "contradict binding"):
            _validate_resolved_mention(mention("Child", quote), {}, {}, candidate_source=raw,
                                        candidate_binding=bad_binding)
        with self.assertRaisesRegex(ValueError, "Active RMEDO"):
            validate_candidate(raw.replace("status: Active", "status: Draft"), mention("Child", quote))

    def test_parent_component_needs_independent_definition(self):
        quote = "a Child **means** an independently defined target."
        raw = source("Root/Child", quote)
        item = mention("Root/Child", quote)
        with self.assertRaisesRegex(ValueError, "parent component"):
            validate_candidate(raw, item)

        parent_quote = "a Root **means** the independently defined parent target."
        parent = source("Root", parent_quote, atom_id="TEST-R-2")
        item["candidate_definition_evidence"]["component_definitions"] = [{
            "term": "Root", "authority": "PARENT@1", "excerpt": parent_quote,
        }]
        validate_candidate(raw, item, authorities={"PARENT@1": parent}, targets={"PARENT@1": "Root"})

    def test_title_details_cropped_conditional_and_unrelated_body_fail(self):
        quote = "a Child **means** an independently defined target."
        cases = (
            ("---\natom_id: TEST-R-1\nversion: 1\nstatus: Active\ncontent_role: Requirement\nsubjects:\n  governs: Child\n---\n# " + quote + "\n\nNo body definition.\n", quote),
            (source("Child", quote, structured=True) + "\n## Details\n\na Child **means** another target.\n", "a Child **means** another target."),
            (source("Child", quote + " Extra qualifier."), quote),
            (source("Child", "If approved, " + quote), "If approved, " + quote),
            (source("Child", quote), "an Other **means** an independently defined target."),
        )
        for raw, excerpt in cases:
            with self.subTest(excerpt=excerpt), self.assertRaises(ValueError):
                validate_candidate(raw, mention("Child", excerpt))

    def test_structured_conditional_or_example_heading_cannot_define_target(self):
        quote = "a Child **means** an independently defined target."
        for heading in ("Example definition", "If approved"):
            raw = source("Child", quote, structured=True).replace("# Define target", "# " + heading)
            with self.subTest(heading=heading), self.assertRaisesRegex(ValueError, "unconditional"):
                validate_candidate(raw, mention("Child", quote))


if __name__ == "__main__":
    unittest.main()
