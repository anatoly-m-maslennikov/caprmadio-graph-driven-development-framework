---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - extension-promotion
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1149
  derived_from:
    - CA-A-058
---
# Extract one Extension candidate from Project Adaptation

## Applicable when

Use this Method when an operator selects reusable Project Adaptation authority for extraction as one Extension candidate.

## Procedure

1. Seal the operator-selected adaptation Atoms and resolve their direct dependency closure across current active authority.
2. Traverse declared required dependencies to the complete closure and preserve each selected and transitively required source Atom reference exactly.
3. Reject the extraction when any required dependency is absent, ambiguous, or unresolved; do not omit it or infer a replacement.
4. Assign the candidate its own stable identity and preserve the exact selected membership, transitive closure, source revisions, and frontier digest.
5. Emit the bounded candidate without modifying its source Project Adaptation authority.

## Outcome

One independently identified Extension candidate contains the selected Project Adaptation authority and its complete attributable required dependency closure.

## Failure or stop

Stop on unresolved required dependencies, stale source revisions, ambiguous closure, or a candidate boundary that cannot be attributed exactly.
