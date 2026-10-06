---
atom_id: CAPRMEDIO-GOV-REQU-371
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Session-State Envelope
  depends_on:
    occurrent:
      - runtime
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 10
updated_at: "2026-09-09 21:56:59 +0400"
relations:
  child_of:
    - CA-R-1054
---
# Define the bounded session-state envelope

the bounded session-state envelope **must** contain **only** routing invariants, current scope, applicable settings, compact session state, **and** references needed to load active authority on demand.
