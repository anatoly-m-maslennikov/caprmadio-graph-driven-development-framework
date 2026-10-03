---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "extension-lifecycle"
  depends_on: []
version: 7
updated_at: "2026-09-17 02:43:52 +0000"
relations:
  evaluation_for:
    - CA-M-252
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify manage installed Extensions

## Claim checked

CA-M-252 applies one exact Extension lifecycle transition atomically **and** reports its resulting installed state, **or** restores the prior state completely.

## Applicable when

Apply whenever exact Extension source **or** version resolution, installed-state planning, lifecycle effects, **or** rollback handling changes.

## Test case

Use one bounded Extension lifecycle trace: install an exact package into an empty inventory, update it **to** a second exact source **and** version, downgrade it **to** the first exact source **and** version, uninstall it, **then** attempt one transition containing a deliberately failing file effect.

## Acceptance criteria

Install, update, downgrade, **and** uninstall each produce exactly the planned identity, source, version, file inventory, **and** verification status. The failing transition restores the complete prior installed state **and** reports rollback evidence.

## Failure disposition

Reject the realization **and** preserve initial inventory, transition plan, source **and** version resolution, final inventories, failed effect, **and** rollback evidence.

## Post-effect failure coverage

execute the failing transition from a recorded prior installed state. inject its fault **after** **>=1** planned file **or** installed-state effect is applied **and** **before** final verification succeeds. for a single atomic publication, inject **after** publication; a rejected plan **or** unavailable package **before** apply does **not** prove rollback.

- compare the complete prior **and** restored installed state: exact identity, source, version, selected inventory, **and** owned Carrier bytes.
- verify that the failed transition leaves no partially selected Extension **or** unplanned file effect, reports failure rather than successful installation, **and** preserves actual recovery evidence.
- preserve unrelated Carriers **and** accepted Journal history. immutable evidence of the attempted transition is **not** installed-state residue **to** erase.
- fail the Evaluation **if** restoration is incomplete, unverified, **or** reported as complete solely because the failing effect itself was rejected.
