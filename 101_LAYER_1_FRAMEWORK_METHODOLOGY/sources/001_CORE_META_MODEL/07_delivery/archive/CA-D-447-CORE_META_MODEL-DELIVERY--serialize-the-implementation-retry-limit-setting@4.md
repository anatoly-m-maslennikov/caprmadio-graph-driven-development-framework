---
version: 4
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-361", "CA-R-1488", "CA-R-1489", "CA-D-408", "CA-D-460", "CA-D-470", "CA-M-295"]}
subjects:
  governs: "Implementation Retry Limit/Carrier"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Implementation Retry Limit"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Carrier"
cce_version: cce_1
cce_form: serialization
---
# Serialize the implementation retry-limit setting

an explicitly selected Implementation Retry Limit **must** use the integer field assigned **to** its owning source Carrier:

- Framework Instance Settings TOML: `implementation.retry_limit`.
- Default Settings TOML: the same field under CA-D-408.
- a Plan Atom's own File Carrier frontmatter: `implementation_retry_limit`, including a Hub's optional matching File Carrier.

## inheritance and ownership

- allowed values follow CA-R-1488; the default value is owned **only** by Default Settings.
- omitted instance values resolve under CA-M-279; omitted Plan fields inherit under CA-M-295 **without** copied values. preserve explicit **=0**.
- a Hub override belongs **to** that same Plan identity, **not** a separate Objective **or** settings file; do **not** use `epic_overrides`.
- a folder-only Hub has no file-based override. do **not** create a file merely **to** materialize inheritance; a supplied Plan File Carrier requires DoD under CA-D-470.
