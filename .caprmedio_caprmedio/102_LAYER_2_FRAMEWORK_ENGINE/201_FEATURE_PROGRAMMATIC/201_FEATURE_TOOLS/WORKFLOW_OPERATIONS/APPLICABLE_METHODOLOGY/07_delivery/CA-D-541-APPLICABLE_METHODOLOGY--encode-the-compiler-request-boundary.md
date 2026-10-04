---
atom_id: CA-D-541
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:37:19 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY/Carrier"
  depends_on: [Tool, Workflow, Action, Methodology Source, Extension, Project Configuration, Operator, Journal]
relations:
  delivery_for: [CA-R-1839, CA-R-1840, CA-R-1841]
---
# Summary

Encode the strict governed request boundary for the Applicable Methodology compiler.

## Scope

The strict native request boundary for the Applicable Methodology compiler; it does not define a second Workflow or Journal interface.

## Claim

The delivered compiler **must** accept an explicit mode and exact governed bindings, and **must not** accept caller-supplied source edits, arbitrary conflict winners, or unbound approval text.

## Details

```toml
[tool_binding]
name = "COMPILE_APPLICABLE_METHODOLOGY"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"
workflow_id = "CA-O-011"
action_ids = ["CA-O-004", "CA-O-005", "CA-O-006", "CA-O-007", "CA-O-008", "CA-O-009"]
operations = ["dry_run", "apply", "recover_publication"]
```

The strict request contains `operation`; `project_root`; expected Project Structure, Framework Settings, and Project Configuration revision/digest bindings; `projection_target`; and, for `apply` or `recover_publication`, the expected assessed frontier digest plus exact decision and prior-publication evidence references. The Tool resolves all source locations from governed Project Structure/Settings. `apply` refuses a request without a fresh publishable assessment; `recover_publication` accepts only a failed-publication receipt and never a source-change instruction.

Unknown fields, mixed operations, mutable source/output paths outside governed declarations, `edit_source`, raw source patch, arbitrary selected candidate, raw approval text, or a TOML-only approval are explicit errors. Canonical shared Run/Journal handles are references, not caller-authored event payloads.

### Sources

- CA-R-1839 through CA-R-1841; CA-O-011 v12; CA-P-1442 v1.
