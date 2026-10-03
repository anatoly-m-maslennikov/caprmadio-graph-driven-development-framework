---
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - "CA-M-006"
  method_for:
    - "CA-R-1375"
  replacement_of:
    - "CA-M-107"
    - "CA-M-108"
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
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-106-CORE_META_MODEL-CORE-METHOD--declare-methodology-expansion-mappings.md
---
# Declare methodology expansion mappings

**before** an Extension **or** Local Configuration relies on a mapped element, declare its source element, exact canonical target, mapping rule, intended Scope, **and** applicable Core distinctions; retain the source provenance **and** apply the same mapping procedure regardless of provenance. evaluate the mapping under CA-E-249 **before** activation **or** reliance **and** **after** a material source, target, rule, Scope, **or** authority change. **if** canonical ownership **or** preservation remains unresolved, **then** stop the affected application **and** return the evidence **to** the Operator; an approval **must not** authorize loss **or** reinterpretation of applicable Core authority.
