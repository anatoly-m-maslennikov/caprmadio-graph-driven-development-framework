+++
artifact_subtype = "governance"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]

[scope]
kind = "project"
id = "dset-specs-loops-framework"

[[relations]]
type = "projection_of"

[relations.range]
semantic_type = "decision"
layer = "gov"
through = "CAPRMEDIO-ATOMIC-RECORD-210"

[relations.range.scope]
kind = "project"
id = "dset-specs-loops-framework"

[[relations]]
type = "projection_of"

[relations.range]
semantic_type = "qa"
subtype = "test_plan"
layer = "gov"
through = "CAPRMEDIO-ATOMIC-RECORD-211"

[relations.range.scope]
kind = "project"
id = "dset-specs-loops-framework"

[[relations]]
type = "projection_of"

[relations.range]
semantic_type = "qa"
subtype = "evaluation_plan"
layer = "gov"
through = "CAPRMEDIO-ATOMIC-RECORD-115"

[relations.range.scope]
kind = "project"
id = "dset-specs-loops-framework"

[[relations]]
type = "projection_of"

[relations.range]
semantic_type = "decision"
layer = "gov"
through = "CAPRMEDIO-ATOMIC-RECORD-078"

[relations.range.scope]
kind = "layer"
id = "gov"

[[relations]]
type = "projection_of"

[relations.range]
semantic_type = "qa"
subtype = "test_plan"
layer = "gov"
through = "CAPRMEDIO-ATOMIC-RECORD-079"

[relations.range.scope]
kind = "layer"
id = "gov"

[[relations]]
type = "projection_of"

[relations.range]
semantic_type = "qa"
subtype = "evaluation_plan"
layer = "gov"
through = "CAPRMEDIO-ATOMIC-RECORD-080"

[relations.range.scope]
kind = "layer"
id = "gov"

[[relations]]
type = "projection_of"

[relations.range]
semantic_type = "decision"
layer = "tool"
through = "CAPRMEDIO-ATOMIC-RECORD-170"

[relations.range.scope]
kind = "layer"
id = "tool"

[[relations]]
type = "projection_of"

[relations.range]
semantic_type = "decision"
layer = "implementation"
through = "CAPRMEDIO-ATOMIC-RECORD-201"

[relations.range.scope]
kind = "layer"
id = "implementation"

[[relations]]
type = "projection_of"

[relations.range]
semantic_type = "decision"
layer = "ops"
through = "CAPRMEDIO-ATOMIC-RECORD-175"

[relations.range.scope]
kind = "layer"
id = "ops"
+++

# Methodology projection set

This evergreen carrier binds the current project and layer semantic frontiers
to the package fragments that compile them:

- Behavior specification: `080_dset-gov-specification-methodology.md`
- Deterministic Test case: `CAPRMEDIO-GOV-plan-tests.md`
- Qualitative Evaluation case: `CAPRMEDIO-GOV-plan-evaluations.md`
- TOOL executable specification: `CAPRMEDIO-TOOL-REFERENCE-specification-methodology.toml`
- IMPL profile and methodology specifications: `CAPRMEDIO-REALIZATION-REFERENCE-profile-local-python-tools.toml`
- OPS operational specification: `CAPRMEDIO-FIELD-REFERENCE-specification-methodology.toml`

It owns projection metadata only. The linked fragments own their respective
compiled content, and the immutable atoms own authority and QA definitions.
