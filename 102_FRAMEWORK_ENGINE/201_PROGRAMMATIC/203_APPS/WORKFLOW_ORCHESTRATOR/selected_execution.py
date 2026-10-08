"""Interpret one frozen, source-bound selected Workflow through shared Run support.

This module deliberately has no route-domain branches.  The MCP-owned manifest
declares the Workflow, Steps, Action bindings and `On Result` transitions; the
TOOLS-owned Run tracker seals admission and Journal evidence.  This APPS layer
only freezes/rechecks the graph and gives registered native Action adapters the
actual Run context.
"""
from __future__ import annotations

from collections.abc import Callable, Mapping
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import tomllib
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


MANIFEST_DEFAULT = "_projection/selected_workflow_bindings.json"
RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
SECRET_TERMS = {"secret", "password", "token", "credential", "api_key", "apikey"}
ActionHandler = Callable[[dict[str, Any]], Mapping[str, Any]]


class SelectedExecutionError(RuntimeError):
    """A selected request cannot safely progress through the queue."""


class LifecycleAdmissionError(SelectedExecutionError):
    """A source-derived lifecycle refusal before queue or Run admission."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)

    def record(self) -> dict[str, str]:
        return {"code": self.code, "message": self.message}


def preflight_selected_lifecycle(root: Path, route: object, parameters: object) -> dict[str, Any] | None:
    """Admit a status request from its authoritative model before a Run exists.

    The native handler repeats this same source observation immediately before
    its effect.  This early check is intentionally only an admission gate: it
    does not retain caller-controlled model data or create Run/Journal state.
    """
    if route != "change_atom_status":
        return None
    import sys

    tools_root = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
    if tools_root not in sys.path:
        sys.path.insert(0, tools_root)
    try:
        import lifecycle_intents
    except ImportError as error:
        raise SelectedExecutionError("source-derived lifecycle admission is unavailable") from error
    try:
        preflight = lifecycle_intents.preflight_atom_lifecycle(
            Path(root), "change_status", parameters,
        )
    except lifecycle_intents.LifecycleError as error:
        raise LifecycleAdmissionError(error.code, str(error)) from error
    # This source-derived, serializable seal is retained only by the preview
    # observation and frozen queue request. It excludes the live Atom object
    # and accepts no caller-authored status model.
    return {
        "operation": preflight["operation"],
        "prior": dict(preflight["prior"]),
        "requested_status": preflight["requested_status"],
        "current_status": preflight["current_status"],
        "status_model": dict(preflight["status_model"]),
        "archive": preflight["archive"],
    }


def manifest_relative_path(root: Path) -> str:
    """Locate the one Project-local selected Workflow projection."""
    root = root.resolve(strict=True)
    settings_paths = sorted(
        path for path in root.glob(".caprmedio_*/caprmedio_project_settings.toml")
        if path.is_file() and not path.is_symlink() and not path.parent.is_symlink()
    )
    if len(settings_paths) != 1:
        raise SelectedExecutionError("Project settings carrier is missing or ambiguous")
    settings_path = settings_paths[0]
    try:
        settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise SelectedExecutionError("Project settings carrier is invalid") from error
    paths = settings.get("paths", {})
    if not isinstance(paths, dict):
        raise SelectedExecutionError("Project control root is invalid")
    default = settings_path.parent.relative_to(root).as_posix()
    value = paths.get("control_root", default)
    if not isinstance(value, str) or not value:
        raise SelectedExecutionError("Project control root is invalid")
    control = Path(value)
    control_path = root / control
    if (control.is_absolute() or ".." in control.parts or control.as_posix() in {"", "."}
            or control_path.is_symlink() or not control_path.is_dir()):
        raise SelectedExecutionError("Project control root is invalid")
    try:
        control_path.resolve().relative_to(root)
    except ValueError as error:
        raise SelectedExecutionError("Project control root is invalid") from error
    return (control / MANIFEST_DEFAULT).as_posix()


def canonical_json(value: object) -> bytes:
    """Stable JSON bytes used only for frozen request and manifest comparisons."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _contains_secret(value: object) -> bool:
    if isinstance(value, Mapping):
        return any(str(key).lower().replace("-", "_") in SECRET_TERMS or _contains_secret(item)
                   for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_secret(item) for item in value)
    return False


def _frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    close = text.find("\n---\n", 4)
    if close < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:close].splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


_ACTION_HANDLERS: dict[str, ActionHandler] = {}
_IMPLEMENTATION_AGENT: Callable[[str, Mapping[str, Any]], Mapping[str, Any]] | None = None


def register_action_handler(action_definition_id: str, handler: ActionHandler) -> None:
    """Register a native Action adapter without adding a Workflow policy branch."""
    if not isinstance(action_definition_id, str) or not action_definition_id:
        raise ValueError("Action definition ID is required")
    if not callable(handler):
        raise TypeError("Action handler must be callable")
    previous = _ACTION_HANDLERS.get(action_definition_id)
    if previous is not None and previous is not handler:
        raise ValueError(f"Action handler already registered for {action_definition_id}")
    _ACTION_HANDLERS[action_definition_id] = handler


def register_implementation_agent(agent: Callable[[str, Mapping[str, Any]], Mapping[str, Any]]) -> None:
    """Install the explicit O016 Agent bridge for subsequently created queues."""
    if not callable(agent):
        raise TypeError("implementation agent must be callable")
    global _IMPLEMENTATION_AGENT
    if _IMPLEMENTATION_AGENT is not None and _IMPLEMENTATION_AGENT is not agent:
        raise ValueError("implementation agent is already registered")
    _IMPLEMENTATION_AGENT = agent


def make_revert_action_handler(service: Any) -> ActionHandler:
    """Adapt an injected CA-O-131 service to the shared selected-run session.

    The caller owns the governed ``observe`` and ``apply_effect`` capabilities
    used to construct ``service``.  This APPS module never substitutes file
    writes, hashes, or a second Journal for those capabilities.  Register the
    returned handler with ``register_action_handler('CA-O-131', handler)``.
    """
    execute = getattr(service, "execute_with_session", None)
    if not callable(execute):
        raise TypeError("revert service must expose execute_with_session")

    def handler(context: dict[str, Any]) -> dict[str, Any]:
        parameters = context.get("parameters")
        if not isinstance(parameters, Mapping):
            raise SelectedExecutionError("CA-O-131 requires a reversal parameter mapping")
        manifest = parameters.get("approved_reversal_manifest", parameters.get("reversal_manifest"))
        if not isinstance(manifest, Mapping):
            raise SelectedExecutionError("CA-O-131 requires an approved reversal manifest")
        result = execute(
            manifest, context["session"], context["requested_action_run_id"],
            parameters.get("cancel_after_effect_id"),
        )
        if not isinstance(result, Mapping) or not isinstance(result.get("outcome"), str):
            raise SelectedExecutionError("CA-O-131 returned an invalid reversal result")
        outcome = result["outcome"]
        terminal_outcome = {
            "reverted": "completed", "no_op": "no_op", "failed": "failed",
            "partial_failure": "partial", "blocked": "interrupted_pending",
            "canceled": "cancelled", "recording_blocked": "interrupted_pending",
        }.get(outcome, "interrupted_pending")
        account = result.get("effect_account", {})
        effects = account.get("effects", []) if isinstance(account, Mapping) else []
        manifest_id = result.get("manifest_id")
        effect_refs = [
            f".caprmedio_runtime/revert_changes/{manifest_id}:terminal/{item['effect_id']}"
            for item in effects
            if isinstance(item, Mapping) and item.get("status") == "completed"
            and isinstance(item.get("effect_id"), str) and isinstance(manifest_id, str)
        ]
        return {
            "result": outcome, "terminal_outcome": terminal_outcome,
            "effect_refs": effect_refs, "native_result": dict(result),
            # execute_with_session has already terminalized the actual Action
            # through the same lazy session.  Do not append a duplicate Action
            # terminal event from the generic interpreter.
            "action_terminal_recorded": bool(result.get("run_receipt_refs")),
        }

    return handler


