---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - feature-boundary
version: 1
updated_at: 2026-08-25 02:10:26 +0400
relations:
  method_for:
    - CA-R-1163
    - CA-R-1164
    - CA-R-1165
    - CA-R-1166
    - CA-R-1167
    - CA-R-1168
---
# Register executable Tool folders as active Tool units

## Applicable when

Apply when an immediate native `TOOLS` folder owns one canonical independently executable deterministic Tool but lacks current Scope Unit registration.

## Procedure

1. Resolve the immediate native Tool folders, their canonical executable entrypoints, and the current project graph.
2. Exclude shared libraries, caches, tests, migration collections, and other folders that do not own one canonical independently executable Tool.
3. For each admitted Tool folder, define exactly one immediate `TOOLS` child Scope Unit with matching authority and Delivery coordinates, register its Unit Name and filename token, and include it in the canonical graph source.
4. Treat the registered Tool as active unless current project authority or Configuration explicitly disables it, then allow MCP to derive exposure only through the current Tool frontier.

## Outcome

Every admitted immediate executable Tool folder has one current Tool Scope Unit and one deterministic MCP-discoverable identity without turning infrastructure folders into Tools.

## Failure or stop

Stop when a folder has no unique canonical executable entrypoint, conflicts with an existing Tool identity, lacks a valid authority or Delivery coordinate, or has an ambiguous enablement decision.
