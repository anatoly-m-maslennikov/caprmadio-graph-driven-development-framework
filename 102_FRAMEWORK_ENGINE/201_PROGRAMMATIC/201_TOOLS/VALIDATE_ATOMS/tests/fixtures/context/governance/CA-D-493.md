---
atom_id: CA-D-493
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Tool/VALIDATE_ATOMS/Result"
  depends_on:
    - "Tool/VALIDATE_ATOMS"
    - "Workflow Run"
    - "Step Run"
    - "Atom/Revision"
    - "Evaluation"
version: 3
updated_at: "2026-09-24 14:07:30 +0000"
relations:
  delivery_for:
    - CA-R-1622
    - CA-R-1623
  relates_to:
    - CA-O-087
---
# Summary

Serialize Atom validator results

## Claim

a `VALIDATE_ATOMS` result **must** use the following closed JSON object, with **every** listed top-level key present.

### Common representations

- String, Path, Integer, Digest, File Binding, **and** Atom Binding follow CA-D-492. missing facts use explicit null **only** where admitted below; never fill them from a filename **or** directory.
- a Span is null **or** an object with positive integer `start_line`, `start_column`, `end_line`, **and** `end_column`; positions are one-based Unicode code-point coordinates, end-exclusive. an unlocatable failure uses null, **not** invented coordinates.
- a Diagnostic has required `code: String`, `severity: error | warning | info`, `path: Path or null`, `span: Span`, `property: String or null`, `authority: list of Atom Binding`, `reason: String`, **and** `evidence: String or null`. it carries bounded relevant evidence **only**, never secrets **or** complete unrelated files.
- an Outcome has required `code: String`, `outcome: passed | failed | not_applicable | not_checked`, `authority: list of Atom Binding`, `reason: String`, **and** `finding_indexes: list of nonnegative Integer` pointing into the result's ordered findings. a failed mandatory check has **>=1** error finding; warnings **and** informational findings alone do **not** fail an Atom.

### Top-level object

| Key | Exact shape |
|---|---|
| `schema_version` | Integer **=1** |
| `result` | `valid`, `invalid`, `incomplete`, **or** `error` |
| `bindings` | object described below |
| `selection` | object described below |
| `coverage` | object described below |
| `carriers` | list of Carrier Assessment below |
| `findings` | list of Diagnostic |
| `currentness` | object described below |
| `execution` | object described below |

### Bindings, selection, and Carriers

- `bindings`: required `methodology: list of Atom Binding`, `action: Atom Binding or null`, `rules: list of Atom Binding`, `context: list of File Binding`, `workflow: Atom Binding or null`, **and** `step: Atom Binding or null`. context records verified digests **when** readable. Workflow/Step bindings are null for direct calls.
- `selection`: required `requested: object or null`, `source_roots: list of Path`, `selected: list of Path`, `excluded: list of Selection Record`, **and** `unresolved: list of Selection Record`. a Selection Record has `path: Path or null`, `atom_id: String or null`, `reason: String`. requested echoes the admitted selector **without** disclosing protected content; malformed unaccepted requests use null.
- a Carrier Assessment has required `path: Path`, `atom_id: String or null`, `version: Integer >=1 or null`, `sha256: Digest or null`, `representation: source | projected | unresolved`, `source_path: Path or null`, **and** `outcomes: list of Outcome`. missing identity, unreadable bytes, **or** unresolved representation remains null/unresolved with an explicit outcome.
- distinguish a logical Atom Revision from its Carriers. faithful source/projected copies share identity but each selected Carrier receives its own fidelity assessment; do **not** diagnose them as two source definitions. two authoritative Carriers claiming the same identity/Revision remain a duplicate-source finding. historical Revisions with different Versions are **not**, by themselves, duplicate identities.

### Coverage and result

- `coverage` has required `targets: object`, `rules: object`, `outcomes: object`, **and** `gaps: list of Diagnostic`.
- targets has nonnegative integer `selected`, `assessed`, `excluded`, **and** `unresolved`; count selected/assessed Carriers, **not** reference-context reads **or** logical identities. assessed counts Carriers with recorded outcomes, **not** necessarily complete coverage.
- rules has nonnegative integer `required`, `supported`, **and** `unsupported`, with required **=** supported **+** unsupported. count distinct applicable mechanical check obligations from the independent source-bound inventory, **not** merely loaded adapters.
- outcomes has nonnegative integer `passed`, `failed`, `not_applicable`, **and** `not_checked`; these equal totals across Carrier Assessments. semantic-only obligations are explicitly excluded from this mechanical denominator with their reason; undecided applicability is a coverage gap, **not** `not_applicable`.
- `error` takes precedence over `incomplete`, which takes precedence over complete `invalid` **or** `valid`. incomplete/error retains known failed checks; it does **not** turn them into passes. `valid` requires a nonempty selected set, complete mechanical coverage, unchanged inputs, **and** no failed checks. warnings alone **may** coexist with `valid`.
- known failures belong **in** findings; incomplete obligations belong **in** gaps. avoid duplicating the same record **in** both; use an Outcome's reason **to** explain a blocked check.

### Currentness, execution, and ordering

- `currentness` has required `state: unchanged | changed | unverified` **and** `affected_inputs: list of File Binding`. membership changes are recorded through the affected inventory-root Path; unchanged requires membership **and** relevant content verification.
- `execution` has required `limits: object`, `limit_sources: object`, `stopped_by: String or null`, `diagnostics: list of Diagnostic`, **and** `run_context: object`. effective limit names/values follow CA-D-492; limit_sources maps those names **to** `request`, `instance`, **or** `default`. unavailable pre-validation limits use empty objects. stopped_by is a limit key **or** null. run_context carries **only** admitted input identifiers; no generated timestamp **or** random ID is required.
- sort Carriers/selection lists by normalized absolute path; sort authority bindings by Atom ID, Version, path, **and** digest. sort diagnostics by path, span start/end, code, property, severity, **and** reason, with null before non-null values; deduplicate identical diagnostics. sort Outcomes by code **and** ordered authority bindings. use Unicode code-point order, **not** locale-dependent order. assign finding indexes **after** sorting.
- map results **to** process exits: `valid = 0`, `invalid = 1`, `incomplete = 2`, `error = 3`. malformed requests return this same error envelope with available diagnostics, zero unexecuted counts, empty unexecuted lists, null unavailable bindings, **and** currentness unverified; do **not** fabricate assessments.
