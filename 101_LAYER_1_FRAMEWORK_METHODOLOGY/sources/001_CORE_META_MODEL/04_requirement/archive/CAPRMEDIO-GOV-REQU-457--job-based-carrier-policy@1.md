---
subject_scopes:
  - carrier-format
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-451--all-markdown-artifacts-have-frontmatter
      - CAPRMEDIO-GOV-REQU-453--artifact-carrier-format-policy
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-CNST-001--github-preview-compatibility
---

# Requirement — Select carriers by their governed job

Every governed Markdown artifact starts with valid YAML frontmatter containing
its applicable non-derived properties. Frontmatter is non-empty, does not
duplicate narrative body content, and does not repeat semantic route
coordinates already determined by the registered artifact type.

DSET uses these default carrier boundaries:

| Carrier | Governed job |
|---|---|
| Markdown with YAML frontmatter | Human-governed atomic and maintained artifacts with narrative meaning |
| TOML | Human-edited configuration executed directly by tools |
| JSON | External contracts, standardized schemas, wire data, and generated machine data |
| NDJSON | Append-only journals and ordered record streams under `.caprmedio_journal` |
| Native format | Source code, Tests, Evaluations, CI workflows, lockfiles, host manifests, and other prescribed implementation files |

Carrier selection follows the artifact's authoring and consumption boundary,
not its layer or implementation language. A binding standard, ecosystem, or
external obligation keeps its prescribed format and does not gain a parallel
writable representation.

Markdown frontmatter uses `---`. YAML is not a standalone DSET artifact format.
Embedded source examples are content rather than separate artifacts.

## Primary claim

DSET uses Markdown with YAML frontmatter for human-governed artifacts, TOML for
executable human configuration, JSON for standardized machine boundaries,
NDJSON for append-only journals, and native formats for implementation.

## Rationale

The merged carrier policy gives every Markdown artifact a uniform readable
envelope while reserving each structured format for the job it serves best.
