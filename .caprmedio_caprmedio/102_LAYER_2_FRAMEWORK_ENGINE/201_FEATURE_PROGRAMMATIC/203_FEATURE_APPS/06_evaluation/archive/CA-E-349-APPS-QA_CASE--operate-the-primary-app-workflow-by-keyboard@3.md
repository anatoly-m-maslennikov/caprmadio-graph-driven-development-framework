---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - app-accessibility
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-819
---
# Operate the primary App workflow by keyboard

## Claim checked

The primary App workflow remains operable without specialist craft work or a
pointer-only interaction.

## Test case

Complete the primary Operator workflow using only a keyboard. Record the
browser and assistive-technology boundary used; automated checks may support
but cannot replace this interaction case.

## Acceptance criteria

Focus is visible, control names and roles are meaningful, traversal order is
predictable, status changes are announced, error recovery is reachable, and no
required action is pointer-only.

## Failure disposition

Reject the App workflow when any required action, status, or recovery path is
unavailable or ambiguous through keyboard operation.

## Sources

- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/understanding/)
