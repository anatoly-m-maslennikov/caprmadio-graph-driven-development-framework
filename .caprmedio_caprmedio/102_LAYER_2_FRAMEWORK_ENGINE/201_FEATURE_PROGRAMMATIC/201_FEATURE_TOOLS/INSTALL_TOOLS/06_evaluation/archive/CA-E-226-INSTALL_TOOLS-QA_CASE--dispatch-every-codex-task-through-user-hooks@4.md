---
atom_id: CA-E-226
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103
  check_of:
    - CA-D-011
---
# Dispatch every Codex task through user Hooks

## Claim checked

One installed user-level dispatcher makes the same CAPRMEDIO Hook boundaries available to every subsequently started or resumed Codex task without depending on project-local Hook discovery.

## Test case

Prepare a Codex user Hook carrier with unrelated groups, install Tools into two repositories, prepare a third uninstalled repository with a lookalike launcher, and invoke each managed Hook command from every repository and once outside any repository. Compile each tool-event matcher as the host's full-value regular expression and test it against representative Codex tool names, including `functions.exec` and `apply_patch`.

## Acceptance criteria

Installation preserves every unrelated group and creates exactly one generic group for each of `PreToolUse`, `PostToolUse`, `SessionStart`, and `Stop`. Each tool-event group carries the valid full-value matcher `.*`; the invalid bare quantifier `*` is absent. The matcher accepts every representative tool name, and the paired callback performs one actual installed end-to-end commit after a representative file edit. Each installed repository carries local Git activation `caprmedio.codex-hooks = v1`, and its invocation delegates only to its executable `.caprmedio_install/bin/commit-trigger`. The uninstalled repository and outside invocation exit successfully without effect. No command embeds an absolute project path, release digest, or executable dependency in the Codex user directory.

## Failure disposition

Reject installation if a matcher is syntactically invalid or misses a supported tool name, if the paired callback does not commit the representative edit, or if installation duplicates or removes unrelated groups, depends on project trust or a fixed repository path, invokes the wrong installation, or performs work outside an installed repository.
