---
atom_id: CA-P-962
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
    - CA-P-961
---
# Repair Core Meta-Model Carrier authority

the Assignee **must** apply the admitted CA-P-961 dispositions **to** Carrier-related authority **in** CORE_META_MODEL.

## Claim Scope

((active CORE_META_MODEL Atoms admitted for change by CA-P-961) **or** (their necessary successor Atoms) **or** (direct affected references **in** active RMED Atoms **in** (CORE_META_MODEL, LOCAL_CONFIGURATION) required for those replacements) **or** (exact prior Revision Archives of the changed Atoms))

## Definition of Done

the Task is **not** Done **if** ((an admitted Core disposition remains unapplied) **or** (a resulting Carrier specification has no D authority owner) **or** (a retained R contribution is lost) **or** (a retained M contribution is lost) **or** (a retained E contribution is lost) **or** (equivalent authority is independently duplicated) **or** (a changed Atom lacks required identity preservation) **or** (a changed Atom lacks required Revision preservation) **or** (a changed Atom lacks required Subject coverage) **or** (a changed Atom lacks its justified Local Tier) **or** (a required prior Archive is **not** byte-exact) **or** ((a predecessor is archived) **and** (an active RMED relation still requires that predecessor as its active target)) **or** ((a predecessor is archived) **and** ((a required out-of-scope repair lacks Operator approval) **or** (a required out-of-scope repair lacks verified completion)))).

## Details

refresh **and** compare source bytes against the disposition record **before** mutation. apply one admitted disposition at a time. reuse existing D authority; add a new D Atom **only** **when** a distinct Carrier contribution has no owner. preserve Current Scope ownership **and** intended Claim Scope.

preserve exact prior Revision Carriers **and** a complete old-to-new identity mapping. do **not** relabel an R Identifier as D. revise Subjects, Summary, CCE content, filename, **and** metadata together according **to** the current authority applicable **to** the result. retain the original Claim **where** its non-Carrier contribution remains necessary.

prepare each successor together with its mapped incoming-reference repairs. establish the successor, repair required active methodology references, **and** verify their targets **before** archiving the predecessor. preserve the prior Revisions of repaired consumers. do **not** defer a repair required for safe retirement **to** CA-P-964. that Task verifies completed repairs **and** performs remaining non-blocking reconciliation.

**if** an affected external consumer needs a repair outside this mutation Scope, **then** request the necessary Operator approval **and** keep the predecessor Active **until** that required repair is verified complete. a handoff entry alone does **not** satisfy this prerequisite. do **not** broaden this Task **to** edit Project authority, Tools, selected Settings, **or** generated Projections.

**after** **every** replacement, check its allocated clauses, active reference targets, **and** admitted Local Tier. record the completed reference repairs **and** remaining non-blocking items for CA-P-964. do **not** rewrite historical evidence **or** silently transfer Atoms between source owners.
