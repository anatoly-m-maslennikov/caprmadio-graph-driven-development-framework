---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 9
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1129
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Read generic Artifact metadata

## Applicable when

use this Method **when** framework internals need selected frontmatter **and** derived identity for **=1** generic Artifact.

## Procedure

1. resolve **=1** generic Artifact carrier from the caller-supplied carrier identity **or** path, **without** applying CAPRMEDIO Atom selector semantics.
2. seal its path, filename, **and** source digest, **then** parse **only** its frontmatter **without** loading its body.
3. return the requested registered fields **and** carrier-derived identity; represent **every** absent field **and** **every** parse error explicitly.
4. mark the result as a form-agnostic helper result **and** retain the source identity **and** digest needed **to** attribute it.
5. return no mutation plan **and** do **not** expose this helper as a public substitute for `ATOM_READ`.

## Outcome

callers receive an attributable body-free metadata result for **=1** generic Artifact carrier.

## Failure or stop

return an explicit result for an absent carrier, ambiguous identity, unsupported field, **or** malformed frontmatter **without** mutation.
