---
atom_id: CA-D-579
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 7
updated_at: "2026-10-06 23:22:17 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite driver carrier"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, JUnit Report, Runtime, MCP, Workflow, Source Carrier, Compiled Candidate]
relations:
  delivery_for: [CA-R-1886, CA-R-1887, CA-M-343, CA-M-344]
---
# Summary

Deliver the Release suite driver and JUnit report boundary

## Scope

The carrier and sealed-environment boundary for the closed RELEASE_VERSION Unit driver.

## Claim

The Release Unit driver **must** remain the fixed sealed driver at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_suite.py`, with source-bound JUnit evidence, exactly two 2GiB disposable tmpfs mounts, and a host-independent captured-deadline guard that admits no caller control.

## Details

```toml
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_suite.py"
command = ["python", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_suite.py"]
working_directory = "."
report = "CAPRMEDIO_RELEASE_SUITE_REPORT"
source_bindings = "CAPRMEDIO_RELEASE_SOURCE_BINDINGS"
source_bindings_sha256 = "CAPRMEDIO_RELEASE_SOURCE_BINDINGS_SHA256"

[execution]
temporary_mount_options = "rw,nosuid,nodev,exec,size=2g,mode=1777"
temporary_mounts = ["/tmp", "/workspace/.caprmedio_tmp"]
workspace = "read-only"
network = "none"
docker_socket = "forbidden"
output = "/output"

[unit_deadline]
authority = "captured effective_unit_timeout_seconds"
maximum_seconds = 7200
enforcement = "installed-N Python PID 1; reserve=min(1.0, deadline/2); TERM at deadline-reserve; KILL at hard deadline; reap; timeout exit 124"
```

The Suite Owner preflights the inspected/admitted installed-N Python `-c` capability before launch; unsupported invocation is non-passing before launch. After exact sealed-command equality and existing selected-N image/PATH inspection, it constructs exactly `--entrypoint <inspected/admitted-installed-N-python> IMAGE -c CONSTANT_GUARD <canonical-decimal-captured-seconds> -- <exact-sealed-child-argv>`. The constant executor-owned guard validates the finite bounded internal duration, uses `Popen(argv, start_new_session=True)`, and never calls a shell, string evaluator, host interpreter, candidate image, caller command, caller environment, caller timeout, new setting, or new public field. It reserves `min(1.0, deadline / 2)` seconds before hard expiry; it sends TERM at `start + deadline - reserve`, KILL at `start + deadline` if needed, and reaps its own child. Initiating TERM latches timeout and returns `124` after reaping regardless of child status; only a child exit observed before TERM forwards its normal status. Reap/wait failure is non-passing; PID 1 exit terminates remaining container processes. No termination phase extends the configured/effective deadline. The existing host CLI timeout and labelled CID cleanup are observers/best-effort containment only.

The sealed source workspace, source-binding schema-2 envelope, package/reference rows, fixed driver command, phase rules, output-only JUnit path, private deadline snapshot, source probes, revalidation, and refusal behavior remain unchanged. `--rm` is not a receipt. Only normal terminal receipt plus complete source-bound JUnit evidence and currentness revalidation can pass; every timeout, host loss, guard failure, missing receipt, incomplete report, or changed context is non-passing and retains N. This delivery creates no new route, Workflow, gate, manifest/member, CLI, environment variable, setting, or caller field.
