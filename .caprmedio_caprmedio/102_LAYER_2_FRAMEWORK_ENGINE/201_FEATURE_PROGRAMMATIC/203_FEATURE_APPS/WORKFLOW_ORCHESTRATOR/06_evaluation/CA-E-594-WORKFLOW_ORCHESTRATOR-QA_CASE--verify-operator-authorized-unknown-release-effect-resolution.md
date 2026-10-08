---
atom_id: CA-E-594
content_role: Evaluation
type: QA Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-07 04:17:42 +0400"
subjects:
  governs: "Operator-authorized unknown Release effect resolution/evaluation"
  depends_on: [Release Version, Workflow Run, Step Run, Action Run, Operator, Permission, Journal, Source, Queue, DBOS, Implementation]
relations:
  evaluation_for: [CA-R-1895, CA-M-351, CA-D-589]
  relates_to: [CA-E-583, CA-C-517]
---
# Summary

verify Operator-authorized unknown Release effect resolution

## Scope

the exact N15 unknown closed Unit effect and its one-shot resolution through the existing explicit Release recovery endpoint.

## Claim

the Evaluation **must** verify that the resolution records only one existing-kind `interrupted` terminal history with `unknown_effect` reason for the exact existing occurrence, preserves all predecessor history and never runs or reports the Unit effect.

## Details

- submit only the six-key `resolve_release_unknown_effect` request and verify the exact C517 SHA-256 `1d3d7c3c1d10827362952d684193fe844e634d18dfa5098a32f54af4863974d4`, N15 checkpoint and frozen occurrence derive the remaining pins rather than accepting caller claims.
- verify CA-D-572 admits resolver authority only through the exact ordered four-pin selection `[CA-R-1895, CA-M-351, CA-E-594, CA-D-589]` from its JSON `## Unknown-effect resolver authority` block, where each pin is exactly `atom_id`, `version`, `source_path`, `digest`; absent, duplicate, reordered, malformed or stale pins block before resolution.
- with that exact request, binding and checkpoint, verify one authorized resolution produces existing-kind Action, Step and Workflow `interrupted` facts with `unknown_effect` reason, one companion record with literal schema `release_unknown_effect_resolution_v1`, exactly four ordered authority pins and exactly three ordered `[Action, Step, Workflow]` event refs, and no effect call, Docker call, DBOS history edit, promotion or retirement.
- with the worker-ready carrier absent or stale, verify the fixed host-isolated one-shot existing recovery CLI resolves this exact control case without starting a worker, calling `DBOS.launch`, replaying/dispatching the original Workflow or running a Unit/effect.
- submit ordinary recovery with that absent or stale ready carrier and verify its existing readiness refusal remains unchanged.
- repeat the identical request and verify the original resolution reference returns with no second Journal append, start or terminal fact.
- remove or alter authorization, C517 digest, request identity, snapshot, checkpoint digest, occurrence identity, source freshness, permission or resolver authority and verify refusal precedes Journal/checkpoint mutation.
- provide an original pending event, typed Unit result, Unit terminal receipt, conflicting terminal fact or prior resolution and verify refusal preserves the existing carrier and never replaces it.
- verify `resolved` and idempotent `already_resolved` responses have exactly their declared fields and refer to the original record/events; verify `blocked` has only its declared fields. None may claim `passed`, `failed`, `completed`, promoted or a pending-recording recovery result.
- separately verify ordinary recovery still blocks an unresolved effect and exact pending-event recovery still appends only original saved event bytes.
