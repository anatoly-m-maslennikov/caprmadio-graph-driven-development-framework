---
atom_id: CA-D-536
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:17 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/REVERT_CHANGES/Carrier"
  depends_on: [Tool, Workflow, Action, Operator, Artifact, Journal]
relations:
  delivery_for: [CA-R-1833, CA-R-1834]
---
# Summary

Encode REVERT_CHANGES Tool binding

## Scope

The delivery Carrier and minimum MCP request/result contract for the REVERT_CHANGES Tool.

## Claim

The REVERT_CHANGES binding **must** expose strict request and result Carriers at one declared implementation location.

## Details

```toml
[tool_binding]
name = "REVERT_CHANGES"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/REVERT_CHANGES/revert_changes.py"
action_ids = ["CA-O-131"]
mcp_name = "revert_changes"
```

The strict request has `operation` (`admit`, `execute`, or `recover_recording`), `reversal_request` for admission, `approved_reversal_manifest` for execution, and `pending_recording_event` only for storage recovery. Unknown fields, mixed modes, missing exact bindings, or a raw inverse instruction are explicit errors. The strict result has `outcome`, `manifest_id`, `effect_account`, `evidence_refs`, and `run_receipt_refs`; an admitted result additionally carries its manifest, while blocked/error results name the exact invalid binding. The Tool exposes no generic delete/reset parameter and no auto-apply mode.
