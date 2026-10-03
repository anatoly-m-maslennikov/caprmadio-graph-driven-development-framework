---
artifact_subtype: implementation_decision
subject_scopes:
  - carrier-format
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: resolution_of
    targets:
      - CAPRMEDIO-GOV-CNFL-001--all-toml-carrier-conflict
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-METH-013--immutable-atoms-and-role-aware-conflict-handling
      - CAPRMEDIO-GOV-METH-026--native-package-successors
      - CAPRMEDIO-GOV-METH-027--legacy-structured-snapshots
---

# Decision — Preserve immutable semantics through TOML carrier migration

An emitted atomic artifact keeps an immutable semantic identity and record:
its stable IDs, Type and subtype, claim or QA definition, authority, acceptance
state, scope, provenance, rationale, relations, and Markdown body content do not
change. Carrier bytes and filename extensions are representation, not semantic
identity.

An explicit operator-authorized representation migration may change those
bytes only when one deterministic transaction:

- parses the old carrier and the proposed TOML carrier into the same normalized
  semantic value, including explicit reconstruction of YAML nulls;
- records old and new paths, whole-file digests, normalized-semantic digests,
  carrier IDs, governing Decision, timestamp, source Git blob return address,
  declared loss, and LLM session IDs in
  `dset/scopes/gov/migrations/carrier-transitions.toml`;
- updates atom seals, legacy selector seals, artifact classification, retained
  links, generated views, and the bootstrap bundle in the same validated
  transaction;
- rejects missing inputs, collisions, unsupported values, semantic drift,
  partial resealing, stale evidence, or rollback mismatch; and
- becomes a no-op after the committed cutover.

Markdown artifacts keep their paths and bodies while YAML frontmatter becomes
TOML frontmatter. A historical standalone YAML file moves to an adjacent
`<stem>.legacy.toml` envelope because its sibling `<stem>.toml` already owns
current truth. The envelope records the original path and digest and stores a
lossless TOML payload plus explicit null paths. Readers never treat the
historical envelope as current authority.

After cutover, `dset/` contains no `.yaml` or `.yml` artifact carriers and no
Markdown YAML frontmatter. Standards-compliant JSON Schema, GitHub Actions,
host skill metadata, ecosystem manifests, wire formats, and runtime journals
retain externally prescribed formats because they are not CAPRMEDIO-owned artifact
encodings.

This Decision fully replaces `CAPRMEDIO-GOV-METH-013--immutable-atoms-and-role-aware-conflict-handling`,
`CAPRMEDIO-GOV-METH-026--native-package-successors`, and `CAPRMEDIO-GOV-METH-027--legacy-structured-snapshots`. It carries forward the
still-applicable semantic immutability, append-only lifecycle, explicit and
acyclic replacement/absorption, role-before-priority conflict classification,
universal-priority, retirement, and stable-lookup consequences. Their current
independent owners—especially `CAPRMEDIO-GOV-METH-020--priority-profile` and
`CAPRMEDIO-REQUIREMENT-GOV-020..026`—remain active. Only permanent byte identity and
retained YAML are withdrawn; historical package and structured data remain
preserved through TOML envelopes and the transition ledger.

This emitted Decision atom is immutable. Later correction requires a successor
Decision and append-only lifecycle event.

## Primary claim

Atomic semantics and identity are immutable, but an explicitly authorized lossless carrier migration may convert every CAPRMEDIO-owned YAML artifact carrier to TOML under one transactional old-to-new digest ledger.

## Rationale

Carrier encoding is not the project claim itself; preserving semantic values, stable IDs, provenance, relations, body content, and a verifiable transition map retains history without keeping YAML in the current repository.
