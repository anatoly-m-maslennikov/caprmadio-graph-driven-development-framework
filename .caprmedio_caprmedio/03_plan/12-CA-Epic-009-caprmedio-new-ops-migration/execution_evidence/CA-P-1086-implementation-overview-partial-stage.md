# CA-P-1086 partial stage — Implementation Overview

Non-authoritative execution evidence, 2026-09-13 12:46:19 +0400. This stage applies only the Operator-approved distinction between historical implementation event records in the Journal and the current-state Projection now named Implementation Overview. It does not complete CA-P-1086 or decide graph Projection Type admission.

The two source Atoms retain their identities and primary Claims: GOV-REQU-322 defines the current-state Projection Type; META-REQU-115 classifies the current realization view as a Projection. Both now govern `Projection/Type: Implementation Overview` through scalar GOVERNS and unique direct prerequisite references. The former Implementation-role classification in META115 is removed because META113 limits Content Role to Atoms. The realization, coverage, lineage, retention, native-target, Ops-evidence and Verification boundaries remain. META105 remains the source authority for implementation bindings in the shared Journal and is unchanged. Generic Journal and operational-record work remain with P1088/P983.

The existing `implementation_record` carrier token and `irec` prefix remain exactly as registered by read-only D397@4. GOV322's `project_graph_state.artifacts.enabled_types` entry remains byte-for-byte unchanged. This is compatibility preservation for the existing serialized binding, not a new semantic Type alias named Implementation Record. The project settings still enable that token. `generate_meta_requirement_catalog.py` and `generate_proof_currentness_catalog.py` use it as a Projection discriminator; changing it here would require out-of-scope settings and implementation changes. No normalization rule deriving the token from the current human Type name was found in the reviewed D authority. No new token or alias is introduced.

The former human name remains in GOV322's original historical rationale, preserved verbatim and followed by an explanation of the rename. Exact former source revisions, old names, Journal history, prior inventories and completion evidence remain untouched as history. Generic English uses of record are not prohibited. Generated Applicable Methodology copies are unchanged and may continue to display the prior name until their separately governed regeneration; this stage makes no generated-output or runtime-conformance claim.

## Exact source changes

| Source | Before | After | Change class |
|---|---:|---:|---|
| CAPRMEDIO-GOV-REQU-322 | 16 | 17 | semantic_revision |
| CAPRMEDIO-META-REQU-115 | 9 | 10 | semantic_revision |

The source filename Summary Slugs change to match Implementation Overview under D282/D283. Assigned Atom-ID segments remain exact. Each old active pathname disappears only after its exact bytes are added as its version-suffixed archive; the successor uses the same Atom identity. This is a same-identity semantic revision and Carrier move, not a replacement, Claim absorption or independent-Claim split under R1432. M274's replacement exception is neither needed nor granted.

## Lineage and ownership

The scan of all 1,562 current admitted source carriers found the former human Type name only in these two selected Core sources, and found no other active source reference to either changed Atom ID or filename. GOV296 uses ordinary plural implementation records for native provenance; that use is unchanged. D397 contains the retained serialization token and remains a read-only source in PROJECT_CONFIGURATION. Two historical migration scripts mention the token; they are not run or changed. Prior P1078/P1087 inventories and P1079/P1080/P1081 evidence remain immutable. Both sources are new bounded P1087 reservations, absent from the P1078 selected inventory, so this stage has no ownership transfer from a P1078 owner. The ordered partial map records that exact disposition and is appended after P1081's accepted source map; P1087's administrative completion map is not a source map.

## Partial completion boundary

CA-P-1086 remains Active v3 with this stage linked; all other Tasks retain their exact bytes. The graph-Type admission question is still pending. No other source, settings, code, runtime, generated output, Draft or historical record is modified. The remaining 28 P1086 reservations are not implicitly accepted or completed. Universal R/D/M/E counts and M274 exceptions remain unresolved. No successor Task is executed.

The source map carries exact old/new paths, revisions, hashes, archives, source-authority references, and Task/evidence administration. Verification checks the 1,562-source admitted frontier with exactly two revisions advanced, all 53 excluded Drafts, all baseline repository files outside the explicit outputs, the prior Task chain, and the raw Git index (`54ec1294d1bd71d296f56bbef952eed63fe84f8d498bd4e1b93d04257db14e1b`). Canonical Journal events record exactly these source, archive, Task and evidence results append-only; prior bytes remain unchanged. Git materialization is pending because no Git mutation is authorized.
