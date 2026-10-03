"""Default local workflow prompt guards; legacy evaluator contracts are separate."""
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]


def prompt(name):
    return " ".join((HERE / name).read_text().split())


class DefaultLocalWorkflowPromptRegressions(unittest.TestCase):
    def test_three_steps_are_scope_check_fix(self):
        readme = prompt("README.md")
        for phrase in ("gather scope", "check selected Atoms", "fix confirmed", "CA-O-108",
                       "CA-O-109", "CA-O-110"):
            self.assertIn(phrase, readme)
        self.assertIn("Gather the requested active RMED Atom scope", prompt("CA-O-108.prompt.md"))
        self.assertIn("Check one selected RMED Atom locally", prompt("CA-O-109.prompt.md"))
        self.assertIn("Fix confirmed local issues", prompt("CA-O-110.prompt.md"))

    def test_check_uses_one_concise_six_outcome_report(self):
        check = prompt("CA-O-109.prompt.md")
        readme = prompt("README.md")
        self.assertIn("one concise report", check)
        for outcome in ("properties", "CCE", "Scope", "Claim", "Details", "Summary"):
            self.assertIn(outcome, check)
        self.assertIn("actual defect quotes", readme)
        self.assertIn("one short progress list", readme)

    def test_atom_checks_finish_before_fix_without_cross_atom_barrier(self):
        self.assertIn("Complete all six checks for an Atom before its normal fix phase",
                      prompt("README.md"))
        self.assertIn("every required check before this Atom's fix phase",
                      prompt("CA-O-109.prompt.md"))
        self.assertIn("all six checks concluded and no remaining issues",
                      prompt("CA-O-110.prompt.md"))

    def test_default_scope_excludes_nonlocal_audits(self):
        readme = prompt("README.md")
        for excluded in ("graphs", "Entity completeness", "cross-Atom comparisons",
                         "classification"):
            self.assertIn(excluded, readme)
        self.assertIn("do not turn exclusions into passes or blockers", prompt("CA-O-109.prompt.md"))

    def test_default_fix_is_not_rechecked(self):
        fix = prompt("CA-O-110.prompt.md")
        readme = prompt("README.md")
        self.assertIn("fixed_not_rechecked", fix)
        self.assertIn("does not recheck saved output", fix)
        self.assertIn("no recheck loop", readme)
        self.assertNotIn("closure_freshness.close_batch", fix)

    def test_identity_write_and_handoff_guards_remain(self):
        fix = prompt("CA-O-110.prompt.md")
        for phrase in ("caller-granted permission", "Preserve identity and history",
                       "Never replay a completed effect", "updated_at",
                       "meaning changes increment Version"):
            self.assertIn(phrase, fix)
        self.assertIn("fresh Terra/high reviewer", prompt("README.md"))
        self.assertIn("same-stage handoff", prompt("README.md"))

    def test_context_budget_comes_from_actual_settings(self):
        readme = prompt("README.md")
        self.assertIn("The caller resolves `rmed_review.context_headroom_fraction`", readme)
        self.assertIn("Hand off at the configured threshold", readme)
        self.assertIn("do not hard-code a fallback", readme)
        self.assertNotIn("90%", readme)
        self.assertNotIn("10%", readme)

    def test_legacy_material_is_optional_not_destroyed(self):
        readme = prompt("README.md")
        self.assertIn("existing evaluator prompts", readme)
        self.assertIn("optional reference material", readme)
        self.assertIn("not erased, relabeled, or implicitly invoked", readme)

    def test_gather_returns_the_selection_without_dispatching(self):
        gather = prompt("CA-O-108.prompt.md")
        self.assertIn("retain the whole requested scope", gather)
        self.assertIn("gathering does not dispatch reviewers", gather)
        self.assertIn("Source Atoms remain unchanged", gather)
        self.assertNotIn("Hand the next Atom", gather)

    def test_fixer_reads_only_its_own_findings(self):
        fix = prompt("CA-O-110.prompt.md")
        self.assertIn("one Atom, its own report", fix)
        self.assertIn("No other reports", fix)
        self.assertNotIn("completed selected-scope reports", fix)

    def test_default_prompts_have_no_nine_section_boilerplate(self):
        for name in ("CA-O-108", "CA-O-109", "CA-O-110"):
            raw = (HERE / f"{name}.prompt.md").read_text()
            with self.subTest(prompt=name):
                self.assertNotIn("###", raw)
                self.assertLessEqual(len(raw.split()), 160)


if __name__ == "__main__":
    unittest.main()
