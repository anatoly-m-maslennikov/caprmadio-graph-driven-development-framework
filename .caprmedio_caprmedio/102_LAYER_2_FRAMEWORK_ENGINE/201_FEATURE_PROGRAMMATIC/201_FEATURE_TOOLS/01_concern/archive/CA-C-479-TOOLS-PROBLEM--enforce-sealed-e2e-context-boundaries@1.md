---
atom_id: CA-C-479
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 22:11:52 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Candidate E2E context"
  depends_on: [Tool, Release Version, Candidate Manifest, Docker Image, Test Suite, JUnit Report]
relations:
  concern_about: [CA-P-1751, CA-P-1745]
---
# Summary

Enforce sealed E2E context boundaries

## Concern

The real-loader golden tests reject malformed context bindings but accept a scratch root equal to the source root and arbitrary Harness admission values, contrary to D582's dedicated scratch and fixed per-Harness context.

## Evidences

The focused context suite ran 13 cases: 11 passed, while two enforcing cases failed because ReleaseE2EContextError was not raised. No loader mock or Docker was used.

## Blast radius

P1751 behavioral acceptance and the separately admitted Candidate E2E/Full Gate boundary. Real Docker and runtime installation remain separately unproved.

## Disposition

Require a strict executor-owned scratch descendant and the exact fixed opt-in keys/values for each of the three Harnesses, including the sealed immutable candidate image. Preserve the enforcing tests and independently review the code.
