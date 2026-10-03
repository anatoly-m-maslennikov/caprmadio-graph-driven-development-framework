---
atom_id: CA-M-105
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - Entity/canonical definition
  depends_on:
    continuant:
      - Entity
      - Property
      - Project
      - Operator
version: 4
updated_at: 2026-09-05 00:35:16 +0400
relations:
  child_of:
    - CA-M-002
    - CA-M-006
---
# One concept, one definition

**to** represent a kind of information **in** the Project, use **`=1`** canonical Entity, including a Property, for that kind **in** the same context:

1. reuse its existing canonical definition instead of introducing another Entity **or** Property for the same information.
2. treat mappings, explanations, **and** realizations as representations of that definition rather than additional canonical definitions.
3. **if** choosing between competing canonical definitions requires an unresolved decision, **then** stop the affected mapping **or** adaptation **and** return the alternatives **and** their evidence to the Operator.
