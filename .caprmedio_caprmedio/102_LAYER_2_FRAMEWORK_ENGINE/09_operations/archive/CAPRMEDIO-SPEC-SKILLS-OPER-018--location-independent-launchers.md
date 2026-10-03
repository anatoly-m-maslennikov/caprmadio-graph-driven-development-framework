+++
artifact_subtype = "test_result"
schema_version = "1.0"
priority = "high"
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
context = ["repository=anatoly-m-maslennikov/dset-specs-loops-framework", "environment=portable-host-fixtures", "python=3.14.6"]
observed_at = "2026-07-21T01:55:04+04:00"
evidence_location = "dset/scopes/skill/changes/make-dset-self-hosting-and-skills-thin/proofs/CAPRMEDIO-SPEC-SKILLS-OPER-018--location-independent-launchers.md"
polarity = "supports"
currentness = "current"
reopen_when = "A wrapper command, governed executable instruction, launcher renderer, supported shell contract, or subject revision changes."

[subject]
id = "CAPRMEDIO-SPEC-SKILLS-EVAL-054--location-independent-launcher-test-case"
revision = "b7d79ec08c9a446f8a5358ac44c4c26bf7486d42"
intended_use = "Support the bounded claim that every executable DSET instruction uses one package-local launcher without ambient PATH fallback."

[producer]
identity = "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
performed_work = "Audited rendered command surfaces and ran hostile-path, Unicode, metacharacter, POSIX, WSL, and PowerShell fixture coverage."

[method]
description = "Render each wrapper and governed executable instruction for supported host forms, reject bare commands, and compare exact launcher identities and arguments."
setup = "Python 3.14.6; local macOS execution with deterministic macOS, Linux, WSL, and native-Windows rendering fixtures."

[[relations]]
type = "evidence_for"
target = "CAPRMEDIO-SPEC-SKILLS-EVAL-054--location-independent-launcher-test-case"
+++

# Test result — Location-independent launchers

Every executable DSET instruction resolves through the installed package-local
launcher. Host rendering contains no ambient `dset` fallback and preserves
arguments across spaces, Unicode, and shell metacharacters. The complete
310-Test suite passed.

Native hosted execution on every declared operating system remains a separate
external gate; this record proves deterministic rendering and local execution.
