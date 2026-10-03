---
version: 10
updated_at: "2026-09-17 05:07:33 +0000"
relations: {"child_of":["CA-E-001"],"evaluation_for":["CA-M-298","CA-O-054","CA-R-1375"]}
subjects:
  governs: "Methodology Source/expansion mapping"
  depends_on:
    - "Methodology Source"
    - "Core Meta-Model"
    - "Extension"
    - "Project Configuration"
    - "Operator"
    - "Entity"
---
# Evaluate methodology expansion mappings

a methodology expansion mapping Evaluation **must** return `fail` **if** a source element, exact canonical target, mapping rule, intended Scope, **or** applicable Core Meta-Model distinction at **any** Local Tier is missing, canonical ownership is ambiguous, preservation is unproven, **or** the mapping redefines, replaces, shadows, weakens, deletes, contradicts, **or** reinterprets applicable Core Meta-Model authority at **any** Local Tier; it **must** return `pass` **only** **when** the declared mapping preserves that authority **and** stays within its permitted expansion boundary. an Operator-approved loss **must not** count as conformance; report the failed boundary **and** leave the affected application stopped.
