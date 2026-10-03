"""Real CLI regressions for the new adapters with exact, frozen authority inputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest
from typing import Any, cast

from golden_fixtures import fingerprint, isolated_directory

TOOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL))

from validate_atoms_workers.authority import resolve_context  # noqa: E402
from validate_atoms_workers.check_dispatch import ADAPTER_CODES  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from validate_atoms_workers.settings import CEILINGS  # noqa: E402


def frozen_sources() -> list[dict[str, Any]]:
    entries: dict[str, Any] = {}
    for name in (
        "registry",
        "schema_authority",
        "graph_authority",
        "structure_authority",
        "context_authority",
    ):
        entries.update(
            json.loads((TOOL / "validate_atoms_workers" / (name + ".json")).read_text())["sources"]
        )
    fixtures = TOOL / "tests/fixtures"
    result = []
    for identifier, entry in entries.items():
        paths = sorted(fixtures.glob("*/" + identifier + ".md"))
        matches = [
            path
            for path in paths
            if hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
        ]
        if not matches:
            raise AssertionError("Missing exact fixture: " + identifier)
        path = matches[0]
        text = path.read_text()
        result.append(
            dict(
                binding=dict(
                    atom_id=identifier,
                    version=entry["version"],
                    path=str(path),
                    sha256=entry["sha256"],
                ),
                text=text,
                metadata=parse_carrier(text.encode(), path).metadata,
            )
        )
    return result


def run_cli(
    root: Path,
    carrier: str,
    reference: str | None = None,
    request_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    authority = root / "authority"
    atoms = root / "atoms"
    authority.mkdir()
    atoms.mkdir()
    frontier = []
    for source in frozen_sources():
        binding = dict(source["binding"])
        path = authority / (binding["atom_id"] + ".md")
        path.write_bytes(source["text"].encode())
        binding["path"] = str(path)
        frontier.append(binding)
    target = atoms / "EX-P-1-TEST-PLAN--do-work.md"
    target.write_text(carrier)
    if reference is not None:
        (atoms / "reference.md").write_text(reference)
    request = dict(
        schema_version=1,
        source_roots=[str(atoms)],
        reference_roots=[str(atoms)],
        allowed_read_roots=[str(root)],
        methodology=dict(kind="sources", roots=[str(authority)], frontier=frontier),
        selection=dict(atoms=[dict(carrier_path=str(target))]),
        limits=dict(CEILINGS),
    )
    request.update(request_context or {})
    before = fingerprint(root)
    process = subprocess.run(
        [sys.executable, "-B", str(TOOL / "validate_atoms.py"), "--input", "-"],
        input=json.dumps(request),
        text=True,
        capture_output=True,
        timeout=20,
    )
    if process.returncode != 2:
        raise AssertionError(process.stderr + process.stdout)
    if fingerprint(root) != before:
        raise AssertionError("Read-only validation modified its inputs")
    return cast(dict[str, Any], json.loads(process.stdout))


PLAN = """---
atom_id: EX-P-1
version: 1
status: Active
content_role: Plan
type: Plan
current_scope_unit: TEST
claim_target_scope_unit: TEST
author: Test Operator
local_tier: Standard
global_tier: 2
updated_at: "2026-09-25T00:00:00Z"
subjects:
  governs: Atom
  depends_on: []
relations: {}
autonomous_confidence_threshold: 99
implementation_retry_limit: 0
---
# Summary

Do work

## Objective

the Assignee **must** do the work.

## Details

### Definition of Done

the Plan is **not** Done **if** the work is missing.
"""


class ExtendedIntegration(unittest.TestCase):
    def test_twenty_additional_adapters_are_registered(self) -> None:
        expected = {
            "relations.resolution",
            "subjects.resolution",
            "subjects.migration",
            "frontmatter.updated_at_quoting",
            "property.admission",
            "owner.resolution",
            "model.domains",
            "tier.resolution",
            "projection.fidelity",
            "plan.retry_domain",
            "plan.blocking_resolution",
            "plan.override_selection",
            "property.single_location",
            "body.additional_properties",
            "address.consistency",
            "plan.decomposition_resolution",
            "target.resolution",
            "status.resolution",
            "status.placement",
            "plan.model",
            "plan.assignee_resolution",
        }
        self.assertTrue(expected <= ADAPTER_CODES)
        context = resolve_context(frozen_sources())
        self.assertEqual(context.required, 51)
        self.assertEqual(context.supported, 51)
        self.assertEqual({o.code for o in context.obligations if not o.supported}, set())

    def test_cli_passes_good_encodings_without_claiming_complete_coverage(self) -> None:
        with isolated_directory() as directory:
            report = run_cli(Path(directory), PLAN)
        outcomes = {o["code"]: o for o in report["carriers"][0]["outcomes"]}
        for code in (
            "plan.retry_domain",
            "plan.override_selection",
            "frontmatter.updated_at_quoting",
            "property.single_location",
            "plan.model",
        ):
            self.assertEqual(outcomes[code]["outcome"], "passed", (code, report["findings"]))
        self.assertEqual(report["result"], "incomplete")
        self.assertEqual(report["execution"]["diagnostics"], [])

    def test_assignee_resolution_is_not_applicable_to_non_plan_carrier(self) -> None:
        requirement = (
            PLAN.replace("content_role: Plan", "content_role: Requirement")
            .replace("type: Plan", "type: Requirement")
        )
        with isolated_directory() as directory:
            report = run_cli(Path(directory), requirement)
        outcomes = {o["code"]: o for o in report["carriers"][0]["outcomes"]}
        self.assertEqual(outcomes["plan.assignee_resolution"]["outcome"], "not_applicable")

    def test_cli_retains_independent_failures_with_context_gaps(self) -> None:
        bad = PLAN.replace("implementation_retry_limit: 0", "implementation_retry_limit: -1")
        bad = bad.replace('updated_at: "2026-09-25T00:00:00Z"', "updated_at: 2026-09-25T00:00:00Z")
        bad = bad.replace("relations: {}", "relations:\n  blocks: [EX-R-2]")
        reference = (
            PLAN.replace("EX-P-1", "EX-R-2")
            .replace("content_role: Plan", "content_role: Requirement")
            .replace("type: Plan", "type: Requirement")
        )
        with isolated_directory() as directory:
            report = run_cli(Path(directory), bad, reference)
        outcomes = {o["code"]: o for o in report["carriers"][0]["outcomes"]}
        for code in (
            "plan.retry_domain",
            "frontmatter.updated_at_quoting",
            "plan.blocking_resolution",
        ):
            self.assertEqual(outcomes[code]["outcome"], "failed", (code, report["findings"]))
        self.assertEqual(outcomes["author.resolution"]["outcome"], "not_checked")
        self.assertEqual(report["execution"]["diagnostics"], [])


if __name__ == "__main__":
    unittest.main()
