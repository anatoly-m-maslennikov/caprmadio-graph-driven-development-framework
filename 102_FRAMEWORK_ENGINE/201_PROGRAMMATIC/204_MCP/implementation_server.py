"""Reloadable Project-local stdio implementation behind the stable gateway."""
import argparse
from pathlib import Path
import sys
from typing import Any

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations

TOOLS_ROOT = Path(__file__).resolve().parents[1] / '201_TOOLS'
TOOLS = TOOLS_ROOT / 'RMED_ATOMS_BASE_REVISE'
sys.path.insert(0, str(TOOLS_ROOT))
sys.path.insert(0, str(TOOLS_ROOT / 'VALIDATE_ATOMS'))
sys.path.insert(0, str(TOOLS))
from rmed_atoms_base_revise import Request, run  # noqa: E402 - repository path bootstrap
from capability_discovery.service import Service, Query, Context, Observation, Watch  # noqa: E402
sys.path.insert(0, str(TOOLS_ROOT.parent / '203_APPS/WORKFLOW_ORCHESTRATOR'))
from orchestrator import Request as OrchestratorRequest, run as orchestrate  # noqa: E402
from selected_routes import QUERY_ROUTE_NAMES, register_selected_routes  # noqa: E402


def register_orchestrator(server, root):
    @server.tool(name='workflow_orchestrator', structured_output=True, annotations=ToolAnnotations(
        read_only_hint=False, destructive_hint=False, idempotent_hint=True, open_world_hint=False))
    def workflow_orchestrator(request: OrchestratorRequest) -> dict[str, Any]:
        """Enqueue or inspect an independent Run; requires an explicitly initialized local worker."""
        try:
            return orchestrate(root, request)
        except (ValueError, OSError, RuntimeError) as error:
            raise ToolError(str(error)) from error


def create_server(root):
    root = Path(root).resolve(strict=True)
    discovery = Service(root, exposed=('discover_tools', 'discover_operations',
        'get_execution_context', 'get_execution_status', 'resume_execution_context',
        'watch_execution', 'rmed_atoms_base_revise', 'workflow_orchestrator',
        *QUERY_ROUTE_NAMES))
    server = MCPServer('CAPRMEDIO', version='0.1.0', instructions=
        'Discovery and read-only Run observation; Operator-authorized, caller-coordinated '
        'gather/check/fix. workflow_orchestrator enqueues explicitly authorized Runs '
        'for a separately started worker. No recheck or automatically started Runs.')
    register_orchestrator(server, root)

    @server.tool(name='rmed_atoms_base_revise', structured_output=True, annotations=ToolAnnotations(
        read_only_hint=False, destructive_hint=False, idempotent_hint=False, open_world_hint=False))
    def workflow(request: Request) -> dict[str, Any]:
        """Describe or coordinate RMED Atoms Base Revise; root is fixed at server startup."""
        try:
            return run(root, request)
        except (ValueError, OSError, RuntimeError, KeyError, TypeError, IndexError) as error:
            raise ToolError(str(error)) from error

    annotations = ToolAnnotations(read_only_hint=True, destructive_hint=False,
                                  idempotent_hint=True, open_world_hint=False)

    @server.tool(name='discover_tools', annotations=annotations)
    def discover_tools(request: Query) -> dict[str, Any]:
        """Find declared Tools and observed source availability."""
        return discovery.discover(request)

    @server.tool(name='discover_operations', annotations=annotations)
    def discover_operations(request: Query) -> dict[str, Any]:
        """Find active methodology Actions and Workflows."""
        return discovery.discover(request, operations=True)

    @server.tool(name='get_execution_context', annotations=annotations)
    def get_execution_context(request: Context) -> dict[str, Any]:
        """Read an exact capability definition without executing it."""
        return discovery.context(request)

    @server.tool(name='get_execution_status', annotations=annotations)
    def get_execution_status(request: Observation) -> dict[str, Any]:
        """Read saved Run progress and optional results."""
        return discovery.status(request)[0]

    @server.tool(name='resume_execution_context', annotations=annotations)
    def resume_execution_context(request: Observation) -> dict[str, Any]:
        """Recover saved inputs and pending work without dispatch or replay."""
        return discovery.resume(request)

    @server.tool(name='watch_execution', annotations=annotations)
    async def watch_execution(request: Watch) -> dict[str, Any]:
        """Wait for saved Run changes and confirmed Journal events using a cursor."""
        return await discovery.watch(request)

    register_selected_routes(server, root)
    return server


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root', required=True, type=Path)
    args = parser.parse_args()
    create_server(args.project_root).run(transport='stdio')
