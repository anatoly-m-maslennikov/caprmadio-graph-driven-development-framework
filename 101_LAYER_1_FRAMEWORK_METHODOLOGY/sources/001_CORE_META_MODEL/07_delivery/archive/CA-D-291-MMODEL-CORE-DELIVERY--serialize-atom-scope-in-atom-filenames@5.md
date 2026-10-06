---
atom_id: CA-D-291
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Atom/Scope/Filename Token
  depends_on:
    continuant:
      - Atom/Scope
      - Scope Unit
version: 5
updated_at: 2026-09-04 00:22:20 +0400
relations: {}
---
# Serialize Atom Scope in Atom Filenames

**every** Project-owned Atom filename **must** serialize its non-Project Scope Unit Atom Scope exactly once **and** **must** omit that segment **if** the Project Scope Unit is its Atom Scope.
