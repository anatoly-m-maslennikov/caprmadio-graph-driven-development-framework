---
atom_id: CA-M-115
subjects:
  governs: "Atom Claim Boundary Authoring"
  depends_on:
    - "Atom"
    - "Claim"
    - "Atom/Claim/Scope"
    - "CCE"
cce_version: cce_1
cce_form: method
version: 16
updated_at: "2026-09-10 03:25:26 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Author one CCE Claim per Atom

**to** author an Atom, the Author **must** perform **all** of:

1. identify one statement whose complete effect **must** be accepted, replaced, **and** retired together.
2. split **every** independently replaceable component into another Atom.
3. identify **`=1`** resolved atomic **or** composite Claim Scope; omit its duplicate representation for a Current-scope Atom **and** represent its different target explicitly for a Relational Atom.
4. write the complete Claim **in** the current CCE version.
5. remove **every** duplicate alternate authoritative statement.
