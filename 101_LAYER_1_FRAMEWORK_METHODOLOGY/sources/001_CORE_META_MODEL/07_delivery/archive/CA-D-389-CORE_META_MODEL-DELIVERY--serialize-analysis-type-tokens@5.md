---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Analysis/Type"
  depends_on:
    - "Carrier"
version: 5
updated_at: "2026-09-17 14:04:43 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Analysis Type Tokens

an Analysis Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Rationale: `RATIONALE`.
- External Analysis Report: `EXTERNAL_ANALYSIS_REPORT`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
