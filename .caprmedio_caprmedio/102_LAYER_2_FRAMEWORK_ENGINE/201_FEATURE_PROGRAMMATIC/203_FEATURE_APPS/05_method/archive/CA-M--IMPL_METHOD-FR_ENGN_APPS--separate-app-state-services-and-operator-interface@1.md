---
subject_scopes:
  - framework-engine-apps
version: 1
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Separate App state, services, and operator interface

Keep governed source, derived database or index state, local-server state, and transient interface state explicit and separate. Let backend services own filesystem, database, and process effects behind typed interfaces; let the frontend consume versioned service contracts and never bypass governed Doers to mutate project authority. Treat reconnect, stale data, cancellation, partial failure, and restart as normal state transitions with visible operator feedback.

Supervise background work through explicit startup, shutdown, timeout, and recovery boundaries. Validate untrusted input on the trusted side, encode rendered output for its context, and grant each interface only the capabilities it needs. Make primary workflows keyboard-operable and understandable, and evaluate service contracts, state transitions, rendered behavior, accessibility, and security separately.

Candidate alignment: CA-M-002, CA-M-005, CA-D-001, CA-D-002, CA-R-861.

## Sources

- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
- [OWASP Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [Python documentation: task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)
