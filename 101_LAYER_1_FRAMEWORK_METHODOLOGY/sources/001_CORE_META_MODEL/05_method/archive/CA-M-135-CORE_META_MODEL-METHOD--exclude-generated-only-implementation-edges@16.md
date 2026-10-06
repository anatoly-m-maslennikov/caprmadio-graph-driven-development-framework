---
subjects:
  governs: "provenance"
  depends_on: []
version: 16
updated_at: "2026-09-14 06:21:07 +0400"
relations: {}
---
# Exclude generated-only implementation edges

provenance validation inspects **every** recorded change **in** the governed selection. a change contributes an Implementation Relation, implementation coverage, **or** semantic traceability edge **only** **when** it changes **`>=1`** non-generated governed source.

an update **only** **to** generated Projections remains an auditable refresh. it retains its required Journal provenance but cannot become an implementation input **to** the semantic graph that produced the generated Carrier. a mixed change participates **only** through its substantive non-generated governed source changes.
