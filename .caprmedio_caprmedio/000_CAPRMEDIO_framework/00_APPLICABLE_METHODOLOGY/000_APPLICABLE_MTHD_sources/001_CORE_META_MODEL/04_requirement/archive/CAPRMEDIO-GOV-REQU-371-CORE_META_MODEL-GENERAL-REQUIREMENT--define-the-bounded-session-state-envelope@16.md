---
subjects:
  governs: "Session-State Envelope"
  depends_on:
    - "runtime"
version: 16
updated_at: "2026-09-10 07:34:05 +0400"
relations: {}
---
# Define the bounded session-state envelope

the bounded session-state envelope **must** contain **only** routing invariants, current scope, applicable settings, compact session state, **and** references needed **to** load active authority on demand.
