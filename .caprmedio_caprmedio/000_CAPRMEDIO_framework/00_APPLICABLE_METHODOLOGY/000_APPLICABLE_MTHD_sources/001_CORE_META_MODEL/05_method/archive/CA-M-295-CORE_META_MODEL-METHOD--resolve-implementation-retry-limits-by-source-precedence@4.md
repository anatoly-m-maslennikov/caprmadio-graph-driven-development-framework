---
version: 4
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-R-1489
  relates_to:
    - CA-M-279
subjects:
  governs: "Implementation Retry Limit/resolution"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Implementation Retry Limit"
    - "Operator"
    - "Framework Instance Settings"
    - "Default Settings"
    - "Property"
cce_version: cce_1
cce_form: method
---
# Resolve implementation retry limits by source precedence

**to** resolve an effective Implementation Retry Limit, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current execution context.
2. the current Plan's explicit Implementation Retry Limit.
3. the nearest Hub with an explicit limit, walking `IS_DECOMPOSITION_OF` from nearest **to** farthest **and** reading its own current Plan File Carrier under CA-D-447.
4. Framework Instance Settings, resolving an omitted instance parameter through Default Settings under CA-M-279.

## resolution constraints

- a missing file **or** retry field preserves inheritance; another explicit field does **not** stop this lookup.
- determine presence, **not** truthiness: **=0** is an explicit limit.
- an invalid **or** ambiguous reached source requires Operator disposition **without** silent fallback; an absent effective value stops the affected retry decision.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values **or** create separate Objective/settings files. retain explicit overrides even **when** equal **to** the inherited value.
- use the same Plan identity for a Hub's file **and** folder; ignore unrelated files **and** historical Revisions.
- resolution does **not** reset the consumed retry count governed by CA-O-024.
