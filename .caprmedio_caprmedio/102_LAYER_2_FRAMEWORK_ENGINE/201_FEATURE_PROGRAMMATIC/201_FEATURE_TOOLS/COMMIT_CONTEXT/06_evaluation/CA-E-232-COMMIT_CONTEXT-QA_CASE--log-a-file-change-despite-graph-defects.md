---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Work Journal/Governed File Change Event"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
version: 6
updated_at: "2026-09-16 21:24:29 +0000"
relations:
  evaluation_for:
    - CA-R-1491
    - CA-R-804

llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Log a file change despite graph defects

## Claim checked

COMMIT_CONTEXT records an observed file action **without** requiring the surrounding Project graph **or** the changed Carrier **to** conform **to** Applicable Methodology.

## Cases

1. change an Atom while unrelated Carriers share an identity **and** one authored relation names a mismatched **or** missing target.
2. change a Carrier with a broken Atom filename, a legacy ID, invalid lifecycle placement, **or** malformed authored properties.
3. repeat capture for the same observation **without** running a Project-conformance Evaluation.

## Acceptance

- capture returns the actual file action, exact observable path, **and** its observed evidence **without** mutation.
- use unambiguous available classification **and** relation bindings; retain unknown **or** conflicting values as such. do **not** invent a conforming Atom ID, Version, target, **or** graph state.
- preserve a recordable native Carrier observation **when** optional Atom classification fails.
- already available diagnostics **may** accompany the context. their absence **must not** require a conformance scan **or** block the Journal.
- the returned context does **not** assert that the Project passed an Evaluation.

## Failure disposition

reject the logger Implementation **if** it blocks recordable facts on Project-conformance defects, silently repairs observed values, requires a conformance scan, **or** mutates the Project during capture.
