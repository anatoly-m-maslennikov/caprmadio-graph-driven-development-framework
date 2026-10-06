---
atom_id: CA-C-449
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-06 00:05:51 +0000"
subjects:
  governs: "Host Docker MCP test environment"
  depends_on: [Implementation, Evaluation, Workflow, MCP]
relations:
  concern_about: [CA-P-1600, CA-P-1601, CA-P-1602, CA-P-1603, CA-P-1604, CA-P-1528, CA-P-1519, CA-P-1708, CA-P-1710, CA-P-1712]
---
# Summary

Restore declared host Docker MCP test environment

## Concern

The current host dependencies, Docker API and canonical methodology publication are available, but real initial-runtime acceptance has exposed package startup defects. Initial installation remains unverified until the fixed complete-package and MCP canary passes.

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

P1600–P1604, P1528 and whole-image closure remain unfinished. Dependency provisioning, current Docker access and canonical methodology publication are verified. The current first-install canary failure blocks initial runtime acceptance; source/mock gate passes are not relabelled immutable-image, queue or all-Workflow proof. Both failed build attempts retain their actual evidence without publishing a runtime or Skill.

## Disposition

Use `.caprmedio_runtime/host-tests/bin/python` for the declared host driver. Repair the installed-layout startup, bind a fresh source-current package plan and immutable image, and pass its fixed real complete-package/MCP canary before the journaled first installation. Leave fixture directories as the Operator requested. Preserve earlier cache/network/socket and cleanup evidence as historical. Keep complete Release test gates separate from the successful build or initial installation; preserve strict assertions and actual Run evidence.

## Current environment observation

After the Operator restarted Docker and disabled sandboxing, the current session successfully connected to Docker Engine 29.8.2 with exit code 0. Earlier permission-denied and daemon-unreachable observations remain historical; their exact causes are not retroactively asserted. The declared host-test interpreter remains available, and current Unit driver/phase verification passed 20/20. This clears current socket access, not all functional release proof. Actual source publication, full Docker/MCP acceptance and complete runtime installation are still being verified; keep this Concern active until those environment-sensitive gates run.

## Current first-release acceptance

- Canonical methodology Workflow `release-methodology-first-cut-20261006-01` actually completed and recorded its terminal receipts; currentness verification passed for 1,035 selected source Atoms, with no source conflicts. Commit `394c7916e` saves the verified gate integration, compiled output and actual Journal evidence.
- Bootstrap attempt `attempt-7zzecq1r` built immutable image `sha256:6adf7da271f6f7264b7a16d4a00efd8c76311b51a48df73254f3aa81dd3a54a9`, then its real canary failed when the non-root runtime could not read root-owned owner-only archived source files. Commit `6372cfa5d` preserves source modes while assigning packaged files to the runtime user; all 12 focused bootstrap tests pass.
- Attempt `attempt-cbufqc4p` built immutable image `sha256:3775500f653b2004af0e3d76538653f37827a5c3b6af7c69c43184194bd18ab8`. The real file check passed, but MCP startup failed with `ModuleNotFoundError: workflow_evidence` from the relocated RMED Base Revise Tool. Its hardcoded Engine-root resolution is being repaired; retained stdout/stderr and command receipts remain under `.caprmedio_runtime/framework/bootstrap-image-evidence`.
- Both failures occurred before installation. Neither failed image is acceptance evidence; no current selector or project Skill was published. Docker access is not the current blocker. Retain prior N-to-N+1, complete-suite and all-Workflow acceptance as separate unfinished Tasks.
