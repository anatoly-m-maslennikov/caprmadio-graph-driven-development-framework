---
atom_id: CA-R-1895
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 03:38:00 +0400"
subjects:
  governs: "Operator-authorized unknown Release effect resolution"
  depends_on: [Release Version, Workflow Run, Step Run, Action Run, Operator, Permission, Journal, Source, DBOS, Implementation]
relations:
  relates_to: [CA-R-1883, CA-O-164, CA-C-517]
---
# Summary

terminalize one Operator-authorized unknown Release effect

## Scope

one existing frozen **CA-O-164** Release Workflow Run whose exact in-progress Action effect is unobserved after host loss.

## Claim

WORKFLOW_ORCHESTRATOR **must** terminalize an unknown Release effect only through the separately typed `resolve_release_unknown_effect` operation on the existing explicit Release recovery endpoint, and only as an existing `interrupted` terminal outcome with unknown-effect reason, without replaying, inferring or replacing that effect.

## Details

- the sole admitted instance is Run `release-epic-resume-20261006-N15`, frozen snapshot `3bfdd04e1b9901c97a6af49c59e01731c456ea5313816db657457e94bd35a9f7`, checkpoint digest `71d93f97c0f07b84e94d49d5bd18a4ab83d86e3e52d00e39368ce881153a4344`, and in-progress CA-O-185/CA-O-168 occurrence `release-epic-resume-20261006-N15:step:5:action:1` with parent Step `release-epic-resume-20261006-N15:step:5`.
- admission requires the exact frozen request identity, retained host binding, current resolver authority, current source and permission checks, and C517 Operator decision reference `.caprmedio_caprmedio/01_concern/CA-C-517-QUESTION--resolve-the-unknown-n15-unit-outcome.md` SHA-256 `1d3d7c3c1d10827362952d684193fe844e634d18dfa5098a32f54af4863974d4`.
- admission requires no pending original-event carrier, no Action result for the occurrence, and no competing canonical terminal receipt or earlier resolution. It authenticates original frozen facts; it does not re-authorize or execute the old effect.
- resolver authority closes only when CA-D-572's trusted JSON `## Unknown-effect resolver authority` block contains one exact ordered resolver-authority selection: CA-R-1895, CA-M-351, CA-E-594, CA-D-589. Every selected pin object has exactly `atom_id`, positive-integer `version`, safe Project-relative `source_path` and lowercase-64-hex `digest`; no self/final output hash is admitted.
- the resolution appends canonical interruption facts once for the existing Action, parent Step and Workflow while preserving every original start, completed receipt and history. Repeats return the original resolution reference and append nothing.
- the existing Journal terminal kind is `interrupted`; `unknown_effect` is its reason and resolution kind, not a new Unit/lifecycle outcome. It is neither a Unit pass nor failure and cannot justify promotion, retirement, later phase execution, Docker use or a new Release Run.
- ordinary `recover_selected_release` retains its current unresolved-effect refusal. Pending original-event append recovery remains distinct and may recover only its exact saved bytes.
