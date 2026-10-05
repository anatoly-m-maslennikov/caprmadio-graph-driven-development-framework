---
atom_id: CA-D-579
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 22:00:58 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite driver carrier"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, JUnit Report, Runtime, MCP, Workflow, Source Carrier, Compiled Candidate]
relations:
  delivery_for: [CA-R-1886, CA-M-343]
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
schema_version = 1
top_level_fields = ["schema_version", "candidate_snapshot_manifest_sha256", "mapping_rules", "package_rows"]
mapping_rules_fields = ["source_path", "sha256"]
package_row_fields = ["resource", "source_path", "destination_path", "sha256", "mode"]
junit_case_properties = ["caprmedio.test_id", "caprmedio.source_bindings_sha256", "caprmedio.source_probe"]

[maintained_module_rules]
path = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_suite_bindings.json"
schema_version = 1
top_level_fields = ["schema_version", "module_probes"]
module_probe_fields = ["test_module_source_path", "source_paths"]
```

The Suite Owner reads the maintained module-rule carrier as a sealed package row, forms canonical JSON with the exact closed envelope above, writes it before the workspace is mounted read-only, and supplies its SHA-256 in `CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256`. The envelope's `mapping_rules` is an object with the listed source path and SHA-256; `package_rows` preserve the complete typed `compilation.package_rows` order. The complete test-module set is derived from package-row source paths matching `102_FRAMEWORK_ENGINE/**/test_*.py`, sorted by source path; module rules contain only source-path-sorted explicit probes and may name only one of those test modules plus source-path-sorted package rows. The driver derives, rather than stores, **=1** binding record for each discovered `unittest.TestCase.id()`: its source references are the test method definition carrier plus that module's explicit probes. The driver rejects an envelope whose schema, candidate digest, rule-carrier digest, row set, test-module set, probe target, derived test-ID/report-ID set, source reference, order, or SHA-256 is not exact. Each `caprmedio.source_probe` is canonical JSON with exactly `source_path` and `sha256`, and post-execution admission verifies it against the same envelope and sealed package rows. The driver writes **=1** JUnit testcase row per executed test ID only at `CAPRMEDIO_RELEASE_SUITE_REPORT`, uses `/tmp` and the writable output mount for temporary fixtures, and records no host-absolute path. It accepts no public MCP request, new Workflow, arbitrary test selector, path override, report override, or caller-provided coverage claim. The existing RELEASE_VERSION Tool's sealed suite invocation supplies this carrier contract.
