---
subject_scopes:
  - relation-tooling
priority: high
version: 6
updated_at: "2026-09-09 21:56:59 +0400"
relations:
  concern_about:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-529--patch-artifact-relations
    - CA-R-877-REQUIREMENT-BSEED_GOVERNANCE--validate-directional-relational-atoms
    - CA-R-883-REQUIREMENT-BSEED_GOVERNANCE--register-contract-endpoint-relations
---
# Relation Tools do not resolve Scope Unit endpoints

The current executable relation registry and relation-processing code resolve active Markdown Artifact identities but do not resolve `.`, `./<FULL NAME>`, or `../<FULL NAME>` Scope Unit references as project-graph nodes relative to the source Atom's owner. They also do not parse or validate `relational_endpoints` descriptors and implement an earlier relation-metadata schema that lacks the registered relation family, ordering domain, target-position, and node-class fields required by the current Applicable Methodology.

Until the Tool realization is updated and evaluated, it cannot validate or patch the remaining Contract endpoint relations without producing false missing-target or incomplete-schema results.
