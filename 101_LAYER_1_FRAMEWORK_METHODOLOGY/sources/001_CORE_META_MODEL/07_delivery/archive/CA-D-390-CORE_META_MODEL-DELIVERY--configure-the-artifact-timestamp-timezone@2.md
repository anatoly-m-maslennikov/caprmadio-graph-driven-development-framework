---
atom_id: CA-D-390
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/Artifact Timestamp Timezone"
  depends_on:
    continuant:
      - "Framework Instance Settings"
      - "Artifact/Revision"
      - "Carrier"
version: 2
updated_at: "2026-09-11 22:30:02 +0400"
relations:
  child_of:
    - "CA-D-311"
    - "CA-R-1402"
---
# Configure the Artifact timestamp timezone

the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` **to** `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS`, **and** the setting supplies its timezone interpretation.
