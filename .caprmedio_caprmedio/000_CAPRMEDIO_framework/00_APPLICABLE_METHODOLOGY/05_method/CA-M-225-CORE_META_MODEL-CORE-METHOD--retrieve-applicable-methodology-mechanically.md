---
atom_id: CA-M-225
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Applicable Methodology Retrieval
  depends_on:
    continuant:
      - Applicable Methodology
      - Atom/Subjects
version: 7
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-225-CORE_META_MODEL-CORE-METHOD--retrieve-applicable-methodology-mechanically.md
---
# Retrieve Applicable Methodology Mechanically

**to** retrieve Applicable Methodology for one Subject **or** Process query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.
