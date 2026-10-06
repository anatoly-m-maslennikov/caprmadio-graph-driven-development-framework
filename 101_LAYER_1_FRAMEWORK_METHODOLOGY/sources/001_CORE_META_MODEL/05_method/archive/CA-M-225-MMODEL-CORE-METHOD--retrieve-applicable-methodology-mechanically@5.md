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
      - Atom/Claim/Claim-Subject Relation
version: 5
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Retrieve Applicable Methodology Mechanically

**to** retrieve Applicable Methodology for one Subject **or** Process query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom relations, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.
