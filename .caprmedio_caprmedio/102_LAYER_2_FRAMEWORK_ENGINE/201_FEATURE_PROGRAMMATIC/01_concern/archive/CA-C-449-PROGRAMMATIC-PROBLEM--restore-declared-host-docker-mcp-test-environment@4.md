---
atom_id: CA-C-449
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-05 13:18:22 +0000"
subjects:
  governs: "Host Docker MCP test environment"
  depends_on: [Implementation, Evaluation, Workflow, MCP]
relations:
  concern_about: [CA-P-1600, CA-P-1601, CA-P-1602, CA-P-1603, CA-P-1604, CA-P-1528, CA-P-1519, CA-P-1708, CA-P-1710, CA-P-1712]
---
# Summary

Restore declared host Docker MCP test environment

## Concern

The declared host test dependencies are available, but the current session again denies Docker API access and atomic directory publication. These execution restrictions leave host Release regression, real installation and fresh immutable-image acceptance incomplete.

## Evidences

- Revision 1 preserves the original empty repository environment and distribution-cache rename failures. The Operator then widened the access profile and requested another attempt.
- That attempt encountered a network allowlist denial for files.pythonhosted.org. Offline provisioning lacked the exact MCP wheel and the psycopg-binary wheel required by DBOS. A newly created empty directory inside the original UV cache still failed to rename with EPERM; cleanup of that empty probe was also denied. No alternate endpoint, permission modification or denial bypass followed.
- The Operator installed the declared groups in .caprmedio_runtime/host-tests from macOS Terminal. Import verification now succeeds for MCP 2.3.0, DBOS 2.31.1, PyYAML 6.0.3, jsonschema 4.26.0 and pydantic 2.13.5. The broken repository .venv was preserved.
- SelectedDockerHarnessTransportTests passed 3/3 in 2.475 seconds: actual MCP stdio reconnection and structured results, refusal of error/text-only pseudo-results, and container-visible fixture input roots.
- The W01-W15/J01-J08 golden-corpus check passed 1/1 in 1.731 seconds. It verifies the bound fixture corpus, not Workflow execution or Docker behavior.
- The fresh Docker image inventory attempt failed with permission denied while trying to connect to unix:///Users/am/.docker/run/docker.sock. Read-only inspection shows the socket belongs to am with mode srwxr-xr-x; no file mode or Docker endpoint was changed. This evidence does not establish the origin of the connection denial.
- The Operator-directed cleanup removed unused image sha256:057792974dc2d81f84f99dee5535a44d5ee30513b03f6154381d99aa0bd558cd. It is no longer a usable acceptance image. A newly built source-bound image will be required before the image batches can be accepted.
- After the Operator reloaded the permission profile, Docker image inventory succeeded. It lists the identity-mapping development image, Python base and Alpine base; the old acceptance image is absent. This clears the socket-access blocker, not any functional acceptance gate.
- The host Release regression invocation using `.caprmedio_runtime/host-tests/bin/python -B -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/tests -p 'test_release*.py' -q` exited 1. Its output contains `PermissionError: [Errno 1] Operation not permitted` for cleanup beneath `/tmp/tmpejw78nkw/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP`, including rmdir/unlink. Other disposable fixture paths also failed cleanup. No permission modification, equivalent retry or alternate-path cleanup followed.
- The same invocation reported `release-action-frozen-binding-mismatch` in Release Action tests. P1712 corrects their macOS /tmp versus /private/tmp fixture aliases and adds a root-equality regression without changing production checks or cleanup. AST checks pass; fixture execution remains unverified under this separate permission boundary.
- P1710's focused provider run also failed fourteen fixture cleanups, first under /tmp/tmpe5spxd0y/.caprmedio_install/workflow_orchestrator/runs/fixture-workflow. Its three pure result conversion checks pass, but the fixture run is not a pass. No cleanup suppression or alternate-path rerun occurred.
- The independent compiler location/selection/expansion suite passed40/40. This is narrow compiler regression evidence, not Release, Docker or Workflow acceptance.
- The Operator's macOS Terminal successfully accessed Docker and removed the original empty fixture directory. With Codex sandboxing disabled, Docker inventory and a new temporary-directory create/remove probe both passed. After returning to am-default, Docker inventory passed and temporary-file create/remove passed, but removal of a new empty directory still returned EPERM. This isolates the observed directory-cleanup restriction to the managed execution environment; its exact enforcement cause remains unconfirmed. The Operator instructed leaving that empty directory untouched. No cleanup suppression or host fixture acceptance followed.
- The Operator subsequently directed leaving all test fixture directories in place, so cleanup is no longer an acceptance blocker. An explicit test-only retention runner detaches TemporaryDirectory finalizers, declares retained paths and preserves original test assertions and failure exit codes; production cleanup and publication are unchanged.
- Under that retention policy the current Release source-admission and manifest suites passed 15/15. The canonical selected manifest remains fifteen routes. The complete Release Action suite passed 15/23; eight cases stopped at source publication. The retained original exception is `PermissionError: [Errno 1] Operation not permitted` while atomically renaming a `.release-sources-*` staging directory to `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources`. No Docker effect was reached.
- A retained Release-suite golden case independently failed before its functional assertions at the atomic `.release-render-*` staging-directory rename to `_release_materialized/<digest>`. This is an effect/publication permission denial, not fixture teardown, and cannot be cleared merely by retaining directories. No test assertion or production publication guard was weakened.

- The later permission update expanded filesystem write scope to the root. A fresh read-only image inspection still returned permission denied at the same Docker socket. The retained Release-suite golden case again stopped at `release_compilation.py:313`, before functional assertions, when `.release-render-*` was atomically published to `_release_materialized/<digest>`. The exact retained fixture is `/var/folders/56/ylp5765x6hnc8chzplc_rjqh0000gn/T/tmp04cv0vum`. Broad filesystem write configuration therefore did not clear either observed execution restriction; the precise enforcement cause remains unconfirmed.

## Blast radius

P1600–P1604, P1528, current host Release regression acceptance and whole-image closure remain unfinished. Dependency provisioning is cleared; the latest current-session socket retry is denied. Earlier successful Docker inventory remains historical evidence, not present access. Passing host transport and fixture checks are not relabelled immutable-image, queue or all-Workflow proof. Existing containers and protected source carriers were not changed by this retry.

## Disposition

Use .caprmedio_runtime/host-tests/bin/python for the declared host driver. Bind a new source-current immutable acceptance image and update only the stale explicit test image bindings, preserving strict assertions. Leave fixture directories as the Operator requested; use the explicit test-only retention runner where needed. Continue independent source/code work while atomic directory publication remains denied; do not replace publication with an unsafe partial write or bypass the permission boundary. Preserve earlier cache/network/socket and cleanup evidence as historical. Do not weaken tests, fabricate Run receipts or treat host checks or an image build as functional completion.
