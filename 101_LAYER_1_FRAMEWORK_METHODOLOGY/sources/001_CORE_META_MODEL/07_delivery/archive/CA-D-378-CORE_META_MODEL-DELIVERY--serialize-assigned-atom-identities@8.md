---
subjects:
  governs: "Atom/Identifier"
  depends_on:
    - "Atom/Content Role"
    - "Project"
    - "Atom/Content Role: Plan/Type: Plan/Identifier"
version: 8
updated_at: "2026-09-22 14:41:44 +0000"
relations: {}
---
# Serialize Assigned Atom Identities

**every** assigned Atom ID **must** begin with the registered uppercase Project identity prefix. the Project-owned Atom ID encoding **must** match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. the Atom Content Role Identity Letter **must** be **in** (Concern: C, Analysis: A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Implementation: I, Operations: O). a `<PROJECT_PREFIX>-P` Identifier **must** identify a Plan Atom, including one labeled Epic, **and** **must not** identify a separate non-Atom collection.
