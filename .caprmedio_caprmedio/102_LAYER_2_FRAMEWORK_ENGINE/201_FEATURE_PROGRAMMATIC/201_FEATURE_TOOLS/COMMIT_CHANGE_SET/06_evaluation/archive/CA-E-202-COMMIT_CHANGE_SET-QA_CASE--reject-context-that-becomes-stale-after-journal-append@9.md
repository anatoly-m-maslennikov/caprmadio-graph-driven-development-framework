---
subjects:
  governs: "Commit Context"
  depends_on:
    - "Tool/COMMIT_CHANGE_SET"
    - "Journal/Record"
    - "Artifact/Carrier"
    - "Project"
version: 9
updated_at: "2026-09-17 03:51:29 +0000"
relations: {"evaluation_for":["CA-M-087","CA-R-805","CA-R-812","CA-R-802","CA-R-1385","CA-R-1491"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: evaluation
---
# Reject context that becomes stale after Journal append

## Claim checked

the Git Doer rejects a sealed action whose expected Git base **or** subject frontier changed **before** its Git effect, even **when** its historical Journal observation was already appended.

## Test case

1. prepare **=1** admitted sealed `UPDATE` action with its Initiative, exact targets, expected Git base, subject frontier, **and** outbox identity. append its intact historical Journal observation **and** retain the exact accepted record as evidence.
2. change the expected Git base **or** a sealed subject-frontier digest **after** the Journal append. capture the new state **before** the Git Doer is invoked.
3. submit the selected outbox item **to** COMMIT_CHANGE_SET under its current independently admitted envelope **and** Git-gate lease. the prior append is the setup of this case, **not** an admission prerequisite, receipt authorization, **or** permission **to** omit Git revalidation.

## Acceptance criteria

- the Doer returns a deterministic stale-context diagnostic **before** staging its own targets **or** creating a Commit.
- preserve the complete current index, observed later Project state, **and** accepted Journal records. do **not** erase, duplicate, reseal, **or** rebind the historical observation **to** the later Project state.
- preserve the failed item's stable identity, actual lease/fencing outcome, blocking reason, **and** durable outbox state for admitted reconciliation. do **not** silently refresh the sealed action, discard pending work, **or** report success.
- retry requires resolution of the failed precondition **and** current authority under CA-R-1385; a stale **or** expired lease grants no Git effect. an uncertain earlier effect requires reconciliation **before** replay under CA-R-805.
- **every** later Git action still passes through the same gate **and** its own current admission checks. this blocked item does **not** establish a new universal FIFO rule **or** block independent non-Git intake, context, **or** Journal work under CA-R-802.

## Failure disposition

reject the Doer **if** it stages **or** commits the rejected target state, absorbs **or** overwrites unrelated changes, loses **or** alters accepted history, invents a fresh successful action from stale input, **or** bypasses the common Git gate **or** unresolved applicable guards.
