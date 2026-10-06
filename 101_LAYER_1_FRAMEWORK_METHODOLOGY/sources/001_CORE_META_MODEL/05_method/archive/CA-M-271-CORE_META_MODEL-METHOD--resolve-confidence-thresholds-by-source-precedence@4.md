---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Confidence Threshold/resolution"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Confidence Threshold"
    - "Operator"
    - "Hub Atom"
    - "Framework Instance Settings"
    - "Property"
    - "AI Agent"
version: 4
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - "CA-R-1428"
---
# Resolve confidence thresholds by source precedence

**to** resolve an effective Confidence Threshold, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current decision context.
2. an explicit value on the current Plan.
3. the nearest Hub with an explicit value, walking `IS_DECOMPOSITION_OF` from nearest **to** farthest; read its own current Plan File Carrier under CA-D-472, **not** a separate Objective targeting a folder.
4. the Framework Instance Settings default.

## resolution constraints

- a missing file **or** requested field preserves inheritance; another explicit field does **not** stop lookup for the omitted field.
- use current Plan Revisions, **not** historical Carrier copies **or** unrelated nearby files; a Label is **not** an override source.
- **if** a reached source is invalid **or** ambiguous, **or** no source supplies a value, request Operator disposition **before** the affected autonomous action; do **not** invent a value **or** silently fall through past invalid authority.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values into Plan overrides. preserve an explicit selection even **when** it **=** the inherited value; a later upstream change **must not** overwrite it.
- this resolution **must not** create another Atom, settings file, **or** execution permission.
