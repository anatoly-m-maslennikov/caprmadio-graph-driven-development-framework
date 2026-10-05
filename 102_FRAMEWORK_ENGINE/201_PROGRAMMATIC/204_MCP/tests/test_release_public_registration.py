"""Pure public-registration guard for the additive Release MCP route."""
from __future__ import annotations

import sys
import types
import unittest
from unittest.mock import patch


MCP = __import__("pathlib").Path(__file__).resolve().parents[1]
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))

from selected_routes import (  # noqa: E402
    SELECTED_ROUTE_NAMES,
    SelectedRouteError,
    register_selected_routes,
)


class _ToolAnnotations:
    def __init__(self, **values: object) -> None:
        self.values = values


class _Server:
    def __init__(self) -> None:
        self.names: list[str] = []

    def tool(self, *, name: str, structured_output: bool, annotations: object):
        del structured_output, annotations

        def decorate(function):
            self.names.append(name)
            return function

        return decorate


def _manifest(names: tuple[str, ...]) -> dict[str, object]:
    return {"routes": [{"route": name} for name in names]}


class ReleasePublicRegistrationTest(unittest.TestCase):
    def register(self, loaded: object) -> list[str]:
        server = _Server()
        mcp_module = types.ModuleType("mcp")
        types_module = types.ModuleType("mcp.types")
        types_module.ToolAnnotations = _ToolAnnotations
        mcp_module.types = types_module
        with patch.dict(sys.modules, {"mcp": mcp_module, "mcp.types": types_module}), \
                patch("selected_routes.load_selected_manifest", return_value=loaded):
            register_selected_routes(server, ".")
        return server.names

    def test_static_fifteen_names_remain_unchanged(self) -> None:
        self.assertEqual(15, len(SELECTED_ROUTE_NAMES))
        self.assertNotIn("release_version", SELECTED_ROUTE_NAMES)

    def test_current_fifteen_manifest_omits_release(self) -> None:
        names = self.register(_manifest(SELECTED_ROUTE_NAMES))
        self.assertEqual(list(SELECTED_ROUTE_NAMES), names[:len(SELECTED_ROUTE_NAMES)])
        self.assertNotIn("release_version", names)

    def test_exact_admitted_sixteen_manifest_registers_release(self) -> None:
        names = self.register(_manifest((*SELECTED_ROUTE_NAMES, "release_version")))
        self.assertEqual([*SELECTED_ROUTE_NAMES, "release_version"], names[:16])
        self.assertEqual(1, names.count("release_version"))

    def test_invalid_or_stale_manifest_omits_release(self) -> None:
        for error in (
            SelectedRouteError("release-source-pin-stale: source pin is stale"),
            SelectedRouteError("selected workflow binding manifest is invalid"),
        ):
            server = _Server()
            mcp_module = types.ModuleType("mcp")
            types_module = types.ModuleType("mcp.types")
            types_module.ToolAnnotations = _ToolAnnotations
            mcp_module.types = types_module
            with self.subTest(error=str(error)), \
                    patch.dict(sys.modules, {"mcp": mcp_module, "mcp.types": types_module}), \
                    patch("selected_routes.load_selected_manifest", side_effect=error):
                register_selected_routes(server, ".")
            self.assertEqual(list(SELECTED_ROUTE_NAMES), server.names[:len(SELECTED_ROUTE_NAMES)])
            self.assertNotIn("release_version", server.names)


if __name__ == "__main__":
    unittest.main()
