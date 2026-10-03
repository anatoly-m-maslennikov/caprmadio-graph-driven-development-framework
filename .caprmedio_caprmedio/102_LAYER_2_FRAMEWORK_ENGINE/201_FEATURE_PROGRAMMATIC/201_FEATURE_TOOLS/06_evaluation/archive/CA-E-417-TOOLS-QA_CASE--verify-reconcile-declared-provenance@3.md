---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "provenance"
  depends_on: []
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-251
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify reconcile declared provenance

## Claim checked

CA-M-251 read-only classifies declared provenance links as current, missing, conflicting, stale, or unverifiable without inferring repair or adoption.

## Applicable when

Apply whenever declared-provenance comparison or finding classification changes.

## Test case

Select Artifacts whose declared source, draft, session, revision, and digest links together contain one current, missing, conflicting, stale, and unverifiable case. Reconcile them and compare all selected carriers before and after.

## Acceptance criteria

The result assigns each case exactly its corresponding classification with attributable source evidence. No selected Artifact changes, no link is repaired, and no adoption decision is created.

## Failure disposition

Reject the realization and preserve selected carriers, declared links, observed targets, classifications, before-and-after digests, and no-mutation proof.
