"""Current CA-D-479/470 expectations, authored before adapter changes."""

import unittest
from test_authority_checks import run_check, outcome
from test_schema_extended import run
from test_extended_integration import run_cli
from golden_fixtures import isolated_directory
from pathlib import Path
from typing import Any


LAYOUTS = {
    "Requirement": ["Scope", "Claim", "Details"],
    "Method": ["Scope", "Claim", "Details"],
    "Evaluation": ["Scope", "Claim", "Details"],
    "Delivery": ["Scope", "Claim", "Details"],
    "Concern": ["Concern", "Evidences", "Blast radius"],
    "Analysis": ["Question", "Scope", "Approach", "Results", "TLDR"],
    "Plan": ["Objective", "Details"],
    "Operations": ["Operation", "Details"],
}


def body(role: str) -> str:
    text = "# Summary\nA short summary\n\n"
    for title in LAYOUTS[role]:
        text += "## " + title + "\n" + ("" if title == "Details" else "A value.\n")
    if role == "Plan":
        text += "\n### Definition of Done\nnot done if the required result is absent.\n"
    return text


class CurrentBodyTests(unittest.TestCase):
    def test_absent_summary_has_one_diagnostic_not_two(self) -> None:
        result = self.check_body("Requirement", "# Old title\nUnstructured claim.\n")
        summary = [f for f in result["findings"] if f.get("property") == "Summary"]
        self.assertEqual(len(summary), 1)

    def test_existing_misplaced_summary_still_fails(self) -> None:
        result = self.check_body(
            "Requirement", "## Scope\nAll cases.\n# Summary\nTitle\n## Claim\nClaim.\n## Details\n"
        )
        self.assertTrue(any(
            f.get("property") == "Summary" and "start" in f["reason"]
            for f in result["findings"]
        ))

    def test_rmed_scope_is_required_once_before_claim(self) -> None:
        for role in ("Requirement", "Method", "Evaluation", "Delivery"):
            text = body(role)
            for bad in (
                text.replace("## Scope\nA value.\n", ""),
                text.replace("## Scope\nA value.", "## Scope\n"),
                text + "\n## Scope\nAnother scope\n",
                text.replace("## Scope", "## Swap").replace("## Claim", "## Scope").replace("## Swap", "## Claim"),
            ):
                with self.subTest(role=role, body=bad):
                    self.assertEqual(outcome(self.check_body(role, bad), "body.sections")["outcome"], "failed")

    def test_scope_is_not_duplicate_rmed_frontmatter(self) -> None:
        checked = run("property.single_location", {"content_role": "Requirement", "scope": "duplicate"}, body("Requirement"))
        self.assertTrue(checked.findings)

    def test_real_cli_checks_new_rmed_scope_layout(self) -> None:
        for role in ("Requirement", "Method", "Evaluation", "Delivery"):
            for text, expected in ((body(role), "passed"), (body(role).replace("## Scope\nA value.\n", ""), "failed")):
                with isolated_directory() as directory:
                    carrier = f"---\natom_id: EX-R-1\nversion: 1\nstatus: Active\ncontent_role: {role}\n---\n" + text
                    report = run_cli(Path(directory), carrier)
                    outcomes = {o["code"]: o["outcome"] for o in report["carriers"][0]["outcomes"]}
                    self.assertEqual(outcomes["body.sections"], expected)

    def check_body(self, role: Any, text: str) -> dict[str, Any]:
        return run_check(["CA-D-479"], {"content_role": role}, text)

    def test_each_current_role_layout_and_empty_details(self) -> None:
        for role in LAYOUTS:
            with self.subTest(role=role):
                self.assertEqual(
                    outcome(self.check_body(role, body(role)), "body.sections")["outcome"], "passed"
                )

    def test_missing_duplicate_reordered_and_nested_sections_fail(self) -> None:
        text = body("Requirement")
        for bad in [
            text.replace("## Details", "### Details"),
            text + "\n## Details\n",
            text.replace("## Details", ""),
            text.replace("## Claim", "## Swap")
            .replace("## Details", "## Claim")
            .replace("## Swap", "## Details"),
        ]:
            self.assertEqual(
                outcome(self.check_body("Requirement", bad), "body.sections")["outcome"], "failed"
            )

    def test_primary_property_and_summary_cannot_be_empty(self) -> None:
        for bad in [
            body("Requirement").replace("A value.", ""),
            body("Requirement").replace("A short summary", ""),
        ]:
            self.assertEqual(
                outcome(self.check_body("Requirement", bad), "body.sections")["outcome"], "failed"
            )

    def test_unknown_or_missing_role_is_not_guessed(self) -> None:
        for role in ["", "Implementation", ["Requirement"]]:
            self.assertEqual(
                outcome(self.check_body(role, body("Requirement")), "body.sections")["outcome"],
                "not_checked",
            )

    def test_fenced_examples_do_not_add_or_close_properties(self) -> None:
        text = body("Requirement").replace(
            "A value.", "A value.\n```md\n## Details\n# Summary\n```"
        )
        self.assertEqual(
            outcome(self.check_body("Requirement", text), "body.sections")["outcome"], "passed"
        )

    def test_plan_definition_of_done_is_nested_under_details(self) -> None:
        meta = {"content_role": "Plan", "type": "Plan"}
        good = body("Plan")
        self.assertEqual(
            outcome(run_check(["CA-D-470"], meta, good), "plan.sections")["outcome"], "passed"
        )
        for bad in [
            good.replace("### Definition", "## Definition"),
            good.replace("### Definition", "#### Definition"),
            good.replace("### Definition", "### Notes\n#### Definition"),
            good + "\n### Definition of Done\nAnother\n",
            good.replace("not done if the required result is absent.", ""),
            good.replace("## Objective", "## Claim"),
        ]:
            self.assertEqual(
                outcome(run_check(["CA-D-470"], meta, bad), "plan.sections")["outcome"], "failed"
            )

    def test_plan_model_uses_objective_not_claim(self) -> None:
        meta = {"content_role": "Plan", "type": "Plan"}
        good = run("plan.model", meta, body("Plan"))
        self.assertEqual(good.findings, [])
        self.assertEqual(good.gaps, [])
        self.assertTrue(
            run("plan.model", meta, body("Plan").replace("## Objective", "## Claim")).findings
        )

    def test_role_body_properties_are_not_duplicate_frontmatter(self) -> None:
        for role, fields in {
            "Plan": ["objective", "details", "definition_of_done"],
            "Analysis": ["question", "scope", "approach", "results", "tldr"],
            "Concern": ["concern", "evidences", "blast_radius"],
            "Operations": ["operation", "details"],
        }.items():
            for field in fields:
                with self.subTest(role=role, field=field):
                    self.assertTrue(
                        run(
                            "property.single_location",
                            {"content_role": role, "type": "Plan", field: "duplicate"},
                            body(role),
                        ).findings
                    )

    def test_additional_properties_uses_role_layout(self) -> None:
        for role in LAYOUTS:
            with self.subTest(role=role):
                checked = run(
                    "body.additional_properties", {"content_role": role, "type": "Plan"}, body(role)
                )
                self.assertEqual(checked.findings, [])
                self.assertEqual(checked.gaps, [])

    def test_real_cli_reports_old_plan_layout_and_passes_new_sections(self) -> None:
        def carrier(text: str) -> str:
            return (
                "---\natom_id: EX-P-1\nversion: 1\nstatus: Active\ncontent_role: Plan\ntype: Plan\n---\n"
                + text
            )

        for text, expected in [
            (body("Plan"), "passed"),
            (body("Plan").replace("## Objective", "## Claim"), "failed"),
        ]:
            with isolated_directory() as directory:
                report = run_cli(Path(directory), carrier(text))
                outcomes = {o["code"]: o["outcome"] for o in report["carriers"][0]["outcomes"]}
                self.assertEqual(outcomes["body.sections"], expected)
                self.assertEqual(outcomes["plan.sections"], expected)
                self.assertEqual(outcomes["plan.model"], expected)


if __name__ == "__main__":
    unittest.main()
