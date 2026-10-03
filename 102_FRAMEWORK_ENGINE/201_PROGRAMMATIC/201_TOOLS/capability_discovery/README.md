# Capability discovery and Run observation

Six canonical JSON Tools share a derived, read-only catalog:

- `discover_tools`: query, Scope Unit selection, availability, pagination.
- `discover_operations`: active Operations and their declared Tool bindings.
- `get_execution_context`: exact Atom ID or Tool name, content, direct referenced definitions and input schema where registered.
- `get_execution_status`: saved Run progress; `include_results` includes retained reports/history, with optional selection `ordinal`.
- `resume_execution_context`: original request, frozen selection/criteria, progress states and handoffs; no dispatch or fix admission.
- `watch_execution`: bounded async observation, cursor-based replay of confirmed Journal events and saved status changes.

Every CLI accepts `--project-root` and `--input FILE` (or `-` for standard input). MCP uses the same implementation, with the Project fixed at server startup.

Availability distinguishes source files from MCP registration, not installation verification. Catalog diagnostics report malformed or ambiguous sources. Discovery never executes a candidate entrypoint.

The registered observation backend currently supports RMED Atoms Base Revise. Unknown Runs are explicit errors. Action results use that Run's frozen selection ordinals; independent Action Run backends are not registered yet. A fixed report remains `fixed_not_rechecked`, not a clean check.

Notifications require a caller's wait request. They are not unsolicited host messages. Save the returned cursor and provide it on the next call. An observation timeout does not fail the underlying Run. Pending Journal appends are not confirmed notifications.

Restart the MCP connection after changing its server registrations.
