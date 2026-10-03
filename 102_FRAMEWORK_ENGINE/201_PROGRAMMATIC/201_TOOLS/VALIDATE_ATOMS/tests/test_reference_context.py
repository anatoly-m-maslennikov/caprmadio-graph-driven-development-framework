"""Reference failures preserve independent checks and never repair carrier values."""

from __future__ import annotations

from copy import deepcopy
import hashlib
from pathlib import Path
import sys
from typing import Any
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from golden_fixtures import fingerprint, isolated_directory  # noqa: E402
from validate_atoms_workers.authority import Obligation, Record, resolve_context  # noqa: E402
from validate_atoms_workers.check_graph_extended import _index, _records  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from validate_atoms_workers.read_io import LimitReached, ReadContext  # noqa: E402
from validate_atoms_workers.reference_context import references  # noqa: E402
from validate_atoms_workers.runtime import execute  # noqa: E402
from validate_atoms_workers.settings import CEILINGS  # noqa: E402


class FailingReferenceReader(ReadContext):
    """Deterministic inaccessible-directory simulation, without host permission changes."""

    def discover(self, roots: list[str]) -> list[Path]:
        if any(Path(root).name == "unavailable-references" for root in roots):
            raise OSError("Reference directory is unavailable")
        return super().discover(roots)


def authority(path: Path, *, legacy: bool = False) -> Record:
    raw = (HERE / "fixtures/authority_checks/CA-D-270.md").read_bytes()
    if legacy:
        # Keep testing missing legacy identity/status even after source migration.
        opening, frontmatter, body = raw.split(b"---", 2)
        frontmatter = b"".join(line for line in frontmatter.splitlines(keepends=True)
                               if not line.startswith((b"atom_id:", b"status:")))
        raw = b"---".join((opening, frontmatter, body))
    parsed = parse_carrier(raw, path)
    return dict(
        binding=dict(
            atom_id="CA-D-270",
            version=parsed.metadata["version"],
            path=str(path),
            sha256=hashlib.sha256(raw).hexdigest(),
        ),
        text=parsed.text,
        metadata=parsed.metadata,
    )


