---
atom_id: CA-R-1839
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:13:12 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY"
  depends_on: [Tool, Workflow, Step, Action, Methodology Source, Extension, Project Configuration, Atom Revision, Projection]
relations:
  relates_to: [CA-O-011, CA-O-152, CA-O-004, CA-M-226]
---
# Summary

Select the complete active Applicable Methodology source frontier without excluding activated installed Extensions.

## Scope

The source-selection boundary of the native `COMPILE_APPLICABLE_METHODOLOGY` Tool for one CA-O-011 Applicable Methodology Workflow Run.

## Claim

`COMPILE_APPLICABLE_METHODOLOGY` **must** discover and retain the complete current eligible frontier: Active CORE_META_MODEL sources, every activated installed Extension at its Framework-Settings-selected Revision, and Active PROJECT_CONFIGURATION sources.

## Details

The request binds the Project root, current Project Structure, Framework Instance Settings, requested projection target, and the current source-root declaration. The Tool obtains layer membership and activated Extension identities/Revisions from those governed inputs; it does not hardcode Extension names, require an Extension collection Carrier, or require `002_INSTALLED_EXTENSIONS` to be empty. An empty activated-Extension contribution is valid only when the current settings select none.

For every candidate the returned frontier records layer, optional Extension identity and selected Extension Revision, source Carrier path, Atom ID, Atom Revision, Active status, content role, and source-byte digest. It preserves the source Carrier's authored body, frontmatter, and original Relations as source facts. Draft, archived, inactive, malformed, inaccessible, ambiguous, or out-of-bound candidates are reported with their exact reason; an incomplete or ambiguous frontier is not publishable.

The result is either `{ outcome: "selected", source_frontier, source_frontier_digest, excluded_candidates, evidence_refs }` or `{ outcome: "blocked", source_frontier: null, blocking_findings, evidence_refs }`. Selection is read-only: it does not select a conflict winner, edit source authority, create output, or assert a Journal receipt. Shared Run/Step/Action receipt semantics remain owned by the shared Run-support contract.

### Sources

- CA-O-011 v12 and CA-O-152 v2; CA-O-004 v5.
- CA-P-1442 v1 and CA-A-1142 v2, W13/G5 source-to-RMED handoff.
