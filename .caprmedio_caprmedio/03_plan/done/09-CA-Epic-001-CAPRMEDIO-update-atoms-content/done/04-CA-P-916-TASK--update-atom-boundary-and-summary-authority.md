---
atom_id: CA-P-916
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Atom Claim, Claim Scope, and Summary Authority
    occurrent:
      - Atom Boundary Authority Update
  depends_on:
    occurrent:
      - CA-P-908
version: 1
updated_at: 2026-08-28 21:11:50 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Update Atom Boundary and Summary Authority

**when** CA-P-908 is Done, **then** the Assignee **must** make Atom-boundary and Summary authority preserve one independently governable Claim and one atomic or composite Claim Scope.

## Scope

`((every CA-P-905 frontier entry assigned to ATOM_CLAIM_SCOPE_AND_SUMMARY) union (every replacement or new authority Atom created from such an entry))`

## Definition of Done

the Task is **not done if** (an Atom may have zero or more than one independently replaceable Claim **or** an Atom may have zero or more than one Claim Scope **or** logical composition alone is treated as proof of multiple Claims or Claim Scopes **or** independently replaceable governing effects remain joined in one Atom **or** a composite Scope Expression cannot use parentheses, set or logical operators, explicit Atom IDs, or field predicates including WHERE **or** a Summary is authoritative **or** a Summary has identity or lifecycle independent from its source Atom **or** a Summary is derived from less than the complete Claim and Claim Scope **or** a Summary must rephrase the complete Claim instead of concisely projecting its navigational effect **or** a Summary adds, broadens, narrows, or contradicts its source authority **or** a Claim, Claim Scope, or Translation is reconstructed or validated from the Summary **or** any replaced conflicting authority remains active).

## Details

distinguish logical composition from authority multiplicity by independent replaceability. permit one Claim to govern one joint effect through composite conditions, value sets, and operators. permit one Claim Scope to select an atomic or composite set through deterministic Scope Expression syntax. derive the Summary for navigation, then derive its filename slug and H1 Carrier forms without making any of them authoritative.
