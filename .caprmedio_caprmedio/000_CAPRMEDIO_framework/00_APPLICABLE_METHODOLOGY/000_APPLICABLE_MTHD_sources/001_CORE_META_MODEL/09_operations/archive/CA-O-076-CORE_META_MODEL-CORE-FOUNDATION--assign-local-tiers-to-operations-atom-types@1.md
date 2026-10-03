---
cce_version: cce_1
cce_form: classification
subjects:
  governs: "Atom/Content Role: Operations/Local Tier"
  depends_on:
    - "Atom/Content Role: Operations/Type"
    - "Scope Unit"
    - "Atom/Local Tier: Core"
    - "Atom/Local Tier: General"
    - "Atom/Local Tier: Standard"
    - "Atom/Content Role: Operations/Type: Foundation"
    - "Atom/Content Role: Operations/Type: Rule"
    - "Atom/Content Role: Operations/Type: Action"
    - "Atom/Content Role: Operations/Type: Workflow"
    - "Atom/Content Role: Operations/Type: Actor"
version: 1
updated_at: "2026-09-20 23:49:39 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-O-070", "CA-O-071", "CA-O-072", "CA-O-073", "CA-O-074", "CA-R-1287", "CA-R-659", "CA-R-1431", "CA-R-660", "CA-R-1442", "CA-R-1443"]}
---
# Assign Local Tiers to Operations Atom Types

**within** a non-Project methodology Scope Unit, the Local Tier of an Operations Atom **must** match its Type as follows:

| Operations Atom Type | Local Tier |
|---|---|
| Foundation | Core |
| Rule | General |
| Action | Standard |
| Workflow | Standard |
| Actor | Standard |
