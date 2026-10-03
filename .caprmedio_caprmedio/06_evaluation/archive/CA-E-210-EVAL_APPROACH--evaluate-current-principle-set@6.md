---
subject_scopes:
  - principles
tier: core
version: 6
updated_at: 2026-08-21 04:43:43
relations:
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
    - CA-M-002-PRINCIPLE-METHOD--dry_dont-repeat-yourself
    - CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable
  evaluation_for:
    - CA-INTENT
    - CAPRMEDIO-REQU-026--define-the-project-principle-universe
    - CA-R-820-REQUIREMENT-BSEED_SEMANTICS--expand-intent-through-principles
    - CA-R-821-REQUIREMENT-BSEED_GOVERNANCE--require-complete-intent-statement-principle-coverage
    - CA-R-822-REQUIREMENT-BSEED_SEMANTICS--allow-many-to-many-intent-principle-expansion
    - CA-R-823-REQUIREMENT-BSEED_SEMANTICS--exclude-intent-principle-expansion-from-dry-duplication
    - CA-R-824-REQUIREMENT-BSEED_SEMANTICS--align-intent-with-compiled-requirement-principles
    - CA-R-828-REQUIREMENT-BSEED_GOVERNANCE--validate-intent-against-compiled-requirement-principles
    - CA-R-829-REQUIREMENT-BSEED_SEMANTICS--keep-project-principles-as-authority-peers
    - CA-R-830-REQUIREMENT-BSEED_GOVERNANCE--reserve-principle-conflict-resolution-to-the-operator
    - CA-R-839-REQUIREMENT-BSEED_SEMANTICS--treat-principle-statements-as-one-meaning
    - CA-R-840-REQUIREMENT-BSEED_GOVERNANCE--place-human-readable-principle-statement-before-formal-statement
    - CA-R-854-REQUIREMENT-BSEED_SEMANTICS--distinguish-provided-outcome-and-operating-way-principles
    - CA-R-855-REQUIREMENT-BSEED_GOVERNANCE--validate-principle-content-role-semantics
---
# Evaluate the current Principle set

## Claim checked

Within the bounded universe of currently known project-wide invariants, the active Project Principle set is MECE, DRY, pairwise aligned, and collectively aligned with the active Intent.

## Applicable conditions

Apply after every governed change to the active Intent or Project Principle set and whenever either is reviewed.

## Check

Enumerate every currently known project-wide invariant, every independent statement in the active Intent, and every active Project Principle. Confirm that each known invariant has exactly one canonical Principle owner, no Principle meaning duplicates another owner, and every Principle is aligned with every other active Principle. Confirm that every independent Intent statement is expanded by at least one active Principle and that the compiled meaning of the active Principle set is semantically aligned with the active Intent. Treat faithful vertical expansion from Intent into Principles as permitted refinement rather than DRY duplication. For every Principle with a formal statement, confirm that its human-readable statement appears first and that both statements are semantically equivalent. Confirm that every Plan Principle states who may perform or authorize governed actions, every Requirement, Delivery, and Ops Principle states what CAPRMEDIO provides, and every Method and Evaluation Principle states how CAPRMEDIO works.

## Acceptance

Pass only when the current set is mutually exclusive, collectively exhaustive for the currently known invariant universe, free of duplicate semantic ownership, pairwise conflict-free, covers every independent Intent statement, is collectively aligned with the active Intent, every formal Principle statement faithfully re-expresses its preceding human-readable statement, and every Principle has the Content-role semantics governed for its role. Passing establishes conformance of the admitted Intent and current Principle set only; it does not establish Principle-set completeness or rule out an undiscovered invariant.

## Failure

Record every missing owner, uncovered Intent statement, Intent-Principle misalignment, statement-order failure, human/formal semantic mismatch, overlap, duplicate meaning, Content-role semantic mismatch, or conflict as a Concern. Route a conflict between active Project Principles to the Operator.
