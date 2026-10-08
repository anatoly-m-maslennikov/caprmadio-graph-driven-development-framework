"""Read-only D572 admission for the closed unknown-effect resolver authority."""
from __future__ import annotations

import copy
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
AUTHORITY_REF = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/07_delivery/CA-D-572-TOOLS-DELIVERY--serialize-additive-release-route-source-admission.md"
)
UNKNOWN_SECTION = re.compile(
    r"^## Unknown-effect resolver authority\n+```json\n(.*?)\n```$", re.MULTILINE | re.DOTALL,
)
PRIVATE_SECTION = re.compile(
    r"^## Private implementation carriers\n+```json\n(.*?)\n```$", re.MULTILINE | re.DOTALL,
)
sys.path.insert(0, str(MCP))

import release_source_admission as admission_module  # noqa: E402
from release_source_admission import ReleaseSourceAdmissionError  # noqa: E402


def authority_pin(raw: bytes) -> dict[str, object]:
    match = re.search(r"^atom_id:\s*(CA-D-572)\s*$.*?^version:\s*(\d+)\s*$", raw.decode("utf-8"), re.MULTILINE | re.DOTALL)
    if match is None:
        raise AssertionError("D572 source identity/version frontmatter is unavailable")
    return {
        "atom_id": match[1], "version": int(match[2]), "source_path": AUTHORITY_REF,
        "digest": hashlib.sha256(raw).hexdigest(),
    }


def json_section(pattern: re.Pattern[str], raw: bytes, *, label: str) -> list[dict[str, object]]:
    match = pattern.search(raw.decode("utf-8"))
    if match is None:
        raise AssertionError(f"D572 {label} JSON section is unavailable")
    payload = json.loads(match[1])
    if not isinstance(payload, list):
        raise AssertionError(f"D572 {label} is not a pin list")
    return payload


class UnknownResolverReaderAPITests(unittest.TestCase):
    def test_reader_exists_before_final_source_bytes_arrive(self) -> None:
        self.assertTrue(callable(getattr(admission_module, "derive_unknown_effect_resolver_authority", None)))


class UnknownResolverSourceAdmissionTests(unittest.TestCase):
    """The reader has no public manifest field and cannot affect Release admission."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.authority_raw = (REPOSITORY / AUTHORITY_REF).read_bytes()
        if UNKNOWN_SECTION.search(cls.authority_raw.decode("utf-8")) is None:
            raise unittest.SkipTest("waiting for D572 unknown-effect resolver authority source bytes")
        cls.expected = json_section(UNKNOWN_SECTION, cls.authority_raw, label="unknown-effect resolver authority")
        cls.private_carriers = json_section(PRIVATE_SECTION, cls.authority_raw, label="private carriers")
        cls.release_frontier = [admission_module._table_pin(row) for row in admission_module._tables(
            cls.authority_raw.decode("utf-8"))[2][2:]]
        cls.asserted_ids = ["CA-R-1895", "CA-M-351", "CA-E-594", "CA-D-589"]
        if [row.get("atom_id") for row in cls.expected] != cls.asserted_ids:
            raise AssertionError("D572 unknown-effect resolver authority order is not the closed R/M/E/D set")

    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/unknown-resolver-source-admission"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for relative in {AUTHORITY_REF, *[row["source_path"] for row in self.expected],
                         *[row["source_path"] for row in self.private_carriers]}:
            source, target = REPOSITORY / relative, self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    @contextmanager
    def trusted_authority(self, raw: bytes):
        authority = self.root / AUTHORITY_REF
        original = authority.read_bytes()
        try:
            authority.write_bytes(raw)
            with patch.object(admission_module, "AUTHORITY_PIN", authority_pin(raw)):
                yield
        finally:
            authority.write_bytes(original)

    def derive(self) -> list[dict[str, object]]:
        reader = getattr(admission_module, "derive_unknown_effect_resolver_authority", None)
        self.assertTrue(callable(reader), "missing pure unknown-effect resolver authority reader")
        return reader(self.root)

    def test_current_d572_derives_the_closed_ordered_resolver_pins_without_release_frontier_change(self) -> None:
        before = (self.root / AUTHORITY_REF).read_bytes()
        resolved = self.derive()
        self.assertEqual(self.expected, resolved)
        self.assertEqual(self.asserted_ids, [row["atom_id"] for row in resolved])
        self.assertEqual(self.release_frontier, [admission_module._table_pin(row) for row in admission_module._tables(
            (self.root / AUTHORITY_REF).read_text(encoding="utf-8"))[2][2:]])
        self.assertEqual(before, (self.root / AUTHORITY_REF).read_bytes())

    def test_absent_extra_and_reordered_resolver_authority_refuse(self) -> None:
        raw = (self.root / AUTHORITY_REF).read_bytes()
        match = UNKNOWN_SECTION.search(raw.decode("utf-8"))
        self.assertIsNotNone(match)
        variants = (
            UNKNOWN_SECTION.sub("", raw.decode("utf-8")),
            UNKNOWN_SECTION.sub(lambda found: found.group(0).replace(match.group(1), json.dumps([*self.expected, self.expected[-1]])), raw.decode("utf-8")),
            UNKNOWN_SECTION.sub(lambda found: found.group(0).replace(match.group(1), json.dumps(list(reversed(self.expected)))), raw.decode("utf-8")),
        )
        for altered in variants:
            with self.subTest(altered=altered[:80]):
                with self.trusted_authority(altered.encode("utf-8")):
                    with self.assertRaises(ReleaseSourceAdmissionError):
                        self.derive()

    def test_each_resolver_pin_stale_refuses_without_release_frontier_change(self) -> None:
        authority_before = (self.root / AUTHORITY_REF).read_bytes()
        for pin in self.expected:
            with self.subTest(atom_id=pin["atom_id"]):
                path = self.root / pin["source_path"]
                original = path.read_bytes()
                try:
                    path.write_bytes(original + b"\nfixture-stale\n")
                    with self.assertRaises(ReleaseSourceAdmissionError):
                        self.derive()
                finally:
                    path.write_bytes(original)
        self.assertEqual(authority_before, (self.root / AUTHORITY_REF).read_bytes())


if __name__ == "__main__":
    unittest.main()
