"""Explicit worker providers, scoped to one frozen selected dispatch at a time."""
from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import fields, is_dataclass
import json
from pathlib import Path
import sys
from typing import Any

from implementation_agent import ImplementationAgent
from selected_execution import SelectedExecution, SelectedExecutionError, canonical_json, make_revert_action_handler


class SelectedNativeProviders:
    """Keep Implementation transport separate from Base Revise and Revert authority.

    Construction starts no Agent or Run. Revert is bound only when its Action
    receives the exact frozen parameters and the existing selected session.
    No provider is installed in the process-wide Action registry.
    """

    def __init__(self, root: str | Path, *, implementation_agent: Callable[..., Mapping[str, Any]] | None = None,
                 release_image_executor: Any | None = None):
        self.root = Path(root).resolve(strict=True)
        self.implementation_agent = implementation_agent if implementation_agent is not None else ImplementationAgent()
        if not callable(self.implementation_agent):
            raise TypeError("implementation agent must be callable")
        # Private native injection only; never selected client parameters.
        self.release_image_executor = release_image_executor

    def execution(self, frozen: Mapping[str, Any]) -> SelectedExecution:
        """Build providers from the queue's frozen request, never ambient effects."""
        try:
            parameters = json.loads(canonical_json(frozen["request"]["execution"].get("parameters")))
        except (KeyError, TypeError, ValueError) as error:
            raise SelectedExecutionError("native providers require the frozen selected execution") from error

        def revert(context: dict[str, Any]) -> Mapping[str, Any]:
            if (context.get("action_definition_id") != "CA-O-131"
                    or context.get("sealed_outer_admission") is not True
                    or canonical_json(context.get("parameters")) != canonical_json(parameters)):
                raise SelectedExecutionError("Revert provider requires the exact frozen selected Action context")
            manifest = parameters.get("approved_reversal_manifest", parameters.get("reversal_manifest")) if isinstance(parameters, Mapping) else None
            request = manifest.get("request") if isinstance(manifest, Mapping) else None
            if not isinstance(request, Mapping):
                return self._blocked("RMED remainder: selected Revert requires an approved reversal manifest with its exact request")
            tools = Path(__file__).resolve().parents[2] / "201_TOOLS" / "WORKFLOW_OPERATIONS" / "REVERT_CHANGES"
            if str(tools) not in sys.path:
                sys.path.insert(0, str(tools))
            from native_revert_provider import NativeRevertProviderError, make_native_revert_service

            try:
                service = make_native_revert_service({
                    "project_root": str(self.root), "approved_reversal_request": request,
                })
            except NativeRevertProviderError as error:
                return self._blocked(str(error))
            return make_revert_action_handler(service)(context)

        handlers = {"CA-O-131": revert}
        if frozen["request"]["execution"].get("operation_route") == "release_version":
            handlers.update(self._release_handlers(frozen, parameters))
        return SelectedExecution(self.root, handlers=handlers,
                                 implementation_agent=self.implementation_agent)

    @staticmethod
    def _json_value(value: Any) -> Any:
        if hasattr(value, "model_dump"):
            return value.model_dump(mode="json", by_alias=True)
        if is_dataclass(value):
            return {field.name: SelectedNativeProviders._json_value(getattr(value, field.name)) for field in fields(value)}
        if isinstance(value, Mapping):
            return {key: SelectedNativeProviders._json_value(item) for key, item in value.items()}
        if isinstance(value, (list, tuple)):
            return [SelectedNativeProviders._json_value(item) for item in value]
        if isinstance(value, Path):
            return str(value)
        if value is None or isinstance(value, (str, int, float, bool)):
            return value
        raise SelectedExecutionError("Release returned an unsupported private result type")

    @staticmethod
    def _shared_retirement_recording(
        result: Any, *, candidate_sha256: str, workflow_run_id: str,
        step_run_id: str, action_run_id: str, step_atom_id: str,
        action_atom_id: str, frozen_result: str, effect_refs: list[str],
    ) -> dict[str, str] | None:
        """Validate the private-to-shared receipt handoff for one retired image.

        The packet is evidence about an already-observed retirement, never an
        instruction supplied by the selected caller.  The generic dispatcher
        alone may turn its pending result into the frozen terminal edge after
        its exact Action receipt is durable.
        """
        packet = getattr(result, "shared_action_recording", None)
        if packet is None:
            return None
        required = {
            "on_recorded_result", "candidate_snapshot_manifest_sha256",
            "prior_image_digest", "retirement_receipt_ref",
            "retirement_receipt_sha256",
        }
        if (not isinstance(packet, Mapping) or set(packet) != required
                or any(not isinstance(packet[key], str) or not packet[key] for key in required)):
            raise SelectedExecutionError("Release retirement recording handoff is not closed")
        if (getattr(result, "outcome", None) != "pending"
                or getattr(result, "effect_outcome", None) != "retired"
                or getattr(result, "phase", None) != "retire"
                or getattr(result, "workflow_run_id", None) != workflow_run_id
                or getattr(result, "step_run_id", None) != step_run_id
                or getattr(result, "action_run_id", None) != action_run_id
                or getattr(result, "step_atom_id", None) != step_atom_id
                or getattr(result, "action_atom_id", None) != action_atom_id
                or getattr(result, "candidate_snapshot_manifest_sha256", None) != candidate_sha256
                or packet["candidate_snapshot_manifest_sha256"] != candidate_sha256
                or packet["on_recorded_result"] != frozen_result
                or effect_refs != [packet["retirement_receipt_ref"]]):
            raise SelectedExecutionError("Release retirement recording handoff differs from the frozen result")
        output = getattr(result, "output", None)
        if (getattr(output, "prior_image_digest", None) != packet["prior_image_digest"]
                or getattr(output, "receipt_sha256", None) != packet["retirement_receipt_sha256"]):
            raise SelectedExecutionError("Release retirement recording evidence differs from the private result")
        return dict(packet)

    def _private_release_image_executor(self) -> Any:
        """Return the program-owned image executor only when a Release Run begins.

        The Docker CLI executor is an implementation dependency, never a
        caller-selected Release parameter. Constructing it has no Docker
        effect; its first command remains inside the admitted image Action.
        Tests may inject an explicit private executor.
        """
        if self.release_image_executor is not None:
            return self.release_image_executor
        from release_image import DockerSubprocessExecutor

        return DockerSubprocessExecutor()

    @staticmethod
    def _canonical_terminal_receipt_ref(terminal_receipt: Mapping[str, Any]) -> str:
        """Return the sole sealed Journal event that closed one Action Run."""
        event_receipt = terminal_receipt.get("event_receipt")
        if not isinstance(event_receipt, Mapping):
            raise SelectedExecutionError("Release Action terminal receipt lacks its sealed Journal event identity")
        event_id = event_receipt.get("event_id")
        if not isinstance(event_id, str) or not event_id or event_id != event_id.strip():
            raise SelectedExecutionError("Release Action terminal receipt lacks a valid sealed Journal event identity")
        return event_id

    @staticmethod
    def _restored_completed_result_is_proven(
        session: Any, *, index: int, run: Any, shared_recordings: Mapping[int, Mapping[str, Any]],
        requested_action: str, action_run_id: str, expected_result: str,
        progress_reader: Callable[[str], Mapping[str, Any]],
        allowed_private_outcomes: frozenset[str] = frozenset({"completed"}),
    ) -> bool:
        """Require this Session's canonical terminal evidence before cached reuse.

        A checkpoint's ``shared_recordings`` entry is an untrusted recovery
        hint.  It cannot replace the exact Session terminal fact or its
        receipts and therefore can never by itself advance a Release phase.
        """
        if not callable(progress_reader):
            return False
        result = getattr(run, "results", {}).get(index)
        recording = shared_recordings.get(index)
        context = getattr(run, "contexts", {}).get(index)
        if (result is None or getattr(result, "outcome", None) not in allowed_private_outcomes or context is None
                or getattr(context, "action_run_id", None) != action_run_id
                or not isinstance(recording, Mapping)
                or recording.get("terminal_outcome") != "completed"):
            return False
        refs = recording.get("receipt_refs")
        if not isinstance(refs, tuple) or not refs or any(not isinstance(item, str) for item in refs):
            return False
        terminal = getattr(session, "terminal", {}).get(requested_action)
        if not isinstance(terminal, Mapping):
            return False
        if (terminal.get("disposition") != "terminal"
                or terminal.get("outcome") != "completed"
                or terminal.get("run_id") != action_run_id
                or terminal.get("effect_refs") != list(getattr(result, "effect_evidence_refs", ()))
                or not isinstance(terminal.get("result_ref"), str)
                or not terminal.get("result_ref")):
            return False
        try:
            terminal_event_id = SelectedNativeProviders._canonical_terminal_receipt_ref(terminal)
        except SelectedExecutionError:
            return False
        if refs != (terminal_event_id,):
            return False
        try:
            progress = progress_reader(requested_action)
        except Exception:
            # The trusted runtime reader is unavailable or rejected the fixed
            # run identity.  A sealed checkpoint alone is never enough to
            # reuse a private native effect.
            return False
        if not isinstance(progress, Mapping):
            return False
        if (
            progress.get("action_run_id") != action_run_id
            or progress.get("result") != expected_result
            or progress.get("effect_refs") != list(getattr(result, "effect_evidence_refs", ()))
        ):
            return False
        seen: set[str] = set()
        for receipt in getattr(session, "receipts", []):
            if not isinstance(receipt, Mapping):
                return False
            event_id = receipt.get("event_id")
            if not isinstance(event_id, str) or not event_id or event_id in seen:
                return False
            seen.add(event_id)
        return set(refs).issubset(seen)

    @staticmethod
    def _pending_recording_is_reconciled(
        session: Any, *, result: Any, pending_recording: Mapping[str, Any],
        requested_action: str, action_run_id: str, expected_result: str,
        progress_reader: Callable[[str], Mapping[str, Any]],
        allowed_private_outcomes: frozenset[str],
    ) -> bool:
        """Require current canonical evidence before clearing one pending hint.

        The checkpoint's pending identity describes a failed append, not a
        result.  Clearing it is safe only once the exact event identity,
        terminal result, and saved progress all agree in the reconstructed
        Session.  This function cannot append or replay anything.
        """
        if not callable(progress_reader) or not isinstance(pending_recording, Mapping):
            return False
        if set(pending_recording) != {"event_id", "event_outcome"}:
            return False
        event_id = pending_recording.get("event_id")
        event_outcome = pending_recording.get("event_outcome")
        if (
            not isinstance(event_id, str) or not event_id
            or event_outcome not in {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}
            or result is None or getattr(result, "outcome", None) not in allowed_private_outcomes
        ):
            return False
        terminal = getattr(session, "terminal", {}).get(requested_action)
        if (
            not isinstance(terminal, Mapping)
            or terminal.get("disposition") != "terminal"
            or terminal.get("outcome") != event_outcome
            or terminal.get("run_id") != action_run_id
            or terminal.get("effect_refs") != list(getattr(result, "effect_evidence_refs", ()))
        ):
            return False
        try:
            terminal_event_id = SelectedNativeProviders._canonical_terminal_receipt_ref(terminal)
        except SelectedExecutionError:
            return False
        if terminal_event_id != event_id:
            return False
        matching = 0
        for receipt in getattr(session, "receipts", []):
            if not isinstance(receipt, Mapping):
                return False
            matching += receipt.get("event_id") == event_id
        if matching != 1:
            return False
        try:
            progress = progress_reader(requested_action)
        except Exception:
            return False
        return (
            isinstance(progress, Mapping)
            and progress.get("action_run_id") == action_run_id
            and progress.get("result") == expected_result
            and progress.get("effect_refs") == list(getattr(result, "effect_evidence_refs", ()))
        )

    @staticmethod
    def _restored_action_without_typed_result_is_blocked(
        context: Mapping[str, Any], *, cached_result: bool,
    ) -> bool:
        """Reject an already-started Release Action whose private state is absent.

        Canonical Run evidence establishes only that the shared Action began.
        It cannot prove whether a native helper effect occurred.  A resumed
        action therefore needs its matching typed private result; otherwise it
        remains blocked rather than being replayed.
        """
        return context.get("restored_action") is True and not cached_result

    def _release_handlers(self, frozen: Mapping[str, Any], parameters: Any) -> dict[str, Callable]:
        """One lazy, process-local private frontier per frozen actual dispatch.

        Shared SelectedExecution remains the only recorder. Process-restart
        reconstruction/recording recovery is not supplied by this closure.
        """
        release_root = Path(__file__).resolve().parents[2] / "201_TOOLS/RELEASE_VERSION"
        mcp_root = Path(__file__).resolve().parents[2] / "204_MCP"
        for location in (release_root, mcp_root):
            if str(location) not in sys.path:
                sys.path.insert(0, str(location))
        from release_actions import (PHASES, AdmittedImageExecutor, SelectedReleaseActionContext,
                                     begin_release_action_run, execute_release_action)
        from release_checkpoint import (
            dump_release_checkpoint,
            extract_pending_recordings,
            load_release_checkpoint,
        )
        from selected_routes import load_selected_manifest
        from workflow_run_support import RunExecutionSession

        execution = json.loads(canonical_json(frozen["request"]["execution"]))
        graph = json.loads(canonical_json(frozen.get("graph")))
        admitted = load_selected_manifest(self.root)
        selected = SelectedExecution(self.root)
        current_graph = selected._revalidate(frozen)
        if (not isinstance(parameters, Mapping) or not isinstance(graph, Mapping)
                or frozen["request"].get("operation") != "enqueue_selected"
                or execution.get("mode") != "execute"
                or graph.get("route") != "release_version"
                or graph.get("workflow", {}).get("atom_id") != "CA-O-164"
                # The admitted source is the current O164@3 graph.  This is
                # deliberately an equality to the source admission, rather
                # than the retired hard-coded @2 provider contract.
                or graph["workflow"].get("version") != 3
                or not admitted.get("release_source_admissions")
                or execution.get("definition_manifest") != {"manifest_ref": admitted["manifest_ref"],
                    "manifest_digest": admitted["canonical_manifest_sha256"]}
                or canonical_json(current_graph) != canonical_json(graph)):
            raise SelectedExecutionError("Release requires the exact current source-admitted frozen O164 dispatch")
        steps = graph.get("steps", [])
        pairs = [(step.get("atom_id"), step.get("actions", [{}])[0].get("atom_id")) for step in steps
                 if isinstance(step, Mapping) and isinstance(step.get("actions"), list) and len(step["actions"]) == 1]
        if pairs != [phase[:2] for phase in PHASES] or len(steps) != len(PHASES):
            raise SelectedExecutionError("Release frozen Step/Action occurrences differ from the admitted ten phases")

        def expected_result_for(index: int) -> str:
            """Resolve one frozen graph result; never infer it from progress."""
            action = steps[index]["actions"][0]
            result_map = action.get("result_map", {})
            edges = steps[index].get("on_result", [])
            if (not isinstance(result_map, Mapping) or len(edges) != 1
                    or not isinstance(edges[0], Mapping)
                    or not isinstance(edges[0].get("result"), str)):
                raise SelectedExecutionError("Release phase lacks one frozen source result transition")
            expected = result_map.get(edges[0]["result"], edges[0]["result"])
            if not isinstance(expected, str):
                raise SelectedExecutionError("Release phase has an invalid frozen result mapping")
            return expected

        def reconcile_pending_recordings(
            session: RunExecutionSession,
            run: Any,
            checkpoint: Callable[[Any], None],
            progress_reader: Any,
            pending_recordings: dict[int, dict[str, str]],
            shared_recordings: dict[int, dict[str, Any]],
        ) -> str | None:
            """Replace only canonically reconciled pending hints with receipts.

            A pending identity stays in the sealed checkpoint until the exact
            Journal event is visible in the restored Session and its saved
            progress still agrees.  Nothing here invokes a Release phase.
            """
            if not pending_recordings:
                return None
            if not callable(progress_reader):
                return "Release pending Journal recovery lacks the trusted progress reader"
            resolved: list[tuple[int, dict[str, str], str]] = []
            requested_workflow = frozen["request"]["run_id"]
            for saved_index, record in sorted(pending_recordings.items()):
                context = getattr(run, "contexts", {}).get(saved_index)
                result = getattr(run, "results", {}).get(saved_index)
                if context is None or result is None:
                    return "Release pending Journal recovery lacks the exact private phase context"
                requested_step = SelectedExecution._requested_step_id(requested_workflow, saved_index + 1, 1)
                requested_action = f"{requested_step}:action:1"
                allowed = frozenset({"completed"})
                if saved_index == len(PHASES) - 1 and getattr(result, "outcome", None) == "pending":
                    if not isinstance(getattr(result, "shared_action_recording", None), Mapping):
                        return "Release pending retirement recovery lacks its closed handoff"
                    allowed = frozenset({"pending"})
                if not self._pending_recording_is_reconciled(
                    session,
                    result=result,
                    pending_recording=record,
                    requested_action=requested_action,
                    action_run_id=context.action_run_id,
                    expected_result=expected_result_for(saved_index),
                    progress_reader=progress_reader,
                    allowed_private_outcomes=allowed,
                ):
                    return "Release pending Journal recovery has no exact canonical receipt and matching progress"
                terminal = session.terminal[requested_action]
                try:
                    terminal_event_id = self._canonical_terminal_receipt_ref(terminal)
                except SelectedExecutionError:
                    return "Release pending Journal recovery lacks the sealed terminal event identity"
                resolved.append((saved_index, record, terminal_event_id))
            for saved_index, record, terminal_event_id in resolved:
                shared_recordings[saved_index] = {
                    "terminal_outcome": record["event_outcome"],
                    "receipt_refs": (terminal_event_id,),
                }
            pending_recordings.clear()
            try:
                checkpoint(run)
            except Exception as error:
                return f"Release pending Journal recovery checkpoint could not be saved: {error}"
            return None

        private_run, private_session = None, None
        shared_recordings: dict[int, dict[str, Any]] = {}
        pending_recordings: dict[int, dict[str, str]] = {}

        def release(context: dict[str, Any]) -> Mapping[str, Any]:
            nonlocal private_run, private_session, shared_recordings, pending_recordings
            session = context.get("session")
            if (not isinstance(session, RunExecutionSession) or context.get("sealed_outer_admission") is not True
                    or Path(context.get("project_root", "")).resolve() != self.root
                    or context.get("route") != "release_version"
                    or canonical_json(context.get("parameters")) != canonical_json(parameters)
                    or canonical_json(context.get("workflow_definition")) != canonical_json(graph["workflow"])
                    or session.request.get("request_id") != execution.get("request_id")
                    or canonical_json(session.request.get("parameters")) != canonical_json(parameters)):
                raise SelectedExecutionError("Release provider requires the exact frozen selected Session context")
            matches = [index for index, pair in enumerate(pairs) if pair ==
                       (context.get("step_definition_id"), context.get("action_definition_id"))]
            if len(matches) != 1:
                raise SelectedExecutionError("Release Step/Action pair is not selected")
            index = matches[0]
            requested_workflow = frozen["request"]["run_id"]
            requested_step = SelectedExecution._requested_step_id(requested_workflow, index + 1, 1)
            requested_action = f"{requested_step}:action:1"
            workflow = session.actual.get(requested_workflow, {})
            step = session.actual.get(requested_step, {})
            action = session.actual.get(requested_action, {})
            if (workflow.get("run_id") != context.get("workflow_run_id")
                    or step.get("run_id") != context.get("step_run_id")
                    or action.get("run_id") != context.get("action_run_id")
                    or step.get("parent_run_id") != workflow.get("run_id")
                    or action.get("parent_run_id") != step.get("run_id")
                    or context.get("requested_action_run_id") != requested_action
                    or canonical_json(context.get("action_definition")) != canonical_json(steps[index]["actions"][0])
                    or canonical_json(context.get("step_definition")) != canonical_json({key: value for key, value in steps[index].items()
                        if key not in {"actions", "on_result"}})
                    or (private_session is not None and private_session is not session)):
                raise SelectedExecutionError("Release actual Workflow/Step/Action parent identities differ")
            if index:
                prior_action = f"{SelectedExecution._requested_step_id(requested_workflow, index, 1)}:action:1"
                recorded = session.terminal.get(prior_action, {})
                if recorded.get("disposition") != "terminal" or recorded.get("outcome") != "completed":
                    return self._blocked("Release previous Action is not durably completed; no next phase or replay")
            if private_run is None:
                checkpoint_writer = context.get("checkpoint_writer")
                checkpoint_reader = context.get("checkpoint_reader")
                if not callable(checkpoint_writer) or not callable(checkpoint_reader):
                    return self._blocked("Release requires the injected private checkpoint reader and writer before any effect")
                executor = AdmittedImageExecutor(
                    str(self.root), workflow["run_id"], self._private_release_image_executor(),
                )
                try:
                    persisted = checkpoint_reader()
                except Exception as error:  # Reader is a trusted runtime boundary, not caller data.
                    return self._blocked(f"Release checkpoint could not be read before any effect: {error}")

                def checkpoint(run: Any) -> None:
                    checkpoint_writer(dump_release_checkpoint(
                        run,
                        shared_recordings=shared_recordings,
                        pending_recordings=pending_recordings,
                    ))

                if persisted is None:
                    private_run = begin_release_action_run(
                        parameters, workflow_run_id=workflow["run_id"], image_executor=executor,
                        checkpoint_callback=checkpoint,
                    )
                elif isinstance(persisted, Mapping):
                    try:
                        restored, restored_recordings = load_release_checkpoint(
                            persisted, expected_request=parameters,
                            expected_workflow_run_id=workflow["run_id"], image_executor=executor,
                        )
                    except Exception as error:
                        return self._blocked(f"Release checkpoint is not admitted for this frozen Run: {error}")
                    # Contexts are retained source bindings, not caller data.
                    if any(
                        item.workflow_atom_id != graph["workflow"]["atom_id"]
                        or item.workflow_version != graph["workflow"]["version"]
                        or item.project_root != str(self.root)
                        or item.workflow_run_id != workflow["run_id"]
                        or (item.step_atom_id, item.action_atom_id) != pairs[saved_index]
                        for saved_index, item in restored.contexts.items()
                    ):
                        return self._blocked("Release checkpoint contexts differ from the exact current source-3 graph")
                    private_run = restored
                    shared_recordings = dict(restored_recordings)
                    try:
                        pending_recordings = {
                            index: dict(record)
                            for index, record in extract_pending_recordings(persisted).items()
                        }
                    except Exception as error:
                        return self._blocked(f"Release checkpoint pending recording identity is invalid: {error}")
                    private_run.checkpoint_callback = checkpoint
                    if pending_recordings:
                        blocker = reconcile_pending_recordings(
                            session, private_run, checkpoint,
                            context.get("checkpoint_progress_reader"),
                            pending_recordings, shared_recordings,
                        )
                        if blocker is not None:
                            return self._blocked(blocker)
                    # A persisted pre-effect frontier means a process stopped
                    # between checkpoint and helper invocation.  There is no
                    # recovery entry here, so replay is intentionally blocked.
                    if private_run.in_progress is not None:
                        return self._blocked("Release checkpoint records an in-progress effect; replay requires an explicit recovery entry")
                else:
                    return self._blocked("Release checkpoint reader returned an invalid checkpoint carrier")
                private_session = session
            typed = SelectedReleaseActionContext(
                str(self.root), workflow["run_id"], step["run_id"], action["run_id"],
                workflow["run_id"], step["run_id"], pairs[index][0], pairs[index][1],
                private_run.frozen_parameters_sha256,
                workflow_atom_id=graph["workflow"]["atom_id"],
                workflow_version=graph["workflow"]["version"],
            )
            cached_result = index in private_run.results
            if self._restored_action_without_typed_result_is_blocked(
                context, cached_result=cached_result,
            ):
                return self._blocked(
                    "Release restored Action lacks its typed private result; no effect replay"
                )
            cached_retirement = (
                cached_result
                and index == len(PHASES) - 1
                and getattr(private_run.results[index], "outcome", None) == "pending"
                and isinstance(getattr(private_run.results[index], "shared_action_recording", None), Mapping)
            )
            if cached_result:
                expected_result = expected_result_for(index)
                progress_reader = context.get("checkpoint_progress_reader")
                if not self._restored_completed_result_is_proven(
                    session, index=index, run=private_run, shared_recordings=shared_recordings,
                    requested_action=requested_action, action_run_id=action_run_id,
                    expected_result=expected_result, progress_reader=progress_reader,
                    allowed_private_outcomes=frozenset({"pending"}) if cached_retirement else frozenset({"completed"}),
                ):
                    return self._blocked("Release cached result lacks exact canonical Session and progress proof; no replay")
            result = execute_release_action(parameters, context=typed, run=private_run)
            refs = list(result.effect_evidence_refs)
            for reference in refs:
                reference_path = reference.split("#", 1)[0]
                relative = Path(reference_path)
                try:
                    observed = (self.root / relative).resolve(strict=True)
                    observed.relative_to(self.root)
                except (OSError, ValueError):
                    observed = None
                if (not reference_path or reference_path in {".", "./"}
                        or relative.is_absolute() or ".." in relative.parts or observed is None):
                    raise SelectedExecutionError("Release returned an unavailable or unsafe observed effect reference")
            outcome = {"completed": "completed", "prepared": "no_op", "failed": "failed"}.get(result.outcome, "interrupted_pending")
            label = result.outcome
            if result.outcome == "completed":
                edges = steps[index].get("on_result", [])
                if len(edges) != 1 or not isinstance(edges[0].get("result"), str):
                    raise SelectedExecutionError("Release completed phase lacks one frozen source result transition")
                label = edges[0]["result"]
            recording = None
            if getattr(result, "shared_action_recording", None) is not None:
                edges = steps[index].get("on_result", [])
                if len(edges) != 1 or not isinstance(edges[0].get("result"), str):
                    raise SelectedExecutionError("Release retired phase lacks one frozen source result transition")
                candidate = getattr(getattr(private_run, "request", None), "candidate_snapshot_manifest", None)
                candidate_sha256 = getattr(candidate, "sha256", None)
                if not isinstance(candidate_sha256, str):
                    raise SelectedExecutionError("Release retirement recording lacks the frozen candidate identity")
                recording = self._shared_retirement_recording(
                    result, candidate_sha256=candidate_sha256,
                    workflow_run_id=workflow["run_id"], step_run_id=step["run_id"],
                    action_run_id=action["run_id"], step_atom_id=pairs[index][0],
                    action_atom_id=pairs[index][1], frozen_result=edges[0]["result"],
                    effect_refs=refs,
                )
                label, outcome = "pending", "completed"
            if cached_retirement:
                # The final native retirement remains `pending` in the
                # private adapter by design.  Its separately proven shared
                # Action terminal receipt turns the restored graph result
                # into the frozen completion edge without rerunning the
                # effect or re-recording the handoff.
                label, outcome = expected_result, "completed"
            output = {"result": label, "terminal_outcome": outcome, "effect_refs": refs,
                      "native_result": self._json_value(result)}

            # The current shared Session already proves this reconstructed
            # Action terminal result.  Do not ask the generic executor to
            # append a duplicate event, and do not re-offer the retirement
            # handoff that the canonical receipt has already closed.
            if cached_result:
                output["action_terminal_recorded"] = True
                recording = None

            def record_shared_receipt(
                terminal_receipt: Any, pending_event_ids: Any, canonical_receipts: Any,
            ) -> None:
                """Persist the private frontier only after the sole Session terminal write.

                No caller flag or private effect upgrades a Release result.  A
                terminal receipt with pending Journal evidence remains merely a
                checkpointed private observation, so the generic executor will
                stop at ``recording_pending`` rather than take an On Result edge.
                """
                writer = context.get("checkpoint_writer")
                if not callable(writer):
                    raise SelectedExecutionError("Release checkpoint writer disappeared before shared receipt recording")
                if not isinstance(pending_event_ids, list) or any(not isinstance(item, str) or not item for item in pending_event_ids):
                    raise SelectedExecutionError("Release shared receipt recorder received invalid pending event identities")
                # A failed Journal append has already been retained by the
                # Session as recording_pending.  Persist the private frontier
                # without a shared-recording hint and let the generic executor
                # stop; do not turn a recorder outage into a second effect or
                # an exception that obscures that truthful pending result.
                if not isinstance(terminal_receipt, Mapping) or terminal_receipt.get("disposition") != "terminal":
                    if isinstance(terminal_receipt, Mapping) and terminal_receipt.get("disposition") == "recording_pending":
                        if (
                            len(pending_event_ids) != 1
                            or not isinstance(terminal_receipt.get("outcome"), str)
                            or terminal_receipt["outcome"] not in {
                                "completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending",
                            }
                        ):
                            raise SelectedExecutionError(
                                "Release pending Journal recording lacks one exact original event identity"
                            )
                        pending_recordings[index] = {
                            "event_id": pending_event_ids[0],
                            "event_outcome": terminal_receipt["outcome"],
                        }
                    writer(dump_release_checkpoint(
                        private_run,
                        shared_recordings=shared_recordings,
                        pending_recordings=pending_recordings,
                    ))
                    return
                if (terminal_receipt.get("outcome") != outcome
                        or terminal_receipt.get("run_id") != action["run_id"]
                        or terminal_receipt.get("effect_refs") != refs
                        or not isinstance(terminal_receipt.get("result_ref"), str)
                        or not terminal_receipt.get("result_ref")):
                    raise SelectedExecutionError("Release shared receipt differs from the exact Action result")
                receipt_ref = self._canonical_terminal_receipt_ref(terminal_receipt)
                if not pending_event_ids:
                    shared_recordings[index] = {
                        "terminal_outcome": outcome,
                        "receipt_refs": (receipt_ref,),
                    }
                writer(dump_release_checkpoint(
                    private_run,
                    shared_recordings=shared_recordings,
                    pending_recordings=pending_recordings,
                ))

            if not cached_result:
                output["record_shared_receipt"] = record_shared_receipt
            if recording is not None and not cached_result:
                output["shared_action_recording"] = recording
            return output

        return {action_id: release for _step_id, action_id, _phase in PHASES}

    @staticmethod
    def _blocked(reason: str) -> dict[str, Any]:
        return {"result": "blocked", "terminal_outcome": "interrupted_pending", "effect_refs": [],
                "native_result": {"outcome": "blocked", "blockers": [reason]}}

    def dispatch(self, run_id: str) -> dict[str, Any]:
        """Load one persisted request and use the existing shared Run dispatcher."""
        frozen = SelectedExecution(self.root).load(run_id)
        return self.execution(frozen).dispatch(frozen)

    def recover_release(self, run_id: str, request_identity: str) -> dict[str, Any]:
        """Invoke only the sealed private Release recovery boundary."""
        frozen = SelectedExecution(self.root).load(run_id)
        request = frozen.get("request") if isinstance(frozen, Mapping) else None
        execution = request.get("execution") if isinstance(request, Mapping) else None
        import sys
        tools_root = Path(__file__).resolve().parents[2] / "201_TOOLS"
        if str(tools_root) not in sys.path:
            sys.path.insert(0, str(tools_root))
        from workflow_run_support import _canonical_digest
        if (not isinstance(execution, Mapping) or execution.get("operation_route") != "release_version"
                or _canonical_digest(execution) != request_identity):
            raise SelectedExecutionError("Release recovery request does not match the frozen Release request")
        return self.execution(frozen).recover_release(frozen)
