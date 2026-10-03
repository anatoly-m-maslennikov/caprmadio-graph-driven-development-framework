---
atom_id: CA-P-1090
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Artifact/Carrier"
  depends_on:
    - "Artifact"
    - "Artifact/Revision"
    - "Projection"
    - "Journal"
    - "Atom"
    - "Scope Unit"
    - "Relation Kind"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-13 05:38:50 +0400"
relations:
  depends_on:
    - CA-P-1089
---
# Reconcile general Projection and Journal carriers

the Assignee **must** reconcile the general Delivery authority for Projection **and** Journal Carriers.

## Scope

(generic Projection **and** Journal Carrier authority selected by CA-P-1087, excluding view-specific output specifications owned by CA-P-1084 **and** Operation-specific records owned by CA-P-983). the source admission boundary is selected active RMEDO authority **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`, reconstructed from CA-P-976 **and** the ordered accepted source maps, including the sealed CA-P-980 direct-Subjects stage. Project Principles are read-only governing prerequisites. Drafts, prior archives, completed Task records, sealed evidence, generated Applicable Methodology, settings values, Tool Implementation, **and** unrelated CAP Atoms are excluded from mutation. administrative Task records, exact prior revisions, **and** append-only Journal evidence are recorded separately.

## Definition of Done

the Task is **not** Done **if** (a necessary generic Carrier rule lacks D authority **or** stored metadata obscures source authority **or** a derived output cannot represent its required source traceability **or** Journal record identity cannot be distinguished from event identity **or** a generic rule imposes an unapproved concrete Project path **or** stale outputs are treated as current authority).

## Details

reuse existing D Atoms for identifiers, revision **and** timestamp representation, fields, filenames, placement, **and** content boundaries. distinguish what is stored from how it is formatted, what it requires, **and** what is checked. specify enough source identity **and** revision metadata for derived outputs **without** independently maintaining duplicate truth. preserve append-only Journal Carrier responsibilities, registered location, **and** permitted physical partitioning. a Projection **may** have its own Artifact identity **without** gaining authority over its derived facts. do **not** force all Projections into JSON, move actual carriers, rebuild outputs, change settings values, **or** implement logging. hand graph-view-specific D refinements **to** CA-P-1084 **and** execution/state-change-specific D refinements **to** CA-P-983.

reuse accepted authority **and** preserve one Claim **and** one Claim Scope Unit per Atom. R establishes the model, M covers Implementation choices **or** conventions, E checks correctness, D specifies Carriers, **and** reusable Actions **or** Processes belong **to** O. do **not** require an Atom **in** **every** Content Role. do **not** settle the unapproved per-Entity R/D/M/E counts **or** invent Entities merely **to** satisfy a count.

review this sub-Epic **before** execution. execute Tasks sequentially, **only** **after** the explicit prerequisite is Done, with **every** Task **in** its own subagent. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve existing staged changes; creating this Epic grants no Git mutation **or** exception **to** the CA-M-274 commit-before-archive rule, including the unresolved replacement of CA-M-232. creating a Task does **not** execute it.
