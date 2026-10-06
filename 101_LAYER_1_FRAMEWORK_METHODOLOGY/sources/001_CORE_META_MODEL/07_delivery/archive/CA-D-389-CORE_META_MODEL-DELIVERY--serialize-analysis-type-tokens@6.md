---
subjects:
  governs: "Atom/Content Role: Analysis/Type"
  depends_on:
    - "Carrier"
version: 6
updated_at: "2026-09-17 14:04:43 +0000"
relations: {}
---
# Serialize Analysis Type Tokens

an Analysis Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Rationale: `RATIONALE`.
- External Analysis Report: `EXTERNAL_ANALYSIS_REPORT`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
