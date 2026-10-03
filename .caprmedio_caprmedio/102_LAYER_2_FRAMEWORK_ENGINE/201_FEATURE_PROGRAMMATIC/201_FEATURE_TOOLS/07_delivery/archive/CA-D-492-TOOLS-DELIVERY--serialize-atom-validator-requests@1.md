---
atom_id: CA-D-492
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Tool/VALIDATE_ATOMS/Request"
  depends_on:
    - "Tool/VALIDATE_ATOMS"
    - "Workflow Run"
    - "Scope Unit"
    - "Artifact/Revision"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  delivery_for:
    - CA-R-1622
    - CA-R-1623
  relates_to:
    - CA-O-081
---
# Summary

Serialize Atom validator requests

## Claim

a `VALIDATE_ATOMS` request **must** use a versioned JSON object with these interface fields:

- `schema_version`: **=1** integer, initially `1`.
- `root`: **=1** absolute requested folder path.
- `methodology`: **=1** object identifying source-authority roots **or** the selected Applicable Methodology, plus exact Workflow/Step/Action bindings **when** supplied by an executor.
- `allowed_read_roots`: **>=1** explicit absolute paths; the Tool **must not** infer permission from an Atom reference.
- optional `selection`: caller restrictions on target membership; omission selects **all** Atom candidates **in** `root`, with non-source **and** historical classification remaining explicit.
- optional `reference_roots`: additional admitted context for resolving references, **not** additional targets.
- optional `limits`: selected resource limits; optional `run_context`: executor-supplied Run identifiers.
- optional `rule_bundle`: a derived check bundle with governing identity/Revision bindings; it is **not** independent methodology authority.

an unsupported field, ambiguous context, **or** invalid shape produces an explicit request finding; omitted optional values remain distinguishable from explicit values. paths **in** this request select inputs, **not** missing Atom Properties.
