---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Evidence/Git reference validation"
  depends_on:
    - "Carrier"
    - "Artifact/Revision"
    - "Journal/Record"
version: 1
updated_at: "2026-09-16 17:31:26 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - "CA-D-448"
---
# Validate Git release evidence bindings

## Cases

1. encode one repository **and** the full commit object ID of the evaluated candidate.
2. supply a branch name, HEAD, **or** tag label **without** its resolved commit ID.
3. retain a tag label with its resolved commit ID, **then** move the tag **or** branch.
4. evaluate changed working-tree content **and** attempt **to** identify it **only** by the earlier commit ID.
5. inspect release references recorded through the existing Journal **and** proof-frontier Carriers.

## Acceptance

case 1 passes the exact-reference check. case 2 fails. case 3 retains the original immutable binding rather than following the changed label. case 4 fails the claimed committed-content binding **unless** the selected representation explicitly identifies the actual candidate differences. case 5 introduces no second authoritative release log **or** competing Journal schema.

## Failure disposition

identify the exact invalid binding **and** block reliance on that evidence. these cases authorize no commit, tag, merge, push, **or** release operation.
