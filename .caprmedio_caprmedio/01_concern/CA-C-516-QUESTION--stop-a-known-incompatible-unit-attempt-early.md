---
atom_id: CA-C-516
content_role: Concern
type: Question
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 20:51:00 +0000"
subjects:
  governs: "Early interruption of a known-incompatible Unit attempt"
  depends_on: [Operator, Workflow, Action, Evaluation, Journal, Docker Image]
relations:
  concern_about: [CA-P-1117, CA-P-1809, CA-P-1815]
---
# Summary

Stop a known-incompatible Unit attempt early

## Concern

Under the Epic's autonomous best-option envelope, stop an exact disposable Unit container when independent verification has already found a deterministic fixture setup failure, rather than spending the full test budget on that known-invalid candidate. Retain the actual interruption and use a fresh candidate after repairs; never label the interrupted attempt a pass.

## Evidences

- N14 snapshot: `395e762201a7a8f8d6645009cb139f4788458b80c0bca620b56224771046a720`.
- Independent retained-E2E fixture setup failed because full_suite_golden/control_fixture.py omits the five declared D580 v7 selected-refresh leaves.
- Before stop, Docker inspect bound container `5056054d79a1` to exactly the N14 read-only workspace/output mounts and immutable N image `sha256:79899cfe59fb36c8da5ce1c12ea52c529a61738e51100b3d3e8488c52496d54e`; no other container was targeted.
- Its Unit receipt records exit 137 after 104.1833622080012 seconds, zero validated-report tests, empty coverage and no JUnit report. That is incomplete coverage, not evidence that no tests ran.
- N14 records 22 actual Events: 11 starts, 8 completions and 3 interruptions, with no pending recording. No package, image, E2E, promotion or retirement followed.

## Blast radius

Only the identified N14 disposable Unit container and its recorded incomplete attempt. Installed N, candidate/history bytes, other containers and permissions remain unchanged.

## Decision

This bounded choice was used once under CA-P-1117 autonomy. Repair the shared fixture, independently verify its exact closure and dependent setups, then admit a fresh N15. Do not replay N14, weaken the Unit gate, introduce an automatic stop policy, or infer release completion from scheduler success. Keep this Question for Operator review of the choice.
