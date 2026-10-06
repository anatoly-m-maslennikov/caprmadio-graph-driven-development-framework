---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    - "Subject"
    - "Atom/Subjects"
    - "Entity"
    - "Action"
    - "Process"
    - "Atom/Claim"
version: 8
updated_at: "2026-09-17 17:16:37 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reference Every Prerequisite Subject through DEPENDS_ON

**every** canonical Entity, Action, **or** Process required by an Atom's Claim **without** governing that target **must** be referenced directly through DEPENDS_ON **in** the Atom's Subjects Property.
