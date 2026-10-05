"""Pure sealed-envelope handoff tests for the Release suite owner."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_handoff import PackageRow  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_suite import (  # noqa: E402
    COMPILED_PROBE_TEST_MODULE,
    MODULE_RULES_RELATIVE,
    SUITE_DRIVER_COMMAND,
    SUITE_DRIVER_WORKING_DIRECTORY,
    _source_bindings_bytes,
    _trusted_context_bindings,
    require_declared_suite_command,
)


class ReleaseSuiteBindingsHandoffTests(unittest.TestCase):
    """The envelope is derived only from sealed typed package rows."""

    def setUp(self) -> None:
        # Retain the tiny carrier: the suite itself retains evidence and this
        # macOS profile can deny nested temporary-directory cleanup.
        self.root = Path(tempfile.mkdtemp(prefix="release-suite-bindings-")).resolve()
        self.test_source = COMPILED_PROBE_TEST_MODULE
        self.probe_source = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        self.compiled_source = ".caprmedio_caprmedio/compiled/candidate/module.md"
        self.rule_source = MODULE_RULES_RELATIVE
        payloads = {
            self.test_source: b"import unittest\n",
            self.probe_source: b"VALUE = 1\n",
            self.compiled_source: b"compiled\n",
        }
        for relative, payload in payloads.items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
        rules = {
            "schema_version": 1,
            "module_probes": [{
                "test_module_source_path": self.test_source,
                "source_paths": [self.probe_source],
                "compiled_candidate_probe": True,
            }],
        }
        rule_path = self.root / self.rule_source
        rule_path.parent.mkdir(parents=True, exist_ok=True)
        rule_path.write_bytes(json.dumps(rules, sort_keys=True, separators=(",", ":")).encode("utf-8"))
        engine_rows = [
            PackageRow(
                resource="FRAMEWORK_ENGINE",
                source_path=relative,
                destination_path="FRAMEWORK_ENGINE/" + relative.removeprefix("102_FRAMEWORK_ENGINE/"),
                sha256=hashlib.sha256((self.root / relative).read_bytes()).hexdigest(),
                mode=0o644,
            )
            for relative in (self.probe_source, self.rule_source, self.test_source)
        ]
        self.rows = engine_rows + [PackageRow(
            resource="METHODOLOGY",
            source_path=self.compiled_source,
            destination_path="METHODOLOGY/compiled/candidate/module.md",
            sha256=hashlib.sha256((self.root / self.compiled_source).read_bytes()).hexdigest(),
            mode=0o644,
        )]
        self.context = SimpleNamespace(reference_rows=(), control_context_digest="b" * 64)

    def test_envelope_preserves_package_order_and_binds_rule_digest(self) -> None:
        payload = _source_bindings_bytes(
            self.root, "a" * 64, self.rows, ".caprmedio_caprmedio/compiled/candidate", self.context,
        )

        envelope = json.loads(payload)
        self.assertEqual(envelope["schema_version"], 2)
        self.assertEqual(envelope["candidate_snapshot_manifest_sha256"], "a" * 64)
        self.assertEqual(envelope["reference_rows"], [])
        self.assertEqual(envelope["control_context_digest"], "b" * 64)
        self.assertEqual(envelope["mapping_rules"], {
            "source_path": self.rule_source,
            "sha256": self.rows[1].sha256,
        })
        self.assertEqual([row["source_path"] for row in envelope["package_rows"]],
                         [row.source_path for row in self.rows])

    def test_rejects_rule_probe_not_present_in_sealed_rows(self) -> None:
        rule_path = self.root / self.rule_source
        rule_path.write_text(json.dumps({
            "schema_version": 1,
            "module_probes": [{
                "test_module_source_path": self.test_source,
                "source_paths": ["102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/missing.py"],
                "compiled_candidate_probe": True,
            }],
        }, sort_keys=True, separators=(",", ":")), encoding="utf-8")
        self.rows[1] = self.rows[1].model_copy(update={
            "sha256": hashlib.sha256(rule_path.read_bytes()).hexdigest(),
        })

        with self.assertRaisesRegex(ReleaseContractError, "module probe"):
            _source_bindings_bytes(
                self.root, "a" * 64, self.rows, ".caprmedio_caprmedio/compiled/candidate", self.context,
            )

    def test_rejects_invalid_compiled_candidate_probe_declarations(self) -> None:
        base = {
            "test_module_source_path": self.test_source,
            "source_paths": [self.probe_source],
            "compiled_candidate_probe": True,
        }
        cases = {
            "non_boolean": [{**base, "compiled_candidate_probe": "true"}],
            "absent": [{**base, "compiled_candidate_probe": False}],
            "duplicate": [base, base],
            "static_compiled": [{**base, "source_paths": [self.compiled_source]}],
        }
        for label, probes in cases.items():
            with self.subTest(label=label):
                rule_path = self.root / self.rule_source
                rule_path.write_bytes(json.dumps({
                    "schema_version": 1,
                    "module_probes": probes,
                }, sort_keys=True, separators=(",", ":")).encode("utf-8"))
                self.rows[1] = self.rows[1].model_copy(update={
                    "sha256": hashlib.sha256(rule_path.read_bytes()).hexdigest(),
                })
                with self.assertRaises(ReleaseContractError):
                    _source_bindings_bytes(
                        self.root, "a" * 64, self.rows, ".caprmedio_caprmedio/compiled/candidate", self.context,
                    )

    def test_declared_driver_command_has_no_manifest_command_fallback(self) -> None:
        declared = SimpleNamespace(
            runner="local-subprocess",
            command=list(SUITE_DRIVER_COMMAND),
            working_directory=SUITE_DRIVER_WORKING_DIRECTORY,
        )
        require_declared_suite_command(declared)
        with self.assertRaises(ReleaseContractError):
            require_declared_suite_command(SimpleNamespace(
                runner="local-subprocess", command=["python", "-m", "unittest"], working_directory=".",
            ))

    def test_fresh_executor_image_context_changes_the_revalidation_bindings(self) -> None:
        candidate = SimpleNamespace(manifest=SimpleNamespace(sha256="a" * 64))
        compilation = SimpleNamespace(child_materialization_root=".caprmedio_caprmedio/compiled/candidate")
        before = _trusted_context_bindings(
            candidate, compilation, SimpleNamespace(source_context_sha256="b" * 64), "N",
        )
        after = _trusted_context_bindings(
            candidate, compilation, SimpleNamespace(source_context_sha256="c" * 64), "N",
        )
        self.assertNotEqual(before, after)
        self.assertEqual(after["selected_n_image_context"], "c" * 64)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
