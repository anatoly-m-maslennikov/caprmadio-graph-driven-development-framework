"""Golden coverage for source-derived, pure Atom status-model resolution."""

from __future__ import annotations

import copy
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from authoritative_status_models import StatusModelError, resolve_status_model  # noqa: E402


class AuthoritativeStatusModelsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.sources = (
            self.root
            / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement"
        )
        self.sources.mkdir(parents=True)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _source(
        self,
        atom_id: str,
        role: str,
        statuses: list[str],
        *,
        revision: int = 1,
        atom_type: str | None = None,
        active: bool = True,
    ) -> Path:
        suffix = atom_type.lower().replace(" ", "-") if atom_type else role.lower()
        path = self.sources / f"{atom_id}--{suffix}.md"
        governs = f"Atom/Content Role: {role}/Status"
        if atom_type:
            governs = f"Atom/Content Role: {role}/Type: `{atom_type}`"
        path.write_text(
            "---\n"
            f"atom_id: {atom_id}\n"
            "content_role: Requirement\n"
            f"status: {'Active' if active else 'Archived'}\n"
            f"version: {revision}\n"
            "subjects:\n"
            f"  governs: \"{governs}\"\n"
            "---\n"
            "# Summary\n\nFixture status authority\n\n"
            "## Claim\n\n"
            f"the Core allowed values of {role} Status **must** be exactly ({', '.join(statuses)}).\n",
            encoding="utf-8",
        )
        return path

    def _resolve(self, role: str, requested_status: str, atom_type: str | None = None) -> dict[str, object]:
        atom: dict[str, str] = {"content_role": role}
        if atom_type:
            atom["type"] = atom_type
        return resolve_status_model(self.root, atom, requested_status)

    def test_all_core_role_domains_and_exact_casing(self) -> None:
        cases = (
            ("Requirement", ["Draft", "Active", "Archived"], "Draft"),
            ("Method", ["Draft", "Active", "Archived"], "Active"),
            ("Evaluation", ["Draft", "Active", "Archived"], "Archived"),
            ("Delivery", ["Draft", "Active", "Archived"], "Active"),
            ("Plan", ["Active", "Backlog", "Done", "Canceled", "Archived"], "Done"),
            ("Concern", ["draft", "active", "resolved", "canceled"], "resolved"),
            ("Operations", ["Draft", "Active", "Archived"], "Archived"),
            ("Analysis", ["Draft", "Done", "Archived"], "Done"),
        )
        for index, (role, statuses, requested) in enumerate(cases, start=1):
            with self.subTest(role=role):
                source = self._source(f"CA-R-{9000 + index}", role, statuses, revision=index)
                model = self._resolve(role, requested)
                self.assertEqual(model["content_role"], role)
                self.assertIsNone(model["type"])
                self.assertEqual(model["statuses"], statuses)
                self.assertEqual(model["requested_status"], requested)
                pin = model["model_sources"][0]
                self.assertEqual(pin["atom_id"], f"CA-R-{9000 + index}")
                self.assertEqual(pin["revision"], index)
                self.assertEqual(pin["path"], source.relative_to(self.root).as_posix())
                with self.assertRaisesRegex(StatusModelError, "requested status"):
                    self._resolve(role, requested.swapcase())

    def test_specialized_type_precedes_role_fallback_without_duplicate_domain(self) -> None:
        self._source("CA-R-9101", "Operations", ["Draft", "Active", "Archived"])
        self._source(
            "CA-R-9102", "Operations", ["Draft", "Proposed", "Archived"], atom_type="Action", revision=2
        )
        selected = self._resolve("Operations", "Proposed", "Action")
        self.assertEqual(selected["type"], "Action")
        self.assertEqual(selected["statuses"], ["Draft", "Proposed", "Archived"])
        self.assertEqual(selected["model_sources"][0]["atom_id"], "CA-R-9102")

        fallback = self._resolve("Operations", "Active", "Workflow")
        self.assertEqual(fallback["type"], "Workflow")
        self.assertEqual(fallback["model_sources"][0]["atom_id"], "CA-R-9101")

    def test_duplicate_specialized_or_role_domains_are_ambiguous(self) -> None:
        self._source("CA-R-9201", "Operations", ["Draft", "Active", "Archived"])
        self._source("CA-R-9202", "Operations", ["Draft", "Proposed", "Archived"], atom_type="Action")
        self._source("CA-R-9203", "Operations", ["Draft", "Proposed", "Archived"], atom_type="Action", revision=2)
        with self.assertRaisesRegex(StatusModelError, "ambiguous"):
            self._resolve("Operations", "Proposed", "Action")
        self._source("CA-R-9204", "Requirement", ["Draft", "Active", "Archived"])
        self._source("CA-R-9205", "Requirement", ["Draft", "Active", "Archived"], revision=2)
        with self.assertRaisesRegex(StatusModelError, "ambiguous"):
            self._resolve("Requirement", "Active")

    def test_missing_and_unsupported_domains_refuse_without_a_caller_default(self) -> None:
        with self.assertRaisesRegex(StatusModelError, "no current status model"):
            self._resolve("Implementation", "Active")
        self._source("CA-R-9301", "Concern", ["draft", "active", "resolved", "canceled"])
        with self.assertRaisesRegex(StatusModelError, "requested status"):
            self._resolve("Concern", "Archived")
        with self.assertRaisesRegex(StatusModelError, "content_role"):
            resolve_status_model(self.root, {}, "Active")

    def test_forged_or_stale_caller_model_is_rejected_but_exact_pin_is_accepted(self) -> None:
        source = self._source("CA-R-9401", "Requirement", ["Draft", "Active", "Archived"], revision=1)
        atom = {"content_role": "Requirement"}
        current = resolve_status_model(self.root, atom, "Active")
        self.assertEqual(resolve_status_model(self.root, atom, "Active", supplied_model=current), current)

        forged = copy.deepcopy(current)
        forged["statuses"] = ["Draft", "Active", "Reviewed", "Archived"]
        with self.assertRaisesRegex(StatusModelError, "differs"):
            resolve_status_model(self.root, atom, "Active", supplied_model=forged)

        self._source("CA-R-9401", "Requirement", ["Draft", "Active", "Archived"], revision=2)
        with self.assertRaisesRegex(StatusModelError, "differs"):
            resolve_status_model(self.root, atom, "Active", supplied_model=current)
        self.assertNotEqual(source.read_bytes(), b"")

    def test_configured_methodology_source_binding_is_used_instead_of_a_hardcoded_root(self) -> None:
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir(exist_ok=True)
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n", encoding="utf-8"
        )
        configured = self.root / "operator-methodology/sources/001_CORE_META_MODEL/04_requirement"
        configured.mkdir(parents=True)
        (control / "project_structure.toml").write_text(
            "[[scope_units]]\n"
            "scope_unit_name = \"METHODOLOGY_SOURCES\"\n"
            "authority_path = \"operator-methodology/sources\"\n",
            encoding="utf-8",
        )
        source = configured / "CA-R-9501--plan.md"
        source.write_text(
            "---\natom_id: CA-R-9501\ncontent_role: Requirement\nstatus: Active\nversion: 1\n"
            "subjects:\n  governs: \"Atom/Content Role: Plan/Status\"\n---\n"
            "# Summary\n\nFixture\n\n## Claim\n\n"
            "the Core allowed values of Plan Status **must** be exactly (Active, Backlog, Done, Canceled, Archived).\n",
            encoding="utf-8",
        )
        model = self._resolve("Plan", "Done")
        self.assertEqual(model["model_sources"][0]["path"], source.relative_to(self.root).as_posix())

    def test_structured_quoted_subjects_and_duplicate_yaml_keys_are_not_silently_accepted(self) -> None:
        structured = self.sources / "CA-R-9601--action.md"
        structured.write_text(
            "---\natom_id: CA-R-9601\ncontent_role: Requirement\nstatus: Active\nversion: 3\n"
            "subjects:\n  governs: 'Atom/Content Role: Operations/Type: `Action`'\n---\n"
            "# Summary\n\nFixture\n\n## Claim\n\n"
            "the Core allowed values of Operations Status **must** be exactly (Draft, Proposed, Archived).\n",
            encoding="utf-8",
        )
        self.assertEqual(self._resolve("Operations", "Proposed", "Action")["model_sources"][0]["atom_id"], "CA-R-9601")

        duplicate = self.sources / "CA-R-9602--duplicate.md"
        duplicate.write_text(
            "---\natom_id: CA-R-9602\natom_id: CA-R-9603\ncontent_role: Requirement\nstatus: Active\nversion: 1\n"
            "subjects:\n  governs: \"Atom/Content Role: Requirement/Status\"\n---\n"
            "# Summary\n\nFixture\n\n## Claim\n\n"
            "the Core allowed values of Requirement Status **must** be exactly (Draft, Active, Archived).\n",
            encoding="utf-8",
        )
        with self.assertRaises(StatusModelError) as rejected:
            self._resolve("Requirement", "Active")
        self.assertEqual(rejected.exception.code, "source-invalid")

    def test_source_pin_hash_is_the_exact_parsed_source_bytes(self) -> None:
        source = self._source("CA-R-9701", "Requirement", ["Draft", "Active", "Archived"], revision=9)
        source_bytes = source.read_bytes()
        model = self._resolve("Requirement", "Active")
        self.assertEqual(model["model_sources"][0]["sha256"], hashlib.sha256(source_bytes).hexdigest())

    def test_source_version_must_be_a_positive_yaml_integer(self) -> None:
        source = self.sources / "CA-R-9801--invalid-version.md"
        for raw_version in ('"1"', "0", "true"):
            with self.subTest(version=raw_version):
                source.write_text(
                    "---\natom_id: CA-R-9801\ncontent_role: Requirement\nstatus: Active\n"
                    f"version: {raw_version}\nsubjects:\n"
                    "  governs: \"Atom/Content Role: Requirement/Status\"\n---\n"
                    "# Summary\n\nFixture\n\n## Claim\n\n"
                    "the Core allowed values of Requirement Status **must** be exactly (Draft, Active, Archived).\n",
                    encoding="utf-8",
                )
                with self.assertRaises(StatusModelError) as rejected:
                    self._resolve("Requirement", "Active")
                self.assertEqual(rejected.exception.code, "source-invalid")

    def test_status_authority_requires_its_own_content_role(self) -> None:
        source = self.sources / "CA-R-9802--missing-content-role.md"
        source.write_text(
            "---\natom_id: CA-R-9802\nstatus: Active\nversion: 1\nsubjects:\n"
            "  governs: \"Atom/Content Role: Requirement/Status\"\n---\n"
            "# Summary\n\nFixture\n\n## Claim\n\n"
            "the Core allowed values of Requirement Status **must** be exactly (Draft, Active, Archived).\n",
            encoding="utf-8",
        )
        with self.assertRaises(StatusModelError) as rejected:
            self._resolve("Requirement", "Active")
        self.assertEqual(rejected.exception.code, "source-invalid")

    def test_multiple_status_domain_claims_in_one_source_are_ambiguous(self) -> None:
        source = self.sources / "CA-R-9803--multiple-domains.md"
        source.write_text(
            "---\natom_id: CA-R-9803\ncontent_role: Requirement\nstatus: Active\nversion: 1\nsubjects:\n"
            "  governs: \"Atom/Content Role: Requirement/Status\"\n---\n"
            "# Summary\n\nFixture\n\n## Claim\n\n"
            "the Core allowed values of Requirement Status **must** be exactly (Draft, Active, Archived).\n\n"
            "the Core allowed values of Plan Status **must** be exactly (Active, Backlog, Done, Canceled, Archived).\n",
            encoding="utf-8",
        )
        with self.assertRaises(StatusModelError) as rejected:
            self._resolve("Requirement", "Active")
        self.assertEqual(rejected.exception.code, "source-invalid")


if __name__ == "__main__":
    unittest.main()
