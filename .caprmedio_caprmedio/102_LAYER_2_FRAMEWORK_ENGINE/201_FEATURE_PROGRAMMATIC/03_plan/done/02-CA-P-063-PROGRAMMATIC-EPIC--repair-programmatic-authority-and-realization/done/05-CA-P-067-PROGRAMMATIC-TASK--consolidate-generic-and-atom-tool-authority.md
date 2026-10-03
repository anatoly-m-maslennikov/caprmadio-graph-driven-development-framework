---
cce_version: cce_1
cce_form: obligation
subjects:
  - tool-authority
  - atom-operations
  - mcp
version: 2
updated_at: 2026-08-23 16:07:22 +0400
autonomous_confidence_threshold: 98
---
# Consolidate generic and Atom-specific Tool authority

WHEN CA-P-066 is Done, THE Assignee MUST establish one non-duplicative authority boundary between generic PROGRAMMATIC Tools, Atom-specific Tools, and MCP exposure.

## Scope

`(ALL Atoms WHERE (Current Scope IN (PROGRAMMATIC, MCP, TOOLS, TARGET_SET, GRAPH_CHECK, BULK_CHANGE, PROJECTION_REBUILD, IMPLEMENTATION_INVENTORY, ADOPT_RECONCILE, COMMIT_TRIGGER, COMMIT_CONTEXT, APPEND_CHANGE_RECORDS, COMMIT_CHANGE_SET, INSTALL_TOOLS, START_BACKGROUND_SERVICES, ATOM_SEARCH, ATOM_READ, ATOM_CREATE, ATOM_UPDATE, ATOM_MOVE, ATOM_ARCHIVE, ATOM_PROMOTE, ATOM_UPGRADE, MIGRATE_ATOM_IDENTITY, REBIND_ATOM_RELATIONS, CLOSE_ATOM, REPLACE_ATOM) AND Lifecycle State = active AND Content Role = REQUIREMENT))`

## Definition of Done

THE Task is NOT DONE IF (CA-P-066 is not Done OR two active Tool Requirements independently own the same operation semantics OR MCP owns Tool behavior instead of exposing registered Tools OR generic artifact operations contradict CAPRMEDIO Markdown Atom operations OR archive, promote, and upgrade are conflated OR upgrade lacks an explicit target Tier OR singular and bulk operation contracts are incompatible OR the exact Task Scope Resolution and ownership matrix are not recorded).

## Details

Keep search and read mutation-free. Keep create, update, move, archive, promote, and upgrade as distinct Atom operation capabilities that accept singular or bulk target sets where valid. Promotion changes `draft` to `active`; upgrade requires an explicit higher target Tier and may also require a governed move to an upper Scope Unit.

## Task Scope Resolution

Git base: `b7dc96eca7198d07a1e191bd7bf97f303ae10a03`.

Frozen at: `2026-08-23 16:07:22 +0400`.

`CA-P-066` is Done. The exact semantic target set contains 25 active Requirements; its preserved predecessor revision is named by the following local archive carrier and SHA-256.

| Boundary | Predecessor revisions |
| --- | --- |
| MCP delegation | `CA-R-1088@3` `836b265f202b7707d651c21dc2a557cda95ece860a86e580d790e19f63566d2c`; `REQU-719@2` `0e828542f2632313af3b2c1bb67c1a6263d41394d55bd2e4b3ab84beea29bd41`; `REQU-720@2` `317e74ae0708e42a26e318654d195c3f9d17a0393ce4d05121e917c1bccb8106` |
| Tool class and selectors | `CA-R-1066@7` `8b09b24816d6e47c38a15129698e6475120d5f6fbea8a1301bcd78f6feb109ae`; `CA-R-1067@5` `2a514b48355f00af20fdc746ea6d69aad0fc1260572457b05442a63b33a1de5a` |
| Generic Artifact Tools | `REQU-527@3` `a62c4b4545f106119fe6589104416fd572e79d0da36c6d95fec916c9bb4114f0`; `REQU-528@3` `1d5d97a25f13ff3824c987b670df5d0a3d0d6e4d8bcfdb5c6cdb06b7edf50f8b`; `REQU-529@6` `7ad5e3e2da1f397fc46fbbf652a5fd889a78b57b8b473c9bcbaef7d26b9c4cba`; `REQU-530@3` `781e87c6a2224c33aa120e5ca66685fd46a804fcb0a1a4add95209ae09069917`; `REQU-531@3` `61b04108855a7034366909e4b2f4b295d3f7b188a5deb73a8dbce9e58f7c3647`; `REQU-532@3` `8c9a212033c4aead2779fde93adacd9717f4db26330bfe82c511f2d3d6f18d4c`; `REQU-533@3` `0404a51d1dc5c35af0b09e6ee09b75ca5c70de669f75eab9b05fc06ac5f68f57`; `REQU-537@3` `65a28fb59ba05a1a99530ba7612df4f8fff29dac0941ff168481fe5339714807` |
| Atom Finders and Doers | `CA-R-863@3` `1dcf574d0a2ec75bc12f18a508c839b6253af07e000d3856790ec72b7674f2dd`; `CA-R-864@3` `ff54492a02165dda1d9405ce4be584957887cfad20409d3d1ea203c1455e70a8`; `CA-R-865@3` `c73e800f71b9b93a6e33487abca685a7ce05bcddb76324c063653034281e9d50`; `CA-R-866@3` `769fa2bbc3ab691b955bb120a95f3379d9aa67c1364e6fcb1b116f81163e2507`; `CA-R-867@3` `964d7a88d20b5bbdb5322b11248f2d5b561cc0e7e1a60be92c364c4928dd04cd`; `CA-R-868@3` `e3643437814844c8fed68eecc1f422fe8860f010ea7e2ee66d8604db8eefd60f`; `CA-R-869@3` `37a09a6e76392fdc974604e0aee98d0f40b90725c44f86ec49f1e4cc65561dfb`; `CA-R-870@3` `2dcffec67b9f6e01a359ee6f401d72b7958027574d0779e727f4c7f55fbddfe0` |
| Atom coordinators | `CA-R-1041@1` `1ea1388ea1d49d1d291ac5bd3c5834f6a9aaa5b2fcbf456f127316ee059c7bd2`; `CA-R-1042@2` `90481f39e702f98bc33576a8e3b3654da0b4febdfb21526a9c8f215ba48ff9ed`; `CA-R-1048@3` `b43bf99b37d4402dcb965b0832dd9cebe8638315a1a9969c13ada3b6758fba4c`; `CA-R-1049@3` `7937b91d6807fd26092f55b32ae5fccb5b7bd38a3b9dd239e1df221db956b21e` |

