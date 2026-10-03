# Repair candidate component

## Current local profile (contract 6)

The current prompts use `atom_local`: local Properties, CCE and
Scope/Claim/Details/Summary only. Supply one candidate and the compact local rule
pack. Independently review proposed and saved output under the same profile,
and compare information preservation. No Entity/Subject resolution, graph
audit or affected-reference scan is required for same-identity local repairs.

CA-R-1432 distinguishes a Summary value from lossless serialization. The repair
gate permits balanced strong-markup changes that preserve every visible word,
case, space and punctuation mark; this supports required operator bolding without
replacing the Atom. It does not normalize links, code, HTML, escaped characters,
or unsupported emphasis. Actual Summary-value changes still require replacement,
and every admitted proposal still needs an independent change assessment.

`repair_gate.admit_proposal` accepts contract 6 without broadening its permission
boundary. Subject and relation targets must remain unchanged; unambiguous
encoding normalization can preserve the same target values. Replacements,
splits and path changes are rejected for a separate authorized run. `candidate`
never grants source mutation or establishes conformance.

For a legacy single-H1 R/M/D Carrier whose only coverage gaps are missing
registered body sections, `layout_repair_gate.admit_layout_recoding` also accepts
matching contract-6 local reviews. It requires a complete independent final
evaluation, exact lossless title/Claim mapping, equivalent Scope assessment,
unchanged graph targets and same path. Compact local packets need no unrelated
graph resources. Non-layout gaps, changed Claim text, Summary, or identity still
block this narrow entry point. The original failed/blocked report is retained;
successful preview admission is not permission to write or a saved-source pass.

The detailed contract-5 notes below describe historical full-audit callers.
Their affected-reference obligations are not extra checks in the local pass.

## Historical full-audit profile (contract 5)

This is a preview-only component for CA-O-107, not a source-writing Tool and not
an alternative authority. Use the bound CA-O-107, CA-O-067, CA-R-1432, CA-R-1464,
CA-R-1766, CA-R-1700, CA-D-276, CA-D-283 and CA-D-496
texts together with the current evaluation authority and caller permissions.

1. Supply the full context, input freshness evidence, permissions and any reserved
   successor identities to `propose_repair.prompt.md`. Its disposition is provisional.
2. After generation, independently assess the exact output under CA-O-067.
   Have the caller bind that assessment and its own preflight evidence, then validate the candidate
   using `repair_gate.admit_proposal(evaluation, proposal,
   context=review_context, permission=caller_permission,
   preflight=caller_preflight)`.

Output-bound assessment and preflight follow generation; requiring them before
the output exists would create a circular dependency. They remain mandatory for
admission. The generator cannot supply its own independent assessment.
3. Keep the proposal and its original source binding as retained evidence.
4. Independently evaluate the full final output text under newly bound candidate
   context; require zero findings and coverage gaps. Check that no original
   necessary information was lost.
5. Only the parent repair Action may subsequently authorize history, reference
   maintenance and source mutation under fresh inputs and exact permissions.
   After an authorized write, independently evaluate the actual saved source
   and check affected active references before reporting `verified`.

`candidate` never means `verified`. The gate always returns
`source_mutation_permitted: false`. It rejects incomplete evaluations,
source/context mismatches, missing finding resolutions, malformed permissions,
unsafe paths, incomplete carried identities, same-ID Summary changes, formatting
changes that alter non-timestamp frontmatter, unchanged, invalid or non-advancing
timezone-bearing `updated_at`, and absent or mismatched caller preflight. A
`recoding` keeps Atom ID, Version, Summary and the complete Markdown body,
refreshes only `updated_at`, and may only delete a
Requirement, Method or Delivery `type` whose value exactly repeats its
`content_role`. A `revision` may compose that same deletion with other repairs,
subject to an independent original-to-final assessment. For either disposition,
the only admitted path change removes the matching uppercase role token
(`-REQUIREMENT`, `-METHOD` or `-DELIVERY`) immediately before the first `--`
in the basename; every other path piece stays identical, the role stays the
same, and the final `type` field is absent. Both the original and renamed paths
require exact caller permission. No other same-ID rename or genuine Type change
is admitted. Isolated recoding still rejects every other metadata or body
change. Formatting likewise refreshes only `updated_at`. The gate does not prove semantic preservation, assess CA-O-067, reserve IDs, resolve
filesystem symlinks, evaluate the new text, write source files, record history
or commit. Those remain caller obligations.

