"""Small regression tests for untrusted carriers and read boundaries."""

from pathlib import Path
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
# The standalone Tool root must be importable before loading its public test subjects.
from validate_atoms_workers.parsing import CarrierError, parse_carrier  # noqa: E402
from validate_atoms_workers.read_io import ReadContext, ReadFailure, LimitReached  # noqa: E402


class CarrierTests(unittest.TestCase):
    def test_valid_and_no_identity_inference(self) -> None:
        parsed = parse_carrier(b"---\nstatus: Active\n---\n# Summary\n\nHi\n", Path("/CA-R-001.md"))
        self.assertEqual(parsed.metadata, {"status": "Active"})
        self.assertNotIn("atom_id", parsed.metadata)

    def test_duplicate_nested_key(self) -> None:
        with self.assertRaises(CarrierError):
            parse_carrier(b"---\nsubjects: {governs: A, governs: B}\n---\nx", Path("/a.md"))

    def test_unsafe_tag(self) -> None:
        with self.assertRaises(CarrierError):
            parse_carrier(
                b'---\nx: !!python/object/apply:os.system ["exit 0"]\n---\nx', Path("/a.md")
            )

    def test_alias_is_explicitly_unsupported(self) -> None:
        with self.assertRaises(CarrierError) as caught:
            parse_carrier(b"---\na: &a [*a]\n---\nx", Path("/a.md"))
        self.assertEqual(caught.exception.code, "YAML_UNSUPPORTED")

    def test_invalid_utf8(self) -> None:
        with self.assertRaises(CarrierError):
            parse_carrier(b"\xff", Path("/a.md"))

    def test_deep_yaml_is_bounded(self) -> None:
        data = b"---\nx: " + b"[" * 100 + b"0" + b"]" * 100 + b"\n---\nx"
        with self.assertRaises(CarrierError):
            parse_carrier(data, Path("/a.md"))


class ReadTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = HERE.parents[4] / ".caprmedio_tmp"
        parent.mkdir(exist_ok=True)
        self.root = Path(tempfile.mkdtemp(dir=parent, prefix="validator-input-test-"))
        self.limits = dict(
            max_candidates=10,
            max_file_bytes=20,
            max_total_read_bytes=40,
            timeout_seconds=30,
            max_findings=100,
        )
        self.reader = ReadContext([str(self.root)], self.limits)

    def test_denied_secret_without_content_read(self) -> None:
        with self.assertRaises(ReadFailure):
            self.reader.read(self.root / ".env")
        self.assertEqual(self.reader.bytes_read, 0)

    def test_outside_root(self) -> None:
        with self.assertRaises(ReadFailure):
            self.reader.read(Path("/etc/hosts"))

    def test_budget_and_currentness(self) -> None:
        path = self.root / "a.md"
        path.write_bytes(b"original")
        self.reader.read(path)
        path.write_bytes(b"changed")
        self.assertEqual(self.reader.currentness()["state"], "changed")
        path.write_bytes(b"x" * 21)
        with self.assertRaises(LimitReached):
            self.reader.read(path)

    def test_symlink_escape(self) -> None:
        path = self.root / "outside.md"
        path.symlink_to("/etc/hosts")
        with self.assertRaises(ReadFailure):
            self.reader.read(path)


if __name__ == "__main__":
    unittest.main()
