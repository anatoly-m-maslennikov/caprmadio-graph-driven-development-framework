---
atom_id: "CA-E-249"
tier: "core"
version: 2
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  child_of:
    - "CA-E-001"
  evaluation_for:
    - "CA-M-106"
    - "CA-R-1375"
cce_version: "cce_1"
cce_form: "evaluation"
subjects:
  governs:
    continuant:
      - "Methodology Source/expansion mapping"
  depends_on:
    continuant:
      - "Methodology Source"
      - "Core Meta-Model"
      - "Extension"
      - "Local Configuration"
      - "Operator"
      - "Entity"
---
# Evaluate methodology expansion mappings

a methodology expansion mapping Evaluation **must** return `fail` **if** a source element, exact canonical target, mapping rule, intended Scope, **or** applicable Core distinction is missing, canonical ownership is ambiguous, preservation is unproven, **or** the mapping redefines, replaces, shadows, weakens, deletes, contradicts, **or** reinterprets applicable Core authority; it **must** return `pass` **only** **when** the declared mapping preserves that authority **and** stays within its permitted expansion boundary. an Operator-approved loss **must not** count as conformance; report the failed boundary **and** leave the affected application stopped.
