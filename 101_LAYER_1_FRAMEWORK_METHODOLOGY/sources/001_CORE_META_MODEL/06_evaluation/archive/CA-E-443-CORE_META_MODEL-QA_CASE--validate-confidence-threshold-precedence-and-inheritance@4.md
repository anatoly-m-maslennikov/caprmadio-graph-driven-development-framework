---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Confidence Threshold/resolution validation"
  depends_on:
    - "Atom/Content Role: Plan/Type: Objective"
    - "Confidence Threshold"
    - "Autonomous Confidence Threshold"
    - "Operator"
    - "Atom/Content Role: Plan/Type: Task"
    - "Epic"
    - "Framework Instance Settings"
    - "Property"
    - "Concern"
    - "Carrier"
version: 4
updated_at: "2026-09-21 00:39:50 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for":["CA-R-1043","CA-R-1044","CA-R-1045","CA-R-1427","CA-R-1428","CA-M-271","CA-R-1553","CA-D-273","CA-D-278","CAPRMEDIO-META-REQU-144"]}
---
# Validate confidence-threshold precedence and inheritance

## Claim checked

the effective Confidence Threshold follows CA-M-271 **and** controls autonomous continuation according **to** CA-R-1553 **without** duplicating inherited authority.

## Test case

create a Framework Instance Settings default, an outer Epic, an inner Epic, **and** a Task with distinct permitted threshold values. successively omit the Task value, the inner Epic value, **and** the outer Epic value. add direct Operator input for one Task context **and** an unrelated Task **without** that input. also create an explicit Task override equal **to** the Epic value, **then** change the Epic value. test confidence below, equal **to**, **and** above the selected threshold. test a missing default **when** no override applies, an invalid selected value, ambiguous input, **and** an action **without** required authority.

## Epic Carrier cases

- for **every** Epic with an explicit threshold, use **only** its own active Objective Atom under CA-D-273. keep that Objective outside its target Epic.
- omit an inner Epic's Objective **or** its confidence field while leaving a retry field; confirm confidence inheritance from the nearest outer explicit source.
- place an unrelated Objective nearby; confirm its physical location does **not** make it an inherited source. ignore non-active Objective revisions.
- **when** the Epic source is reached **in** precedence, reject multiple active Objectives for the same Epic, malformed override metadata, **or** an invalid selected threshold **without** falling through **to** a lower source. do **not** create a settings file, Objective, **or** copied override during resolution.

## Acceptance criteria

direct Operator input wins **only** **in** its stated context; **otherwise** Task, nearest explicit enclosing Epic, **and** Framework Instance Settings supply the value **in** that precedence. omitted values resolve **without** copied overrides. changing an inherited source affects inheriting Tasks but **not** an explicit Task override, including one that previously equalled the inherited value. no applicable source, an invalid selected source, **or** ambiguous input requests Operator disposition **without** invented values **or** silent fallback. confidence below the effective threshold blocks autonomous continuation; confidence equal **to** **or** above it does **not** create authority. threshold selection does **not** mutate source Settings **or** override Properties.

## Failure disposition

record a Concern identifying the affected source, context, inherited value, Carrier, **or** permission boundary.
