# Remove retired Atom properties

`remove_retired_atom_properties.py` is a bounded migration helper. Its pure
transformer only removes top-level `cce_form`, `cce_version`, and `llm_session_ids`
YAML properties. The CLI additionally performs the required revision lifecycle:
increment the carried Version by one and preserve the complete prior bytes in
the sibling `archive/<stem>@<prior-version>.md` file. `updated_at`, status,
identities, every other field, and Markdown bodies remain byte-for-byte intact.
Journal/governed change-set orchestration remains the caller's job.

Use the approved `validate-atoms` runtime dependency group (PyYAML 6.0.3), with the
same Python environment used for `VALIDATE_ATOMS`:

```sh
uv run --group validate-atoms python \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/migrations/remove_retired_atom_properties.py \
  --report /absolute/path/validation.json \
  --source-root /absolute/path/source-atoms \
  --output /absolute/path/new-migration-plan.json
```

This default dry-run reads only the report's explicitly selected carriers. It
selects `PROPERTY_RETIRED` findings for the three exact property names, verifies
every selected carrier's report SHA256, and writes a plan. Paths must identify
Markdown source files beneath `--source-root`. Symlinks, multiple hard links,
`.env` paths, and history/archive/draft/status directories are refused. Other properties
or diagnostics never become implicit migration targets.

The plan contains `baseline` bindings for all selected carriers, `changes` with
path, before/after SHA256, complete reversible UTF-8 `before`/`after` text,
`removed` property names, prior `version`, `after_version`, `archive`,
`archive_sha256`, `blockers`, and counts. A stale/missing/unsupported
carrier creates a blocker; a plan with blockers cannot be applied. Exit code 0
means the plan or apply succeeded; 2 means blocked/invalid input or an IO error.
An incomplete validator report may still supply exact source carrier bindings;
this helper makes no claim of complete Atom conformance.

Review the plan, then apply that exact file:

```sh
uv run --group validate-atoms python \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/migrations/remove_retired_atom_properties.py \
  --apply /absolute/path/new-migration-plan.json \
  --output /absolute/path/new-migration-receipt.json
```

`--output` is optional for apply (the receipt otherwise goes to stdout). Output
files must be new and their parent directories must already exist. Apply never
discovers or recurses over source files. It validates the plan's exact permitted
transformation, preflights every source baseline and archive before writing,
then saves the exact prior revision, rechecks each carrier immediately before
replacement, and reads it back afterwards. Sources are replaced atomically from
a sibling temporary file after fsync, preserving the original permission mode.
The last check verifies both the source inode and SHA256 through no-follow file
descriptors. Existing matching archives are reused;
conflicting archives block the plan/apply. A concurrent
change or IO failure after writes begin can stop a partially applied batch; the
plan retains the full original bytes, and rerunning it skips exact after-states.
It is not a multi-file transaction and should run under the caller's exclusive
mutation context. Unchanged baseline carriers are never written.
An existing receipt/output path is rejected before any source/archive mutation.

Applying the same plan twice is idempotent: exact after-states are reported as
`already_applied`. Regenerate validation after applying; its next dry-run has no
changes. A stale report is rejected, even if the carrier happens to have no
retired keys now; it cannot silently replace a completed migration's state.

The pure importable API is
`remove_retired_properties(raw: bytes) -> tuple[bytes, list[str]]`. It uses safe
YAML node locations, not whole-document serialization. Scalars, quoted keys,
block/flow list values, multiline values, Unicode and CRLF are supported. Nested
lookalike keys and all body bytes are preserved. Duplicate keys, merges, YAML
anchors/aliases, custom tags, top-level flow mappings, and explicit/indented or
multiline top-level keys are rejected with `MigrationError`. Comments outside
removed value syntax are retained. A semantic check ensures every retained YAML
node stays identical after surgery. No additional libraries are required.
