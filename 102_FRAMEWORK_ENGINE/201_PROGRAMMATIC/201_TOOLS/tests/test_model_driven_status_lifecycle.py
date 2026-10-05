"""Real-source golden native effects; not MCP, queue or immutable-image proof."""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
REPOSITORY = TOOLS.parents[2]
CONTROL = Path(".caprmedio_caprmedio")
SOURCE = CONTROL / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"
sys.path.insert(0, str(TOOLS))

from atom_operations import atom_from_path, frontmatter_scalar, ToolError  # noqa: E402
from authoritative_status_models import resolve_status_model, StatusModelError  # noqa: E402
import lifecycle_intents  # noqa: E402
from lifecycle_intents import carrier_descriptor, change_status_atom_action, LifecycleError, preflight_atom_lifecycle  # noqa: E402


DOMAINS = (
    ("Requirement", "R", "04_requirement", "CA-R-1309", ("Draft", "Active", "Archived")),
    ("Method", "M", "05_method", "CA-R-1397", ("Draft", "Active", "Archived")),
    ("Evaluation", "E", "06_evaluation", "CA-R-1398", ("Draft", "Active", "Archived")),
    ("Delivery", "D", "07_delivery", "CA-R-1399", ("Draft", "Active", "Archived")),
    ("Plan", "P", "03_plan", "CA-R-1539", ("Active", "Backlog", "Done", "Canceled", "Archived")),
    ("Concern", "C", "01_concern", "CA-R-1608", ("draft", "active", "resolved", "canceled")),
    ("Operations", "O", "09_operations", "CA-R-1874", ("Draft", "Active", "Archived")),
    ("Analysis", "A", "02_analysis", "CA-R-1875", ("Draft", "Done", "Archived")),
)
AUTHORITY_IDS = tuple(row[3] for row in DOMAINS) + (
    "CA-R-1308", "CA-R-1521", "CA-R-1312", "CA-R-1311", "CA-R-1419",
    "CA-D-461", "CA-D-466", "CA-D-565", "CA-D-289", "CA-D-434",
    "CA-D-446", "CA-D-288", "CA-D-483", "CA-D-324",
)


