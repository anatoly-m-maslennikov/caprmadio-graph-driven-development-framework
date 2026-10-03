---
atom_id: CA-E-381
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Applicable Methodology Retrieval Tool/Validation
  depends_on:
    continuant:
      - Applicable Methodology Retrieval Tool
    occurrent:
      - Applicable Methodology Retrieval Tool/Execution
version: 3
updated_at: 2026-09-01 02:45:00 +0400
relations:
  evaluation_for:
    - CA-M-227
---
# Validate Source-Backed Subject Retrieval

## Test case

the Applicable Methodology Retrieval Tool Validation **must not pass** if (a Subject query matches a non-governing Carrier **or** a Process query matches a non-occurrent governed Subject Path **or** a prerequisite governor is omitted **or** compilation order changes **or** an unresolved prerequisite passes silently **or** a projected Carrier differs from its Source Carrier after Projection metadata removal **or** the same frontier and query produce different results **or** retrieval writes a persistent Subject Index Carrier, cache, Source Carrier, or generated methodology Carrier).

## Sources

- [CA-M-227 — Retrieve Subject Authority Without Persistent Indexes](../05_method/CA-M-227-RETRIEVE_APPLICABLE_METHODOLOGY-CORE-IMPL_METHOD--retrieve-subject-authority-without-persistent-indexes.md)
- [CA-R-1241 — Require Source-Backed Subject Retrieval](../04_requirement/CA-R-1241-RETRIEVE_APPLICABLE_METHODOLOGY-CORE-REQUIREMENT--require-source-backed-subject-retrieval.md)
