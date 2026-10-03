---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 5
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  method_for:
    - CA-R-1124
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind one deterministic script to one Tool

## Applicable when

Use this Method when admitting or reviewing an independently executable deterministic script, including one invoked exclusively by a Skill.

## Procedure

1. Select the active Tool Scope Units and independently executable deterministic entry scripts within one declared frontier.
2. Resolve each script's declared Tool identity and each Tool's canonical entrypoint from their owning authority carriers; include entrypoints invoked only through a Skill.
3. Compare the two sets and require one exact Tool-to-entrypoint binding in each direction.
4. Classify imported modules, workers, and shared libraries that are not independently executable as implementation support, even when several Tools call them.
5. Report every missing, duplicate, cross-boundary, or orphan binding with the Tool identity and both relevant paths.

## Outcome

Every independently executable deterministic script has exactly one Tool owner, and every Tool has exactly one canonical executable entrypoint.

## Failure or stop

Do not infer ownership from directory proximity, import topology, or invocation by a Skill; treat ambiguous or multi-owner bindings as blocking findings.