class ModelDrivenStatusLifecycleTest(unittest.TestCase):
    """Only fresh disposable Projects are writable by these native invocations."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.authority_paths: dict[str, Path] = {}
        for path in (REPOSITORY / SOURCE).rglob("*.md"):
            if "archive" in path.parts or "archived" in path.parts:
                continue
            match = re.match(r"^(CA-[A-Z]+-\d+)-", path.name)
            if match and match[1] in AUTHORITY_IDS:
                if match[1] in cls.authority_paths:
                    raise AssertionError(f"current authority is ambiguous: {match[1]}")
                cls.authority_paths[match[1]] = path
        if set(cls.authority_paths) != set(AUTHORITY_IDS):
            raise AssertionError(f"missing current authorities: {set(AUTHORITY_IDS) - set(cls.authority_paths)}")

    def setUp(self) -> None:
        temporary_root = REPOSITORY / ".caprmedio_tmp/tests/model-driven-status-lifecycle"
        temporary_root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary_root, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        control = self.root / CONTROL
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n', encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            '[[scope_units]]\nscope_unit_name = "METHODOLOGY_SOURCES"\n'
            f'authority_path = "{SOURCE.as_posix()}"\n', encoding="utf-8",
        )
        self.sources: dict[str, Path] = {}
        for atom_id in AUTHORITY_IDS:
            source = self.authority_paths[atom_id]
            destination = self.root / source.relative_to(REPOSITORY)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            self.assertEqual(source.read_bytes(), destination.read_bytes())
            self.sources[atom_id] = destination

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def snapshot(self) -> dict[str, str | None]:
        return {path.relative_to(self.root).as_posix():
                hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
                for path in self.root.rglob("*")}

    def atom(self, role: str, status: str, *, number: int = 8000,
             atom_type: str | None = None, container: str | None = None,
             relations: str = "relations: {}", draft: bool = False) -> Path:
        row = next(row for row in DOMAINS if row[0] == role)
        _, letter, directory, _, _ = row
        folder = self.root / CONTROL / "fixture" / directory
        if container:
            folder /= container
        if status in {"Draft", "draft"}:
            folder /= "draft"
        elif role == "Plan" and status == "Backlog":
            folder /= "001_backlog"
        elif status != "Active":
            folder /= status.lower()
        folder.mkdir(parents=True, exist_ok=True)
        name = f"CA-{letter}--golden.md" if draft else f"CA-{letter}-{number}--golden.md"
        path = folder / name
        identity = "" if draft else f"atom_id: CA-{letter}-{number}\n"
        type_value = f"type: {atom_type}\n" if atom_type else ""
        path.write_text(
            f"---\n{identity}content_role: {role}\n{type_value}status: {status}\n"
            "version: 3\nupdated_at: 2026-01-01 00:00:00 +0000\n"
            f"{relations}\n---\n# Summary\n\nGolden immutable meaning\n\n"
            "## Details\n\nThe whole body must survive the status transition.\n",
            encoding="utf-8",
        )
        return path

    def request(self, path: Path, status: str) -> dict[str, object]:
        actual = atom_from_path(self.root, path)
        return {"target": carrier_descriptor(self.root, actual), "status": status}

    def execute(self, request: dict[str, object]) -> dict[str, object]:
        return change_status_atom_action(self.root, request, execute=True, authorized=True)

    def assert_model(self, result: dict[str, object], request: dict[str, object]) -> None:
        expected = resolve_status_model(self.root, request["target"], request["status"])
        self.assertEqual(expected, result["status_model"])
        for pin in expected["model_sources"]:
            actual = self.root / pin["path"]
            self.assertEqual(pin["sha256"], hashlib.sha256(actual.read_bytes()).hexdigest())
            self.assertEqual(str(pin["revision"]), frontmatter_scalar(actual.read_text().split("\n---\n", 1)[0][4:], "version"))

    def assert_no_effect(self, result: dict[str, object]) -> None:
        self.assertFalse(any(effect["state"] != "unchanged" for effect in result["effects"]))
        if "effect_refs" in result:
            self.assertEqual([], result["effect_refs"])

    def test_actual_eight_role_domains_and_exact_source_pins(self) -> None:
        for role, _, _, source_id, statuses in DOMAINS:
            with self.subTest(role=role):
                atom_type = {"Operations": "Action", "Analysis": "Analysis Report", "Plan": "Task"}.get(role)
                path = self.atom(role, "active" if role == "Concern" else "Done" if role == "Analysis" else "Active",
                                 atom_type=atom_type)
                actual = atom_from_path(self.root, path)
                for status in statuses:
                    model = resolve_status_model(self.root, actual, status)
                    self.assertEqual(list(statuses), model["statuses"])
                    self.assertEqual(source_id, model["model_sources"][0]["atom_id"])
                    self.assertEqual(hashlib.sha256(self.sources[source_id].read_bytes()).hexdigest(),
                                     model["model_sources"][0]["sha256"])
                with self.assertRaises(StatusModelError):
                    resolve_status_model(self.root, actual, statuses[0].swapcase())

    def test_actual_typed_atoms_use_role_fallback(self) -> None:
        for role, atom_type, status, source_id in (
            ("Operations", "Action", "Active", "CA-R-1874"),
            ("Operations", "Workflow", "Active", "CA-R-1874"),
            ("Analysis", "Rationale", "Done", "CA-R-1875"),
            ("Plan", "Task", "Active", "CA-R-1539"),
            ("Plan", "EPIC", "Active", "CA-R-1539"),
        ):
            with self.subTest(role=role, atom_type=atom_type):
                path = self.atom(role, status, atom_type=atom_type)
                model = resolve_status_model(self.root, atom_from_path(self.root, path), status)
                self.assertEqual(atom_type, model["type"])
                self.assertEqual(source_id, model["model_sources"][0]["atom_id"])

    def test_declared_fixture_type_extension_overrides_without_invented_status_values(self) -> None:
        """A labelled disposable Project extension, not a production source pin."""
        source = self.sources["CA-R-1874"]
        extension = source.with_name("CA-R-9900--fixture-action-domain.md")
        text = source.read_text(encoding="utf-8").replace('"CA-R-1874"', '"CA-R-9900"').replace(
            "atom_id: CA-R-1874", "atom_id: CA-R-9900"
        )
        text = re.sub(r'(?m)^(\s*governs:)\s*.*$',
                      r'\1 "Atom/Content Role: Operations/Type: `Action`/Status"', text, count=1)
        extension.write_text(text, encoding="utf-8")
        action = self.atom("Operations", "Active", atom_type="Action")
        selected = resolve_status_model(self.root, atom_from_path(self.root, action), "Active")
        self.assertEqual("CA-R-9900", selected["model_sources"][0]["atom_id"])
        self.assertEqual(["Draft", "Active", "Archived"], selected["statuses"])
        workflow = self.atom("Operations", "Active", number=8001, atom_type="Workflow")
        fallback = resolve_status_model(self.root, atom_from_path(self.root, workflow), "Active")
        self.assertEqual("CA-R-1874", fallback["model_sources"][0]["atom_id"])

    def test_every_role_same_status_is_noop_before_all_writes(self) -> None:
        for role, status in ((row[0], "active" if row[0] == "Concern" else "Done"
                             if row[0] in {"Analysis", "Plan"} else "Active") for row in DOMAINS):
            with self.subTest(role=role):
                path = self.atom(role, status)
                request = self.request(path, status)
                before = self.snapshot()
                result = self.execute(request)
                self.assertEqual("no-op", result["outcome"])
                self.assert_no_effect(result)
                self.assertEqual(before, self.snapshot())
                self.assertEqual(request["target"]["version"], result["observed"]["version"])
                self.assertEqual(request["target"]["updated_at"], result["observed"]["updated_at"])
                self.assert_model(result, request)

    def test_all_archival_roles_apply_current_d565_destination_and_preserve_whole_body(self) -> None:
        for role, _, directory, _, statuses in DOMAINS:
            if "Archived" not in statuses:
                continue
            with self.subTest(role=role):
                path = self.atom(role, "Done" if role == "Analysis" else "Active")
                request = self.request(path, "Archived")
                before_atom = atom_from_path(self.root, path)
                canonical_current = self.root / CONTROL / "fixture" / directory
                destination = canonical_current / "archived" / f"{path.stem}@3.md"
                self.assertFalse(destination.parent.exists())
                result = self.execute(request)
                self.assertEqual("applied", result["outcome"])
                self.assertFalse(path.exists())
                self.assertEqual(destination.relative_to(self.root).as_posix(), result["observed"]["path"])
                self.assertEqual("Archived", result["observed"]["status"])
                self.assertEqual(3, result["observed"]["version"])
                after_atom = atom_from_path(self.root, destination)
                self.assertEqual(before_atom.content, after_atom.content)
                self.assertEqual(before_atom.atom_id, after_atom.atom_id)
                self.assert_model(result, request)

    def test_plan_local_container_backlog_done_canceled_and_reactivation(self) -> None:
        path = self.atom("Plan", "Active", atom_type="Task", container="parent-plan")
        local = path.parent
        for status, folder in (("Backlog", "001_backlog"), ("Done", "done"),
                               ("Canceled", "canceled"), ("Active", None)):
            request = self.request(path, status)
            result = self.execute(request)
            self.assertEqual("applied", result["outcome"])
            expected = local / folder / "CA-P-8000--golden.md" if folder else local / "CA-P-8000--golden.md"
            self.assertEqual(expected.relative_to(self.root).as_posix(), result["observed"]["path"])
            path = expected
            self.assert_model(result, request)

    def test_concern_lowercase_nonactive_transitions_never_borrow_archive(self) -> None:
        path = self.atom("Concern", "active", atom_type="Problem")
        local = self.root / CONTROL / "fixture/01_concern"
        for status in ("resolved", "canceled", "active"):
            request = self.request(path, status)
            result = self.execute(request)
            expected = local / status / path.name
            self.assertEqual(expected.relative_to(self.root).as_posix(), result["observed"]["path"])
            path = expected
            self.assert_model(result, request)
        before = self.snapshot()
        with self.assertRaises(StatusModelError):
            resolve_status_model(self.root, atom_from_path(self.root, path), "Archived")
        self.assertEqual(before, self.snapshot())

    def test_preview_denied_execution_and_destination_collision_are_unchanged(self) -> None:
        path = self.atom("Requirement", "Active")
        request = self.request(path, "Archived")
        before = self.snapshot()
        preview = change_status_atom_action(self.root, request)
        self.assertEqual("preview", preview["outcome"])
        self.assert_no_effect(preview)
        self.assertEqual(before, self.snapshot())
        with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
            change_status_atom_action(self.root, request, execute=True, authorized=False)
        self.assertEqual(before, self.snapshot())
        destination = path.parent / "archived" / f"{path.stem}@3.md"
        destination.parent.mkdir()
        destination.write_bytes(b"reserved destination; must survive")
        collided = self.snapshot()
        with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
            self.execute(request)
        self.assertEqual(collided, self.snapshot())

    def test_caller_models_and_revoked_authority_refuse_before_effects(self) -> None:
        path = self.atom("Requirement", "Active")
        request = self.request(path, "Archived")
        for field, value in (("content_role", "Plan"), ("statuses", ["Active", "Reviewed", "Archived"])):
            forged = copy.deepcopy(request)
            forged["status_model"] = resolve_status_model(self.root, forged["target"], "Archived")
            forged["status_model"][field] = value
            before = self.snapshot()
            with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
                self.execute(forged)
            self.assertEqual(before, self.snapshot())
        source = self.sources["CA-R-1309"]
        original = source.read_bytes()
        for changed in (original.replace(b'status: "Active"', b'status: "Archived"').replace(
                            b"status: Active", b"status: Archived"),):
            source.write_bytes(changed)
            before = self.snapshot()
            with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
                self.execute(request)
            self.assertEqual(before, self.snapshot())
            source.write_bytes(original)

    def test_native_exact_status_refusals_leave_all_project_bytes_unchanged(self) -> None:
        for role, current, denied in (("Requirement", "Active", "Reviewed"),
                                      ("Requirement", "Active", "active"),
                                      ("Plan", "Done", "done"),
                                      ("Concern", "resolved", "Active"),
                                      ("Analysis", "Done", "Active")):
            with self.subTest(role=role, denied=denied):
                path = self.atom(role, current)
                request = self.request(path, denied)
                before = self.snapshot()
                with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
                    self.execute(request)
                self.assertEqual(before, self.snapshot())

    def test_source_change_after_pure_preflight_is_reobserved_before_effect(self) -> None:
        source = self.sources["CA-R-1309"]
        original = source.read_bytes()
        allowed = lifecycle_intents._execute_allowed
        changes = (original + b"\nChanged after admission.\n",
                   original.replace(b'status: "Active"', b'status: "Archived"').replace(
                       b"status: Active", b"status: Archived"))
        for offset, changed in enumerate(changes):
            with self.subTest(revocation=b"Changed after" not in changed):
                path = self.atom("Requirement", "Active", number=8000 + offset,
                                 container=f"race-{offset}")
                request = self.request(path, "Archived")
                before_target = path.read_bytes()
                preflight = preflight_atom_lifecycle(self.root, "change_status", request)
                self.assertEqual(hashlib.sha256(original).hexdigest(),
                                 preflight["status_model"]["model_sources"][0]["sha256"])
                changed_snapshot = []

                def change_authority(*, execute: bool, authorized: bool) -> bool:
                    source.write_bytes(changed)
                    changed_snapshot.append(self.snapshot())
                    return allowed(execute=execute, authorized=authorized)

                try:
                    with patch.object(lifecycle_intents, "_execute_allowed", side_effect=change_authority):
                        with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
                            self.execute(request)
                    self.assertEqual(before_target, path.read_bytes())
                    self.assertEqual(1, len(changed_snapshot))
                    self.assertEqual(changed_snapshot[0], self.snapshot())
                    self.assertFalse((path.parent / "archived").exists())
                    self.assertFalse((path.parent / "archive").exists())
                finally:
                    source.write_bytes(original)

    def test_archive_retains_legacy_history_and_reports_refs_without_repair(self) -> None:
        path = self.atom("Requirement", "Active", relations="relations:\n  depends_on: [CA-R-8001]")
        successor = self.atom("Requirement", "Active", number=8001)
        referrer = self.atom("Requirement", "Active", number=8002,
                             relations="relations:\n  depends_on: [CA-R-8000]")
        unchanged = {candidate: candidate.read_bytes() for candidate in (successor, referrer)}
        legacy = path.parent / "archive" / f"{path.stem}@2.md"
        legacy.parent.mkdir()
        legacy.write_bytes(b"immutable legacy revision evidence")
        unchanged[legacy] = legacy.read_bytes()
        result = self.execute(self.request(path, "Archived"))
        self.assertEqual("applied", result["outcome"])
        self.assertEqual({"inbound", "outgoing"}, {item["direction"] for item in result["broken_references"]})
        self.assertFalse(result["repair_handoff"]["automatic_repair"])
        for candidate, raw in unchanged.items():
            self.assertEqual(raw, candidate.read_bytes())

    def test_actual_unassigned_draft_same_status_is_noop(self) -> None:
        path = self.atom("Requirement", "Draft", draft=True)
        request = self.request(path, "Draft")
        self.assertIsNone(request["target"]["atom_id"])
        before = self.snapshot()
        result = self.execute(request)
        self.assertEqual("no-op", result["outcome"])
        self.assert_no_effect(result)
        self.assertEqual(before, self.snapshot())
        self.assertIsNone(result["observed"]["atom_id"])

    def test_identified_to_draft_removes_assignment_but_retains_same_meaning(self) -> None:
        path = self.atom("Requirement", "Active")
        before = atom_from_path(self.root, path)
        history = path.parent / "archive" / f"{path.stem}@2.md"
        history.parent.mkdir()
        history.write_bytes(b"old identified revision evidence")
        before_history = history.read_bytes()
        result = self.execute(self.request(path, "Draft"))
        self.assertEqual("applied", result["outcome"])
        destination = self.root / result["observed"]["path"]
        self.assertFalse(path.exists())
        self.assertEqual("CA-R--golden.md", destination.name)
        self.assertIsNone(result["observed"]["atom_id"])
        after = atom_from_path(self.root, destination)
        self.assertIsNone(frontmatter_scalar(after.frontmatter, "atom_id"))
        self.assertEqual(before.content, after.content)
        self.assertEqual(3, result["observed"]["version"])
        self.assertEqual(before_history, history.read_bytes())


if __name__ == "__main__":
    unittest.main()
