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
version: 7
updated_at: 2026-09-04 23:52:10 +0400
relations: {}
---
# Validate Type-Qualified Status and Artifact Activity

the Evaluation **must** reject an Artifact **if** its Status domain is resolved outside its complete qualified Type **or** Atom Content Role **and** Type path, its current Status cardinality is not **`=1`**, its current Status is not an allowed value of that resolved domain, its Activity cardinality is not **`=1`**, its Activity does not derive as Active exactly from Status Active **or** as Inactive from any other Status, a prior transition coexists as current Status metadata, **or** a second revision-disposition axis duplicates Status.
