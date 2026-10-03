---
atom_id: CA-P-933
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Project Scope Unit Graph Source Authority
    occurrent:
      - Project Scope Unit Graph Source Authority Repair
  depends_on:
    occurrent:
      - CA-P-931
version: 1
updated_at: 2026-08-31 20:56:10 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Repair Project Scope Unit Graph Source Authority

**when** CA-P-931 is Done, **then** the Assignee **must** make the current Project Scope Unit Graph authority admit exact authoritative source Artifact revisions and correct every current Project Scope Unit Delivery binding.

## Scope

`((CAPRMEDIO-META-REQU-627) union (all active Delivery Atoms owned by the 13 current Project Scope Units) union (their exact predecessor archives) union (their governed Directory Carrier receipts))`

## Definition of Done

the Task is **not done if** (Project Scope Unit Graph source authority requires a source to be an Atom when the authoritative source is another Artifact **or** **any** current Scope Unit Delivery Atom retains `.caprmedio_project` **or** its authority path differs from its exact `.caprmedio_caprmedio` Directory Carrier **or** its Delivery path differs from the current root Delivery topology **or** an exact predecessor archive is missing **or** a current Scope Unit Directory Carrier lacks a receipt that binds its current revision and digest).

## Details

preserve the requirement for exact source revision, digest, and Work Journal provenance. broaden only the admitted authoritative source Artifact kind. commit changed Scope Unit folders from descendants to ancestors so every final Directory Carrier receipt binds its current tree.
