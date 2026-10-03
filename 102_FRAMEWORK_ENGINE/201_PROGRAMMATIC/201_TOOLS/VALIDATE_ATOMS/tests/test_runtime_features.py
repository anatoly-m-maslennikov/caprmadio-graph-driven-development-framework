"""Settings, projections and mutable-input regression tests."""

from pathlib import Path
import hashlib
import json
import sys
import tempfile
from typing import Any
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from validate_atoms_workers.projection import verify_projection  # noqa: E402
from validate_atoms_workers.read_io import LimitReached, ReadContext  # noqa: E402
from validate_atoms_workers.settings import CEILINGS, resolve_limits  # noqa: E402
from validate_atoms_workers.runtime import execute  # noqa: E402


class RuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(
            tempfile.mkdtemp(dir=HERE.parents[4] / ".caprmedio_tmp", prefix="validator-runtime-")
        )
        self.reader = ReadContext([str(self.root)], dict(CEILINGS))

    def test_independent_limit_fallbacks(self) -> None:
        defaults = self.root / "defaults.toml"
        defaults.write_text(
            "[atom_validation]\nmax_candidates=10\nmax_file_bytes=10000\n"
            "max_total_read_bytes=100000\ntimeout_seconds=30\nmax_findings=30\n"
        )
        instance = self.root / "instance.toml"
        instance.write_text("[atom_validation]\nmax_findings=12\n")
        values, origins = resolve_limits(
            dict(
                limits={"max_candidates": 5},
                default_settings={"path": str(defaults)},
                framework_settings={"path": str(instance)},
            ),
            self.reader,
        )
        self.assertEqual(values["max_candidates"], 5)
        self.assertEqual(origins["max_candidates"], "request")
        self.assertEqual(values["max_findings"], 12)
        self.assertEqual(origins["max_findings"], "instance")
        self.assertEqual(origins["max_file_bytes"], "default")

    def test_bad_setting_never_falls_back(self) -> None:
        settings = self.root / "settings.toml"
        settings.write_text("[atom_validation]\nmax_candidates=true\n")
        with self.assertRaises(ValueError):
            resolve_limits(
                dict(limits=dict(CEILINGS), framework_settings={"path": str(settings)}), self.reader
            )

    def test_stale_settings_binding(self) -> None:
        settings = self.root / "settings.toml"
        settings.write_text("[atom_validation]\n")
        with self.assertRaises(ValueError):
            resolve_limits(
                dict(default_settings={"path": str(settings), "sha256": "0" * 64}), self.reader
            )

    def test_membership_changes(self) -> None:
        self.reader.inventory(self.root)
        (self.root / "new.md").write_text("x")
        current = self.reader.currentness()
        self.assertEqual(current["state"], "changed")
        self.assertEqual(current["affected_inputs"], [{"path": str(self.root)}])

    def test_currentness_reads_count_toward_budget(self) -> None:
        path = self.root / "a.md"
        path.write_bytes(b"12345")
        self.reader.limits["max_total_read_bytes"] = 9
        self.reader.read(path)
        with self.assertRaises(LimitReached) as caught:
            self.reader.currentness()
        self.assertEqual(caught.exception.limit, "max_total_read_bytes")

    def test_projection_exact_bytes_and_changed_bytes(self) -> None:
        source = self.root / "source.md"
        original = b"---\natom_id: TEST-R-1\n---\n# Summary\n\nOne\n"
        source.write_bytes(original)
        projected = original.replace(
            b"atom_id:", b"projection:\n  source_carrier_path: source.md\natom_id:"
        )
        path = self.root / "projected.md"
        assessment: dict[str, Any] = {}
        self.assertIsNone(
            verify_projection(parse_carrier(projected, path), path, self.reader, assessment)
        )
        self.assertEqual(assessment["representation"], "projected")
        bad = projected.replace(b"One", b"Two")
        failure = verify_projection(parse_carrier(bad, path), path, self.reader, {})
        self.assertIsNotNone(failure)
        self.assertEqual(failure["code"], "PROJECTION_FIDELITY")  # type: ignore[index]

    def test_source_fingerprints_are_real_bytes(self) -> None:
        path = self.root / "a.md"
        raw = b"\r\nnot-normalized\r\n"
        path.write_bytes(raw)
        self.reader.read(path)
        self.assertEqual(self.reader.fingerprints[str(path)], hashlib.sha256(raw).hexdigest())

    def test_runtime_limits_fail_closed(self) -> None:
        request = dict(
            source_roots=[str(self.root)],
            allowed_read_roots=[str(self.root)],
            methodology={"kind": "sources", "roots": [str(self.root)]},
            selection={"atoms": [{"atom_id": "UNKNOWN"}]},
            limits={"max_candidates": 1},
        )
        report = execute(request)
        self.assertEqual(report["result"], "error")
        self.assertEqual(report["execution"]["diagnostics"][0]["code"], "SETTINGS_INVALID")
        json.dumps(report, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
