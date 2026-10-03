---
atom_id: CA-D-493
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
  governs: "Tool/VALIDATE_ATOMS/Result"
  depends_on:
    - "Tool/VALIDATE_ATOMS"
    - "Workflow Run"
    - "Step Run"
    - "Atom/Revision"
    - "Evaluation"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  delivery_for:
    - CA-R-1622
    - CA-R-1623
  relates_to:
    - CA-O-083
---
# Summary

Serialize Atom validator results

## Claim

a `VALIDATE_ATOMS` result **must** use a versioned JSON object carrying the Workflow outcome **and** its assessment evidence.

- `schema_version`: initially `1`; `result`: **=1** value **in** (`valid`, `invalid`, `incomplete`, `error`).
- `bindings`: exact methodology, Workflow, Step, Action, **and** checked rule identity/Revision bindings.
- `selection`: requested boundary, selected candidates, exclusions with reasons, **and** unresolved candidates.
- `coverage`: target **and** rule totals with passed, failed, not-applicable, **and** not-checked counts.
- `carriers`: per-target locator, internally declared identity/Revision **when** available, observed content fingerprint, **and** check outcomes. missing identity stays null, **not** a filename-derived value.
- `findings`: stable check code, severity, source locator/span, Property **or** section, governing rule identity/Revision **when** resolvable, reason, **and** supporting bounded evidence. do **not** copy secrets **or** whole unrelated Carriers.
- `currentness`: unchanged, changed, **or** unverified, with affected input references; `execution`: available Run/Step results **and** execution diagnostics.

map terminal results **to** exit codes: `valid = 0`, `invalid = 1`, `incomplete = 2`, `error = 3`. malformed requests return an error envelope with available evidence **and** explicitly empty unexecuted portions, **not** fabricated bindings.
