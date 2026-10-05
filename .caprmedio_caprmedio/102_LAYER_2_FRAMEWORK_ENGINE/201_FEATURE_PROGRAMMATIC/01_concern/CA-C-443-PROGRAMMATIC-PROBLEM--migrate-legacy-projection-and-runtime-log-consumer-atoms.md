---
atom_id: CA-C-443
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Legacy Projection and Runtime Journal Consumer Alignment"
  depends_on: [Implementation, Projection, Journal, Carrier]
version: 2
updated_at: "2026-10-05 00:24:06 +0000"
relations: {concern_about: [CA-M-153, CA-E-067, CA-M-154, CA-E-068, CA-M-104, CA-D-354, CA-R-1059, CA-R-1068]}
---
# Summary

Migrate legacy Projection and runtime-log consumer atoms

## Concern

Older GRAPH_UI, GRAPH_SERVER, projection-generator, and background-service RMED carriers still prescribe Projection files beside Scope Units or under legacy .caprmedio paths and treat all runtime logs as disposable non-authoritative state. They need alignment with the current _projection placement and runtime Journal rules, but lack explicit Atom ID frontmatter required by the admitted lifecycle mutator. The legacy GRAPH_UI Delivery carrier also uses a pre-current-format identity.

## Evidences

CA-M-153 and CA-E-067 prescribe .caprmedio/mrt_atoms.html and per-unit STGs. CA-R-1059 and CA-R-1068 prescribe per-unit-root STGs. CA-M-154 and CA-E-068 prescribe logs only under .caprmedio_runtime and assert cleanup changes no Journal. CA-M-104 and CA-D-354 contain older log/projection delivery wording. Their inspected carriers have no atom_id field. The current parser rejects such target carriers rather than silently guessing or assigning identity.

## Blast radius

Current methodology sources govern the new placement and authority distinction; these older child carriers remain inconsistent until identity-safe migration and consumer alignment. Do not bypass MCP mutation, silently renumber the legacy Delivery, or claim all child consumers have been updated. Preserve prior revisions and Journal provenance during the migration.

## Repair result on 2026-10-05

Nine legacy CA-ID consumer carriers have now been explicitly migrated and aligned through sealed MCP Updates: CA-M-153@15, CA-E-067@15, CA-M-154@14, CA-E-068@15, CA-M-104@10, CA-D-354@8, CA-R-1059@15, CA-R-1068@12, and the related background-service test CA-E-223@10. Each retains its prior Atom ID and exact Summary, adds explicit current identity/classification metadata, and preserves the entire old carrier as an immutable archive revision. The eight consumer-v1 Runs stopped before effects at the container historical-proof ownership check; after a read-only project-scoped Git trust repair, their consumer-v2 Runs completed. CA-E-223 completed in consumer-v1. Persistent-view placement now uses _projection, and technical/business runtime logs remain governed Journals in configured local or remote sinks, not indiscriminately disposable runtime state. The legacy GRAPH_UI Delivery with identity CAPRMEDIO-FRAMEWORK-ENGINE-DELV-005 remains unchanged: no explicit canonical mapping was found, the Operator was asked whether to use the next unused CA-D number with an old-to-new binding, and CA-C-448 records that Question. Therefore this Problem remains Active; nine completed repairs are not full consumer closure. All successful effects and the rejected pre-effect attempts remain attributable in the shared Run Journal.
