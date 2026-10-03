"""Source-authored Operator membership cases, including real public CLI calls."""

import hashlib
import unittest
from pathlib import Path
from typing import Any

from golden_fixtures import isolated_directory
from test_extended_integration import frozen_sources, PLAN, run_cli
from validate_atoms_workers.authority import resolve_context
from validate_atoms_workers.check_dispatch import _execute
from validate_atoms_workers.check_operators import load_operators_registry
from validate_atoms_workers.read_io import ReadContext, LimitReached
from validate_atoms_workers.settings import CEILINGS


REGISTRY = '[[operators]]\nname = "Test Operator"\nrole = "project owner"\n'


def assess(
    root: Path, metadata: dict[str, Any], raw: str | None = REGISTRY, **binding: Any
) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    request: dict[str, Any] = {}
    if raw is not None:
        path = root / "operators_registry.toml"
        path.write_text(raw)
        request["operators_registry"] = dict(path=str(path), **binding)
    reader = ReadContext([str(root)], dict(CEILINGS))
    sources = frozen_sources()
    context = resolve_context(sources)
    obligation = next(o for o in context.obligations if o.code == "author.resolution")
    return _execute(
        obligation,
        metadata,
        "",
        context,
        dict(sources=sources, operators_registry=load_operators_registry(request, reader)),
    )


class OperatorRegistryTests(unittest.TestCase):
    def test_exact_membership_not_role_case_alias_or_whitespace(self) -> None:
        for author, expected in [
            ("Test Operator", "passed"),
            ("Other Operator", "failed"),
            ("test operator", "failed"),
            (" Test Operator", "failed"),
            ("project owner", "failed"),
        ]:
            with self.subTest(author=author), isolated_directory() as directory:
                outcome, findings, gaps = assess(Path(directory), {"author": author})
                self.assertEqual(outcome["outcome"], expected)
                self.assertEqual(
                    [f["code"] for f in findings],
                    [] if expected == "passed" else ["AUTHOR_UNREGISTERED"],
                )
                self.assertEqual(gaps, [])

    def test_missing_and_invalid_author_values(self) -> None:
        cases: list[dict[str, Any]] = [
            {},
            {"author": None},
            {"author": []},
            {"author": " "},
            {"author": 1},
        ]
        for metadata in cases:
            with self.subTest(metadata=metadata), isolated_directory() as directory:
                outcome, findings, _ = assess(Path(directory), metadata)
                self.assertEqual(outcome["outcome"], "failed")
                self.assertEqual(findings[0]["property"], "author")

    def test_invalid_or_absent_registry_never_proves_nonmembership(self) -> None:
        for raw in [
            None,
            "",
            "bad [toml",
            "operators = []",
            "operators = 1",
            REGISTRY * 2,
            REGISTRY.replace('role = "project owner"', ""),
            REGISTRY.replace('role = "project owner"', "role = 1"),
            REGISTRY.replace('name = "Test Operator"', 'name = " "'),
            REGISTRY + "extra = true\n",
            "unexpected = true\n" + REGISTRY,
            REGISTRY + 'name = "Duplicate key"\n',
        ]:
            with self.subTest(raw=raw), isolated_directory() as directory:
                outcome, findings, gaps = assess(Path(directory), {"author": "Unknown"}, raw)
                self.assertEqual(outcome["outcome"], "not_checked")
                self.assertEqual(findings, [])
                self.assertTrue(gaps)

    def test_stale_digest_is_incomplete(self) -> None:
        with isolated_directory() as directory:
            outcome, findings, gaps = assess(
                Path(directory), {"author": "Test Operator"}, sha256="0" * 64
            )
            self.assertEqual(outcome["outcome"], "not_checked")
            self.assertFalse(findings)
            self.assertTrue(gaps)

    def test_bounded_missing_denied_and_symlink_reads(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            actual = root / "operators_registry.toml"
            actual.write_text(REGISTRY)
            link = root / "registry-link.toml"
            link.symlink_to(actual)
            for path in [root / "missing.toml", root / ".env", link]:
                reader = ReadContext([str(root)], dict(CEILINGS))
                result = load_operators_registry({"operators_registry": {"path": str(path)}}, reader)
                self.assertIsNone(result["names"])
                self.assertTrue(result["error"])
            reader = ReadContext([str(root / "other")], dict(CEILINGS))
            self.assertIsNone(
                load_operators_registry({"operators_registry": {"path": str(actual)}}, reader)[
                    "names"
                ]
            )
            reader = ReadContext([str(root)], dict(CEILINGS, max_file_bytes=1))
            with self.assertRaises(LimitReached):
                load_operators_registry({"operators_registry": {"path": str(actual)}}, reader)

    def test_registry_participates_in_currentness(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            path = root / "operators_registry.toml"
            path.write_text(REGISTRY)
            reader = ReadContext([str(root)], dict(CEILINGS))
            self.assertEqual(
                load_operators_registry({"operators_registry": {"path": str(path)}}, reader)["names"],
                frozenset({"Test Operator"}),
            )
            self.assertIn(str(path), reader.fingerprints)
            path.write_text(REGISTRY.replace("Test Operator", "Another Operator"))
            self.assertEqual(reader.currentness()["state"], "changed")

    def test_cli_passes_registered_and_reports_unregistered_without_assignee(self) -> None:
        for author, expected in [("Test Operator", "passed"), ("Unknown Operator", "failed")]:
            with self.subTest(author=author), isolated_directory() as directory:
                root = Path(directory)
                registry = root / "operators_registry.toml"
                registry.write_text(REGISTRY)
                digest = hashlib.sha256(registry.read_bytes()).hexdigest()
                report = run_cli(
                    root,
                    PLAN.replace("author: Test Operator", "author: " + author),
                    request_context={
                        "operators_registry": {"path": str(registry), "sha256": digest}
                    },
                )
                outcomes = {o["code"]: o for o in report["carriers"][0]["outcomes"]}
                self.assertEqual(outcomes["author.resolution"]["outcome"], expected)
                self.assertEqual(outcomes["plan.assignee_resolution"]["outcome"], "not_checked")
                self.assertIn(
                    {"path": str(registry), "sha256": digest}, report["bindings"]["context"]
                )
                self.assertEqual(report["currentness"]["state"], "unchanged")

    def test_cli_stale_registry_does_not_fail_author_membership(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            registry = root / "operators_registry.toml"
            registry.write_text(REGISTRY)
            report = run_cli(
                root,
                PLAN,
                request_context={"operators_registry": {"path": str(registry), "sha256": "0" * 64}},
            )
            outcome = next(
                o for o in report["carriers"][0]["outcomes"] if o["code"] == "author.resolution"
            )
            self.assertEqual(outcome["outcome"], "not_checked")
            self.assertFalse(any(f["code"] == "AUTHOR_UNREGISTERED" for f in report["findings"]))


if __name__ == "__main__":
    unittest.main()
