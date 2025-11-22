# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .agent_instructions import AgentInstructions

__all__ = ["WorkflowInstructions"]


class WorkflowInstructions(TypedDict, total=False):
    instructions: Required[Iterable[AgentInstructions]]
    """List of agent instructions for the workflow. Must contain at least one agent."""
