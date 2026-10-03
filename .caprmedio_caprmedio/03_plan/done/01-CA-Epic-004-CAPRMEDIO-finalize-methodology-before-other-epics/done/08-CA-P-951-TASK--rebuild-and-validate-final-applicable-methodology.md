---
atom_id: CA-P-951
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Final Applicable Methodology
    occurrent:
      - Final Applicable Methodology Compilation and Validation
  depends_on:
    occurrent:
      - CA-P-950
version: 1
updated_at: 2026-09-03 21:28:22 +0400
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-950
---
# Rebuild and Validate the Final Applicable Methodology

**when** CA-P-950 is Done, **then** the Assignee **must** compile, atomically apply, **and** validate the final Applicable Methodology from the exact resolved Methodology Source frontier.

## Scope

`((all final Active RMEDO Atom revisions in CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION) union (the current methodology compiler, retrieval, graph, validation, and test Carriers) union (the generated APPLICABLE_METHODOLOGY RMEDO Carrier tree) union (all completion evidence for CA-P-944 through CA-P-950))`

## Definition of Done

the Task is **not done if** (compilation selects Concern, Analysis, Plan, Implementation, Draft, Archived, Done, **or** Canceled Atoms **or** **any** conflict, unresolved conflict, gap, ambiguity, invalid cycle, duplicate, missing Subject, missing Term, Extension rewrite, Local Configuration rewrite, failing conformance check, source mismatch, stale approval, **or** Projection drift remains **or** a generated Atom changes source Claim authority, identity, **or** revision **or** a generated Atom omits its repository-relative source path **or** two identical dry-runs differ **or** deletion followed by regeneration changes the output **or** the validated source frontier is not a Core-only fixed point **and** a Core-plus-Extensions-plus-Local fixed point **or** **any** relevant Tool or test fails **or** another active Epic starts **before** this Epic is Done).

## Details

preserve APPLICABLE_METHODOLOGY as a non-authoritative generated Projection. record exact source-frontier, report, generated-tree, Tool, **and** test receipts before moving this Task **and** Epic to Done.
