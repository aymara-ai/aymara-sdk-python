# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .tool_dict import ToolDict
from .tool_array import ToolArray
from .tool_string import ToolString

__all__ = ["AgentInstructions", "Tools"]

Tools: TypeAlias = Union[ToolArray, ToolDict, ToolString]


class AgentInstructions(TypedDict, total=False):
    system_prompt: Required[str]

    agent_name: Optional[str]

    tools: Tools
    """Instructions for the agent, can be a string or a list/dict of tools."""
