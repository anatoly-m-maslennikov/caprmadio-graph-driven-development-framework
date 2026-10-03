---
atom_id: CA-D-295
cce_version: cce_1
cce_form: placement
subjects:
  governs:
    continuant:
      - Artifact/Carrier Placement
  depends_on:
    continuant:
      - Artifact/Activity
      - Artifact/Revision/Status
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-295-CORE_META_MODEL-CORE-DELIVERY--place-carriers-by-revision-status.md
---
# Place Carriers by Revision Status

an Artifact Carrier **must** live directly **in** its canonical current directory **if** Artifact Activity **`=`** Active **and** **otherwise** **must** live **in** the lowercase subdirectory named for its current Revision Status.
