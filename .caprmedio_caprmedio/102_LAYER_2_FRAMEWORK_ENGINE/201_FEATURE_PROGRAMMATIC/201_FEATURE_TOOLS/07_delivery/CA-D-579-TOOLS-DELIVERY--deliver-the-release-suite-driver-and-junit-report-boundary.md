---
atom_id: CA-D-579
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-06 00:17:58 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite driver carrier"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, JUnit Report, Runtime, MCP, Workflow, Source Carrier, Compiled Candidate]
relations:
  delivery_for: [CA-R-1886, CA-R-1887, CA-M-343, CA-M-344]
---
# Summary

Deliver the Release suite driver and JUnit report boundary

## Scope

The carrier and sealed-environment boundary for the unchanged closed RELEASE_VERSION Unit driver.

## Claim

The Release Unit driver **must** be delivered at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_suite.py` and accept only the sealed environment contract below to write its Unit JUnit report and source-bound Unit test evidence.

## Details

```toml
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_suite.py"
runner = "local-subprocess"
command = ["python", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_suite.py"]
working_directory = "."
report = "CAPRMEDIO_RELEASE_SUITE_REPORT"
source_bindings = "CAPRMEDIO_RELEASE_SOURCE_BINDINGS"
source_bindings_sha256 = "CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256"

[environment]
required = [
  "CAPRMEDIO_RELEASE_PROJECT_ROOT",
  "CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT",
  "CAPRMEDIO_RELEASE_CANDIDATE_MANIFEST_SHA256",
  "CAPRMEDIO_RELEASE_SUITE_REPORT",
  "CAPRMEDIO_RELEASE_SOURCE_BINDINGS",
  "CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256",
]
forbidden = ["test_selector", "test_path", "report_path_override", "source_binding_override", "host_path"]

[execution]
temporary_directory = "/tmp"
python_bytecode = "disabled"

[source_bindings_contract]
path = "/workspace/.caprmedio_release/source_bindings.json"
producer = "RELEASE_VERSION suite owner"
source = "sealed compilation.package_rows"
schema_version = 2
top_level_fields = ["schema_version", "candidate_snapshot_manifest_sha256", "mapping_rules", "package_rows", "reference_rows", "control_context_digest"]
mapping_rules_fields = ["source_path", "sha256"]
package_row_fields = ["resource", "source_path", "destination_path", "sha256", "mode"]
reference_row_fields = ["source_path", "sha256", "mode"]
junit_case_properties = ["caprmedio.test_id", "caprmedio.source_bindings_sha256", "caprmedio.source_probe"]

[maintained_module_rules]
path = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_suite_bindings.json"
schema_version = 1
top_level_fields = ["schema_version", "module_probes"]
module_probe_fields = ["test_module_source_path", "source_paths"]
optional_module_probe_fields = ["compiled_candidate_probe"]

[compiled_candidate_probe]
required_true_count = 1
test_module_source_path = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/tests/test_release_compilation.py"
selection = "first source-path-sorted sealed METHODOLOGY package row beneath the bound compiled-candidate root"
absent_flag = false

[sandbox_paths]
project_root = "/workspace"
source_bindings = "/workspace/.caprmedio_release/source_bindings.json"
report = "/output/coverage.xml"
```

The Suite Owner reads the maintained module-rule carrier as a sealed package row, forms canonical JSON with the exact closed envelope above, writes it before the workspace is mounted read-only, and supplies its SHA-256 in `CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256`. The envelope's `mapping_rules` is an object with the listed source path and SHA-256; `package_rows` preserve the complete typed `compilation.package_rows` order. `reference_rows` are the source-path-sorted private closure from CA-D-580, with exactly the listed fields. `control_context_digest` is the exact private-context digest from CA-D-580 and is rederived before and after execution; it neither duplicates nor turns the existing trusted selected-N/image bindings into caller fields. The sealed phase map is separately derived from the same package rows before this fixed CLI is invoked: `candidate_e2e` is exactly `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`, and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`; every other declared test module is `unit`. The closed Unit test-module set is therefore the source-path-sorted `unit` subset of package-row paths matching `102_FRAMEWORK_ENGINE/**/test_*.py`. Module rules contain only source-path-sorted explicit probes for that Unit subset and may name only one of those test modules plus source-path-sorted package rows. Candidate-E2E modules are excluded only by that sealed assignment and never by a caller selector or a JUnit skip. The driver derives, rather than stores, **=1** binding record for each discovered Unit `unittest.TestCase.id()`: its source references are the test method definition carrier plus that module's explicit probes. Exactly one rule, for the named compilation module, must set the optional boolean `compiled_candidate_probe` to true; an absent flag means false. The driver and observer independently derive exactly the first source-path-sorted sealed METHODOLOGY row whose source path starts with the bound compiled-candidate root plus `/`, and require its exact probe. Reject non-boolean, duplicated or misplaced true flags, absence of a compiled row, and static source paths beneath that runtime root. This is one compiled-carrier integrity attestation, not a substitute for the complete compiled tree digest. The driver rejects an envelope whose schema, candidate digest, rule-carrier digest, row set, reference-row closure, control-context digest, Unit test-module set, probe target, derived test-ID/report-ID set, source reference, order, or SHA-256 is not exact. Each `caprmedio.source_probe` is canonical JSON with exactly `source_path` and `sha256`, and post-execution admission verifies it against the same envelope and sealed package rows. Actual Unit evidence carries the same `control_context_digest`. The driver writes **=1** JUnit testcase row per executed Unit test ID only at `CAPRMEDIO_RELEASE_SUITE_REPORT`, uses `/tmp` through `TMPDIR` for child-process temporary files and the writable `/output` mount for driver-owned result files, and records no host-absolute path. The production CLI validates the exact sandbox paths above before any read or output creation. Issuance and Unit admission require the exact declared driver command, not arbitrary manifest commands. Disposable tests may call private implementation functions with their own sealed fixture frame; they create no public CLI selector or override. It accepts no public MCP request, new Workflow, arbitrary test selector, path override, report override, caller-provided coverage claim, or arbitrary reference file. The existing RELEASE_VERSION Tool's sealed Unit invocation supplies this carrier contract; CA-D-582 defines the later private Candidate E2E executor but does not claim it is already implemented, and only their actual aggregate Full Gate can precede promotion.
