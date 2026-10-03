---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/ATOM_ARCHIVE"
  depends_on:
    - "Atom"
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Archive Selected Active Atoms"
    - "Journal/Record"
version: 9
updated_at: "2026-09-17 02:57:30 +0000"
relations: {"evaluation_for":["CA-R-868","CA-O-029","CA-D-289","CA-D-303"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify archive selected active atoms

## Claim checked

ATOM_ARCHIVE follows CA-R-868 **and** CA-O-029: withdraw the complete selected active authority while preserving exact historical Carriers under CA-D-289 **and** CA-D-303.

## Test cases

1. use an isolated fixture with **=1** singly selected active Atom, **>=2** active Atoms selected as a bulk set, **=1** Draft, **=1** already archived Atom, **and** an existing historical reference **to** a bulk source. record exact before-state paths, IDs, Versions, bytes, **and** digests.
2. record singular **and** bulk dry runs. attempt apply **without** delegated authority; submit mixed-lifecycle, non-Atom, repeated-target, stale-source, invalid-destination, **and** destination-collision requests. **every** rejected preflight leaves the fixture unchanged.
3. archive the valid single **and** bulk selections through sealed Initiative envelopes. verify the role-local destinations, required `@<version>` basenames, unchanged IDs, Versions, Summaries, **and** byte digests. current discovery excludes them, the Draft remains a Draft, **and** the historical reference still resolves.
4. from an independent before-state, inject a failure **after** **>=1** selected archive effect **or**, for one atomic publication, **after** publication **and** **before** final verification. also exercise a postcondition failure.

## Acceptance criteria

- valid applies archive **all** selected Atoms **and** leave no active selected Carrier. no promotion, upgrade, unrelated mutation, **or** loss of existing history occurs.
- dry runs mutate nothing **and** expose the full archive map, including the suffix. an unchanged active filename is **not** the expected archive filename.
- a post-effect failure restores **every** selected mutable source **and** destination **to** its before-state. preserve accepted Journal evidence **and** report failure with the actual recovery result, **not** archive success.
- a preflight rejection alone does **not** establish rollback coverage. incomplete **or** unverified restoration fails the Evaluation.

## Failure disposition

reject a realization that violates **any** required case. retain lifecycle classifications, authority result, archive map, current-authority result, exact before/after digests, historical-reference evidence, injected fault position, **and** recovery evidence.
