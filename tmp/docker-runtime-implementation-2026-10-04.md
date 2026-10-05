# Docker runtime implementation

Status: mount-layout and MCP namespace defects fixed; mocked container recovery tests passed; the live one-Atom pilot completed through MCP.

## Authority changes

- R: CA-R-1818 and CA-R-1819.
- M: CA-M-324 and CA-M-325.
- E: CA-E-537 and CA-E-538.
- D: CA-D-525 and CA-D-526.
- CA-M-321: Version 2 admits the isolated Docker Agent adapter alongside the native read-only adapter; Version 1 is retained in archive.
- Eleven canonical shared-Journal records were appended through the existing API. Current result hashes were verified.

## Implementation

- One pinned runtime image; separate MCP, DBOS worker, and Codex Agent services.
- Explicit build/start/stop/restart/status/logs/MCP controls. No startup hook or automatic Workflow admission.
- Docker queue/dispatch state separated from native state. Stopped Docker routing fails visibly instead of falling back to native.
- Agent receives supplied context, not Project mounts. Only the worker applies authorized proposals.
- Runtime-only credential seed and private persistent Agent cache. No credentials or Project Atoms in the build context.
- Non-root containers, read-only image, dropped capabilities, private service network, no host ports or Docker socket mounts.
- Mock Agent and opt-in real-container tests.

## Initial validation

- Orchestrator suite: 44 tests, 42 passed, 2 actual-container tests skipped because the image is unavailable.
- MCP protocol/hot-reload suite: 10 passed.
- Ruff 0.16.8 checks and formatting: new Docker adapters and tests passed.
- Git whitespace check passed.
- No paid Agent calls, real Project Atom review, Docker worker startup, native queue migration, commit, or push was performed.

## Initial blocker (resolved)

The first build failed fetching the ghcr.io uv image. The Dockerfile now installs pinned uv from PyPI. Python 3.14.7 was pulled successfully and pinned by digest, but the next build was explicitly denied access to auth.docker.io by the active network policy.

No alternate route was used to bypass the denial. That registry-authentication domain must be permitted before image building can continue; subsequent build dependencies may expose further restrictions. Container lifecycle tests and a separately authorized live Agent pilot remain unverified.

Setup: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/README.md.

## Validation after the Codex restart

- Docker access succeeded; the daemon reported version 29.7.2.
- The pinned runtime image built successfully as `caprmedio-runtime:local`, manifest digest `sha256:862f4667ec07dc0fb784dc7f1286a136502a8088bc18236a6c6f3e3d8cd5e4f6`.
- Opt-in container suite: 2 tests attempted, both errored during worker startup, before Workflow admission or Agent dispatch. These are not passing tests.
- A disposable diagnostic fixture confirmed the mock Agent becomes healthy, but the worker exits while saving `worker.json`.
- Error: `OSError: [Errno 18] Invalid cross-device link`. The temporary carrier is under `/workspace/.caprmedio_tmp/rmed-base-revise/atomic/`; its destination is `/workspace/.caprmedio_install/workflow_orchestrator/docker/worker.json`. Separate Docker bind mounts prevent atomic replacement across that boundary, despite the host directories sharing a filesystem.
- Current CA-D-321 requires atomic-write intermediates under `.caprmedio_tmp/`. No sibling-temporary fallback or non-atomic overwrite was introduced.
- All three disposable fixtures' containers, networks, and fixture authentication volumes were removed by their scoped cleanup. No real runtime containers remain.
- No credentials were seeded, no paid Agent was called, and CA-R-1815 remains unchanged (SHA-256 `1fde4fcaf6a3a1c67d5c83660902da374265bc02f53bd6c4d3e45d7252e52753`).
- The native Run `base-revise-replacements-20261004-0305` was observed queued before testing. No queue was migrated and no fresh Docker Run was admitted.
- Git whitespace check passed.

Next decision: preserve the Project Temporary State rule by using one Project filesystem mount for the worker, while retaining immutable executable code, read-only Git metadata, and an Agent with no Project mount. This broader worker mount has not been applied without Operator approval.

## Approved correction and rerun

The Operator authorized the correction. Worker/MCP now use one Project filesystem
at `/project`; Git metadata and the Engine mirror are read-only. Execution uses
immutable image code at `/workspace`. The Agent remains without Project access.
Current Project Temporary State placement is preserved; no non-atomic fallback
was introduced. Workflow fingerprints now bind the selected Project's definition
instead of assuming authority lives beside the immutable executable code.

Container tests exposed a second defect after startup was fixed: the MCP SDK's
filtered subprocess environment omitted the Docker namespace. The gateway now
explicitly forwards only `CAPRMEDIO_RUNTIME_NAMESPACE`; its regression test also
proves an unrelated test-secret environment value is not forwarded.

- CA-D-525 advanced to Version 2; Version 1 is retained in `archive/`.
- Two confirmed shared-Journal receipts: `docker-project-mount-20261004-archive`
  and `docker-project-mount-20261004-update` (partition lines 53 and 54).
- Orchestrator native/mock/configuration suite: 45 tests, 43 passed and 2 opt-in
  container tests skipped in that command.
- Separate opt-in real-container suite: 2 tests passed in 58.545 seconds.
- Gateway hot-reload suite: 9 tests passed in 32.321 seconds.
- Ruff syntax/undefined-name checks passed for the changed runtime, gateway,
  and test modules. Git whitespace checks passed.
- All test fixtures were cleaned up using their own Compose namespaces.
- Live services `caprmedio-ea535e2c0d4e-agent-1` and
  `caprmedio-ea535e2c0d4e-worker-1` reported healthy. Authentication is runtime-only
  in the Agent's private volume; no credential content was printed.
- The native MCP generation reloaded successfully with an unchanged registry.
- MCP admitted fresh Run `base-revise-docker-20261004055029`, selecting only
  CA-R-1815 and 39 current criteria, with confidence threshold 90, fixes enabled,
  and replacements enabled. The old native queue was not migrated.
- At admission, the result was `queued`; model execution and final outcome remain
  subject to the Run's saved evidence.

## Live pilot result

- Run `base-revise-docker-20261004055029` completed at
  `2026-10-04T05:54:48.449550+04:00` after real Codex Agent check and fix calls.
- The reviewer concluded all six local checks and recorded five findings.
  The fixer addressed them through one authorized replacement:
  CA-R-1815 → CA-R-1820. The predecessor is preserved in `archive/`.
- Gather, check, and fix coverage were each 100%, with no recording blockers,
  unresolved findings, or pending Operator question.
- Active successor SHA-256:
  `3bbf6c505d4d37194c2573ee08b7e48e11d5ab93de8e4030ff0aa0c77236d7b7`.
  Archived predecessor SHA-256:
  `c288ddc7f460813f420d9430f0ee504329c5e6b4f8ee8d2866485b46a04fae50`.
  Both saved files matched the shared-Journal receipts at partition lines 61–62;
  line 60 retains the original source binding. The original active path is absent.
- Terminal Atom state: `replaced_not_rechecked`. No semantic recheck was added;
  coverage and applied corrections are not a claim that the successor is clean.
- Full report: `tmp/RMED Atoms Base Revise/base-revise-docker-20261004055029.md`.
- Both live runtime services remained healthy. No native queue was migrated,
  and no commit or push was performed.
