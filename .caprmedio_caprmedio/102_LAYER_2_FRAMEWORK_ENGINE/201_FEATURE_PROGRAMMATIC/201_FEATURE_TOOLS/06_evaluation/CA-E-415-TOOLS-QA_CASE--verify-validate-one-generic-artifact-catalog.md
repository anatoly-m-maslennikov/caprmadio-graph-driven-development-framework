---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Validate Artifact Catalog"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Revision"
    - "Projection"
version: 7
updated_at: "2026-09-17 22:44:34 +0000"
relations: {"evaluation_for":["CA-R-1142","CA-O-034"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify validate one generic Artifact catalog

## Claim checked

CA-O-034 fails closed **and** separately identifies **every** missing, stale, duplicate, unknown **and** inconsistent catalog entry against declared authority.

## Applicable when

apply **when** generic catalog comparison **or** discrepancy classification changes.

## Test cases

- establish a valid catalog baseline with its registered definition **and** exact declared authority frontier. verify its expected entries, ordering **and** source facts independently of the validator being checked.
- create separate invalid variants for a missing entry, stale source facts, a duplicate entry, an unknown entry **and** inconsistent entry data. identify the exact changed entry **or** absence **and** expected discrepancy for **every** variant; keep unrelated baseline facts unchanged.
- validate the baseline **and** **every** invalid variant, **then** repeat against unchanged inputs. compare the catalog **and** **all** authority Carriers **before** **and** **after** **every** validation.

## Acceptance criteria

- the valid baseline passes **without** invented discrepancies.
- **every** invalid variant fails **and** identifies its expected discrepancy with attributable entry, expected authority contribution **and** observed frontier evidence. no defect is hidden by another variant **or** accepted because a total finding count happened **to** match.
- **if** a combined variant is also used, establish its complete expected discrepancy set explicitly; do **not** assume the five classes are mutually exclusive for arbitrary defective entries.
- repeated unchanged inputs produce the same classified findings. no catalog **or** authority Carrier changes during validation.

## Failure disposition

reject missing, invented, unattributed **or** nondeterministic findings, false acceptance, **or** mutation. preserve the catalog definition, baseline, authority frontier, separate variants, expected **and** actual findings, **and** no-mutation evidence.
