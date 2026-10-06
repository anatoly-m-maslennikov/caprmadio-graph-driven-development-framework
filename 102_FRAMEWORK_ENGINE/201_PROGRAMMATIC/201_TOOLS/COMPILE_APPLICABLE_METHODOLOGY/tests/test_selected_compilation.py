from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


TOOL = Path(__file__).resolve().parents[1] / "compile_applicable_methodology.py"
SPEC = importlib.util.spec_from_file_location("selected_compiler", TOOL)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)


def carrier(atom_id: str, *, relations: str = "{}", status: str = "Active", version: int = 1) -> bytes:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        f"status: {status}\n"
        f"version: {version}\n"
        "updated_at: 2026-10-04 00:00:00 +0400\n"
        f"relations: {relations}\n"
        "---\n"
        f"# {atom_id}\n\nclaim\n"
    ).encode()


class SelectedCompilationTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = Path.cwd() / ".caprmedio_tmp/selected-compilation-tests"
        temporary.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=temporary))
        self.control = self.root / ".caprmedio_caprmedio"
        self.source = self.control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for role in compiler.ROLE_BY_DIRECTORY:
                (self.source / layer / role).mkdir(parents=True, exist_ok=True)
        (self.source / "002_INSTALLED_EXTENSIONS").mkdir(parents=True)
        structure = self.control / "project_structure.toml"
        structure.parent.mkdir(parents=True, exist_ok=True)
        structure.write_text(
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            f"authority_path = {json.dumps(self.source.relative_to(self.root).as_posix())}\n"
            'delivery_path = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"\n'
        )
        (self.source / "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml").write_text("")
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text(
            "[extensions.example]\nenabled = true\nrevision = \"v2\"\n"
        )
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def write(self, relative: str, value: bytes) -> Path:
        path = self.source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value)
        return path

    def bindings(self) -> dict[str, str]:
        return compiler.governed_bindings(self.root, compiler.methodology_paths(self.root))

    def request(self, operation: str = "dry_run", **extra: object) -> dict[str, object]:
        result: dict[str, object] = {
            "operation": operation,
            "project_root": self.root.as_posix(),
            "governed_bindings": self.bindings(),
        }
        result.update(extra)
        return result

    def output_bytes(self) -> dict[str, bytes]:
        output = self.root / compiler.methodology_paths(self.root).output
        return {
            path.relative_to(output).as_posix(): path.read_bytes()
            for _, directory in compiler.ROLES
            for path in sorted((output / directory).rglob("*"))
            if path.is_file()
        }

    def test_golden_active_core_extension_and_project_configuration_preserve_source_fidelity(self) -> None:
        core = self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001", relations="\n  relates_to:\n    - CA-R-900"))
        extension = self.write("002_INSTALLED_EXTENSIONS/example/v2/05_method/CA-M-002--extension.md", carrier("CA-M-002"))
        project = self.write("003_PROJECT_CONFIGURATION/07_delivery/CA-D-003--project.md", carrier("CA-D-003"))
        before = {path: path.read_bytes() for path in (core, extension, project)}

        dry = compiler.run_request(self.request())
        self.assertEqual("assessed", dry["outcome"])
        self.assertEqual(["CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"], [row["source_layer"] for row in dry["source_frontier"]])
        self.assertEqual("example", dry["source_frontier"][1]["extension_id"])
        self.assertEqual("v2", dry["source_frontier"][1]["extension_revision"])

        applied = compiler.run_request(self.request("apply", expected_source_frontier_digest=dry["source_frontier_digest"]))
        self.assertEqual("pending_recording", applied["outcome"])
        self.assertEqual(before, {path: path.read_bytes() for path in before})
        output = self.root / compiler.methodology_paths(self.root).output / "04_requirement" / core.name
        self.assertEqual(self.control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/04_requirement" / core.name, output)
        rendered = output.read_bytes()
        self.assertIn(b"  source_atom_id: CA-R-001", rendered)
        self.assertIn(b"  original_relations_sha256:", rendered)
        self.assertIn(b"  relates_to:\n    - CA-R-900", rendered)

    def test_configured_control_root_owns_projection_and_canonical_journal(self) -> None:
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_test_control"\n'
        )
        places = compiler.methodology_paths(self.root)
        self.assertEqual(Path(".caprmedio_test_control/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"), places.output)
        journal = self.root / ".caprmedio_test_control/_journal/decisions.ndjson"
        journal.parent.mkdir(parents=True)
        journal.write_text(json.dumps({"event_id": "decision-1", "event_digest": "digest-1"}) + "\n")

        record = compiler.journal_record(
            self.root,
            ".caprmedio_test_control/_journal/decisions.ndjson#decision-1",
            "digest-1",
            places,
        )

        self.assertEqual("decision-1", record["event_id"])

    def test_strict_request_boundary_rejects_unauthorized_fields_without_effects(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        before = compiler.source_state_snapshot(self.root, compiler.methodology_paths(self.root))
        for prohibited in (
            "source_root", "output_path", "edit_source", "source_patch", "selected_candidate", "approval_text", "approval", "journal_event", "unexpected_operation_field",
        ):
            with self.subTest(prohibited=prohibited):
                request = self.request()
                request[prohibited] = "caller-controlled"
                result = compiler.run_request(request)
                self.assertEqual("blocked", result["outcome"])
                self.assertIn(result["blocking_findings"][0]["code"], {"request-field-forbidden", "request-field-unknown"})
        self.assertEqual(before, compiler.source_state_snapshot(self.root, compiler.methodology_paths(self.root)))

    def test_toml_only_approval_is_not_a_decision_and_preserves_prior_output(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        self.write("003_PROJECT_CONFIGURATION/04_requirement/CA-R-001--project.md", carrier("CA-R-001", version=2))
        dry = compiler.run_request(self.request())
        approval = self.source / "003_PROJECT_CONFIGURATION/applicable_methodology_conflict_approvals.toml"
        approval.write_text('schema = "caprmedio.applicable_methodology_conflict_approvals.v1"\n')
        prior = self.root / compiler.methodology_paths(self.root).output
        prior.mkdir(parents=True, exist_ok=True)
        sentinel = prior / "sentinel"
        sentinel.write_text("prior")

        result = compiler.run_request(self.request("apply", expected_source_frontier_digest=dry["source_frontier_digest"]))
        self.assertEqual("blocked", result["outcome"])
        self.assertEqual("preserved", result["publication"]["prior_output_state"])
        self.assertEqual("prior", sentinel.read_text())

    def test_exact_canonical_journal_decision_is_required_then_source_change_forces_reassessment(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        selected = self.write("003_PROJECT_CONFIGURATION/04_requirement/CA-R-001--project.md", carrier("CA-R-001", version=2))
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text("")
        assessed = compiler.run_request(self.request())
        conflict = assessed["conflicts"][0]
        journal = self.control / "_journal/decisions.ndjson"
        journal.parent.mkdir(parents=True, exist_ok=True)
        event = {
            "event_id": "decision-1",
            "event_digest": "digest-1",
            "outcome": "approved",
            "operator": "TEST_OPERATOR",
            "details": {
                "conflict_id": conflict["conflict_id"],
                "source_frontier_digest": assessed["source_frontier_digest"],
                "selected_source_carrier_path": selected.relative_to(self.root).as_posix(),
            },
        }
        journal.write_text(json.dumps(event) + "\n")
        decision_refs = [{
            "conflict_id": conflict["conflict_id"],
            "journal_record_ref": journal.relative_to(self.root).as_posix() + "#decision-1",
            "journal_record_digest": "digest-1",
        }]
        applied = compiler.run_request(self.request("apply", expected_source_frontier_digest=assessed["source_frontier_digest"], decision_refs=decision_refs))
        self.assertEqual("pending_recording", applied["outcome"])
        self.assertEqual(selected.relative_to(self.root).as_posix(), applied["output_plan"][0]["source_carrier_path"])
        self.assertEqual(selected.relative_to(self.root).as_posix(), applied["decision_provenance"][0]["selected_source_carrier_path"])

        selected.write_bytes(carrier("CA-R-001", version=3))
        stale = compiler.run_request(self.request("apply", expected_source_frontier_digest=assessed["source_frontier_digest"], decision_refs=decision_refs))
        self.assertEqual("blocked", stale["outcome"])
        self.assertEqual("decision-source-frontier-stale", stale["blocking_findings"][0]["code"])

    def test_rejected_and_stale_canonical_decisions_preserve_prior_projection(self) -> None:
        core = self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text("")
        initial = compiler.run_request(self.request())
        self.assertEqual("pending_recording", compiler.run_request(self.request("apply", expected_source_frontier_digest=initial["source_frontier_digest"]))["outcome"])
        before = self.output_bytes()
        selected = self.write("003_PROJECT_CONFIGURATION/04_requirement/CA-R-001--project.md", carrier("CA-R-001", version=2))
        assessed = compiler.run_request(self.request())
        conflict = assessed["conflicts"][0]
        journal = self.control / "_journal/decisions.ndjson"
        journal.parent.mkdir(parents=True)

        for outcome, digest, expected in (
            ("rejected", assessed["source_frontier_digest"], "decision-journal-not-approved"),
            ("approved", "stale-frontier", "decision-source-frontier-stale"),
        ):
            with self.subTest(outcome=outcome):
                journal.write_text(json.dumps({
                    "event_id": "decision-1",
                    "event_digest": "digest-1",
                    "outcome": outcome,
                    "operator": "TEST_OPERATOR",
                    "details": {
                        "conflict_id": conflict["conflict_id"],
                        "source_frontier_digest": digest,
                        "selected_source_carrier_path": selected.relative_to(self.root).as_posix(),
                    },
                }) + "\n")
                result = compiler.run_request(self.request(
                    "apply",
                    expected_source_frontier_digest=assessed["source_frontier_digest"],
                    decision_refs=[{
                        "conflict_id": conflict["conflict_id"],
                        "journal_record_ref": journal.relative_to(self.root).as_posix() + "#decision-1",
                        "journal_record_digest": "digest-1",
                    }],
                ))
                self.assertEqual("blocked", result["outcome"])
                self.assertEqual(expected, result["blocking_findings"][0]["code"])
                self.assertEqual("preserved", result["publication"]["prior_output_state"])
                self.assertEqual(before, self.output_bytes())

        self.assertTrue(core.is_file())

    def test_source_correction_handoff_requires_fresh_selection_and_assessment(self) -> None:
        selected = self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text("")
        before = compiler.source_state_snapshot(self.root, compiler.methodology_paths(self.root))
        initial_selection = compiler.select_sources_action(self.request())
        handoff = compiler.apply_corrections_action(self.request())

        self.assertEqual("reassess_required", handoff["outcome"])
        self.assertFalse(handoff["source_edit_supported"])
        self.assertEqual("source_owner_correction_request", handoff["correction_request_or_receipt"]["kind"])
        self.assertEqual(["CA-O-004", "CA-O-005"], handoff["correction_request_or_receipt"]["required_follow_up_actions"])
        self.assertEqual(before, compiler.source_state_snapshot(self.root, compiler.methodology_paths(self.root)))

        selected.write_bytes(carrier("CA-R-001", version=2))
        reselection = compiler.select_sources_action(self.request())
        reassessment = compiler.assess_sources_action(self.request())
        self.assertNotEqual(initial_selection["source_frontier_digest"], reselection["source_frontier_digest"])
        self.assertEqual(reselection["source_frontier_digest"], reassessment["source_frontier_digest"])
        self.assertEqual("assessed", reassessment["outcome"])

    def test_source_change_after_staging_preserves_prior_output_before_publication(self) -> None:
        source = self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text("")
        initial = compiler.run_request(self.request())
        self.assertEqual(
            "pending_recording",
            compiler.run_request(self.request("apply", expected_source_frontier_digest=initial["source_frontier_digest"]))["outcome"],
        )
        before = self.output_bytes()
        assessed = compiler.run_request(self.request())
        real_stage = compiler.stage_outputs
        real_replace = compiler.replace_outputs_atomically
        staged: list[Path] = []

        def stage_then_change_source(*args: object, **kwargs: object) -> Path:
            staging = real_stage(*args, **kwargs)
            staged.append(staging)
            source.write_bytes(carrier("CA-R-001", version=2))
            return staging

        with mock.patch.object(compiler, "stage_outputs", side_effect=stage_then_change_source), mock.patch.object(
            compiler, "replace_outputs_atomically", wraps=real_replace
        ) as replace_outputs:
            result = compiler.run_request(self.request(
                "apply", expected_source_frontier_digest=assessed["source_frontier_digest"]
            ))

        self.assertEqual("blocked", result["outcome"])
        self.assertEqual("BLOCKED", result["apply_status"])
        self.assertEqual("source-frontier-changed", result["blocking_findings"][0]["code"])
        self.assertEqual("before-publication", result["blocking_findings"][0]["details"]["phase"])
        self.assertEqual("preserved", result["publication"]["prior_output_state"])
        self.assertFalse(replace_outputs.called)
        self.assertEqual(before, self.output_bytes())
        self.assertTrue(staged)
        self.assertTrue(all(not path.exists() for path in staged))

    def test_source_change_after_output_replacement_requires_recovery_without_success_claim(self) -> None:
        source = self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text("")
        initial = compiler.run_request(self.request())
        self.assertEqual(
            "pending_recording",
            compiler.run_request(self.request("apply", expected_source_frontier_digest=initial["source_frontier_digest"]))["outcome"],
        )
        before = self.output_bytes()
        source.write_bytes(carrier("CA-R-001", version=2))
        assessed = compiler.run_request(self.request())
        real_replace = compiler.replace_outputs_atomically

        def replace_then_change_source(*args: object, **kwargs: object) -> None:
            real_replace(*args, **kwargs)
            source.write_bytes(carrier("CA-R-001", version=3))

        with mock.patch.object(compiler, "replace_outputs_atomically", side_effect=replace_then_change_source):
            result = compiler.run_request(self.request(
                "apply", expected_source_frontier_digest=assessed["source_frontier_digest"]
            ))

        self.assertEqual("publication_recovery_required", result["outcome"])
        self.assertEqual("EFFECT_APPLIED_STALE", result["apply_status"])
        self.assertFalse(result["publishable"])
        self.assertEqual("source-frontier-changed-after-output-replacement", result["blocking_findings"][0]["code"])
        self.assertEqual("output_replacement_completed", result["publication"]["effect_state"])
        self.assertEqual("source_frontier_changed_after_prepublication_check", result["publication"]["freshness_state"])
        self.assertIn("output_digest", result["publication"])
        self.assertNotEqual(before, self.output_bytes())

    def test_publication_failure_and_uncertainty_report_no_success_receipt(self) -> None:
        requirement = self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        method = self.write("001_CORE_META_MODEL/05_method/CA-M-001--core.md", carrier("CA-M-001"))
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text("")
        initial = compiler.run_request(self.request())
        self.assertEqual("pending_recording", compiler.run_request(self.request("apply", expected_source_frontier_digest=initial["source_frontier_digest"]))["outcome"])
        before = self.output_bytes()
        requirement.write_bytes(carrier("CA-R-001", version=2))
        method.write_bytes(carrier("CA-M-001", version=2))
        current = compiler.run_request(self.request())
        real_replace = compiler.os.replace

        calls = 0

        def fail_second(source: Path, target: Path) -> None:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("injected publication failure")
            real_replace(source, target)

        with mock.patch.object(compiler.os, "replace", side_effect=fail_second):
            failed = compiler.run_request(self.request("apply", expected_source_frontier_digest=current["source_frontier_digest"]))
        self.assertEqual("blocked", failed["outcome"])
        self.assertEqual("atomic-replacement-failed", failed["blocking_findings"][0]["code"])
        self.assertEqual("preserved", failed["publication"]["prior_output_state"])
        self.assertEqual([], failed["run_receipt_refs"])
        self.assertEqual(before, self.output_bytes())

        calls = 0

        def fail_replacement_and_rollback(source: Path, target: Path) -> None:
            nonlocal calls
            calls += 1
            if calls in {2, 3}:
                raise OSError("injected uncertain recovery")
            real_replace(source, target)

        with mock.patch.object(compiler.os, "replace", side_effect=fail_replacement_and_rollback):
            uncertain = compiler.run_request(self.request("apply", expected_source_frontier_digest=current["source_frontier_digest"]))
        self.assertEqual("blocked", uncertain["outcome"])
        self.assertEqual("atomic-replacement-uncertain", uncertain["blocking_findings"][0]["code"])
        self.assertEqual("uncertain", uncertain["publication"]["prior_output_state"])
        self.assertEqual([], uncertain["run_receipt_refs"])

    def test_recovery_requires_canonical_failed_publication_evidence_and_preserves_shared_receipt_context(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text("")
        assessed = compiler.run_request(self.request())
        missing = compiler.run_request(self.request("recover_publication", expected_source_frontier_digest=assessed["source_frontier_digest"]))
        self.assertEqual("blocked", missing["outcome"])
        self.assertEqual("request-recovery-evidence-missing", missing["blocking_findings"][0]["code"])
        not_canonical = compiler.run_request(self.request("recover_publication", expected_source_frontier_digest=assessed["source_frontier_digest"], failed_publication_ref="journal://failed-publication-1"))
        self.assertEqual("decision-journal-reference-invalid", not_canonical["blocking_findings"][0]["code"])

        journal = self.control / "_journal/publications.ndjson"
        journal.parent.mkdir(parents=True)
        journal.write_text(json.dumps({
            "event_id": "failed-publication-1",
            "event_digest": "failed-publication-digest",
            "event": "failed",
            "outcome": "failed",
            "details": {"source_frontier_digest": assessed["source_frontier_digest"]},
        }) + "\n")
        shared_refs = [{"run_id": "shared-action-run"}]
        recovered = compiler.run_request(self.request(
            "recover_publication",
            expected_source_frontier_digest=assessed["source_frontier_digest"],
            failed_publication_ref=journal.relative_to(self.root).as_posix() + "#failed-publication-1",
            run_receipt_refs=shared_refs,
        ))
        self.assertEqual("pending_recording", recovered["outcome"])
        self.assertEqual(shared_refs, recovered["run_receipt_refs"])
        self.assertEqual(journal.relative_to(self.root).as_posix() + "#failed-publication-1", recovered["evidence_refs"]["failed_publication"]["failed_publication_ref"])

        published_handoff = compiler.publish_action(self.request(
            "apply",
            expected_source_frontier_digest=assessed["source_frontier_digest"],
            run_receipt_refs=shared_refs,
        ))
        self.assertEqual("pending_recording", published_handoff["outcome"])
        self.assertEqual(shared_refs, published_handoff["run_receipt_refs"])
        self.assertEqual("shared_passthrough_pending_canonical_recording", published_handoff["action_handoff"]["run_receipt_behavior"])

        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001", version=2))
        stale = compiler.run_request(self.request(
            "recover_publication",
            expected_source_frontier_digest=assessed["source_frontier_digest"],
            failed_publication_ref=journal.relative_to(self.root).as_posix() + "#failed-publication-1",
        ))
        self.assertEqual("blocked", stale["outcome"])
        self.assertEqual("recovery-source-frontier-stale", stale["blocking_findings"][0]["code"])

    def test_inactive_or_unselected_extension_is_excluded_and_not_published(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        self.write("002_INSTALLED_EXTENSIONS/example/v1/05_method/CA-M-001--old.md", carrier("CA-M-001"))
        inactive = self.write("002_INSTALLED_EXTENSIONS/example/v2/05_method/CA-M-002--inactive.md", carrier("CA-M-002", status="Inactive"))
        result = compiler.run_request(self.request())
        self.assertEqual("blocked", result["outcome"])
        exclusions = {row["source_carrier_path"]: row["reason"] for row in result["excluded_candidates"]}
        self.assertEqual("extension-revision-unselected", exclusions[(self.source / "002_INSTALLED_EXTENSIONS/example/v1/05_method/CA-M-001--old.md").relative_to(self.root).as_posix()])
        self.assertEqual("inactive", exclusions[inactive.relative_to(self.root).as_posix()])

    def test_every_settings_activated_extension_revision_is_retained(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        self.write("002_INSTALLED_EXTENSIONS/example/v2/05_method/CA-M-002--example.md", carrier("CA-M-002"))
        self.write("002_INSTALLED_EXTENSIONS/other/r7/06_evaluation/CA-E-003--other.md", carrier("CA-E-003"))
        self.write("003_PROJECT_CONFIGURATION/07_delivery/CA-D-004--project.md", carrier("CA-D-004"))
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text(
            "[extensions.example]\nenabled = true\nrevision = \"v2\"\n\n"
            "[extensions.other]\nenabled = true\nrevision = \"r7\"\n"
        )

        result = compiler.run_request(self.request())

        self.assertEqual("assessed", result["outcome"])
        extensions = {(row.get("extension_id"), row.get("extension_revision")) for row in result["source_frontier"] if row["source_layer"] == "INSTALLED_EXTENSIONS"}
        self.assertEqual({("example", "v2"), ("other", "r7")}, extensions)

    def test_cli_remains_a_json_compatibility_wrapper(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text("")
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            exit_code = compiler.run(["--root", self.root.as_posix()])
        self.assertEqual(0, exit_code)
        self.assertEqual("assessed", json.loads(stream.getvalue())["outcome"])


if __name__ == "__main__":
    unittest.main()
