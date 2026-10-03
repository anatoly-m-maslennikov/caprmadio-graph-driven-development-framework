---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Type-Qualified Status Validation"
  depends_on:
    - "Artifact/Revision/Status"
    - "Artifact/Activity"
    - "Atom/Content Role"
    - "Type"
    - "Atom/Content Role: Plan/Type: Plan/Status"
version: 15
updated_at: "2026-09-22 14:41:44 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Type-Qualified Status and Artifact Activity

the Evaluation **must** reject an Artifact **if** **any** applicable condition holds:

- **when** an explicitly defined Status model applies, its Status domain is resolved outside its complete qualified Type **or** Atom Content Role **and** Type path, its current Status cardinality **`!=1`**, its current Status is **not** an allowed value of that domain, its Activity cardinality **`!=1`**, its Activity violates CA-R-1395 **or** CA-R-1396, a prior transition coexists as current Status metadata, **or** a second revision-disposition axis duplicates Status.
- **when** no explicitly defined Status model applies, its Activity cardinality **`!=0`** under CA-R-1307.

the Evaluation **must not** substitute Active **or** Inactive for absent Activity **or** a missing, invalid, **or** ambiguous Status. an Artifact outside the applicability of CA-R-1307 **must not** fail this Evaluation merely because it has no Status **or** Activity.
