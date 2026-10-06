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
version: 9
updated_at: "2026-09-16 21:24:29 +0000"
relations:
  relates_to:
    - CA-R-1491
---
# Serialize Work Journal Event Properties

**every** Work Journal Event Carrier record **must** serialize its Event identity, Action identity, Type value, action Kind, Author, timezone-qualified Occurred At, session provenance, **and** Structural Scope **in** its registered schema.

- the Carrier **must** preserve recorded Project identifiers, filenames, paths, **and** other observed values exactly through safe encoding; those values **must not** be rewritten **to** satisfy current Atom naming **or** classification rules.
- a recorded Atom ID, including a legacy **or** nonconforming ID, is payload data. its presence does **not** establish that the identified Atom conforms **to** Applicable Methodology.
- event-format, required-field, event-identity, digest, **and** append-only integrity checks apply under CA-R-1491. current Project grammar **must not** become an additional payload-admission gate.
