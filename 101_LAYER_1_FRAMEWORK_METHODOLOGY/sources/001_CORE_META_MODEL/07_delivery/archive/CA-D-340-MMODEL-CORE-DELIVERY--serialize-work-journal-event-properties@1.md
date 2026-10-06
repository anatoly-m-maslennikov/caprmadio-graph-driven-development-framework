---
atom_id: CA-D-340
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Work Journal/Event/Carrier Serialization
  depends_on:
    continuant:
      - Work Journal/Event/Type
version: 1
updated_at: 2026-08-28 23:25:00 +0400
relations: {}
---
# Serialize Work Journal Event Properties

every Work Journal Event Carrier record **must** serialize its Event identity, Action identity, Event Type, action Kind, Author, timezone-qualified Occurred At, session provenance, and Structural Scope in its registered schema.
