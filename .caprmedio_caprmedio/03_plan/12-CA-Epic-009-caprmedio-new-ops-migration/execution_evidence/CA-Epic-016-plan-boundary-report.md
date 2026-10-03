# CA-Epic-016 — Projection and Journal model

Plan-only boundary record, 2026-09-13 05:38:50 +0400. The Operator requested a new Epic with Tasks. No source authority or migration Task is executed by this change.

The Epic is nested at the current CA-Epic-015 checkpoint. Existing P1086 is moved into it with the same identity; five new Tasks are added. There is no duplicate source-versus-Projection Task.

## Ordered Tasks

1. P1087 — Inventory Projection and Journal authority and allocate bounded responsibility.
2. P1086 — Reconcile source authority and Projection classification (existing Task, revised).
3. P1088 — Reconcile the general Journal model and historical records.
4. P1089 — Reconcile graph participation, shared identity, and graph-owned Relation Kinds.
5. P1090 — Reconcile generic Projection and Journal D-defined Carriers.
6. P1091 — Add/check E coverage, validate examples and task boundaries, hand off.

## Authority boundary

Single source of truth is per fact: governing Atom Claims, structural facts from Scope Units, historical records in Journals, and derived Projection contents are not interchangeable. A Projection or Journal may also be a graph node. Its represented/internal relations do not become interchangeable with relations connecting that Artifact to other graph nodes. Each graph kind owns its Relation Kinds; instances reuse those definitions. Multiple views do not create another authoritative fact or another identity for the represented node.

## Non-overlap and sequence

CA-P-1081 -> CA-P-1087 -> CA-P-1086 -> CA-P-1088 -> CA-P-1089 -> CA-P-1090 -> CA-P-1091 -> CA-P-1082 -> CA-P-1083 -> CA-P-1084 -> CA-P-1085 -> CA-P-980

P1082 retains Subject links; P1083 retains composed navigation; P1084 retains graph-view-specific Carrier refinements; P1085 checks their integration. P980 retains Operation composition/control flow. P983 retains state-change versus process-execution logging specialization and consumes the general Journal model. P1087 records any source-ownership transfers from the immutable P1078 inventory before source execution. Earlier Done records and sealed evidence remain historical and unchanged.

The main Epic now contains 116 Tasks: 8 Done and 108 Active, with one chain of 115 prerequisite edges. This count is Task status, not percentage of effort or a claim of source implementation. Execution remains sequential, one Task per dedicated subagent, with a review before this new sub-Epic and a review of the remaining parent after closure.

Scope remains selected active CORE_META_MODEL RMEDO authority. No additional P source exception, settings edits, Tool implementation, generated-output rebuild, historical-data migration, commit or push is authorized. Existing staged work is preserved. M232 commit-before-archive handling and the proposed per-Entity R/D/M/E cardinalities remain unresolved; this plan does not decide them.

## Pre-creation review

A read-only subagent reviewed each proposed Task and their pairwise boundaries. The bounded corrections identify M274 as the commit-before-archive authority (M232 is the replacement target), preserve Entity/Action/Process Subject target domains, and distinguish Journal records from the events they describe. No additional Operator decision was required. Task schema, unique identities, sequence, prerequisite references, and absence of cycles were checked before creation.
