---
atom_id: CA-E-586
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-06 23:22:17 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite runner QA"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, Source Carrier, Compiled Candidate, JUnit Report, Writable Output]
relations:
  evaluation_for: [CA-R-1886, CA-M-343, CA-D-579]
---
# Summary

Verify complete and source-bound Release suite evidence

## Scope

The Release Version closed Unit driver, its phase-derived declared-case discovery, sealed JUnit evidence boundary, two fixed temporary mounts, and source-owned deadline containment.

## Claim

The QA case **must** prove that the Unit Gate passes only after every phase-assigned Unit test executes once with valid immutable-envelope source evidence, normal terminal receipt, JUnit evidence, and currentness revalidation; it must reject capacity, timeout, host-loss, incomplete, fabricated, or non-passing evidence.

## Details

Use isolated fixtures to prove complete exact phase assignment, fresh discovery, exact Unit-ID/JUnit-ID equality, envelope/probe integrity, source digest enforcement, compiled-candidate evidence, and refusal of omissions, duplicates, skips, errors, failures, mutable/read-only boundary violations, invalid reports, or caller selection. A passing Unit remains only an image-build prerequisite, never a Full Gate or promotion authority.

Assert the executor produces exactly the existing two disposable tmpfs mounts, `/tmp` and `/workspace/.caprmedio_tmp`, each `rw,nosuid,nodev,exec,size=2g,mode=1777`; no third mount, writable source workspace, socket, network, privilege, host path, resource increase, deadline increase, or changed output boundary is admitted. Exercise finite captured deadline validation and the private snapshot without adding any public field.

Use unit mocks to prove the exact executor argv is `--entrypoint <inspected/admitted installed-N python> IMAGE -c CONSTANT_GUARD <canonical-decimal-captured-seconds> -- <exact sealed child argv>`; preflight the image Python `-c` capability before launch; reject unsupported invocation before launch; and never admit a shell or caller field. Prove `reserve = min(1.0, deadline / 2)`, TERM at `start + deadline - reserve`, KILL at hard expiry, and reaping of the owned child. Prove a child exit observed before TERM forwards normally, but TERM latches timeout: a child that handles TERM and exits zero still yields `124` after reaping. No termination step extends the captured deadline. Assert all guard failures are non-passing. Within existing approved E2E coverage, when Docker is available, sever only the host CLI observer of an over-budget disposable container and verify the daemon container terminates by that captured deadline; capability absence is a non-passing environment blocker, not a new harness or gate. Neither `--rm`, absent container, nor missing receipt may be credited as a Unit pass.
