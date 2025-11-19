# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .agent_instructions import AgentInstructions

__all__ = ["WorkflowInstructions"]


class WorkflowInstructions(BaseModel):
    instructions: List[AgentInstructions]
    """List of agent instructions for the workflow. Must contain at least one agent."""
