---
subjects:
  governs:
    occurrent:
      - Shared Programmatic Evaluation Coverage Mapping
  depends_on:
    continuant:
      - Programmatic Policy
      - Evaluation Coverage
    occurrent:
      - Validation
version: 2
updated_at: 2026-08-30 17:21:33 +0400
relations:
  derived_from:
    - CA-A-053
    - CA-A-055
---
# Map shared PROGRAMMATIC Evaluation coverage

## Scope resolution

CA-P-072 completed with 11 active shared PROGRAMMATIC Methods: `CA-M-110` and
`CA-M-157` through `CA-M-166`. Before this Task, their only related current
Evaluation was project-root `CA-E-250`. That carrier combined technical-contract
conformance, dependency-exception review, and installed-runtime admission under
the obsolete FRAMEWORK_ENGINE SOFTWARE boundary. It is archived as version 2;
its three independently executable meanings are now owned by `CA-E-253` through
`CA-E-255` at PROGRAMMATIC.

The final successor-inclusive validation set contains 32 current carriers:
11 active shared Methods, 20 active shared Evaluations, and one unchanged
PROGRAMMATIC Method draft. The draft remains an unaccepted configuration and
prerequisite candidate; it has no shared Evaluation owner.

## Method-to-Evaluation coverage map

| Shared Method | Canonical shared Evaluation cases | Observable boundary covered |
|---|---|---|
| `CA-M-110` | `CA-E-253`, `CA-E-254`, `CA-E-255` | changed-component technical-contract conformance, incomplete bounded exception rejection, and installed selected-runtime realization when delivered |
| `CA-M-157` | `CA-E-256` | deterministic result from declared inputs without an implicit host observation or effect |
| `CA-M-158` | `CA-E-257`, `CA-E-258` | visible state and lifecycle ownership; interrupted lifecycle recovery after restart where state is recoverable |
| `CA-M-159` | `CA-E-259` | replaceable technical boundary preserves declared input, result, and failure contract |
| `CA-M-160` | `CA-E-260`, `CA-E-261` | decision is formed before its effect; incomplete plans stop at the effect boundary |
| `CA-M-161` | `CA-E-262`, `CA-E-263`, `CA-E-264`, `CA-E-265` | file precondition failure, partial-write recovery, non-zero subprocess failure, and subprocess timeout |
| `CA-M-162` | `CA-E-266` | changed hand-authored source respects its bound or records its required exception |
| `CA-M-163` | `CA-E-267`, `CA-E-268`, `CA-E-269` | diagnostic schema and severity, secret redaction, and observable diagnostic-emission failure |
| `CA-M-164` | `CA-E-270` | changed-code automation and typing ratchet remains at its admitted passing boundary |
| `CA-M-165` | `CA-E-271` | performance claim has a representative workload, preserved baseline, and comparable observation |
| `CA-M-166` | `CA-E-272` | declared public or host boundary preserves its accepted compatibility behavior |

## Candidate-theme applicability and non-applicability

| Theme | Disposition |
|---|---|
| Changed code | Covered by `CA-E-253`, `CA-E-266`, and `CA-E-270`; each applies only to the Method's stated changed-component or changed-source condition. |
| Public behavior | Covered by `CA-E-272` only when a current Requirement, technical contract, or pinned external origin declares a public or host boundary. Consumer UI behavior, protocol details, and endpoint semantics remain child-Scope authority; no fabricated universal public-behavior case is admitted. |
| Installed runtime | Covered by `CA-E-255` only when a lower-Scope Delivery declares an installable component. It does not claim a cross-platform envelope, which CA-A-053 explicitly defers. |
| Diagnostic schema | Covered by `CA-E-267`, with redaction and logging-failure boundaries separately owned by `CA-E-268` and `CA-E-269`. Journal and Work Journal semantics remain outside this coverage. |
| Performance | Covered by `CA-E-271` for a claimed performance change. No coverage percentage or numerical budget is treated as correctness; numerical thresholds remain deferred until a bounded owner admits them. |
| Interruption and restart | Covered by `CA-E-258` only where a component owns recoverable state or lifecycle. Stateless functions and components without recoverable lifecycle state are explicitly not applicable. |
| Partial write | Covered by `CA-E-263` only where a component writes, replaces, or removes files. |
| Subprocess failure and timeout | Covered separately by `CA-E-264` and `CA-E-265` only where a component invokes a subprocess. Components with no subprocess boundary are explicitly not applicable. |

## Ownership boundary

These Evaluations specify one mechanism-neutral bounded check each. They do not
select a test framework, linting or typing tool, supported platform, sink,
numeric performance budget, implementation architecture, or child-Scope
behavior. One Evaluation has one `evaluation_for` target; shared applicability
is limited to the stated conditions across Tools, App backend services, and MCP
components. Component-specific realization and public interaction checks remain
with their child Scope Units for CA-P-074.

## Validation result

The 20 current Evaluation carriers have unique IDs `CA-E-253` through
`CA-E-272`, unique summaries, one `evaluation_for` Method target each, and
direct `derived_from: CA-A-053` lineage. Every active shared Method has at
least one canonical Evaluation, and each applicable failure boundary named by
CA-P-073 has one owner or the explicit non-applicability condition above.
