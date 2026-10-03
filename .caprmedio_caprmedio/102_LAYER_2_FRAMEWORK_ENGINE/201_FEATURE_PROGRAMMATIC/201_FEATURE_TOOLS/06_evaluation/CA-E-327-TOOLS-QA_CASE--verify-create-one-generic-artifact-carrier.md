---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on:
    - "Artifact"
    - "Artifact/Carrier"
version: 9
updated_at: "2026-09-17 21:58:20 +0000"
relations:
  evaluation_for:
    - CA-M-209
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify create one generic Artifact carrier

## Claim checked

CA-M-209 derives **and** creates **=1** non-Atom generic Artifact Carrier under its admitted schema **without** overwrite **or** identity collision.

## Applicable when

apply **when** generic Artifact construction **or** Carrier-identity derivation mechanics change.

## Test cases

- supply one structural owner **and** **all** inputs required by an admitted non-Atom Carrier schema that derive a known valid destination.
- include an admitted schema that does **not** require Atom Content Role, title **or** Markdown body, **and** verify that their absence alone is **not** rejected.
- repeat with inputs that collide with an existing Carrier identity **or** destination, **and** with a required schema input missing.

## Acceptance criteria

- collision **and** missing-required-input cases create nothing **and** leave existing Carriers unchanged.
- authorized valid creation produces **=1** Carrier at the derived destination with the identity, complete schema-valid content **and** Carrier digest required by the selected schema.
- Atom-specific fields are required **only** **when** the admitted schema actually requires them; this Evaluation does **not** define a new schema **or** a public substitute for `ATOM_CREATE`.

## Failure disposition

reject incorrect derivation, incomplete content, invented universal Atom-field requirements **or** an overwrite. preserve construction inputs, selected schema, destination **and** identity resolution, collision evidence **and** complete Carrier digest.
