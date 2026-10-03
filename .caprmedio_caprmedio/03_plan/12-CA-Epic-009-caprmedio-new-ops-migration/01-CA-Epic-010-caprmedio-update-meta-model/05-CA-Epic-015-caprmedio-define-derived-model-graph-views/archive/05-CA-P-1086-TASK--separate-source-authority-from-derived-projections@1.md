---
atom_id: CA-P-1086
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Projection"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Entity"
    - "Term"
    - "Relation"
    - "CAPRMEDIO Graph"
    - "Entities Graph"
    - "Terms Graph"
    - "Subject Projection"
    - "Artifact/Revision"
    - "Scope Unit"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-13 04:38:30 +0400"
relations:
  depends_on:
    - CA-P-1081
---
# Separate source authority from derived Projections

the Assignee **must** reconcile source authority **and** Projection classification across the selected model-graph authority.

## Scope

(selected active RMEDO Atoms **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL` concerning model facts, graph Projections, their derived views, **and** the corresponding GOVERNS **and** DEPENDS_ON assignments). include the current results of CA-P-1079, CA-P-1080, **and** CA-P-1081 where affected; those Tasks' historical completion records **and** evidence remain unchanged. the CA-P-976 admission boundary applies with its ordered accepted source maps. Drafts, archives, generated Applicable Methodology copies, runtime, Tool Implementation, Settings values, **and** unrelated CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** (a graph Projection, including the Entities Graph, is treated as an independent authoritative source of its represented model facts **or** a Claim governing a Projection is assigned **to** the represented Entity instead of the appropriate Projection Entity **or** a derived view reauthors an upstream fact **or** a Projection chain loses traceability **to** the authoritative source Claims **or** a similar source-versus-Projection misclassification remains unreviewed **in** the selected authority **or** artificial Entity distinctions are introduced merely **to** satisfy an unaccepted Atom-count limit).

## Details

apply the latest Operator correction: source Atoms remain the single source of truth for the represented model facts; the Entities Graph is already a Projection, **and** multiple further Projections **may** be derived from the same source authority **or** from its Projections **without** becoming independent authorities. distinguish the source Atoms that specify a Projection from the derived Artifact that implements that specification. a graph's governing specification does **not** make its derived contents authoritative.

classify graph Projections **and** their derived views **in** the existing Projection Entity branch. resolve exact canonical Subject Paths from governing authority; do **not** guess a new path scheme **or** maintain a parallel independent graph-Entity taxonomy. preserve graph-qualified Relation Kind ownership **without** treating the source facts, a graph Projection, **and** a further filtered view as the same governed Entity. a Claim about a Projection governs the appropriate Projection Entity **and** references its prerequisite Entities through DEPENDS_ON.

review CA-R-1438 **and** CA-R-1456 together, then examine the analogous Terms Graph, terminology indexes, Subject Projection, **and** composed-view authority, including CA-R-1335, CA-R-1454, CA-R-1455, **and** CA-R-1281. this list is a set of anchors, **not** an exhaustive admission list. record the reviewed source identities **and** dispositions. correct demonstrated source-Subject, definition, **and** Evaluation conflicts while preserving distinct valid Claims **and** their source identity. perform semantic consolidation **only** where the current one-Claim authority permits it; do **not** invent Property nodes merely **to** avoid apparent duplication.

the proposed **`<=1`** R **and** **`<=1`** D per Entity is **not** finalized by this Task. multiplicity across Scope Units, Local Tiers, **and** Content Roles remains subject **to** the Operator's separate decision. do **not** use misassigned Projection Claims as evidence that duplicate governing authority is necessary. M **and** E cardinalities remain undecided.

this Task owns the bounded correction of the previously selected source-versus-Projection authority. record ownership transfers relative **to** the immutable CA-P-1078 inventory **and** produce an ordered changed-source map for subsequent Tasks. CA-P-1082 **and** later Tasks consume the corrected authority; unexecuted proposals based on the earlier graph classification require fresh review. D representation remains with CA-P-1084, **and** Operation-specific composition **and** control flow remain with CA-P-980.

review this inserted Task **and** its dependency changes **before** execution. execute **only** this Task **in** its own subagent; **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve exact prior source revisions **and** append-only Journal history. the unresolved commit-before-archive exception for CA-M-232 is **not** approved by this correction; escalate **before** **any** replacement that needs that exception. creating this Task does **not** execute it.
