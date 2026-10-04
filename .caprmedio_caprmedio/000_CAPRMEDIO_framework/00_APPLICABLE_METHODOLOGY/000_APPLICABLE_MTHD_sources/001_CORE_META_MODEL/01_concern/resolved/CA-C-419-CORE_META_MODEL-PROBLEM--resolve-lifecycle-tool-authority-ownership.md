---
atom_id: CA-C-419
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
version: 2
updated_at: "2026-10-04 18:15:44 +0000"
subjects:
  governs: "Lifecycle Tool authority/Scope Unit"
  depends_on: [Operations, Implementation, Plan, Artifact/Carrier]
relations:
  concern_about: [CA-P-1444]
---
# Summary

Resolve lifecycle Tool authority ownership

## Concern

Legacy lifecycle Tool folders are not declared Scope Units, so their names cannot supply admitted Scope metadata or Global Tiers.

## Evidences

P1444 directly read current project_structure.toml: TOOLS is declared, ATOM_CREATE/ATOM_UPDATE/REPLACE_ATOM/ATOM_ARCHIVE are not. Four O and matching R/E carriers have legacy incomplete properties/body boundaries.

## Blast radius

### Resolution

P1466/P1467/P1468 migrated all four lifecycle O and matching R/E carriers to the registered TOOLS owner with explicit properties and actual Global Tier. P1471/P1472 independently accepted that ownership boundary; P1472's separate numbering/Journal findings are C428/C429. No four new Scope Units were invented. This ownership defect is resolved; later implementation must use declared ownership rather than folder inference.

### Original impact

Resolve the actual registered owning Scope Unit and tier from authoritative Project Structure; use TOOLS where this is the declared owner. No mandatory invention of four Scope Units, no folder-derived authority. Preserve Engine-local capability/delivery details; generic lifecycle definitions belong Core. Narrow source/RMED migration precedes code acceptance.
