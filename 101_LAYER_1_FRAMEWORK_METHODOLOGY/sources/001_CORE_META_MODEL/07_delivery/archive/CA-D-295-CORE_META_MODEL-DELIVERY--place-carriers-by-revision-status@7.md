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
version: 7
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
---
# Place Carriers by Revision Status

an Artifact Carrier **must** live directly **in** its canonical current directory **if** Artifact Activity **`=`** Active **and** **otherwise** **must** live **in** the lowercase subdirectory named for its current Revision Status.
