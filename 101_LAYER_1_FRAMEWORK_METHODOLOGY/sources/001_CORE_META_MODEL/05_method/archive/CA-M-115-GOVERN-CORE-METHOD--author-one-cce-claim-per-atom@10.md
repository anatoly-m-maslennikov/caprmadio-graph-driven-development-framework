---
atom_id: CA-M-115
subjects:
  governs:
    occurrent:
      - Atom Claim Boundary Authoring
  depends_on:
    continuant:
      - Atom
      - Claim
      - Atom/Claim/Scope
      - CCE
cce_version: cce_1
cce_form: method
version: 10
updated_at: 2026-09-04 00:22:20 +0400
relations: {}
---
# Author one CCE Claim per Atom

**to** author an Atom, the Author **must** perform **all** of:

1. identify one statement whose complete effect **must** be accepted, replaced, **and** retired together.
2. split **every** independently replaceable component into another Atom.
3. identify **`=1`** atomic **or** composite Claim Scope.
4. write the complete Claim **in** the current CCE version.
5. remove **every** duplicate alternate authoritative statement.
