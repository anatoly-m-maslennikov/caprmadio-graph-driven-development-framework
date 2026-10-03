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
version: 1
updated_at: 2026-08-27 20:26:51 +0400
relations: {}
---
# Retrieve Applicable Methodology Mechanically

to retrieve Applicable Methodology for one Subject or Process query, the Retriever **must** select matching GOVERNS paths from the applicable GOVERNS index, add DEPENDS_ON authority only through transitive prerequisite closure in the applicable DEPENDS_ON index, retain compilation output order, and return no Atom **if** no matching GOVERNS path exists.
