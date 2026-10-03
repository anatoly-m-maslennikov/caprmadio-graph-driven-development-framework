---
subject_scopes:
  - relation-model
version: 2
updated_at: 2026-08-22 01:51:09
relations:
  child_of:
    - CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable
    - CA-E-206-EVAL_APPROACH--require-usable-inputs-for-reliance
  evaluation_for:
    - CA-R-877-REQUIREMENT-BSEED_GOVERNANCE--validate-directional-relational-atoms
    - CA-R-882-REQUIREMENT-BSEED_GOVERNANCE--encode-relational-semantic-shape
    - CA-R-883-REQUIREMENT-BSEED_GOVERNANCE--register-contract-endpoint-relations
---
# Validate a directional Contract Atom

## Claim checked

An active Contract-family Atom has one ordinary Content role and role-local Type, declares relational shape, identifies exactly one controlling endpoint and at least one controlled endpoint, and is owned by the narrowest enabled common Structural scope containing its endpoints.

## Test case

Construct one valid relational Requirement with `semantic_shape: relational`, one `relational_endpoints.controller` descriptor, two `relational_endpoints.followers` descriptors, exact full Scope Unit names, registered Content roles, and one separately registered flow relation. Then independently remove relational shape, remove or duplicate the controller, mismatch the controller role with the Atom role, remove every follower, omit a follower's roles, use a short Scope Unit prefix, substitute an unknown or inactive endpoint, select a Type outside the Requirement role, add the retired `contract_for` or `controls_endpoint` relation, and place the carrier outside its narrowest enabled common scope.

## Acceptance criteria

The valid fixture passes. Every invalid fixture fails and identifies the exact missing, duplicate, abbreviated, inactive, unknown, role-inconsistent, Type-inconsistent, retired, or incorrectly owned element. The validator does not infer a Contract from cross-unit placement or from a flow relation alone.

## Failure disposition

Record a Concern naming the invalid Contract carrier and stop Contract acceptance for that carrier.
