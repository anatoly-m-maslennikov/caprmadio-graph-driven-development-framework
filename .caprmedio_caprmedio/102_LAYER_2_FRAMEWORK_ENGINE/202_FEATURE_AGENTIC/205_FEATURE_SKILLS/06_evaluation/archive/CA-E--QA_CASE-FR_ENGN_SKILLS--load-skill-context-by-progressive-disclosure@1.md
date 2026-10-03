---
subject_scopes:
  - framework-engine-skills
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Load Skill context by progressive disclosure

Given a Skill with catalog metadata, body instructions, and multiple references or assets, execute a request needing exactly one referenced resource. Verify that discovery loads only metadata, activation loads the body, execution loads only the required resource, and irrelevant resources do not enter the task context.

Candidate alignment: CA-E-001, CA-E-002, CA-M-003, CA-M-005, CA-R-861.

## Sources

- [Agent Skills: adding Skills support](https://agentskills.io/client-implementation/adding-skills-support)
- [Agent Skills specification and documentation](https://github.com/agentskills/agentskills)
