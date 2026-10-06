---
subjects:
  - scope-topology
version: 3
updated_at: 2026-08-23 01:44:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-230--external-boundary-obligations
  child_of:
    - CAPRMEDIO-META-REQU-127--define-three-governance-loci
---
# Preserve external boundary obligations

An operator-accepted DDL, file schema, API, protocol, host format,
supported-platform interface, CI interface, dependency boundary, or comparable
external obligation is represented by its semantic contribution and external
Governance origin.

An obligation imposed by an identified external source occupies the Requirement
Content role, has external Governance origin, and pins the applicable external
source version or digest. Its graph connections are typed relations in Atom
frontmatter and do not create another Governance origin.

Implementation must conform to the exact committed obligation revision it consumes and cannot rewrite it. A changed external source creates a new committed revision when the same obligation remains identifiable. A different obligation requires a new Atom with an explicit replacement relation. Existing Implementations remain bound to their consumed revisions until lineage-impact review determines their disposition.

METAMODEL defines this boundary without assigning concrete external Type names.
GOVERNANCE owns their registered names, carriers, identities, and catalog
entries.

## Primary claim

External boundary obligations use the Requirement Content role, preserve their
pinned source revision and Governance origin, and cannot be rewritten by their
Implementations.
