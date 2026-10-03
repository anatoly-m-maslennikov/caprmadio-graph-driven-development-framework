"""Independent golden fixtures and real-command tests for retired-field removal."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "remove_retired_atom_properties.py"
REPO = SCRIPT.parents[4]


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


class TransformationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        spec = importlib.util.spec_from_file_location("retired_fixer_under_test", SCRIPT)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        cls.transform = staticmethod(module.remove_retired_properties)

    def test_three_fields_golden_bytes(self) -> None:
        before = (
            b"---\natom_id: CA-R-1\ncce_version: cce_1\ncce_form: obligation\n"
            b"llm_session_ids:\n  - codex:example\n  - claude:other\n"
            b'version: 3\nupdated_at: "2026-09-25T00:00:00Z"\n'
            b"subjects: {governs: Atom}\n---\n# Summary\n\nExample\n\n## Claim\n\nKeep this.\n"
        )
        expected = (
            b"---\natom_id: CA-R-1\n"
            b'version: 3\nupdated_at: "2026-09-25T00:00:00Z"\n'
            b"subjects: {governs: Atom}\n---\n# Summary\n\nExample\n\n## Claim\n\nKeep this.\n"
        )
        actual, removed = self.transform(before)
        self.assertEqual(actual, expected)
        self.assertCountEqual(removed, ["cce_version", "cce_form", "llm_session_ids"])
        self.assertEqual(self.transform(actual), (expected, []))

    def test_clean_atom_is_byte_identical(self) -> None:
        raw = b"---\nversion: 1\nrelations: {}\n---\n# Keep original title\n"
        self.assertEqual(self.transform(raw), (raw, []))

    def test_nested_keys_and_body_are_not_removed(self) -> None:
        raw = (
            b"---\nversion: 1\nmetadata:\n  cce_form: leave\n"
            b"  llm_session_ids: [leave]\n---\n## Claim\ncce_version: leave\n"
        )
        self.assertEqual(self.transform(raw), (raw, []))

    def test_quoted_key_and_unicode_and_crlf(self) -> None:
        raw = '---\r\n"cce_form": obligation\r\nversion: 2\r\n---\r\n# Кратко\r\n'.encode()
        expected = '---\r\nversion: 2\r\n---\r\n# Кратко\r\n'.encode()
        self.assertEqual(self.transform(raw), (expected, ["cce_form"]))

    def test_flow_value_and_block_value(self) -> None:
        raw = (
            b"---\nllm_session_ids: [one, two]\ncce_form: |\n"
            b"  old description\n  next line\nversion: 2\n---\nBody"
        )
        actual, removed = self.transform(raw)
        self.assertEqual(actual, b"---\nversion: 2\n---\nBody")
        self.assertCountEqual(removed, ["llm_session_ids", "cce_form"])

    def test_indentless_sequence(self) -> None:
        raw = b"---\nversion: 1\nllm_session_ids:\n- one\n- two\nstatus: Active\n---\nBody\n"
        expected = b"---\nversion: 1\nstatus: Active\n---\nBody\n"
        self.assertEqual(self.transform(raw), (expected, ["llm_session_ids"]))

    def test_comments_on_retained_properties_preserved(self) -> None:
        raw = b"---\ncce_form: old # remove\n# version comment\nversion: 4 # keep\n---\nBody\n"
        expected = b"---\n# version comment\nversion: 4 # keep\n---\nBody\n"
        self.assertEqual(self.transform(raw), (expected, ["cce_form"]))

    def test_frontmatter_like_text_in_body_preserved(self) -> None:
        raw = b"---\ncce_form: old\nversion: 1\n---\n```yaml\ncce_form: example\n---\n```\n"
        expected = b"---\nversion: 1\n---\n```yaml\ncce_form: example\n---\n```\n"
        self.assertEqual(self.transform(raw), (expected, ["cce_form"]))

    def test_malformed_and_ambiguous_inputs_fail_closed(self) -> None:
        cases = [
            b"not frontmatter",
            b"---\ncce_form: old\nversion: [\n---\nBody\n",
            b"---\ncce_form: a\ncce_form: b\nversion: 1\n---\nBody\n",
            b"---\nversion: 1\nversion: 2\n---\nBody\n",
            b"---\ncce_form: &old abc\nversion: *old\n---\nBody\n",
            b"---\n{cce_form: old, version: 1}\n---\nBody\n",
            b"---\n? cce_form\n: old\nversion: 1\n---\nBody\n",
            b"---\nx: !!python/object/apply:os.system [echo unsafe]\n---\nBody\n",
            b"---\ncce_form: old\nversion: 1\n---\n\xff",
        ]
        for raw in cases:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                self.transform(raw)


class CommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not SCRIPT.is_file():
            raise AssertionError("Fixer executable is missing; refusal tests cannot count as passes")

    def setUp(self) -> None:
        root = REPO / ".caprmedio_tmp"
        root.mkdir(exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="retired-fixer-test-", dir=root))
        self.source = self.root / "sources"
        self.source.mkdir()
        self.atom = self.source / "atom.md"
        self.before = b"---\ncce_form: old\nversion: 2\n---\n# Summary\n\nSame claim\n"
        self.after = b"---\nversion: 3\n---\n# Summary\n\nSame claim\n"
        self.atom.write_bytes(self.before)
        self.report = self.root / "report.json"
        self.plan = self.root / "plan.json"
        self.receipt = self.root / "receipt.json"

    def write_report(self, paths: list[Path] | None = None) -> None:
        paths = paths or [self.atom]
        value = {
            "findings": [
                {"code": "PROPERTY_RETIRED", "property": "cce_form", "path": str(path)}
                for path in paths
            ],
            "carriers": [{"path": str(path), "sha256": digest(path.read_bytes())} for path in paths],
        }
        self.report.write_text(json.dumps(value))

    def call(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)

    def preview(self) -> subprocess.CompletedProcess[str]:
        return self.call("--report", str(self.report), "--source-root", str(self.source), "--output", str(self.plan))

    def test_real_cli_preview_apply_and_idempotency(self) -> None:
        self.write_report()
        preview = self.preview()
        self.assertEqual(preview.returncode, 0, preview.stderr + preview.stdout)
        self.assertEqual(self.atom.read_bytes(), self.before)
        plan = json.loads(self.plan.read_text())
        self.assertEqual(len(plan["changes"]), 1)
        self.assertEqual(plan["changes"][0]["before_sha256"], digest(self.before))
        applied = self.call("--apply", str(self.plan), "--output", str(self.receipt))
        self.assertEqual(applied.returncode, 0, applied.stderr + applied.stdout)
        self.assertEqual(self.atom.read_bytes(), self.after)
        self.assertEqual((self.source / "archive" / "atom@2.md").read_bytes(), self.before)
        repeated = self.call("--apply", str(self.plan))
        self.assertEqual(repeated.returncode, 0, repeated.stderr + repeated.stdout)
        self.assertEqual(self.atom.read_bytes(), self.after)

    def test_stale_report_does_not_modify_sources(self) -> None:
        self.write_report()
        changed = self.before.replace(b"old", b"new")
        self.atom.write_bytes(changed)
        result = self.preview()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.atom.read_bytes(), changed)

    def test_stale_plan_aborts_entire_batch(self) -> None:
        second = self.source / "second.md"
        second.write_bytes(self.before)
        self.write_report([self.atom, second])
        preview = self.preview()
        self.assertEqual(preview.returncode, 0, preview.stderr + preview.stdout)
        changed = self.before.replace(b"old", b"changed")
        second.write_bytes(changed)
        result = self.call("--apply", str(self.plan))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.atom.read_bytes(), self.before)
        self.assertEqual(second.read_bytes(), changed)

    def test_conflicting_archive_is_not_overwritten(self) -> None:
        self.write_report()
        archived = self.source / "archive" / "atom@2.md"
        archived.parent.mkdir()
        archived.write_bytes(b"unrelated preserved history")
        result = self.preview()
        if result.returncode == 0:
            result = self.call("--apply", str(self.plan))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.atom.read_bytes(), self.before)
        self.assertEqual(archived.read_bytes(), b"unrelated preserved history")

    def test_matching_archive_can_be_reused(self) -> None:
        self.write_report()
        archived = self.source / "archive" / "atom@2.md"
        archived.parent.mkdir()
        archived.write_bytes(self.before)
        preview = self.preview()
        self.assertEqual(preview.returncode, 0, preview.stderr + preview.stdout)
        result = self.call("--apply", str(self.plan))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertEqual(self.atom.read_bytes(), self.after)
        self.assertEqual(archived.read_bytes(), self.before)

    def test_path_outside_source_root_rejected(self) -> None:
        outside = self.root / "outside.md"
        outside.write_bytes(self.before)
        self.write_report([outside])
        self.assertNotEqual(self.preview().returncode, 0)
        self.assertEqual(outside.read_bytes(), self.before)

    def test_symlink_rejected(self) -> None:
        linked = self.source / "linked.md"
        linked.symlink_to(self.atom)
        self.write_report([linked])
        self.assertNotEqual(self.preview().returncode, 0)
        self.assertEqual(self.atom.read_bytes(), self.before)

    def test_archived_file_rejected(self) -> None:
        archived = self.source / "archive" / "old@1.md"
        archived.parent.mkdir()
        archived.write_bytes(self.before)
        self.write_report([archived])
        self.assertNotEqual(self.preview().returncode, 0)
        self.assertEqual(archived.read_bytes(), self.before)

    def test_tampered_plan_cannot_change_claim(self) -> None:
        self.write_report()
        self.assertEqual(self.preview().returncode, 0)
        plan = json.loads(self.plan.read_text())
        plan["changes"][0]["after"] = self.after.replace(b"Same claim", b"Different claim").decode()
        plan["changes"][0]["after_sha256"] = digest(plan["changes"][0]["after"].encode())
        self.plan.write_text(json.dumps(plan))
        self.assertNotEqual(self.call("--apply", str(self.plan)).returncode, 0)
        self.assertEqual(self.atom.read_bytes(), self.before)

    def test_existing_receipt_path_aborts_before_changes(self) -> None:
        self.write_report()
        self.assertEqual(self.preview().returncode, 0)
        self.receipt.write_bytes(b"preserved receipt")
        result = self.call("--apply", str(self.plan), "--output", str(self.receipt))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.atom.read_bytes(), self.before)
        self.assertEqual(self.receipt.read_bytes(), b"preserved receipt")

    def test_apply_preserves_source_permissions(self) -> None:
        self.atom.chmod(0o640)
        self.write_report()
        self.assertEqual(self.preview().returncode, 0)
        result = self.call("--apply", str(self.plan))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertEqual(self.atom.stat().st_mode & 0o777, 0o640)


if __name__ == "__main__":
    unittest.main()
