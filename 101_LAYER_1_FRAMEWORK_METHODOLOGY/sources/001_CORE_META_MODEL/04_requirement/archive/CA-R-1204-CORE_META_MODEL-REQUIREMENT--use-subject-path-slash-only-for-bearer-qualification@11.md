---
cce_version: cce_1
cce_form: requirement
subjects:
  governs: "Subject Path"
  depends_on:
    - "Dependent Entity"
    - "IS_BORNE_BY"
    - "Entity"
version: 11
updated_at: "2026-09-17 17:16:41 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Use Subject Path Slash Only for Bearer Qualification

**in** a Subject Path, `/` **must** express **only** one IS_BORNE_BY edge from the following Dependent Entity occurrence **to** the immediately preceding qualified Entity occurrence.
