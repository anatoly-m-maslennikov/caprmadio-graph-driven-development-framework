---
cce_version: cce_1
cce_form: obligation
subjects:
  - carrier-format
version: 6
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-457--job-based-carrier-policy
    - CAPRMEDIO-GOV-METH-024--toml-optional-unset-normalization
    - CAPRMEDIO-GOV-METH-025--json-schema-boundary
    - CAPRMEDIO-GOV-ANRP-018--artifact-carrier-format-policy
  relates_to:
    - CAPRMEDIO-GOV-CNST-001--github-preview-compatibility
  child_of:
    - CA-R-1054
---
# Select carriers by their governed job

Every governed Markdown artifact starts with valid YAML frontmatter containing its applicable non-derived properties. Frontmatter is non-empty, does not duplicate narrative body content, and does not repeat semantic route coordinates already determined by the registered artifact type.

CAPRMEDIO uses these default carrier boundaries:

| Carrier | Governed job |
|---|---|
| Markdown with YAML frontmatter | Human-governed Atoms and narrative Projections |
| Markdown without frontmatter | Narrative documentation, reports, and other human-readable native material that is not an Atom or Journal |
| TOML | Default for every CAPRMEDIO-owned, non-Atom, non-Journal structured technical carrier intended for deterministic technical consumption or maintenance, including version declarations, settings, maps, and structured technical Projections |
| YAML | Atoms with a registered YAML carrier, or a non-Atom technical carrier whose required branching, anchors, tags, multi-document structure, or host-ecosystem contract cannot be represented adequately in TOML |
| JSON | External contracts, standardized schemas, wire data, or generated machine data whose interoperability or consumer contract requires JSON |
| NDJSON | Append-only Journals and ordered record streams under the applicable `.caprmedio` role folder |
| Native format | Source code, Tests, Evaluations, CI workflows, lockfiles, host manifests, and other prescribed implementation files |

Carrier selection follows the artifact's primary authoring and consumption boundary, not its layer or implementation language. Atoms and Journals follow their own registered carrier rules. For everything else CAPRMEDIO owns, TOML is the default whenever the file contains structured technical state that should be read deterministically by Tools, LLMs, or other software while remaining directly maintainable by humans.

A different structured carrier is permitted only when a required feature or binding external contract makes TOML inadequate; familiarity or existing usage alone is not sufficient. The governing Requirement or registered carrier definition records that reason. A binding standard, ecosystem, or external obligation keeps its prescribed format and does not gain a parallel writable representation.

Markdown frontmatter uses `---`. Markdown does not carry structured technical state merely to make that state human-readable. Standalone YAML does not replace TOML for technical state when TOML is sufficient. Embedded source examples are content rather than separate artifacts.
