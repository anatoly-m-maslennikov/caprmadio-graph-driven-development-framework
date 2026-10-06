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
      - Applicable Methodology/Compilation Output
      - Applicable Methodology/Compilation Output/Subject Index
version: 2
updated_at: 2026-08-27 20:40:00 +0400
relations: {}
---
# Retrieve Applicable Methodology Mechanically

to retrieve Applicable Methodology for one Subject or Process query, the Retriever **must** derive GOVERNS and DEPENDS_ON indexes on demand from the generated projected Atom Carriers, select matching GOVERNS paths, add DEPENDS_ON authority only through transitive prerequisite closure, retain compilation output order, store no Index Carrier, and return no Atom **if** no matching GOVERNS path exists.
