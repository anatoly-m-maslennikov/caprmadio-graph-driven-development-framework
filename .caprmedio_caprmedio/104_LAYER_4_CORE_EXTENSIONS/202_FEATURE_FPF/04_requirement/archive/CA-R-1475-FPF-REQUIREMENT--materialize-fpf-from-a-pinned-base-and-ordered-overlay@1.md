---
atom_id: CA-R-1475
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "FPF"
  depends_on:
    - "Extension"
    - "Extension Candidate"
    - "Skill"
    - "Content Digest"
version: 1
updated_at: "2026-09-15 02:22:01 +0400"
relations: {}
---
# Materialize FPF from a pinned base and ordered overlay

**every** FPF Extension Candidate **must** be materialized reproducibly from **`=1`** exact upstream FPF source revision and **`=1`** ordered project-owned patch overlay, and its immutable manifest **must** identify the complete base inventory and digest, **every** ordered overlay input and digest, the resulting inventory and digest, the exact Extension version, the intended behavior changes, preserved upstream behavior, affected paths, and acceptance Evaluations.
