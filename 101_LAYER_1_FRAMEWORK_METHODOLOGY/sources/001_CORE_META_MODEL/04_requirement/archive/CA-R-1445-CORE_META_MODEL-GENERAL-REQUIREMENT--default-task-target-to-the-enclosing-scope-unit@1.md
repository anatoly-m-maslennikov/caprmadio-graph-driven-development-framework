---
atom_id: CA-R-1445
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Claim/Structural Entity"
  depends_on:
    continuant:
      - Scope Unit
      - "Atom Collection/Type: Epic"
version: 1
updated_at: "2026-09-12 03:06:55 +0400"
relations: {}
---
# Default Task Target to the Enclosing Scope Unit

a Task Atom with a containing Scope Unit **and** **without** an explicit Claim Structural Entity **must** use its nearest containing Scope Unit as its Claim Structural Entity, independently of containment **in** an Epic **or** nested Epics.
