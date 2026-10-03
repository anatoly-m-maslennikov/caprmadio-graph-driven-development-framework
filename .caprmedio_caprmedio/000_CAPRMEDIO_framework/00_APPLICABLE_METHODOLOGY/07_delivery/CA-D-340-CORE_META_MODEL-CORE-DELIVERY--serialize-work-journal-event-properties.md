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
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-340-CORE_META_MODEL-CORE-DELIVERY--serialize-work-journal-event-properties.md
---
# Serialize Work Journal Event Properties

**every** Work Journal Event Carrier record **must** serialize its Event identity, Action identity, Type value, action Kind, Author, timezone-qualified Occurred At, session provenance, **and** Structural Scope **in** its registered schema.