class ReferenceContextRegressionTests(unittest.TestCase):
    def test_bound_identity_enriches_only_reference_copy(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            source = authority(root / "source.md", legacy=True)
            parsed = parse_carrier(source["text"].encode(), Path(source["binding"]["path"]))
            original = dict(
                path=Path(source["binding"]["path"]), metadata=parsed.metadata, parsed=parsed
            )
            original_metadata = deepcopy(parsed.metadata)
            source_snapshot = deepcopy(source)
            reader = ReadContext([str(root)], dict(CEILINGS))
            rows, complete = references(
                {"reference_roots": [str(root)]}, reader, [original], [source]
            )
            self.assertTrue(complete)
            enriched = next(row for row in rows if row["path"] == original["path"])
            self.assertEqual(enriched["metadata"]["atom_id"], "CA-D-270")
            self.assertEqual(enriched["metadata"]["version"], source["binding"]["version"])
            self.assertNotIn("status", enriched["metadata"])
            self.assertIsNot(enriched["metadata"], original["metadata"])
            self.assertEqual(original["metadata"], original_metadata)
            self.assertEqual(parsed.metadata, original_metadata)
            self.assertNotIn("atom_id", parsed.metadata)
            self.assertEqual(source, source_snapshot)
            check = Check(Obligation("test", [], True, "test"), resolve_context([]))
            check.inputs = dict(references=rows, sources=[source])
            self.assertIn("CA-D-270", _index(_records(check)))

    def test_bound_identity_resolves_without_a_selected_candidate(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            source = authority(root / "source.md", legacy=True)
            reader = ReadContext([str(root)], dict(CEILINGS))
            rows, complete = references({"reference_roots": [str(root)]}, reader, [], [source])
            self.assertTrue(complete)
            self.assertEqual(rows[0]["metadata"]["atom_id"], "CA-D-270")
            self.assertNotIn("atom_id", source["metadata"])
            self.assertNotIn("status", rows[0]["metadata"])

    def test_failed_root_retains_other_root_and_existing_context(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            available = root / "references"
            available.mkdir()
            target = available / "target.md"
            target.write_text("---\natom_id: TEST-R-1\nversion: 1\n---\n# Summary\n")
            unavailable = root / "unavailable-references"
            existing: list[Record] = [
                dict(path=root / "candidate.md", metadata={"atom_id": "TEST-R-2"})
            ]
            reader = FailingReferenceReader([str(root)], dict(CEILINGS))
            before = fingerprint(root)
            rows, complete = references(
                {"reference_roots": [str(unavailable), str(available)]}, reader, existing, []
            )
            self.assertFalse(complete)
            self.assertEqual(before, fingerprint(root))
            by_path = {row["path"]: row for row in rows}
            self.assertIsInstance(by_path[unavailable]["parsed"], OSError)
            self.assertEqual(by_path[target]["metadata"]["atom_id"], "TEST-R-1")
            self.assertNotIn(root / "candidate.md", by_path)
            self.assertEqual(reader.read(target), target.read_bytes())

    def test_explicit_frontier_excludes_cached_candidate_but_keeps_original(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            candidates, originals = root / "candidates", root / "originals"
            candidates.mkdir()
            originals.mkdir()
            candidate = candidates / "candidate.md"
            original = originals / "original.md"
            payload = "---\natom_id: TEST-R-1\nversion: 1\n---\n# Summary\n"
            candidate.write_text(payload)
            original.write_text(payload)
            cached = dict(
                path=candidate,
                metadata={"atom_id": "TEST-R-1", "version": 1},
                parsed=parse_carrier(payload.encode(), candidate),
            )
            rows, complete = references(
                {"reference_roots": [str(originals)]},
                ReadContext([str(root)], dict(CEILINGS)),
                [cached],
                [],
            )
            self.assertTrue(complete)
            self.assertEqual([row["path"] for row in rows], [original])

    def test_explicit_frontier_reuses_cached_row_only_when_its_path_is_admitted(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            references_root = root / "references"
            references_root.mkdir()
            target = references_root / "target.md"
            payload = "---\natom_id: TEST-R-1\nversion: 1\n---\n# Summary\n"
            target.write_text(payload)
            cached = dict(
                path=target,
                metadata={"atom_id": "TEST-R-1", "version": 1, "cached": True},
                parsed=parse_carrier(payload.encode(), target),
            )
            reader = ReadContext([str(root)], dict(CEILINGS))
            rows, complete = references(
                {"reference_roots": [str(references_root)]}, reader, [cached], []
            )
            self.assertTrue(complete)
            self.assertEqual(rows[0]["metadata"], cached["metadata"])
            self.assertNotIn(str(target), reader.fingerprints)

    def test_explicit_frontier_retains_genuine_duplicate_revisions_at_distinct_paths(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            references_root = root / "references"
            references_root.mkdir()
            payload = "---\natom_id: TEST-R-1\nversion: 1\n---\n# Summary\n"
            first, second = references_root / "first.md", references_root / "second.md"
            first.write_text(payload)
            second.write_text(payload)
            rows, complete = references(
                {"reference_roots": [str(references_root)]},
                ReadContext([str(root)], dict(CEILINGS)),
                [],
                [],
            )
            self.assertTrue(complete)
            self.assertEqual([row["path"] for row in rows], [first, second])
            self.assertEqual(
                [row["metadata"] for row in rows],
                [{"atom_id": "TEST-R-1", "version": 1}] * 2,
            )

    def test_omitted_roots_keep_cached_context_but_mark_it_incomplete(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            candidate = root / "candidate.md"
            cached = dict(path=candidate, metadata={"atom_id": "TEST-R-1", "version": 1})
            rows, complete = references(
                {}, ReadContext([str(root)], dict(CEILINGS)), [cached], []
            )
            self.assertFalse(complete)
            self.assertEqual(rows, [cached])

    def test_reference_budget_exhaustion_is_not_swallowed(self) -> None:
        class ExhaustedReader(ReadContext):
            def discover(self, roots: list[str]) -> list[Path]:
                raise LimitReached("max_candidates")

        with isolated_directory() as directory:
            reader = ExhaustedReader([directory], dict(CEILINGS))
            with self.assertRaises(LimitReached):
                references({"reference_roots": [directory]}, reader, [], [])

    def test_nonexistent_directory_is_not_a_complete_empty_inventory(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            reader = ReadContext([directory], dict(CEILINGS))
            rows, complete = references(
                {"reference_roots": [str(root / "missing")]}, reader, [], []
            )
            self.assertFalse(complete)
            self.assertIsInstance(rows[0]["parsed"], OSError)

    def test_reference_candidate_limit_applies_across_roots(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            paths = [root / "one.md", root / "two.md"]
            for path in paths:
                path.write_text("---\nversion: 1\n---\n# Summary\n")
            reader = ReadContext([directory], {**CEILINGS, "max_candidates": 1})
            with self.assertRaises(LimitReached):
                references({"reference_roots": [str(path) for path in paths]}, reader, [], [])

    def test_failed_reference_root_still_checks_good_and_bad_selected_carriers(self) -> None:
        with isolated_directory() as directory:
            root = Path(directory)
            atoms, methodology = root / "atoms", root / "methodology"
            atoms.mkdir()
            methodology.mkdir()
            source = authority(methodology / "CA-D-270.md")
            Path(source["binding"]["path"]).write_text(source["text"])
            good, bad = atoms / "good.md", atoms / "bad.md"
            good.write_text(
                '---\natom_id: TEST-R-1\nversion: 1\nupdated_at: "2026-09-24T00:00:00Z"\n---\n# Summary\nGood\n'
            )
            bad.write_text(
                '---\natom_id: TEST-R-2\nversion: false\nupdated_at: "2026-09-24T00:00:00Z"\n---\n# Summary\nBad\n'
            )
            request: dict[str, Any] = dict(
                schema_version=1,
                source_roots=[str(atoms)],
                allowed_read_roots=[str(root)],
                methodology=dict(
                    kind="sources", roots=[str(methodology)], frontier=[source["binding"]]
                ),
                selection=dict(atoms=[{"carrier_path": str(good)}, {"carrier_path": str(bad)}]),
                reference_roots=[str(root / "unavailable-references")],
                limits=dict(CEILINGS),
            )
            before = fingerprint(root)
            with patch("validate_atoms_workers.runtime.ReadContext", FailingReferenceReader):
                report = execute(request)
            self.assertEqual(before, fingerprint(root))
            self.assertEqual(report["result"], "incomplete")
            self.assertEqual(report["selection"]["selected"], sorted((str(good), str(bad))))
            self.assertEqual(report["coverage"]["targets"]["assessed"], 2)
            self.assertFalse(report["execution"]["diagnostics"])
            self.assertIn(
                "REFERENCE_CONTEXT_INCOMPLETE", {gap["code"] for gap in report["coverage"]["gaps"]}
            )
            outcomes = {
                carrier["path"]: next(
                    outcome
                    for outcome in carrier["outcomes"]
                    if outcome["code"] == "frontmatter.version"
                )
                for carrier in report["carriers"]
            }
            self.assertEqual(outcomes[str(good)]["outcome"], "passed")
            self.assertEqual(outcomes[str(bad)]["outcome"], "failed")
            self.assertTrue(
                any(
                    finding["path"] == str(bad) and finding["code"] == "PROPERTY_TYPE"
                    for finding in report["findings"]
                )
            )


if __name__ == "__main__":
    unittest.main()
