"""Interpret one frozen, source-bound selected Workflow through shared Run support.

This module deliberately has no route-domain branches.  The MCP-owned manifest
declares the Workflow, Steps, Action bindings and `On Result` transitions; the
TOOLS-owned Run tracker seals admission and Journal evidence.  This APPS layer
only freezes/rechecks the graph and gives registered native Action adapters the
actual Run context.
"""
from __future__ import annotations

from collections.abc import Callable, Mapping
import hashlib
import json
from pathlib import Path
import re
import tempfile
import tomllib
from typing import Any


MANIFEST_DEFAULT = "_projection/selected_workflow_bindings.json"
RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
SECRET_TERMS = {"secret", "password", "token", "credential", "api_key", "apikey"}
ActionHandler = Callable[[dict[str, Any]], Mapping[str, Any]]


class SelectedExecutionError(RuntimeError):
    """A selected request cannot safely progress through the queue."""


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

            def atom_lifecycle(context: dict[str, Any]) -> dict[str, Any]:
                action = lifecycle.get(context["route"])
                if action is None:
                    return {"result": "blocked", "effect_refs": []}
                result = action(self.root, context["parameters"], execute=True, authorized=True)
                native_outcome = result.get("outcome")
                result_label = {"duplicate": "no-op", "no-op": "no-op"}.get(native_outcome, native_outcome)
                terminal_outcome = {
                    "applied": "completed", "no-op": "no_op", "duplicate": "no_op",
                    "failed": "failed", "partial": "partial", "canceled": "cancelled",
                    "recording-blocked": "interrupted_pending", "blocked": "interrupted_pending",
                }.get(native_outcome, "interrupted_pending")
                return {"result": result_label, "terminal_outcome": terminal_outcome,
                        "effect_refs": paths(result.get("effects")), "native_result": result}

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
                    output = dict(result)
                    if label == "built":
                        output["terminal_outcome"] = "completed"
                    elif label == "no_op":
                        output["terminal_outcome"] = "no_op"
                    elif label == "failed":
                        output["terminal_outcome"] = "failed"
                    elif label in {"blocked", "pending_recording"}:
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
            implementation_results = {
                "evaluation_ready": "evaluation ready", "prepared": "tests prepared",
                "implemented": "implementation delivered", "passed": "checks pass",
                "failed": "checks fail", "retry_permitted": "retry admitted",
                "repaired": "repair completed", "implementation_defect": "repair admission",
                "test_implementation_defect": "repair admission",
            }
            for action_id, handler in implementation_actions.ACTION_HANDLERS.items():
                def implementation(context: dict[str, Any], handler: Any = handler) -> dict[str, Any]:
                    result = handler(
                        context["parameters"], agent=self.implementation_agent,
                        selected_project_root=self.root,
                    )
                    if not isinstance(result, Mapping) or not isinstance(result.get("result"), str):
                        raise SelectedExecutionError("implementation Action returned an invalid queue envelope")
                    label = implementation_results.get(result["result"], result["result"])
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
                    result = handler(context["parameters"])
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

    def run_directory(self, run_id: str) -> Path:
        if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
            raise SelectedExecutionError("invalid selected Run ID")
        return self.root / ".caprmedio_install/workflow_orchestrator/runs" / run_id

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
            __import__("os").fsync(temporary.fileno())
            temporary_path = Path(temporary.name)
        temporary_path.replace(path)

    @staticmethod
    def _read(path: Path) -> dict[str, Any]:
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
        """Translate the immutable D547 edge list without adding a route policy.

        The manifest represents each source Step/Action pair once and represents
        only actual ``On Result`` edges.  A missing edge is intentionally *not*
        interpreted as a successor: a native adapter must return a truthful
        ``terminal_outcome`` for that source result.
        """
        ordered = route.get("ordered_steps")
        entry = route.get("entry_step")
        if not isinstance(ordered, list) or not ordered or not isinstance(entry, str):
            raise SelectedExecutionError("D547 selected Workflow must bind ordered Steps and entry_step")
        transitions: dict[str, list[dict[str, Any]]] = {}
        raw_edges = route.get("on_result")
        if not isinstance(raw_edges, list):
            raise SelectedExecutionError("D547 selected Workflow On Result bindings are invalid")
        for raw in raw_edges:
            if not isinstance(raw, Mapping) or set(raw) != {"from", "condition", "to"}:
                raise SelectedExecutionError("D547 selected On Result binding is invalid")
            source, condition, target = raw["from"], raw["condition"], raw["to"]
            if not all(isinstance(value, str) and value for value in (source, condition, target)):
                raise SelectedExecutionError("D547 selected On Result binding has an invalid endpoint")
            transition = {"result": condition}
            if target == "complete":
                transition["terminal"] = "completed"
            else:
                transition["next"] = target
            transitions.setdefault(source, []).append(transition)
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
            step["on_result"] = transitions.get(step["atom_id"], [])
            normalized.append(step)
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

    @staticmethod
    def _support_definition(binding: Mapping[str, Any]) -> dict[str, Any]:
        """Translate a manifest pin into the shared service's source pin shape."""
        return {"atom_id": binding["atom_id"], "version": binding["version"],
                "path": binding["path"], "digest": binding["sha256"]}

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
                    expected.append({
                        "requested_run_id": f"{requested_step_id}:action:{action_ordinal}",
                        "kind": "action",
                        "definition": cls._support_definition(action),
                        "parent_requested_run_id": requested_step_id,
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
        return merged

    def _execute_graph(self, frozen: Mapping[str, Any], session: Any) -> dict[str, Any]:
        graph = frozen["graph"]
        request = frozen["request"]
        run_id = request["run_id"]
        steps = {row["atom_id"]: row for row in graph["steps"]}
        manifest_ordinals = {row["atom_id"]: ordinal for ordinal, row in enumerate(graph["steps"], start=1)}
        visit_limits = self._run_visit_limits(
            graph, self._declared_run_visit_limits(request["execution"]),
        )
        visit_counts: dict[str, int] = {}
        next_step = graph["entry_step"]
        journal_preparation = self._prepare_journal_query_before_run(graph, request["execution"])
        workflow_actual = session.start_run(run_id)
        workflow_run_id = workflow_actual["run_id"]
        results: list[dict[str, Any]] = []
        implementation_prior_results: list[dict[str, Any]] = []
        structural_prior_results: list[dict[str, Any]] = []
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
            for action_ordinal, action in enumerate(step["actions"], start=1):
                requested_action_id = f"{requested_step_id}:action:{action_ordinal}"
                actual_action = session.start_run(requested_action_id)
                action_run_id = actual_action["run_id"]
                handler = self.handlers.get(action["atom_id"])
                if handler is None:
                    raise SelectedExecutionError(f"no native handler registered for Action {action['atom_id']}")
                parameters = request["execution"].get("parameters")
                if graph["workflow"]["atom_id"] == "CA-O-016":
                    parameters = self._implementation_packet(parameters, step["atom_id"], implementation_prior_results)
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
                    "target_frontier": request["execution"].get("target_frontier"),
                    "effects": request["execution"].get("effects"),
                    "initiative": request["execution"].get("initiative"),
                    "sealed_outer_admission": True,
                    "session": session,
                    "requested_action_run_id": requested_action_id,
                }
                if action["atom_id"] == "CA-O-162":
                    context["journal_preparation"] = journal_preparation
                if graph["workflow"]["atom_id"] == "CA-O-015":
                    # This is executor-retained state only; structural Actions
                    # never admit caller-provided prior-result assertions.
                    context["structural_prior_results"] = list(structural_prior_results)
                output = handler(context)
                if not isinstance(output, Mapping) or not isinstance(output.get("result"), str):
                    raise SelectedExecutionError("native Action handler returned no declared result")
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
                            "native_result": output.get("native_result"),
                            "compiler_publication_recording": output.get("compiler_publication_recording")}
                self._write(progress_path, progress)
                terminal_receipt: Mapping[str, Any] | None = None
                if output.get("action_terminal_recorded") is not True:
                    action_outcome = output.get("terminal_outcome", "completed")
                    if action_outcome not in {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}:
                        raise SelectedExecutionError("native Action handler returned an invalid terminal outcome")
                    terminal_receipt = session.finish_run(
                        action_run_id, outcome=action_outcome,
                        result_ref=progress_path.relative_to(self.root).as_posix(),
                        effect_refs=effect_refs,
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
                session.finish_run(step_run_id, outcome=terminal, result_ref=result_ref,
                                   effect_refs=step_effect_refs)
                session.finish_run(workflow_run_id, outcome=terminal, result_ref=result_ref,
                                   effect_refs=effect_refs)
                return {**output, "result_ref": result_ref, "effect_refs": effect_refs}
            step_result_path = self.run_directory(run_id) / f"{requested_step_id}.json"
            self._write(step_result_path, {"result": final_result, "step_run_id": step_run_id,
                                            "action_results": results})
            session.finish_run(step_run_id, outcome="completed",
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

    def _shared_dispatch(self, frozen: Mapping[str, Any]) -> dict[str, Any]:
        """Late import keeps APPS importable while the shared service is replaced."""
        import sys
        tools_root = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
        if tools_root not in sys.path:
            sys.path.insert(0, tools_root)
        from workflow_run_support import RunTracker  # owned by P1510

        execution = dict(frozen["request"]["execution"])

        def observe(request: dict[str, Any]) -> dict[str, Any]:
            graph = self._revalidate(frozen)
            return {"selected": request.get("operation_route") == graph["route"], "current": True,
                    "observed": {"manifest_ref": graph["manifest_ref"],
                                 "manifest_digest": graph["manifest_digest"]}}

        tracker = RunTracker(self.root, source_observer=observe,
                             executor=lambda _request, session: self._execute_graph(frozen, session))
        return tracker.run_selected_operation(execution)

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
