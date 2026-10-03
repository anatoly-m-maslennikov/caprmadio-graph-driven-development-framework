---
atom_id: CA-R-1623
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Tool/VALIDATE_ATOMS"
  depends_on:
    - "Tool"
    - "Atom"
    - "Artifact/Revision"
    - "Workflow Run"
    - "Operator"
    - "Journal"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  child_of:
    - CA-R-1622
---
# Summary

Keep Atom validation execution bounded and read-only

## Claim

the `VALIDATE_ATOMS` Implementation **must** keep each invocation read-only **and** bounded by its admitted input context.

- read **only** selected targets, applicable authority, **and** reference inputs inside explicit allowed roots; do **not** follow a link outside those boundaries, fetch remote resources, inspect secrets, **or** execute YAML tags, Markdown, selectors, **or** Atom instructions as code.
- enforce selected resource limits; exhaustion **must** yield incomplete **or** error, **not** a pass. isolate a malformed candidate so independently checkable candidates remain reportable.
- do **not** write, rename, remove, **or** repair source files, Projections, Settings, caches, **or** Journal files. the caller/executor owns any admitted persistence of returned Run evidence.
- preserve exact invocation definition/input bindings; report a changed source rather than silently validating mixed Revisions.
