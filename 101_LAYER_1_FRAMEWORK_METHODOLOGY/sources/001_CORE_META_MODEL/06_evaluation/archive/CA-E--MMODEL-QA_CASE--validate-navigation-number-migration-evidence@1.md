---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Scope Unit/Navigational Order Number"
    - "Directory Carrier/Numeric Prefix"
    - "Carrier"
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: "2026-09-16 21:56:43 +0000"
relations:
  relates_to:
    - CA-E-469
    - CA-D-300
    - CA-D-445
    - CA-M-291
---
# Validate Navigation Number Migration Evidence

## Claim checked

a Project Structure candidate retains each existing, consistently encoded Navigational Order Number **and** cannot be completed while an admitted unit's number lacks accepted creation-order evidence **or** explicit Operator selection.

## Test case

prepare fixtures with a declared greatest Structural Level that makes `102_LAYER_2_FRAMEWORK_ENGINE` decode to level `1` and navigation number `2`, plus matching numbered authority **and** Delivery Carriers. include an admitted unnumbered native Tool **or** App Carrier with an explicit selected number, and another such Carrier with no selection. then introduce differing authority/Delivery prefixes, a candidate number unequal to the encoded number, a number copied from the parent folder, a value inferred only from alphabetical order **or** filesystem time, and a native layout incorrectly rejected solely because it is unnumbered.

## Acceptance criteria

the matching numbered fixture preserves the decoded value in the candidate declaration. the selected unnumbered native fixture passes without a folder rename. the unresolved unnumbered fixture blocks candidate completion rather than receiving a guessed value. each conflicting **or** unsupported value fails with the unit, path, observed value, selected value, **and** source evidence identified. an admitted native layout does **not** fail solely for lacking a numeric prefix.

## Failure disposition

record a Concern for each mismatched **or** unsupported value; request an Operator decision for a genuinely unresolved selection. do **not** activate the candidate until every admitted Scope Unit has a supported value.
