"""One bounded proposal at a time; no Project or Docker mounts in this service."""

import asyncio
import json
import os
from pathlib import Path
import tempfile
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from agent import CodexAgent
from contracts import AgentOutput

MAX_BYTES = 8 * 1024 * 1024
busy = False
calls = 0


class Dispatch(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    context: dict
    phase: Literal["check", "fix"]
    timeout: int = Field(ge=1, le=3600)


def mock_output(context, phase):
    import copy
    import time

    if "SLOW_MOCK" in context["source_content"]:
        time.sleep(15)
    if phase == "check":
        report = {
            key: context[key] for key in ("workflow_run_id", "atom_id", "source", "criteria_sha256")
        }
        report.update(
            checks={
                name: {"status": "passed", "evidence": "mock quotation"}
                for name in ("properties", "cce", "scope", "claim", "details", "summary")
            },
            findings=[],
            blockers=[],
            corrections=[],
            unresolved_findings=[],
            rejected_findings=[],
            fix_blockers=[],
            coverage_gaps=[],
            result="checked_clean",
        )
        if "bad wording" in context["source_content"]:
            report["checks"]["cce"]["status"] = "failed"
            report.update(
                findings=[{"id": "f1", "check": "cce", "evidence": "bad wording"}],
                unresolved_findings=[{"finding_id": "f1"}],
                result="issues",
            )
        candidate = None
    else:
        report = copy.deepcopy(context["report"])
        report.update(
            result="fixed_not_rechecked",
            unresolved_findings=[],
            corrections=[{"finding_id": "f1", "change": "mock correction"}],
        )
        candidate = (
            context["source_content"]
            .replace("bad wording", "good wording")
            .replace("2026-10-01T00:00:00Z", "2026-10-04T00:00:00Z")
        )
    return {"report_json": json.dumps(report), "candidate_content": candidate, "confidence": 99.0}


def execute(dispatch):
    if os.environ.get("CAPRMEDIO_AGENT_MODE") == "mock":
        return mock_output(dispatch.context, dispatch.phase)
    with tempfile.TemporaryDirectory(prefix="caprmedio-agent-") as directory:
        return CodexAgent(container_isolation=True).execute(
            dispatch.context, dispatch.phase, Path(directory), dispatch.timeout
        )


async def health(request):
    mode = os.environ.get("CAPRMEDIO_AGENT_MODE", "codex")
    ready = mode == "mock" or (Path.home() / ".codex/auth.json").is_file()
    return JSONResponse({"ready": ready, "mode": mode, "busy": busy, "calls": calls})


async def submit(request):
    global busy, calls
    chunks = bytearray()
    async for chunk in request.stream():
        chunks.extend(chunk)
        if len(chunks) > MAX_BYTES:
            return JSONResponse({"error": "request_too_large"}, status_code=413)
    try:
        dispatch = Dispatch.model_validate_json(bytes(chunks))
    except ValidationError:
        return JSONResponse({"error": "invalid_dispatch"}, status_code=422)
    if busy:
        return JSONResponse({"error": "agent_busy"}, status_code=409)
    busy = True
    calls += 1
    try:
        value = await asyncio.to_thread(execute, dispatch)
        admitted = AgentOutput.model_validate(value).model_dump()
        if len(json.dumps(admitted).encode()) > MAX_BYTES:
            raise ValueError("response_too_large")
        return JSONResponse(admitted)
    except RuntimeError, ValueError, OSError:
        return JSONResponse({"error": "agent_execution_failed"}, status_code=502)
    finally:
        busy = False


app = Starlette(routes=[Route("/health", health), Route("/execute", submit, methods=["POST"])])
