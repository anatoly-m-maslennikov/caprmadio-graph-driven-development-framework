---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 00:15:00 +0400
relations:
  evaluation_for:
    - CA-M-203
---
# Verify bind one deterministic script to one tool

## Claim checked

CA-M-203 establishes a one-to-one mapping between independently executable deterministic entry scripts and Tool owners, including a script invoked only by a Skill.

## Applicable when

Apply whenever an independently executable script, Tool Scope Unit, Skill invocation, or canonical entrypoint declaration changes.

## Test case

Consider one bounded declared frontier containing: a correctly bound script invoked only by a Skill, one Tool with two declared entrypoints, one orphan executable script, one Tool without an entrypoint, and two non-executable imported worker modules. Resolve its bindings twice without changing the frontier.

## Acceptance criteria

The Skill-invoked entrypoint is accepted as the Tool's sole canonical script; duplicate, orphan, and missing bindings are distinct blocking findings; worker modules are not treated as Tools; and repeated resolution returns the same bindings and findings.

## Failure disposition

Reject the binding Method and preserve the declared frontier, executable inventory, Skill invocation evidence, Tool declarations, support-module classification, bindings, findings, and repeated result.
