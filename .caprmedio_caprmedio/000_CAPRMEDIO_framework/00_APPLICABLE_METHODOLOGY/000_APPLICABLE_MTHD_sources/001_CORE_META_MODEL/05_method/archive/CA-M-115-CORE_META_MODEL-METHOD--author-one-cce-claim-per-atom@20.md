---
subjects:
  governs: "Atom Claim Boundary Authoring"
  depends_on:
    - "Atom"
    - "Claim"
    - "Atom/Claim"
    - "CCE"
version: 20
updated_at: "2026-09-22 23:02:20 +0000"
relations: {}
---
# Summary

Author one CCE Claim per Atom

## Claim

**to** author an Atom, the Author **must** perform **all** of:

1. identify one statement whose complete effect **must** be accepted, replaced, **and** retired together.
2. split **every** independently replaceable component into another Atom.
3. resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit **as** the default during authoring **or** select an explicitly permitted different target; carry the resolved value under CA-D-482. express **any** narrower **or** composite applicability as part of the Claim text under CA-D-477; those restrictions alone do **not** make the Atom Relational.
4. write the complete Claim **in** the current CCE version.
5. remove **every** duplicate alternate authoritative statement.
