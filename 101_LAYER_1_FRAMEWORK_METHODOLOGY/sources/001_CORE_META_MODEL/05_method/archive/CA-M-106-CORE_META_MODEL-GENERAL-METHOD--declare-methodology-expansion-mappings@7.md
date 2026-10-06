---
version: 7
updated_at: "2026-09-10 05:28:44 +0400"
relations:
  child_of:
    - "CA-M-006"
  method_for:
    - "CA-R-1375"
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs:
    continuant:
      - "Methodology Source/expansion mapping"
  depends_on:
    continuant:
      - "Methodology Source"
      - "Extension"
      - "Local Configuration"
      - "Core Meta-Model"
      - "Operator"
atom_id: "CA-M-106"
---
# Declare methodology expansion mappings

**before** an Extension **or** Local Configuration relies on a mapped element, declare its source element, exact canonical target, mapping rule, intended Scope, **and** applicable Core Meta-Model distinctions at **any** Local Tier; retain the source provenance **and** apply the same mapping procedure regardless of provenance. evaluate the mapping under CA-E-249 **before** activation **or** reliance **and** **after** a material source, target, rule, Scope, **or** authority change. **if** canonical ownership **or** preservation remains unresolved, **then** stop the affected application **and** return the evidence **to** the Operator; an approval **must not** authorize loss **or** reinterpretation of applicable Core Meta-Model authority at **any** Local Tier.
