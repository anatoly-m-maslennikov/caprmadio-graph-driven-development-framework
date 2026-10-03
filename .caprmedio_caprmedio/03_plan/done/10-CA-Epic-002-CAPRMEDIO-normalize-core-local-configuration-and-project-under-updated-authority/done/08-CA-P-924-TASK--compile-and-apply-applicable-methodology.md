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
version: 2
updated_at: 2026-08-30 16:32:06 +0400
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

## Completion Evidence

two byte-identical dry-runs produced digest `3fb8edbd382ff536362eea0dda429e406683503b6213ebf9f711490b261b285e`, selected 632 Atoms, **and** admitted application with zero conflicts from source-frontier digest `5f32d52ff0363624d6dc2bbd80243bb4b4eb6e2b7262d96f89183f81b75d935a`.

the compiler applied 632 RMEDO Atom Carriers with generated-tree digest `7a78d9a32c6000167b6cddad43f6f4fc8e3988d8d93b5c816d3d34aef62d9e3a`; **every** generated Carrier includes a relative source Carrier path, **and** the generated surface contains **only** `04_requirement`, `05_method`, `06_evaluation`, `07_delivery`, **and** `09_ops`.

all nine compiler tests pass.
