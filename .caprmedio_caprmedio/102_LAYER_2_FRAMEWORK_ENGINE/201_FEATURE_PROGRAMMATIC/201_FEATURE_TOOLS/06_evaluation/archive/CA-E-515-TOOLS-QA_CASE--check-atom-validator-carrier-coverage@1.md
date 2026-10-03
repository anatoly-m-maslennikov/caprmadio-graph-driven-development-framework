---
atom_id: CA-E-515
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/VALIDATE_ATOMS"
  depends_on:
    - "Tool"
    - "Atom/Property"
    - "Atom/Frontmatter"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Relation"
    - "Evaluation"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  evaluation_for:
    - CA-M-316
    - CA-R-1622
  relates_to:
    - CA-E-506
    - CA-O-082
---
# Summary

Check Atom validator carrier coverage

## Claim

the `VALIDATE_ATOMS` carrier coverage check **must** demonstrate faithful execution of applicable mechanical rules **without** replacing semantic review.

- exercise the valid **and** invalid fixtures governed by CA-E-506, including explicit internal Properties, Draft identity exceptions, role-specific Statuses, body sections, fenced headings, duplicate YAML keys, unknown fields, missing values, **and** independently stored inverse Relations.
- add admitted extension Properties **and** previously unknown Scope Unit names: accept them **when** their applicable authority is supported; reject unsupported assumptions rather than hard-code Project contents.
- remove a Property while retaining its filename token **or** expected folder: require a missing-internal-value finding. conflicting outward representations remain separate findings.
- break **=1** candidate's YAML: require its failure **and** continued independent coverage, **not** omission. exclude a candidate explicitly: require its exclusion reason **and** accurate coverage.
- provide an unsupported governing rule **or** unresolved external reference context: require incomplete coverage, never a false pass.
- a mechanically valid multi-Claim Atom **must not** be labeled semantically approved by this Tool.
