---
subject_scopes:
  - methodology-sync
project_settings:
  paths:
    framework_root: .caprmedio/000_caprmedio_framework
version: 2
updated_at: 2026-08-18 20:19:17
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Provide an explicit root-to-installed-methodology sync script

The repository provides one directly executable script that synchronizes reusable root methodology into `.caprmedio/000_caprmedio_framework` through the canonical synchronization engine.

Preview is the default. Mutation requires an explicit apply flag. Synchronization is one-way from root source to installed methodology; the script never copies installed carriers back to root source.

An applied run verifies that no methodology drift remains and fails nonzero if the repository is invalid, synchronization fails, or residual drift remains. Output identifies every affected carrier concisely and deterministically.
