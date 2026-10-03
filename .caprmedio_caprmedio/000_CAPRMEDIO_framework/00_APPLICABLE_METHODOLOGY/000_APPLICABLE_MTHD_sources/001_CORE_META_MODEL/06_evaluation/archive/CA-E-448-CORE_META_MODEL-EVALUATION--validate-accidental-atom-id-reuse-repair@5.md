---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Identity/collision repair"
  depends_on:
    - "Atom/Identity"
    - "Atom/Content Role"
    - "Atom/Claim"
    - "Atom/Scope"
    - "Artifact/Revision"
    - "Carrier/Canonical Address"
    - "Project"
    - "Operator"
    - "Confidence Threshold"
    - "Work Journal"
version: 5
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  evaluation_for:
    - CA-M-276
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate accidental Atom ID reuse repair

the Evaluation **must** reject completion of an Atom ID collision repair under CA-M-276 **if** **any** of:

- the original owner was selected **without** sufficient recorded assignment evidence **or** the required Operator decision, **or** its valid Atom ID changed.
- a later accidental reuse retains the colliding ID, receives a previously used number, **or** receives an ID outside its Project prefix **and** Content Role sequence.
- an affected Claim, Content Role, Atom Scope, Claim Target Scope Unit, **or** textual Claim Scope changes beyond the approved identity-reference correction, a distinct Claim is lost **or** merged, **or** an unrelated identity changes.
- a prior Revision **or** historical Record is rewritten, history becomes unreachable, **or** the Work Journal lacks the exact mapping between the historical Carrier **and** its corrected identity.
- an affected current reference resolves ambiguously, remains unresolved, **or** resolves **to** a different intended Claim; an uncertain reference is rebound **without** the required Operator decision.
- legitimate same-Atom Revisions **or** derived copies are renumbered as accidental reuse, **or** lookup **or** compilation silently selects an identity winner.

the Evaluation **must** distinguish a paused collision awaiting an Operator decision from a completed repair. its checks **must** cover the verified-original-owner case, reversed Carrier discovery order, an unknown original owner, an ambiguous incoming reference, **and** legitimate same-Atom Revisions **or** derived copies.
