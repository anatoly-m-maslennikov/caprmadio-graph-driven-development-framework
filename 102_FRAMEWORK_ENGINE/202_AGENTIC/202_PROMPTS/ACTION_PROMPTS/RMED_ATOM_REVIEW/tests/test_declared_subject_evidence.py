"""Adversarial admission tests for explicit dependent-Subject evidence."""
import json
import hashlib
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from declared_subject_evidence import validate_declared_subject_evidence  # noqa: E402
from review_evidence import ReviewContext, _validate_resolved_mention  # noqa: E402


def source(entity, excerpt, *, status="Active", role="Requirement", depends_on=None,
           title="Define an Atom Revision"):
    declared = [entity] if depends_on is None else depends_on
    return (
        "---\n"
        f"status: {status}\n"
        f"content_role: {role}\n"
        "subjects:\n"
        '  governs: "Atom/Revision/Property"\n'
        f"  depends_on: {json.dumps(declared)}\n"
        "---\n"
        f"# {title}\n\n"
        f"{excerpt}\n"
    )


def evidence(entity, authority, excerpt):
    return {"entity": entity, "authority": authority, "excerpt": excerpt}


def mention(entity, authority, excerpt, proof=None):
    result = {
        "entity": entity,
        "resolution_basis": "meaning",
        "rationale": "A reviewer must evaluate this eligible source use against the candidate mention.",
        "definitions": [{"authority": authority, "excerpt": excerpt}],
    }
    if proof is not None:
        result["declared_subject_evidence"] = proof
    return result


