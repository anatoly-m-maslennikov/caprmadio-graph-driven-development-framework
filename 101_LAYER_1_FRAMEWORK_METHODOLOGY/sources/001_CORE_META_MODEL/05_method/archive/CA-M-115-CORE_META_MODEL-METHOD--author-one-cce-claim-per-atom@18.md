---
subjects:
  governs: "Atom Claim Boundary Authoring"
  depends_on:
    - "Atom"
    - "Claim"
    - "Atom/Claim"
    - "CCE"
cce_version: cce_1
cce_form: method
version: 18
updated_at: "2026-09-22 17:59:17 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Author one CCE Claim per Atom

**to** author an Atom, the Author **must** perform **all** of:

1. identify one statement whose complete effect **must** be accepted, replaced, **and** retired together.
2. split **every** independently replaceable component into another Atom.
3. resolve **`=1`** Claim Target Scope Unit independently of ownership. use the current Scope Unit **when** the target is omitted for a Current-scope Atom; otherwise preserve the explicit permitted target under CA-D-476. express **any** narrower **or** composite applicability as part of the Claim text under CA-D-477; those restrictions alone do **not** make the Atom Relational.
4. write the complete Claim **in** the current CCE version.
5. remove **every** duplicate alternate authoritative statement.