Permission is a separate caller-owned mapping:

```json
{
  "paths": ["relative/source.md", "relative/authorized-successor.md"],
  "dispositions": ["revision", "replacement"],
  "provenance": "Exact Operator instruction or admitted delegation"
}
```

All candidate paths must occur in that exact list, including the original source.
The original evaluation and raw parts are checked together, not trusted from
an editable summary status.

The caller-owned preflight must agree exactly with the requested candidate;
the gate verifies agreement but does not establish the claimed facts:

```json
{
  "source": {"path": "relative/source.md", "atom_id": "CA-R-1", "version": 1, "sha256": "..."},
  "context_sha256": "...",
  "provenance": "Caller re-read current bindings and authority",
  "attempt": 0,
  "retry_budget": 0,
  "identity_assessment": {
    "source": {"path": "relative/source.md", "atom_id": "CA-R-1", "version": 1, "sha256": "..."},
    "context_sha256": "...",
    "classification": "refinement",
    "outputs": [{"path": "relative/source.md", "atom_id": "CA-R-1", "version": 1, "sha256": "..."}],
    "provenance": "External CA-O-067 assessment"
  }
}
```

`attempt: 0` is the initial candidate, not a retry; both retry values are
nonnegative integers and `attempt` cannot exceed `retry_budget`. For a
`replacement` or `split`, add `successor_reservations` with the exact output
`bindings`, nonblank reservation `provenance`, and a nonblank
`history_reference_plan`. Permission does not replace any preflight field, and
these fields are not generated inside the proposal.

The fixer disposition and the CA-O-067 semantic change class are separate:

| Fixer disposition | Admitted CA-R-1432 assessment class |
| --- | --- |
| `formatting` | `carrier_only` |
| `recoding` | `carrier_only` |
| `revision` | `refinement` or `semantic_revision` |
| `replacement` | `replacement` |
| `split` | `replacement` |

The independent assessment must use the canonical class, not copy the fixer
operation name. Agreement with this table does not prove the assessment true.
For a `revision`, that external class drives Version: `refinement` retains it;
`semantic_revision` increments it by exactly one. Every output must instead
carry a valid, later, different timezone-bearing `updated_at`; the gate does
not invent dates or certify wall-clock freshness.

Temporary transformations may compose without changing source. Admit only the
single complete original-to-final proposal, resolving every original confirmed
finding exactly once; there is no deferred-finding admission protocol and any
coverage gap still blocks. Temporary states are retained evidence, not mutation
candidates or verification results. A composed role-echo deletion plus content
or Subject repair uses `revision`: independently assess the entire original-to-final
delta as `refinement` or `semantic_revision`. Do not reuse an intermediate
`carrier_only` assessment or label the composition `recoding`. The narrow isolated
recoding contract remains byte-strict. Neither admission nor a temporary passing
evaluation proves that source, history or affected-reference checks have passed.

Run the tests from the repository root using the VALIDATE_ATOMS environment:

```sh
python -m unittest discover -s 102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW/repair -v
```

The tests exercise admission behavior, not LLM correctness. The prompt still
needs an independent semantic repair replay before production source use.

## Independently evaluated carrier corrections

Two explicit entry points admit narrowly bounded `carrier_only` compositions
without changing the ordinary `admit_proposal` dispositions:

- `layout_repair_gate.admit_layout_recoding`: disposition `layout_recoding`.
  Requires an exact lossless legacy-H1 section map, independently assessed
  equivalent Scope, preserved Claim and Summary, unchanged Version, and only
  original `layout_dependency` gaps resolved by a complete passing final review.
