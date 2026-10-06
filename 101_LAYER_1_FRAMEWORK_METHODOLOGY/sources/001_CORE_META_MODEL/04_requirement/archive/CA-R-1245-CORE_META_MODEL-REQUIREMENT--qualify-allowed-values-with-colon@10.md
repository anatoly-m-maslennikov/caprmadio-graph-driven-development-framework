---
cce_version: cce_1
cce_form: requirement
subjects:
  governs: "Subject Expression"
  depends_on:
    - "IS_ALLOWED_VALUE_OF"
    - "Property"
version: 10
updated_at: "2026-09-17 17:16:39 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Qualify Allowed Values with Colon

**in** a Subject Expression, `:` **must** express **only** one IS_ALLOWED_VALUE_OF relation from the following value **to** the immediately preceding Property occurrence.
