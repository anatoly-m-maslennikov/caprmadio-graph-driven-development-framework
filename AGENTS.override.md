<!-- codex-wide-delegation:start -->
## Workload-driven parallel delegation

For substantial tasks, proactively use subagents for independently executable responsibilities. Before the first spawn, identify the full set of ready lanes, including independent investigation, implementation, and verification where useful. Each lane needs a distinct deliverable, bounded scope, and acceptance check. Use direct execution for small tasks or work whose dependencies prevent useful delegation.

Choose the worker count from the useful ready lanes and currently available worker slots. When four to ten substantial independent lanes are ready and capacity permits, launch four to ten workers before waiting for results. Three is not a preferred count or a planning ceiling. Keep the work granular enough for ownership but large enough to justify each handoff. Do not create filler work to occupy slots. Explicit task-specific worker limits still apply.

Delegate clear contracts with paths, ownership, checks, and compact expected returns. Workers share the filesystem: concurrent mutation requires exclusive file and shared-state scopes; read-only lanes may share inputs. Dependent lanes wait for their inputs. Keep Git index, commits, and integration under one owner. Use scripts for deterministic mechanics, and select configured worker roles appropriate to the lane.

Use compact context, reuse an existing worker for the same responsibility, and consume verified returns without duplicating successful work. As workers finish, launch further ready lanes within runtime capacity. Wait expiration does not cancel a worker; stop one only for user cancellation or a confirmed safety/scope violation. State the selected lane count and concrete constraints briefly when coordination matters.
<!-- codex-wide-delegation:end -->

<!-- codex-continuous-lanes:start -->
## Continuous lane scheduling

Policy version: `wide-delegation.1.1`.

Maintain a compact lane table for substantial work: deliverable, owner,
exclusive edit scope, dependencies, acceptance check, and
ready/running/blocked/done status.

Refresh it when a worker finishes or a dependency changes. Before waiting,
dispatch all substantial ready lanes within available capacity, up to ten
workers. Reuse suitable workers. Explicit task-specific limits still apply.

When capacity remains unused, identify the concrete blockers. Do not treat
sequential release gates as blocking independent investigation, test
preparation, or fixture work. Keep shared-state mutations exclusive and
dependent execution ordered; do not create filler tasks.

Never cancel workers merely because a wait expires. This guidance does not
alter verifier/process timeout settings or authorize bypassing release gates.
<!-- codex-continuous-lanes:end -->
