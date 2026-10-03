---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Producer Result/Flow Direction"
  depends_on:
    - "Scope Unit"
    - "Relation"
    - "Producer"
    - "Consumer"
    - "Process"
priority: medium
version: 1
updated_at: "2026-09-17 16:22:39 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should the backward-coupling rule use Atom-owned Demands?

which Atom-owned Relation **and** result-flow condition should trigger the proposal **in** CAPRMEDIO-METHODOLOGY-REQU-515 **after** the obsolete between-Layer dependency model **in** CAPRMEDIO-REQU-040 is removed?

## Evidence

- CAPRMEDIO-REQU-040 requires **every** dependency between Project Layers **to** point from an earlier Layer **to** a later one. its only active dependent is CAPRMEDIO-METHODOLOGY-REQU-515.
- CA-R-932 defines a Consumer-owned Demand about a Producer; CA-R-945 defines the opposite Producer-result flow. neither establishes an additional edge **in** the Scope Unit tree under CA-R-718.
- CAPRMEDIO-METHODOLOGY-REQU-515 requires proposing peer-scope remodeling for necessary backward coupling that cannot be removed, re-owned, **or** represented as Operations feedback. the proposal trigger is valuable, but its graph kind **and** feedback meaning are unspecified; current Operations Atoms define behavior rather than record feedback evidence.

## Principle check

CA-M-002 rejects a second Scope Unit dependency system; CA-M-006 requires direction **and** endpoint meanings **to** remain coherent; CA-R-1490 preserves the unique proposal condition. these Principles do **not** determine whether the old trigger denotes a Demand, Producer-result flow, **or** a Process control-flow condition.

## Disposition

preserve the exact two source Claims pending a targeted replacement. resolve the trigger against admitted Atom-owned Relations **and** distinguish those Relations from the Scope Unit tree. preserve the proposal **and** its applicable constraints through an O definition **only** after its operational boundary is clear; do **not** silently reverse an edge, invent a Scope Unit dependency, **or** drop the sole incoming proposal rule.
