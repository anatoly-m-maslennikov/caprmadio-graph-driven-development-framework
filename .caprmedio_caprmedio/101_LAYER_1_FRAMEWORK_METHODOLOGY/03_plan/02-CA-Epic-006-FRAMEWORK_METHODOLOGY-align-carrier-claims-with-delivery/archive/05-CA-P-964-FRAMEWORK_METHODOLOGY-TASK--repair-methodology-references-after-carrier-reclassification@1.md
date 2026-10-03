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
version: 1
updated_at: "2026-09-10 13:41:47 +0400"
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-963
---
# Repair methodology references after Carrier reclassification

the Assignee **must** reconcile active methodology references with the surviving authority produced by CA-P-962 **and** CA-P-963.

## Claim Scope

(references **in** active CORE_META_MODEL **or** LOCAL_CONFIGURATION Atoms whose targets **or** required interpretation changed under CA-P-962 **or** CA-P-963)

## Definition of Done

the Task is **not** Done **if** (an in-scope reference still resolves **to** a retired **or** wrong-role authority owner **or** a reference changes its meaning through a blind Identifier substitution **or** a required Evaluation target is lost **or** a new reference cycle **or** unresolved in-scope target is introduced **or** an out-of-scope affected consumer is omitted from the handoff).

## Details

consume the complete clause **and** identity mappings. repair exact typed references, Evaluation targets, applicable authority references, **and** active prose references **only** **where** the mapped authority requires a change. **if** a split creates multiple legitimate targets, **then** select the target set by the original consumer Claim rather than by filename similarity.

recheck Subject coverage **and** Carrier metadata of revised consumers. preserve exact prior Revisions for these changes. do **not** alter unchanged Claims **or** rewrite historical citations **and** Archives.

inspect incoming references from Project Atoms, other Plans, Tools, **and** generated Projections read-only. record exact affected paths **and** required follow-up **where** they are outside this Scope; do **not** silently expand the Epic **to** repair them. distinguish such downstream work from unresolved source-level references.
