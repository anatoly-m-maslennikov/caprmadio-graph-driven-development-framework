---
atom_id: CA-P-924
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Applicable Methodology
    occurrent:
      - Applicable Methodology Compilation
  depends_on:
    occurrent:
      - CA-P-923
version: 1
updated_at: 2026-08-29 05:10:05 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Compile and Apply Applicable Methodology

**when** CA-P-923 is Done **and** the current dry-run has zero unresolved conflicts, **then** the Assignee **must** compile **and** atomically apply the Applicable Methodology from the exact approved source frontier.

## Scope

`((the exact final active RMEDO Atom revisions in CORE_META_MODEL and LOCAL_CONFIGURATION) union (the empty non-contributing INSTALLED_EXTENSIONS Scope Unit) union (the current compiler authority, executable Carrier, and tests) union (the generated APPLICABLE_METHODOLOGY RMEDO Atom Carrier directories))`

## Definition of Done

the Task is **not done if** (an unresolved **or** stale-approved conflict permits application **or** compilation selects CAP, Implementation, Draft, Archived, Done, **or** Canceled Atoms **or** output **contains** a monolithic methodology JSON **or** persistent Subject Index **or** a projected Atom Carrier changes source Claim authority, identity, **or** revision **or** a projected Carrier omits its repository-relative source Carrier path **or** source authority changes during staging **or** replacement cannot roll back atomically **or** identical resolved source frontiers produce different output **or** output cannot be regenerated **after** deletion **or** **any** generated Carrier gains independent authority).

## Details

dry-run **before** apply. replace **only** generated RMEDO output directories. preserve exact selected source bytes except for registered Projection provenance. record the source-frontier **and** generated-tree digests.
