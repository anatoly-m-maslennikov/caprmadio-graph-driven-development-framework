---
atom_id: CA-R-1414
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - Atom/Revision/Identifier
  depends_on:
    continuant:
      - Atom/Identity
      - Atom/Revision/Version
      - "Atom/Revision/Status: Draft"
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1414-CORE_META_MODEL-CORE-REQUIREMENT--give-every-non-draft-atom-revision-one-identifier.md
---
# Give Every Non-Draft Atom Revision One Identifier

**every** non-Draft Atom Revision **must** have **`=1`** Identifier composed from its Atom Identity **and** Version.
