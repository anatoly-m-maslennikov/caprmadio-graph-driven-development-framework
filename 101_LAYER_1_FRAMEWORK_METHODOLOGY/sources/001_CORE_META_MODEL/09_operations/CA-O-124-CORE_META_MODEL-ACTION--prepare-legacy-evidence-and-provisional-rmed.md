---
atom_id: CA-O-124
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Legacy Evidence and Provisional RMED Preparation"
  depends_on: [Action, Implementation, Spec, Atom, Artifact/Revision, Evaluation, Operator, AI Agent]
version: 1
updated_at: "2026-10-04 15:07:31 +0000"
relations:
  relates_to: [CA-O-006, CA-O-007, CA-O-008, CA-O-017, CA-O-019, CA-O-103]
---
# Summary

Prepare legacy evidence and provisional RMED

## Operation

Legacy Evidence and Provisional RMED Preparation **means** the optional reusable Action that prepares a bounded, attributable legacy-evidence and provisional-RMED packet for review, **without** adopting observations as governing authority.

1. receive the admitted preparation request, assigned Actor, exact legacy source/window and exclusions, available evidence, existing governing sources or their explicitly established absence, intended review destination, output contract and applicable permission, capability and confidence bounds. concrete legacy paths, extraction adapters and output formats are caller-bound project or Engine inputs, **not** fixed by this Action. resolve missing preparation contracts **before** claiming readiness; do **not** expand collection, access or work authority.
2. preserve the exact source/evidence identity, Revision or snapshot binding, window, locators and available acquisition provenance needed to trace each observation. distinguish actual behavior observed in the bound evidence from historical requests, descriptions and assistant implementation reports. unavailable or unverified provenance remains explicit; neither a report nor a source's current presence proves historical execution.
3. identify the relevant existing accepted R/M/E/D and their current source bindings, or record their evidenced absence. separate **observed** behavior, **inferred** interpretation and **unknown** facts, retaining the evidence and rationale for each. missing initial RMED or Journal history is a legitimate recorded condition, **not** permission to invent authority, decisions, execution or history.
4. prepare only the requested provisional R/M/E/D interpretations and candidate preserve/change decisions supported by that packet. attribute each proposed decision to its observation, inference, existing authority and uncertainty as applicable; distinguish the Actor's recommendation from an actual Operator decision. identify conflicts with existing authority without resolving them by treating observed behavior as authoritative. proposed RMED remains reviewable input, not accepted source Claims, active authority or an implementation instruction.
5. check that the bounded packet retains its source/window, attributable observations, existing or absent authority, inferred interpretations, explicit unknowns, candidate preserve/change decisions and unresolved admission needs. substantive unknowns may remain in a complete reviewable packet when explicitly qualified; missing essential source bounds, permission, provenance or preparation contracts return **blocked**, with the exact missing inputs and retained partial evidence. do **not** turn incomplete extraction into a readiness or behavior-equivalence claim.
6. return **ready-for-review** with the packet, its exact evidence/authority bindings, limitations and proposed handoff, or **blocked** with the missing contracts or other unmet preparation gates. the caller retains the result and controls any authorized persistence and next work. changed source/window, evidence, proposed decisions or governing authority makes the corresponding preparation binding stale; retain the prior result and identify the affected work rather than silently reusing it or erasing its limitations.
7. hand proposed content to separately admitted authoring and decision routes; CA-O-103 prepares authorized Atom content, while CA-O-006/CA-O-007/CA-O-008 retain their identified-conflict correction, actual decision and authorized mutation domains. this Action neither invokes those routes automatically nor certifies their completion. reuse CA-O-017 and CA-O-019 **only after** governing inputs are actually admitted and their own implementation, Evaluation and permission prerequisites are met.

## Details

This preparation Action does **not** refactor or alter the legacy implementation, mutate source Claims, activate proposed RMED, fabricate or backfill Journal history, select an approval on the Operator's behalf, or establish behavior equivalence. Absence of initial authority can support preparation, but does **not** authorize implementation or bypass a downstream gate. No mandatory graph faces, value schema, extraction adapter or additional Workflow/Step is adopted. Independent source review, governed persistence, authority admission and downstream implementation/Evaluation remain separate work.

An isolated legacy fixture with no initial RMED/Journal can yield a ready reviewable packet of traceable observations, provisional interpretations and explicit unknowns. If its required source/window or provenance cannot be established, the result is blocked with retained partial evidence. A request to refactor or activate the provisional packet is outside this Action; later behavior-equivalence assurance needs its own admitted Evaluation and actual evidence.
