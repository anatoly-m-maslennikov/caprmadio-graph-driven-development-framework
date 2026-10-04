---
atom_id: CA-C-307
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Harvest save selection"
  depends_on:
    - "Project"
    - "Artifact"
version: 1
updated_at: "2026-10-04 11:54:00 +0400"
relations:
  concerns:
    - CA-P-1118
---
# Summary

Select save target IDs from the Carrier basename

## Concern

The checkpoint59 staging selector matched the first Atom ID in each full path, which was the enclosing Epic1117 rather than the leaf filename. It therefore excluded all intended Plan saves.

## Evidences

Actual commit1edf6433a saved only10 validated Analysis/Concern carriers. No unowned paths were staged. The selector is corrected to Path(path).name; the remaining owned Plans and this Concern receive a separate mechanical Git save. The complete strict checker also encountered unfinished A988 while another Agent was writing it; it is excluded explicitly from this previous-completion checkpoint rather than called complete. A988 must independently finish and pass before its own save.

## Blast radius

Save grouping and concurrent diagnostic scope only. No lost or fabricated harvest coverage, no undo of unrelated edits, no claim that1edf6433a alone saved the Plan roll-up.
