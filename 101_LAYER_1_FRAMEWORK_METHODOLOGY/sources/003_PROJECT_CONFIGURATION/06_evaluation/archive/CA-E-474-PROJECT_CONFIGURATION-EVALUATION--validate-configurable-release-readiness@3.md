---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Release Readiness"
  depends_on:
    - "Step"
    - "Refresh Required Release Projections"
    - "Assess Release Readiness"
    - "Implementation Workflow"
    - "Operator"
    - "Projection"
    - "Journal/Record"
    - "Artifact/Revision"
    - "Project"
    - "Version"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Evaluation"
version: 3
updated_at: "2026-09-18 14:16:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - "CA-O-025"
    - "CA-O-026"
    - "CA-O-027"
    - "CAPRMEDIO-META-REQU-102"
    - "CAPRMEDIO-GOV-REQU-353"
---
# Validate configurable release readiness

## Cases

1. use a Project with no selected release-readiness Workflow; execute its admitted implementation mode under CA-O-016.
2. select CA-O-025 for a candidate with complete passing current evidence **and** required approvals; contrast it with failed, blocked, missing, **or** stale required checks.
3. provide one required stale Projection **and** one enabled but unrequired Projection. repeat with already-current required output, a source conflict, failed refresh, **and** a changed source Revision.
4. change a material candidate input **after** Evaluation. separately change an unrelated Artifact **without** changing the evaluated dependency set **or** an additional invalidation condition.
5. approve a source correction, **then** complete it. separately omit approval **or** exhaust the accepted revisit allowance.
6. complete readiness **without** executing the configured release event; compare with a successful authorized release recorded **in** the shared Journal.
7. use a non-Git candidate binding satisfying the selected gates. inspect the selected Workflow's Step bindings **and** its dependency on the existing Core implementation flow.

## Acceptance

- case 1 requires no universal development **or** release-readiness setting.
- readiness succeeds **only** for the exact candidate with complete passing current checks **and** satisfied approvals.
- refresh is limited **to** the selected required set **and** existing Projection contracts; source conflicts are **not** repaired **in** generated copies.
- changed material inputs block reuse of affected evidence; unrelated changes alone do **not** invalidate it. historical evidence is unchanged.
- approved source changes require affected implementation work under CA-O-016 **before** another authorized readiness attempt. absent approval **or** exhausted allowance blocks continuation; no silent budget reset occurs.
- readiness alone does **not** freeze a Version. successful release produces a factual Journal Record, **not** a new Operations Atom.
- Workflow nodes are Steps, **every** Step references **`=1`** Action with its parameters **and** inputs, the implementation loop is **not** duplicated, **and** non-Git Projects require no Git mechanics.

## Failure disposition

report the failing source Revision, case, expected result, **and** observed result. do **not** execute release side effects **or** change source authority **to** make a fixture pass.
