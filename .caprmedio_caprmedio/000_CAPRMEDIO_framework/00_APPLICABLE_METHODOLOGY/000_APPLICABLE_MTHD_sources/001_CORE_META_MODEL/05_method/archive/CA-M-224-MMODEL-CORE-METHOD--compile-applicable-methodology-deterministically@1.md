---
atom_id: CA-M-224
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Applicable Methodology Compilation
  depends_on:
    continuant:
      - Applicable Methodology/Sources
      - Applicable Methodology
      - Applicable Methodology/Compilation Output
      - Local Configuration
version: 1
updated_at: 2026-08-27 20:26:51 +0400
relations: {}
---
# Compile Applicable Methodology Deterministically

to compile Applicable Methodology, the Compiler **must** perform all of:

1. read only the Source Layer Carriers under `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/` that have an exact governed source reference.
2. confirm the ordered structural Source Layers as CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION.
3. include every active authoritative CORE_META_MODEL Source Atom revision.
4. include every active authoritative LOCAL_CONFIGURATION Source Atom revision that records a retained Project selection or resolution.
5. record INSTALLED_EXTENSIONS as an empty non-contributing structural Source Layer and include no Installed Extension Source Atom revision.
6. apply the exact LOCAL_CONFIGURATION selection, replacement, priority, compatibility, and Customization-reference decisions, and exclude every inactive, replaced, incompatible, or lower-priority Source Atom revision.
7. stop without generating an Output **if** selection or resolution does not produce one unambiguous Source Atom revision for every retained authority.
8. order retained Source Atom revisions by Source Layer order, Atom ID, and canonical relative Carrier path.
9. generate one `APPLICABLE_METHODOLOGY` Projection with the provenance and Subject Indexes required by CA-R-1229 and CA-R-1230.
10. calculate the source-frontier digest from the canonical UTF-8 JSON serialization of the ordered Source Layer, Atom ID, Atom revision, canonical relative Carrier path, and Carrier SHA-256 records.
11. calculate the output digest from the canonical UTF-8 JSON serialization of the ordered Output manifest and both Subject Indexes.
12. stop without generating an Output **if** either digest cannot be reproduced or either Subject Index refers to an Atom revision outside the retained ordered source frontier.
13. preserve every Source Carrier unchanged, use no LLM inference, and treat the generated Projection as non-authoritative and fully regenerable from the recorded source frontier.
