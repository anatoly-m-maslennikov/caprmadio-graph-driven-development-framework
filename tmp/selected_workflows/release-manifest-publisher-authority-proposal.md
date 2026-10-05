# Proposal: publish the additive selected Release manifest projection

## Gap

CA-D-572@5 defines the closed source-admission record a sixteen-route selected
workflow manifest must contain.  It does not authorize a programmatic publisher
to replace the current fifteen-route projection.  The existing loader validates
either already-materialized projection but intentionally has no publication
operation.

## Proposed bounded authority

Authorize one local publisher to create only the additive sixteen-route successor
of `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` when and
only when it first loads the current canonical fifteen-route projection through
the existing loader and derives the Release route and its admission record from
the active D572@5-declared source frontier.

The publisher must preserve the fifteen existing route rows, source freshness,
and query-source admissions byte-for-byte as input values; append exactly one
`release_version` row and the one derived `release_source_admissions` record;
recompute the binding and canonical digests; write atomically; then reload the
exact published bytes through the existing loader and confirm discovery of the
sixteen-route successor.  Its default operation is a non-writing plan/dry run;
only an explicit execute mode may write the projection.

## Explicit exclusions

This authority does not authorize Atom allocation, changes to D572/P1622/O164
or any source, caller approval, Release execution, Run/Journal creation,
dispatch, queue/Docker actions, credential use, a canonical manifest rewrite
other than the exact additive successor, or claims of runtime/full-release
acceptance.