class SelectedExecution:
    """Durable selected graph state at the APPS boundary."""

    def __init__(
        self,
        root: str | Path,
        *,
        handlers: Mapping[str, ActionHandler] | None = None,
        implementation_agent: Callable[[str, Mapping[str, Any]], Mapping[str, Any]] | None = None,
    ):
        self.root = Path(root).resolve(strict=True)
        self.implementation_agent = implementation_agent or _IMPLEMENTATION_AGENT
        self.handlers = {**self._native_handlers(), **_ACTION_HANDLERS}
        if handlers:
            self.handlers.update(handlers)

    def _native_handlers(self) -> dict[str, ActionHandler]:
        """Load available domain adapters without making them graph policy owners.

        Each adapter receives only its Action context.  Source `result_map`
        values are interpreted below from the frozen manifest, so native tools
        never choose a successor Step.
        """
        import sys
        tools_root = Path(__file__).resolve().parents[2] / "201_TOOLS"
        for path in (tools_root, tools_root / "WORKFLOW_OPERATIONS" / "PROJECT_STRUCTURE",
                     tools_root / "GENERATE_ENTITY_GRAPH", tools_root / "COMPILE_APPLICABLE_METHODOLOGY",
                     Path(__file__).resolve().parents[3] / "202_AGENTIC" / "202_PROMPTS" / "ACTION_PROMPTS" / "IMPLEMENTATION_WORKFLOW"):
            text = str(path)
            if text not in sys.path:
                sys.path.insert(0, text)
        available: dict[str, ActionHandler] = {}

        def paths(value: object) -> list[str]:
            """Retain only real, repository-relative effect references."""
            candidates = value.get("paths", []) if isinstance(value, Mapping) else value
            if not isinstance(candidates, list):
                return []
            output: list[str] = []
            for item in candidates:
                if isinstance(item, str):
                    output.append(item)
                elif isinstance(item, Mapping):
                    carrier = item.get("carrier")
                    candidate = item.get("path")
                    if not isinstance(candidate, str) and isinstance(carrier, Mapping):
                        candidate = carrier.get("path")
                    if isinstance(candidate, str):
                        output.append(candidate)
            return sorted(set(output))

        try:
            import lifecycle_intents

            lifecycle = {
                "create_atom": lifecycle_intents.create_atom_action,
                "update_atom": lifecycle_intents.update_atom_action,
                "replace_atom": lifecycle_intents.replace_atom_action,
                "change_atom_status": lifecycle_intents.change_status_atom_action,
            }

            def admitted_update_assessment(context: Mapping[str, Any]) -> dict[str, Any] | None:
                """Return the one completed O145 seal for this frozen Update input."""
                prior_results = context.get("lifecycle_prior_results")
                if not isinstance(prior_results, list):
                    return None
                expected_digest = lifecycle_intents.update_assessment_seal(context["parameters"])["request_digest"]
                matches: list[dict[str, Any]] = []
                for prior in prior_results:
                    if not isinstance(prior, Mapping):
                        continue
                    native = prior.get("native_result")
                    receipt = prior.get("completed_receipt")
                    if (prior.get("step_definition_id") != "CA-O-145"
                            or prior.get("action_definition_id") != "CA-O-067"
                            or prior.get("result") != "identity-preserving"
                            or not isinstance(native, Mapping)
                            or not isinstance(receipt, Mapping)
                            or receipt.get("disposition") != "terminal"
                            or receipt.get("outcome") != "completed"):
                        continue
                    assessment = native.get("assessment")
                    if isinstance(assessment, Mapping) and assessment.get("request_digest") == expected_digest:
                        matches.append(dict(assessment))
                return matches[0] if len(matches) == 1 else None

            def atom_lifecycle(context: dict[str, Any]) -> dict[str, Any]:
                action = lifecycle.get(context["route"])
                if action is None:
                    return {"result": "blocked", "effect_refs": []}
                call: dict[str, Any] = {"execute": True, "authorized": True}
                if context["route"] == "update_atom":
                    assessment = admitted_update_assessment(context)
                    if assessment is None:
                        return {"result": "reassessment-required", "terminal_outcome": "interrupted_pending", "effect_refs": []}
                    call["assessment"] = assessment
                if context["route"] == "replace_atom":
                    return replacement_atom(context, action, call)
                result = action(self.root, context["parameters"], **call)
                native_outcome = result.get("outcome")
                result_label = {"duplicate": "no-op", "no-op": "no-op"}.get(native_outcome, native_outcome)
                terminal_outcome = {
                    "applied": "completed", "no-op": "no_op", "duplicate": "no_op",
                    "failed": "failed", "partial": "partial", "canceled": "cancelled",
                    "recording-blocked": "interrupted_pending", "blocked": "interrupted_pending",
                }.get(native_outcome, "interrupted_pending")
                effects = result.get("effects")
                changed_effects = [
                    effect for effect in effects
                    if isinstance(effect, Mapping) and effect.get("state") == "changed"
                ] if isinstance(effects, list) else []
                effect_refs = paths(changed_effects)
                history = result.get("history")
                prior_revision = history.get("prior_revision") if isinstance(history, Mapping) else None
                if isinstance(prior_revision, Mapping) and isinstance(prior_revision.get("path"), str):
                    effect_refs = sorted({*effect_refs, prior_revision["path"]})
                return {"result": result_label, "terminal_outcome": terminal_outcome,
                        "effect_refs": effect_refs, "native_result": result}

            def replacement_atom(
                context: dict[str, Any], action: Callable[..., Mapping[str, Any]], call: Mapping[str, Any],
            ) -> dict[str, Any]:
                """Execute O051 once as O128's predeclared source-bound child.

                The predecessor Journal result and the current shared Journal
                context are verified before the lifecycle Tool is allowed to
                create a successor or archive the predecessor.  After a real
                effect, all recording failures retain that fact as partial and
                never expose a completed edge that could replay it.
                """
                session = context.get("session")
                requested_child = context.get("replacement_requested_run_id")
                binding = context.get("replacement_action_binding")
                writer = context.get("replacement_result_writer")
                if (
                    session is None or not isinstance(requested_child, str) or not requested_child
                    or not isinstance(binding, Mapping) or not callable(writer)
                ):
                    return {"result": "replacement-recording-unavailable",
                            "terminal_outcome": "interrupted_pending", "effect_refs": []}
                try:
                    prior_event_id = self._replacement_prior_result_event(context.get("parameters"))
                    author, local_date, timezone, occurred_at = self._replacement_journal_context(session)
                    structural_scope = self._replacement_structural_scope(binding)
                except SelectedExecutionError:
                    return {"result": "predecessor-journal-required",
                            "terminal_outcome": "interrupted_pending", "effect_refs": []}

                # A recovered or retained child is evidence of an earlier
                # invocation.  This executor cannot manufacture a second O051
                # effect for that requested identity.
                if requested_child in getattr(session, "actual", {}):
                    return {"result": "replacement-recovery-required",
                            "terminal_outcome": "interrupted_pending", "effect_refs": []}
                try:
                    child_actual = session.start_run(requested_child)
                    child_run_id = child_actual["run_id"]
                    result = action(self.root, context["parameters"], **dict(call))
                except Exception:
                    # The shared session's normal interruption handling owns
                    # unexpected Tool failures.  No parent success or edge is
                    # fabricated here.
                    raise
                if not isinstance(result, Mapping) or not isinstance(result.get("outcome"), str):
                    raise SelectedExecutionError("replacement Action returned an invalid result")
                result = dict(result)
                native_outcome = result["outcome"]
                changed_effects = [
                    effect for effect in result.get("effects", [])
                    if isinstance(effect, Mapping) and effect.get("state") == "changed"
                ] if isinstance(result.get("effects"), list) else []
                effect_refs = paths(changed_effects)
                canonical_event: Mapping[str, Any] | None = None
                recording: Mapping[str, Any] | None = None
                recording_error: str | None = None
                if native_outcome == "applied":
                    try:
                        canonical_event = self._replacement_canonical_event(
                            parameters=context.get("parameters"), native_result=result,
                            prior_event_id=prior_event_id, replacement_binding=binding,
                            replacement_action_run_id=child_run_id,
                            execution_request_id=context.get("execution_request_id"),
                            author=author, occurred_at=occurred_at,
                            structural_scope=structural_scope,
                        )
                    except SelectedExecutionError as error:
                        recording_error = str(error)
                try:
                    payload: dict[str, Any] = {
                        "replacement_action_run_id": child_run_id,
                        "native_result": result,
                    }
                    if canonical_event is not None:
                        payload["canonical_event"] = dict(canonical_event)
                    if recording_error is not None:
                        payload["recording_error"] = recording_error
                    result_ref = writer(payload)
                    if not isinstance(result_ref, str) or not result_ref:
                        raise SelectedExecutionError("replacement result writer returned an invalid reference")
                except Exception:
                    # There is no durable child result carrier from which to
                    # retain an honest partial observation; let the shared
                    # session interrupt the open Runs rather than invent one.
                    raise

                if canonical_event is not None:
                    try:
                        import selected_replacement_journal
                        import work_journal
                        append_context = work_journal.seal_append_context(
                            self.root, canonical_event, author=author,
                            local_date=local_date, timezone=timezone,
                        )
                        selected_replacement_journal.preflight(
                            self.root, canonical_event, append_context,
                        )
                        recording = selected_replacement_journal.record_selected_replacement(
                            self.root, canonical_event=canonical_event,
                            append_context=append_context,
                        )
                    except Exception as error:
                        # The effect is already real.  The saved child carrier
                        # plus its Session effect observation makes this a
                        # partial recording state, not a success or replay.
                        recording_error = type(error).__name__

                child_outcome = {
                    "applied": "completed", "no-op": "no_op", "duplicate": "no_op",
                    "failed": "failed", "partial": "partial", "canceled": "cancelled",
                    "recording-blocked": "interrupted_pending", "blocked": "interrupted_pending",
                }.get(native_outcome, "interrupted_pending")
                if native_outcome == "applied" and (
                    recording_error is not None
                    or not isinstance(recording, Mapping)
                    or recording.get("state") != "completed"
                ):
                    child_outcome = "partial"
                if effect_refs:
                    session.note_effects(child_run_id, result_ref=result_ref, effect_refs=effect_refs)
                child_receipt = session.finish_run(
                    child_run_id, outcome=child_outcome, result_ref=result_ref, effect_refs=effect_refs,
                )
                child_recorded = (
                    isinstance(child_receipt, Mapping)
                    and child_receipt.get("disposition") == "terminal"
                    and child_receipt.get("outcome") == "completed"
                )
                if native_outcome == "applied" and (
                    not child_recorded
                    or not isinstance(recording, Mapping)
                    or recording.get("state") != "completed"
                ):
                    return {
                        "result": "recording-pending", "terminal_outcome": "partial",
                        "effect_refs": effect_refs, "native_result": result,
                        "replacement_recording": recording,
                        "replacement_child_receipt": child_receipt,
                    }
                result_label = {"duplicate": "no-op", "no-op": "no-op"}.get(native_outcome, native_outcome)
                return {
                    "result": result_label, "terminal_outcome": child_outcome,
                    "effect_refs": effect_refs, "native_result": result,
                    "replacement_recording": recording,
                    "replacement_child_receipt": child_receipt,
                }

            def assess_update_identity(context: dict[str, Any]) -> dict[str, Any]:
                """CA-O-067 is a read-only assessment; O145 owns its edge."""
                result = lifecycle_intents.update_atom_action(
                    self.root, context["parameters"], execute=False, authorized=True
                )
                native_outcome = result.get("outcome")
                if native_outcome == "replace_handoff":
                    return {"result": "replacement-required", "terminal_outcome": "interrupted_pending",
                            "effect_refs": [], "native_result": result}
                if native_outcome in {"preview", "no-op"}:
                    evidence = result.get("assessment_evidence")
                    if not isinstance(evidence, Mapping):
                        return {"result": "unresolved", "terminal_outcome": "interrupted_pending",
                                "effect_refs": [], "native_result": result}
                    result["assessment"] = lifecycle_intents.update_assessment_seal(context["parameters"], evidence)
                    return {"result": "identity-preserving", "effect_refs": [], "native_result": result}
                return {"result": str(native_outcome or "blocked"), "terminal_outcome": "interrupted_pending",
                        "effect_refs": [], "native_result": result}

            available["CA-O-128"] = atom_lifecycle
            available["CA-O-067"] = assess_update_identity
        except ImportError:
            pass
        try:
            import project_structure

            structural_handlers = project_structure.queue_action_handlers(self.root)
            structural_results = {
                ("CA-O-004", "selected"): "current sources selected",
                ("CA-O-012", "prepared"): "proposal ready",
                ("CA-O-005", "accepted"): "checks complete",
                ("CA-O-013", "authorized"): "authorization valid",
                ("CA-O-014", "completed"): "cutover completed",
                ("CA-O-014", "no_op"): "cutover completed",
            }

            def structure(context: dict[str, Any]) -> dict[str, Any]:
                """O015-only adapter; shared O004/O005 are never global aliases."""
                action_id = context["action_definition_id"]
                handler = structural_handlers.get(action_id)
                if handler is None:
                    return {"result": "blocked", "terminal_outcome": "interrupted_pending", "effect_refs": []}
                result = handler(context)
                if not isinstance(result, Mapping) or not isinstance(result.get("result"), str):
                    raise SelectedExecutionError("Project Structure Action returned an invalid queue envelope")
                native_result = result.get("native_result")
                effect_refs = result.get("effect_refs", [])
                label = structural_results.get((action_id, result["result"]), result["result"])
                output: dict[str, Any] = {"result": label, "effect_refs": effect_refs,
                                          "native_result": native_result}
                if label in {"blocked", "stale", "conflict"}:
                    output["terminal_outcome"] = "interrupted_pending"
                elif action_id == "CA-O-005" and context["step_definition_id"] == "CA-O-144":
                    # O144 has no outgoing On Result edge; the adapter's accepted
                    # current-state assessment is its declared terminal evidence.
                    output["terminal_outcome"] = "completed"
                return output

            for action_id in structural_handlers:
                available[action_id] = structure
        except ImportError:
            pass
        try:
            import generate_entity_graph
            for action_id, handler in generate_entity_graph.queue_action_handlers(self.root).items():
                def graph_projection(context: dict[str, Any], handler: Any = handler) -> dict[str, Any]:
                    result = handler(context)
                    if not isinstance(result, Mapping) or not isinstance(result.get("result"), str):
                        raise SelectedExecutionError("graph projection Action returned an invalid queue envelope")
                    label = result["result"]
                    native_result = result.get("graph_result", result)
                    output = {**result, "native_result": native_result}
                    if label == "built":
                        output["terminal_outcome"] = "completed"
                    elif label == "no_op":
                        output["terminal_outcome"] = "no_op"
                    elif label == "failed":
                        output["terminal_outcome"] = "failed"
                    elif label in {"blocked", "pending_recording", "stale", "incomplete", "conflicting"}:
                        output["terminal_outcome"] = "interrupted_pending"
                    return output
                available[action_id] = graph_projection
        except ImportError:
            pass
        def revert_not_configured(_context: dict[str, Any]) -> dict[str, Any]:
            """Refuse CA-O-131 before its governed service can apply an effect."""
            raise SelectedExecutionError(
                "CA-O-131 requires register_action_handler('CA-O-131', make_revert_action_handler(service))"
            )

        available["CA-O-131"] = revert_not_configured
        try:
            import implementation_actions
            for action_id, handler in implementation_actions.ACTION_HANDLERS.items():
                def implementation(context: dict[str, Any], handler: Any = handler) -> dict[str, Any]:
                    result = handler(
                        context["parameters"], agent=self.implementation_agent,
                        selected_project_root=self.root,
                        trusted_execution_authorization=context.get("trusted_execution_authorization"),
                    )
                    if not isinstance(result, Mapping) or not isinstance(result.get("result"), str):
                        raise SelectedExecutionError("implementation Action returned an invalid queue envelope")
                    # Result labels are the source Workflow's edge conditions.
                    # A stale projection cannot translate them into a second,
                    # competing result vocabulary.
                    label = result["result"]
                    output: dict[str, Any] = {"result": label, "effect_refs": [], "native_result": result}
                    if label in {"blocked", "retry_blocked", "unresolved", "authority_change_required", "environment_blocker"}:
                        output["terminal_outcome"] = "interrupted_pending"
                    return output
                available[action_id] = implementation
        except ImportError:
            pass
        try:
            import compile_applicable_methodology
            for action_id, handler in compile_applicable_methodology.ACTION_ADAPTERS.items():
                structural_handler = available.get(action_id)

                def compiler(context: dict[str, Any], handler: Any = handler,
                             structural_handler: ActionHandler | None = structural_handler) -> dict[str, Any]:
                    if context["workflow_definition_id"] != "CA-O-011":
                        if structural_handler is not None:
                            return dict(structural_handler(context))
                        return {"result": "blocked", "terminal_outcome": "interrupted_pending", "effect_refs": []}
                    result = handler(self._compiler_parameters_for_executor(context))
                    if not isinstance(result, Mapping) or not isinstance(result.get("outcome"), str):
                        raise SelectedExecutionError("compiler Action returned an invalid result")
                    outcome = result["outcome"]
                    step_id = context["step_definition_id"]
                    output: dict[str, Any] = {"result": outcome, "effect_refs": [], "native_result": result}
                    if (step_id == "CA-O-157" and context["action_definition_id"] == "CA-O-009"
                            and outcome == "pending_recording" and result.get("apply_status") == "APPLIED"):
                        publication = result.get("publication")
                        frontier = result.get("source_frontier_digest")
                        planned = publication.get("output_plan") if isinstance(publication, Mapping) else None
                        output_digest = publication.get("output_digest") if isinstance(publication, Mapping) else None
                        if (not isinstance(frontier, str) or not frontier or not isinstance(output_digest, str)
                                or not output_digest or not isinstance(planned, list)):
                            output.update(result="blocked", terminal_outcome="interrupted_pending")
                        else:
                            paths = sorted({
                                item["output_path"] for item in planned
                                if isinstance(item, Mapping) and isinstance(item.get("output_path"), str)
                            })
                            if len(paths) != len(planned):
                                output.update(result="blocked", terminal_outcome="interrupted_pending")
                            else:
                                output.update(
                                    result="publication recording required",
                                    # The graph remains interim until its completed Action receipt is
                                    # persisted below; this requests that receipt's terminal outcome.
                                    terminal_outcome="completed",
                                    effect_refs=paths,
                                    compiler_publication_recording={
                                        "on_recorded_result": "completed publication from the still-valid final frontier",
                                        "source_frontier_digest": frontier,
                                        "output_digest": output_digest,
                                        "output_paths": paths,
                                    },
                                )
                    elif (step_id == "CA-O-157" and context["action_definition_id"] == "CA-O-009"
                          and outcome == "publication_recovery_required"
                          and result.get("apply_status") == "EFFECT_APPLIED_STALE"):
                        publication = result.get("publication")
                        planned = publication.get("output_plan") if isinstance(publication, Mapping) else None
                        effect_state = publication.get("effect_state") if isinstance(publication, Mapping) else None
                        refs = self._publication_output_paths(planned)
                        # The compiler reports this only after replacement.  Its
                        # top-level plan must exactly be the observed
                        # publication plan; otherwise an arbitrary result
                        # carrier cannot claim already-applied effects.
                        if (effect_state != "output_replacement_completed"
                                or result.get("output_plan") != planned or refs is None):
                            output["terminal_outcome"] = "interrupted_pending"
                        else:
                            # Preserve the compiler's raw recovery-required
                            # result while terminalizing the known performed,
                            # incomplete effect.  No graph successor is
                            # inferred from this receipt.
                            output.update(terminal_outcome="partial", effect_refs=refs)
                    elif outcome in {"blocked", "pending_recording"}:
                        output["terminal_outcome"] = "interrupted_pending"
                    elif step_id == "CA-O-152" and outcome == "assessed":
                        output["result"] = "complete exact selection"
                    elif step_id == "CA-O-153" and outcome == "assessed" and (
                        result.get("unresolved_conflict_count") == 0 and result.get("can_apply") is True
                    ):
                        output["result"] = "required checks complete, no unresolved conflict, required approvals valid"
                    elif step_id == "CA-O-157" and outcome == "published":
                        output["result"] = "completed publication from the still-valid final frontier"
                        publication = result.get("publication")
                        planned = publication.get("output_plan", []) if isinstance(publication, Mapping) else []
                        output["effect_refs"] = sorted({
                            item["output_path"] for item in planned
                            if isinstance(item, Mapping) and isinstance(item.get("output_path"), str)
                        })
                    else:
                        # The compiler Action deliberately does not manufacture
                        # source corrections or decisions.  A result that does
                        # not exactly satisfy one reviewed edge pauses instead
                        # of becoming an inferred continuation.
                        output["terminal_outcome"] = "interrupted_pending"
                    return output
                available[action_id] = compiler
        except ImportError:
            pass
        try:
            import query_actions

            available.update(query_actions.ACTION_HANDLERS)
        except ImportError:
            pass
        return available

    def _compiler_parameters_for_executor(self, context: Mapping[str, Any]) -> dict[str, Any]:
        """Bind the compiler's path reference to this Action executor only.

        The frozen request describes the host Project when the Action is
        admitted.  A Docker worker sees that same Project at ``/project``.
        Preserve every frozen value other than the execution-local path, and
        refuse a missing or substituted executor root rather than letting an
        Action select an arbitrary filesystem root.
        """
        parameters = context.get("parameters")
        if not isinstance(parameters, Mapping):
            raise SelectedExecutionError("compiler Action frozen parameters are invalid")
        frozen_root = parameters.get("project_root")
        if not isinstance(frozen_root, str) or not frozen_root:
            raise SelectedExecutionError("compiler Action frozen Project root is invalid")
        executor_root = context.get("project_root")
        if not isinstance(executor_root, Path) or executor_root != self.root:
            raise SelectedExecutionError("compiler Action execution Project root is invalid")
        request = dict(parameters)
        request["project_root"] = executor_root.as_posix()
        return request

    @staticmethod
    def _publication_output_paths(plan: object) -> list[str] | None:
        """Return the exact, safe output references in a compiler plan.

        These are receipt references, not a fresh filesystem observation: the
        compiler's stale-frontier outcome is specifically the evidence that
        replacement happened before currentness was lost.
        """
        if not isinstance(plan, list):
            return None
        paths: list[str] = []
        for item in plan:
            if not isinstance(item, Mapping):
                return None
            output_path = item.get("output_path")
            if (not isinstance(output_path, str) or not output_path
                    or "\\x00" in output_path or "\\" in output_path):
                return None
            candidate = Path(output_path)
            if candidate.is_absolute() or candidate == Path(".") or ".." in candidate.parts:
                return None
            if candidate.as_posix() != output_path:
                return None
            paths.append(output_path)
        if len(paths) != len(set(paths)):
            return None
        return sorted(paths)

    @staticmethod
    def _graph_parameters_with_actual_recording(
        parameters: object,
        session: Any,
        *,
        workflow_run_id: str,
        step_run_id: str,
        action_run_id: str,
    ) -> object:
        """Replace caller recording claims with this Action's real start receipt.

        Graph publication occurs after the shared session has recorded the
        actual Action start and before it can append the terminal fact.  The
        injected object is intentionally execution-local rather than part of
        the sealed caller parameter JSON, so an arbitrary ``receipt_refs``
        array cannot satisfy the graph Tool's recording gate.
        """

        if not isinstance(parameters, Mapping):
            return parameters
        receipts = getattr(session, "receipts", None)
        if not isinstance(receipts, list) or not receipts or not isinstance(receipts[-1], Mapping):
            return parameters
        try:
            import generate_entity_graph
        except ImportError:
            return parameters
        try:
            recording = generate_entity_graph.actual_run_recording_context(
                workflow_run_id, step_run_id, action_run_id, receipts[-1]
            )
        except generate_entity_graph.EntityGraphError:
            # Leave the caller shape intact.  The graph Tool then reports its
            # stable recording-context blocker without an effect.
            return parameters
        return {**parameters, "run_recording_context": recording}

    def run_directory(self, run_id: str) -> Path:
        if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
            raise SelectedExecutionError("invalid selected Run ID")
        folder = self.root / ".caprmedio_install/workflow_orchestrator/runs" / run_id
        cursor = self.root
        for part in folder.relative_to(self.root).parts:
            cursor = cursor / part
            if cursor.is_symlink() or (cursor.exists() and not cursor.is_dir()):
                raise SelectedExecutionError("selected Run directory contains an unsafe carrier")
        return folder

    def _safe_path(self, relative: str) -> Path:
        if not isinstance(relative, str) or not relative:
            raise SelectedExecutionError("definition path is required")
        candidate = self.root / relative
        if Path(relative).is_absolute() or ".." in Path(relative).parts:
            raise SelectedExecutionError("unsafe definition path")
        try:
            resolved = candidate.resolve(strict=True)
            resolved.relative_to(self.root)
        except (OSError, ValueError, FileNotFoundError) as error:
            raise SelectedExecutionError("unsafe or unavailable definition path") from error
        cursor = self.root
        for part in Path(relative).parts:
            cursor /= part
            if cursor.is_symlink():
                raise SelectedExecutionError("definition symlinks are not admitted")
        if not resolved.is_file():
            raise SelectedExecutionError("definition path is not a file")
        return resolved

    @staticmethod
    def _write(path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", delete=False) as temporary:
            temporary.write(canonical_json(value))
            temporary.flush()
            os.fsync(temporary.fileno())
            temporary_path = Path(temporary.name)
        temporary_path.replace(path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)

    @staticmethod
    def _read(path: Path) -> dict[str, Any]:
        if path.is_symlink():
            raise SelectedExecutionError("saved selected execution evidence cannot be a symlink")
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise SelectedExecutionError("invalid saved selected execution evidence") from error
        if not isinstance(value, dict):
            raise SelectedExecutionError("invalid saved selected execution evidence")
        return value

    @staticmethod
    def _manifest_without_digest(manifest: dict[str, Any]) -> dict[str, Any]:
        value = dict(manifest)
        value.pop("canonical_manifest_sha256", None)
        return value

    def _load_manifest(self, execution: Mapping[str, Any]) -> tuple[dict[str, Any], str, str]:
        manifest_ref = execution.get("definition_manifest", {}).get("manifest_ref") if isinstance(
            execution.get("definition_manifest"), Mapping) else None
        manifest_digest = execution.get("definition_manifest", {}).get("manifest_digest") if isinstance(
            execution.get("definition_manifest"), Mapping) else None
        if not isinstance(manifest_ref, str) or not isinstance(manifest_digest, str):
            raise SelectedExecutionError("selected definition manifest is required")
        path = self._safe_path(manifest_ref)
        if path.relative_to(self.root).as_posix() != manifest_relative_path(self.root):
            raise SelectedExecutionError("selected definition manifest location is not admitted")
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise SelectedExecutionError("invalid selected definition manifest") from error
        if not isinstance(manifest, dict):
            raise SelectedExecutionError("invalid selected definition manifest")
        canonical_digest = manifest.get("canonical_manifest_sha256")
        expected = _sha256(canonical_json(self._manifest_without_digest(manifest)))
        if canonical_digest != expected or manifest_digest != expected:
            raise SelectedExecutionError("selected definition manifest digest is stale or invalid")
        return manifest, manifest_ref, expected

    @staticmethod
    def _route(manifest: Mapping[str, Any], route: str) -> dict[str, Any]:
        rows = manifest.get("routes")
        if not isinstance(rows, list):
            raise SelectedExecutionError("selected definition manifest routes are invalid")
        matches = [row for row in rows if isinstance(row, dict) and row.get("route") == route]
        if len(matches) != 1:
            raise SelectedExecutionError("selected route is not admitted by the definition manifest")
        return matches[0]

    def _definition(self, binding: Mapping[str, Any], *, expected_kind: str) -> dict[str, Any]:
        """Validate either the D547 source pin or the legacy test pin shape."""
        if {"atom_id", "version", "source_path", "digest"} <= set(binding):
            normalized = {
                "atom_id": binding["atom_id"], "kind": expected_kind,
                "version": binding["version"], "path": binding["source_path"],
                "sha256": binding["digest"],
            }
        elif {"atom_id", "kind", "version", "path", "sha256"} <= set(binding):
            normalized = dict(binding)
        else:
            raise SelectedExecutionError(f"invalid {expected_kind} definition binding")
        if normalized.get("kind") != expected_kind:
            raise SelectedExecutionError(f"invalid {expected_kind} definition binding")
        if not isinstance(normalized["atom_id"], str) or not isinstance(normalized["version"], int):
            raise SelectedExecutionError(f"invalid {expected_kind} definition identity")
        if not isinstance(normalized["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", normalized["sha256"]):
            raise SelectedExecutionError(f"invalid {expected_kind} definition digest")
        path = self._safe_path(str(normalized["path"]))
        if _sha256(path.read_bytes()) != normalized["sha256"]:
            raise SelectedExecutionError(f"{expected_kind} definition changed after admission")
        metadata = _frontmatter(path)
        if metadata.get("atom_id") != normalized["atom_id"] or metadata.get("version") != str(normalized["version"]):
            raise SelectedExecutionError(f"{expected_kind} definition identity changed after admission")
        return normalized

    def _d547_steps(self, route: Mapping[str, Any]) -> tuple[list[dict[str, Any]], str]:
        """Translate source-bound D547 edges without adding a route policy.

        A current source Workflow graph table wins over its serialized manifest
        projection.  That keeps labels and branches bound to the admitted
        source bytes, while manifests without this table retain their existing
        D547 representation.  A missing edge is intentionally *not*
        interpreted as a successor: a native adapter must return a truthful
        ``terminal_outcome`` for that source result.
        """
        ordered = route.get("ordered_steps")
        entry = route.get("entry_step")
        if not isinstance(ordered, list) or not ordered or not isinstance(entry, str):
            raise SelectedExecutionError("D547 selected Workflow must bind ordered Steps and entry_step")
        normalized: list[dict[str, Any]] = []
        seen_steps: set[str] = set()
        for raw in ordered:
            if not isinstance(raw, Mapping) or set(raw) != {"step", "action"}:
                raise SelectedExecutionError("D547 selected ordered Step/Action binding is invalid")
            step = self._definition(raw["step"], expected_kind="step")
            action = self._definition(raw["action"], expected_kind="action")
            if step["atom_id"] in seen_steps:
                raise SelectedExecutionError("D547 selected Workflow has duplicate Step bindings")
            seen_steps.add(step["atom_id"])
            step["actions"] = [action]
            normalized.append(step)
        source_edges = self._source_bound_d547_edges(route, seen_steps)
        raw_edges = source_edges if source_edges is not None else route.get("on_result")
        if not isinstance(raw_edges, list):
            raise SelectedExecutionError("D547 selected Workflow On Result bindings are invalid")
        transitions: dict[str, list[dict[str, Any]]] = {}
        pairs: set[tuple[str, str]] = set()
        for raw in raw_edges:
            if not isinstance(raw, Mapping) or set(raw) != {"from", "condition", "to"}:
                raise SelectedExecutionError("D547 selected On Result binding is invalid")
            source, condition, target = raw["from"], raw["condition"], raw["to"]
            if not all(isinstance(value, str) and value for value in (source, condition, target)):
                raise SelectedExecutionError("D547 selected On Result binding has an invalid endpoint")
            if (source, condition) in pairs:
                raise SelectedExecutionError("D547 selected Workflow has duplicate On Result conditions")
            pairs.add((source, condition))
            transition = {"result": condition}
            if source_edges is not None:
                terminal = {"completed": "completed", "blocked": "interrupted_pending"}.get(target)
                if terminal is not None:
                    transition["terminal"] = terminal
                elif target in seen_steps:
                    transition["next"] = target
                else:
                    raise SelectedExecutionError("D547 source Workflow has an undeclared terminal result")
            elif target == "complete":
                transition["terminal"] = "completed"
            else:
                transition["next"] = target
            transitions.setdefault(source, []).append(transition)
        for step in normalized:
            step["on_result"] = transitions.get(step["atom_id"], [])
        if entry not in seen_steps:
            raise SelectedExecutionError("D547 selected Workflow entry_step is not bound")
        for source, values in transitions.items():
            if source not in seen_steps:
                raise SelectedExecutionError("D547 On Result source is not a bound Step")
            for transition in values:
                target = transition.get("next")
                if target is not None and target not in seen_steps:
                    raise SelectedExecutionError("D547 On Result target is not a bound Step")
        return normalized, entry

    def _source_bound_d547_edges(
        self, route: Mapping[str, Any], bound_steps: set[str],
    ) -> list[dict[str, str]] | None:
        """Read the admitted Workflow's canonical On Result table when present."""
        binding = route.get("workflow")
        if not isinstance(binding, Mapping):
            raise SelectedExecutionError("D547 selected Workflow binding is invalid")
        workflow = self._definition(binding, expected_kind="workflow")
        # W09 has an admitted canonical table whose newer graph deliberately
        # supersedes the stale serialized projection.  Other selected routes
        # keep their own existing manifest interpretation.
        if workflow["atom_id"] != "CA-O-016":
            return None
        source = self._safe_path(str(workflow["path"]))
        raw = source.read_bytes()
        if _sha256(raw) != workflow["sha256"]:
            raise SelectedExecutionError("Workflow definition changed while reading source graph")
        try:
            lines = raw.decode("utf-8").splitlines()
        except UnicodeDecodeError as error:
            raise SelectedExecutionError("Workflow definition is not UTF-8") from error
        header = "| From Step | Result condition | Next Step **or** terminal result |"
        indexes = [index for index, line in enumerate(lines) if line.strip() == header]
        if not indexes:
            return None
        separator = re.compile(r"\|\s*:?-{3,}:?\s*\|\s*:?-{3,}:?\s*\|\s*:?-{3,}:?\s*\|")
        if (len(indexes) != 1 or indexes[0] + 1 >= len(lines)
                or separator.fullmatch(lines[indexes[0] + 1].strip()) is None):
            raise SelectedExecutionError("D547 source Workflow On Result table is invalid")
        edges: list[dict[str, str]] = []
        for line in lines[indexes[0] + 2:]:
            stripped = line.strip()
            if not stripped.startswith("|"):
                break
            cells = [value.strip() for value in stripped.strip("|").split("|")]
            if len(cells) != 3 or not all(cells):
                raise SelectedExecutionError("D547 source Workflow On Result row is invalid")
            source_step, condition, target = cells
            if source_step not in bound_steps:
                raise SelectedExecutionError("D547 source Workflow On Result source is not a bound Step")
            edges.append({"from": source_step, "condition": condition, "to": target})
        if not edges:
            raise SelectedExecutionError("D547 source Workflow On Result table has no edges")
        return edges

    def _validate_graph(self, execution: Mapping[str, Any]) -> dict[str, Any]:
        if _contains_secret(execution):
            raise SelectedExecutionError("selected execution carries a secret field")
        if execution.get("mode") != "execute":
            raise SelectedExecutionError("enqueue_selected accepts only an execute request")
        route_name = execution.get("operation_route")
        if not isinstance(route_name, str) or not route_name:
            raise SelectedExecutionError("selected operation route is required")
        manifest, manifest_ref, manifest_digest = self._load_manifest(execution)
        route = self._route(manifest, route_name)
        manifest_freshness = manifest.get("source_freshness")
        if manifest_freshness is not None and (
            not isinstance(manifest_freshness, Mapping)
            or execution.get("source_freshness") != manifest_freshness
        ):
            raise SelectedExecutionError("selected request source freshness does not match definition manifest")
        workflow = route.get("workflow")
        if not isinstance(workflow, Mapping):
            raise SelectedExecutionError("selected Workflow binding is required")
        validated_workflow = self._definition(workflow, expected_kind="workflow")
        native_calls = route.get("native_action_calls", [])
        if not isinstance(native_calls, list):
            raise SelectedExecutionError("selected native Action bindings are invalid")
        validated_native_calls = [self._definition(binding, expected_kind="action") for binding in native_calls
                                  if isinstance(binding, Mapping)]
        if len(validated_native_calls) != len(native_calls):
            raise SelectedExecutionError("selected native Action binding is invalid")
        steps = route.get("steps")
        entry_step: str | None = None
        if "ordered_steps" in route:
            validated_steps, entry_step = self._d547_steps(route)
            graph = {
                "route": route_name, "workflow": validated_workflow,
                "steps": validated_steps, "entry_step": entry_step,
                "native_action_calls": validated_native_calls,
                "manifest_ref": manifest_ref, "manifest_digest": manifest_digest,
            }
            return graph
        if not isinstance(steps, list) or not steps:
            raise SelectedExecutionError("selected Workflow must bind ordered Steps")
        validated_steps: list[dict[str, Any]] = []
        step_ids: set[str] = set()
        for raw_step in steps:
            if not isinstance(raw_step, Mapping):
                raise SelectedExecutionError("selected Step binding is invalid")
            step = self._definition(raw_step, expected_kind="step")
            if step["atom_id"] in step_ids:
                raise SelectedExecutionError("selected Workflow has duplicate Step bindings")
            step_ids.add(step["atom_id"])
            actions = raw_step.get("actions")
            if not isinstance(actions, list) or not actions:
                raise SelectedExecutionError("selected Step must bind ordered Actions")
            validated_actions = []
            for raw_action in actions:
                if not isinstance(raw_action, Mapping):
                    raise SelectedExecutionError("selected Action binding is invalid")
                action = self._definition(raw_action, expected_kind="action")
                validated_actions.append(action)
            transitions = raw_step.get("on_result")
            if not isinstance(transitions, list) or not transitions:
                raise SelectedExecutionError("selected Step must bind On Result transitions")
            step["actions"] = validated_actions
            step["on_result"] = [dict(item) for item in transitions if isinstance(item, Mapping)]
            if len(step["on_result"]) != len(transitions):
                raise SelectedExecutionError("selected On Result transition is invalid")
            validated_steps.append(step)
        graph = {
            "route": route_name,
            "workflow": validated_workflow,
            "steps": validated_steps,
            "entry_step": validated_steps[0]["atom_id"],
            "native_action_calls": validated_native_calls,
            "manifest_ref": manifest_ref,
            "manifest_digest": manifest_digest,
        }
        return graph

    @staticmethod
    def _validate_query_admission(graph: Mapping[str, Any], execution: Mapping[str, Any]) -> None:
        """Keep native query input rejection ahead of selected-Run dispatch."""
        if graph.get("route") not in {"find_and_fetch_artifacts", "find_and_fetch_journal_events"}:
            return
        steps = graph.get("steps")
        if not isinstance(steps, list) or len(steps) != 1 or not isinstance(steps[0], Mapping):
            raise SelectedExecutionError("query Workflow must bind exactly one Step")
        step = steps[0]
        actions = step.get("actions")
        if not isinstance(actions, list) or len(actions) != 1 or not isinstance(actions[0], Mapping):
            raise SelectedExecutionError("query Step must bind exactly one Action")
        try:
            import query_actions
        except ImportError as error:
            raise SelectedExecutionError("query request adapter is unavailable") from error
        try:
            query_actions.validate_query_parameters({
                "route": graph["route"],
                "workflow_definition_id": graph["workflow"]["atom_id"],
                "step_definition_id": step["atom_id"],
                "action_definition_id": actions[0]["atom_id"],
                "parameters": execution.get("parameters"),
            })
        except query_actions.QueryActionError as error:
            raise SelectedExecutionError("query request is not admitted") from error

    def _validate_lifecycle_admission(
        self, graph: Mapping[str, Any], execution: Mapping[str, Any], *,
        expected_admission: Mapping[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        """Run source-derived status admission at each pre-Run queue boundary."""
        current = preflight_selected_lifecycle(
            self.root, graph.get("route"), execution.get("parameters"),
        )
        if current is None:
            return None
        expected = expected_admission
        if expected is None:
            receipt = execution.get("proposal_receipt")
            freshness = receipt.get("source_freshness") if isinstance(receipt, Mapping) else None
            observed = freshness.get("observed") if isinstance(freshness, Mapping) else None
            expected = observed.get("lifecycle_admission") if isinstance(observed, Mapping) else None
        if not isinstance(expected, Mapping):
            raise LifecycleAdmissionError(
                "status-preview-admission-missing",
                "status execution requires the source-derived preview admission",
            )
        if canonical_json(dict(expected)) != canonical_json(current):
            raise LifecycleAdmissionError(
                "status-model-stale",
                "authoritative status-model source changed after lifecycle admission",
            )
        return current

    @staticmethod
    def _support_definition(binding: Mapping[str, Any]) -> dict[str, Any]:
        """Translate a manifest pin into the shared service's source pin shape."""
        return {"atom_id": binding["atom_id"], "version": binding["version"],
                "path": binding["path"], "digest": binding["sha256"]}

    @staticmethod
    def _replacement_child_requested_id(requested_action_run_id: str) -> str:
        """Name the one source-bound O051 invocation below one O128 visit."""
        return f"{requested_action_run_id}:nested:CA-O-051"

    @staticmethod
    def _replacement_native_binding(graph: Mapping[str, Any]) -> dict[str, Any]:
        """Return the sole admitted O051 binding for a W03 graph.

        O128's source names O051 as the effect owner.  The frozen D547 graph is
        therefore the only authority for this child Action definition; callers
        cannot supply another definition, version, or source path.
        """
        native_calls = graph.get("native_action_calls")
        if not isinstance(native_calls, list):
            raise SelectedExecutionError("replacement graph has no native Action bindings")
        matches = [binding for binding in native_calls
                   if isinstance(binding, Mapping) and binding.get("atom_id") == "CA-O-051"]
        if len(matches) != 1:
            raise SelectedExecutionError("replacement graph must bind exactly one CA-O-051 Action")
        binding = matches[0]
        required = {"atom_id", "kind", "version", "path", "sha256"}
        if set(binding) != required or binding.get("kind") != "action":
            raise SelectedExecutionError("replacement CA-O-051 Action binding is invalid")
        return dict(binding)

    @classmethod
    def build_requested_runs(
        cls,
        graph: Mapping[str, Any],
        run_id: str,
        run_visit_limits: Mapping[str, int] | None = None,
    ) -> list[dict[str, Any]]:
        """Build every caller-authorized selected Run before an execution starts.

        A Step's identity is its manifest position, not its traversal position.
        Callers may authorize a finite number of revisits for a manifest Step;
        each visit then has a separate requested Step and Action identity.  The
        shared lazy session creates Journal evidence only if this interpreter
        actually starts that predeclared identity.
        """
        if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
            raise SelectedExecutionError("invalid selected Run ID")
        steps = graph.get("steps")
        workflow = graph.get("workflow")
        if not isinstance(steps, list) or not isinstance(workflow, Mapping):
            raise SelectedExecutionError("selected Workflow graph is invalid")
        limits = cls._run_visit_limits(graph, run_visit_limits)
        expected: list[dict[str, Any]] = [{
            "requested_run_id": run_id,
            "kind": "workflow",
            "definition": cls._support_definition(workflow),
        }]
        for manifest_ordinal, step in enumerate(steps, start=1):
            step_id = step.get("atom_id")
            actions = step.get("actions")
            if not isinstance(step_id, str) or not isinstance(actions, list):
                raise SelectedExecutionError("selected Workflow graph is invalid")
            for visit in range(1, limits[step_id] + 1):
                requested_step_id = cls._requested_step_id(run_id, manifest_ordinal, visit)
                expected.append({
                    "requested_run_id": requested_step_id,
                    "kind": "step",
                    "definition": cls._support_definition(step),
                    "parent_requested_run_id": run_id,
                })
                for action_ordinal, action in enumerate(actions, start=1):
                    requested_action_id = f"{requested_step_id}:action:{action_ordinal}"
                    expected.append({
                        "requested_run_id": requested_action_id,
                        "kind": "action",
                        "definition": cls._support_definition(action),
                        "parent_requested_run_id": requested_step_id,
                    })
                    if (graph.get("route") == "replace_atom"
                            and action.get("atom_id") == "CA-O-128"):
                        replacement = cls._replacement_native_binding(graph)
                        expected.append({
                            "requested_run_id": cls._replacement_child_requested_id(requested_action_id),
                            "kind": "action",
                            "definition": cls._support_definition(replacement),
                            "parent_requested_run_id": requested_action_id,
                        })
        return expected

    @staticmethod
    def _requested_step_id(run_id: str, manifest_ordinal: int, visit: int) -> str:
        """Keep first-visit IDs compatible while making later visits explicit."""
        first_visit = f"{run_id}:step:{manifest_ordinal}"
        return first_visit if visit == 1 else f"{first_visit}:visit:{visit}"

    @staticmethod
    def _declared_run_visit_limits(execution: Mapping[str, Any]) -> Mapping[str, int] | None:
        parameters = execution.get("parameters")
        if not isinstance(parameters, Mapping):
            return None
        limits = parameters.get("run_visit_limits")
        if limits is None:
            return None
        if not isinstance(limits, Mapping):
            raise SelectedExecutionError("run_visit_limits must be a Step-to-positive-integer mapping")
        return limits

    @staticmethod
    def _run_visit_limits(
        graph: Mapping[str, Any], run_visit_limits: Mapping[str, int] | None,
    ) -> dict[str, int]:
        """Accept only explicit, finite revisit authority for bound Steps."""
        steps = graph.get("steps")
        if not isinstance(steps, list):
            raise SelectedExecutionError("selected Workflow graph is invalid")
        step_ids = [step.get("atom_id") for step in steps if isinstance(step, Mapping)]
        if len(step_ids) != len(steps) or any(not isinstance(step_id, str) for step_id in step_ids):
            raise SelectedExecutionError("selected Workflow graph is invalid")
        declared = dict(run_visit_limits or {})
        if set(declared) - set(step_ids):
            raise SelectedExecutionError("run_visit_limits includes an unbound Step")
        limits: dict[str, int] = {}
        for step_id in step_ids:
            limit = declared.get(step_id, 1)
            if type(limit) is not int or limit < 1 or limit > 100:
                raise SelectedExecutionError("run_visit_limits must contain positive bounded visit limits")
            limits[step_id] = limit
        return limits

    def _validate_requested_runs(self, execution: Mapping[str, Any], graph: Mapping[str, Any], run_id: str) -> None:
        """Require the caller's requested Runs to exactly bind every allowed visit."""
        requested = execution.get("requested_runs")
        if not isinstance(requested, list):
            raise SelectedExecutionError("selected execution must declare requested Runs")
        expected = self.build_requested_runs(
            graph, run_id, self._declared_run_visit_limits(execution),
        )
        if canonical_json(requested) != canonical_json(expected):
            raise SelectedExecutionError("requested Runs do not exactly bind the selected Workflow graph")

    @staticmethod
    def _workflow_identity(execution: Mapping[str, Any]) -> str | None:
        direct = execution.get("workflow_run_id")
        if isinstance(direct, str):
            return direct
        requested = execution.get("requested_runs")
        if isinstance(requested, list):
            workflow_rows = [row for row in requested if isinstance(row, Mapping) and row.get("kind") == "workflow"]
            if len(workflow_rows) == 1 and isinstance(workflow_rows[0].get("requested_run_id"), str):
                return str(workflow_rows[0]["requested_run_id"])
        return None

    def _validated_freeze(self, request: Mapping[str, Any]) -> dict[str, Any]:
        """Build the exact immutable value before its durable request carrier write."""
        if not isinstance(request, Mapping) or request.get("operation") != "enqueue_selected":
            raise SelectedExecutionError("selected enqueue operation is required")
        run_id = request.get("run_id")
        execution = request.get("execution")
        if not isinstance(run_id, str) or not isinstance(execution, Mapping):
            raise SelectedExecutionError("selected run ID and execution are required")
        requested_workflow_id = self._workflow_identity(execution)
        if requested_workflow_id != run_id:
            raise SelectedExecutionError("requested Workflow Run identity must match enqueue_selected run_id")
        graph = self._validate_graph(execution)
        self._validate_requested_runs(execution, graph, run_id)
        return {"request": {"operation": "enqueue_selected", "run_id": run_id,
                             "execution": dict(execution)}, "graph": graph}

    def freeze(self, request: Mapping[str, Any]) -> dict[str, Any]:
        frozen = self._validated_freeze(request)
        self._validate_query_admission(frozen["graph"], frozen["request"]["execution"])
        lifecycle_admission = self._validate_lifecycle_admission(
            frozen["graph"], frozen["request"]["execution"],
        )
        if lifecycle_admission is not None:
            frozen["lifecycle_admission"] = lifecycle_admission
        run_id = frozen["request"]["run_id"]
        path = self.run_directory(run_id) / "selected_request.json"
        if path.exists():
            saved = self._read(path)
            if canonical_json(saved) != canonical_json(frozen):
                raise SelectedExecutionError("Run ID already binds a different selected request")
            return saved
        self._write(path, frozen)
        return frozen

    def load(self, run_id: str) -> dict[str, Any]:
        """Read only the exact frozen selected request for one queue identity."""
        path = self.run_directory(run_id) / "selected_request.json"
        if not path.is_file():
            raise FileNotFoundError(path)
        return self._read(path)

    def _revalidate(self, frozen: Mapping[str, Any]) -> dict[str, Any]:
        request = frozen.get("request")
        if not isinstance(request, Mapping) or not isinstance(request.get("execution"), Mapping):
            raise SelectedExecutionError("saved selected request is invalid")
        current = self._validate_graph(request["execution"])
        if canonical_json(current) != canonical_json(frozen.get("graph")):
            raise SelectedExecutionError("selected Workflow graph changed after queue admission")
        return current

    @staticmethod
    def _transition(step: Mapping[str, Any], result: str) -> Mapping[str, Any]:
        for transition in step["on_result"]:
            condition = transition.get("result", transition.get("when"))
            if condition in (result, "*"):
                if "next" in transition or "terminal" in transition:
                    return transition
        raise SelectedExecutionError("no declared On Result transition admits Action result")

    @staticmethod
    def _implementation_packet(parameters: object, step_id: str,
                               prior_results: list[dict[str, Any]]) -> dict[str, Any]:
        """Select one explicit O016 Step packet and retain only observed state.

        O016's request parameters deliberately have a small, explicit shape:
        ``base_packet`` contains common, admitted inputs and ``step_packets``
        maps each manifest Step ID to its additional input mapping.  The
        executor selects by the manifest-bound Step ID; it never infers a
        packet from position or from a successor edge.
        """
        if not isinstance(parameters, Mapping):
            raise SelectedExecutionError("implementation Workflow requires a packet mapping")
        base = parameters.get("base_packet")
        packets = parameters.get("step_packets")
        if not isinstance(base, Mapping) or not isinstance(packets, Mapping):
            raise SelectedExecutionError("implementation Workflow requires base_packet and step_packets")
        packet = packets.get(step_id)
        if not isinstance(packet, Mapping):
            raise SelectedExecutionError(f"implementation Workflow has no packet for Step {step_id}")
        merged = {**base, **packet}
        if merged.get("context") not in {"Integrated", "Isolated"}:
            raise SelectedExecutionError(f"implementation packet context is missing for Step {step_id}")
        retained = base.get("retained_state", {})
        if not isinstance(retained, Mapping):
            raise SelectedExecutionError("implementation base retained_state is invalid")
        step_retained = packet.get("retained_state", {})
        if not isinstance(step_retained, Mapping):
            raise SelectedExecutionError(f"implementation packet retained_state is invalid for Step {step_id}")
        merged["retained_state"] = {**retained, **step_retained, "prior_results": list(prior_results)}
        merged["prior_results"] = list(prior_results)
        retry = merged.get("retry")
        if isinstance(retry, Mapping):
            consumed = retry.get("consumed")
            if isinstance(consumed, int) and not isinstance(consumed, bool) and consumed >= 0:
                # CA-O-024 counts when a permitted repair-and-evaluation round
                # starts, not when CA-O-096 is merely checked.  A completed
                # source-bound CA-O-099 repair retains a started round; at
                # CA-O-099 itself, its immediately preceding admitted O096
                # decision begins the next round.  Re-deriving from the
                # frozen base and exact prior results makes repeated gate
                # checks idempotent.
                completed_rounds = sum(
                    1 for prior in prior_results
                    if prior.get("step_definition_id") == "CA-O-099"
                    and prior.get("action_definition_id") == "CA-O-021"
                    and prior.get("result") == "repaired"
                )
                admitted_rounds = sum(
                    1 for prior in prior_results
                    if prior.get("step_definition_id") == "CA-O-096"
                    and prior.get("action_definition_id") == "CA-O-024"
                    and prior.get("result") == "retry_permitted"
                )
                rounds_started = completed_rounds
                if step_id == "CA-O-099" and admitted_rounds > completed_rounds:
                    rounds_started += 1
                merged["retry"] = {**retry, "consumed": consumed + rounds_started}
        return merged

    @staticmethod
    def _finish_selected_run(session: Any, requested_id: str, run_id: str, *,
                             recovery: bool = False, **result: Any) -> Mapping[str, Any]:
        """Reuse canonical finals, or record recovery without a second start."""
        if not recovery:
            return session.finish_run(run_id, **result)
        terminal = session.terminal.get(requested_id)
        if terminal is not None:
            expected = {"run_id": run_id, "disposition": "terminal", **result}
            if any(terminal.get(key) != value for key, value in expected.items()):
                raise SelectedExecutionError("retained Run terminal differs from recovered graph evidence")
            return dict(terminal)
        if requested_id in session.interrupted:
            if result.get("outcome") == "interrupted_pending":
                # Retain the original uncertainty; do not invent another
                # interruption or pretend a failed recovery attempt is final.
                return dict(session.interrupted[requested_id])
            return session.recover_run(run_id, **result)
        return session.finish_run(run_id, **result)

    def _replacement_prior_result_event(self, parameters: object) -> str:
        """Find the one sealed Journal result for W03's exact predecessor.

        The current lifecycle Tool repeats the carrier descriptor validation at
        effect time.  This separate Journal check is deliberately earlier: a
        replacement may not publish a successor or archive a predecessor whose
        requested historical state has no canonical result event.
        """
        if not isinstance(parameters, Mapping):
            raise SelectedExecutionError("replacement parameters are invalid")
        predecessor = parameters.get("predecessor")
        if not isinstance(predecessor, Mapping):
            raise SelectedExecutionError("replacement predecessor is invalid")
        path = predecessor.get("path")
        version = predecessor.get("version")
        digest = predecessor.get("digest")
        if (
            not isinstance(path, str) or not path or Path(path).is_absolute() or ".." in Path(path).parts
            or type(version) is not int or version < 1
            or not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None
        ):
            raise SelectedExecutionError("replacement predecessor lacks an exact path, version, and digest")
        try:
            import work_journal
            matches: list[str] = []
            for carrier in work_journal._all_journal_parts(self.root):
                _bytes, records = work_journal._carrier_records(carrier)
                for record in records:
                    event = work_journal.validate_sealed_event(record)
                    result = event.get("result")
                    if (
                        event.get("schema_version") == 3
                        and event.get("event") == "completed"
                        and event.get("kind") == "governed_project_change"
                        and isinstance(result, Mapping)
                        and result.get("state") == "present"
                        and result.get("path") == path
                        and result.get("version") == version
                        and result.get("sha256") == digest
                    ):
                        event_id = event.get("event_id")
                        if isinstance(event_id, str):
                            matches.append(event_id)
        except (OSError, work_journal.WorkJournalError) as error:
            raise SelectedExecutionError("replacement predecessor Journal evidence is unavailable") from error
        if len(matches) != 1:
            raise SelectedExecutionError("replacement predecessor lacks one exact canonical Journal result")
        return matches[0]

    def _replacement_journal_context(self, session: Any) -> tuple[str, str, str, str]:
        """Bind W03 provenance to this selected session's active Journal context."""
        try:
            import work_journal
        except ImportError as error:
            raise SelectedExecutionError("canonical Work Journal support is unavailable") from error
        tracker = getattr(session, "tracker", None)
        context = getattr(tracker, "journal_context", None)
        if not isinstance(context, Mapping):
            raise SelectedExecutionError("replacement requires the current tracker Journal context")
        author = context.get("author")
        timezone = context.get("timezone")
        if not isinstance(author, str) or not isinstance(timezone, str):
            raise SelectedExecutionError("replacement tracker Journal context is invalid")
        try:
            now = dt.datetime.now(ZoneInfo(timezone))
            local_date = now.date().isoformat()
            work_journal.validate_partition(author, local_date, timezone)
        except (ValueError, ZoneInfoNotFoundError, work_journal.WorkJournalError) as error:
            raise SelectedExecutionError("replacement tracker Journal context is invalid") from error
        return author, local_date, timezone, now.isoformat(timespec="seconds")

    def _replacement_structural_scope(self, binding: Mapping[str, Any]) -> str:
        """Read the scope from the exact admitted O051 carrier, not a caller packet."""
        path = binding.get("path")
        digest = binding.get("sha256")
        if not isinstance(path, str) or not isinstance(digest, str):
            raise SelectedExecutionError("replacement CA-O-051 Action binding is invalid")
        source = self._safe_path(path)
        if _sha256(source.read_bytes()) != digest:
            raise SelectedExecutionError("replacement CA-O-051 Action definition changed after admission")
        scope = _frontmatter(source).get("current_scope_unit")
        if not isinstance(scope, str) or not scope:
            raise SelectedExecutionError("replacement CA-O-051 Action has no current scope")
        return scope

    def _replacement_canonical_event(
        self,
        *,
        parameters: object,
        native_result: Mapping[str, Any],
        prior_event_id: str,
        replacement_binding: Mapping[str, Any],
        replacement_action_run_id: str,
        execution_request_id: object,
        author: str,
        occurred_at: str,
        structural_scope: str,
    ) -> dict[str, Any]:
        """Build only the observed O051 replacement provenance event."""
        if not isinstance(parameters, Mapping) or not isinstance(execution_request_id, str) or not execution_request_id:
            raise SelectedExecutionError("replacement request identity is invalid")
        requested_predecessor = parameters.get("predecessor")
        history = native_result.get("history")
        observed = native_result.get("predecessor")
        successors = native_result.get("successors")
        if (
            not isinstance(requested_predecessor, Mapping)
            or not isinstance(history, Mapping)
            or not isinstance(history.get("predecessor"), Mapping)
            or not isinstance(observed, Mapping)
            or not isinstance(successors, list)
            or not successors
        ):
            raise SelectedExecutionError("replacement did not return complete observed provenance")
        original = history["predecessor"]
        for field in ("path", "version", "digest"):
            if original.get(field) != requested_predecessor.get(field):
                raise SelectedExecutionError("replacement observed predecessor differs from its admitted input")
        predecessor_id = original.get("atom_id")
        successor_ids = [item.get("atom_id") if isinstance(item, Mapping) else None for item in successors]
        if (
            not isinstance(predecessor_id, str) or not predecessor_id
            or any(not isinstance(item, str) or not item for item in successor_ids)
            or len(successor_ids) != len(set(successor_ids))
        ):
            raise SelectedExecutionError("replacement returned invalid successor identities")
        result_path = observed.get("path")
        result_filename = observed.get("filename")
        result_version = observed.get("version")
        result_digest = observed.get("digest")
        if (
            not isinstance(result_path, str) or not result_path or Path(result_path).is_absolute()
            or ".." in Path(result_path).parts or not isinstance(result_filename, str) or not result_filename
            or type(result_version) is not int or result_version < 1
            or not isinstance(result_digest, str) or re.fullmatch(r"[0-9a-f]{64}", result_digest) is None
            or not isinstance(replacement_action_run_id, str) or not replacement_action_run_id
        ):
            raise SelectedExecutionError("replacement returned an invalid archived predecessor")
        try:
            import work_journal
        except ImportError as error:
            raise SelectedExecutionError("canonical Work Journal support is unavailable") from error
        event = {
            "schema_version": 3,
            "event_id": f"selected-replacement:{replacement_action_run_id}",
            "action_id": replacement_binding["atom_id"],
            "event": "completed",
            "kind": "governed_project_change",
            "subject_kind": "file",
            "author": author,
            "occurred_at": occurred_at,
            "llm_session": {"app": "run-support", "uuid": execution_request_id},
            "structural_scope": structural_scope,
            "action_type": "MOVE+UPDATE",
            "sources": [],
            "previous_result_event": prior_event_id,
            "predecessor_atom_id": predecessor_id,
            "successor_atom_ids": successor_ids,
            "result": {
                "state": "present",
                "filename": result_filename,
                "version": result_version,
                "path": result_path,
                "sha256": result_digest,
            },
        }
        return work_journal.with_event_digest(event)

    def _execute_graph(self, frozen: Mapping[str, Any], session: Any, *, recovery: bool = False) -> dict[str, Any]:
        graph = frozen["graph"]
        request = frozen["request"]
        run_id = request["run_id"]
        steps = {row["atom_id"]: row for row in graph["steps"]}
        manifest_ordinals = {row["atom_id"]: ordinal for ordinal, row in enumerate(graph["steps"], start=1)}
        visit_limits = self._run_visit_limits(
            graph, self._declared_run_visit_limits(request["execution"]),
        )
        visit_counts: dict[str, int] = {}
        restored_actions = set(getattr(session, "actual", {})) if recovery else set()
        next_step = graph["entry_step"]
        journal_preparation = self._prepare_journal_query_before_run(graph, request["execution"])
        workflow_actual = session.start_run(run_id)
        workflow_run_id = workflow_actual["run_id"]
        results: list[dict[str, Any]] = []
        implementation_prior_results: list[dict[str, Any]] = []
        structural_prior_results: list[dict[str, Any]] = []
        lifecycle_prior_results: list[dict[str, Any]] = []
        while next_step:
            step = steps.get(next_step)
            if step is None:
                raise SelectedExecutionError("On Result transition references an unbound Step")
            visit = visit_counts.get(next_step, 0) + 1
            if visit > visit_limits[next_step]:
                raise SelectedExecutionError(
                    "selected Workflow exhausted the caller-declared Step visit limit before Action dispatch"
                )
            visit_counts[next_step] = visit
            requested_step_id = self._requested_step_id(run_id, manifest_ordinals[next_step], visit)
            actual_step = session.start_run(requested_step_id)
            step_run_id = actual_step["run_id"]
            final_result: str | None = None
            step_effect_refs: list[str] = []
            terminal_recording_pending = False
            for action_ordinal, action in enumerate(step["actions"], start=1):
                requested_action_id = f"{requested_step_id}:action:{action_ordinal}"
                actual_action = session.start_run(requested_action_id)
                action_run_id = actual_action["run_id"]
                handler = self.handlers.get(action["atom_id"])
                if handler is None:
                    raise SelectedExecutionError(f"no native handler registered for Action {action['atom_id']}")
                parameters = request["execution"].get("parameters")
                trusted_execution_authorization: Mapping[str, Any] | None = None
                if graph["workflow"]["atom_id"] == "CA-O-016":
                    parameters = self._implementation_packet(parameters, step["atom_id"], implementation_prior_results)
                    # Carry the already-sealed execution authorization into the
                    # selected Step packet; retry admission must bind to this
                    # retained evidence rather than a caller-supplied boolean.
                    execution_authorization = request["execution"].get("operator_authorization")
                    if isinstance(execution_authorization, Mapping):
                        trusted_execution_authorization = execution_authorization
                        parameters = {**parameters, "operator_authorization": dict(execution_authorization)}
                if graph.get("route") in {"build_entities_graph", "build_terms_graph"}:
                    parameters = self._graph_parameters_with_actual_recording(
                        parameters,
                        session,
                        workflow_run_id=workflow_run_id,
                        step_run_id=step_run_id,
                        action_run_id=action_run_id,
                    )
                context = {
                    "project_root": self.root,
                    "workflow_run_id": workflow_run_id,
                    "step_run_id": step_run_id,
                    "action_run_id": action_run_id,
                    "workflow_definition": graph["workflow"],
                    "step_definition": {key: value for key, value in step.items() if key not in {"actions", "on_result"}},
                    "action_definition": action,
                    "action_binding": action,
                    "route": graph["route"],
                    "workflow_definition_id": graph["workflow"]["atom_id"],
                    "step_definition_id": step["atom_id"],
                    "action_definition_id": action["atom_id"],
                    "parameters": parameters,
                    "trusted_execution_authorization": trusted_execution_authorization,
                    "target_frontier": request["execution"].get("target_frontier"),
                    "effects": request["execution"].get("effects"),
                    "initiative": request["execution"].get("initiative"),
                    "sealed_outer_admission": True,
                    "session": session,
                    "requested_action_run_id": requested_action_id,
                }
                if (graph.get("route") == "replace_atom"
                        and action.get("atom_id") == "CA-O-128"):
                    replacement_binding = self._replacement_native_binding(graph)
                    replacement_requested_run_id = self._replacement_child_requested_id(requested_action_id)
                    replacement_result_path = (
                        self.run_directory(run_id) / f"{replacement_requested_run_id}.json"
                    )

                    def write_replacement_result(payload: Mapping[str, Any], *, _path: Path = replacement_result_path) -> str:
                        if not isinstance(payload, Mapping):
                            raise SelectedExecutionError("replacement result writer requires an evidence mapping")
                        self._write(_path, dict(payload))
                        return _path.relative_to(self.root).as_posix()

                    context.update({
                        "replacement_action_binding": replacement_binding,
                        "replacement_requested_run_id": replacement_requested_run_id,
                        "replacement_result_writer": write_replacement_result,
                        "execution_request_id": request["execution"].get("request_id"),
                    })
                if graph.get("route") == "release_version":
                    checkpoint_path = self.run_directory(run_id) / "release_action_run.json"
                    context["checkpoint_writer"] = lambda payload: self._write(checkpoint_path, payload)
                    context["checkpoint_reader"] = lambda: (
                        self._read(checkpoint_path) if checkpoint_path.exists() else None
                    )
                    def read_progress(requested_id: str) -> dict[str, Any]:
                        allowed = {row.get("requested_run_id") for row in
                                   request["execution"].get("requested_runs", []) if row.get("kind") == "action"}
                        if requested_id not in (allowed or {requested_action_id}):
                            raise SelectedExecutionError("Release progress reader is outside the frozen Action set")
                        return self._read(self.run_directory(run_id) / f"{requested_id}.json")
                    context["checkpoint_progress_reader"] = read_progress
                    context["restored_action"] = requested_action_id in restored_actions
                if action["atom_id"] == "CA-O-162":
                    context["journal_preparation"] = journal_preparation
                if graph["workflow"]["atom_id"] == "CA-O-015":
                    # This is executor-retained state only; structural Actions
                    # never admit caller-provided prior-result assertions.
                    context["structural_prior_results"] = list(structural_prior_results)
                if graph["workflow"]["atom_id"] == "CA-O-127":
                    context["lifecycle_prior_results"] = list(lifecycle_prior_results)
                output = handler(context)
                if not isinstance(output, Mapping) or not isinstance(output.get("result"), str):
                    raise SelectedExecutionError("native Action handler returned no declared result")
                output = dict(output)
                result_map = action.get("result_map", {})
                if not isinstance(result_map, Mapping):
                    raise SelectedExecutionError("selected Action result map is invalid")
                final_result = result_map.get(output["result"], output["result"])
                if not isinstance(final_result, str):
                    raise SelectedExecutionError("selected Action result map is invalid")
                effect_refs = output.get("effect_refs", [])
                if not isinstance(effect_refs, list) or any(not isinstance(item, str) for item in effect_refs):
                    raise SelectedExecutionError("native Action handler returned invalid effect references")
                progress_path = self.run_directory(run_id) / f"{requested_action_id}.json"
                progress = {"result": final_result, "action_run_id": action_run_id,
                            "effect_refs": effect_refs,
                            "native_result": output.get("native_result"),
                            "compiler_publication_recording": output.get("compiler_publication_recording")}
                if output.get("shared_action_recording") is not None:
                    progress["shared_action_recording"] = output["shared_action_recording"]
                self._write(progress_path, progress)
                terminal_receipt: Mapping[str, Any] | None = None
                if output.get("action_terminal_recorded") is not True:
                    action_outcome = output.get("terminal_outcome", "completed")
                    if action_outcome not in {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}:
                        raise SelectedExecutionError("native Action handler returned an invalid terminal outcome")
                    terminal_receipt = self._finish_selected_run(
                        session, requested_action_id, action_run_id, recovery=recovery, outcome=action_outcome,
                        result_ref=progress_path.relative_to(self.root).as_posix(),
                        effect_refs=effect_refs,
                    )
                checkpoint_receipt = output.get("record_shared_receipt")
                if checkpoint_receipt is not None:
                    if graph.get("route") != "release_version" or not callable(checkpoint_receipt):
                        raise SelectedExecutionError("private shared-recording callback is outside Release")
                    checkpoint_receipt(terminal_receipt, list(session.pending), list(session.receipts))
                terminal_recording_pending = (
                    isinstance(terminal_receipt, Mapping)
                    and terminal_receipt.get("disposition") == "recording_pending"
                )
                recording = output.get("compiler_publication_recording")
                if recording is not None:
                    if not isinstance(recording, Mapping):
                        raise SelectedExecutionError("compiler publication recording handoff is invalid")
                    if (terminal_receipt is not None and terminal_receipt.get("disposition") == "terminal"
                            and terminal_receipt.get("outcome") == "completed"):
                        completed = recording.get("on_recorded_result")
                        if not isinstance(completed, str):
                            raise SelectedExecutionError("compiler publication recording handoff is incomplete")
                        final_result = result_map.get(completed, completed)
                        # The Tool's raw pending_recording result remains intact,
                        # while this derived carrier can now reflect the sealed
                        # shared Action receipt that admitted the graph edge.
                        progress["result"] = final_result
                        self._write(progress_path, progress)
                    else:
                        # The native effect is already applied, but without the
                        # shared Action receipt it cannot take the published
                        # On Result edge.  The durable dispatch result prevents
                        # re-entering this Action while recording is pending.
                        output["terminal_outcome"] = "interrupted_pending"
                release_recording = output.get("shared_action_recording")
                if release_recording is not None:
                    if graph.get("route") != "release_version" or step["atom_id"] != "CA-O-179":
                        raise SelectedExecutionError("Release recording handoff is outside its final selected Step")
                    if not isinstance(release_recording, Mapping):
                        raise SelectedExecutionError("Release recording handoff is invalid")
                    completed = release_recording.get("on_recorded_result")
                    edges = step.get("on_result", [])
                    if (len(edges) != 1 or completed != edges[0].get("result")
                            or edges[0].get("terminal") != "completed"):
                        raise SelectedExecutionError("Release recording handoff differs from the frozen completion edge")
                    if (isinstance(terminal_receipt, Mapping)
                            and terminal_receipt.get("disposition") == "terminal"
                            and terminal_receipt.get("outcome") == "completed"
                            and terminal_receipt.get("run_id") == action_run_id
                            and terminal_receipt.get("result_ref") == progress_path.relative_to(self.root).as_posix()
                            and terminal_receipt.get("effect_refs") == effect_refs):
                        final_result = completed
                        progress["result"] = final_result
                        self._write(progress_path, progress)
                    else:
                        final_result = "recording_pending"
                        output["terminal_outcome"] = "interrupted_pending"
                elif (graph.get("route") == "release_version"
                        and isinstance(terminal_receipt, Mapping)
                        and terminal_receipt.get("disposition") != "terminal"):
                    # A saved effect result is not authority for the next phase
                    # until the sole shared recorder has its exact terminal fact.
                    final_result = "recording_pending"
                    output["terminal_outcome"] = "interrupted_pending"
                elif (graph.get("route") in {"build_entities_graph", "build_terms_graph"}
                        and terminal_recording_pending):
                    # The projection has already been materialized, and must
                    # remain available for Journal recovery.  It is not,
                    # however, a completed selected Action until the shared
                    # recorder has durably appended its terminal fact.  Do
                    # not replay the generator to manufacture that evidence.
                    final_result = "recording_pending"
                    output["terminal_outcome"] = "interrupted_pending"
                    progress["result"] = final_result
                    self._write(progress_path, progress)
                if (graph["workflow"]["atom_id"] == "CA-O-015"
                        and isinstance(terminal_receipt, Mapping)
                        and terminal_receipt.get("disposition") == "terminal"
                        and terminal_receipt.get("outcome") == "completed"
                        and terminal_receipt.get("result_ref") == progress_path.relative_to(self.root).as_posix()
                        and terminal_receipt.get("effect_refs") == effect_refs):
                    structural_prior_results.append({
                        "workflow_run_id": workflow_run_id,
                        "workflow_definition_id": graph["workflow"]["atom_id"],
                        "step_run_id": step_run_id,
                        "step_definition_id": step["atom_id"],
                        "action_run_id": action_run_id,
                        "action_definition_id": action["atom_id"],
                        "result": final_result,
                        "result_ref": progress_path.relative_to(self.root).as_posix(),
                        "native_result": output.get("native_result"),
                        "completed_receipt": dict(terminal_receipt),
                    })
                if (graph["workflow"]["atom_id"] == "CA-O-127"
                        and isinstance(terminal_receipt, Mapping)
                        and terminal_receipt.get("disposition") == "terminal"
                        and terminal_receipt.get("outcome") == "completed"
                        and terminal_receipt.get("result_ref") == progress_path.relative_to(self.root).as_posix()
                        and terminal_receipt.get("effect_refs") == effect_refs):
                    lifecycle_prior_results.append({
                        "workflow_run_id": workflow_run_id,
                        "workflow_definition_id": graph["workflow"]["atom_id"],
                        "step_run_id": step_run_id,
                        "step_definition_id": step["atom_id"],
                        "action_run_id": action_run_id,
                        "action_definition_id": action["atom_id"],
                        "result": final_result,
                        "result_ref": progress_path.relative_to(self.root).as_posix(),
                        "native_result": output.get("native_result"),
                        "completed_receipt": dict(terminal_receipt),
                    })
                step_effect_refs.extend(effect_refs)
                results.append({"step_run_id": step_run_id, "action_run_id": action_run_id,
                                "step_definition_id": step["atom_id"],
                                "action_definition_id": action["atom_id"], "result": final_result,
                                "effect_refs": effect_refs})
                if graph["workflow"]["atom_id"] == "CA-O-016":
                    native = output.get("native_result")
                    implementation_prior_results.append({
                        "step_definition_id": step["atom_id"],
                        "action_definition_id": action["atom_id"],
                        "result": final_result,
                        "outputs": native.get("outputs", {}) if isinstance(native, Mapping) else {},
                        "evidence": native.get("evidence", []) if isinstance(native, Mapping) else [],
                        "retained_state": native.get("retained_state", {}) if isinstance(native, Mapping) else {},
                    })
                if terminal_recording_pending:
                    # The effect and its pending Action receipt are retained,
                    # but an unrecorded terminal fact cannot authorize either
                    # another Action or an On Result transition.
                    break
            if terminal_recording_pending:
                transition = {"terminal": "interrupted_pending"}
            else:
                try:
                    transition = self._transition(step, final_result or "")
                except SelectedExecutionError:
                    terminal_outcome = output.get("terminal_outcome")
                    if not isinstance(terminal_outcome, str):
                        raise
                    transition = {"terminal": terminal_outcome}
            if "terminal" in transition:
                terminal = transition["terminal"]
                if not isinstance(terminal, str):
                    raise SelectedExecutionError("selected terminal result is invalid")
                if terminal not in {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}:
                    raise SelectedExecutionError("selected terminal result is not a truthful Run outcome")
                result_path = self.run_directory(run_id) / "graph_result.json"
                output = {"outcome": terminal, "workflow_run_id": workflow_run_id,
                          "workflow_definition_id": graph["workflow"]["atom_id"], "step_results": results}
                self._write(result_path, output)
                result_ref = result_path.relative_to(self.root).as_posix()
                effect_refs = sorted({reference for row in results for reference in row["effect_refs"]})
                self._finish_selected_run(session, requested_step_id, step_run_id, recovery=recovery,
                                          outcome=terminal, result_ref=result_ref, effect_refs=step_effect_refs)
                self._finish_selected_run(session, run_id, workflow_run_id, recovery=recovery,
                                          outcome=terminal, result_ref=result_ref, effect_refs=effect_refs)
                return {**output, "result_ref": result_ref, "effect_refs": effect_refs}
            step_result_path = self.run_directory(run_id) / f"{requested_step_id}.json"
            self._write(step_result_path, {"result": final_result, "step_run_id": step_run_id,
                                            "action_results": results})
            self._finish_selected_run(session, requested_step_id, step_run_id, recovery=recovery, outcome="completed",
                               result_ref=step_result_path.relative_to(self.root).as_posix(),
                               effect_refs=step_effect_refs)
            next_step = transition["next"]
            if not isinstance(next_step, str):
                raise SelectedExecutionError("selected transition target is invalid")
        raise SelectedExecutionError("selected Workflow has no terminal result")

    def _prepare_journal_query_before_run(
        self, graph: Mapping[str, Any], execution: Mapping[str, Any],
    ) -> Any | None:
        """Seal CA-O-163's source after generic admission but before Run evidence."""
        if graph.get("route") != "find_and_fetch_journal_events":
            return None
        try:
            import query_actions
        except ImportError as error:
            raise SelectedExecutionError("Journal query adapter is unavailable") from error
        steps = graph.get("steps")
        if not isinstance(steps, list) or len(steps) != 1 or not isinstance(steps[0], Mapping):
            raise SelectedExecutionError("Journal query route must retain exactly one source Step")
        step = steps[0]
        actions = step.get("actions")
        if step.get("atom_id") != "CA-O-163" or not isinstance(actions, list) or len(actions) != 1:
            raise SelectedExecutionError("Journal query route must retain CA-O-163 and one Action")
        action = actions[0]
        if not isinstance(action, Mapping) or action.get("atom_id") != "CA-O-162":
            raise SelectedExecutionError("Journal query route must retain CA-O-162")
        context = {
            "route": graph["route"],
            "workflow_definition_id": graph["workflow"]["atom_id"],
            "step_definition_id": step["atom_id"],
            "action_definition_id": action["atom_id"],
            "parameters": execution.get("parameters"),
        }
        try:
            return query_actions.prepare_journal_query(self.root, context)
        except query_actions.QueryActionError as error:
            raise SelectedExecutionError(str(error)) from error

    def _shared_tracker(self, frozen: Mapping[str, Any]) -> Any:
        """Late import keeps APPS importable while the shared service is replaced."""
        import sys
        tools_root = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
        if tools_root not in sys.path:
            sys.path.insert(0, tools_root)
        from workflow_run_support import RunTracker  # owned by P1510

        def observe(request: dict[str, Any]) -> dict[str, Any]:
            graph = self._revalidate(frozen)
            lifecycle_admission = preflight_selected_lifecycle(
                self.root, graph.get("route"), request.get("parameters"),
            )
            lifecycle_current = (
                lifecycle_admission is None
                or canonical_json(lifecycle_admission) == canonical_json(frozen.get("lifecycle_admission"))
            )
            return {"selected": request.get("operation_route") == graph["route"], "current": lifecycle_current,
                    "observed": {"manifest_ref": graph["manifest_ref"],
                                 "manifest_digest": graph["manifest_digest"],
                                 **({"lifecycle_admission": lifecycle_admission}
                                    if lifecycle_admission is not None else {})}}

        return RunTracker(self.root, source_observer=observe,
                          executor=lambda _request, session: self._execute_graph(frozen, session))

    def _shared_dispatch(self, frozen: Mapping[str, Any]) -> dict[str, Any]:
        return self._shared_tracker(frozen).run_selected_operation(dict(frozen["request"]["execution"]))

    def recover_release(self, frozen: Mapping[str, Any]) -> dict[str, Any]:
        """Explicitly reconcile one accepted Release; never redispatch intent.

        This private-runtime capability is not registration of a public MCP
        route.  The canonical dispatch and Journal, not progress or checkpoint
        assertions, establish which actual Runs are already in existence.
        """
        import sys
        tools_root = Path(__file__).resolve().parents[2] / "201_TOOLS"
        for location in (tools_root, tools_root / "RELEASE_VERSION"):
            if str(location) not in sys.path:
                sys.path.insert(0, str(location))
        import work_journal
        from release_checkpoint import dump_release_checkpoint, extract_pending_recordings, load_release_checkpoint
        from selected_run_recovery import read_selected_run_evidence, validate_selected_run_events
        from workflow_run_support import RunExecutionSession, _canonical_digest, _proposal, _validate_common

        request = frozen.get("request") if isinstance(frozen, Mapping) else None
        if not isinstance(request, Mapping) or not isinstance(request.get("run_id"), str):
            raise SelectedExecutionError("saved Release request is invalid")
        run_id = request["run_id"]
        graph = self._revalidate(frozen)
        if graph.get("route") != "release_version":
            raise SelectedExecutionError("selected recovery is admitted only for Release Version")
        execution = _validate_common(request["execution"])
        tracker = self._shared_tracker(frozen)
        observation = tracker._observe(execution)
        if not observation["selected"] or not observation["current"]:
            raise SelectedExecutionError("Release recovery source admission is not current")
        proposal = _proposal(execution, observation)
        tracker._validate_execute(execution, proposal, _canonical_digest(proposal))
        folder = self.run_directory(run_id)

        with work_journal._event_lock(self.root, f"selected-release-recovery:{execution['request_id']}"):
            evidence = read_selected_run_evidence(self.root, execution)
            checkpoint = self._read(folder / "release_action_run.json")
            private_run, recordings = load_release_checkpoint(
                checkpoint, expected_request=execution["parameters"], expected_workflow_run_id=run_id,
            )
            if private_run.in_progress is not None:
                raise SelectedExecutionError("Release has an unresolved in-progress effect; recovery cannot replay it")
            pending_packets = extract_pending_recordings(checkpoint)
            pending_ids = [packet["event_id"] for packet in pending_packets.values()]
            accepted_path = folder / "accepted.json"
            if accepted_path.exists():
                previous = self._read(accepted_path).get("result")
                if not isinstance(previous, Mapping):
                    raise SelectedExecutionError("saved dispatch result is invalid")
                retained = previous.get("pending_event_ids", [])
                if not isinstance(retained, list) or any(not isinstance(item, str) or not item for item in retained):
                    raise SelectedExecutionError("saved pending event identities are invalid")
                pending_ids.extend(retained)
            pending_ids = list(dict.fromkeys(pending_ids))
            canonical_events = [item["event"] for item in evidence["events"]]
            canonical_by_id = {event["event_id"]: event for event in canonical_events}
            initial_session = RunExecutionSession.restore(tracker, execution, evidence["events"])
            pending_events: list[dict[str, Any]] = []
            for event_id in pending_ids:
                event = canonical_by_id.get(event_id)
                already_recorded = event is not None
                if not already_recorded:
                    retained, event, _append_context, _path = work_journal._read_pending_event(self.root, event_id)
                    if (retained["result_ref"] != event["result_ref"]
                            or retained["effect_refs"] != event["effect_refs"]):
                        raise SelectedExecutionError("pending recording references differ from its sealed original event")
                matching = [(index, packet) for index, packet in pending_packets.items() if packet["event_id"] == event_id]
                if matching and matching[0][1]["event_outcome"] != event["outcome"]:
                    raise SelectedExecutionError("pending checkpoint outcome differs from its original sealed event")
                if matching:
                    phase_context = private_run.contexts.get(matching[0][0])
                    actual = event.get("run", {})
                    if (phase_context is None or actual.get("kind") != "action"
                            or actual.get("run_id") != phase_context.action_run_id
                            or actual.get("parent_run_id") != phase_context.step_run_id
                            or actual.get("definition", {}).get("atom_id") != phase_context.action_atom_id):
                        raise SelectedExecutionError("pending event differs from its exact checkpoint phase occurrence")
                self._validate_release_pending_progress(folder, initial_session, event)
                if not already_recorded:
                    pending_events.append(event)
            # Validate the entire recovered lifecycle before the first append;
            # arbitrary IDs in a progress carrier cannot admit foreign events.
            validate_selected_run_events(execution, canonical_events + pending_events)
            for event in pending_events:
                work_journal.recover_pending_event(self.root, event["event_id"])
            evidence = read_selected_run_evidence(self.root, execution)
            session = RunExecutionSession.restore(tracker, execution, evidence["events"])
            workflow = session.actual.get(run_id)
            if not isinstance(workflow, Mapping):
                raise SelectedExecutionError("Release recovery has no canonical Workflow start")
            terminal = session.terminal.get(run_id)
            if terminal is not None:
                self._validate_release_saved_result(folder, workflow["run_id"], terminal)
                if terminal.get("outcome") == "completed":
                    exact_recordings = self._validate_release_complete_frontier(frozen, session, private_run)
                    self._write(folder / "release_action_run.json", dump_release_checkpoint(
                        private_run, shared_recordings=exact_recordings, pending_recordings={},
                    ))
            elif run_id not in session.interrupted:
                raise SelectedExecutionError("Release has no canonical interruption; a live or uncertain Run cannot be resumed")
            else:
                # Source/permission seals are reopened after recording recovery
                # and before any previously unstarted phase is admitted.
                self._revalidate(frozen)
                current = tracker._observe(execution)
                current_proposal = _proposal(execution, current)
                if not current["selected"] or not current["current"]:
                    raise SelectedExecutionError("Release recovery admission changed before continuation")
                tracker._validate_execute(execution, current_proposal, _canonical_digest(current_proposal))
                self._execute_graph(frozen, session, recovery=True)
            result = tracker._session_result(execution, proposal, session)
            # Only canonical final Workflow evidence may replace the prior
            # pending dispatch result.  Intent is retained for every other case.
            final = session.terminal.get(run_id)
            if (not session.pending and isinstance(final, Mapping)
                    and final.get("disposition") == "terminal"):
                if final.get("outcome") == "completed":
                    latest = self._read(folder / "release_action_run.json")
                    final_run, _final_recordings = load_release_checkpoint(
                        latest, expected_request=execution["parameters"], expected_workflow_run_id=run_id,
                    )
                    exact = self._validate_release_complete_frontier(frozen, session, final_run)
                    self._write(folder / "release_action_run.json", dump_release_checkpoint(
                        final_run, shared_recordings=exact, pending_recordings={},
                    ))
                self._write(accepted_path, {"result": result})
                (folder / "dispatch-intent.json").unlink(missing_ok=True)
            return result

    def _validate_release_pending_progress(self, folder: Path, session: Any,
                                           event: Mapping[str, Any]) -> None:
        """Bind pending original terminal bytes to the saved graph observation."""
        if event.get("event") == "started":
            return  # Full request/lineage binding is checked by reconstruction.
        actual = event.get("run")
        if not isinstance(actual, Mapping):
            raise SelectedExecutionError("pending Release event has no Run")
        if actual.get("kind") == "action":
            candidates = [(requested_id, record) for requested_id, record in session.actual.items()
                          if record.get("run_id") == actual.get("run_id") and record == actual]
            if len(candidates) != 1:
                raise SelectedExecutionError("pending Release Action occurrence is ambiguous")
            progress_path = folder / f"{candidates[0][0]}.json"
            progress = self._read(progress_path)
            expected_ref = progress_path.relative_to(self.root).as_posix()
            if (event.get("result_ref") != expected_ref or progress.get("action_run_id") != actual.get("run_id")
                    or progress.get("effect_refs") != event.get("effect_refs")):
                raise SelectedExecutionError("pending Release Action does not match its saved observation")
        else:
            result_ref = event.get("result_ref")
            if result_ref is not None:
                path = self._safe_path(result_ref)
                if path.parent != folder:
                    raise SelectedExecutionError("pending Release parent result is outside its Run")
                self._read(path)

    def _validate_release_complete_frontier(self, frozen: Mapping[str, Any], session: Any,
                                            private_run: Any) -> dict[int, dict[str, Any]]:
        """A completed Workflow requires every exact phase, not a final flag."""
        from release_actions import PHASES
        graph = frozen["graph"]
        steps = graph["steps"]
        if (len(steps) != len(PHASES) or set(private_run.contexts) != set(range(len(PHASES)))
                or set(private_run.results) != set(range(len(PHASES)))):
            raise SelectedExecutionError("completed Release lacks its complete ten-phase typed frontier")
        # Native retirement intentionally remains pending: its sole shared
        # completed receipt, not mutation of the native result, closes phase 10.
        retirement = private_run.results[len(PHASES) - 1]
        shared_retired = (retirement.outcome == "pending" and retirement.effect_outcome == "retired"
                          and isinstance(retirement.shared_action_recording, Mapping))
        expected_frontier = len(PHASES) - 1 if shared_retired else len(PHASES)
        if (private_run.next_phase != expected_frontier or private_run.in_progress is not None
                or (private_run.stopped and not shared_retired)):
            raise SelectedExecutionError("completed Release has an unfinished or uncertain phase frontier")
        exact: dict[int, dict[str, Any]] = {}
        requested_workflow = frozen["request"]["run_id"]
        workflow = session.actual[requested_workflow]
        for index, step in enumerate(steps):
            context = private_run.contexts[index]
            result = private_run.results[index]
            requested_step = self._requested_step_id(requested_workflow, index + 1, 1)
            requested_action = f"{requested_step}:action:1"
            actual_step = session.actual.get(requested_step, {})
            actual_action = session.actual.get(requested_action, {})
            terminal = session.terminal.get(requested_action, {})
            step_terminal = session.terminal.get(requested_step, {})
            expected_pair = PHASES[index][:2]
            if (len(step["actions"]) != 1 or (step["atom_id"], step["actions"][0]["atom_id"]) != expected_pair
                    or context.workflow_run_id != workflow["run_id"]
                    or context.step_run_id != actual_step.get("run_id")
                    or context.action_run_id != actual_action.get("run_id")
                    or (context.step_atom_id, context.action_atom_id) != expected_pair
                    or actual_action.get("parent_run_id") != actual_step.get("run_id")
                    or actual_step.get("parent_run_id") != workflow["run_id"]
                    or (result.outcome != "completed" and not (index == len(PHASES) - 1 and shared_retired))
                    or step_terminal.get("disposition") != "terminal" or step_terminal.get("outcome") != "completed"):
                raise SelectedExecutionError("completed Release has a missing or mismatched phase occurrence")
            progress_path = self.run_directory(requested_workflow) / f"{requested_action}.json"
            progress = self._read(progress_path)
            receipt = terminal.get("event_receipt")
            edges = step["on_result"]
            effects = list(result.effect_evidence_refs)
            if (len(edges) != 1 or progress.get("result") != edges[0].get("result")
                    or progress.get("action_run_id") != context.action_run_id or progress.get("effect_refs") != effects
                    or terminal.get("disposition") != "terminal" or terminal.get("outcome") != "completed"
                    or terminal.get("run_id") != context.action_run_id
                    or terminal.get("result_ref") != progress_path.relative_to(self.root).as_posix()
                    or terminal.get("effect_refs") != effects or not isinstance(receipt, Mapping)
                    or receipt.get("event_id") != terminal.get("event_id")
                    or receipt not in session.receipts):
                raise SelectedExecutionError("completed Release phase lacks exact canonical receipt and progress proof")
            exact[index] = {"terminal_outcome": "completed", "receipt_refs": (receipt["event_id"],)}
        return exact

    def _validate_release_saved_result(self, folder: Path, run_id: str, terminal: Mapping[str, Any]) -> None:
        path = folder / "graph_result.json"
        value = self._read(path)
        effects = sorted({ref for row in value.get("step_results", []) for ref in row.get("effect_refs", [])})
        if (terminal.get("disposition") != "terminal" or value.get("workflow_run_id") != run_id
                or terminal.get("outcome") != value.get("outcome")
                or terminal.get("result_ref") != path.relative_to(self.root).as_posix()
                or terminal.get("effect_refs") != effects):
            raise SelectedExecutionError("canonical Release final differs from its saved graph result")

    def dispatch(self, frozen: Mapping[str, Any], *, run_support: Callable[[Path, dict[str, Any], Callable[[Any], dict[str, Any]]], Mapping[str, Any]] | None = None) -> dict[str, Any]:
        request = frozen.get("request") if isinstance(frozen, Mapping) else None
        if not isinstance(request, Mapping) or not isinstance(request.get("run_id"), str):
            raise SelectedExecutionError("saved selected request is invalid")
        run_id = request["run_id"]
        folder = self.run_directory(run_id)
        accepted = folder / "accepted.json"
        if accepted.exists():
            return self._read(accepted)["result"]
        intent = folder / "dispatch-intent.json"
        if intent.exists():
            return {"disposition": "recording_pending", "outcome": "interrupted_pending",
                    "workflow_run_id": run_id, "reason": "uncertain selected dispatch intent retained; no replay"}
        graph = self._revalidate(frozen)
        self._validate_query_admission(graph, request["execution"])
        try:
            self._validate_lifecycle_admission(
                graph, request["execution"],
                expected_admission=frozen.get("lifecycle_admission"),
            )
        except LifecycleAdmissionError as error:
            return {
                "disposition": "blocked", "outcome": "blocked", "workflow_run_id": run_id,
                "effect_refs": [], "lifecycle_error": error.record(),
                "diagnostics": [str(error)],
            }
        self._write(intent, {"run_id": run_id, "state": "dispatching", "graph": frozen["graph"]})
        try:
            if run_support is None:
                result = self._shared_dispatch(frozen)
            else:
                result = run_support(self.root, dict(request["execution"]),
                                     lambda session: self._execute_graph(frozen, session))
            if not isinstance(result, Mapping):
                raise SelectedExecutionError("shared selected Run support returned an invalid result")
            value = dict(result)
            self._write(accepted, {"result": value})
            intent.unlink(missing_ok=True)
            return value
        except Exception as error:
            self._write(folder / "dispatch_uncertain.json", {"run_id": run_id, "reason": str(error)})
            return {"disposition": "recording_pending", "outcome": "interrupted_pending",
                    "workflow_run_id": run_id, "reason": "uncertain selected dispatch intent retained; no replay"}


def build_requested_runs(
    graph: Mapping[str, Any],
    run_id: str,
    run_visit_limits: Mapping[str, int] | None = None,
) -> list[dict[str, Any]]:
    """Public requested-Run planner for selected-route callers and fixtures.

    The graph must be the already validated selected graph returned by
    :meth:`SelectedExecution._validate_graph`; callers remain responsible for
    sealing the returned rows in their execute request before dispatch.
    """
    return SelectedExecution.build_requested_runs(graph, run_id, run_visit_limits)
