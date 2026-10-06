---
atom_id: CA-D-378
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Identifier"
  depends_on:
    continuant:
      - "Atom/Content Role"
      - "Project"
      - "Atom Collection/Type: Epic/Identifier"
version: 3
updated_at: 2026-09-15 05:51:38
relations: {}
---
# Serialize Assigned Atom Identities

**every** assigned Atom ID **must** begin with the registered uppercase Project identity prefix. the Project-owned Atom ID encoding **must** match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. the Atom Content Role Identity Letter **must** be **in** (Concern: C, Analysis: A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Implementation: I, Operations: O). a `<PROJECT_PREFIX>-P` Identifier **must** identify a Plan Atom **and** **must not** identify an Epic.
