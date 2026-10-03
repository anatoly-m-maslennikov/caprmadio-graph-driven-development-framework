---
cce_version: cce_1
cce_form: method
version: 8
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - CA-M-002
    - CA-M-006
subjects:
  governs: "Entity/canonical definition"
  depends_on:
    - "Entity"
    - "Property"
    - "Project"
    - "Operator"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# One concept, one definition

**to** represent a kind of information **in** the Project, use **`=1`** canonical Entity, including a Property, for that kind **in** the same context:

1. reuse its existing canonical definition instead of introducing another Entity **or** Property for the same information.
2. treat mappings, explanations, **and** realizations as representations of that definition rather than additional canonical definitions.
3. **if** choosing between competing canonical definitions requires an unresolved decision, **then** stop the affected mapping **or** adaptation **and** return the alternatives **and** their evidence **to** the Operator.
