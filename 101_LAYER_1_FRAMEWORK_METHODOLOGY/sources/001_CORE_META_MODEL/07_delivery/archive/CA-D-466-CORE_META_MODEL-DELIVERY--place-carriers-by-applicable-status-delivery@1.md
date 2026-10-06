---
cce_version: cce_1
cce_form: placement
subjects:
  governs: "Artifact/Carrier Placement"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
    - "Atom/Content Role: Delivery"
version: 1
updated_at: "2026-09-20 23:55:10 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-461"]}
---
# Place Carriers by Applicable Status Delivery

**when** Activity applies **and** an Artifact has **`=1`** valid current Revision Status, its Carrier placement **must** follow the most specific applicable Delivery rule for that Artifact Type; **only when** no more specific mapping exists, Active uses the canonical current directory **and** another Status uses its lowercase Status subdirectory. **when** Activity does **not** apply, Carrier placement **must not** derive a Status directory from absent Activity.
