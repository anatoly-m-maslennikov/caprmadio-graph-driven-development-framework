---
atom_id: CA-P-1484
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Shared selected Run support"
  depends_on: [Implementation, Workflow, Action]
version: 1
updated_at: "2026-10-04 22:39:38 +0400"
relations:
  is_decomposition_of: [CA-P-1133]
  blocks: [CA-P-1122, CA-P-1162, CA-P-1163]
---
# Summary

Specify shared selected run support

## Objective

Author one bounded reviewed-implementation specification packet after source-stage acceptance. Inherit P1117's 90% confidence threshold and current Operator-selected thirteen-request scope. Estimate <=15 minutes. No harvesting or FPF.

### Inputs

Current accepted A1142 source registry and root source-stage acceptance P1119/P1132; Operator Goal and relevant active Project Principles. J01–J08 from Done P1443/P1451; R1720v17/R1525v6/R1728v16; current work_journal.py storage API.

### Ownership and output

WORKFLOW_OPERATIONS/RUN_SUPPORT authority carriers; reserve R1821–1824, E541–544, D527–529; no code. You are not alone; preserve others' edits. Use apply_patch. Exact Workflow/Step/Action Run identities/definition revisions, standalone/nested lineage, start/terminal/no-op/failure/cancel/partial outcomes, durable same-event retry without Action replay, currentness and source selection; one canonical Events Journal. Define a small shared interface for callers, not a new Workflow. Return proposed interface immediately to root.

RMED must be sufficient for the intended implementation, correctly split by meaning/carrier/construction/assurance and avoid duplicating existing admitted authority. Keep complete Atom properties, Summary/Scope/Claim/Details and truthful exact source references. Save only this packet's output/result. Code implementation waits for independent RMED review. Record gaps/uncertainty to root; do not expand into another source campaign.

### Verification

Reopen owned saved carriers; check their properties, one coherent claim/scope, source-driven functional cases and exact input/output contract. Report actual paths/IDs/versions and remaining issues. Static authoring is not a runtime pass.

## Details

### Saved output

P1484 authored the following eleven TOOLS-root carriers. `WORKFLOW_OPERATIONS`
and `RUN_SUPPORT` are not declared Scope Units in the live Project Structure;
to avoid silently inventing one, their governing subject is carried in the
existing declared `TOOLS` authority path. A separately authorized structural
change may later relocate these carriers.

- [CA-R-1821](../../../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1821-TOOLS-REQUIREMENT--admit-only-current-authorized-selected-operation-runs.md)
  through [CA-R-1824](../../../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1824-TOOLS-REQUIREMENT--recover-selected-run-journal-evidence-without-replaying-effects.md):
  current Operator/source admission; exact Run identity, definition/revision
  and lineage; truthful outcome mapping; and canonical Journal recovery
  without effect replay.
- CA-E-541 through CA-E-544 in
  `201_FEATURE_TOOLS/06_evaluation/`: source/currentness, identity/lineage,
  outcome truth, and failed append identical/conflicting retry functional
  cases.
- CA-D-527 through CA-D-529 in `201_FEATURE_TOOLS/07_delivery/`: one
  `run_selected_operation(request) -> result` interface, schema-v5 selected-Run
  extension of the existing `work_journal` append API, and a shared
  non-executable TOOLS-library location.

The chosen service is deliberately small: a request supplies an operation route
and typed parameters, optional exact expected definition revisions, sealed
Initiative, explicit sealed current Operator authorization, optional real
lineage, and a stable idempotency key; preview is the default and only explicit
`execute` starts a Run. The result returns an honest disposition, actual
identities/bindings only if started, outcome/effect/report references, Journal
receipt or recording blocker, and retry disposition. Retry preserves the same
original Event payload/identity; a separate recovered fact cannot mutate it.
The schema-v5 event remains immutable: durability/receipt state is derived only
from the actual append receipt or pending runtime evidence, not serialized into
or mutated on the original event. It retains existing sealed append/receipt
durability and schema-v4 read support. This is not code or a runtime pass.

### Static verification

At 2026-10-04 22:39:38 +0400, root's bounded independent review correction and
the Docker Python static verifier reopened all eleven owned carriers and passed
their front matter IDs/roles/scopes, exact Claim/Scope/Details sections, EOF
newlines, and P1484 saved-output evidence.
The source-driven cross-link check confirmed R/E/D IDs and the exact
R1720v17/R1525v6/R1728v16/R1643v22/R1644v17/R1094v10 source references. The
current `work_journal.py` API supplies sealed append, fsync, receipt and
same-event collision behavior but schema-v4 requires `workflow_run_id` for
every event; D528 records the bounded schema-v5 extension needed for
standalone Action Runs. Receipt state is derived after append rather than put
in the sealed event. This static check is not implementation, append, or
runtime evidence.

### Downstream frontier

Independent RMED review remains required before any implementation. The main
implementation gap is the specified schema-v5 selected-Run event support and
shared library; no code was changed by this task. P1491 must consume D527,
not duplicate execution behavior in MCP. Root retains aggregate acceptance,
dependent binding, and any Scope Unit declaration decision.

### Definition of Done

The bounded specification or acceptance packet is saved with exact owned outputs and one proportionate check, ready for independent review. Implementation remains gated; root owns aggregate acceptance.