class DeclaredSubjectEvidenceTests(unittest.TestCase):
    def test_legacy_leading_assertion_is_not_invalidated_by_later_sections(self):
        entity = 'Production Evaluation Checklist'
        excerpt = 'Every Logging Policy must be referenced by its Production Evaluation Checklist.'
        raw = source(entity, excerpt) + '\n## Rationale\n\nSome supporting explanation.\n'
        item = mention(entity, 'R@1', excerpt, evidence(entity, 'R@1', excerpt))
        self.assertTrue(validate_declared_subject_evidence(item, {'R@1': raw}))

    def test_legacy_later_sections_cannot_supply_leading_assertion_proof(self):
        entity = 'Production Evaluation Checklist'
        excerpt = 'Every Logging Policy must be referenced by its Production Evaluation Checklist.'
        for heading in ('Rationale', 'Details', 'Examples', 'Severity policy'):
            raw = source(entity, 'The leading policy remains independently stated.')
            raw += f'\n## {heading}\n\n{excerpt}\n'
            item = mention(entity, 'R@1', excerpt, evidence(entity, 'R@1', excerpt))
            with self.subTest(heading=heading), self.assertRaises(ValueError):
                validate_declared_subject_evidence(item, {'R@1': raw})

    def test_structured_preamble_and_hypothetical_titles_remain_ineligible(self):
        entity = 'Atom/Revision'
        excerpt = 'Every Atom Revision must have one Author.'
        variants = [source(entity, excerpt, title=title) + '\n## Rationale\n\nExplanation.\n'
                    for title in ('Summary', 'Hypothetical policy', 'Proposed definition')]
        variants.append(source(entity, excerpt) + '\n## Scope\n\nRevisions.\n## Claim\n\nOther content.\n')
        for raw in variants:
            item = mention(entity, 'R@1', excerpt, evidence(entity, 'R@1', excerpt))
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                validate_declared_subject_evidence(item, {'R@1': raw})

    def test_historical_r1636_leading_policy_declares_checklist_without_new_definition(self):
        # R-1636 was split and archived. Preserve this grammar regression as
        # explicit fixture text; do not reactivate archived repository bytes.
        excerpt = ('**every** production-relevant component **must** define a Logging Policy '
                   'that supports its Evaluation Controls **and** is referenced by its '
                   'Production Evaluation Checklist. the policy identifies the events **and** '
                   'context required **to** understand normal operation, detect failure, '
                   'correlate distributed work, **and** investigate real production issues.')
        entity = 'Production Evaluation Checklist'
        raw = source(entity, excerpt, title='Require production logging policies')
        raw += '\n## Severity policy\n\nAdditional policy remains outside the leading assertion.\n'
        item = mention(entity, 'CA-R-1636@19', excerpt, evidence(entity, 'CA-R-1636@19', excerpt))
        self.assertTrue(validate_declared_subject_evidence(item, {'CA-R-1636@19': raw}))

    def test_exact_governs_target_is_eligible_without_a_dependency_duplicate(self):
        entity = "Artifact Transition"
        excerpt = "A transition changes the Artifact through its governed operation."
        raw = source(entity, excerpt, depends_on=[]).replace(
            '  governs: "Atom/Revision/Property"', f'  governs: "{entity}"')
        item = mention(entity, "R@1", excerpt, evidence(entity, "R@1", excerpt))
        self.assertTrue(validate_declared_subject_evidence(item, {"R@1": raw}))

    def test_rejects_cropped_direct_bullet_with_indented_or_lazy_continuation(self):
        entity = "Atom/Revision"
        excerpt = "Every Atom Revision must have one Author."
        for continuation in ("  if approved, preserve the predecessor.",
                             "if approved, preserve the predecessor."):
            raw = source(entity, f"- {excerpt}\n{continuation}")
            item = mention(entity, "R@1", excerpt, evidence(entity, "R@1", excerpt))
            with self.subTest(continuation=continuation), self.assertRaisesRegex(ValueError, "complete asserted"):
                validate_declared_subject_evidence(item, {"R@1": raw})

    def test_untrusted_nested_subject_lanes_do_not_create_declarations(self):
        entity = "Atom/Revision"
        excerpt = "Every Atom Revision must have one Author."
        raw = source(entity, excerpt, depends_on={"untrusted": [entity]})
        item = mention(entity, "R@1", excerpt, evidence(entity, "R@1", excerpt))
        for trusted in (frozenset(), frozenset({"R@1"})):
            with self.subTest(trusted=trusted), self.assertRaisesRegex(ValueError, "explicitly declare"):
                validate_declared_subject_evidence(
                    item, {"R@1": raw}, admitted_legacy_principles=trusted)

    def test_real_r1720_and_m113_admit_without_full_path_spelling(self):
        root = Path(__file__).resolve().parents[6]
        sources = (
            ("Work Journal/Event", "CA-R-1720@18",
             root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1720-CORE_META_MODEL-CORE-REQUIREMENT--use-one-project-journal-for-governed-provenance.md",
             "**every** Project **must** use **`=1`** authoritative Work Journal for **all** CAPRMEDIO-governed provenance events, including Artifact changes, Workflow Runs, Step Runs, Action executions, **and** Implementation lifecycle events. **every** admitted event record **must** retain **`=1`** canonical Event identity **and** be recorded **only** once as historical authority; another log **or** view references that record instead of independently recording the same historical fact. distinct events **in** the same execution remain distinct records."),
            ("Author", "CA-M-113@17",
             root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-113-CORE_META_MODEL--write-claims-in-caprmedio-controlled-english.md",
             "**to** write one Claim **in** CAPRMEDIO Controlled English, the Author **must** satisfy **all** of the following:"),
            ("CCE", "CA-M-113@17",
             root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-113-CORE_META_MODEL--write-claims-in-caprmedio-controlled-english.md",
             "use the controlled English subset of the identified CCE version."),
        )
        for entity, authority, path, excerpt in sources:
            with self.subTest(entity=entity):
                item = mention(entity, authority, excerpt, evidence(entity, authority, excerpt))
                self.assertTrue(validate_declared_subject_evidence(item, {authority: path.read_text()}))

    def test_historical_r1312_declared_transition_grammar(self):
        # Current R-1312 no longer declares Artifact Transition. This test
        # checks evidence grammar, not continued admission of that Entity.
        entity = 'Artifact Transition'
        excerpt = ('admission, acceptance, commitment, activation, completion, **and** '
                   'archival transitions **must** remain distinct from the Artifact Revision '
                   'Status value they **may** establish.')
        raw = source(entity, excerpt)
        item = mention(entity, 'FIXTURE-R-1312@1', excerpt,
                       evidence(entity, 'FIXTURE-R-1312@1', excerpt))
        self.assertTrue(validate_declared_subject_evidence(item, {'FIXTURE-R-1312@1': raw}))

    def test_legacy_principle_needs_context_admission_and_candidate_applicability(self):
        raw_principle = (Path(__file__).resolve().parents[6] / ".caprmedio_caprmedio/03_plan/"
                         "CA-P-032-PRINCIPLE-ACTION_POLICY--distinguish-human-operators-from-ai-agents.md").read_text()
        candidate_raw = source("Atom", "Every Atom is reviewed.")
        other_raw = source("Atom", "Every other Atom is reviewed.")
        candidate_binding = {"atom_id": "TEST-R-1", "version": 1,
                             "path": "candidate.md", "sha256": hashlib.sha256(candidate_raw.encode()).hexdigest()}
        other_binding = {"atom_id": "TEST-R-2", "version": 1,
                         "path": "other.md", "sha256": hashlib.sha256(other_raw.encode()).hexdigest()}
        principle_binding = {"atom_id": "CA-P-032", "version": 5,
                             "path": "principle.md", "sha256": hashlib.sha256(raw_principle.encode()).hexdigest()}
        packet = {
            "confidence_threshold": .99,
            "sources": [{"binding": candidate_binding, "text": candidate_raw},
                        {"binding": other_binding, "text": other_raw},
                        {"binding": principle_binding, "text": raw_principle}],
            "authority_bindings": [principle_binding],
            "candidate_bindings": [candidate_binding, other_binding],
            "principle_admissions": [{"binding": principle_binding,
                                        "applicable_to": ["candidate.md"],
                                        "reason": "Fixture reviews this exact Principle.",
                                        "provenance": "Fixture records explicit operator admission."}],
        }
        context = ReviewContext(packet)
        authorities = context.authorities([principle_binding], candidate=candidate_binding)
        excerpt = "**every** Actor that performs **or** authorizes a governed action **must** have **`=1`** Type **in** (Operator, AI Agent)."
        item = mention("AI Agent", "CA-P-032@5", excerpt,
                       evidence("AI Agent", "CA-P-032@5", excerpt))
        with self.assertRaisesRegex(ValueError, "Active RMEDO"):
            validate_declared_subject_evidence(item, authorities)
        trusted = context.admitted_principle_references([principle_binding], candidate=candidate_binding)
        self.assertTrue(validate_declared_subject_evidence(
            item, authorities, admitted_legacy_principles=trusted))
        with self.assertRaisesRegex(ValueError, "applicability"):
            context.admitted_principle_references([principle_binding], candidate=other_binding)

    def test_semantic_rationale_is_required_but_eligibility_is_not_entailment(self):
        entity = "Artifact Transition"
        excerpt = "The Status remains independently governed by its own rule."
        raw = source(entity, excerpt)
        item = mention(entity, "R@1", excerpt, evidence(entity, "R@1", excerpt))
        self.assertTrue(validate_declared_subject_evidence(item, {"R@1": raw}))
        item["rationale"] = ""
        with self.assertRaisesRegex(ValueError, "semantic rationale"):
            validate_declared_subject_evidence(item, {"R@1": raw})

    def test_real_d446_r1078_and_r1412_sources_admit_declared_parents(self):
        root = Path(__file__).resolve().parents[6]
        cases = (
            ("Atom/Identity", "CA-D-446@7", root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-446-CORE_META_MODEL-CORE--give-every-non-draft-atom-revision-one-identifier.md", "**every** non-Draft Atom Revision **must** have **`=1`** Identifier composed from its Atom Identity **and** Version."),
            ("Atom/Revision", "CA-R-1078@15", root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1078-CORE_META_MODEL-CORE-REQUIREMENT--give-every-atom-revision-one-author.md", "**every** Atom Revision **must** have **`=1`** Author."),
            ("Atom/Revision", "CA-R-1412@9", root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1412-CORE_META_MODEL-CORE--give-every-atom-revision-one-status.md", "**every** Atom Revision **must** have **`=1`** Status."),
        )
        for entity, authority, path, excerpt in cases:
            with self.subTest(authority=authority):
                item = mention(entity, authority, excerpt, evidence(entity, authority, excerpt))
                self.assertTrue(validate_declared_subject_evidence(item, {authority: path.read_text()}))

    def test_rejects_wrong_target_unbound_reference_and_mismatched_body(self):
        entity = "Atom/Revision"
        excerpt = "Every Atom Revision must have one Author."
        raw = source(entity, excerpt)
        cases = (
            (mention(entity, "R@1", excerpt, evidence("Atom/Identity", "R@1", excerpt)), {"R@1": raw}),
            (mention(entity, "R@1", excerpt, evidence(entity, "R@1", excerpt)),
             {"R@1": source(entity, excerpt, depends_on=["Atom/Revision/Author"])}),
            (mention(entity, "R@1", excerpt, evidence(entity, "OTHER@1", excerpt)), {"R@1": raw}),
            (mention(entity, "R@1", excerpt, evidence(entity, "R@1", "Every Revision must have one Author.")), {"R@1": source(entity, "Every Revision must have one Author.")}),
        )
        for item, authorities in cases:
            with self.subTest(item=item), self.assertRaises(ValueError):
                validate_declared_subject_evidence(item, authorities)

    def test_rejects_inactive_plan_concern_title_metadata_and_conditional_sources(self):
        entity = "Atom/Revision"
        excerpt = "Every Atom Revision must have one Author."
        metadata_only = source(entity, "Body does not identify the bearer.").replace(
            "content_role: Requirement\n", "content_role: Requirement\n"
            "note: Every Atom Revision must have one Author.\n")
        cases = (
            source(entity, excerpt, status="Draft"),
            source(entity, excerpt, role="Plan"),
            source(entity, excerpt, role="Concern"),
            source(entity, "Body does not identify the bearer.", title="Every Atom Revision must have one Author."),
            metadata_only,
            source(entity, "If approved, every Atom Revision must have one Author."),
            source(entity, "Example: every Atom Revision must have one Author."),
            source(entity, "Proposed: every Atom Revision must have one Author."),
        )
        for raw in cases:
            proof_excerpt = next((line.strip() for line in raw.splitlines()
                                  if "Atom Revision" in line and not line.startswith("#")), excerpt)
            item = mention(entity, "R@1", proof_excerpt, evidence(entity, "R@1", proof_excerpt))
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                validate_declared_subject_evidence(item, {"R@1": raw})

    def test_candidate_self_admission_is_rejected(self):
        entity = "Atom/Revision"
        excerpt = "Every Atom Revision must have one Author."
        raw = source(entity, excerpt)
        item = mention(entity, "R@1", excerpt, evidence(entity, "R@1", excerpt))
        with self.assertRaisesRegex(ValueError, "self-admit"):
            validate_declared_subject_evidence(item, {"R@1": raw}, candidate_source=raw)

    def test_declared_dependency_proof_does_not_promote_literal_identity_admission(self):
        entity = "Atom/Revision"
        excerpt = "Every Atom Revision must have one Author."
        raw = source(entity, excerpt)
        item = mention(entity, "R@1", excerpt, evidence(entity, "R@1", excerpt))
        item["resolution_basis"] = "identity"
        with self.assertRaisesRegex(ValueError, "not identity admission"):
            validate_declared_subject_evidence(item, {"R@1": raw})

    def test_rejects_cropped_conditional_quote_and_heading_scoped_examples(self):
        entity = "Atom/Revision"
        asserted = "Every Atom Revision must have one Author."
        cropped = source(entity, "If approval is granted, " + asserted)
        cropped_item = mention(entity, "R@1", asserted, evidence(entity, "R@1", asserted))
        with self.assertRaisesRegex(ValueError, "complete asserted Claim paragraph"):
            validate_declared_subject_evidence(cropped_item, {"R@1": cropped})

        for body in (
            "# Define an Atom Revision\n\n## Claim\n\n### Hypothetical example\n\n" + asserted,
            "# Define an Atom Revision\n\n## Details\n\n" + asserted,
        ):
            raw = (
                "---\nstatus: Active\ncontent_role: Requirement\nsubjects:\n"
                '  governs: "Atom/Revision/Author"\n'
                '  depends_on: ["Atom/Revision"]\n---\n' + body + "\n"
            )
            item = mention(entity, "R@1", asserted, evidence(entity, "R@1", asserted))
            with self.subTest(body=body), self.assertRaisesRegex(ValueError, "Claim context"):
                validate_declared_subject_evidence(item, {"R@1": raw})

    def test_invalid_proof_is_rejected_even_with_an_exact_governing_anchor(self):
        entity = "Atom/Revision"
        anchor_excerpt = "Atom Revision is the exact governed Entity."
        invalid_excerpt = "Every Atom Revision must have one Author."
        anchor = source(entity, anchor_excerpt)
        dependent = source(entity, invalid_excerpt)
        item = mention(entity, "ANCHOR@1", anchor_excerpt,
                       evidence(entity, "MISSING@1", invalid_excerpt))
        with self.assertRaises(ValueError):
            _validate_resolved_mention(item, {"ANCHOR@1": anchor, "DEPENDENT@1": dependent},
                                        {"ANCHOR@1": entity, "DEPENDENT@1": "Atom/Revision/Author"})


if __name__ == "__main__":
    unittest.main()
