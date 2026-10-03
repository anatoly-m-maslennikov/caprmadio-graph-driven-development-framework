# VALIDATE_ATOMS first golden slice

This is a prepared, deliberately incomplete test corpus for CA-P-1112. Its
25 manifest cases exercise malformed public requests against CA-D-492@3 and
CA-D-493@3. They now run against the delivered implementation, never a mock validator.

Run from the repository root with the pinned environment:

```sh
.caprmedio_tmp/implementation/validate-atoms-20260924/venv/bin/python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/tests -p 'test_validate_atoms_e2e.py' -v
```

Every case invokes the real delivered command twice, once with a request file
and once through stdin. The harness relocates the literal `/__fixture__` prefix
to a fresh isolated tree under `.caprmedio_tmp`, compares the entire handwritten
expected report, independently checks closed report shapes and coverage
accounting, and fingerprints the tree before and after each call. It imports no
implementation modules. A missing executable fails; nothing is skipped.
If the host denies deletion of its temporary directories, the harness warns
and retains the isolated run tree; cleanup cannot mask the command assertion.

The JSON reports and requests were authored from the source contracts, not
captured from implementation output. The stable malformed-request diagnostic
is `REQUEST_INVALID` with reason `Request does not conform to CA-D-492.`; these
unaccepted requests have empty execution bindings, null requested selection,
unverified currentness, and zero unexecuted counts. Source authority copies are
byte-exact; `source_bindings.json` records their original paths and digests.

The `/__fixture__` prefix is a test transport placeholder, not a new request
field or semantic permission. Requests are invalid before candidate discovery,
so they intentionally need no target Atom tree. Only harness setup writes the
isolated tree; source fixture bytes are never modified.

## Coverage and completion limits

Covered now: malformed JSON shape, duplicate keys, non-finite numbers, missing
and unknown fields, unsupported versions, Boolean/integer confusion, relative
and duplicate roots, invalid selectors and statuses encoding, nulls, unknown
nested fields, invalid limits, malformed digests, and executable bundle keys.

This slice does **not** satisfy the complete CA-P-1112/CA-E-515–518 gate.
Additional tests now exercise good/bad mock carriers, primitive encodings,
retired fields, body sections, authority gaps, selected tiers, projections,
protected reads, settings fallback, read budgets, and currentness. Independent
review regressions cover gap attribution, false projection fidelity, numeric
coercion, access-time changes, and directory-descriptor reads.
Pending work includes complete per-obligation positive/negative/boundary golden
reports, full extensible admission/reference/placement checks, all budget/race
combinations, and Unicode spans/order.
The manifest is not a claim that these obligations disappeared: the independent
source evaluations copied under `fixtures/context/governance/` retain them.

A fully valid aggregate case is currently authority-blocked: the source review
did not find normative admission for the generic `Requirement` Type or a
settled Actor/Subject registry encoding. Good supported subchecks must retain
an incomplete aggregate when those obligations are unresolved. The tests must
not invent an admission schema or shrink the authority frontier to force green.

The initial missing-command baseline failed before implementation. The original
89-test slice included 25 golden request cases through file and stdin invocation.
The expanded corpus adds exact supporting authority fixtures, positive/negative
schema and domain cases, bounded reference resolution, revision ambiguity,
projection/source coalescing, graph cycles, structure and placement, Plan override
inheritance, and additional real CLI good/bad carrier tests. Fixtures are frozen
under `tests/fixtures/`, not read from the live methodology. Source edits invalidate
the corresponding pin rather than silently changing expected behavior.

The CLI integration tests assert 49 supported adapters out of 51 known obligations
under the exact inventory, while retaining the two Actor-identity gaps and an
`incomplete` aggregate. They verify read-only fingerprints and coexistence of
independent findings with unresolved context. This is evidence for the supported
slice, not completion of the full acceptance gate.
