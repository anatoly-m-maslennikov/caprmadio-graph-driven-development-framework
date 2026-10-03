---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on:
    - "Artifact"
    - "Artifact/Carrier"
    - "Atom/Content Role"
version: 8
updated_at: "2026-09-17 20:26:41 +0000"
relations:
  method_for:
    - CA-R-1132
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Create one generic Artifact carrier

## Applicable when

use this Method **when** a canonical Tool delegates generic construction of **=1** non-Atom Artifact Carrier under its admitted schema.

## Procedure

1. accept the structural owner **and** **all** inputs required by the admitted Artifact Carrier schema.
2. derive the canonical identity, filename, **and** owner-relative destination required by that schema **and** its active Carrier rules.
3. preflight the resolved destination **and** identity against existing carriers **and** reject **every** collision **or** implicit overwrite.
4. build the Carrier from the supplied schema-valid inputs, preserving the derivation inputs **in** the dry-run result.
5. on authorized apply, create exactly the derived Carrier **and** verify its required identity, placement, complete schema-valid content, **and** Carrier digest.

## Outcome

**=1** generic Artifact Carrier is created with the identity, placement, **and** content required by its admitted schema, **or** the repository remains unchanged.

## Failure or stop

reject an absent structural owner **or** schema-required input, invalid derivation, collisions, **and** requests that treat this helper as a public alternative **to** `ATOM_CREATE`. Content Role, title, **and** body **must not** be required universally merely because Markdown Atoms use them.
