---
cce_version: cce_1
cce_form: method
subjects:
  governs: "release"
  depends_on:
    - "Journal/Record"
    - "Artifact/Revision"
version: 12
updated_at: "2026-09-17 20:09:12 +0000"
relations:
  method_for:
    - CA-R-1147
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Record one verified release outcome

## Applicable when

use this Method **after** one release attempt has a sealed factual outcome **and** attributable verification evidence.

## Procedure

1. seal one release-attempt identity with its attempted version, release revision **or** commit, manifest, verification results, Work Journal event, actor, **and** completion time.
2. determine success **only** from the declared release acceptance criteria **and** their attributable evidence.
3. for success, record the verified release success **in** one immutable Journal Record binding the version, exact revisions, checks, evidence, Journal, **and** canonical Git identity.
4. for a failed attempt established by its declared acceptance criteria **and** attributable evidence, record the failed non-release attempt **in** Journal Records that bind the same attempted version, exact revision, checks, **and** Work Journal event as the attempt **and** preserves the version as unreleased.
5. reject duplicate **or** conflicting outcomes for the same release-attempt identity.

## Outcome

a successful release has one immutable Journal Record of verified success; an evidenced failed attempt has explicitly bound Journal evidence of a failed non-release attempt **and** never becomes a release claim.

## Failure or stop

do **not** infer success from intent, partial checks, **or** an unsealed manifest; stop on missing evidence **or** conflicting release identity. missing verification **must not** be treated as evidence that the release attempt failed; retain the observed missing-evidence fact **without** inventing an outcome.
