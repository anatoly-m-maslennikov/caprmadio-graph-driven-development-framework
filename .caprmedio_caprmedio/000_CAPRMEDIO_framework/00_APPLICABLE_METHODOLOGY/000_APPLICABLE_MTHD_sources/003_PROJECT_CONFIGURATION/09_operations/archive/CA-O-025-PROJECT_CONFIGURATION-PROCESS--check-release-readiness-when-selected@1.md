---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Release Readiness"
  depends_on:
    - "Process"
    - "Action"
    - "Operator"
    - "Implementation Process"
    - "Select Reconciliation Sources"
    - "Assess Source Conflicts"
    - "Propose Source Corrections"
    - "Obtain Source Correction Decision"
    - "Apply Approved Source Corrections"
    - "Refresh Required Release Projections"
    - "Implementation Evaluation"
    - "Assess Release Readiness"
    - "Implementation Retry Control"
    - "Artifact/Revision"
    - "Journal/Record"
    - "Project Configuration"
    - "Atom"
    - "Projection"
    - "Atom/Content Role: Evaluation"
    - "Version"
    - "Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-16 17:31:26 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - "CA-O-016"
    - "CA-O-004"
    - "CA-O-005"
    - "CA-O-006"
    - "CA-O-007"
    - "CA-O-008"
    - "CA-O-020"
    - "CA-O-024"
    - "CA-O-026"
    - "CA-O-027"
    - "CAPRMEDIO-META-REQU-102"
    - "CAPRMEDIO-GOV-REQU-353"
---
# Check release readiness when selected

Release Readiness **means** the configurable Process used by this Project **when** the Operator **or** applicable Project Configuration selects a release-readiness check. selection supplies the candidate, the release boundary, required Projections, applicable Evaluations, approval gates, **and** accepted retry limits. missing **or** conflicting selections block execution rather than creating implicit defaults.

## Entry conditions

1. use CA-O-016 for development **and** Implementation repair; do **not** duplicate its implementation loop here.
2. begin this Process **after** the selected candidate's implementation work has completed under CA-O-016 **or** its applicable completion evidence has been validated.
3. use the following Action nodes. the Process does **not** add Process nodes **or** require **every** Project **to** select this release flow.

## Flow

| Node **and** Action | Result condition | Next node **or** outcome |
|---|---|---|
| select — CA-O-004 | complete exact candidate source selection | assess |
| assess — CA-O-005 | required checks complete; no unresolved conflict | refresh |
| assess — CA-O-005 | conflict with an authorized correction route | propose |
| propose — CA-O-006 | supported exact proposal | decide |
| decide — CA-O-007 | current explicit approval for a source correction | correct |
| decide — CA-O-007 | current explicit disposition requiring no correction | select, subject **to** the accepted revisit allowance |
| correct — CA-O-008 | correction completed | stop this readiness attempt; use CA-O-016 for affected implementation work **before** an authorized new readiness attempt |
| refresh — CA-O-026 | required Projections current for the selected sources | evaluate |
| evaluate — CA-O-020 | **all** selected applicable Evaluations passed for this candidate | gate |
| evaluate — CA-O-020 | failed, blocked, **or** unevaluated required check | stop; CA-O-016 owns implementation repair **and** CA-O-024 controls its retry accounting |
| gate — CA-O-027 | current complete evidence **and** required approvals | report this candidate ready; stop |
| gate — CA-O-027 | changed inputs, missing evidence, **or** unmet approval | report the blocker; do **not** report readiness |
| **any** node | failed work, unresolved confidence **or** permission gate, rejected decision, **or** unavailable retry allowance | stop **and** escalate with actual results |

## Execution boundaries

- reassessment **or** a new candidate does **not** silently reset a retry budget. **every** autonomous revisit requires an applicable accepted allowance; missing **or** exhausted allowance requires Operator disposition.
- source corrections use CA-O-008's governed revision **or** replacement workflow. projected content **must not** become the correction target.
- optional Atom consolidation is a separately authorized source change, **not** a mandatory release step.
- record actual execution outcomes **in** the shared Journal. successful readiness is **not** release execution **and** does **not** freeze a Version under CAPRMEDIO-META-REQU-102.
- this Process selects no Git branch, commit, tag, merge, publication, **or** universal Framework Instance workflow setting.
