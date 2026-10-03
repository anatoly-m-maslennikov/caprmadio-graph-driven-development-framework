---
atom_id: CA-D-295
cce_version: cce_1
cce_form: placement
subjects:
  governs: "Artifact/Carrier Placement"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
    - "Atom/Content Role: Delivery"
version: 10
updated_at: "2026-09-11 02:13:22 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Place Carriers by Revision Status

**when** Activity applies under CA-R-1307 **and** the Artifact has **`=1`** valid current Revision Status, its Carrier **must** live directly **in** its canonical current directory **if** Activity **`=`** Active, **and** **otherwise** **must** live **in** the lowercase subdirectory named for that Status. **when** Activity does **not** apply, its Carrier placement **must** follow its applicable Delivery Atoms **without** deriving a subdirectory from an absent Status **or** treating absent Activity as Inactive.
