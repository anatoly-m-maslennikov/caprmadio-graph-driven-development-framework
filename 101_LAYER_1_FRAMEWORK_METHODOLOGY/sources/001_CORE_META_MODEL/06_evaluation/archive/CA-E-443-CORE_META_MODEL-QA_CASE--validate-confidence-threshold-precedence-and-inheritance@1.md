---
atom_id: CA-E-443
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - "Confidence Threshold/resolution validation"
  depends_on:
    continuant:
      - "Confidence Threshold"
      - "Autonomous Confidence Threshold"
      - "Operator"
      - "Atom/Content Role: Plan/Type: Task"
      - "Epic"
      - "Framework Instance Settings"
      - "Property"
      - "Concern"
      - "Carrier"
version: 1
updated_at: "2026-09-09 02:24:28 +0400"
relations:
  evaluation_for:
    - "CA-R-1043"
    - "CA-R-1044"
    - "CA-R-1045"
    - "CA-R-1427"
    - "CA-R-1428"
    - "CA-M-271"
    - "CA-M-130"
    - "CA-D-273"
    - "CA-D-278"
    - "CAPRMEDIO-META-REQU-144"
---
# Validate confidence-threshold precedence and inheritance

## Claim checked

the effective Confidence Threshold follows CA-M-271 **and** controls autonomous continuation according **to** CA-M-130 **without** duplicating inherited authority.

## Test case

create a Framework Instance Settings default, an outer Epic, an inner Epic, **and** a Task with distinct permitted threshold values. successively omit the Task value, the inner Epic value, **and** the outer Epic value. add direct Operator input for one Task context **and** an unrelated Task **without** that input. also create an explicit Task override equal **to** the Epic value, **then** change the Epic value. test confidence below, equal **to**, **and** above the selected threshold. test a missing default **when** no override applies, an invalid selected value, ambiguous input, **and** an action **without** required authority.

## Acceptance criteria

direct Operator input wins **only** **in** its stated context; **otherwise** Task, nearest explicit enclosing Epic, **and** Framework Instance Settings supply the value **in** that precedence. omitted values resolve **without** copied overrides. changing an inherited source affects inheriting Tasks but **not** an explicit Task override, including one that previously equalled the inherited value. no applicable source, an invalid selected source, **or** ambiguous input requests Operator disposition **without** invented values **or** silent fallback. confidence below the effective threshold blocks autonomous continuation; confidence equal **to** **or** above it does **not** create authority. threshold selection does **not** mutate source Settings **or** override Properties.

## Failure disposition

record a Concern identifying the affected source, context, inherited value, Carrier, **or** permission boundary.
