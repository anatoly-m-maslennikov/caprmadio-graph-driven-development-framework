---
atom_id: CAPRMEDIO-META-REQU-158
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Journal
  depends_on:
    continuant:
      - Project
      - Artifact
      - Implementation
version: 9
updated_at: "2026-09-10 22:35:50 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-007-CORE-REQUIREMENT--full-minimal-traceability
---
# Use one Project Journal for governed provenance

**every** Project **must** use **`=1`** authoritative Journal for **all** governed actions **and** Artifact changes, including workflow **and** Implementation events. this Project-wide Journal is its Work Journal; its append-only history **must** remain replayable, checkable, **and** recoverable independently of Git topology **or** another secondary record.
