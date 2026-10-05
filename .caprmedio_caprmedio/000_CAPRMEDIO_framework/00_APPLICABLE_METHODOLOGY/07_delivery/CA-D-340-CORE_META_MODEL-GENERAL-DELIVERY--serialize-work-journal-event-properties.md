---
subjects:
  governs: "Work Journal/Event/Carrier Serialization"
  depends_on:
    - "Work Journal/Event/Type"
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
version: 11
updated_at: "2026-09-29 22:34:46 +0000"
relations:
  relates_to:
    - CA-R-1491
atom_id: "CA-D-340"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-340-CORE_META_MODEL-GENERAL-DELIVERY--serialize-work-journal-event-properties.md
  source_atom_id: CA-D-340
  source_atom_revision: 11
  source_sha256: f10f4d14cda74263ab6c9ab5cad1f98ffc4f32a843ba4adf5ac01ce349710504
  original_relations_sha256: fa17cb2940d3d5f3c20487f9702e146d5406ed2c969cbd11a75fa082ea547405
---
# Summary
Serialize Work Journal Event Properties

## Scope
serialization of Work Journal Event Carrier records.

## Claim
**every** Work Journal Event Carrier record **must** serialize its Event identity, Action identity, Type value, action Kind, Author, timezone-qualified Occurred At, session provenance, **and** Structural Scope **in** its registered schema.

- the Carrier **must** preserve recorded Project identifiers, filenames, paths, **and** other observed values exactly through safe encoding; those values **must not** be rewritten **to** satisfy current Atom naming **or** classification rules.
- a recorded Atom ID, including a legacy **or** nonconforming ID, is payload data. its presence does **not** establish that the identified Atom conforms **to** Applicable Methodology.
- event-format, required-field, event-identity, digest, **and** append-only integrity checks apply under `CA-R-1491-CORE_META_MODEL-CORE-REQUIREMENT--keep-project-validation-out-of-journal-admission`. current Project grammar **must not** become an additional payload-admission gate.

## Details