- `subject_repair_gate.admit_subject_recoding`: disposition `subject_recoding`.
  Requires a confirmed Subjects finding and an actual DEPENDS_ON correction;
  the complete Markdown body, GOVERNS, Version and all other frontmatter bytes
  stay unchanged except a refreshed timestamp and optional ordinary role-echo
  Type omission. Any original coverage gap blocks. Subjects must use a simple
  block mapping; DEPENDS_ON may use a block or flow list. Ambiguous encodings,
  aliases, tags, actual Type changes and unrelated renames are rejected.

Both take original `evaluation`, `proposal`, exact caller `permission` and
`preflight`, plus `context` and `final_context` as complete frozen packet
dictionaries and `final_evaluation` with its raw parts. Layout admission also
takes `section_mapping`. Original and final reports are validated separately;
every original confirmed finding still requires exactly one supported resolution.
The final output must pass all ten checks with no findings or gaps.

Preflight binds the original source, both context hashes, exact output binding,
retry budget and caller provenance. Its independent identity assessment uses
those same bindings, `classification: carrier_only`, `independent: true` and
confidence at least 0.99 and both caller thresholds. `final_review` separately
binds the final source/context and canonical JSON evaluation SHA-256 with its
independence/provenance. `freshness` binds the original source and
`layout_repair_gate.authority_digest(context)` with caller re-read provenance.
`authority_aliases` explicitly maps unchanged original authority bindings to
their final-context snapshot paths; all authority bytes, keyed control resources
and applicable Principles must remain consistent. These checks validate evidence
agreement; the caller remains responsible for genuine freshness and independence.

Neither gate coerces a carrier-only change into refinement or increments Version
to fit another operation. Both return only `candidate` with
`source_mutation_permitted: false`, retain original/final report hashes, and
require independent saved-source and affected-reference verification after any
subsequently authorized write. Isolated recoding remains byte-strict.

## Temporary layout proposals

`layout_preview.admit_layout_preview()` is a separate pure validator for a
caller-constructed temporary proposal, not a route around `admit_proposal()`.
It accepts only a simple legacy body with one initial H1 and no later headings:

- the exact initial H1 value becomes Summary, never a value from a filename; this layout migration preserves the carried Atom ID and does not itself change Summary meaning;
- all remaining body text is carried verbatim into Claim;
- Scope is supplied explicitly by the caller, with provenance, and remains an
  unassessed proposal—not a derived fact or an equivalence assertion;
- Details is empty; the complete frontmatter and carried identity stay intact.

The exact source digest, body spans, proposed Scope, and output text must agree.
Complex legacy layouts are rejected instead of guessed. The result is only
`preview`, is unclassified, and always has `source_mutation_permitted: false`.
Missing Principles or other authority remain missing. Independent full
evaluation, preservation review, and CA-O-067 classification are still needed;
normal repair admission and its unresolved-coverage prohibition are unchanged.
This component creates no files and does not wire an automatic Workflow step.

### Exact simple-exclusion extraction

`scope_extraction_preview.admit_scope_extraction_preview()` is candidate-only. It
recognizes only the ASCII grammar `**every** BEARER other than EXCLUSION **must**
PREDICATE.` and moves that exact selector into Scope. The map binds source and
proposed body hashes, literal selector text, and exact Summary, Scope, Claim and
Details spans. Compound, conditional and non-ASCII selectors fail closed. It
makes no semantic-equivalence claim.

`scope_extraction_repair_gate.admit_scope_extraction_subject_recoding()` requires
the preview, a real constrained `depends_on` delta, full original and final
reports, final authority freshness, and independently supplied Scope and identity
evidence. It admits only original Subjects defects directly repaired by the
declared-subject delta, finite canonical `CA-D-479` heading omissions, or an exact
ordinary role-echo Type line removed from frontmatter. A passing final report
cannot withdraw any other original finding. It returns only `candidate` with
`source_mutation_permitted: false`.

The temporary preview preparer keeps its existing default when no fourth JSON
argument is supplied. Its optional fourth configuration has the constrained shape
`{"CA-R-...":{"kind":"simple_exclusion"}}`; the normal Scope map must repeat the
syntactically derived selector plus period exactly. This config prepares a
temporary candidate and exact map only; it neither proves Scope equivalence nor
authorizes a source write.
