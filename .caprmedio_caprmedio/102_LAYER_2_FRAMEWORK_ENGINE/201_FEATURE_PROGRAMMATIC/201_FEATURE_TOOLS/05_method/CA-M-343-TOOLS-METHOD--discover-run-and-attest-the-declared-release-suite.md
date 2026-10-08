---
atom_id: CA-M-343
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-06 23:22:17 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite test procedure"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, Source Carrier, Compiled Candidate, JUnit Report, Writable Output]
relations:
  method_for: [CA-R-1886]
---
# Summary

Discover, run, and attest the declared Release suite

## Scope

The deterministic closed Unit Gate execution and source-attestation procedure for one sealed Release Version candidate.

## Claim

RELEASE_VERSION **must** execute every once-assigned sealed Unit test once under its immutable envelope, retain observed JUnit/source evidence, and enforce the captured effective Unit deadline inside the disposable installed-N container independently of the host Docker CLI.

## Details

Derive the complete sealed package-row test set and its one-to-one phase map; the three CA-R-1890 paths are `candidate_e2e` and every other `102_FRAMEWORK_ENGINE/**/test_*.py` row is `unit`. Discover each Unit module in a fresh standard-library `unittest` child process, reject an empty, duplicate, unknown, altered, skipped, failed, errored, timed-out, or incomplete case set, and require exactly one JUnit row and one derived source-binding record with at least one sealed source reference per executed Unit ID. Validate the immutable envelope, its candidate/package rows, maintained module rules, source probes, and compiled-candidate probe exactly as delivered by CA-D-579; no focused subset, caller selector, source mutation, or fabricated report passes.

Before execution, resolve `[release_suite].unit_timeout_seconds` only from captured CA-D-580 settings bytes, write and later verify the private CA-D-579 deadline snapshot, and permit a fixture value only to shorten it. The Suite Owner shall preflight the inspected/admitted installed-N Python `-c` capability, then pass the captured effective deadline to a fixed executor-owned watchdog as the sole deadline authority. The watchdog is container PID 1 and starts only the already equality-checked sealed Unit argv with `Popen(argv, start_new_session=True)`, never a shell or command string. Let `reserve = min(1.0, deadline / 2)`: by a monotonic clock it sends TERM to the child process group at `start + deadline - reserve`, sends KILL at hard expiry `start + deadline` if needed, and reaps its own child. Initiating that TERM latches the outcome as timed out, so the guard exits `124` after reaping regardless of the child status; only a child exit observed before that TERM is forwarded unchanged. Setup, preflight, launch, signalling, wait, or reap failure is non-passing. It receives no caller command, timeout, setting, environment field, or public contract.

The host Docker CLI may observe and best-effort contain a labelled container but is not deadline authority. Host loss, CLI timeout, missing CID, `--rm`, or a later missing container never proves a terminal outcome or a pass. A Unit passes only after its normal terminal receipt, complete JUnit/source evidence, and post-run source/currentness revalidation; otherwise it retains N and authorizes no later release effect. This Method creates neither a selected Workflow nor an MCP route.
