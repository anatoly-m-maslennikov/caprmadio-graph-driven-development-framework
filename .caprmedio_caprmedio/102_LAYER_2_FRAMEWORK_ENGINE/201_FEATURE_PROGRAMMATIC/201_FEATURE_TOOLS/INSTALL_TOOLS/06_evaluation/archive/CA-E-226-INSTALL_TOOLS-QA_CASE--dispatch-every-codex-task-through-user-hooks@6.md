---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-25 01:49:10 +0400
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103
---
# Dispatch every Codex task through asynchronous user Hook intake

## Claim checked

One installed user-level dispatcher makes durable asynchronous CAPRMEDIO intake available to every Codex task without project-local Hook discovery or host-visible provenance delay.

## Test case

Prepare a user Hook carrier with unrelated groups, install Tools into two repositories, prepare a third uninstalled repository with a lookalike launcher, and invoke the PostToolUse command from each repository and outside a repository. Compile matcher .* against representative supported tool names and inspect the async setting and accepted event.

## Acceptance criteria

Installation preserves unrelated groups and creates exactly one generic PostToolUse command group with matcher .* and async: true. Each installed repository carries caprmedio.codex-hooks = v1 and delegates only to its executable installed commit-trigger launcher. One invocation atomically accepts an inbox event and returns without scanning or running the provenance pipeline. The uninstalled repository and outside invocation exit without effect. No command embeds an absolute project path, release digest, or executable dependency in the Codex user directory.

## Failure disposition

Reject installation if the matcher is invalid, async is absent, intake blocks for provenance work, accepted input is lost, unrelated groups change, dispatch depends on project trust or a fixed repository path, the wrong installation runs, or work occurs outside an activated installed repository.
