---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Admit Sealed Drafts as Active Atoms"
  depends_on:
    - "Action"
    - "Tool/ATOM_PROMOTE"
    - "Atom"
    - "Atom/Identifier"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 9
updated_at: "2026-09-17 23:09:21 +0000"
relations:
  evaluation_for:
    - CA-O-066
    - CA-R-869
    - CA-D-450
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify promote sealed atom drafts

## Claim checked

CA-O-066 admits the complete selected Draft set under CA-R-869 with canonical role-matching identities, exact bytes **and** complete transaction recovery.

## Applicable when

apply **to** **any** realization **before** it can admit Draft authority into the active graph.

## Test cases

1. prepare independent singular **and** frozen bulk fixtures with valid Drafts, Operator-supplied IDs admitted by CA-D-450 **and** CA-D-378, complete historical assignment evidence **and** absent active destinations. retain exact before-state paths **and** digests.
2. verify mutation-free dry runs. separately test absent apply authority, a non-Draft source, missing **or** invalid ID, role mismatch, repeated ID, an ID used **only** by an archived **or** replaced Atom, a non-next number, incomplete history evidence **and** a destination collision. reject the complete affected request **without** promotion.
3. **after** a valid preview, independently change a source digest, add a destination **or** admit a competing use of an assigned ID. reject apply **without** silently changing the ID, selected set **or** sealed request.
4. apply valid singular **and** bulk requests through sealed Initiative envelopes. **every** source **must** yield **`=1`** canonical active Carrier with its admitted stable ID **and** unchanged full byte digest; remove **all** selected Draft Carriers **and** preserve unrelated files.
5. from independently restored baselines, inject an effect failure **after** a promotion write **and** a failed post-write verification. exercise singular **and** bulk recovery, including failure **after** an earlier bulk member was moved. retain **any** accepted Journal evidence of actual effects.

## Acceptance criteria

**every** rejected preflight leaves its mutable before-state unchanged. successful admission preserves exact bytes, complete membership, canonical filenames **and** placement **and** unique historical identity admission. **every** post-effect failure restores **all** selected mutable sources **and** destinations **to** their exact before-state, preserves unrelated Carriers **and** accepted Journal evidence, **and** reports failure rather than promotion success. incomplete **or** unverified restoration **must** fail this Evaluation. preflight rejection alone does **not** prove rollback.

## Failure disposition

reject the realization **and** preserve source digests, Draft identities, assigned IDs, historical admission evidence, promotion maps, authorization result, injected failure point, final lifecycle locations **and** **any** partial **or** duplicate active identity. these cases do **not** establish the separate external Project Goal operation boundary.
