---
subjects:
  declared:
    continuant:
      - language
    occurrent:
      - evaluation
  prerequisite:
    continuant:
      - artifact-model
      - cce-language
cce_version: cce_1
cce_form: evaluation
version: 4
updated_at: 2026-08-25 01:29:15
relations: {}
---
# Validate composite Claims and derived Summaries

## Claim checked

every active or draft Atom contains one semantically irreducible CCE Claim and one concise source-faithful Summary derived from the Claim and Claim Scope.

## Test case

create one-clause Claims and explicitly grouped composite Claims whose components must be accepted, replaced, and retired together. include this Claim: **if** an Atom has Content Role **in** Spec Content Roles, **then** its Status **must** be **in** (Draft, Active, Archived). assign its Claim Scope as all Atoms where Content Role is in Spec Content Roles, assign `Atom/Content Role/Spec Content Roles/Status` as its GOVERNS Subject Path, assign `Atom/Content Role/Spec Content Roles` as its DEPENDS_ON Subject Path, and derive `Allowed Statuses for Spec Content Role Atoms` as its Summary, `allowed-statuses-for-spec-content-role-atoms` as its filename Summary slug, and `Allowed Statuses for Spec Content Role Atoms` as its H1. derive every Projection twice. then introduce an independently replaceable component, ambiguous grouping, an added or broadened Summary meaning, reconstruction of the Claim from the Summary, and a Translation derived from the Summary.

## Acceptance criteria

every valid fixture has one precise Claim interpretation, one Claim Scope set, the same reproducible Summary, filename Summary slug, H1, and source-faithful Translation. every invalid fixture fails with the violated Claim boundary, grouping, Scope, Summary, or Translation rule identified.

## Failure disposition

record a Concern naming the affected Claim, Claim Scope, Summary, or derived Projection.
