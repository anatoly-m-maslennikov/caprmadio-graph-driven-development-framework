---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - app-service-interface
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-222
---
# Reject interface bypass of governed Doers

## Claim checked

An App interface cannot bypass its declared backend-service contract or become
a second project-authority mutation path.

## Test case

Submit one Operator-interface request that would change project authority
through the frontend, service API, direct derived-database access, and the
declared governed Doer path.

## Acceptance criteria

Only the governed Doer path can apply the request. Every bypass is rejected
without changing governed source, derived state, or Runtime evidence.

## Failure disposition

Reject the interface when a bypass succeeds, mutates any carrier, or obscures
which declared service and Doer owned the request.

## Sources

- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
- [Python documentation: unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
