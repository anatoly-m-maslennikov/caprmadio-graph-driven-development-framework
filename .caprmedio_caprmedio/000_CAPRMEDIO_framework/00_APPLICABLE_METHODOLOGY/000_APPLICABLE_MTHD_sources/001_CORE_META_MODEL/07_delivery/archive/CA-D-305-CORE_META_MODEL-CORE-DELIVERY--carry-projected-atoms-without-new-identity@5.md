---
atom_id: CA-D-305
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Applicable Methodology/Projected Atom Carrier"
  depends_on:
    - "Applicable Methodology/Member"
    - "Atom/Revision"
    - "Methodology Source/Carrier"
version: 5
updated_at: "2026-09-15 19:28:04 +0400"
relations: {}
---
# Carry Projected Atoms without New Identity

**every** Applicable Methodology projected Atom Carrier **must** preserve its selected authoritative source Atom Revision as follows:

- copy the source Carrier bytes unchanged, including its Frontmatter **and** Main Content.
- retain the source Atom identity **and** Claim authority **without** assigning a new Artifact identity.
- do **not** inject a `projection` block, `source_carrier_path` field, **or** other compiler-added metadata into the projected Atom Carrier.

source traceability **must** remain recoverable from the selected authoritative source frontier **without** adding that bookkeeping **to** Atom content.
