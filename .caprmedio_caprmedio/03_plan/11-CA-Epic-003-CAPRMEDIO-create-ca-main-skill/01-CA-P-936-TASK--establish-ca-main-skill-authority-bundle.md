---
atom_id: CA-P-936
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - CA Main Skill Authority Bundle
    occurrent:
      - CA Main Skill Authority Establishment
  depends_on:
    continuant:
      - CAPRMEDIO Main Skill
      - CAPRMEDIO Routing Tree
      - CAPRMEDIO General System Prompt
version: 2
updated_at: 2026-09-07 19:43:08 +0000
autonomous_confidence_threshold: 99
relations: {}
---
# Establish CA Main Skill Authority Bundle

**when** this Task starts, **then** the Assignee **must** establish the complete accepted authority required to implement the canonical CAPRMEDIO Main Skill with identity `ca` for the current Codex-native vertical slice.

## Scope

`((current active authority governing the CAPRMEDIO Main Skill, CAPRMEDIO Routing Tree, CAPRMEDIO General System Prompt, Tools, MCP, Skills, Codex host serialization, installation, effects, approvals, and runtime lifecycle) union (genuinely missing authority required for the Codex-native CA Main Skill vertical slice))`

## Definition of Done

the Task is **not done if** (the authority bundle does not define the canonical `ca` identity and Codex `$ca` serialization **or** routing inputs, normalization, project resolution, target selection, invocation envelope, effects, approvals, state, lifecycle, transitional dispatch, snapshot pinning, compaction recovery, and resume behavior are incomplete **or** any implementation choice silently substitutes for missing authority **or** duplicate authority is created **or** any material uncertainty below 95 percent confidence remains unresolved with the Operator).

## Details

reconcile current authority before authoring new Atoms. apply the native support boundary in CA-R-826. Claude adapter implementation, installation, and runtime validation are deferred outside this Epic; optional Claude compatibility requires separate Operator authorization through an Extension or an Operator-provided compatibility layer. keep provider-neutral semantics distinct from host-specific invocation syntax. preserve exclusive CAPRMEDIO General System Prompt loading by the Main Skill and require all registered branch or leaf routing through the canonical Routing Tree.
