---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Status: Done"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "File Carrier"
    - "Hub Atom"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1575", "CA-R-1579", "CA-R-1582", "CA-R-1539"]}
---
# Define Plan completion

Plan Status Done **means** that **all** applicable completion conditions hold:

- the Plan satisfies CA-R-1575; absence of work **and** decomposition **must not** count as completion.
- its own work, **if** present, is complete.
- **every** directly decomposed Plan is Done.
- **if** a File Carrier exists, its Definition of Done falsifying Condition Expression evaluates **to** false.

a folder-only Hub derives completion from its decomposed Plans; Canceled **or** Archived work does **not** satisfy Done.
