---
atom_id: CA-D-579
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-05 18:54:35 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite driver carrier"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, JUnit Report, Runtime, MCP, Workflow, Source Carrier, Compiled Candidate]
relations:
  delivery_for: [CA-R-1886, CA-R-1887, CA-M-343, CA-M-344]
---
# Summary

Deliver the Release suite driver and JUnit report boundary

## Scope

The carrier and sealed-environment boundary for the RELEASE_VERSION full-suite driver.

## Claim

The Release suite driver **must** be delivered at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_suite.py` and accept only the sealed environment contract below to write its JUnit report and source-bound test evidence.

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

[source_bindings]
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

The Suite Owner reads the maintained module-rule carrier as a sealed package row, forms canonical JSON with the exact closed envelope above, writes it before the workspace is mounted read-only, and supplies its SHA-256 in `CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256`. The envelope's `mapping_rules` is an object with the listed source path and SHA-256; `package_rows` preserve the complete typed `compilation.package_rows` order. `reference_rows` are the source-path-sorted private closure from CA-D-580, with exactly the listed fields. `control_context_digest` is the exact private-context digest from CA-D-580 and is rederived before and after execution; it neither duplicates nor turns the existing trusted selected-N/image bindings into caller fields. The complete test-module set is derived from package-row source paths matching `102_FRAMEWORK_ENGINE/**/test_*.py`, sorted by source path; module rules contain only source-path-sorted explicit probes and may name only one of those test modules plus source-path-sorted package rows. The driver derives, rather than stores, **=1** binding record for each discovered `unittest.TestCase.id()`: its source references are the test method definition carrier plus that module's explicit probes. Exactly one rule, for the named compilation module, must set the optional boolean `compiled_candidate_probe` to true; an absent flag means false. The driver and observer independently derive exactly the first source-path-sorted sealed METHODOLOGY row whose source path starts with the bound compiled-candidate root plus `/`, and require its exact probe. Reject non-boolean, duplicated or misplaced true flags, absence of a compiled row, and static source paths beneath that runtime root. This is one compiled-carrier integrity attestation, not a substitute for the complete compiled tree digest. The driver rejects an envelope whose schema, candidate digest, rule-carrier digest, row set, reference-row closure, control-context digest, test-module set, probe target, derived test-ID/report-ID set, source reference, order, or SHA-256 is not exact. Each `caprmedio.source_probe` is canonical JSON with exactly `source_path` and `sha256`, and post-execution admission verifies it against the same envelope and sealed package rows. Actual suite evidence carries the same `control_context_digest`. The driver writes **=1** JUnit testcase row per executed test ID only at `CAPRMEDIO_RELEASE_SUITE_REPORT`, uses `/tmp` through `TMPDIR` for child-process temporary files and the writable `/output` mount for driver-owned result files, and records no host-absolute path. The production CLI validates the exact sandbox paths above before any read or output creation. Issuance and suite admission require the exact declared driver command, not arbitrary manifest commands. Disposable tests may call private implementation functions with their own sealed fixture frame; they create no public CLI selector or override. It accepts no public MCP request, new Workflow, arbitrary test selector, path override, report override, caller-provided coverage claim, or arbitrary reference file. The existing RELEASE_VERSION Tool's sealed suite invocation supplies this carrier contract.
