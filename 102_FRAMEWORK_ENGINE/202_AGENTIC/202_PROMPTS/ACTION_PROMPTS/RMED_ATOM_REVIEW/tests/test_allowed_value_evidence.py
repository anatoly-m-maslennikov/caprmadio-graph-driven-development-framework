"""Bounded admission for registered allowed-value Subject paths."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from allowed_value_evidence import validate_allowed_value_evidence  # noqa: E402


PROPERTY = "Atom/Content Role: Evaluation/Type"
VALUE = "Evaluation Control"
ENTITY = f"{PROPERTY}: {VALUE}"
AUTHORITY = "MOCK-R-1662@1"
EXCERPT = (
    "QA Case **and** Evaluation Control **must** be registered as internal values "
    "of `Atom/Content Role: Evaluation/Type`."
)
ACTIVITY_PROPERTY = "Artifact/Activity"
ACTIVITY_EXCERPT = (
    "an Artifact **must** have **`=1`** Activity **in** (Active, Inactive) **if** "
    "an explicitly defined Status model applies **to** it, **and** **`=0`** Activity "
    "**otherwise**."
)
EXECUTION_PROPERTY = "Action/Execution Kind"
EXECUTION_VALUE = "Agentic"
EXECUTION_EXCERPT = (
    "- Agentic: an AI Agent interprets the supplied context **and** instructions **to** "
    "perform the Action. the AI Agent **may** call Tools within its admitted authority."
)
OWNERSHIP_PROPERTY = "Carrier/Ownership Class"
OWNERSHIP_VALUES = ("Framework-Owned", "Project-Owned", "Runtime State")
OWNERSHIP_EXCERPT = (
    '**every** internal CAPRMEDIO Carrier **must** have **`=1`** Ownership Class '
    '**in** (Framework-Owned, Project-Owned, Runtime State).'
)
OWNERSHIP_AUTHORITY = "CA-D-316@11"


def source(body=EXCERPT, *, status="Active", governs=PROPERTY, role="Requirement"):
    return (
        "---\n"
        f"status: {status}\n"
        f"content_role: {role}\n"
        "subjects:\n"
        f"  governs: {json.dumps(governs)}\n"
        "---\n"
        "# Register Type Values\n\n"
        f"{body}\n"
    )


def mention(*, entity=ENTITY, definitions=None, evidence=None):
    result = {
        "entity": entity,
        "definitions": definitions if definitions is not None else [{
            "authority": AUTHORITY,
            "excerpt": EXCERPT,
        }],
    }
    if evidence is not None:
        result["allowed_value_evidence"] = evidence
    return result


def proof(**changes):
    result = {
        "property": PROPERTY,
        "value": VALUE,
        "authority": AUTHORITY,
        "excerpt": EXCERPT,
    }
    result.update(changes)
    return result


def activity_source(body=ACTIVITY_EXCERPT, *, governs=ACTIVITY_PROPERTY,
                    heading="Define Artifact Activity"):
    return (
        "---\n"
        "status: Active\n"
        "content_role: Requirement\n"
        "subjects:\n"
        f"  governs: {json.dumps(governs)}\n"
        "---\n"
        f"# {heading}\n\n"
        f"{body}\n"
    )


def activity_proof(value="Active", **changes):
    result = {
        "property": ACTIVITY_PROPERTY,
        "value": value,
        "authority": "MOCK-R-1307@1",
        "excerpt": ACTIVITY_EXCERPT,
    }
    result.update(changes)
    return result


def activity_mention(value="Active", *, definitions=None, evidence=None):
    return {
        "entity": f"{ACTIVITY_PROPERTY}: {value}",
        "definitions": definitions if definitions is not None else [{
            "authority": "MOCK-R-1307@1",
            "excerpt": ACTIVITY_EXCERPT,
        }],
        "allowed_value_evidence": activity_proof(value) if evidence is None else evidence,
    }


def execution_source(body, *, governs=EXECUTION_PROPERTY, title="Define Action Execution Kind"):
    return source(body, governs=governs).replace("# Register Type Values", "# " + title)


def execution_mention(*, property_path=EXECUTION_PROPERTY, value=EXECUTION_VALUE,
                      authority="MOCK-R-1526@1", excerpt=EXECUTION_EXCERPT):
    return {
        "entity": f"{property_path}: {value}",
        "definitions": [{"authority": authority, "excerpt": excerpt}],
        "allowed_value_evidence": {
            "property": property_path,
            "value": value,
            "authority": authority,
            "excerpt": excerpt,
        },
    }


def ownership_mention(value, *, entity=None, property_path=OWNERSHIP_PROPERTY,
                      authority=OWNERSHIP_AUTHORITY, excerpt=OWNERSHIP_EXCERPT):
    return {
        "entity": entity if entity is not None else f"{property_path}: {value}",
        "definitions": [{"authority": authority, "excerpt": excerpt}],
        "allowed_value_evidence": {
            "property": property_path,
            "value": value,
            "authority": authority,
            "excerpt": excerpt,
        },
    }


class AllowedValueEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.authorities = {AUTHORITY: source()}
        self.targets = {AUTHORITY: PROPERTY}

    def test_absent_proof_is_not_an_error_or_admission(self):
        self.assertFalse(validate_allowed_value_evidence(
            mention(evidence=None), self.authorities, self.targets))

    def test_real_r1662_value_registration_is_admitted(self):
        root = Path(__file__).resolve().parents[6]
        path = root / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/"
            "CA-R-1662-PROJECT_CONFIGURATION-REQUIREMENT--register-type-values-for-evaluation-atoms.md"
        )
        raw = path.read_text()
        authority = "CA-R-1662@26"
        actual = {
            "property": PROPERTY,
            "value": VALUE,
            "authority": authority,
            "excerpt": EXCERPT,
        }
        item = mention(definitions=[{"authority": authority, "excerpt": EXCERPT}], evidence=actual)
        self.assertTrue(validate_allowed_value_evidence(
            item, {authority: raw}, {authority: PROPERTY}))

    def test_second_registered_value_is_admitted_at_its_exact_path(self):
        value = "QA Case"
        item = mention(
            entity=f"{PROPERTY}: {value}",
            evidence=proof(value=value),
        )
        self.assertTrue(validate_allowed_value_evidence(item, self.authorities, self.targets))

    def test_structured_source_accepts_only_claim_prose(self):
        structured = source(
            "## Summary\nIgnore this.\n\n## Scope\nIgnore this too.\n\n## Claim\n\n"
            + EXCERPT + "\n\n## Details\nIgnore this as well."
        )
        self.assertTrue(validate_allowed_value_evidence(
            mention(evidence=proof()), {AUTHORITY: structured}, self.targets))

    def test_rejects_subordinate_heading_context_in_claim_or_legacy_body(self):
        bodies = (
            "## Claim\n\n### If approved\n\n" + EXCERPT,
            "### If approved\n\n" + EXCERPT,
        )
        for body in bodies:
            with self.subTest(body=body), self.assertRaises(ValueError):
                validate_allowed_value_evidence(
                    mention(evidence=proof()), {AUTHORITY: source(body)}, self.targets
                )

    def test_present_proof_requires_exact_bound_definition_citation(self):
        for definitions in ([], [{"authority": AUTHORITY, "excerpt": EXCERPT + " "}],
                            [{"authority": "OTHER@1", "excerpt": EXCERPT}]):
            with self.subTest(definitions=definitions):
                with self.assertRaises(ValueError):
                    validate_allowed_value_evidence(
                        mention(definitions=definitions, evidence=proof()), self.authorities, self.targets)

    def test_rejects_non_rmedo_or_non_active_authority(self):
        cases = (
            (source(status="Draft"), self.targets),
            (source(role="Plan"), self.targets),
            (source(role="[]"), self.targets),
            (source(governs="Atom/Content Role: Requirement/Type"), self.targets),
            (source(), {AUTHORITY: "Atom/Content Role: Requirement/Type"}),
        )
        for raw, targets in cases:
            with self.subTest(raw=raw, targets=targets), self.assertRaises(ValueError):
                validate_allowed_value_evidence(mention(evidence=proof()), {AUTHORITY: raw}, targets)

    def test_rejects_wrong_entity_property_value_or_unbound_authority(self):
        cases = (
            (mention(entity=VALUE, evidence=proof()), self.authorities, self.targets),
            (mention(entity=ENTITY + " Extended", evidence=proof()), self.authorities, self.targets),
            (mention(evidence=proof(property="Atom/Content Role: Requirement/Type")), self.authorities, self.targets),
            (mention(evidence=proof(value="QA Case")), self.authorities, self.targets),
            (mention(entity=f"{PROPERTY}: Unlisted", evidence=proof(value="Unlisted")),
             self.authorities, self.targets),
            (mention(evidence=proof(authority="OTHER@1")), self.authorities, self.targets),
            (mention(evidence={"property": PROPERTY}), self.authorities, self.targets),
        )
        for item, authorities, targets in cases:
            with self.subTest(item=item), self.assertRaises(ValueError):
                validate_allowed_value_evidence(item, authorities, targets)

    def test_rejects_none_and_extra_proof_fields(self):
        for evidence in (None, {**proof(), "extra": "forged"},
                         {**proof(), "value": None}):
            with self.subTest(evidence=evidence), self.assertRaises(ValueError):
                item = mention()
                item["allowed_value_evidence"] = evidence
                validate_allowed_value_evidence(
                    item, self.authorities, self.targets)

    def test_rejects_conditional_negated_or_non_sentence_grammar(self):
        bodies = (
            "**if** QA Case **and** Evaluation Control **must** be registered as internal values "
            "of `Atom/Content Role: Evaluation/Type`.",
            "QA Case **and** Evaluation Control **must not** be registered as internal values "
            "of `Atom/Content Role: Evaluation/Type`.",
            "Other text " + EXCERPT,
        )
        for body in bodies:
            with self.subTest(body=body), self.assertRaises(ValueError):
                validate_allowed_value_evidence(
                    mention(evidence=proof()), {AUTHORITY: source(body)}, self.targets)

    def test_rejects_bound_conditional_or_proposed_value_prefixes(self):
        for prefix in ("if", "If", "Proposed", "proposed", "Draft", "Example", "Unless"):
            body = f"{prefix} {EXCERPT}"
            item = mention(
                definitions=[{"authority": AUTHORITY, "excerpt": body}],
                evidence=proof(excerpt=body),
            )
            with self.subTest(prefix=prefix), self.assertRaises(ValueError):
                validate_allowed_value_evidence(item, {AUTHORITY: source(body)}, self.targets)

    def test_rejects_conditional_title_in_both_carrier_shapes(self):
        for title in ("If approved", "Proposed registration", "Not yet admitted", "Example values"):
            for body in (EXCERPT, "## Claim\n\n" + EXCERPT):
                raw = source(body).replace("# Register Type Values", "# " + title)
                with self.subTest(title=title, body=body), self.assertRaises(ValueError):
                    validate_allowed_value_evidence(
                        mention(evidence=proof()), {AUTHORITY: raw}, self.targets)

    def test_unsupported_value_tokens_fail_closed(self):
        for first in ("QA Case, when approved", "QA Case (provisional)", "some QA Case", "QA/Case"):
            body = EXCERPT.replace("QA Case", first)
            item = mention(
                definitions=[{"authority": AUTHORITY, "excerpt": body}],
                evidence=proof(excerpt=body),
            )
            with self.subTest(first=first), self.assertRaises(ValueError):
                validate_allowed_value_evidence(item, {AUTHORITY: source(body)}, self.targets)

    def test_rejects_summary_scope_details_quotes_and_code(self):
        bodies = (
            "# Summary\n\n" + EXCERPT + "\n\n## Claim\n\nOther Claim.",
            "## Scope\n\n" + EXCERPT + "\n\n## Claim\n\nOther Claim.",
            "## Claim\n\nOther Claim.\n\n## Details\n\n" + EXCERPT,
            "> " + EXCERPT,
            "```markdown\n" + EXCERPT + "\n```",
            "    " + EXCERPT,
            "\t" + EXCERPT,
        )
        for body in bodies:
            with self.subTest(body=body), self.assertRaises(ValueError):
                validate_allowed_value_evidence(
                    mention(evidence=proof()), {AUTHORITY: source(body)}, self.targets)

    def test_rejects_extra_conditional_or_exception_prose_around_registration(self):
        bodies = (
            "this registration is conditional.\n\n" + EXCERPT,
            EXCERPT + "\n\n**otherwise** this exception applies.",
        )
        for body in bodies:
            with self.subTest(body=body), self.assertRaises(ValueError):
                validate_allowed_value_evidence(
                    mention(evidence=proof()), {AUTHORITY: source(body)}, self.targets)

    def test_real_r1526_agentic_named_value_bullet_is_admitted(self):
        root = Path(__file__).resolve().parents[6]
        path = root / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/"
            "CA-R-1526-CORE_META_MODEL-GENERAL-REQUIREMENT--define-action-execution-kind.md"
        )
        authority = "CA-R-1526@4"
        self.assertTrue(validate_allowed_value_evidence(
            execution_mention(authority=authority), {authority: path.read_text()},
            {authority: EXECUTION_PROPERTY}))

    def test_named_value_bullet_rejects_unknown_non_governing_wrong_property_and_cropping(self):
        opening = "Action Execution Kind **means** one selected execution form."
        raw = execution_source(opening + "\n\n" + EXECUTION_EXCERPT)
        authority = "MOCK-R-1526@1"
        cases = (
            (execution_mention(value="Unknown"), raw, {authority: EXECUTION_PROPERTY}),
            (execution_mention(), raw, {authority: "Action"}),
            (execution_mention(property_path="Action/Kind"), raw, {authority: EXECUTION_PROPERTY}),
            (execution_mention(excerpt="- Agentic: an AI Agent interprets the supplied context"), raw,
             {authority: EXECUTION_PROPERTY}),
        )
        for item, evidence_raw, targets in cases:
            with self.subTest(item=item), self.assertRaises(ValueError):
                validate_allowed_value_evidence(item, {authority: evidence_raw}, targets)

    def test_named_value_bullet_rejects_conditional_example_negated_and_non_list_context(self):
        opening = "Action Execution Kind **means** one selected execution form."
        cases = (
            "- Agentic: an AI Agent performs the Action **if** approved.",
            "- Agentic: Example execution by an AI Agent performs the Action.",
            "- Agentic: an AI Agent does **not** perform the Action.",
            "Agentic: an AI Agent performs the Action.",
        )
        authority = "MOCK-R-1526@1"
        for bullet in cases:
            raw = execution_source(opening + "\n\n" + bullet)
            item = execution_mention(excerpt=bullet)
            with self.subTest(bullet=bullet), self.assertRaises(ValueError):
                validate_allowed_value_evidence(item, {authority: raw}, {authority: EXECUTION_PROPERTY})

    def test_real_r1307_conditional_domain_admits_both_activity_values(self):
        root = Path(__file__).resolve().parents[6]
        path = root / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/"
            "CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models.md"
        )
        raw = path.read_text()
        authority = "CA-R-1307@12"
        targets = {authority: ACTIVITY_PROPERTY}
        for value in ("Active", "Inactive"):
            with self.subTest(value=value):
                item = activity_mention(
                    value,
                    definitions=[{"authority": authority, "excerpt": ACTIVITY_EXCERPT}],
                    evidence=activity_proof(value, authority=authority),
                )
                self.assertTrue(validate_allowed_value_evidence(item, {authority: raw}, targets))

    def test_conditional_domain_rejects_wrong_path_value_or_sentence_shape(self):
        authority = "MOCK-R-1307@1"
        targets = {authority: ACTIVITY_PROPERTY}
        malformed = (
            (ACTIVITY_EXCERPT.replace("an Artifact", "an Record"), ACTIVITY_PROPERTY, "Active"),
            (ACTIVITY_EXCERPT, "Artifact/Revision/Status", "Active"),
            (ACTIVITY_EXCERPT, ACTIVITY_PROPERTY, "Unknown"),
            (ACTIVITY_EXCERPT.replace("**`=1`**", "**`>=1`**"), ACTIVITY_PROPERTY, "Active"),
            (ACTIVITY_EXCERPT.replace("**`=0`** Activity", "**`=0`** Status"), ACTIVITY_PROPERTY, "Active"),
            (ACTIVITY_EXCERPT.replace(", **and** **`=0`** Activity **otherwise**", ""), ACTIVITY_PROPERTY, "Active"),
        )
        for body, property_path, value in malformed:
            with self.subTest(body=body, property_path=property_path, value=value):
                evidence = activity_proof(property=property_path, value=value, excerpt=body)
                item = activity_mention(
                    value,
                    definitions=[{"authority": authority, "excerpt": body}],
                    evidence=evidence,
                )
                with self.assertRaises(ValueError):
                    validate_allowed_value_evidence(
                        item, {authority: activity_source(body)}, targets)

    def test_conditional_domain_rejects_context_and_non_domain_classification(self):
        authority = "MOCK-R-1307@1"
        cases = (
            activity_source(heading="Proposed Artifact Activity"),
            activity_source(heading="If approved"),
            activity_source(ACTIVITY_EXCERPT + "\n\nAdditional context."),
            activity_source("> " + ACTIVITY_EXCERPT),
            activity_source("```markdown\n" + ACTIVITY_EXCERPT + "\n```"),
            activity_source().replace("status: Active\n", "status: Active\nstatus: Draft\n"),
        )
        item = activity_mention()
        for raw in cases:
            with self.subTest(raw=raw):
                with self.assertRaises(ValueError):
                    validate_allowed_value_evidence(
                        item, {authority: raw}, {authority: ACTIVITY_PROPERTY})

        # Historical wording is test data, not a lookup of current authority.
        # A renamed/revised source must not make this regression pass merely
        # because its quoted sentence disappeared.
        classification = (
            "the Artifact Property Activity **means** the derived Property that classifies "
            "an Artifact as Active **or** Inactive from its current Revision Status within "
            "the applicability defined by CA-R-1307."
        )
        raw = activity_source(classification, heading="Define Artifact Activity")
        only_classification = activity_mention(
            definitions=[{"authority": "CA-R-1394@10", "excerpt": classification}],
            evidence=activity_proof(authority="CA-R-1394@10", excerpt=classification),
        )
        with self.assertRaises(ValueError):
            validate_allowed_value_evidence(
                only_classification, {"CA-R-1394@10": raw},
                {"CA-R-1394@10": ACTIVITY_PROPERTY})

    def test_conditional_domain_rejects_dependent_only_authority(self):
        authority = "MOCK-R-OTHER@1"
        raw = activity_source(governs="Artifact/Revision/Status").replace(
            "  governs: \"Artifact/Revision/Status\"\n",
            "  governs: \"Artifact/Revision/Status\"\n"
            "  depends_on:\n"
            "    - \"Artifact/Activity\"\n",
        )
        item = activity_mention(
            definitions=[{"authority": authority, "excerpt": ACTIVITY_EXCERPT}],
            evidence=activity_proof(authority=authority),
        )
        with self.assertRaises(ValueError):
            validate_allowed_value_evidence(
                item, {authority: raw}, {authority: "Artifact/Revision/Status"})

    def test_conditional_domain_accepts_another_direct_exact_domain(self):
        authority = "MOCK-R-DISPOSITION@1"
        property_path = "Record/Disposition"
        excerpt = (
            "an Record **must** have **`=1`** Disposition **in** (Kept, Discarded) "
            "**if** an explicitly defined Status model applies **to** it, **and** "
            "**`=0`** Disposition **otherwise**."
        )
        raw = activity_source(
            excerpt, governs=property_path, heading="Define Record Disposition")
        for value in ("Kept", "Discarded"):
            with self.subTest(value=value):
                evidence = {
                    "property": property_path,
                    "value": value,
                    "authority": authority,
                    "excerpt": excerpt,
                }
                item = {
                    "entity": f"{property_path}: {value}",
                    "definitions": [{"authority": authority, "excerpt": excerpt}],
                    "allowed_value_evidence": evidence,
                }
                self.assertTrue(validate_allowed_value_evidence(
                    item, {authority: raw}, {authority: property_path}))

    def test_conditional_domain_rejects_wrong_proof_bearer_or_authority_target(self):
        authority = "MOCK-R-DISPOSITION@1"
        property_path = "Record/Disposition"
        excerpt = (
            "an Record **must** have **`=1`** Disposition **in** (Kept, Discarded) "
            "**if** an explicitly defined Status model applies **to** it, **and** "
            "**`=0`** Disposition **otherwise**."
        )
        raw = activity_source(
            excerpt, governs=property_path, heading="Define Record Disposition")

        wrong_bearer = {
            "property": "Artifact/Disposition",
            "value": "Kept",
            "authority": authority,
            "excerpt": excerpt,
        }
        wrong_bearer_item = {
            "entity": "Artifact/Disposition: Kept",
            "definitions": [{"authority": authority, "excerpt": excerpt}],
            "allowed_value_evidence": wrong_bearer,
        }
        with self.assertRaises(ValueError):
            validate_allowed_value_evidence(
                wrong_bearer_item, {authority: raw}, {authority: property_path})

        correct_proof_wrong_target = {
            "property": property_path,
            "value": "Kept",
            "authority": authority,
            "excerpt": excerpt,
        }
        correct_item = {
            "entity": "Record/Disposition: Kept",
            "definitions": [{"authority": authority, "excerpt": excerpt}],
            "allowed_value_evidence": correct_proof_wrong_target,
        }
        with self.assertRaises(ValueError):
            validate_allowed_value_evidence(
                correct_item, {authority: raw}, {authority: "Record/Status"})

    def test_real_d316_internal_carrier_ownership_domain_is_bounded(self):
        root = Path(__file__).resolve().parents[6]
        path = root / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/"
            "CA-D-316-CORE_META_MODEL-GENERAL-DELIVERY--classify-carriers-by-ownership.md"
        )
        raw = path.read_text()
        targets = {OWNERSHIP_AUTHORITY: OWNERSHIP_PROPERTY}
        for value in OWNERSHIP_VALUES:
            with self.subTest(value=value):
                self.assertTrue(validate_allowed_value_evidence(
                    ownership_mention(value), {OWNERSHIP_AUTHORITY: raw}, targets))

        rejected = (
            (ownership_mention("Framework-Owned", entity="Framework-Owned Carrier"), raw, targets),
            (ownership_mention("Framework-Owned", property_path="Artifact/Ownership Class"), raw, targets),
            (ownership_mention("External-Owned"), raw, targets),
            (ownership_mention("Framework-Owned"), raw + "\nExtra context.\n", targets),
            (ownership_mention(
                "Framework-Owned",
                excerpt=OWNERSHIP_EXCERPT.replace("internal CAPRMEDIO ", ""),
            ), raw.replace("internal CAPRMEDIO ", ""), targets),
            (ownership_mention("Framework-Owned"), raw.replace("status: \"Active\"", "status: \"Draft\""), targets),
            (ownership_mention("Framework-Owned"), raw, {OWNERSHIP_AUTHORITY: "Other/Ownership Class"}),
        )
        for item, evidence_raw, evidence_targets in rejected:
            with self.subTest(item=item):
                with self.assertRaises(ValueError):
                    validate_allowed_value_evidence(
                        item, {OWNERSHIP_AUTHORITY: evidence_raw}, evidence_targets)


if __name__ == "__main__":
    unittest.main()
