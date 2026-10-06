---
atom_id: CA-O-152
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 17:42:12 +0000"
subjects:
  governs: "Applicable Methodology Compilation/Step: select"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Applicable Methodology"
    - "Select Reconciliation Sources"
    - "Methodology Source"
    - "Scope Unit"
    - "Framework Instance Settings"
    - "Extension"
    - "Project Configuration"
    - "Atom/Revision"
relations:
  relates_to: [CA-O-011, CA-O-004]
---
# Summary

Select the Applicable Methodology sources

## Operation

this Step is the select node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-004, Select Reconciliation Sources.

### Inputs and parameters

bind the Workflow Run's requested Applicable Methodology construction, registered Methodology Source Scope Units, current Framework Instance Settings, and applicable source authority.

resolve the complete current source set under CA-R-1228 from registered Methodology Source Scope Units, using Framework Instance Settings for current Extension activation **and** selected Extension Revisions. include CORE_META_MODEL, PROJECT_CONFIGURATION, **and** **every** applicable installed Extension Revision. discover registered source Carriers **without** requiring particular Extension names **or** Project-specific Project Configuration Claims; an empty Extension contribution requires no empty collection Carrier. collect **`=1`** current active Revision of **every** eligible source Atom under CA-R-1315 **without** omitting previously unknown conforming contents.

## Details
