# CA-P-1080 — General vocabulary and unresolved Term diagnostics

Non-authoritative execution evidence. Completed 2026-09-13 03:43:10 +0400. This Task defines diagnostic-index authority; it does not classify every source word or implement a generator.

## Result

Done: the Task Definition of Done falsifier is false. Two source changes resolve P1078 finding G03 by making source evidence, diagnostic distinctions, uncertainty and non-authority explicit. The root reviewed the exact final source contents and accepted this minimal set before completion preparation.

| Atom | Version | Current SHA-256 |
|---|---|---|
| CA-E-444 | 2 -> 3 | df3f04b7af2695008bcc1e763b33f0bca899b1974c07d7618ea3db26b8bf0eae |
| CA-R-1455 | new -> 1 | 49d2c877718c97b19177b3078d785de366a62fadec84450a9123ee5e17648a61 |

R1455 adds one General-tier Requirement for vocabulary diagnostic index admission. Every entry binds to the exact source occurrence, surrounding Claim or reference context and Artifact Revision. Source selection and checked definition coverage bound every judgment. An unresolved Project-specific candidate requires contextual evidence of that use; a suspected meaning never becomes established authority.

The authority distinguishes supported ordinary English use, missing defining authority, conflicting authority or Project-specific uses, and insufficient evidence. Missing-authority judgments require complete checked definition coverage for the declared applicable source authority boundary. Filtered or incomplete selection alone cannot prove absence. Insufficient evidence remains visible and reviewable; the diagnostic check may pass while its underlying source issue remains unresolved.

E444 retains its existing Project-specific meaning, dictionary-only exclusion, direct Subject/reference and composite Subject checks, and adds corresponding diagnostic cases and acceptance criteria. Duplicate agreeing definitions are a defining-authority uniqueness conflict, not fabricated evidence of a meaning conflict. Spelling alone does not transfer one occurrence's classification to another. Scope Unit names, Actor names, IDs, paths, syntax tokens, capitalization and GOVERNS/DEPENDS_ON occurrence are insufficient alone; actual source context still governs admission. General Term naming under R1323 does not authorize changing the spelling of cited occurrences.

Indexes remain non-authoritative Projections. They neither supply definitions nor establish graph relations or another Terms Graph identity. Any separate graph representation requires independently admitted Relation Kind and source Relation authority; no relation family is invented here. No mechanical semantic certainty or full-vocabulary classification is claimed.

## Reuse and boundaries

All three reserved sources were read. R1320 v4 and R1323 v4 are already adequate and remain byte-identical. Shared R1318/R1319/R1325, R1437, R1454, M114, E382 and the predecessor direct-Subjects changes remain unchanged. There is no new M, O or D: the new R expresses an index selection/evidence invariant, E checks it, and no Implementation choice, reusable Action/Process or Carrier format is defined. P1084 retains D, P980 retains Operation composition/control-flow after the later parent review, and P1081/P1082/P1083 retain their separate model concerns.

All 13 live Project Principles were read. Operator authority (P033), DRY (M002), necessary complexity (M005), coherence (M006) and checkability (E001) support the bounded two-source repair, existing definition reuse and explicit uncertainty. The exact source proposal was reviewed by the root. Its two clarifications normalized `each` to **every** under M236 and replaced ambiguous new Claim Scope wording with ordinary lowercase declared source-boundary and definition-coverage language. No new Scope concept or existing Scope authority is changed. Confidence meets the Task's 99% threshold; no unresolved consequential choice is hidden by closure.

R1455 is the next unreused R identity after R1454, checked in live governed source/Project/archive/Journal content and Git filename history. General tier follows R1431 for an independently adjustable derived-set constraint over existing authority. The new and changed Carriers use scalar governs and a unique scalar depends_on list. E444's exact v2 bytes are archived; its prior accepted direct-Subjects encoding is retained. Revision timestamps use actual Project time; default Author omission is preserved under D274/D270.

## Semantic authority fixtures

The following 24 synthetic scenarios were manually reviewed against exact current source Claims. They are evidence for the model distinction, not fabricated generator tests. The source map records each authority identity, revision, hash and Claim start location. Hypothetical wording and definitions in the scenarios add no source Atoms or Project vocabulary authority.

