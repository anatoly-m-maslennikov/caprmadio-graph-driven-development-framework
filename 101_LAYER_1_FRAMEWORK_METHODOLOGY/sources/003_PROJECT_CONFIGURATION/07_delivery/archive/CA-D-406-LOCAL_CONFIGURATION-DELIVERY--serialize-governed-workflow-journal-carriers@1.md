---
atom_id: CA-D-406
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Journal/Carrier"
  depends_on:
    continuant:
      - "Journal"
      - "Work Journal"
      - "Implementation Journal"
      - "Project"
version: 1
updated_at: "2026-09-10 21:10:58 +0400"
relations: {}
---
# Serialize Governed Workflow Journal Carriers

**every** governed CAPRMEDIO workflow **or** local project-control Journal Carrier whose append-only NDJSON representation is **not** already governed by CA-D-328 **or** CA-D-339 **must** use append-only NDJSON **in** its applicable registered authoritative place. the CAPRMEDIO Project Work Journal follows CA-D-328; the Implementation Journal follows CA-D-339.
