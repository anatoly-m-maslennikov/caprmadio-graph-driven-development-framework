---
subjects:
  governs: "projection-pipeline"
  depends_on: []
version: 16
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1059
    - CA-R-1061
    - CA-R-1062
---
# Generate active Requirement Subject Catalog

generate the Subject Catalog through this procedure:

1. resolve **=1** requested structural unit from the common selectors, select **every** active Requirement **in** that unit, exclude inactive Requirements from the displayed rows, **and** bind the output **to** `<selected-structural-unit-root>/stg_requirements_subjects.md`.
2. resolve parent existence, lifecycle, **and** tier against the complete active project Requirement graph **before** restricting displayed rows. treat a Core as structurally valid **only** **when** **every** Requirement parent is a Principle, **and** a Standard as structurally valid **only** **when** **every** Requirement parent is a Core; classify missing, inactive, wrong-tier, cyclic, **or** **otherwise** unplaceable Requirements as Orphans with explicit reasons.
3. require **every** displayed Requirement **to** have one parseable first level-one heading. use its text **after** the `# ` marker verbatim as `Summary`; fail the build **when** that heading is missing **or** ambiguous **and** never substitute filename text.
4. group **every** non-orphan Requirement by its single authored `subject_scopes` value. order Subject groups by the current governed Subject catalog, **then** emit Principle, Core, **and** Standard subsections **in** that order **and** sort rows within **every** tier by numeric Requirement ID.
5. emit exactly three columns: `TYPE + ID`, `Summary`, **and** `Child of`. link `TYPE + ID` as the short identity `REQU-NNN` **to** the canonical Atom; link **every** direct authored `child_of` target **in** `Child of`, sorted by numeric identity **where** multiple targets exist; do **not** replace those targets with ancestors **or** group keys.
6. **after** **all** normal Subject groups, emit **=1** final `Orphans` section. retain the same tier **and** numeric ordering inside it, **and** include the orphan reason **without** adding a fourth table column.
7. bind the selected structural unit, exact complete-graph Atom source frontier, generator version, configuration, source digests, **and** `updated_at`; replace `stg_requirements_subjects.md` atomically **in** that structural-unit root **and** record the completed rebuild through the Work Journal.
8. regenerate from the same frontier **and** configuration **and** require byte-stable semantic output **before** reporting the Subject Catalog current.
