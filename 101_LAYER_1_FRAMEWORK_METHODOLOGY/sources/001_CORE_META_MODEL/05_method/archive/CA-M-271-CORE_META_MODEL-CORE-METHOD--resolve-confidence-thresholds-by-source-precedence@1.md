---
atom_id: CA-M-271
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - "Confidence Threshold/resolution"
  depends_on:
    continuant:
      - "Confidence Threshold"
      - "Operator"
      - "Atom/Content Role: Plan/Type: Task"
      - "Epic"
      - "Framework Instance Settings"
      - "Property"
      - "AI Agent"
version: 1
updated_at: "2026-09-09 02:24:28 +0400"
relations:
  child_of:
    - "CA-R-1428"
---
# Resolve confidence thresholds by source precedence

**to** resolve an effective Confidence Threshold for a decision **or** action, an AI Agent **must** perform **all** of:

1. identify the confidence decision **and** context **to** which the threshold applies.
2. inspect applicable sources **in** this precedence: direct Operator input, an explicit value on the Task, the nearest enclosing Epic with an explicit value, **and** the Framework Instance Settings default. **when** an Epic omits the value, inspect its enclosing Epics from nearest **to** farthest.
3. use the first applicable explicit value; **if** no source supplies a value **or** the selected source is invalid **or** ambiguous, **then** request Operator disposition **before** the affected autonomous action **without** inventing a value **or** silently selecting a lower-precedence source.
4. apply direct Operator input **only** within its stated context; do **not** change unrelated decisions, Tasks, Epics, **or** Settings.
5. do **not** copy an inherited value into a Task **or** Epic override. preserve an explicitly selected override as explicit **when** its value **`=`** the currently inherited value, because later changes **to** the inherited source **must not** silently change that explicit selection.
