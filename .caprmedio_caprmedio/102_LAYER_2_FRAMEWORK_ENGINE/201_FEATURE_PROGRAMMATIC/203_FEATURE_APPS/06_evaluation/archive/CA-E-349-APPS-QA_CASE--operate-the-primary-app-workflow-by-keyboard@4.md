---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "app-accessibility"
  depends_on: []
version: 4
updated_at: "2026-09-17 02:10:33 +0000"
relations:
  evaluation_for:
    - CA-R-819
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
