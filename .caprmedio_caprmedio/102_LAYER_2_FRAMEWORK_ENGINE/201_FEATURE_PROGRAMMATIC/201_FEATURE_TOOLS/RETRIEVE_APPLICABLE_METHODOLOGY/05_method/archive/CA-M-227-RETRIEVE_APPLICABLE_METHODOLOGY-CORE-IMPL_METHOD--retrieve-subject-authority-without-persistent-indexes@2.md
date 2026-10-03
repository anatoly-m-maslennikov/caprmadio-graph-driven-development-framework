---
atom_id: CA-M-227
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Applicable Methodology Retrieval Tool/Execution
  depends_on:
    continuant:
      - Applicable Methodology Retrieval Tool
    occurrent:
      - Applicable Methodology Retrieval
version: 2
updated_at: 2026-09-01 02:25:00 +0400
relations:
  method_for:
    - CA-R-1241
---
# Retrieve Subject Authority Without Persistent Indexes

to retrieve applicable authority, the Tool **must** validate every projected Carrier against its relative `projection.source_carrier_path`, derive `GOVERNS` and `DEPENDS_ON` indexes in memory, seed exact matching governed Subject Paths, close every prerequisite transitively, fail closed on an unresolved prerequisite, emit ordered Source-backed Carrier records, and write no persistent Subject Index Carrier or cache.

## Sources

- [CA-R-1241 — Require Source-Backed Subject Retrieval](../04_requirement/CA-R-1241-RETRIEVE_APPLICABLE_METHODOLOGY-CORE-REQUIREMENT--require-source-backed-subject-retrieval.md)
