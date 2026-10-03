---
atom_id: CA-P-964
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    occurrent:
      - Atom/Content Role
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Claim/Scope
      - Carrier
      - Atom/Local Tier
      - Atom/Revision
      - Autonomous Confidence Threshold
version: 2
updated_at: "2026-09-10 17:35:45 +0400"
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-963
---
# Repair methodology references after Carrier reclassification

the Assignee **must** reconcile active methodology references with the surviving authority produced by CA-P-962 **and** CA-P-963.

## Claim Scope

(references **in** active RMED Atoms **in** (CORE_META_MODEL, LOCAL_CONFIGURATION) whose targets **or** required interpretation changed under CA-P-962 **or** CA-P-963)

## Definition of Done

the Task is **not** Done **if** ((an in-scope reference still targets a retired authority owner **where** an active target is required) **or** (an in-scope reference targets the wrong authority contribution) **or** (a reference changes its meaning through a blind Identifier substitution) **or** (a required Evaluation target is lost) **or** (a new reference cycle is introduced) **or** (a new unresolved in-scope target is introduced) **or** (a required pre-retirement repair was deferred **to** this Task) **or** (an out-of-scope affected consumer is omitted from the handoff)).

## Details

consume the complete clause **and** identity mappings **and** the reference-repair evidence from CA-P-962 **and** CA-P-963. verify that required incoming-reference repairs preceded predecessor retirement. this Task is a final verification **and** remaining non-blocking reconciliation pass, **not** the first repair step for references required **to** keep active authority valid. **if** that ordering was violated, **then** fail the corresponding replacement check rather than silently accepting the broken intermediate state.

reconcile remaining exact typed references, Evaluation targets, applicable authority references, **and** active prose references **only** **where** the mapped authority requires a change. **if** a split creates multiple legitimate targets, **then** select the target set by the original consumer Claim rather than by filename similarity.

recheck Subject coverage **and** Carrier metadata of revised consumers. preserve exact prior Revisions for these changes. do **not** alter unchanged Claims **or** rewrite historical citations **and** Archives.

inspect incoming references from Project Atoms, other Plans, Tools, **and** generated Projections read-only. record exact affected paths **and** required follow-up **where** they are outside this Scope; do **not** silently expand the Epic **to** repair them. distinguish non-blocking downstream work from an external repair required **before** retirement. the latter **must** already have been approved **and** verified complete **before** the affected replacement can pass.
