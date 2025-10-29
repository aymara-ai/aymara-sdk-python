from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `aymara_ai.resources` module.

    This is used so that we can lazily import `aymara_ai.resources` only when
    needed *and* so that users can just import `aymara_ai` and reference `aymara_ai.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("aymara_ai.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
