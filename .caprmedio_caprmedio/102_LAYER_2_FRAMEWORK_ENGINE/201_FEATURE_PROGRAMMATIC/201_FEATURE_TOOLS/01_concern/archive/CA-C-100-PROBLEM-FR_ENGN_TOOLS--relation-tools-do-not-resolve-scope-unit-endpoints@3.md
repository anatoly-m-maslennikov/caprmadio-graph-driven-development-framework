---
subject_scopes:
  - relation-tooling
priority: high
version: 3
updated_at: 2026-08-22 01:51:09
relations:
  concern_about:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-529--patch-artifact-relations
    - CA-R-877-REQUIREMENT-BSEED_GOVERNANCE--validate-directional-relational-atoms
    - CA-R-883-REQUIREMENT-BSEED_GOVERNANCE--register-contract-endpoint-relations
    - CA-R-885-REQUIREMENT-BSEED_GOVERNANCE--register-forward-dependency-relation-kind
---
# Relation Tools do not resolve Scope Unit endpoints

The current executable relation registry and relation-processing code resolve active Markdown Artifact identities but do not resolve `.`, `./<FULL NAME>`, or `../<FULL NAME>` Scope Unit references as project-graph nodes relative to the source Atom's owner. They also do not parse or validate `relational_endpoints` descriptors and implement an earlier relation-metadata schema that lacks the registered relation family, ordering domain, target-position, and node-class fields required by current GOVERNANCE.

Until the Tool realization is updated and evaluated, it cannot validate or patch the new Contract endpoint and Scope Unit dependency relations without producing false missing-target or incomplete-schema results.
