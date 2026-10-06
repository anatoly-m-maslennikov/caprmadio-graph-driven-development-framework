---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Release Readiness"
  depends_on:
    - "Workflow/Relation Kind: On Result"
    - "Step Run"
    - "Workflow Run"
    - "Step"
    - "Workflow"
    - "Action"
    - "Operator"
    - "Implementation Workflow"
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
version: 2
updated_at: "2026-09-18 14:16:20 +0000"
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

Release Readiness **means** the configurable Workflow used by this Project **when** the Operator **or** applicable Project Configuration selects a release-readiness check. selection supplies the candidate, the release boundary, required Projections, applicable Evaluations, approval gates, **and** accepted retry limits. missing **or** conflicting selections block execution rather than creating implicit defaults.

## Entry conditions

1. use CA-O-016 for development **and** Implementation repair; do **not** duplicate its implementation loop here.
2. begin this Workflow **after** the selected candidate's implementation work has completed under CA-O-016 **or** its applicable completion evidence has been validated.
3. use the following Steps. the Workflow does **not** make another Workflow a Step **or** require **every** Project **to** select this release flow.

the entry Step is select. interpret Step bindings **and** run boundaries under CA-R-1509, CA-R-1510, **and** CA-R-1511.

## Steps

| Step | Action reference | Parameters **and** inputs |
|---|---|---|
| select | CA-O-004 | the selected release candidate, release boundary, **and** governing source selection |
| assess | CA-O-005 | the selected frontier **and** required release checks |
| propose | CA-O-006 | identified source conflicts **and** the authorized correction route |
| decide | CA-O-007 | the exact correction proposal, frontier, **and** required approval context |
| correct | CA-O-008 | the exact approved source correction **and** current frontier |
| refresh | CA-O-026 | the candidate **and** its selected required Projections |
| evaluate | CA-O-020 | the exact candidate **and** selected applicable Evaluations |
| gate | CA-O-027 | the exact candidate, checked results, required evidence, **and** approvals |

## Transitions

the transitions below use the Workflow-scoped ON_RESULT Relation under CA-R-1513 **when** the destination is a Step. a terminal outcome ends the Workflow Run; it is **not** another Step **or** Action.

| Step **and** Action | Result condition | Next Step **or** outcome |
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
| **any** Step | failed work, unresolved confidence **or** permission gate, rejected decision, **or** unavailable retry allowance | stop **and** escalate with actual results |

## Execution boundaries

- reassessment **or** a new candidate does **not** silently reset a retry budget. **every** autonomous revisit requires an applicable accepted allowance; missing **or** exhausted allowance requires Operator disposition.
- source corrections use CA-O-008's governed revision **or** replacement workflow. projected content **must not** become the correction target.
- optional Atom consolidation is a separately authorized source change, **not** a mandatory release step.
- record actual execution outcomes **in** the shared Journal. successful readiness is **not** release execution **and** does **not** freeze a Version under CAPRMEDIO-META-REQU-102.
- this Workflow selects no Git branch, commit, tag, merge, publication, **or** universal Framework Instance workflow setting.
