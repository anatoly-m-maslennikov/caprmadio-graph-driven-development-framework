# Summary belongs to its Atom

Non-authoritative execution evidence. Updated 2026-09-14 02:40:31 +0400. This is a bounded source-content amendment within active CA-P-1086, not completion of the meta-model or the New Ops Epic.

## Accepted rule

Summary is an Atom Property, not an independently maintained Projection Artifact. It is created with the Atom and has no independent identity, lifecycle, or timestamp. Changing the Summary requires a completely new Atom ID, even when the Claim is unchanged. All same-ID Revisions retain the same Summary.

## Source edits

| Disposition | Atoms |
|---|---|
| Replace mutable-Summary authority | CAPRMEDIO-META-REQU-122 → CA-R-1464 |
| Replace navigation-Projection wording with the Atom Property definition | CA-R-1272 → CA-R-1465 |
| Align Summary Subject paths, preserving existing Claims | CA-R-1273 v6; CA-R-1274 v6 |
| Make Summary changes replacements rather than carrier-only changes | CA-R-1432 v2 |
| Derive Summary on creation; retain and check it on same-ID revisions | CA-M-111 v17; CA-M-116 v10; CA-M-231 v10 |
| Prevent the existing CCE check from regenerating an Atom's Summary | CA-E-241 v13 |
| Remove filename permission for same-ID Summary changes | CA-D-283 v7 |
| Add positive and negative identity-preservation cases | CA-E-463 v1 |
| Record bounded progress; leave Task Active | CA-P-1086 v12 |

The two predecessors were removed from the Active source location only after their successors existed there. Their full original bytes remain in exact @12 and @6 archives respectively. All eight revised source Atoms retain their original Summary/H1 and filename; their exact previous revisions are also archived. Historical versions are not rewritten to impose the new policy retroactively. Lossless serialization of an unchanged Summary value is not a new Summary.

R1418 cardinality, R1273 source faithfulness, R1274 non-authority, D281 H1 serialization, D282 slug serialization, and E384 Claim/source-faithfulness checks retain their substantive existing responsibilities. No additional Micro-Projection Entity, Summary lifecycle, duplicate timestamp field, or new replacement relation is introduced. M116/M231 keep their existing identities and Summaries; broader Method-versus-Ops classification is not claimed complete by this amendment.

## Verification

- 3 new source Atoms, 8 source revisions, 2 predecessor replacements.
- 10 exact source archives verified against captured pre-edit bytes.
- All 8 same-ID source revisions preserve their Summary.
- Changed frontmatter parses; new identities are unique in methodology sources; Evaluation targets resolve.
- 1,568 other active source Atoms, 53 excluded Drafts, and 17 previous source maps are unchanged.
- Active source frontier: 1,578 + 3 additions − 2 predecessors = 1,579.
- Scoped whitespace check passes.
- Source assertions are verification of this amendment, not proof that future Tool implementations enforce E463.

## Meta-model first; Tools deferred

The Operator explicitly stopped further Tool work until the meta-model is complete. Only the immediately preceding legacy-ID validator/test delta was reverted to its captured pre-edit bytes. Earlier independently authorized replacement support remains untouched.

No new Journal records, commits, hook changes, Tool installation, Settings changes, or generated Applicable Methodology updates were performed. The Git index and existing Journal are byte-identical to this amendment's baseline. Generic R807/M274 replacement rules remain unchanged; their Journal/Git materialization is deferred for this amendment, not falsely reported complete and not removed from the model.

The attached map is derived change evidence, not an alternative authoritative replacement Journal. A later authorized reconciliation must use actual source/archive evidence and actual recording time; it must not fabricate historical completion events. Tool consumers and installed copies remain pending implementation alignment. The prior optional legacy-ID Tool patch and its passing tests do not describe current code: that patch was reverted under the latest decision.

## Remaining work

CA-P-1086 stays Active. Its ten non-Summary reserved sources still need their own dispositions and final source consistency review. M116/M231's broader M/O ownership remains deferred to the existing migration Tasks. Other Tasks and Epics are neither executed nor closed here.
