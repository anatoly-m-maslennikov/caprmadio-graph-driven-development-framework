---
atom_id: CA-R-1825
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Dispatch"
  depends_on: ["Atom", "Atom/Status", "Atom/Revision", "Artifact/Carrier"]
version: 3
updated_at: "2026-10-05 01:57:56 +0000"
relations:
  relates_to: [CA-O-127, CA-O-128, CA-O-129, CA-O-145, CA-O-067, CA-O-051, CA-R-866, CA-R-868, CA-R-1041]
---
# Summary

Resolve current Atom lifecycle dispatch

## Scope

The selected one-Atom lifecycle dispatcher: Create, identity-preserving Update, Replace, and Change Status (including Archive as its shortcut).

## Claim

The dispatcher is a route-specific typed `parameters` payload within CA-D-527's single `run_selected_operation(request) -> result` outer request/result. It must not introduce another outer request, result, Run, receipt, or status vocabulary. The payload admits exactly one complete target Carrier set for Create, or exactly one complete current target/predecessor Carrier set for Update, Replace, or Change Status. A Replace payload additionally names the complete accepted set of one or more distinct successor Carrier sets for that predecessor. It binds the target/predecessor identity and locator, expected current Version/digest, proposed result or status mapping, and the current qualified status model and model revision.

The Tool-side dispatcher derives the applicable status model and destination from the actual carried Content Role and optional Type, not from caller-declared whitelist values. It resolves a specific declared Role/Type model first and otherwise its declared role model, pins exact current authority source references and revisions, and derives the authoritative destination/creation/collision map before mutation. A caller-created, mismatched, stale, ambiguous, missing or unsupported model authority, or a stale destination mapping, stops unchanged before mutation. It then resolves Create only for a new Carrier, Update only when identity and Summary remain fixed, Replace when Summary changes, and Change Status for a status-only lifecycle transition; Archive is Change Status with the model-admitted archive status. A multi-target or unadmitted boundary/result stops before mutation in the shared result.

A Summary-changing Update ends this Run in a terminal non-effect `replace_handoff` with the exact predecessor and proposed complete successor inputs. It neither dispatches nor permits Replace. Replace requires a separately admitted new CA-D-527 request with fresh exact definition, input, currentness, and permission bindings; Update permission never becomes Replace permission. An authorized Archive performs the model-admitted transition even when it newly breaks Relations, reports every newly broken Relation and active referrer for separate repair, and never auto-repairs or retargets them.

## Details

This Requirement reuses the accepted native Create/Update/Archive/Replace requirements and evaluations. Its route-specific result supplies CA-R-1828 inside the CA-D-527 result; shared Run evidence, receipts, recording state, and retry are owned by `WORKFLOW_OPERATIONS/RUN_SUPPORT`.
