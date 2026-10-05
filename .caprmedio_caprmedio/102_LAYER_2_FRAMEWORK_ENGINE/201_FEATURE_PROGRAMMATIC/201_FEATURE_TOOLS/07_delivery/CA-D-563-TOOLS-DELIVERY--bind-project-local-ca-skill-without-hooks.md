---
atom_id: CA-D-563
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Project Skill carrier"
  depends_on: [Tool, Skill, Runtime, Manifest, Project Configuration]
relations:
  delivery_for: [CA-R-1877, CA-R-1878, CA-M-332]
---
# Summary

Bind the project-local `ca` Skill without hooks

## Scope

The complete canonical `ca` Skill payload, staged candidate copy, and project-local no-hook Codex target.

## Claim

After the full-suite gate, Release Version **must** stage the complete `102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/` directory at `.caprmedio_runtime/framework/releases/<candidateSnapshotManifest.sha256>/SKILLS/ca/`, including `SKILL.md`, `agents/openai.yaml`, and every declared resource, then promote it to the project-local Codex target `.agents/skills/ca/` only with the N+1 selection. The active public Skill remains N until promotion.

## Details

The Skill retains its `caprmedio` Project-MCP dependency. Release Version neither registers MCP, changes Codex permissions, writes global configuration, nor changes Codex or Git Hook carriers, hook configuration, unrelated Skills, or user directories. Existing `INSTALL_TOOLS run --without-hooks` suppresses host-hook management only for the Engine Tools runtime and does not substitute for this Skill delivery.
