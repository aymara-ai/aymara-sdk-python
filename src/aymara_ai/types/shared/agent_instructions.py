# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .tool_dict import ToolDict
from .tool_array import ToolArray
from .tool_string import ToolString

__all__ = ["AgentInstructions", "Tools"]

Tools: TypeAlias = Annotated[Union[ToolArray, ToolDict, ToolString], PropertyInfo(discriminator="type")]


class AgentInstructions(BaseModel):
    system_prompt: str

    agent_name: Optional[str] = None

    tools: Optional[Tools] = None
    """Instructions for the agent, can be a string or a list/dict of tools."""
