---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "app-service-interface"
  depends_on: []
version: 5
updated_at: "2026-09-17 02:10:33 +0000"
relations:
  evaluation_for:
    - CA-M-222
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Render untrusted project content only as data

## Claim checked

An App interface renders untrusted project content safely **without** turning data
into executable authority **or** capability.

## Test case

Render **every** supported App view with project text containing HTML, script,
URL, style, **and** bidirectional-control payloads.

## Acceptance criteria

Each value is encoded for its exact output context, executes no active content,
gains no additional capability, **and** remains inspectable as project data.

## Failure disposition

Reject the rendering boundary **when** **any** payload executes, escapes its output
context, gains capability, **or** becomes unavailable for inspection as data.

## Sources

- [OWASP Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
