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
version: 2
updated_at: "2026-09-22 23:02:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1575", "CA-R-1579", "CA-R-1599", "CA-R-1539"]}
---
# Summary

Define Plan completion

## Claim

Plan Status Done **means** that **all** applicable completion conditions hold:

- the Plan satisfies CA-R-1575; absence of work **and** decomposition **must not** count as completion.
- its own work, **if** present, is complete.
- **every** directly decomposed Plan is Done.
- its Definition of Done falsifying Condition Expression evaluates **to** false.

a Hub requires its own Definition of Done **and** completion of its decomposed Plans; Canceled **or** Archived work does **not** satisfy Done.
