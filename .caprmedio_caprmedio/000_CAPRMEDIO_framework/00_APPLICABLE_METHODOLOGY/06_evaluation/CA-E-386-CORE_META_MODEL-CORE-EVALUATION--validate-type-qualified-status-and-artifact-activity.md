---
atom_id: CA-E-386
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Type-Qualified Status Validation
  depends_on:
    continuant:
      - Artifact/Revision/Status
      - Artifact/Activity
      - Atom/Content Role
      - Type
      - "Atom Collection/Type: Epic/Status"
version: 8
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-386-CORE_META_MODEL-CORE-EVALUATION--validate-type-qualified-status-and-artifact-activity.md
---
# Validate Type-Qualified Status and Artifact Activity

the Evaluation **must** reject an Artifact **if** its Status domain is resolved outside its complete qualified Type **or** Atom Content Role **and** Type path, its current Status cardinality is not **`=1`**, its current Status is not an allowed value of that resolved domain, its Activity cardinality is not **`=1`**, its Activity does not derive as Active exactly from Status Active **or** as Inactive from any other Status, a prior transition coexists as current Status metadata, **or** a second revision-disposition axis duplicates Status.
