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
version: 2
updated_at: "2026-09-24 13:59:55 +0000"
relations:
  child_of:
    - CA-R-1622
---
# Summary

Keep Atom validation execution bounded and read-only

## Claim

the `VALIDATE_ATOMS` Implementation **must** keep each invocation read-only **and** bounded by its admitted input context.

- admit bounded inventory enumeration **and** the minimum candidate content needed **to** determine selection inside declared source roots **and** allowed read roots. inspect an excluded candidate **only** for selection; exclusion does **not** admit its full validation **or** add it **to** target coverage.
- read selected targets, applicable authority, **and** necessary reference inputs **only** inside admitted read boundaries. reference resolution does **not** expand the target set.
- enforce actual read permissions **and** protected-file exclusions **before** reading content. caller-supplied roots grant no permission; do **not** follow a link outside admitted boundaries, fetch remote resources, inspect secrets, **or** execute YAML tags, Markdown, selectors, rule bundles, **or** Atom instructions as code.
- enforce selected resource limits; exhaustion **must** yield incomplete **or** error, **not** a pass. isolate a malformed candidate so independently checkable candidates remain reportable.
- do **not** write, rename, remove, **or** repair source files, Projections, Settings, caches, **or** Journal files. the caller/executor owns any admitted persistence of returned Run evidence.
- preserve exact invocation definition/input bindings; report a changed source rather than silently validating mixed Revisions.
