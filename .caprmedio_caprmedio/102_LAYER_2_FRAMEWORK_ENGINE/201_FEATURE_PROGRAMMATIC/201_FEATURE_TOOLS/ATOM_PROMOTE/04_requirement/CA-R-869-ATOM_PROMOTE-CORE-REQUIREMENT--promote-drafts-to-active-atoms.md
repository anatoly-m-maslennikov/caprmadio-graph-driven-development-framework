---
subjects:
  governs: "Tool/ATOM_PROMOTE"
  depends_on:
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 10
updated_at: "2026-09-17 23:09:21 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Promote drafts to active Atoms

the `ATOM_PROMOTE` Tool **must** provide canonical promotion of CAPRMEDIO Markdown Drafts into active Atom authority. promotion is **not** archival **or** upgrade.

the capability **must**:

- admit **`=1`** Draft **or** a frozen bulk set of **`>=2`** Drafts **and** their assigned IDs as an all-or-nothing transaction;
- accept Operator-supplied stable IDs matching the Draft Content Roles **and** the next unreused Project-wide numbers under CA-D-450 **and** CA-D-378;
- preserve **every** source Carrier's complete bytes while deriving its canonical active filename **and** placement;
- reject non-Drafts, missing, invalid, mismatched **or** colliding IDs, historical ID reuse, unresolved identity admission, destination collisions, stale preconditions **and** partial operations;
- default **to** a mutation-free dry run **and** accept `--apply` **only** through an authorized Project-local MCP delegation with a sealed Initiative action envelope;
- restore the complete selected mutable before-state **after** an effect **or** postcondition failure **without** changing unrelated Carriers **or** immutable accepted Journal evidence.

CA-O-066 owns the admission Action. CA-E-307 checks the capability **and** recovery conditions; failed **or** unverified restoration is **not** successful recovery.
