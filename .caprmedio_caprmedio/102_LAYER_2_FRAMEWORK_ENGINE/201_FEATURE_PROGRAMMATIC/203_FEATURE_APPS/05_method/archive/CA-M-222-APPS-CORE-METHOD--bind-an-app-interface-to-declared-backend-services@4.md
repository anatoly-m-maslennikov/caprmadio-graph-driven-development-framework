---
atom_id: CA-M-222
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - app-service-interface
  depends_on:
    continuant:
      - APPS
version: 4
updated_at: 2026-08-27 14:52:39 +0400
relations:
  method_for:
    - CA-R-1187
  derived_from:
    - CA-A-057
---
# Bind an App interface to declared backend services

Bind an App interface to one declared backend-service contract without making
the interface an authority or effect owner.

## Applicable when

Apply at an App interface that presents a declared backend service to an
Operator.

## Procedure

1. Resolve the declared service contract and its admitted commands, queries,
   results, and failures.
2. Render only admitted results and submit only declared commands or queries.
3. Preserve visible request, cancellation, stale-result, and error states.
4. Consume the service contract without bypassing it to mutate project
   authority.
5. Do not impose Tool scheduling, Hook, file-mutation, or MCP protocol behavior
   on another component.

## Outcome

The App interface remains replaceable, reports its service state visibly, and
cannot become a second authority or effect owner.

## Failure or stop

Stop when the service contract is absent or stale, a result cannot be rendered
safely, an interface action would bypass the declared service, or the interface
would assume Tool, MCP, or project-authority behavior.

## Sources

- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
- [OWASP Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [Python documentation: task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)
