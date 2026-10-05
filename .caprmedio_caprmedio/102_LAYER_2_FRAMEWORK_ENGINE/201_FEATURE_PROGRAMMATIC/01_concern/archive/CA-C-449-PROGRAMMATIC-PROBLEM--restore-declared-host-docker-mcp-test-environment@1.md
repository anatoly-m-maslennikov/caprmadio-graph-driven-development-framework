---
atom_id: CA-C-449
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:32:33 +0000"
subjects:
  governs: "Host Docker MCP test environment"
  depends_on: [Implementation, Evaluation, Workflow, MCP]
relations:
  concern_about: [CA-P-1600, CA-P-1601, CA-P-1602, CA-P-1603, CA-P-1604, CA-P-1528, CA-P-1519]
---
# Summary

Restore declared host Docker MCP test environment

## Concern

A usable host test environment for the declared workflow-orchestrator and rmed-workflow-mcp dependency groups is unavailable. Actual immutable-image MCP and queue tests remain unexecuted.

## Evidences

- The repository .venv/bin is empty; uv reports no Python executable and cannot acquire the project environment lock.
- A fresh environment at /private/tmp/caprmedio-epic-host-tests.cgHT0p/venv was created using CPython 3.14.7, but dependency sync failed while renaming a temporary distribution into /Users/am/.cache/uv/archive-v0: Operation not permitted, errno 1.
- A permitted disposable cache under the same exact temporary test directory failed on the same archive directory rename with EPERM. Provisioning stopped; no permission changes or further cache attempts followed.
- The app-bundled Python has pydantic 2.13.5 but not MCP, PyYAML, DBOS or jsonschema; it is not a substitute for the declared groups.
- The fresh image remains sha256:057792974dc2d81f84f99dee5535a44d5ee30513b03f6154381d99aa0bd558cd. Its build and source identity are verified, but no assigned actual-image case or queue Run started.

## Blast radius

P1600–P1604, P1528 and whole-image closure remain unfinished. Current development-worker native contracts for all fifteen Workflows remain independently passing; they are not relabelled image proof. Existing development workers, protected source carriers and temporary failed environment evidence were left intact.

## Disposition

The Operator must restore a usable environment containing the exact declared dependency groups, or resolve the filesystem condition. Then rerun the same strict bounded image batches. Do not retry denied carrier relocation, weaken tests, fabricate Run receipts or treat a built image as functional completion.
