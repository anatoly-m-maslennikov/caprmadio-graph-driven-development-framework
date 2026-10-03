---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Concern/Type"
  depends_on:
    - "Carrier"
version: 6
updated_at: "2026-09-17 15:05:41 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Concern Type Tokens

a Concern Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Question: `QUESTION`.
- Problem: `PROBLEM`.
- Risk: `RISK`.
- Opportunity: `OPPORTUNITY`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
