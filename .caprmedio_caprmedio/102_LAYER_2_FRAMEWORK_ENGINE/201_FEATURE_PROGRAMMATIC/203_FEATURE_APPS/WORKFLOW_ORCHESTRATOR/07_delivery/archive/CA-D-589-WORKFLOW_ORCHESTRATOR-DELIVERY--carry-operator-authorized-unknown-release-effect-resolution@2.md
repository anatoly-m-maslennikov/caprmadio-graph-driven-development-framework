---
atom_id: CA-D-589
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 03:38:00 +0400"
subjects:
  governs: "Operator-authorized unknown Release effect resolution/Carrier"
  depends_on: [Carrier, Release Version, Workflow Run, Step Run, Action Run, Operator, Permission, Journal, Queue, DBOS, Implementation]
relations:
  delivery_for: [CA-R-1895, CA-M-351]
  relates_to: [CA-D-577, CA-D-574, CA-C-517]
---
# Summary

carry Operator-authorized unknown Release effect resolution

## Scope

the typed request, response and retained resolution reference for the N15-specific unknown-effect operation on the existing explicit Release recovery endpoint.

## Claim

the existing Release recovery endpoint Carrier **must** distinguish the Operator-authorized `resolve_release_unknown_effect` operation from ordinary recovery and pending-event recording recovery while retaining only exact identity, approval and evidence bindings.

## Details

- the request's exact keys are `operation`, `run_id`, `request_identity`, `authorization_ref`, `authorization_sha256` and `expected_checkpoint_sha256`, with `operation: resolve_release_unknown_effect`; no extra key is admitted. Snapshot and exact Action/Step/Workflow pins derive from the registered N15 occurrence and frozen checkpoint, not caller claims. Ordinary `recover_selected_release` keeps its existing three-key request shape.
- response variants are closed: `resolved` and `already_resolved` carry exactly `operation`, `run_id`, `disposition`, `resolution_ref`, `event_refs` and `unknown_reason`; `blocked` carries exactly `operation`, `run_id`, `disposition` and `blocked_reason`. No response claims a Unit exit/result, pass, failure, completed Release, promotion or replacement Run.
- resolver authority is closed only by CA-D-572's trusted JSON `## Unknown-effect resolver authority` block exact ordered selection `[CA-R-1895, CA-M-351, CA-E-594, CA-D-589]`. Each selected member is the registry pin object with exactly `atom_id`, positive-integer `version`, safe Project-relative `source_path` and lowercase-64-hex `digest`; root appends the four final pins after their hashes exist, avoiding self-hash.
- the authoritative companion resolution record has literal `schema: release_unknown_effect_resolution_v1`, literal `resolution_kind: unknown_effect`, and exactly `schema`, `resolution_kind`, `run_id`, `workflow_run_id`, `step_run_id`, `action_run_id`, `old_checkpoint_sha256`, `authorization_ref`, `authorization_sha256`, `approved_authority_pins`, `event_refs` and `unknown_reason`. `approved_authority_pins` has exactly the four D572-ordered pins; `event_refs` has exactly three ordered canonical refs `[Action, Step, Workflow]`. It binds C517 and current resolver authority pins and records no duplicate Journal authority; canonical Action, Step and Workflow `interrupted` facts remain the sole historical facts.
- transport/DBOS state is observation and delivery state only. The implementation uses legitimate DBOS API calls and never direct SQLite edits of history.
- ordinary recovery request shape and its unresolved-effect guard remain unchanged. Pending append/crash recovery continues to use only original sealed event bytes, cannot select this operation implicitly and cannot alter an old checkpoint to manufacture proof.
