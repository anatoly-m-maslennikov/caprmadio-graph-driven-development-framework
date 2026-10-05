---
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Step Run"
    - "Artifact/Revision"
    - "Journal"
    - "Operator"
version: 6
updated_at: "2026-10-03 00:06:54 +0400"
relations: {"relates_to": ["CA-R-1510", "CA-R-1511", "CA-R-1519", "CA-R-1520", "CA-R-1720"]}
atom_id: "CA-R-1525"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1525-CORE_META_MODEL-GENERAL-REQUIREMENT--bind-workflow-runs-to-exact-definition-revisions.md
  source_atom_id: CA-R-1525
  source_atom_revision: 6
  source_sha256: b1b4a498fd0b3beb77d9b78eaeffb6ca47e1754300dd666fd78e2502791df29c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Bind Workflow Runs to exact definition Revisions

## Scope

Workflow Runs **and** their exact definition Revisions admitted for execution.

## Claim

**every** Workflow Run **must** retain the exact Workflow graph Revision, referenced Step Atom Revisions, **and** referenced Action definition Revisions admitted for its execution.

## Details

- record references **to** those source Revisions **and** the actual binding used by **every** Step Run **in** the canonical Journal. do **not** create independently maintained copies of the definitions as another authority.
- **before** dispatch **and** on recovery, check whether a bound definition has changed, been withdrawn, **or** become unavailable. a detected change pauses further dispatch for revalidation; the executor **must not** silently substitute the newest Revision **or** assume the old binding remains authorized.
- revalidation **must** identify the exact definitions admitted for the remaining work, check their compatibility with completed effects **and** remaining inputs, **and** satisfy the applicable approval conditions. resume **only** **after** that decision is recorded; unresolved compatibility **or** authority keeps execution blocked.
- completed Step Runs retain their original definition bindings **and** outcomes. revalidation **must not** rewrite history, reset retry allowances, **or** automatically replay completed effects.
- an Action already running follows its admitted interruption policy; a definition change alone does **not** authorize forced termination **or** blind replay. retain its actual result under the binding used **and** revalidate **before** further dispatch.
- definition binding does **not** freeze permissions **or** mutable target state. current authorization, required Operator decisions, **and** input freshness still apply **before** effects.
- a successor Workflow Run obtains its own admitted definition bindings rather than silently inheriting the predecessor's bindings for another Workflow.
