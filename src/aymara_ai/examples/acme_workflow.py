"""Re-export the Acme workflow from the legacy lib namespace for convenience."""

from aymara_ai.lib.examples.acme_workflow import (
    AGENT_REGISTRY,
    AgentLabel,
    WorkflowInput,
    return_agent,
    run_workflow,
    retention_agent,
    run_agent_prompt,
    information_agent,
    run_workflow_prompt,
    classification_agent,
)

__all__ = [
    "AGENT_REGISTRY",
    "AgentLabel",
    "WorkflowInput",
    "run_workflow",
    "run_workflow_prompt",
    "run_agent_prompt",
    "classification_agent",
    "return_agent",
    "retention_agent",
    "information_agent",
]
