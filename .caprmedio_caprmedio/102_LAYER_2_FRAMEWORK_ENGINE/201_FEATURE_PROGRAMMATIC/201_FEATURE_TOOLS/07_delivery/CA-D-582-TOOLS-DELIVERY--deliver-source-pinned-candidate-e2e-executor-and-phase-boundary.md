---
atom_id: CA-D-582
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 20:54:31 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Candidate E2E executor carrier"
  depends_on: [Tool, Release Version, Candidate Manifest, Docker Image, Test Suite, JUnit Report, Journal]
relations:
  delivery_for: [CA-R-1890, CA-M-346]
---
# Summary

Deliver the source-pinned Candidate E2E executor and phase boundary

## Scope

The private host-side executor, sealed phase map, E2E report, and Full Gate input boundary.

## Claim

The Candidate E2E executor **must** accept only a sealed candidate manifest/image binding and closed phase map, execute exactly the three CA-R-1890 harnesses through fixed trusted-host Docker CLI vectors, and emit only source-pinned Candidate E2E evidence for later Full Gate aggregation.

## Details

1. the private executor, `run_release_e2e.py` Driver and sealed Harness context adapter **must** be delivered under `RELEASE_VERSION`. The Driver uses actual `unittest.TestResult` observations and the existing `run_release_suite.py` JUnit reporter semantics. Their absence before test-first implementation is not implementation evidence.
2. `release_e2e_bindings.json` is the schema-version **=1** static grammar Carrier. Its inspect vector is `["docker", "image", "inspect", "--format", "{{.Id}}", "{candidate_image_digest}"]`.
3. **every** Harness vector is `["{trusted_python}", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py", "--start-directory", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests", "--pattern", "<fixed Harness basename>", "--junit", "{e2e_junit_path}"]`. The **only** basenames are `test_docker_e2e.py`, `test_selected_workflows_docker_e2e.py` **and** `test_selected_query_mcp_e2e.py`.
4. the host controller derives the trusted Python, sealed Driver, `PATH`, `TMPDIR`, context Carrier **and** JUnit destination. The **only** child environment keys are `PATH`, `TMPDIR`, `CAPRMEDIO_RELEASE_E2E_CONTEXT` **and** `CAPRMEDIO_CANDIDATE_IMAGE_DIGEST`. The `--junit` argument is the **only** transport for the JUnit destination; it **must** match the destination derived from the sealed report root **and** fixed Harness. There is no JUnit environment override.
5. the closed context binds candidate Manifest SHA-256, inspected immutable image digest, sealed candidate workspace root, Phase Map SHA-256, grammar SHA-256 **and** executor-owned scratch/report roots. Source reads use the sealed read-only candidate workspace; writable fixtures use **only** dedicated scratch.
6. the Phase Map carries source path, SHA-256 **and** phase for **every** real sealed Test Module. The **=3** declared Harnesses have phase `candidate_e2e`; **all** other Test Modules have phase `unit`.
7. the sealed internal context provides fixed Harness admission values: `CAPRMEDIO_DOCKER_E2E=1` for Docker **and** selected-workflow Harnesses; `CAPRMEDIO_DOCKER_QUERY_E2E=1`, `CAPRMEDIO_DOCKER_QUERY_IMAGE={candidate_image_digest}` **and** `CAPRMEDIO_IMAGE={candidate_image_digest}` for the selected-query Harness. These values are read from the sealed context, not accepted from caller environment. **every** Harness uses the inspected immutable candidate image.
8. the configured limits are the **only** `[release_e2e]` parameters: `inspect_timeout_seconds`, `harness_timeout_seconds`, `cleanup_timeout_seconds`, `max_stdout_bytes`, `max_stderr_bytes` **and** `max_junit_bytes`. **every** value **must** be finite **and** **>0**. Explicit Framework Instance values fall back individually to the canonical `001_CORE_META_MODEL/caprmedio_framework_default_settings.toml` values.
9. the host-capable controller is explicit. Missing host capability, timeout, stdout/stderr/JUnit overflow, missing terminal outcome **or** uncertain Docker cleanup is non-passing. Retaining disposable directories is not a failure by itself. The controller accepts no caller command, path, image, tag **or** environment override **and** provides no generic remote interface, socket mount, privileged daemon, image pull, automatic retry **or** auto-run.
10. **every** Harness receipt carries candidate Manifest SHA-256, inspected candidate image digest, Phase Map SHA-256, grammar SHA-256, Harness path/SHA-256, exact argv, start/finish timestamps, exit/timeout outcome **and** bounded retained stdout, stderr **and** JUnit Carrier paths with their actual bytes' SHA-256 values. The Driver emits actual testcase outcomes, not XML guessed from process output.
11. Full Gate aggregation reopens these actual receipt Carriers **and** rejects missing, duplicate, altered, ambiguous, cross-candidate **or** binding-mismatched evidence. Retained command/result/JUnit bindings support canonical Journal admission.
12. this private delivery adds no public MCP route **or** selector. The closed Unit executor remains unchanged. CA-D-572 **must** explicitly admit the new Driver, executor, grammar, Harness **and** control Carriers **before** source-binding admission **or** Workflow dispatch; this Atom does not widen that frontier.
