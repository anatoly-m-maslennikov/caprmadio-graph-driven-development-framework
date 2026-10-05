---
atom_id: CA-C-449
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 09:12:57 +0000"
subjects:
  governs: "Host Docker MCP test environment"
  depends_on: [Implementation, Evaluation, Workflow, MCP]
relations:
  concern_about: [CA-P-1600, CA-P-1601, CA-P-1602, CA-P-1603, CA-P-1604, CA-P-1528, CA-P-1519]
---
# Summary

Restore declared host Docker MCP test environment

## Concern

The declared host test dependencies are now available, but this session cannot connect to the Docker API socket. Actual immutable-image MCP and queue tests remain unexecuted.

## Evidences

- Revision 1 preserves the original empty repository environment and distribution-cache rename failures. The Operator then widened the access profile and requested another attempt.
- That attempt encountered a network allowlist denial for files.pythonhosted.org. Offline provisioning lacked the exact MCP wheel and the psycopg-binary wheel required by DBOS. A newly created empty directory inside the original UV cache still failed to rename with EPERM; cleanup of that empty probe was also denied. No alternate endpoint, permission modification or denial bypass followed.
- The Operator installed the declared groups in .caprmedio_runtime/host-tests from macOS Terminal. Import verification now succeeds for MCP 2.3.0, DBOS 2.31.1, PyYAML 6.0.3, jsonschema 4.26.0 and pydantic 2.13.5. The broken repository .venv was preserved.
- SelectedDockerHarnessTransportTests passed 3/3 in 2.475 seconds: actual MCP stdio reconnection and structured results, refusal of error/text-only pseudo-results, and container-visible fixture input roots.
- The W01-W15/J01-J08 golden-corpus check passed 1/1 in 1.731 seconds. It verifies the bound fixture corpus, not Workflow execution or Docker behavior.
- The fresh Docker image inventory attempt failed with permission denied while trying to connect to unix:///Users/am/.docker/run/docker.sock. Read-only inspection shows the socket belongs to am with mode srwxr-xr-x; no file mode or Docker endpoint was changed. This evidence does not establish the origin of the connection denial.
- The Operator-directed cleanup removed unused image sha256:057792974dc2d81f84f99dee5535a44d5ee30513b03f6154381d99aa0bd558cd. It is no longer a usable acceptance image. A newly built source-bound image will be required before the image batches can be accepted.

## Blast radius

P1600–P1604, P1528 and whole-image closure remain unfinished. The host dependency blocker is cleared for the new environment. Passing host transport and fixture checks are not relabelled immutable-image, queue or all-Workflow proof. Existing containers and protected source carriers were not changed by this retry.

## Disposition

Use .caprmedio_runtime/host-tests/bin/python for the declared host driver. Resume the same strict bounded image batches when Docker API access is restored, after binding a new source-current image rather than the removed image. The cache/network restrictions no longer prevent use of the Operator-installed dependencies, but their diagnostic evidence remains preserved. Do not retry denied carrier relocation, weaken tests, fabricate Run receipts or treat host checks or an image build as functional completion.
