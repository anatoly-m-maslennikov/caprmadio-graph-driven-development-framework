---
atom_id: CA-P-963
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
    - CA-P-962
---
# Repair Local Configuration Carrier authority

the Assignee **must** apply the admitted CA-P-961 dispositions **to** Carrier-related authority **in** LOCAL_CONFIGURATION as expansions of the repaired Core Meta-Model.

## Claim Scope

((active LOCAL_CONFIGURATION Atoms admitted for change by CA-P-961) **or** (their necessary successor Atoms) **or** (direct affected references **in** active RMED Atoms **in** (CORE_META_MODEL, LOCAL_CONFIGURATION) required for those replacements) **or** (exact prior Revision Archives of the changed Atoms))

## Definition of Done

the Task is **not** Done **if** ((an admitted Local disposition remains unapplied) **or** (a Carrier specification has no D authority owner) **or** (a Local Claim rewrites Core authority) **or** (a Local Claim independently duplicates Core authority) **or** (a Type-admission contribution is lost during token extraction) **or** (a current selected configuration value is silently removed) **or** (a current selected configuration value is silently moved) **or** (a current selected configuration value is silently converted into a default) **or** (a required prior Archive is **not** byte-exact) **or** ((a predecessor is archived) **and** (an active RMED relation still requires that predecessor as its active target)) **or** ((a predecessor is archived) **and** ((a required out-of-scope repair lacks Operator approval) **or** (a required out-of-scope repair lacks verified completion)))).

## Details

consume the completed CA-P-962 mapping **and** refresh the Local source inventory. keep Project-specific Type admissions **and** their allowed variation boundaries separate from D Carrier-prefix, token, YAML, TOML, **and** record-format specifications.

preserve the distinction between a configurable Property, its admitted values, its Carrier encoding, **and** the currently selected value. this Task does **not** resolve R1224, R1225, **or** R1227 selections by editing Framework Instance Settings; **if** a proposed disposition depends on those unresolved decisions, **then** ask the Operator **before** changing it.

apply one admitted disposition at a time, preserving exact prior Revisions, Claim allocations, source ownership, intended Scope, meaningful Local Tier, Subjects, **and** old-to-new identity mappings. reuse the Core D owner **where** it is already sufficient; do **not** copy that authority into Local Configuration.

prepare each successor together with its mapped incoming-reference repairs. establish the successor, repair required active methodology references, **and** verify their targets **before** archiving the predecessor. preserve the prior Revisions of repaired consumers. do **not** defer a repair required for safe retirement **to** CA-P-964.

**if** an affected external consumer needs a repair outside this mutation Scope, **then** request the necessary Operator approval **and** keep the predecessor Active **until** that required repair is verified complete. a handoff entry alone does **not** satisfy this prerequisite. record completed reference repairs **and** remaining non-blocking reconciliation for CA-P-964. do **not** edit external consumers, install Extensions, change selected Settings, **or** regenerate projections within this Task.
