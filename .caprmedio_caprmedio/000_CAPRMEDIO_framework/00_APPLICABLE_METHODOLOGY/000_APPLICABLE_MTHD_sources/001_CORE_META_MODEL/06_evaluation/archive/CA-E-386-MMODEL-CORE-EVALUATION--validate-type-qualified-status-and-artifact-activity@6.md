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
      - Entity/Type/Status
      - Artifact/Activity
      - "Atom Collection/Type: Epic/Status"
version: 6
updated_at: 2026-09-04 03:36:02 +0400
relations: {}
---
# Validate Type-Qualified Status and Artifact Activity

the Evaluation **must** reject an Artifact **if** its Status domain is resolved outside its complete Entity-Type path, its current Status cardinality is not **`=1`**, its Activity cardinality is not **`=1`**, its Activity does not derive as Active exactly from Status Active **or** as Inactive from any other Status, a Requirement, Method, Evaluation, **or** Delivery Atom lacks Status **in** (Draft, Active, Archived), a Task Atom lacks Status **in** (Draft, Active, Done, Cancelled), an Epic lacks Status **in** (Active, Done, Cancelled), a prior transition coexists as current Status metadata, **or** a second revision-disposition axis duplicates Status.
