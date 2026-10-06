from __future__ import annotations

import hashlib
import copy
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

import sys

TOOLS = Path(__file__).resolve().parents[1]
REPOSITORY = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))

REQUIREMENT_STATUS_AUTHORITY = (
    REPOSITORY
    / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
    / "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement"
    / "CA-R-1309-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-requirement-status-values.md"
)
SEMANTIC_ASSESSMENT_AUTHORITIES = tuple(
    REPOSITORY
    / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
    / "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement"
    / name
    for name in (
        "CA-R-1875-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-analysis-status-values.md",
        "CA-R-1432-CORE_META_MODEL-GENERAL--classify-admitted-atom-changes-by-semantic-effect.md",
        "CA-R-1464-CORE_META_MODEL--keep-summary-fixed-for-atom-identity.md",
    )
)

from lifecycle_intents import (  # noqa: E402
    LifecycleError,
    carrier_descriptor,
    change_status_atom_action,
    create_atom_action,
    replace_atom_action,
    update_atom_action,
    update_assessment_seal,
)
from atom_operations import Atom, ToolError, atom_from_path, split_frontmatter  # noqa: E402
from authoritative_status_models import resolve_status_model  # noqa: E402


class SelectedAtomLifecycleTest(unittest.TestCase):
    """Golden single-target lifecycle cases for the CA-D-527 route payload."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.requirements = self.root / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/04_requirement"
        self.requirements.mkdir(parents=True)
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n", encoding="utf-8"
        )
        status_authority = self.root / REQUIREMENT_STATUS_AUTHORITY.relative_to(REPOSITORY)
        status_authority.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REQUIREMENT_STATUS_AUTHORITY, status_authority)
        for authority in SEMANTIC_ASSESSMENT_AUTHORITIES:
            destination = self.root / authority.relative_to(REPOSITORY)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(authority, destination)
        self.target = self._atom("CA-R-100", "target", "Stable summary")
        self.successor_one = self._atom("CA-R-101", "first-successor", "First successor")
        self.successor_two = self._atom("CA-R-102", "second-successor", "Second successor")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _atom(
        self,
        atom_id: str,
        slug: str,
        summary: str,
        *,
        status: str = "Active",
        version: int = 1,
        relations: str = "relations: {}",
        include_type: bool = False,
    ) -> Path:
        path = self.requirements / f"{atom_id}--{slug}.md"
        payload = (
            "---\n"
            + f"atom_id: {atom_id}\n"
            + "content_role: Requirement\n"
            + ("type: Requirement\n" if include_type else "")
            + f"status: {status}\n"
            + f"version: {version}\n"
            + "updated_at: 2026-01-01 00:00:00 +0000\n"
            + f"{relations}\n"
            + "---\n"
            + "# Summary\n\n"
            + f"{summary}\n\n"
            + "## Scope\n\n"
            + "Fixture scope.\n\n"
            + "## Claim\n\n"
            + "Fixture claim.\n"
        )
        path.write_text(payload, encoding="utf-8")
        return path

    def _model(self) -> dict[str, object]:
        return resolve_status_model(
            self.root, carrier_descriptor(self.root, "CA-R-100"), "Archived",
        )

    def _carrier(self, atom_id: str, slug: str, summary: str) -> dict[str, str]:
        path = self.requirements / f"{atom_id}--{slug}.md"
        return {
            "path": path.relative_to(self.root).as_posix(),
            "frontmatter": f"atom_id: {atom_id}\ncontent_role: Requirement\nstatus: Active",
            "content": f"# Summary\n\n{summary}\n\n## Scope\n\nFixture.\n",
        }

    @staticmethod
    def _proposal(path: Path, *, summary: str, body_suffix: str = "") -> dict[str, str]:
        text = path.read_text(encoding="utf-8")
        frontmatter, content = text[4:].split("\n---\n", 1)
        current_summary = content.split("# Summary\n\n", 1)[1].split("\n\n", 1)[0]
        return {
            "frontmatter": frontmatter,
            "content": content.replace(current_summary, summary, 1) + body_suffix,
        }

    def test_authorized_create_uses_a_complete_carrier_and_rejects_occupied_destination(self) -> None:
        path = self.requirements / "CA-R-103--created.md"
        carrier = self._carrier("CA-R-103", "created", "Created summary")

        result = create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)

        self.assertEqual(result["operation"], "create")
        self.assertEqual(result["effects"][0]["state"], "changed")
        self.assertEqual(carrier_descriptor(self.root, "CA-R-103")["version"], 1)
        before = path.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "destination-collision"):
            create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)
        self.assertEqual(path.read_bytes(), before)

        missing_identity = dict(carrier)
        missing_identity["path"] = (self.requirements / "CA-R-104--missing-id.md").relative_to(self.root).as_posix()
        missing_identity["frontmatter"] = "content_role: Requirement\nstatus: Active"
        with self.assertRaisesRegex(LifecycleError, "atom-frontmatter-id-required"):
            create_atom_action(self.root, {"carrier": missing_identity}, execute=True, authorized=True)
        mismatch = dict(carrier)
        mismatch["path"] = (self.requirements / "CA-R-105--mismatch.md").relative_to(self.root).as_posix()
        mismatch["frontmatter"] = "atom_id: CA-R-106\ncontent_role: Requirement\nstatus: Active"
        with self.assertRaisesRegex(LifecycleError, "atom-frontmatter-id-mismatch"):
            create_atom_action(self.root, {"carrier": mismatch}, execute=True, authorized=True)

    def test_changed_summary_is_a_terminal_non_effect_replace_handoff(self) -> None:
        before = self.target.read_bytes()
        result = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Changed summary"),
                "change_class": "semantic_revision",
                "successors": [self._carrier("CA-R-105", "replacement", "Changed summary")],
            },
            execute=True,
            authorized=True,
        )

        self.assertEqual(result["outcome"], "replace_handoff")
        self.assertEqual(result["effects"][0]["state"], "unchanged")
        self.assertEqual(result["replace_handoff"]["predecessor"]["atom_id"], "CA-R-100")
        self.assertEqual(result["replace_handoff"]["successors"][0]["frontmatter"].splitlines()[0], "atom_id: CA-R-105")
        self.assertEqual(self.target.read_bytes(), before)

    def test_update_honors_identity_revision_class_and_true_noop(self) -> None:
        before = self.target.read_bytes()
        unproven_carrier_only = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary", body_suffix="\nCarrier note.\n"),
                "change_class": "carrier_only",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(unproven_carrier_only["outcome"], "unresolved")
        self.assertEqual(unproven_carrier_only["classification"]["reason"], "semantic-assessment-unverified")
        self.assertEqual(self.target.read_bytes(), before)

        lossless = self._proposal(self.target, summary="Stable summary")
        lossless["content"] += "\n"
        carrier_only = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": lossless,
                "change_class": "carrier_only",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(carrier_only["observed"]["version"], 1)
        self.assertEqual(carrier_only["effects"][0]["state"], "changed")

        before_semantic = self.target.read_bytes()
        semantic = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary", body_suffix="\nSemantic detail.\n"),
                "change_class": "semantic_revision",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(semantic["outcome"], "unresolved")
        self.assertEqual(semantic["classification"]["requested"], "semantic_revision")
        self.assertIn("lineage-impact review", semantic["classification"]["required"])
        self.assertEqual(self.target.read_bytes(), before_semantic)

        before = self.target.read_bytes()
        noop = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary"),
                "change_class": "carrier_only",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(noop["outcome"], "no-op")
        self.assertEqual(self.target.read_bytes(), before)

    def test_update_rejects_unproven_equivalent_refinement(self) -> None:
        before = self.target.read_bytes()
        result = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary", body_suffix="\nUnproven refinement.\n"),
                "change_class": "equivalent_refinement",
            },
            execute=True,
            authorized=True,
        )

        self.assertEqual(result["outcome"], "unresolved")
        self.assertEqual(result["classification"]["requested"], "equivalent_refinement")
        self.assertEqual(self.target.read_bytes(), before)

    def test_update_rechecks_the_completed_assessment_comparison(self) -> None:
        proposal = self._proposal(self.target, summary="Stable summary")
        proposal["content"] += "\n"
        parameters = {
            "target": carrier_descriptor(self.root, "CA-R-100"),
            "proposed": proposal,
            "change_class": "carrier_only",
        }
        preview = update_atom_action(self.root, parameters, execute=False, authorized=True)
        evidence = preview["assessment_evidence"]
        assessment = update_assessment_seal(parameters, evidence)
        tampered = {
            **assessment,
            "comparison": {
                **assessment["comparison"],
                "target": {**assessment["comparison"]["target"], "digest": "0" * 64},
            },
        }
        before = self.target.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "reassessment-required"):
            update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=tampered)
        self.assertEqual(self.target.read_bytes(), before)

        applied = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual(applied["outcome"], "applied")
        self.assertEqual(applied["assessment"], assessment)

    def _semantic_assessment_report(self, proposed: dict[str, str], *, change_class: str = "semantic_revision") -> dict[str, str]:
        authority_root = SEMANTIC_ASSESSMENT_AUTHORITIES[0].parent
        def pin(path: Path) -> dict[str, str]:
            return {"path": path.relative_to(self.root).as_posix(), "digest": hashlib.sha256(path.read_bytes()).hexdigest()}

        target = carrier_descriptor(self.root, "CA-R-100")
        report = self.root / ".caprmedio_caprmedio/02_analysis/done/CA-A-400--semantic-update-assessment.md"
        report.parent.mkdir(parents=True, exist_ok=True)
        evidence = {
            "target": {"atom_id": target["atom_id"], "path": target["path"], "digest": target["digest"]},
            "proposal": {"frontmatter_digest": hashlib.sha256(proposed["frontmatter"].encode()).hexdigest(),
                         "content_digest": hashlib.sha256(proposed["content"].encode()).hexdigest()},
            "authorityPins": {"r1432": pin(self.root / authority_root.relative_to(REPOSITORY) / SEMANTIC_ASSESSMENT_AUTHORITIES[1].name),
                              "r1464": pin(self.root / authority_root.relative_to(REPOSITORY) / SEMANTIC_ASSESSMENT_AUTHORITIES[2].name)},
            "admittedChangeClass": change_class,
            "primaryClaimIdentityPreserved": True,
            "declaredDelta": "Clarify the same fixture Claim's acceptance detail.",
            "lineageEvidencePins": [pin(self.target)],
        }
        report.write_text(
            "---\natom_id: CA-A-400\ncontent_role: Analysis\ntype: Analysis Report\nstatus: Done\nversion: 1\n"
            "updated_at: 2026-10-06 00:00:00 +0000\nrelations: {}\n---\n# Summary\n\nSemantic update assessment\n"
            "\n## Results\n\n### Update assessment evidence\n\n```json\n"
            + json.dumps(evidence, sort_keys=True, separators=(",", ":")) + "\n```\n",
            encoding="utf-8",
        )
        return pin(report)

    def test_semantic_update_requires_and_consumes_a_bound_done_analysis_report(self) -> None:
        proposal = self._proposal(self.target, summary="Stable summary", body_suffix="\nClarified acceptance detail.\n")
        report = self._semantic_assessment_report(proposal)
        parameters = {
            "target": carrier_descriptor(self.root, "CA-R-100"), "proposed": proposal,
            "change_class": "semantic_revision", "semantic_assessment_report": report,
        }
        preview = update_atom_action(self.root, parameters, execute=False, authorized=True)
        self.assertEqual(preview["outcome"], "preview")
        evidence = preview["assessment_evidence"]
        assessment = update_assessment_seal(parameters, evidence)
        report_path = self.root / report["path"]
        report_path.write_text(report_path.read_text(encoding="utf-8") + "\ntampered\n", encoding="utf-8")
        before = self.target.read_bytes()
        stale = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual(stale["outcome"], "unresolved")
        self.assertEqual(self.target.read_bytes(), before)

        parameters["semantic_assessment_report"] = self._semantic_assessment_report(proposal)
        preview = update_atom_action(self.root, parameters, execute=False, authorized=True)
        assessment = update_assessment_seal(parameters, preview["assessment_evidence"])
        applied = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual(applied["outcome"], "applied")
        self.assertEqual(applied["observed"]["version"], 2)

    def _legacy_update(self, *, legacy_status: str | None = None) -> tuple[dict[str, object], bytes]:
        original = self.target.read_text(encoding="utf-8").replace("atom_id: CA-R-100\n", "").replace(
            "status: Active\n", ""
        ).replace("# Summary\n\nStable summary", "# Stable summary")
        if legacy_status is not None:
            original = original.replace("version: 1\n", f"status: {legacy_status}\nversion: 1\n")
        self.target.write_text(original, encoding="utf-8")
        for args in (("init",), ("add", "--", self.target.relative_to(self.root).as_posix()),
                     ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                      "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null", "commit", "-m", "legacy carrier")):
            subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, check=True)
        commit = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"],
                                capture_output=True, check=True, text=True).stdout.strip()
        fm, content = split_frontmatter(original)
        atom = Atom(self.target, self.target.relative_to(self.root).as_posix(), self.target.name,
                    "CA-R-100", "active", "04_requirement", fm, content)
        target = carrier_descriptor(self.root, atom)
        proposed = {"frontmatter": fm + "\natom_id: CA-R-100\nstatus: Active",
                    "content": content.replace("# Stable summary", "# Summary\n\nStable summary", 1)}
        return {"target": target, "proposed": proposed, "change_class": "carrier_only",
                "legacy_identity_proof": {"atom_id": "CA-R-100", "commit": commit,
                                          "path": atom.relative, "digest": target["digest"]}}, original.encode()

    def test_explicit_historical_migration_is_preview_only_until_authorized_and_preserves_bytes(self) -> None:
        parameters, before = self._legacy_update()
        with self.assertRaisesRegex(ToolError, "declare atom_id"):
            atom_from_path(self.root, self.target)
        without_proof = {k: v for k, v in parameters.items() if k != "legacy_identity_proof"}
        with self.assertRaisesRegex(LifecycleError, "atom-frontmatter-id-required"):
            update_atom_action(self.root, without_proof, execute=True, authorized=True)
        preview = update_atom_action(self.root, parameters)
        self.assertEqual(preview["outcome"], "preview")
        self.assertEqual(self.target.read_bytes(), before)
        self.assertFalse((self.requirements / "archive").exists())
        with self.assertRaisesRegex(LifecycleError, "authorization-required"):
            update_atom_action(self.root, parameters, execute=True)
        result = update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(result["observed"]["atom_id"], "CA-R-100")
        self.assertEqual(result["observed"]["version"], 1)
        self.assertEqual(atom_from_path(self.root, self.target).atom_id, "CA-R-100")
        self.assertEqual((self.root / result["history"]["prior_revision"]["path"]).read_bytes(), before)

    def test_historical_migration_rejects_forged_stale_or_nonhistorical_identity(self) -> None:
        parameters, before = self._legacy_update()
        for key, value in (("commit", "0" * 40), ("digest", "0" * 64), ("atom_id", "CA-R-999"),
                           ("path", "../outside.md")):
            invalid = copy.deepcopy(parameters)
            invalid["legacy_identity_proof"][key] = value
            with self.assertRaisesRegex(LifecycleError, "legacy-proof-invalid|legacy-history-unavailable"):
                update_atom_action(self.root, invalid, execute=True, authorized=True)
            self.assertEqual(self.target.read_bytes(), before)
        self.target.write_bytes(before + b"\nchanged\n")
        with self.assertRaisesRegex(LifecycleError, "legacy-proof-invalid"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)

    def test_historical_migration_does_not_choose_between_duplicate_owners(self) -> None:
        parameters, before = self._legacy_update()
        duplicate = self._atom("CA-R-100", "duplicate", "Distinct claim")
        with self.assertRaisesRegex(LifecycleError, "active-atom-id-ambiguous"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(self.target.read_bytes(), before)
        duplicate.write_text(duplicate.read_text().replace("atom_id: CA-R-100\n", ""))
        with self.assertRaisesRegex(LifecycleError, "active-atom-id-ambiguous"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(self.target.read_bytes(), before)

    def test_historical_migration_cannot_promote_a_draft(self) -> None:
        parameters, before = self._legacy_update(legacy_status="draft")
        with self.assertRaisesRegex(LifecycleError, "legacy-proof-inapplicable"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(self.target.read_bytes(), before)

    def _mapped_delivery(self) -> tuple[dict[str, object], Path, Path, bytes]:
        role = self.requirements.parent / "07_delivery"
        role.mkdir()
        old_id = "CAPRMEDIO-FRAMEWORK-ENGINE-DELV-005"
        source = role / (old_id + "-GRAPH_UI-DELIVERY--stable-delivery.md")
        original = b"---\nversion: 8\nrelations: {}\n---\n# Stable delivery\n\nDeliver the browser locally.\n"
        source.write_bytes(original)
        for args in (("init",), ("add", "--", source.relative_to(self.root).as_posix()),
                     ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                      "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null", "commit", "-m", "legacy delivery")):
            subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, check=True)
        commit = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"],
                                capture_output=True, check=True, text=True).stdout.strip()
        fm, body = split_frontmatter(original.decode())
        old = Atom(source, source.relative_to(self.root).as_posix(), source.name, old_id,
                   "active", "07_delivery", fm, body)
        target = carrier_descriptor(self.root, old)
        destination = role / "CA-D-560-GRAPH_UI--stable-delivery.md"
        return {"target": target,
                "proposed": {"frontmatter": fm + "\natom_id: CA-D-560\ncontent_role: Delivery\nstatus: Active",
                             "content": "# Summary\n\nStable delivery\n\n## Claim\n\nDeliver the browser locally.\n"},
                "change_class": "carrier_only",
                "legacy_identity_proof": {"atom_id": old_id, "commit": commit, "path": old.relative, "digest": target["digest"]},
                "legacy_identity_mapping": {"legacy_atom_id": old_id, "atom_id": "CA-D-560",
                                            "destination": destination.relative_to(self.root).as_posix()}}, source, destination, original

    def test_approved_legacy_identity_encoding_preserves_exact_history_and_explicit_mapping(self) -> None:
        parameters, source, destination, before = self._mapped_delivery()
        preview = update_atom_action(self.root, parameters)
        self.assertEqual(preview["outcome"], "preview")
        self.assertEqual(source.read_bytes(), before)
        self.assertFalse(destination.exists())
        with self.assertRaisesRegex(LifecycleError, "authorization-required"):
            update_atom_action(self.root, parameters, execute=True)
        result = update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(result["observed"]["atom_id"], "CA-D-560")
        self.assertEqual(result["observed"]["version"], 8)
        self.assertFalse(source.exists())
        self.assertEqual(atom_from_path(self.root, destination).atom_id, "CA-D-560")
        self.assertEqual(result["history"]["identity_mapping"], parameters["legacy_identity_mapping"])
        self.assertEqual((self.root / result["history"]["prior_revision"]["path"]).read_bytes(), before)

    def test_identity_mapping_rejects_missing_proof_scope_change_summary_change_and_reserved_ids(self) -> None:
        parameters, source, destination, before = self._mapped_delivery()
        invalid = copy.deepcopy(parameters)
        del invalid["legacy_identity_proof"]
        with self.assertRaisesRegex(LifecycleError, "identity-mapping-invalid"):
            update_atom_action(self.root, invalid, execute=True, authorized=True)
        invalid = copy.deepcopy(parameters)
        invalid["legacy_identity_mapping"]["destination"] = (self.requirements / destination.name).relative_to(self.root).as_posix()
        with self.assertRaisesRegex(LifecycleError, "identity-mapping-invalid"):
            update_atom_action(self.root, invalid, execute=True, authorized=True)
        invalid = copy.deepcopy(parameters)
        invalid["proposed"]["content"] = invalid["proposed"]["content"].replace("Stable delivery", "Changed summary")
        with self.assertRaisesRegex(LifecycleError, "legacy-summary-changed"):
            update_atom_action(self.root, invalid, execute=True, authorized=True)
        archive = source.parent / "archive"
        archive.mkdir()
        (archive / "CA-D-560--reserved@1.md").write_text("legacy reserved ID", encoding="utf-8")
        with self.assertRaisesRegex(LifecycleError, "atom-id-collision"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(source.read_bytes(), before)
        self.assertFalse(destination.exists())

    def test_identity_mapping_cannot_renumber_a_current_ca_identity(self) -> None:
        parameters, before = self._legacy_update()
        parameters["legacy_identity_mapping"] = {"legacy_atom_id": "CA-R-100", "atom_id": "CA-R-999",
                                                  "destination": (self.requirements / "CA-R-999--changed.md").relative_to(self.root).as_posix()}
        parameters["proposed"]["frontmatter"] = parameters["proposed"]["frontmatter"].replace("CA-R-100", "CA-R-999")
        with self.assertRaisesRegex(LifecycleError, "legacy-proof-invalid"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(self.target.read_bytes(), before)

    def test_identity_encoding_migration_rolls_back_when_source_removal_fails(self) -> None:
        parameters, source, destination, before = self._mapped_delivery()
        original_unlink = Path.unlink

        def refuse_source(path: Path, *args: object, **kwargs: object) -> None:
            if path == source:
                raise PermissionError("fixture source-removal failure")
            original_unlink(path, *args, **kwargs)

        with patch.object(Path, "unlink", refuse_source):
            with self.assertRaisesRegex(PermissionError, "source-removal failure"):
                update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(source.read_bytes(), before)
        self.assertFalse(destination.exists())
        self.assertFalse((source.parent / "archive" / (source.stem + "@8.md")).exists())

    def test_replace_publishes_supplied_successors_then_archives_one_predecessor(self) -> None:
        first = self._carrier("CA-R-105", "first-replacement", "First replacement")
        second = self._carrier("CA-R-106", "second-replacement", "Second replacement")
        result = replace_atom_action(
            self.root,
            {
                "predecessor": carrier_descriptor(self.root, "CA-R-100"),
                "successors": [first, second],
                "status_model": self._model(),
            },
            execute=True,
            authorized=True,
        )

        predecessor = result["predecessor"]
        self.assertEqual(result["outcome"], "applied")
        self.assertEqual(len(result["successors"]), 2)
        self.assertFalse(self.target.exists())
        self.assertTrue((self.root / first["path"]).exists())
        self.assertTrue((self.root / second["path"]).exists())
        archived = self.root / predecessor["path"]
        self.assertTrue(archived.exists())
        self.assertIn("@1", archived.name)
        self.assertIn("status: Archived", archived.read_text(encoding="utf-8"))

    def test_replace_requires_prepared_new_successors_and_archives_only_after_all_are_active(self) -> None:
        first = self._carrier("CA-R-105", "first-replacement", "First replacement")
        second = self._carrier("CA-R-106", "second-replacement", "Second replacement")
        original_archive = __import__("lifecycle_intents").archive_atom_revision

        def verify_active_before_archive(root: Path, atom: object, frontmatter: str, content: str) -> object:
            for successor in (first, second):
                candidate = root / successor["path"]
                self.assertTrue(candidate.exists())
                self.assertIn("status: Active", candidate.read_text(encoding="utf-8"))
            return original_archive(root, atom, frontmatter, content)

        with patch("lifecycle_intents.archive_atom_revision", side_effect=verify_active_before_archive):
            result = replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"),
                 "successors": [first, second], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(["CA-R-105", "CA-R-106"], [row["atom_id"] for row in result["successors"]])

    def test_replace_rejects_preexisting_successor_without_archiving_predecessor(self) -> None:
        successor = self._carrier("CA-R-105", "already-present", "Already present")
        create_atom_action(self.root, {"carrier": successor}, execute=True, authorized=True)
        before = self.target.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "destination-collision"):
            replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"),
                 "successors": [successor], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual(before, self.target.read_bytes())

    def test_replace_rejects_preexisting_successor_id_at_unused_destination(self) -> None:
        existing = self._carrier("CA-R-105", "already-present", "Already present")
        create_atom_action(self.root, {"carrier": existing}, execute=True, authorized=True)
        replacement = self._carrier("CA-R-105", "new-destination", "Different destination")
        before_predecessor = self.target.read_bytes()
        before_existing = (self.root / existing["path"]).read_bytes()
        new_destination = self.root / replacement["path"]

        with self.assertRaisesRegex(LifecycleError, "atom-id-collision"):
            replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"),
                 "successors": [replacement], "status_model": self._model()},
                execute=True,
                authorized=True,
            )

        self.assertEqual(before_predecessor, self.target.read_bytes())
        self.assertEqual(before_existing, (self.root / existing["path"]).read_bytes())
        self.assertFalse(new_destination.exists())
        self.assertFalse((self.target.parent / "archive" / "CA-R-100--target@1.md").exists())

    def test_replace_rejects_caller_model_that_contradicts_current_authority(self) -> None:
        successor = self._carrier("CA-R-105", "forged-model", "Replacement summary")
        forged = self._model()
        forged["statuses"] = ["Active", "Reviewed", "Archived"]
        before = self.target.read_bytes()

        with self.assertRaisesRegex(LifecycleError, "model-forged"):
            replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"), "successors": [successor],
                 "status_model": forged},
                execute=True,
                authorized=True,
            )

        self.assertEqual(before, self.target.read_bytes())
        self.assertFalse((self.root / successor["path"]).exists())

    def test_source_model_status_noop_and_archive_relation_diagnostics(self) -> None:
        self.target.write_text(
            self.target.read_text(encoding="utf-8").replace("relations: {}", "relations:\n  depends_on: [CA-R-101]"),
            encoding="utf-8",
        )
        self._atom("CA-R-104", "inbound", "Inbound", relations="relations:\n  depends_on: [CA-R-100]")
        self.assertNotIn("type:", self.target.read_text(encoding="utf-8"))

        noop = change_status_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, "CA-R-100"), "status": "Active"},
            execute=True,
            authorized=True,
        )
        self.assertEqual(noop["outcome"], "no-op")

        archived = change_status_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, "CA-R-100"), "status": "Archived"},
            execute=True,
            authorized=True,
        )
        self.assertEqual(archived["outcome"], "applied")
        self.assertEqual({item["direction"] for item in archived["broken_references"]}, {"inbound", "outgoing"})
        self.assertEqual(archived["repair_handoff"]["operation"], "repair_relations")
        self.assertTrue(self.successor_one.exists())

    def test_replace_reports_partial_when_successor_or_archive_publication_fails(self) -> None:
        first = self._carrier("CA-R-105", "first-partial", "First partial")
        second = self._carrier("CA-R-106", "second-partial", "Second partial")
        original_create = __import__("lifecycle_intents").create_atom_revision
        calls = 0

        def fail_second(*args: object, **kwargs: object) -> object:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise ToolError("injected-successor-failure", "second successor failed")
            return original_create(*args, **kwargs)

        with patch("lifecycle_intents.create_atom_revision", side_effect=fail_second):
            partial = replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"), "successors": [first, second], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual(partial["outcome"], "partial")
        self.assertTrue((self.root / first["path"]).exists())
        self.assertFalse((self.root / second["path"]).exists())
        self.assertTrue(self.target.exists())
        self.assertEqual(partial["unknown_remainder"][0]["phase"], "publish_successor")

        archive_failure = self._carrier("CA-R-107", "archive-partial", "Archive partial")
        with patch("lifecycle_intents.archive_atom_revision", side_effect=ToolError("injected-archive-failure", "archive failed")):
            partial_archive = replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"), "successors": [archive_failure], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual(partial_archive["outcome"], "partial")
        self.assertTrue((self.root / archive_failure["path"]).exists())
        self.assertTrue(self.target.exists())
        self.assertEqual(partial_archive["unknown_remainder"][0]["phase"], "archive_predecessor")

    def test_stale_and_multi_target_requests_stop_before_an_effect(self) -> None:
        descriptor = carrier_descriptor(self.root, "CA-R-100")
        descriptor["digest"] = hashlib.sha256(b"stale").hexdigest()
        before = self.target.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "stale-carrier"):
            update_atom_action(
                self.root,
                {"target": descriptor, "proposed": self._proposal(self.target, summary="Stable summary"), "change_class": "carrier_only"},
                execute=True,
                authorized=True,
            )
        with self.assertRaisesRegex(LifecycleError, "mapping-required"):
            change_status_atom_action(
                self.root,
                {"target": [carrier_descriptor(self.root, "CA-R-100")], "status": "Archived"},
                execute=True,
                authorized=True,
            )
        self.assertEqual(self.target.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
