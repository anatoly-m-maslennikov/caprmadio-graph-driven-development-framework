# Release parallel continuation

## Scope

CA-P-1117 remaining Release implementation and acceptance, with ten independent subagents dispatched. No further harvesting, permission bypass, image retirement or fabricated Workflow Run receipts.

## Environment

The latest am-default check permits Docker inventory and temporary-file deletion. Temporary-directory deletion fails with EPERM. The Operator instructed leaving the empty probe directory untouched. Fixture tests remain blocked; their cleanup is not suppressed.

## Completed evidence

- P1712 fixture-root canonicalization independently accepted by static review: all three modules parse; no production guards or cleanup weakened. Runtime verification pending.
- P1710 provider rejects empty effect paths and project-relative symlinks resolving outside the Project. Root reran the three pure result-serialization cases: 3/3 pass. Fixture cases pending.
- Saved prior task frontier and current environment evidence in commit 194dee472; no push.

## Confirmed remaining work

- Private Release phase state is process-local; durable restart and uncertain-effect reconciliation remain incomplete. Reuse the sole shared recorder rather than create another Journal writer.
- Public Release apply/recovery remains an explicitly blocked boundary pending admitted provider integration.
- Public route 16 needs guarded current-source admission; canonical fifteen-route manifest remains unchanged.
- Exact image-retirement phase must distinguish a successfully observed retirement from pending/uncertain outcomes, while preserving separate durable recording requirements.
- Runtime image adapters currently overwrite explicit image selection with a mutable development tag; the isolated repair must preserve explicit overrides without weakening immutable acceptance assertions.
- Full suite, fresh immutable image, package/Skill promotion and actual MCP/queue acceptance remain unfinished.

## Evidence limits

Suite boundary repair is saved, uncommitted and fixture-unverified: release_suite.py SHA-256 34411db7142c8a04568679391d5bb37d9ab7686a45dc2fbfc370ff26f41eed16; test_release_suite.py db8fe4c11bd85c3352381a6e7c6330c8d883c902ba860de47c816eb4a81735f5. Runner receives the compiled-root and candidate ID; report requires a sealed compiled path; active N package and project-local ca are observed before/after. Static compilation/diff checks pass, not runtime tests.

No release_state.py was added: existing persisted native results omit preflight and strip type identity. A closed typed checkpoint must be added at the existing shared progress write before faithful rehydration is possible. Executor admission remains external and must not be serialized. Existing public Tool refusal is intentionally retained.

The guarded-registration worker attempted an existing fixture admission suite despite the no-temp-fixture instruction. Only partial visible passes were observed before termination; that suite is not accepted as rerun. No cleanup bypass or canonical manifest edit followed. Root's separate four pure registration tests passed.

Independent review accepts the strict image repair f2ba6c494: missing/empty selects the existing development fallback, all other overrides require a lowercase full sha256 ID. False/zero, mutable tags and malformed IDs are rejected. Root rerun: five pure tests pass. Existing exact-image acceptance assertions are unchanged.

Subsequent saved commits: 85a80d698 aligns the Structure with the explicit Methodology delivery destination; 3eec8cffb adds guarded source-admitted Release registration (root rerun: four pure tests); 28f5e572c rejects hook-bearing Skill payloads (root rerun: two pure tests). d7e1c53de initially preserved explicit image selection; independent review identified unrestricted tag overrides and a stricter immutable-ID repair is underway. No actual Release route admission, image build, installation or retirement occurred.

The initial public-entrypoint finding was refined against D560/D572: its effect-free refusal is intentional before source-admitted implementation. The concrete unfinished recovery work is the private provider's process-local state, not an unauthorized requirement to make the preparatory Tool effectful immediately.

Static review and pure tests are not fixture, real Docker Workflow, Journal, durable recovery or Epic completion evidence.
