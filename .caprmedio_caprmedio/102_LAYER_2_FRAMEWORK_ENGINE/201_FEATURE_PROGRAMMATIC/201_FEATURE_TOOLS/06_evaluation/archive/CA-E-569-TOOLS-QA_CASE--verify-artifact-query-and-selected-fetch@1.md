---
atom_id: CA-E-569
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:00:00 +0400"
subjects:
  governs: FIND_AND_FETCH_ARTIFACTS
  depends_on: [Tool, Artifact, Markdown, Journal, Evaluation]
relations:
  evaluation_for: [CA-R-1849, CA-R-1850]
---
# Summary

Verify Artifact query and selected fetch

## Scope

Golden QA for
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/tests/test_find_and_fetch_artifacts.py`.

## Claim

The golden test **must** prove that FIND_AND_FETCH_ARTIFACTS returns only the
correct default IDs or explicitly selected fetch values from one stable
read-only snapshot, and truthfully rejects every unsupported or incomplete
case.

## Details

Fixture distinct frontmatter and section namespaces, equal spelling across them,
explicit null and absent fields, typed scalar values, every status, nested
heading paths, and several IDs. Assert CA-R-1850's precedence and parentheses
for `NOT`, `AND`, and `OR`; equality, inequality, and `IN`; no implicit Active narrowing;
selected-only fetch; bytewise ID ordering; bounded cursor continuation; and a
changed-snapshot cursor rejection. Independently exercise invalid grammar/type,
SQL/code-like input, missing ID, malformed frontmatter, duplicate key/heading,
incomplete read, inaccessible root, filename-only identity, secret-shaped
selection, and attempted mutation. Assert no accepted partial result, mutation,
secret value, fabricated Run/Event, or snapshot enlargement; if execution is
admitted, assert use of the shared RUN_SUPPORT Journal contract.
