# VALIDATE_ATOMS

Read-only implementation of the **Check Atoms** Action (CA-O-087).

## Current readiness

This is an initial, conservative implementation, **not a complete conformance gate**.
It reports supported checks and known failures, but returns `incomplete` while
methodology composition, schema admission, Actor/Entity references, placement,
or another required rule cannot be established. It currently cannot certify a
complete `valid` or `invalid` assessment. An incomplete result is not a pass.

Implemented boundaries include strict JSON request/result models (Pydantic),
bounded safe YAML parsing (PyYAML), duplicate keys, protected paths, no-follow
filesystem reads, independent settings fallback, carried-property selectors,
source revision/digest-bound checks, byte-preserving projection comparison,
duplicate source revisions, deterministic diagnostics, and input currentness.

Twenty additional adapters cover the supported cases of the previously missing
checks. With the exact reviewed source inventory, 50 of 51 known obligations have
adapters; `plan.assignee_resolution` is intentionally deferred by the Operator.
Author resolution is exact Operator registry membership. This count describes adapter
availability, not complete coverage on an individual Atom.

| Group | Checks added |
| --- | --- |
| Schema | Permitted properties, qualified domains, single property location, body properties, quoted timestamps, common Plan structure |
| References | Atom targets, governed Entity paths, legacy Subjects encoding, Plan blocking and decomposition |
| Structure | Owner and target, tiers, qualified statuses, status placement, filename/carrier consistency |
| Context | Retry domain, confidence inheritance/defaults, source-bound projection fidelity |

Checks use explicit carried properties and exact source bindings. A filename or
folder never supplies a missing Atom property. Address and placement checks only
compare known carried values against an admitted representation rule. Unknown
properties fail only with a complete reviewed admission inventory; unresolved
extension declarations remain gaps. Plan checks are structural, not a semantic
claim that a Plan has one indivisible Claim.

Body checks follow CA-D-479 v6: literal `# Summary` and the required,
ordered sections for each supported Content Role. They check section cardinality,
nesting, nonempty values, and duplicate frontmatter properties; fenced examples
are not headings. RMED requires nonempty `## Scope`, nonempty `## Claim`, then
`## Details`; empty Details is allowed. Scope/Claim meaning and Subject confinement
still require semantic evaluation, not heading recognition. Plans follow CA-D-470 v7:
`## Objective`, `## Details`, and one nonempty `### Definition of Done` inside
Details. A Content Role without a reviewed body contract remains a coverage gap.
An absent Summary produces one missing-property diagnostic; an existing but
misplaced Summary still fails placement. Missing layout is not also reported as
a semantic Claim defect by this mechanical checker.

CA-D-268 requires deterministic canonical relation ordering but does not define
its comparator. The checker therefore reports a coverage gap for multi-target
lists rather than inventing lexical sorting, even when a list happens to be
lexically sorted. Endpoint, role and uniqueness checks continue independently.

## Run

Requires Python 3.14 and the `validate-atoms` dependency group in the repository's
`pyproject.toml`. Development checks use `validate-atoms-dev`.

```sh
uv sync --group validate-atoms --group validate-atoms-dev
uv run --group validate-atoms python \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms.py \
  --input /absolute/path/request.json
```

`--input -` reads JSON from stdin. Exactly one JSON report goes to stdout.
Exit codes: `0 valid`, `1 invalid`, `2 incomplete`, `3 error`.
Request and result authority: CA-D-492 and CA-D-493. No request content is executed.

```json
{
  "schema_version": 1,
  "source_roots": ["/absolute/project/atoms"],
  "allowed_read_roots": ["/absolute/project"],
  "methodology": {
    "kind": "sources",
    "roots": ["/absolute/project/methodology_sources"]
  },
  "selection": {
    "atoms": [{"carrier_path": "/absolute/project/atoms/example.md"}]
  },
  "default_settings": {"path": "/absolute/project/default_settings.toml"}
}
```

The five `[atom_validation]` limits resolve independently from request overrides,
then Framework Instance Settings, then explicitly selected Default Settings.
Default settings auto-location is not implemented. Host safety ceilings remain
upper bounds. Ordinary Scope Unit/tier selectors default to active status;
explicit Atom selectors do not add a Status filter. No Atom property is inferred
from its filename or placement. Scope Unit selection requires Project Structure.

`reference_roots` supply bounded context without adding validation targets. They
are needed for reference uniqueness checks. Missing, malformed, inaccessible, or
ambiguous references remain explicit gaps; independent carrier checks still run.
With explicit roots, already-read validation targets are only a cache: they join
reference context only when their paths belong to that frontier. Independently
admitted methodology sources remain included. Distinct carriers with the same
ID are not silently deduplicated. Without roots, available context is partial.
Active RMED target admission can distinguish an Active revision from retained
history. Plan history is not resolved by guessing the highest Version. Faithful
projected copies do not create additional authoritative identities.

Supply `operators_registry: {"path": "/absolute/project/operators_registry.toml"}`
for Author checks (optional SHA-256 pin supported). The registry is authoritative,
not generated from Atom authors. Its only root key is a nonempty `operators` array
of tables, each containing exactly `name` and `role` nonblank strings. Names must
be unique. Example:

```toml
[[operators]]
name = "Example Operator"
role = "project owner"
```

The carried `author` must exactly match one registered name. Unknown names fail;
missing, malformed, inaccessible, or stale registry context leaves membership
incomplete. No case folding, whitespace trimming, aliases, extra identity lookup,
or inferred permissions are applied. The registry is fingerprinted and included
in input-currentness checks. Assignee resolution is not performed for now.

For legacy **authority inputs** without carried identity/status, an exact
`methodology.frontier` binding can enable conditional checks, but leaves admission
incomplete. This never supplies missing properties on validation targets.

## Verification and remaining coverage

```sh
uv run --group validate-atoms --group validate-atoms-dev python -m unittest discover \
  -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/tests
uv run --group validate-atoms-dev ruff check \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS
uv run --group validate-atoms-dev mypy --no-incremental --cache-dir=/dev/null \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS
```

Tests include independently authored JSON golden reports, good/bad mock carriers,
byte-exact source fixtures, actual CLI subprocess calls, read-only fingerprints,
unsafe inputs, and targeted regressions. Test fixtures are created only beneath
`.caprmedio_tmp`; the command creates no files or bytecode. Host-denied cleanup
leaves fixture directories there and emits a warning.

Remaining work includes complete source composition/admission, deferred Assignee
resolution, unsupported extension Property contracts, full address/placement rules, executable
coverage of every rule/boundary, and a complete-positive golden report. Supplied
Rule Bundles are currently reported as unsupported, never executed. YAML aliases,
merge keys, and unsupported projection binding encodings produce visible gaps.
Source spans are currently null; the command does not invent coordinates.

Known conditional gaps also include Project/Operator ownership without identity
context, qualified model overrides not covered by reviewed adapters, non-Plan
placement without its complete mapping, and legacy Subject migration evidence.
The separately unclassified source obligations have not been blanket-exempted.

CA-P-1106 and its child Plans remain Active. No full-acceptance claim is made.
