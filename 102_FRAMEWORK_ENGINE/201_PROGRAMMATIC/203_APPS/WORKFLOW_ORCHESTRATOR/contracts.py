"""Strict caller and replaceable Agent adapter boundaries."""
from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_validator


class Strict(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)


class Selected(Strict):
    atom_id: str = Field(min_length=1, max_length=256)
    path: str = Field(min_length=1)


class Enqueue(Strict):
    operation: Literal['enqueue'] = 'enqueue'
    workflow_id: Literal['CA-O-104'] = 'CA-O-104'
    run_id: str = Field(pattern=r'^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$')
    selection: list[Selected] = Field(max_length=10000)
    criteria_paths: list[str] = Field(min_length=1, max_length=1000)
    author: str = Field(min_length=1)
    journal_author: str | None = Field(default=None, pattern=r'^[A-Za-z0-9][A-Za-z0-9-]{0,38}$')
    scope: str = Field(min_length=1)
    confidence_threshold: float = Field(default=90.0, ge=0, le=100)
    allow_fixes: bool = False
    allow_replacements: bool = False
    agent_timeout_seconds: int = Field(default=600, ge=1, le=3600)

    @model_validator(mode='after')
    def replacement_permission(self):
        if self.allow_replacements and not self.allow_fixes:
            raise ValueError('allow_replacements requires allow_fixes=true')
        return self


class EnqueueSelected(Strict):
    """Tagged APPS queue request; shared RUN_SUPPORT owns inner request semantics."""
    operation: Literal['enqueue_selected'] = 'enqueue_selected'
    run_id: str = Field(pattern=r'^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$')
    execution: dict[str, Any]

    @model_validator(mode='after')
    def selected_execution_is_present(self):
        if not self.execution:
            raise ValueError('execution is required')
        return self


class RecoverSelectedRelease(Strict):
    """One sealed request identity for an already-admitted Release Run."""
    operation: Literal['recover_selected_release'] = 'recover_selected_release'
    run_id: str = Field(pattern=r'^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$')
    request_identity: str = Field(pattern=r'^[0-9a-f]{64}$')


class ResolveReleaseUnknownEffect(Strict):
    """One closed, Operator-authorized resolution of the named N15 effect."""
    operation: Literal['resolve_release_unknown_effect'] = 'resolve_release_unknown_effect'
    run_id: Literal['release-epic-resume-20261006-N15'] = 'release-epic-resume-20261006-N15'
    request_identity: Literal['5228bc2214ef3868794ae48f12c435c266587fd856fcefdd4598612b3ba80ec4'] = '5228bc2214ef3868794ae48f12c435c266587fd856fcefdd4598612b3ba80ec4'
    authorization_ref: Literal['.caprmedio_caprmedio/01_concern/CA-C-517-QUESTION--resolve-the-unknown-n15-unit-outcome.md'] = '.caprmedio_caprmedio/01_concern/CA-C-517-QUESTION--resolve-the-unknown-n15-unit-outcome.md'
    authorization_sha256: Literal['1d3d7c3c1d10827362952d684193fe844e634d18dfa5098a32f54af4863974d4'] = '1d3d7c3c1d10827362952d684193fe844e634d18dfa5098a32f54af4863974d4'
    expected_checkpoint_sha256: Literal['71d93f97c0f07b84e94d49d5bd18a4ab83d86e3e52d00e39368ce881153a4344'] = '71d93f97c0f07b84e94d49d5bd18a4ab83d86e3e52d00e39368ce881153a4344'


class RecoverSelectedReleaseStatus(Strict):
    operation: Literal['recover_selected_release_status'] = 'recover_selected_release_status'
    run_id: str = Field(pattern=r'^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$')
    recovery_transport_handle: str = Field(pattern=r'^[0-9a-f]{32}$')


class Status(Strict):
    operation: Literal['status'] = 'status'
    run_id: str = Field(pattern=r'^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$')


class AgentOutput(Strict):
    report_json: str
    candidate_content: str | None
    confidence: float = Field(ge=0, le=100)
