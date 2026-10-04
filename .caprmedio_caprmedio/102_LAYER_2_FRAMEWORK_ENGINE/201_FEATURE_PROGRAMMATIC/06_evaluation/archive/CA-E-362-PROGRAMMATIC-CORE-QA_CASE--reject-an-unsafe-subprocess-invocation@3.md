---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "subprocess-invocation"
  depends_on:
    - "programmatic software"
version: 3
updated_at: "2026-09-15 21:31:49 +0000"
relations:
  evaluation_for:
    - CA-M-161
  derived_from:
    - CA-A-053
---
# Reject an unsafe subprocess invocation

## Claim checked

**when** no explicit governing exception applies, a PROGRAMMATIC subprocess invocation **must** use an argument array, an explicit timeout, checked exit status, controlled environment input, **and** disabled shell execution under CA-M-161.

## Test case

- evaluate a default-policy invocation expressed as a shell command string with shell execution enabled **and** no governing exception.
- evaluate a bounded argument-array invocation with disabled shell execution, timeout, checked exit status, **and** controlled environment input.

## Acceptance criteria

- reject the first invocation **before** process creation **and** report the unsafe argument **and** shell boundary.
- admit the second invocation **only** **when** its complete bounded effect contract is satisfied.
- evaluate an explicitly permitted exception against its governing authority; this default-policy fixture **must not** create a universal prohibition **or** authorize an exception.

## Failure disposition

reject an invocation that violates its governing effect boundary.
