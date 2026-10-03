---
atom_id: CA-P-906
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Term System and Subject Expression Authority
    occurrent:
      - Term System Authority Update
  depends_on:
    occurrent:
      - CA-P-905
version: 1
updated_at: 2026-08-28 21:11:50 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Update Term Relations and Subject Expression Authority

**when** CA-P-905 is Done, **then** the Assignee **must** make the Term-system and Subject-Expression authority express the accepted relation and qualification model.

## Scope

`((every CA-P-905 frontier entry assigned to TERM_SYSTEM_AND_SUBJECT_EXPRESSION) union (every replacement or new authority Atom created from such an entry))`

## Definition of Done

the Task is **not done if** (the Term system has any primitive relation other than SUBTYPE_OF, IS_BORNE_BY, and IS_ALLOWED_VALUE_OF **or** BEARS is treated as a fourth primitive relation instead of the derived inverse view of IS_BORNE_BY **or** `/` expresses anything other than one bearer edge **or** `:` expresses anything other than assignment of an allowed value **or** a value-qualified Entity cannot bear the next Property in a Subject Expression **or** `INSTANCE_OF` is treated as SUBTYPE_OF or as a Term-system primitive **or** SUBTYPE_OF permits a cycle **or** multiple inheritance fails to inherit every parent invariant conjunctively **or** conflicting inherited invariants do not invalidate the candidate subtype **or** Core authority claims that the extensible taxonomy is closed **or** a reusable Term is identified by a global Subject-Path ordinal **or** any governed Term or Subject Expression segment begins with a lowercase letter **or** any Entity name contains `/` **or** any governed Term redefines a registered CCE operator **or** any Scope Unit name equals a registered CCE operator **or** any replaced conflicting authority remains active).

## Details

govern expressions such as `Atom/Content Role: Plan/Type: Task` and `Atom/Content Role: Requirement/Type: Job`. interpret `Content Role: Plan` as Plan IS_ALLOWED_VALUE_OF Content Role. keep graph-specific relations outside the Term system. define INSTANCE_OF only in the Entity-instance graph. remove the global dependent-Term ordinal-position rule; canonical qualification comes from the complete Subject Expression and its valid bearer edges. keep registered CCE operators lowercase and bold in Atom content, and exclude them from Term capitalization.
