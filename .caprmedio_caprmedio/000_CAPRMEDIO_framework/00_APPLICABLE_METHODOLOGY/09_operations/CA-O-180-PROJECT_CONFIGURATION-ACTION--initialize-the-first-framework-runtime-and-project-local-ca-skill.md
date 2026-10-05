---
atom_id: CA-O-180
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 16:58:11 +0400"
subjects:
  governs: "Initialize first Framework runtime and project-local ca Skill"
  depends_on: [Action, Operator, Framework Package, Runtime, Methodology, Skill, Docker Image, Journal]
relations:
  relates_to: [CA-O-164, CA-R-1525, CA-R-1720, CA-R-1881, CA-M-338, CA-D-575]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-180-PROJECT_CONFIGURATION-ACTION--initialize-the-first-framework-runtime-and-project-local-ca-skill.md
  source_atom_id: CA-O-180
  source_atom_revision: 1
  source_sha256: 327f9e9722ed4346251172e36b42e0ad5a322de62ec13ecce21c52f89790a073
  original_relations_sha256: 288ebaea35a3ae58838c012c2ac1187781290de12e31a00403f1d2e1e6831746
---
# Summary

Initialize the first Framework runtime and project-local ca Skill

## Action

Initialize the first Framework runtime and project-local `ca` Skill **means** the explicit Operator-invoked Action that creates one initial runtime selection only from the empty carrier state defined by CA-R-1881.

## Scope

The Action binds one sealed current source frontier, one empty runtime/Skill state, one complete manifest-addressed package, one immutable image digest, and one canonical Action Run. Its canonical started-Run input binds `requested_run_id`, package-manifest SHA-256, sealed source-context SHA-256, and immutable image digest as one exact intent. It is a bootstrap Action outside CA-O-164's selected Release Version Workflow.

## Details

The Action invokes the admitted FRAMEWORK_INITIALIZATION Tool boundary once. It reopens the exact source and started-Run evidence before any effect; verifies the complete package, hook-free Skill, and inspected immutable image digest and labels bound to the started intent and actual manifest and source-context digests; publishes the Skill; then publishes the selector as the final activation point and emits the terminal result through the canonical Work Journal. Reusing `requested_run_id` with a changed manifest, source-context, or image digest permits only existing-Run inspection or recovery; it does not create another started evidence entry or source ledger. It does not create a selected-workflow binding, candidate N+1, Release Version Run, source delivery, canonical Projection, hook, global setting, MCP registration, image removal, automatic retry, or permanent bootstrap configuration. Existing state or an uncertain effect returns its actual blocked or partial evidence. Later changes use CA-O-164's N-to-N+1 Release Version path.
