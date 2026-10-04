"""Explicit worker providers, scoped to one frozen selected dispatch at a time."""
from __future__ import annotations

from collections.abc import Callable, Mapping
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

    def __init__(self, root: str | Path, *, implementation_agent: Callable[..., Mapping[str, Any]] | None = None):
        self.root = Path(root).resolve(strict=True)
        self.implementation_agent = implementation_agent if implementation_agent is not None else ImplementationAgent()
        if not callable(self.implementation_agent):
            raise TypeError("implementation agent must be callable")

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

        return SelectedExecution(self.root, handlers={"CA-O-131": revert},
                                 implementation_agent=self.implementation_agent)

    @staticmethod
    def _blocked(reason: str) -> dict[str, Any]:
        return {"result": "blocked", "terminal_outcome": "interrupted_pending", "effect_refs": [],
                "native_result": {"outcome": "blocked", "blockers": [reason]}}

    def dispatch(self, run_id: str) -> dict[str, Any]:
        """Load one persisted request and use the existing shared Run dispatcher."""
        frozen = SelectedExecution(self.root).load(run_id)
        return self.execution(frozen).dispatch(frozen)
