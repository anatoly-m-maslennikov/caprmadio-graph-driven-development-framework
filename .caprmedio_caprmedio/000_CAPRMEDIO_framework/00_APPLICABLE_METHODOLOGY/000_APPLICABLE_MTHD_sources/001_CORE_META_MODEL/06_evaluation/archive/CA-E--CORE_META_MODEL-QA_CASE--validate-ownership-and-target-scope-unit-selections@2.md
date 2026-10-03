---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom selection"
  depends_on:
    - "Owned Atoms"
    - "Targeting Atoms"
    - "Subtree-owned Atoms"
    - "Subtree-targeting Atoms"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Claim"
    - "Scope Unit"
    - "Hub Atom"
version: 2
updated_at: "2026-09-22 17:59:17 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-M-273", "CA-R-1448", "CA-R-1449", "CA-R-1588", "CA-D-476", "CA-D-477"]}
---
# Validate ownership and Target Scope Unit selections

## Claim checked

ownership **and** Claim Target Scope Unit produce distinct direct **and** recursive Atom sets independently of textual applicability restrictions.

## Test case

use the complete Unordered Scope Unit **and** Atom fixture **in** CA-E-460. introduce nested Plan Hubs **without** changing the owning Scope Units; add narrower **and** composite Claim Scope restrictions **to** valid Current-scope Claims **without** changing their targets. repeat selection **after** tier-only changes. **then** remove an incoming source from the claimed-complete inventory, substitute ownership for targeting, substitute a Hub for a Scope Unit, **or** infer extra targets from Claim text.

## Acceptance criteria

the four expected sets remain those specified **in** CA-E-460. textual restrictions, Hub nesting, **and** tier-only changes do **not** change ownership **or** the Claim Target Scope Unit. every omitted target resolves under CA-R-1588 **and** CA-D-476. incomplete coverage **or** a substituted target fails explicitly; an incomplete inventory **must not** appear as a complete empty result.

## Failure disposition

report the selected Scope Unit, source inventory, expected set, **and** exact missing, extra, **or** unresolved members.
