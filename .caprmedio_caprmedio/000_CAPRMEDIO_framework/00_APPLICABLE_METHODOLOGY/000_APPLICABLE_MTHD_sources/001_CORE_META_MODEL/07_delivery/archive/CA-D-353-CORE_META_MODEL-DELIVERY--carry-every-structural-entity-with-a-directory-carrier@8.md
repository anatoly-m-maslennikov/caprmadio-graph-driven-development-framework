---
cce_version: cce_1
cce_form: cardinality
subjects:
  governs: "Structural Entity"
  depends_on:
    - "Directory Carrier"
    - "Scope Unit"
    - "Project Structure"
    - "Atom Collection/Type: Epic"
version: 8
updated_at: "2026-09-17 12:25:49 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Carry Every Structural Entity with a Directory Carrier

**every** Structural Entity **must** be carried by **`>=1`** Directory Carrier **unless** it is a Scope Unit established by Project Structure that remains unmaterialized under CA-R-1484.

- absence of its directory does **not** remove **or** invalidate that Scope Unit declaration. materialization remains a separately evaluated condition.
- **every** Epic **must** have **`=1`** Directory Carrier; the Scope Unit declaration exception does **not** extend **to** an Epic.
