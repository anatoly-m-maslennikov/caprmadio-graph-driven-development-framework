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
version: 1
updated_at: 2026-09-01 23:04:33 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Establish CA Main Skill Authority Bundle

**when** this Task starts, **then** the Assignee **must** establish the complete accepted authority required to implement the canonical CAPRMEDIO Main Skill with identity `ca`.

## Scope

`((current active authority governing the CAPRMEDIO Main Skill, CAPRMEDIO Routing Tree, CAPRMEDIO General System Prompt, Tools, MCP, Skills, agent-host serialization, installation, effects, approvals, and runtime lifecycle) union (genuinely missing authority required for the CA Main Skill vertical slice))`

## Definition of Done

the Task is **not done if** (the authority bundle does not define the canonical `ca` identity and `$ca` Codex and `/ca` Claude serializations **or** routing inputs, normalization, project resolution, target selection, invocation envelope, effects, approvals, state, lifecycle, transitional dispatch, snapshot pinning, compaction recovery, and resume behavior are incomplete **or** any implementation choice silently substitutes for missing authority **or** duplicate authority is created **or** any material uncertainty below 95 percent confidence remains unresolved with the Operator).

## Details

reconcile current authority before authoring new Atoms. keep provider-neutral semantics distinct from host-specific invocation syntax. preserve exclusive CAPRMEDIO General System Prompt loading by the Main Skill and require all registered branch or leaf routing through the canonical Routing Tree.
