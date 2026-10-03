"""Contract and mock-evidence tests; these do not simulate LLM judgment."""
import copy
import hashlib
import json
import re
import sys
import tomllib
import unittest
from pathlib import Path

import yaml

from test_split_evaluation import context, contract, gap, merge_evaluations, part

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[4]
CORE = ROOT / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
CHECKS = {"properties", "scope", "claim", "details", "cce", "summary"}
EVALUATORS = {"evaluate_cce", "evaluate_properties", "evaluate_coherence"}
SECTIONS = [
    "1) Role & Mission", "2) Operating Principles (guarantee first-try success)",
    "3) Inputs & Interpretation", "4) Task-Type Playbooks (select matching TASK_TYPE)",
    "5) Formatting & Output Contract", "6) Web, Data, and Citations",
    "7) Error Handling & Edge Cases", "8) Final Validation Checklist (silent)",
    "9) Answer Template (the assistant will follow for final outputs)",
]


def atom(identifier):
    paths = [p for p in CORE.rglob(identifier + "-*.md")
             if not {"archive", "draft", "resolved", "done"}.intersection(p.parts)]
    if len(paths) != 1:
        raise AssertionError((identifier, paths))
    raw = paths[0].read_bytes()
    return paths[0], raw, yaml.safe_load(raw.decode().split("---", 2)[1])


def validate_evidence(evaluation):
    """Exercise production admission, not a second test-only implementation."""
    contract.summarize_evaluations([evaluation], context=context())
    return evaluation["result"]


def route(step, result, edges):
    return edges.get((step, result), "blocked")


def passing_evidence():
    return merge_evaluations([part(group) for group in contract.GROUPS])


class PromptContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = atom("CA-O-104")[1].decode()
        cls.edges = {(a, b): c for a, b, c in re.findall(
            r"^\| (CA-O-\d+) \| (.+?) \| (CA-O-\d+|completed|blocked) \|$",
            cls.workflow, re.M)}
        cls.nodes = set(re.findall(r"^\d\. .* through (CA-O-\d+)\.$", cls.workflow, re.M))
        cls.prompts = {p.stem.removesuffix(".prompt"): p.read_text() for p in HERE.glob("*.prompt.md")}

    def test_three_steps_and_actions_only(self):
        self.assertEqual(self.nodes, {"CA-O-108", "CA-O-109", "CA-O-110"})
        self.assertEqual(set(self.prompts), self.nodes | {"evaluate_atom"} | EVALUATORS)
        actions = set()
        for step in self.nodes:
            binding = re.search(r"Step: (CA-O-\d+) \| Action: (CA-O-\d+) \| Context: (\w+)", self.prompts[step])
            self.assertIsNotNone(binding)
            self.assertEqual(binding[1], step)
            text = atom(step)[1].decode()
            self.assertIn("**`=1`** Action, " + binding[2], text)
            self.assertIn("**in** " + binding[3] + " context", text)
            self.assertEqual(atom(binding[2])[2]["type"], "Action")
            actions.add(binding[2])
        self.assertEqual(len(actions), 3)

    def test_routing_covers_every_result_without_cycles(self):
        for step in self.nodes:
            labels = set(re.search(r"^Results: (.+)$", self.prompts[step], re.M)[1].split(" | "))
            self.assertEqual(labels, {b for a, b in self.edges if a == step})
        self.assertEqual(route("CA-O-108", "ready", self.edges), "CA-O-109")
        self.assertEqual(route("CA-O-108", "empty", self.edges), "completed")
        self.assertEqual(route("CA-O-109", "issues", self.edges), "CA-O-110")
        self.assertEqual(route("CA-O-110", "fixed_not_rechecked", self.edges), "completed")
        for step in self.nodes:
            self.assertEqual(route(step, "blocked", self.edges), "blocked")
            self.assertEqual(route(step, "unexpected", self.edges), "blocked")
        for start in self.nodes:
            def walk(node, visited):
                self.assertNotIn(node, visited)
                for (source, _), target in self.edges.items():
                    if source == node and target in self.nodes:
                        walk(target, visited | {node})
            walk(start, set())

    def test_short_prompts_and_required_sections(self):
        for name, prompt in self.prompts.items():
            with self.subTest(prompt=name):
                self.assertTrue(prompt.startswith("# System Prompt\n"))
                if name in self.nodes:
                    self.assertNotRegex(prompt, r"(?m)^###")
                    self.assertLessEqual(len(prompt.split()), 160)
                else:
                    self.assertEqual(re.findall(r"^### (.+)$", prompt, re.M), SECTIONS)
                self.assertLessEqual(len(prompt.split()), 1800 if name == 'evaluate_coherence' else 1500 if name in EVALUATORS else 550 if name == "evaluate_atom" else 300)
                if name in self.nodes:
                    self.assertIn("Read", prompt)
                    self.assertIn("source", prompt.casefold())
                elif name == "evaluate_atom":
                    self.assertIn("pinned authority and input packet", prompt)
                    self.assertIn("README contract", prompt)
                else:
                    self.assertIn("inline", prompt)
                self.assertNotRegex(prompt, r"\b(?:TODO|TBD)\b")

    def test_evaluation_exactly_covers_authority_checklist(self):
        text = atom("CA-E-520")[1].decode()
        source_checks = set(re.findall(r"^\| (\w+) \|", text, re.M)) - {"Check"}
        self.assertEqual(source_checks, CHECKS)
        sys.path.insert(0, str(HERE))
        from evaluation_contract import LOCAL_GROUPS as GROUPS
        prompt_checks = {check for checks in GROUPS.values() for check in checks}
        self.assertEqual(prompt_checks, CHECKS)
        for group, checks in GROUPS.items():
            for check in checks:
                self.assertIn(check, self.prompts["evaluate_" + group])

    def test_properties_prompt_preserves_optional_specialized_type_boundary(self):
        prompt = self.prompts["evaluate_properties"]
        row = next(line for line in prompt.splitlines() if line.startswith("| `type` |"))
        self.assertIn("ordinary R/M/D omit it unless a specialized Type applies", row)
        self.assertIn("one admitted String", row)
        self.assertIn("never a role-echo placeholder", row)
        self.assertIn("Evaluation retains its applicable Type requirement", row)
        for authority in ("CA-R-1700", "CA-D-276", "CA-D-283"):
            self.assertIn(authority, prompt)

    def test_freshness_permission_and_repair_guards(self):
        evaluation = self.prompts["evaluate_atom"]
        for phrase in ("before and after", "Below-threshold", "do not edit", "incomplete", "prerequisite"):
            self.assertIn(phrase.casefold(), evaluation.casefold())
        repair = " ".join(self.prompts["CA-O-110"].split())
        for phrase in ("Summary change may require replacement", "Formatting-only",
                       "governing checks to force a pass", "missing permission", "fixed_not_rechecked"):
            self.assertIn(phrase, repair)

    def test_project_scope_filename_selection_is_bound_and_not_an_alias_registry(self):
        manifest = json.loads((HERE / "source_bindings.json").read_text())
        entry = next(row for row in manifest["sources"] if row["atom_id"] == "CA-D-498")
        raw = (ROOT / entry["path"]).read_bytes()
        meta = yaml.safe_load(raw.decode().split("---", 2)[1])
        self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"])
        self.assertEqual(meta["current_scope_unit"], "PROJECT_CONFIGURATION")
        self.assertEqual(meta["status"], "Active")
        self.assertNotIn("type", meta)
        self.assertEqual(re.findall(r"^## (.+)$", raw.decode(), re.M), ["Scope", "Claim", "Details"])
        prompt = self.prompts["evaluate_properties"]
        for phrase in ("No filename/location conformance", "do not infer Properties from filenames or folders"):
            self.assertIn(phrase, prompt)

    def test_role_directory_mapping_is_bound_recursively_with_placement_exceptions(self):
        manifest = json.loads((HERE / "source_bindings.json").read_text())
        bindings = {row["atom_id"]: row for row in manifest["sources"]}
        self.assertTrue({"CA-D-296", "CA-D-324", "CA-D-451", "CA-D-466"} <= bindings.keys())
        raw = (ROOT / bindings["CA-D-324"]["path"]).read_text()
        meta = yaml.safe_load(raw.split("---", 2)[1])
        self.assertEqual(meta["current_scope_unit"], "PROJECT_CONFIGURATION")
        self.assertEqual(meta["status"], "Active")
        self.assertNotIn("type", meta)
        self.assertIn("Scope Unit", meta["subjects"]["depends_on"])
        self.assertEqual(re.findall(r"^## (.+)$", raw, re.M), ["Scope", "Claim", "Details"])
        mapping = re.findall(r"^- ([A-Za-z]+): `([0-9]{2}_[a-z]+/)`[;.]$", raw, re.M)
        self.assertEqual(mapping, list(zip(
            ("Concern", "Analysis", "Plan", "Requirement", "Method", "Evaluation", "Delivery", "Implementation", "Operations"),
            ("01_concern/", "02_analysis/", "03_plan/", "04_requirement/", "05_method/", "06_evaluation/", "07_delivery/", "08_implementation/", "09_operations/"))))
        for phrase in ("**every** Scope Unit", "directly under its own authority directory",
                       "`CORE_META_MODEL`", "`PROJECT_CONFIGURATION`", "preserve specific Carrier placement rules"):
            self.assertIn(phrase, raw)
        prompt = self.prompts["evaluate_properties"]
        for phrase in ("No filename/location conformance", "body layout"):
            self.assertIn(phrase, prompt)

    def test_parameters_are_in_settings_not_prompt_constants(self):
        settings = tomllib.loads((CORE / "caprmedio_framework_default_settings.toml").read_text())
        for prompt in self.prompts.values():
            self.assertNotRegex(prompt, r"\b30 (?:Atoms|atoms|candidates)\b")
            self.assertNotIn("10 minutes", prompt)
            self.assertNotRegex(prompt, r"\b(?:10|90)%")
        self.assertIn("context_headroom_fraction", settings["rmed_review"])

    def test_context_budget_and_fresh_worker_handoff_are_bound(self):
        selection = atom("CA-O-105")[1].decode()
        self.assertIn("resolves a requested selection", selection)
        self.assertIn("relevant `atom_local` rules once", selection)
        self.assertIn("keep the configured headroom unused", selection)
        self.assertIn("Atom per fresh reviewer", selection)
        settings_rule = atom("CA-D-497")[1].decode()
        self.assertIn("`rmed_review.context_headroom_fraction`", settings_rule)
        self.assertIn("no default **when** omitted", settings_rule)
        self.assertIn("`rmed_review.target_minutes` parameter is retired", settings_rule)
        evidence_rule = atom("CA-D-496")[1].decode()
        for phrase in ("`progress.json`", "one review report per source Atom",
                       "fixed_not_rechecked", "short handoff"):
            self.assertIn(phrase, evidence_rule)
        self.assertIn("original selection", evidence_rule)
        self.assertIn("Context: Integrated", self.prompts["CA-O-108"])
        for step in ("CA-O-109", "CA-O-110"):
            self.assertIn("Context: Isolated", self.prompts[step])
        readme = " ".join((HERE / "README.md").read_text().split())
        self.assertIn("one fresh Terra/high reviewer", readme)
        self.assertIn("same-stage handoff resumes in a fresh agent", readme)
        for identifier in ("CA-O-104", "CA-O-106", "CA-O-111"):
            self.assertIn("fresh", atom(identifier)[1].decode())
        repair = atom("CA-O-111")[1].decode()
        self.assertIn("does **not** consume a repair retry", repair)
        self.assertIn("without** repeating an already applied edit", repair)

    def test_current_source_bindings(self):
        manifest = json.loads((HERE / "source_bindings.json").read_text())
        self.assertEqual(manifest["workflow"], "CA-O-104")
        required = self.nodes | {"CA-O-104", "CA-O-105", "CA-O-106", "CA-O-111",
                                 "CA-E-520", "CA-D-496", "CA-D-497", "CA-D-479", "CA-D-495",
                                 "CA-R-1245", "CA-R-1248", "CA-R-1307", "CA-R-1436", "CA-R-1662"}
        ids = [s["atom_id"] for s in manifest["sources"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(required.issubset(ids))
        for entry in manifest["sources"]:
            path = (ROOT / entry["path"]).resolve()
            self.assertTrue(path.is_relative_to(ROOT))
            raw = path.read_bytes()
            meta = yaml.safe_load(raw.decode().split("---", 2)[1])
            self.assertEqual(meta["version"], entry["version"])
            self.assertEqual(meta["atom_id"], entry["atom_id"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"], entry["path"])
        for entry in manifest["settings"]:
            self.assertEqual(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest(), entry["sha256"])

    def test_carrier_role_profiles_use_current_role_and_binding_authority(self):
        manifest = json.loads((HERE / "source_bindings.json").read_text())
        bindings = {entry["atom_id"]: entry for entry in manifest["sources"]}
        self.assertEqual(bindings["CA-R-1339"]["version"], 11)
        self.assertEqual(bindings["CA-R-1342"]["version"], 11)
        self.assertEqual(bindings["CA-M-313"]["version"], 5)
        self.assertIn("Entity model", self.prompts["evaluate_cce"])
        self.assertIn("meaning **and** value", self.prompts["evaluate_cce"])
        self.assertIn("Carrier definitions", self.prompts["evaluate_cce"])
        self.assertIn("semantic Content Role reclassification is excluded", self.prompts["evaluate_cce"])
        self.assertIn("reclassify Content Roles", self.prompts["evaluate_coherence"])

    def test_new_authority_self_describes_its_body(self):
        for identifier in ["CA-E-520", "CA-D-496", "CA-D-497",
                           "CA-O-104", "CA-O-105", "CA-O-106", "CA-O-108",
                           "CA-O-109", "CA-O-110", "CA-O-111"]:
            _, raw, meta = atom(identifier)
            text = raw.decode()
            self.assertEqual(meta["status"], "Active")
            self.assertGreaterEqual(meta["version"], 1)
            self.assertIsInstance(meta["subjects"]["governs"], str)
            expected = ["Operation", "Details"] if meta["content_role"] == "Operations" else ["Scope", "Claim", "Details"]
            self.assertEqual(re.findall(r"^## (.+)$", text, re.M), expected)

    def test_mock_corpus_is_separate_from_expected_judgments(self):
        cases = json.loads((HERE / "tests/fixtures/cases.json").read_text())
        self.assertGreaterEqual(len(cases), 8)
        ids = set()
        for case in cases:
            raw = (HERE / "tests/fixtures" / case["file"]).read_text()
            meta = yaml.safe_load(raw.split("---", 2)[1])
            self.assertNotIn(meta["atom_id"], ids)
            ids.add(meta["atom_id"])
            self.assertNotIn("required_failed_checks", raw)
            legacy_checks = {check for group in contract.GROUPS.values() for check in group}
            self.assertTrue(set(case["required_failed_checks"]).issubset(legacy_checks))
        self.assertTrue(any(not c["required_failed_checks"] for c in cases))

    def test_golden_carriers_reach_real_body_checker(self):
        tool_tests = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/tests"
        sys.path.insert(0, str(tool_tests))
        from test_authority_checks import run_check, outcome
        for case in json.loads((HERE / "tests/fixtures/cases.json").read_text()):
            text = (HERE / "tests/fixtures" / case["file"]).read_text()
            meta = yaml.safe_load(text.split("---", 2)[1])
            checked = run_check(["CA-D-479"], meta, text.split("---", 2)[2])
            self.assertEqual(outcome(checked, "body.sections")["outcome"], case["body_check"])

    def test_evidence_cannot_hide_missing_failed_or_blocked_checks(self):
        good = passing_evidence()
        self.assertEqual(validate_evidence(good), "passed")
        for mutation in ("missing", "duplicate", "no_evidence", "failed", "blocked", "unknown"):
            bad = copy.deepcopy(good)
            if mutation == "missing":
                bad["checks"].pop()
            elif mutation == "duplicate":
                bad["checks"][0]["id"] = bad["checks"][1]["id"]
            elif mutation == "no_evidence":
                bad["checks"][0]["evidence"] = []
            else:
                bad["checks"][0]["status"] = mutation
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                validate_evidence(bad)

    def test_failed_result_retains_blockers(self):
        parts = [part(group) for group in contract.GROUPS]
        parts[0]["checks"][0].update(status="failed", findings=[{
            "kind": "violation", "location": "Claim", "excerpt": "must", "reason": "not bold",
            "proposed_fix": "Render **must**", "confidence": 1.0}])
        parts[0]["result"] = "failed"
        parts[1]["checks"][0]["status"] = "blocked"
        parts[1].update(result="blocked", coverage_gaps=[gap("properties", "Missing authority")])
        evidence = merge_evaluations(parts)
        self.assertEqual(validate_evidence(evidence), "failed")
        self.assertEqual(route("CA-O-109", "blocked", self.edges), "blocked")
        evidence["coverage_gaps"] = []
        with self.assertRaises(ValueError):
            validate_evidence(evidence)


if __name__ == "__main__":
    unittest.main()
