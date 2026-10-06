---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "RMEDO Conflict Resolution"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Revision"
    - "Atom/Global Tier"
    - "Atom/Revision/Updated At"
    - "Atom/Local Tier: Principle"
    - "Relation"
    - "Operator"
    - "Autonomous Confidence Threshold"
    - "Journal/Record"
version: 1
updated_at: "2026-09-16 22:42:50 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-O-028
    - CA-O-005
    - CA-O-006
    - CA-O-008
---
# Validate gap-free RMEDO conflict resolution

the Evaluation **must** check whether RMEDO Conflict Resolution follows CA-O-028 **and** its reused Actions **without** losing required authority.

| Case | Expected result |
|---|---|
| an older lower-tier Claim conflicts with higher-tier authority | preserve the higher-tier authority; propose a permitted correction **or** archival of the conflicting Claim |
| a newer lower-tier Claim conflicts with higher-tier authority | Updated At does **not** reverse Global Tier precedence |
| equally applicable same-tier Claims conflict; the newer accepted Claim aligns with Principles | prefer the newer Claim; evaluate the older Atom for correction **or** archival |
| timestamps, applicability, **or** precedence are unresolved | report uncertainty; do **not** invent a winner |
| removing an obsolete Atom improves Principle alignment; **all** coverage checks pass; valid delegation covers archival | archive **without** demanding another per-Atom approval; preserve exact history |
| an Atom has unique still-required content, an incoming reference needs repair, **or** a required Evaluation loses its target | block archival **until** the prerequisite coverage repair is active **and** checked |
| removal hides a conflict **or** leaves a missing required Claim, Relation, reference, **or** check | fail the completion claim |
| **all** Claims of an obsolete Atom are explicitly withdrawn by governing authority | preserve the archive **and** withdrawal evidence; do **not** invent a replacement Claim **or** successor |
| active Principles conflict, the effective confidence threshold is unmet, **or** mutation is outside delegation | ask the Operator; no autonomous resolution **or** mutation |
| a source changes **after** assessment, a correction is partial, **or** required rechecking is absent | no completion; report actual effects **and** reassess **only** within accepted retry bounds |

the check **must** use exact source Revisions **and** compare the affected authority **before** **and** **after** correction. an archival event alone is **not** evidence that coverage, alignment, authorization, **or** conflict resolution passed.
