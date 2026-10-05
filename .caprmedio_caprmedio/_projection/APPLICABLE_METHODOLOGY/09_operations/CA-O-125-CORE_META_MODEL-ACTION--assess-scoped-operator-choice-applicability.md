---
atom_id: CA-O-125
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Scoped Operator-choice Applicability"
  depends_on: [Action, Operator, AI Agent, Atom, Artifact/Revision, Journal]
version: 1
updated_at: "2026-10-04 15:06:54 +0000"
relations:
  relates_to: [CA-O-007, CA-O-008, CA-O-013, CA-O-022, CA-O-023, CA-O-065, CA-O-078, CA-O-118]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-125-CORE_META_MODEL-ACTION--assess-scoped-operator-choice-applicability.md
  source_atom_id: CA-O-125
  source_atom_revision: 1
  source_sha256: 384d40a5248d902591563bd494cb92c492d4bbf3ae586523a201b8bb704337ff
  original_relations_sha256: 578c17b6338a827816194a58a1a8ff63e74697ec3dc4ee0bb0e6c0f5d912b739
---
# Summary

Assess scoped Operator-choice applicability

## Operation

Scoped Operator-choice Applicability Assessment **means** the optional read-only Action that matches supplied literal Operator input to its supported antecedent and returns its prospective choice boundaries and the still-independent choices within a caller-declared packet. An Operator or an AI Agent acting within existing permission may perform the assessment; invoking it does **not** grant permission for any selected effect.

### Inputs

- literal Operator input or annotation with actual provenance, its applicable target and prospective scope; distinguish it from assistant reports, copied wrappers and inferred approval.
- exact question, proposal and alternative versions, including later explicit corrections and the current relevant source state.
- the caller-bounded independent-choice list and its declared completeness, existing settled decisions and delegation, and current applicable Goal, Project Principles, authority and effective confidence requirements. Unknown antecedent or list completeness remains unknown.

### Assessment

1. Check existing settled decisions and complete applicable delegation before identifying a missing Operator choice. Do **not** manufacture a redundant question when existing authority already settles the allowed action; its execution owner still validates the complete bounds.
2. Match the literal input only to an evidence-supported antecedent and alternative. A short answer to one question does **not** settle another independent question. Preserve the actual answer and references rather than substituting an assistant's interpretation for human provenance.
3. Check applicability against the exact proposal, target, scope and current source/context frontier. Preserve later explicit corrections and their prospective bounds. Added benchmark, implementation or other effects are **not** covered by a research-only answer; a changed proposal or frontier does **not** inherit renewed approval. Distinguish the choice, permission, planned effect, actual effect and evidence for each.
4. Return the supported match and its exact applicable boundaries with evidence references, or identify missing, ambiguous, mismatched, superseded or changed applicability and the precise unresolved point. Return the still-independent unanswered choices within the declared list; do **not** claim that all Project choices are known. If required input is unavailable or a check fails, return that limitation and any partial assessment without claiming a complete result.

### Outcome and handoff

The result is an evidence-bound assessment, **not** approval or execution readiness. It identifies the assessed input and antecedent versions, applicable choice/bounds, corrections or currentness limitations, unresolved points and remaining independent choices. Required authoritative decision records are referenced, **not** copied. If the calling domain requires a record or prerequisite that is absent, return the absence; do **not** fabricate it or impose Journal recording on every generic question.

An unresolved result **may** supply one consequential question for the caller, with the relevant Concern, affected Atom, Goal, proposal/alternatives and evidence needed to understand the choice. This Action does **not** ask repeatedly, run a question loop or force another approval. The caller retains invocation, communication, persistence, permission and readiness gates.

## Details

Reuse CA-O-007 for obtaining and recording source-correction decisions and CA-O-008 for authorized source effects; changed applicability is returned to those owners, **not** resolved by copying or rewriting an old Journal record. Structural authorization remains CA-O-013. Priority resolution/activation and alternative selection remain CA-O-022 / CA-O-023: a matching answer does **not** resolve unknown parameters, invent a tie-break or activate a model. Warned-name acceptance remains CA-O-065, not independent naming approval by this assessment. CA-O-078 retains navigation-candidate preparation and its domain decision boundary; CA-O-118 retains coverage accounting, which a human-answer match does **not** turn into covered work or semantic correctness.

Confidence is interpretation evidence, never authority; current Operator authority and complete delegation remain governing. No result expands delegation, adopts a report, creates approval, activates priorities, mutates a target, appends or copies Journal truth, replaces or replays an effect, or authorizes rollback, automatic repair/recheck or Workflow invocation. This generic Action does **not** create a decision/history carrier, output schema or mandatory ceremony. Concrete question/report identifiers, result encoding, presentation and adapters remain caller/Project inputs; actual effects and their proof stay with their existing owners.
