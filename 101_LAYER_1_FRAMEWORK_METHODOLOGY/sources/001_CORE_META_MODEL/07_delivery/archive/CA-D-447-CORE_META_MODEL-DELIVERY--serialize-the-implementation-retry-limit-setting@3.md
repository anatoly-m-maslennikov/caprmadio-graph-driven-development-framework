---
version: 3
updated_at: "2026-09-16 14:01:24 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-D-361
    - CA-R-1488
    - CA-R-1489
    - CA-D-408
    - CA-R-1365
    - CA-R-1367
    - CA-D-351
subjects:
  governs: "Implementation Retry Limit/Carrier"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Implementation Retry Limit"
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom/Content Role: Plan/Type: Objective"
    - "Atom Collection/Type: Epic"
    - "Carrier"
cce_version: cce_1
cce_form: serialization
---
# Serialize the implementation retry-limit setting

an explicitly selected Implementation Retry Limit **must** use the integer field assigned **to** its source Carrier:

- Framework Instance Settings TOML: `implementation.retry_limit`.
- Default Settings TOML: the same field under CA-D-408.
- Task Atom frontmatter: `implementation_retry_limit`.
- frontmatter of the active Objective Atom targeting an Epic: `epic_overrides.implementation_retry_limit`.

## inheritance and ownership

- allowed values follow CA-R-1488; the default value is owned **only** by the Default Settings Carrier.
- an omitted instance value resolves through CA-M-279. omitted Task **or** Epic fields preserve CA-M-295 inheritance **without** copied values.
- the Objective field belongs **to** its target Epic, **not** **to** the Objective's current Scope Unit **or** containing folder. the Objective remains outside its target Epic under CA-D-351.
- an Epic **without** an active Objective has no stored Epic override. do **not** create an Objective **or** another settings file **to** represent inherited values.
- omit `epic_overrides` **when** it has no explicit fields. preserve an explicit **`=0`** limit.
