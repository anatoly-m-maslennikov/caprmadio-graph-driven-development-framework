---
atom_id: CA-M-276
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - "Atom/Identity/collision repair"
  depends_on:
    continuant:
      - "Atom/Identity"
      - "Atom/Content Role"
      - "Atom/Claim"
      - "Atom/Scope"
      - "Atom/Claim/Scope"
      - "Artifact/Revision"
      - "Carrier/Canonical Address"
      - "Project"
      - "Operator"
      - "AI Agent"
      - "Confidence Threshold"
      - "Work Journal"
version: 1
updated_at: "2026-09-11 02:23:49 +0400"
relations:
  method_for:
    - CA-R-728
    - CA-R-732
---
# Repair accidental Atom ID reuse

**to** repair accidental reuse of an assigned Project Atom ID, an AI Agent **must** perform **all** of:

1. identify the distinct source Atoms by exact Carrier address, Revision, **and** recorded history. distinguish accidental reuse from legitimate Revisions of the same Atom **and** derived copies of its Carrier.
2. establish the original valid owner from recorded assignment history. **if** the original owner cannot be established at the effective Confidence Threshold, request an Operator decision for that collision **before** changing its identities **or** references. filename order, discovery order, current filesystem timestamps, **or** the highest Version **must not** select the owner.
3. preserve the original owner's Atom ID. give **every** later accidental reuse the next unreused Project-wide number for its own Content Role under CA-R-732, using the encoding under CA-D-378. this corrects invalid reuse **and** does **not** authorize changing a valid owner's immutable identity.
4. preserve **every** affected Atom's Claim, Content Role, Atom Scope, **and** Claim Scope. preserve its immutable prior Revisions **and** recorded history; record the exact predecessor-to-corrected-identity mapping **in** the existing Work Journal **without** rewriting historical Carriers **or** Records.
5. resolve **every** affected current reference against its intended Atom using the reference's context **and** recorded history. update references **only** **when** their intended targets are established; request an Operator decision for unresolved references. do **not** replace the ambiguous ID indiscriminately.
6. verify that the repaired active identities resolve uniquely **and** **every** affected current reference still identifies its intended Claim **before** declaring the collision repaired. keep unrelated Claims **and** identities unchanged.
7. perform repair as an explicitly authorized source change, **not** as an automatic side effect of lookup **or** compilation. preserve CA-D-336's failure on ambiguous lookup **until** source repair is complete, **and** regenerate affected Projections from their corrected sources through their existing governed workflows.
