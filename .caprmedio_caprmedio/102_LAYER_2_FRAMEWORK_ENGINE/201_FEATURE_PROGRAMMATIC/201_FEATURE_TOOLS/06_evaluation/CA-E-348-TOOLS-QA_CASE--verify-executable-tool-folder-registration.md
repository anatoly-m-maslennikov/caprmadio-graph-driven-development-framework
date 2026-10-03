---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "feature-boundary"
  depends_on:
    - "Project Structure"
    - "Tool"
    - "Projection"
version: 7
updated_at: "2026-09-17 22:33:17 +0000"
relations:
  evaluation_for:
    - CA-R-1483
    - CA-R-1484
    - CA-R-1058
    - CA-M-220
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify executable Tool folder registration

## Claim checked

CA-M-220 admits executable Tool folders through accepted Project Structure declarations, **without** treating folder observations **or** MCP outputs as structural authority.

## Test cases

- provide a valid declared **and** materialized fixture for `GENERATE_PROJECT_GRAPH_STATE`, `CLOSE_ATOM`, `MIGRATE_ATOM_IDENTITY`, `REBIND_ATOM_RELATIONS` **and** `REPLACE_ATOM`. these are fixture members, **not** a closed list of **every** Tool.
- include infrastructure folders, a declared disabled Tool **and** a declared but unmaterialized Tool. distinguish their declarations, executable availability **and** MCP eligibility.
- **in** separate invalid variants, include a duplicate Tool identity **or** an observed executable folder **without** an accepted declaration. repeat resolution over the same unchanged frontier.
- separately exercise an explicitly authorized declaration correction under CA-R-1058, **then** repeat resolution against the resulting accepted declaration. folder discovery alone grants no such authorization.

## Acceptance criteria

- **every** admitted materialized enabled Tool resolves **to** **=1** accepted declaration **and** **=1** eligible MCP identity; the disabled Tool stays declared but is **not** eligible, **and** the unmaterialized declaration is **not** advertised as executable.
- infrastructure folders do **not** become Tool Scope Units. current accepted Names, parents, Types, Labels, applicable orders **and** bindings come from Project Structure.
- duplicate, absent **or** mismatched declarations produce explicit findings **without** inventing structural values **or** publishing a partial frontier as current.
- read-only discovery changes no accepted declaration **or** source Carrier. **only** the separately authorized correction changes its exact approved declaration; repeating resolution does **not** repeat that mutation.
- repeated unchanged resolution returns the same ordered Tool frontier **and** findings.

## Failure disposition

reject invented declarations, unauthorized correction, false executable availability, duplicate identity, lost observations **or** an incomplete current MCP frontier. preserve earlier recoverable output bytes **without** claiming they are current **after** a failed refresh.
