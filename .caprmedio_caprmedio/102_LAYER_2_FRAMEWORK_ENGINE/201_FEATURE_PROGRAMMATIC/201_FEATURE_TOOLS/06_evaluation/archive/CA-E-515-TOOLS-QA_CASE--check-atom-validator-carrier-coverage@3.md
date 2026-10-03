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
version: 3
updated_at: "2026-09-23 23:59:15 +0000"
relations:
  evaluation_for:
    - CA-M-316
    - CA-R-1622
  relates_to:
    - CA-E-506
    - CA-O-087
---
# Summary

Check Atom validator carrier coverage

## Claim

the `VALIDATE_ATOMS` carrier coverage check **must** demonstrate faithful execution of applicable mechanical rules through end-to-end tests using mock Atom Carriers **without** replacing semantic review.

- exercise the valid **and** invalid fixtures governed by CA-E-506, including explicit internal Properties, Draft identity exceptions, role-specific Statuses, body sections, fenced headings, duplicate YAML keys, unknown fields, missing values, **and** independently stored inverse Relations.
- add admitted extension Properties **and** previously unknown Scope Unit names: accept them **when** their applicable authority is supported; reject unsupported assumptions rather than hard-code Project contents.
- remove a Property while retaining its filename token **or** expected folder: require a missing-internal-value finding. conflicting outward representations remain separate findings.
- break **=1** candidate's YAML: require its failure **and** continued independent coverage, **not** omission. exclude a candidate explicitly: require its exclusion reason **and** accurate coverage.
- provide an unsupported governing rule **or** unresolved external reference context: require incomplete coverage, never a false pass.
- a mechanically valid multi-Claim Atom **must not** be labeled semantically approved by this Tool.
- invoke the real delivered command against isolated fixture Projects through its public JSON request/result interface. mock the input Atoms, reference context, **and** selected external boundaries, **not** the validator, rule checks, Relation resolution, **or** returned findings.
- maintain a coverage matrix from **every** applicable machine-checkable rule **and** declared failure class **to** positive **and** negative cases. include boundaries **and** admitted exceptions; an unmapped rule, unsupported check, **or** skipped case is a visible gap, **not** proof of complete coverage.
- include good Atoms, bad Atoms with individual defects, Atoms with multiple independent defects, **and** mixed batches. require clean results for good Atoms **and** **all** expected mechanically detectable errors for bad Atoms, even **when** another Atom failed earlier.
- compare exact expected finding sets, including check code, Atom/Carrier, Property/section, severity, **and** authority binding; reject missing findings, duplicate findings, false positives, wrong targets, **and** wrong failure reasons. verify aggregate result, per-Atom results, coverage, **and** process exit code.
- preserve the distinction between failed checks **and** checks blocked by malformed input **or** missing prerequisites. a blocked check is explicitly not checked; do **not** invent downstream findings **or** count it as passed.
- derive reviewed expectations from the governing Atoms, **not** from the current Tool output. automatic acceptance of generated expected results is **not** test validation. changing authority requires reviewing its fixtures **and** expected results.
- a missing executable, unexecuted end-to-end suite, **or** substituted mock validator **must** fail the completion gate rather than produce a passing **or** silently skipped suite.
