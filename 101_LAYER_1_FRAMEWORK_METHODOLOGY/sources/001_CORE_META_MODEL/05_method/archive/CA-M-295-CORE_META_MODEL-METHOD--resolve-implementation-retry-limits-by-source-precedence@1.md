---
version: 1
updated_at: "2026-09-16 13:33:23 +0000"
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
    - "Implementation Retry Limit"
    - "Operator"
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom Collection/Type: Epic"
    - "Framework Instance Settings"
    - "Default Settings"
    - "Property"
cce_version: cce_1
cce_form: method
---
# Resolve implementation retry limits by source precedence

**to** resolve an effective Implementation Retry Limit, use the first applicable explicit value **in** this precedence:

1. direct Operator input for the current execution context.
2. the Task's explicit Implementation Retry Limit.
3. the nearest enclosing Epic with an explicit Implementation Retry Limit; inspect enclosing Epics from nearest **to** farthest.
4. Framework Instance Settings, resolving an omitted instance parameter through Default Settings under CA-M-279.

## resolution constraints

- determine whether a value is present, **not** whether it is truthy: **=0** is an explicit limit.
- **if** a higher-precedence applicable value is invalid **or** ambiguous, stop **and** ask the Operator; do **not** fall through **to** another source.
- **if** no applicable source supplies a value, report the limit as unresolved **and** stop the affected retry decision.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values into overrides. preserve an explicit override even **when** it **=** the inherited value.
- resolution selects the limit; it does **not** reset the consumed retry count governed by CA-O-024.
