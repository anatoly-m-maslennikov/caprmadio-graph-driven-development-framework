---
atom_id: CA-O-166
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Deliver and compile candidate Methodology"
  depends_on: [Action, Methodology Source, Applicable Methodology, Delivery, Compiler, Artifact/Revision, Journal]
version: 3
updated_at: 2026-10-05 15:29:23 +0400
relations:
  relates_to: [CA-O-164, CA-O-172, CA-O-173, CA-O-011, CA-O-157, CA-R-1525, CA-R-1720]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-166-PROJECT_CONFIGURATION-ACTION--deliver-and-compile-candidate-methodology.md
  source_atom_id: CA-O-166
  source_atom_revision: 3
  source_sha256: 553a2dac5f8413242f119f02a88ff0e1915902ffb7a6d3326c9a1e831aa6ee91
  original_relations_sha256: 2412aa34f65127ba5a57374ed2533116236e14f8403954da720f4926d58d7e42
---
# Summary

Deliver and compile candidate Methodology

## Action

Deliver and compile candidate Methodology **means** the Action that performs one bound `deliver_sources` or `compile` phase for the frozen N+1 candidate; it reuses the applicable compiler contract rather than defining another compiler.

## Scope

`deliver_sources` copies the complete selected candidate Methodology source set, with every source identity, revision and digest, only to the selected staged `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources` delivery target; it never changes or substitutes `METHODOLOGY_SOURCES.authority_path`. `compile` uses the required reviewed selected-snapshot compiler Tool boundary and the delivered, still-matching candidate frontier to materialize only the sealed child `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized/<candidateSnapshotManifest.sha256>/`. It neither produces nor replaces the canonical Applicable Methodology at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/`; the runtime Methodology is a later derived delivery, not compiler output authority.

## Details

No partial source set, implicit root, silently translated Project Structure path, stale compiler output, altered source byte, unreviewed Tool boundary/output layout or changed candidate frontier is success. The reviewed selected-snapshot compiler boundary materializes the sealed child while the existing canonical source-bound compiler authority at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/` remains unchanged; canonical emission is not this Action's output. The Action validates complete source and sealed child manifest/digests before returning; it preserves N, all authoring sources, the canonical Projection, Journals and unrelated deliveries. It does not install a runtime package or Skill, run tests, build an image, promote, remove an image, alter the compiler, or use a second compilation Workflow. A failed or recording-blocked phase retains actual effects and journal evidence without claiming compilation or delivery complete.
