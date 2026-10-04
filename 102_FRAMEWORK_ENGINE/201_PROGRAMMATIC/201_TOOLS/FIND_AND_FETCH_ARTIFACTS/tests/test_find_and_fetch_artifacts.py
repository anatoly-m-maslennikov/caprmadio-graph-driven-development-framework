import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import find_and_fetch_artifacts as artifact_query
from find_and_fetch_artifacts import ArtifactQueryError, query_artifacts
from query_filter import QueryFilterError, evaluate_filter, parse_filter


class ArtifactQueryGoldenTest(unittest.TestCase):
    def fixture(self, root, name, frontmatter, body=""):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\n" + frontmatter + "\n---\n" + body, encoding="utf-8")
        return path

    def assert_rejected(self, root, request, **kwargs):
        with self.assertRaises((ArtifactQueryError, QueryFilterError)):
            query_artifacts(root, request, **kwargs)

    def test_default_ids_selected_values_and_canonical_section_bodies(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            self.fixture(root, "a.md", "atom_id: A\nstatus: Draft\nflag: true\nnullable: null\nwhen: 2026-10-05\nvalues: [zero, one]", "## same/name~x\nalpha\n### child\nchild\n## sibling\nbeta\n```markdown\n## pseudo\n```\n")
            self.fixture(root, "b.md", "artifact_id: B\nstatus: Archived\nflag: 1\nmap: {kind: x, number: 1}", "## same/name~x\nbravo\n")
            self.fixture(root, "c.md", "artifact_id: C\nstatus: Active")
            source_before = {path.name: path.read_bytes() for path in root.glob("*.md")}
            request = {
                "filter": '"fm:/flag" = true OR "fm:/status" IN ("Archived")',
                "select": ["fm:/nullable", "fm:/when", "section:/2:same~1name~0x"], "limit": 2,
            }
            result = query_artifacts(root, request)
            self.assertEqual([row["artifact_id"] for row in result["results"]], ["A", "B"])
            self.assertEqual(result["results"][0]["fm:/nullable"], None)
            self.assertEqual(result["results"][0]["fm:/when"], "2026-10-05")
            self.assertEqual(result["results"][0]["section:/2:same~1name~0x"], "alpha\n### child\nchild\n")
            self.assertEqual(result["results"][1]["fm:/nullable"], "missing")
            self.assertEqual([row["artifact_id"] for row in query_artifacts(root, {})["results"]], ["A", "B", "C"])
            self.assertEqual(query_artifacts(root, {"filter": '"fm:/map" = {"kind":"x","number":1}'})["results"], [{"artifact_id": "B"}])
            self.assertEqual(query_artifacts(root, {"filter": '"fm:/values" IN (["zero","one"])'})["results"], [{"artifact_id": "A"}])
            self.assertEqual(query_artifacts(root, {"filter": '"fm:/status" != "Draft"'})["results"], [{"artifact_id": "B"}, {"artifact_id": "C"}])
            self.assertEqual(source_before, {path.name: path.read_bytes() for path in root.glob("*.md")})
            self.assertTrue(result["coverage"]["complete"])
            self.assertFalse(result["coverage"]["incomplete"])
            self.assertEqual(result["diagnostics"], {"complete": True, "incomplete": False, "findings": []})

    def test_continuation_uses_exact_retained_members_without_enumeration(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            self.fixture(root, "a.md", "artifact_id: A")
            self.fixture(root, "b.md", "artifact_id: B")
            first = query_artifacts(root, {"limit": 1})
            continuation = {"limit": 1, "snapshot": first["snapshot"], "cursor": first["next_cursor"]}
            with patch.object(artifact_query.os, "walk", side_effect=AssertionError("must not enumerate")):
                second = query_artifacts(root, continuation)
            self.assertEqual(second["results"], [{"artifact_id": "B"}])
            self.assertEqual(second["examined_count"], 2)
            self.assertFalse(second["has_more"])

    def test_same_spelling_frontmatter_and_section_selectors_do_not_collide(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            self.fixture(root, "collision.md", "artifact_id: Collision\nsummary: frontmatter value", "## summary\nsection value\n")
            self.fixture(root, "frontmatter-only.md", "artifact_id: FrontmatterOnly\nsummary: section value", "## unrelated\nother\n")

            self.assertEqual(
                query_artifacts(root, {})["results"],
                [{"artifact_id": "Collision"}, {"artifact_id": "FrontmatterOnly"}],
            )
            self.assertEqual(
                query_artifacts(root, {"filter": '"fm:/summary" = "frontmatter value"'})["results"],
                [{"artifact_id": "Collision"}],
            )
            self.assertEqual(
                query_artifacts(root, {"filter": '"section:/2:summary" = "section value\\n"'})["results"],
                [{"artifact_id": "Collision"}],
            )
            fetched = query_artifacts(root, {
                "filter": '"section:/2:summary" = "section value\\n"',
                "select": ["fm:/summary", "section:/2:summary"],
            })
            self.assertEqual(fetched["results"], [{
                "artifact_id": "Collision", "fm:/summary": "frontmatter value",
                "section:/2:summary": "section value\n",
            }])

    def test_continuation_rejects_changed_root_members_and_tamper(self):
        with tempfile.TemporaryDirectory() as raw, tempfile.TemporaryDirectory() as other:
            root = Path(raw)
            item = self.fixture(root, "a.md", "artifact_id: A")
            first = query_artifacts(root, {"limit": 1})
            tampered = dict(first["snapshot"])
            tampered["digest"] = "0" * 64
            self.assert_rejected(root, {"snapshot": tampered, "cursor": first["next_cursor"]})
            self.assert_rejected(Path(other), {"snapshot": first["snapshot"], "cursor": first["next_cursor"]})
            item.write_text("---\nartifact_id: Changed\n---\n", encoding="utf-8")
            self.assert_rejected(root, {"snapshot": first["snapshot"], "cursor": first["next_cursor"]})

    def test_cursor_is_bound_to_filter_selection_settings_and_bytes(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            self.fixture(root, "a.md", "artifact_id: A\nkind: keep")
            self.fixture(root, "b.md", "artifact_id: B\nkind: keep")
            request = {"filter": '"fm:/kind" = "keep"', "select": ["fm:/kind"], "limit": 1}
            first = query_artifacts(root, request)
            self.assert_rejected(root, {"filter": '"fm:/kind" = "other"', "select": ["fm:/kind"], "snapshot": first["snapshot"], "cursor": first["next_cursor"]})
            self.assert_rejected(root, {"filter": request["filter"], "select": [], "snapshot": first["snapshot"], "cursor": first["next_cursor"]})
            self.assert_rejected(root, {"filter": request["filter"], "select": request["select"], "settings": {"max_page_size": 1}, "snapshot": first["snapshot"], "cursor": first["next_cursor"]})
            self.assert_rejected(root, {"filter": request["filter"], "select": request["select"], "snapshot": first["snapshot"], "cursor": first["next_cursor"] + "x"})

    def test_selector_escaping_section_namespace_and_leading_array_zero(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            self.fixture(root, "x.md", "artifact_id: X\nitems: [zero, one]", "## a/b~c\nok\n")
            self.assertEqual(query_artifacts(root, {"select": ["section:/2:a~1b~0c"]})["results"][0]["section:/2:a~1b~0c"], "ok\n")
            for selector in ("section:2:a", "section:/2:a~2b", "fm:/items/01", "fm:/bad~2key"):
                self.assert_rejected(root, {"select": [selector]})
            self.assert_rejected(root, {"filter": '"fm:/missing" = 1 AND "fm:/items/01" = 1'})

    def test_yaml_safe_duplicate_and_identity_failures_are_not_partial_results(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            self.fixture(root, "duplicate-key.md", "artifact_id: One\nartifact_id: Two")
            self.assert_rejected(root, {})
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            self.fixture(root, "missing.md", "status: Draft")
            self.assert_rejected(root, {})
            (root / "missing.md").unlink()
            self.fixture(root, "conflict.md", "atom_id: A\nartifact_id: B")
            self.assert_rejected(root, {})
            (root / "conflict.md").unlink()
            self.fixture(root, "a.md", "artifact_id: Duplicate")
            self.fixture(root, "b.md", "atom_id: Duplicate")
            self.assert_rejected(root, {})
            (root / "a.md").unlink()
            (root / "b.md").unlink()
            self.fixture(root, "headings.md", "artifact_id: Heading", "## duplicate\none\n## duplicate\ntwo\n")
            self.assert_rejected(root, {})

    def test_secret_values_and_forbidden_carriers_are_never_selected_or_read(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            self.fixture(root, "safe.md", "artifact_id: Safe\nconfig: {nested: {token: not-for-output}}")
            (root / "secret.env").write_bytes(b"this must not be read")
            self.assert_rejected(root, {"select": ["fm:/config"]})
            self.assert_rejected(root, {"select": ["fm:/token"]})
            self.assert_rejected(root, {"mutation": {"write": "forbidden"}})
            self.assert_rejected(root, {"filter": '"fm:/config" = __import__("os")'})
            (root / "secret.md").write_text("unreadable secret carrier", encoding="utf-8")
            self.assert_rejected(root, {})

    def test_root_and_symlink_escape_are_rejected(self):
        with tempfile.TemporaryDirectory() as raw, tempfile.TemporaryDirectory() as outside:
            root = Path(raw)
            self.fixture(root, "safe.md", "artifact_id: Safe")
            self.fixture(Path(outside), "outside.md", "artifact_id: Outside")
            link = root / "escape"
            try:
                os.symlink(outside, link)
            except (NotImplementedError, OSError):
                self.skipTest("symlinks are unavailable")
            self.assert_rejected(root, {})
            self.assert_rejected(root / "absent", {})

    def test_every_resolved_budget_rejects_actual_overage(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            first = self.fixture(root, "a.md", "artifact_id: A\nvalue: 1")
            second = self.fixture(root, "b.md", "artifact_id: B\nvalue: 2")
            self.assert_rejected(root, {}, settings={"max_request_bytes": 1})
            self.assert_rejected(root, {"filter": 'NOT (NOT ("fm:/value" = 1))'}, settings={"max_grammar_depth": 1})
            self.assert_rejected(root, {"filter": '"fm:/value" = 1 OR "fm:/value" = 2'}, settings={"max_filter_tokens": 1})
            self.assert_rejected(root, {"filter": '"fm:/value" IN (1, 2)'}, settings={"max_in_members": 1})
            self.assert_rejected(root, {"select": ["fm:/value", "fm:/missing"]}, settings={"max_selected_fields": 1})
            self.assert_rejected(root, {"limit": 2}, settings={"max_page_size": 1})
            self.assert_rejected(root, {}, settings={"max_snapshot_members": 1})
            self.assert_rejected(root, {}, settings={"max_file_bytes": 1})
            total_limit = first.stat().st_size + second.stat().st_size - 1
            self.assert_rejected(root, {}, settings={"max_file_bytes": 10000, "max_total_read_bytes": total_limit})
            with patch.object(artifact_query.time, "monotonic", side_effect=[0, 2]):
                self.assert_rejected(root, {}, settings={"timeout_seconds": 1})
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "bad-a.md").write_text("not markdown", encoding="utf-8")
            (root / "bad-b.md").write_text("not markdown", encoding="utf-8")
            self.assert_rejected(root, {}, settings={"max_findings": 1})

    def test_parser_contract_remains_shared_and_typed(self):
        tree = parse_filter('NOT ("x" = 1) AND "y" != null')
        self.assertTrue(evaluate_filter(tree, lambda key: {"x": True, "y": "ok"}[key]))
        with self.assertRaises(QueryFilterError):
            parse_filter('"x" = __import__("os")')


if __name__ == "__main__":
    unittest.main()
