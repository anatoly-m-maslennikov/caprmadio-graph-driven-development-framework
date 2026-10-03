---
cce_version: cce_1
cce_form: method
subjects:
  governs: "release"
  depends_on: []
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
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

Use this Method after one release attempt has a sealed factual outcome and attributable verification evidence.

## Procedure

1. Seal one release-attempt identity with its attempted version, release revision or commit, manifest, verification results, Work Journal event, actor, and completion time.
2. Determine success only from the declared release acceptance criteria and their attributable evidence.
3. For success, create one immutable Operations Release Record binding the version, exact revisions, checks, evidence, Journal, and canonical Git identity.
4. For failure, create non-release Operations evidence that binds the same attempted version, exact revision, checks, and Work Journal event as the attempt and preserves the version as unreleased.
5. Reject duplicate or conflicting outcomes for the same release-attempt identity.

## Outcome

A successful release has one immutable Release Record; an unsuccessful attempt has explicitly bound non-release Operations evidence and never becomes a release claim.

## Failure or stop

Do not infer success from intent, partial checks, or an unsealed manifest; stop on missing evidence or conflicting release identity.
