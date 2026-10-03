---
subjects:
  governs: "Codex/User Hook/Carrier"
  depends_on: []
version: 10
updated_at: "2026-09-17 02:43:52 +0000"
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103

llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: evaluation
---
# Roll back an unavailable user Hook carrier

## Claim checked

An apply failure at the required Codex user Hook carrier does **not** expose a partially selected Tool release.

## Test case

Install one verified release, change the canonical Tool source so the next apply resolves another release, **and** make the configured Codex user home unavailable as a directory **before** applying again.

## Acceptance criteria

Apply fails with `host-hook-carrier-unavailable`. The current selection manifest **and** canonical Codex Hook fragment remain byte-for-byte equal **to** their pre-apply values, the previously selected release remains active, **and** existing user **and** project Hook carriers remain unchanged.

## Failure disposition

Reject the installer **if** the unavailable carrier selects the new release, changes a retained Hook carrier, hides the cause behind an unstable exception, **or** requires a repository backup for recovery.

## Post-selection failure coverage

retain the original unavailable-before-apply case **and** add a separate authorized fixture **in** which the Hook Carrier becomes unavailable **after** runtime selection changes **and** **before** required Hook registration completes. use isolated fixture Carriers; this Evaluation does **not** authorize changing the Operator's real home **or** host configuration.

- observe the post-selection fault **and** compare the retained selection manifest, canonical Hook fragment, Git Hook registration, activation marker, **and** service registry selection against their exact pre-apply values under CA-M-103.
- preserve unrelated user **and** Project Hook behavior. no partially selected runtime **or** false installation-success receipt **may** remain.
- retain the stable failure diagnostic **and** actual recovery evidence. an unavailable Carrier detected **before** selection does **not** prove this case.
- incomplete **or** unverified restoration fails the Evaluation; preserve its evidence **without** rewriting accepted Journal history.
