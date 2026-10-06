---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Operations/Type/Filename Token"
  depends_on:
    - "Artifact/Carrier"
    - "Atom/Content Role: Operations/Type"
    - "Atom/Local Tier"
version: 1
updated_at: "2026-09-20 23:33:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-O-068"], "relates_to": ["CA-D-283", "CA-D-284", "CA-D-285", "CA-D-455"]}
---
# Serialize Foundation and Rule Atom Type tokens

an Operations Atom File Carrier **must** serialize the additional Type values admitted by CA-O-068 using this mapping **within** the existing Atom filename grammar:

- Foundation: `FOUNDATION`.
- Rule: `RULE`.

keep the Local Tier **and** Type **in** their separate registered filename positions under CA-D-283 **and** CA-D-285. Core/Foundation therefore uses `CORE-FOUNDATION`, **and** General/Rule uses `GENERAL-RULE`; these are two adjacent components, **not** compound Type values. existing Action, Workflow, **and** Actor token mappings remain **in** CA-D-455.
