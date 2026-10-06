---
subjects:
  governs: "Projection"
  depends_on:
    - "Artifact/Revision"
version: 2
updated_at: "2026-09-17 04:06:18 +0000"
relations: {"child_of":["CAPRMEDIO-META-REQU-657"]}
---
# Record Projection dependency provenance only when required

a Projection **must** record dependency provenance **only** **when** its registered job requires that information; no Projection is required **to** persist a blanket source frontier.

this conditional recording obligation does **not** remove source traceability required by CAPRMEDIO-META-REQU-657 **or** a more specific admitted Projection specification.
