---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Carrier/Content"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Summary"
    - "Atom/Claim"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "Atom/Content Role: Plan/Type: Plan/Details"
    - "File Carrier"
    - "Hub Atom"
version: 4
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"relates_to": ["CA-R-1599", "CA-R-1586", "CA-D-482", "CA-D-460"]}
---
# Summary

Serialize Plan file sections

## Claim

**every** Plan Markdown File Carrier **must** contain YAML Frontmatter followed by these body Property sections **in** order:

1. **`=1`** literal `# Summary` heading with the Summary value below it.
2. **`=1`** literal `## Claim` heading with the intended work **or** outcome Claim below it, including its applicability restrictions.
3. **`=1`** literal `## Definition of Done` heading with its falsifying Condition Expression below it.
4. **`<=1`** optional literal `## Details` heading with its supporting details below it.

use CA-D-479 for section boundaries. do **not** repeat these Properties **in** frontmatter **or** create a separate Scope section duplicating restrictions already carried **in** the Claim. a Hub uses this same mandatory file, **not** an additional Objective Atom.