## Ownership Matrix

| Surface | Canonical owner | Owned responsibility | Not owned |
| --- | --- | --- | --- |
| Boundary | `CA-R-1093` | the generic-versus-Atom boundary and action-cardinality rule | any individual Tool operation |
| MCP | `CA-R-1088`, `REQU-719`, `REQU-720` | Tool discovery, projection, transport admission, delegation, and result transport | target resolution, validation, lifecycle meaning, mutation, recovery, or success reinterpretation |
| Generic Artifact Tools | `REQU-527` through `REQU-533`, `REQU-537` | form-agnostic carrier mechanics | CAPRMEDIO Markdown Atom identity, admission, authority, lifecycle, transaction, or public effect |
| Atom Finders | `CA-R-863`, `CA-R-864` | CAPRMEDIO Markdown Atom search and read semantics | mutation |
| Atom Doers | `CA-R-865` through `CA-R-870` | CAPRMEDIO Markdown Atom create, update, move, archive, promote, and upgrade semantics | generic Artifact Tool behavior and MCP transport behavior |
| Atom coordinators | `CA-R-1041`, `CA-R-1042`, `CA-R-1048`, `CA-R-1049` | the stated replacement, closure, identity-migration, and relation-rebinding cases | generic carrier mechanics, MCP transport behavior, Journal appending, and Git mutation |

## Execution Result

`CA-R-1093` was added as a Core `TOOLS` Requirement. It makes the boundary explicit: generic Artifact Tools may be helpers but do not own CAPRMEDIO Markdown Atom semantics; MCP only exposes and delegates; Finders are read-only; Doers dry-run by default and accept `--apply` only under authorized MCP delegation.

Every frozen Requirement advanced by exactly one revision and preserved its exact predecessor in its own local `archive/` folder. The Atom Doers now define atomic as one target and bulk as a frozen set of two or more targets with an all-or-nothing result. `ATOM_ARCHIVE`, `ATOM_PROMOTE`, and `ATOM_UPGRADE` are explicitly distinct. Upgrade requires an explicit enabled `core` or `standard` target Tier that ranks above its source and may move only to an explicitly named ancestor Scope Unit.

## Conflict Check

No active Tool Requirement now independently owns the same semantic behavior as another within this scope. `CA-R-1088` no longer gives MCP Tool behavior, and `REQU-719`/`REQU-720` preserve the canonical Tool's complete contract. Generic Artifact Requirements own only form-agnostic mechanics, while the named Atom Tools own the CAPRMEDIO Markdown Atom specialization. The selected Doer requirements all preserve direct dry-run availability and reject direct `--apply`; MCP admission neither broadens approval nor changes atomic or bulk cardinality.

The new `CA-R-1093` is Core at the `TOOLS` Scope Unit. Existing selected carrier normalization outside the one-revision updates remains the responsibility of `CA-P-068`; no MED Atom or implementation change was made.

## Validation Result

PASS for this Task's scoped Definition of Done.

- `CA-P-066` was already Done before the freeze.
- The 25 exact predecessor revisions are preserved with their SHA-256 values above; every active successor advances exactly once.
- MCP delegates and transports; generic Artifact Tools remain generic; named Atom Tools own CAPRMEDIO Markdown Atom behavior.
- Search and read are mutation-free; every named Atom Doer defaults to dry run and requires authorized MCP delegation for `--apply`.
- Archive, promotion, and upgrade remain distinct; upgrade has explicit `core|standard` higher-tier and ancestor-Scope conditions; atomic and bulk cardinalities are consistent.