| ID | Synthetic input | Reviewed disposition | Authority |
|---|---|---|---|
| F01 | A Claim uses the ordinary word ready in its ordinary English sense; the checked context supplies no Project-specific meaning and no definition. | Accept as general vocabulary; no missing governed definition. | CA-R-1320, CA-R-1455, CA-E-444 |
| F02 | The same ordinary word begins a sentence with a capital letter. | Capitalization does not establish Project-specific status; preserve the exact source occurrence. | CA-R-1320, CA-R-1323, CA-R-1455, CA-E-444 |
| F03 | A hypothetical Claim refers to Zorping as its Project-specific approval criterion, but complete checked definition coverage for the declared applicable source boundary has no active defining authority. | Report a candidate with missing defining authority and its contextual evidence; do not supply the criterion meaning. | CA-R-1319, CA-R-1455, CA-E-444 |
| F04 | Two active definitions assign incompatible Project-specific meanings to the same candidate in the same applicable scope. | Report conflicting defining authority with both source references; choose neither meaning. | CA-R-1318, CA-R-1319, CA-R-1455, CA-E-444 |
| F05 | A unique defining Atom and an applicable source use supply conflicting Project-specific meanings. | Report conflicting use with the defining Atom and exact affected occurrence. | CA-R-1318, CA-R-1455, CA-E-444 |
| F06 | An unfamiliar capitalized phrase occurs with insufficient context to decide ordinary versus Project-specific use. | Keep a source-backed uncertain case and reason; do not promote it to an established Project-specific candidate. | CA-R-1455, CA-E-444 |
| F07 | A capitalized expression occurs only as a DEPENDS_ON target. | The occurrence alone establishes neither a Term nor missing defining authority; assess actual source context. | CA-M-114, CA-R-1455, CA-E-444 |
| F08 | A Scope Unit name or Actor name is used only to identify the referenced unit or person, with no evidence of Project-specific vocabulary meaning. | Do not admit an unresolved Term candidate merely from the name. | CA-R-1455, CA-E-444 |
| F09 | An Atom ID, filesystem path, or syntax token occurs only as an identifier, locator, or notation. | Do not report missing Term definitions from those occurrences alone. | CA-R-1455, CA-E-444 |
| F10 | A name-like expression also has contextual source evidence explicitly assigning it a Project-specific vocabulary role. | Evaluate that actual evidence; the shape of the expression is not a blanket exclusion or sufficient admission. | CA-R-1318, CA-R-1455, CA-E-444 |
| F11 | A definition exists outside a filtered selection, but the index treats its absence from the selected files as proof of missing authority in the applicable scope. | Reject the absence claim; retain the selection and coverage limitation without silently importing a definition. | CA-R-1454, CA-R-1455, CA-E-444 |
| F12 | Definition coverage is incomplete and no matching definition has been observed. | Report uncertainty about coverage or defining authority; no established missing-authority result. | CA-R-1455, CA-E-444 |
| F13 | A diagnostic entry proposes a candidate but cites no exact source occurrence. | Reject the index entry as ungrounded. | CA-R-1455, CA-E-444 |
| F14 | A diagnostic entry cites a source filename but omits its exact Revision and the context supporting its judgment. | Reject incomplete traceability. | CA-R-1455, CA-E-444 |
| F15 | The same spelling has an evidenced ordinary use in one occurrence and an evidenced Project-specific use in another. | Preserve both contexts; spelling alone does not transfer classification or settle a meaning conflict. | CA-R-1320, CA-R-1455, CA-E-444 |
| F16 | An index invents edges from general vocabulary to unresolved candidates merely because entries co-occur or share spelling. | Reject; index membership or co-occurrence supplies no Relation Kind or authoritative source edge. | CA-R-1437, CA-R-1455, CA-E-444 |
| F17 | An implementation labels the diagnostic index a second Non-governed Terms Graph solely from its membership. | Reject the new graph identity; no independently admitted relation authority supports it. | CA-R-1455, CA-E-444 |
| F18 | A separate graph representation uses an independently admitted Relation Kind and exact source Relation declarations. | The index authority does not itself forbid that separately governed representation or invent its edges. | CA-R-1437, CA-R-1455 |
| F19 | The diagnostic index is truthful about insufficient evidence and retains occurrence, context, Revision, coverage and reason. | The diagnostic-index check passes while the underlying classification or authority remains unresolved. | CA-R-1455, CA-E-444 |
| F20 | A reviewer substitutes a guessed definition to make a missing-authority diagnostic disappear. | Reject fabricated authority; retain the evidenced unresolved source issue. | CA-R-1455, CA-E-444 |
| F21 | A classifier asserts that capitalization and token extraction mechanically settle every word's semantic status. | Reject unsupported certainty; retain uncertain cases for review. | CA-M-114, CA-R-1455, CA-E-444 |
| F22 | Two active Definition Atoms provide the same wording and meaning for one governed Term in the same applicable scope. | Report a defining-authority uniqueness conflict; do not falsely claim conflicting meanings. | CA-R-1319, CA-R-1455, CA-E-444 |
| F23 | A complete composite Subject Path is classified as one Term, or a Term's spelling is substituted for the direct Entity, Action or Process reference. | Reject the substitution or composite-Term admission under the retained checks. | CA-R-1325, CA-M-114, CA-E-444 |
| F24 | A unique active Definition Atom establishes a Project-specific meaning and the selected source uses it coherently. | The governed Term remains eligible under existing authority; do not label it unresolved solely to populate a diagnostic index. | CA-R-1318, CA-R-1319, CA-R-1454, CA-R-1455, CA-E-444 |

## Preservation and completion

- Reconstructed the live frontier from P976, P977, P978, P979, the sealed P980 direct-Subjects map and P1079. Before: 1,560 sources / 678 Core. After: 1,561 sources / 679 Core. Only E444 changes; R1455 is added. All other 1,559 prior sources remain byte-identical.
- Preserved all 53 excluded Drafts, 8,361 prior archives, 19 prior evidence files and 109 other Tasks. Added exact E444@2 and P1080@2 archives. This Task alone moves v2 to done v3.
- Hash-checked all 11,867 enumerated existing non-runtime repository files, excluding Git internals, environment-secret carriers and ignored files. Outside the exact Task/source paths and append-only Journal, their bytes remain unchanged. No Tool implementation, Settings values, generated Applicable Methodology or unrelated source mutations occur. Canonical Journal persistence may create its normal runtime receipts; no runtime implementation is edited.
- Raw Git index remains `54ec1294d1bd71d296f56bbef952eed63fe84f8d498bd4e1b93d04257db14e1b`. No staging, unstaging, commit, push or reset. Git materialization remains separately pending.
- The final append-only Journal will bind source/archive/report/map/Task results after root completion review. Exact receipts are returned separately; all prior Journal bytes must remain intact. This report does not claim those not-yet-appended receipts already exist.

## Handoff

Execute only P1081 next, in its own dedicated subagent after this Task is sealed and verified. Consume this map after P1079. R1455/E444 supply diagnostic guards for later views; they do not require future Tasks to invent a Process schema or classify all words. P1082 owns backlinks, P1083 composition/registry, P1084 Carriers, P1085 closure, and P980 Operation flow follows that closure and the parent review. No later Task has been executed here.
