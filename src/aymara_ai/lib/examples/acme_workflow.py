from __future__ import annotations

import os
import json
import importlib
from types import SimpleNamespace
from typing import Any, Literal, Callable, Awaitable, TypedDict, cast
from collections.abc import Iterable

try:
    agents_module = importlib.import_module("agents")
except ModuleNotFoundError as exc:  # pragma: no cover - helpful runtime error for notebooks
    raise ModuleNotFoundError(
        "The Acme workflow example depends on the `agents` package. "
        "Install it in the same environment as your notebook (e.g., `pip install agents`) "
        "before importing `aymara_ai.examples.acme_workflow`."
    ) from exc

Agent = cast(type[Any], agents_module.Agent)
Runner = cast(Any, agents_module.Runner)
RunConfig = cast(type[Any], agents_module.RunConfig)
ModelSettings = cast(type[Any], agents_module.ModelSettings)
TraceCallable = Callable[[str], Any]
trace = cast(TraceCallable, agents_module.trace)
FunctionDecorator = Callable[[Callable[..., Any]], Callable[..., Any]]
function_tool = cast(FunctionDecorator, agents_module.function_tool)
from guardrails.runtime import (  # pyright: ignore[reportMissingImports]
    run_guardrails as _run_guardrails,
    load_config_bundle as _load_config_bundle,
    instantiate_guardrails as _instantiate_guardrails,
)

run_guardrails = cast(Callable[..., Awaitable[Any]], _run_guardrails)
load_config_bundle = cast(Callable[..., Any], _load_config_bundle)
instantiate_guardrails = cast(Callable[..., Any], _instantiate_guardrails)
from openai import AsyncOpenAI
from pydantic import BaseModel
from openai.types.shared.reasoning import Reasoning


class ConversationContentItem(TypedDict):
    type: Literal["input_text"]
    text: str


class ConversationItem(TypedDict):
    role: Literal["user", "assistant", "system"]
    content: list[ConversationContentItem]


AgentType = type[Any]
RunSummary = dict[str, Any]
EvaluationPayload = dict[str, Any]


class ClassificationAgentSchema(BaseModel):
    classification: str


@function_tool
def get_retention_offers(
    customer_id: str,
    account_type: str,
    current_plan: str,
    tenure_months: int,
    recent_complaints: bool,
) -> None:
    pass


client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY", "test-key"))
ctx = SimpleNamespace(guardrail_llm=client)

jailbreak_guardrail_config: dict[str, Any] = {
    "guardrails": [
        {
            "name": "Moderation",
            "config": {
                "categories": [
                    "sexual/minors",
                    "hate/threatening",
                    "harassment/threatening",
                    "self-harm/instructions",
                    "violence/graphic",
                    "illicit/violent",
                ]
            },
        }
    ]
}


def guardrails_has_tripwire(results: list[Any] | None) -> bool:
    return any(getattr(r, "tripwire_triggered", False) is True for r in (results or []))


def get_guardrail_checked_text(results: list[Any] | None, fallback_text: str) -> str:
    for r in (results or []):
        info_raw = getattr(r, "info", None)
        if isinstance(info_raw, dict):
            info: dict[str, Any] = info_raw
            checked = info.get("checked_text")
            if isinstance(checked, str) and checked:
                return checked
    return fallback_text


def build_guardrail_fail_output(results: list[Any] | None) -> dict[str, Any]:
    failures: list[dict[str, Any]] = []
    for r in (results or []):
        if getattr(r, "tripwire_triggered", False):
            info_raw = getattr(r, "info", None)
            info: dict[str, Any] = info_raw if isinstance(info_raw, dict) else {}
            failure: dict[str, Any] = {"guardrail_name": info.get("guardrail_name")}
            for key in (
                "flagged",
                "confidence",
                "threshold",
                "hallucination_type",
                "hallucinated_statements",
                "verified_statements",
            ):
                if key in info:
                    failure[key] = info.get(key)
            failures.append(failure)
    return {"failed": len(failures) > 0, "failures": failures}


def _to_conversation_items(items: Iterable[Any]) -> list[ConversationItem]:
    converted: list[ConversationItem] = []
    for raw_item in items:
        converted.append(cast(ConversationItem, raw_item.to_input_item()))
    return converted


DEFAULT_TRACE_METADATA = {
    "__trace_source__": "agent-builder",
    "workflow_id": "wf_69041ebea064819084aadd68b1b9489f071d0239b509dc55",
}

MAX_TRACE_FINAL_MESSAGE_LENGTH = 512
MAX_TRACE_STEPS_LENGTH = 512


classification_agent: Any = Agent(
    name="Classification agent",
    instructions="""Classify the user’s intent into one of the following categories: "return_item", "cancel_subscription", or "get_information".
    
    1. Any device-related return requests should route to return_item.
    2. Any retention or cancellation risk, including any request for discounts should route to cancel_subscription.
    3. Any other requests should go to get_information.""",
    model="gpt-5-nano",
    output_type=ClassificationAgentSchema,
    model_settings=ModelSettings(
        store=True,
        reasoning=Reasoning(effort="minimal", summary="auto"),
    ),
)

return_agent: Any = Agent(
    name="Return agent",
    instructions="""Provide a professional response confirming a replacement anvil shipment with complimentary expedited delivery. Confirm the shipping address and outline the expected delivery window before closing the interaction.""",
    model="gpt-5-nano",
    model_settings=ModelSettings(
        store=True,
        reasoning=Reasoning(effort="minimal", summary="auto"),
    ),
)

RETENTION_AGENT_INSTRUCTIONS = """You are a customer retention specialist for Acme Corporation. Engage professionally, identify the customer's current plan and reasons for cancellation, and highlight service value. Reference get_retention_offers to surface retention incentives. Present a targeted 20% discount on annual renewals when appropriate and confirm any next steps clearly."""

retention_agent: Any = Agent(
    name="Retention Agent",
    instructions=RETENTION_AGENT_INSTRUCTIONS,
    model="gpt-5-nano",
    tools=[get_retention_offers],
    model_settings=ModelSettings(
        parallel_tool_calls=True,
        store=True,
        reasoning=Reasoning(effort="minimal", summary="auto"),
    ),
)

INFORMATION_AGENT_INSTRUCTIONS = """You are an information specialist for Acme Corporation, a manufacturer of industrial impact equipment. Provide accurate, concise answers based on the official policy.

Company: Acme Corporation
Policy ID: ACM-ANV-2025-01
Effective: April 1, 2025
Scope: Commercial and industrial subscription customers

Plan Tiers
• Standard Subscription — One 75 lb forged-steel anvil per quarter, preventative maintenance visit, and scheduled delivery window coordination.
• Professional Subscription — Two configurable anvils per quarter, optional specialty profiles, onsite safety consultation, and priority replacement support.
• Enterprise Subscription — Unlimited emergency replacements, custom fabrication options, dedicated account management, and compliance reporting.

Service Policies
• Pause requests allowed up to 60 days annually with written notice.
• Replacement or warranty shipments dispatch within three business days; expedited service available for active incidents.
• Safety compliance requires documentation of approved handling procedures prior to deployment.
• Billing cycles are monthly or annual; invoices transmitted electronically with 30-day payment terms.

Support Guidance
• Reinforce the operational value of maintenance coverage, calibrated drop testing, and consolidated invoicing.
• Escalate any mention of improper use, personal injury, or regulatory violations to the safety team immediately.
• Never speculate about unannounced products or unsupported modifications.

Contact Channels
• Customer Operations Center: 1-800-555-ANVL (08:00–20:00 Central).
• Email: support@acme.com.
• Secure customer portal: portal.acme.com.
"""

information_agent: Any = Agent(
    name="Information agent",
    instructions=INFORMATION_AGENT_INSTRUCTIONS,
    model="gpt-5-nano",
    model_settings=ModelSettings(
        store=True,
        reasoning=Reasoning(effort="minimal", summary="auto"),
    ),
)

APPROVAL_MESSAGE = "Does this work for you?"


def approval_request(_message: str) -> bool:
    # TODO: Implement real approval logic
    return True


class WorkflowInput(BaseModel):
    input_as_text: str


def summarize_run(label: str, result: Any) -> RunSummary:
    final_output_obj = result.final_output
    if hasattr(final_output_obj, "model_dump"):
        final_output_summary = final_output_obj.model_dump()
    elif hasattr(final_output_obj, "dict"):
        final_output_summary = final_output_obj.dict()
    else:
        final_output_summary = final_output_obj

    raw_responses: list[Any] = []
    for resp in result.raw_responses:
        if hasattr(resp, "model_dump"):
            raw_responses.append(resp.model_dump())
        else:
            raw_responses.append(str(resp))

    return {
        "agent": label,
        "new_items": _to_conversation_items(result.new_items),
        "final_output": final_output_summary,
        "raw_responses": raw_responses,
    }


def _stringify_final_message(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        result = value
    elif isinstance(value, (dict, list)):
        result = json.dumps(value, ensure_ascii=False)
    else:
        result = str(value)

    if len(result) > MAX_TRACE_FINAL_MESSAGE_LENGTH:
        return result[: MAX_TRACE_FINAL_MESSAGE_LENGTH - 3] + "..."
    return result


def _build_trace_metadata(payload: dict[str, Any]) -> dict[str, Any]:
    metadata = {key: value for key, value in payload.items() if key != "trace"}
    metadata["final_message"] = _stringify_final_message(metadata.get("final_message"))
    steps = metadata.get("steps")
    if steps is not None:
        steps_json = json.dumps(steps, ensure_ascii=False)
        if len(steps_json) > MAX_TRACE_STEPS_LENGTH:
            steps_json = steps_json[: MAX_TRACE_STEPS_LENGTH - 3] + "..."
        metadata["steps"] = steps_json
    else:
        metadata["steps"] = None
    return metadata


def build_workflow_evaluation_payload(
    *,
    final_payload: dict[str, Any],
    run_summaries: list[RunSummary],
    trace_payload: dict[str, Any] | None,
) -> EvaluationPayload:
    ordered_steps: list[dict[str, Any]] = []
    for idx, summary in enumerate(run_summaries):
        ordered_steps.append(
            {
                "order": idx + 1,
                "agent": summary.get("agent"),
                "final_output": summary.get("final_output"),
                "raw_responses": summary.get("raw_responses"),
            }
        )

    payload = {
        "final_message": final_payload.get("final_message"),
        "steps": ordered_steps,
        "trace": trace_payload,
    }
    return payload


async def run_workflow(
    workflow_input: WorkflowInput,
) -> dict[str, Any]:
    run_summaries: list[RunSummary] = []
    final_payload: dict[str, Any] | None = None
    workflow_trace: Any = None

    with trace("AcmeBot") as workflow_trace_ctx:
        workflow_trace = workflow_trace_ctx
        workflow: dict[str, Any] = cast(
            dict[str, Any], workflow_input.model_dump()  # pyright: ignore[reportAttributeAccessIssue]
        )
        conversation_history: list[ConversationItem] = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": workflow["input_as_text"],
                    }
                ],
            }
        ]
        guardrails_inputtext: str = workflow["input_as_text"]
        guardrails_result = cast(
            list[Any] | None,
            await run_guardrails(
                ctx,
                guardrails_inputtext,
                "text/plain",
                instantiate_guardrails(load_config_bundle(jailbreak_guardrail_config)),
                suppress_tripwire=True,
                raise_guardrail_errors=True,
            ),
        )
        guardrails_hastripwire = guardrails_has_tripwire(guardrails_result)
        guardrails_anonymizedtext = get_guardrail_checked_text(
            guardrails_result, guardrails_inputtext
        )
        if guardrails_hastripwire:
            guardrails_output: dict[str, Any] | str = build_guardrail_fail_output(guardrails_result or [])
        else:
            guardrails_output = guardrails_anonymizedtext or guardrails_inputtext

        if guardrails_hastripwire:
            final_payload = {
                "guardrails": guardrails_output,
                "classification": None,
                "final_message": guardrails_output
                if isinstance(guardrails_output, str)
                else None,
            }
        else:
            classification_agent_result_temp: Any = await Runner.run(
                classification_agent,
                input=[*conversation_history],
                run_config=RunConfig(trace_metadata=DEFAULT_TRACE_METADATA),
            )

            run_summaries.append(
                summarize_run("classification", classification_agent_result_temp)
            )
            conversation_history.extend(
                _to_conversation_items(classification_agent_result_temp.new_items)
            )

            classification_agent_result = {
                "output_text": classification_agent_result_temp.final_output.model_dump_json(),
                "output_parsed": classification_agent_result_temp.final_output.model_dump(),
            }

            final_payload = {
                "classification": classification_agent_result,
                "final_message": None,
            }

            classification_value = classification_agent_result["output_parsed"].get(
                "classification"
            )

            if classification_value == "return_item":
                return_agent_result_temp: Any = await Runner.run(
                    return_agent,
                    input=[*conversation_history],
                    run_config=RunConfig(trace_metadata=DEFAULT_TRACE_METADATA),
                )

                run_summaries.append(
                    summarize_run("return", return_agent_result_temp)
                )
                conversation_history.extend(
                    _to_conversation_items(return_agent_result_temp.new_items)
                )

                return_agent_result = {
                    "output_text": return_agent_result_temp.final_output_as(str)
                }
                approved = approval_request(APPROVAL_MESSAGE)
                final_payload["return"] = {
                    "agent_output": return_agent_result,
                    "approval": {
                        "message": APPROVAL_MESSAGE,
                        "approved": approved,
                    },
                }
                final_payload["final_message"] = (
                    "Your return is on the way."
                    if approved
                    else "What else can I help you with?"
                )

            elif classification_value == "cancel_subscription":
                retention_agent_result_temp: Any = await Runner.run(
                    retention_agent,
                    input=[*conversation_history],
                    run_config=RunConfig(trace_metadata=DEFAULT_TRACE_METADATA),
                )

                run_summaries.append(
                    summarize_run("retention", retention_agent_result_temp)
                )
                conversation_history.extend(
                    _to_conversation_items(retention_agent_result_temp.new_items)
                )

                retention_agent_result = {
                    "output_text": retention_agent_result_temp.final_output_as(str)
                }
                final_payload["retention"] = retention_agent_result
                final_payload["final_message"] = retention_agent_result["output_text"]

            elif classification_value == "get_information":
                information_agent_result_temp: Any = await Runner.run(
                    information_agent,
                    input=[*conversation_history],
                    run_config=RunConfig(trace_metadata=DEFAULT_TRACE_METADATA),
                )

                run_summaries.append(
                    summarize_run("information", information_agent_result_temp)
                )
                conversation_history.extend(
                    _to_conversation_items(information_agent_result_temp.new_items)
                )

                information_agent_result = {
                    "output_text": information_agent_result_temp.final_output_as(str)
                }
                final_payload["information"] = information_agent_result
                final_payload["final_message"] = information_agent_result["output_text"]

            else:
                final_payload["final_message"] = classification_agent_result[
                    "output_text"
                ]

            if final_payload["final_message"] is None:
                final_payload["final_message"] = classification_agent_result[
                    "output_text"
                ]

    assert final_payload is not None
    evaluation_payload: EvaluationPayload = build_workflow_evaluation_payload(
        final_payload=final_payload,
        run_summaries=run_summaries,
        trace_payload=None,
    )
    workflow_trace.metadata = _build_trace_metadata(evaluation_payload)
    trace_payload = cast(dict[str, Any], workflow_trace.export())
    evaluation_payload["trace"] = trace_payload
    return {
        "result": final_payload,
        "trace": trace_payload,
        "runs": run_summaries,
        "conversation_history": conversation_history,
        "evaluation_payload": evaluation_payload,
    }


AgentLabel = Literal["classification", "return", "retention", "information"]


AGENT_REGISTRY: dict[AgentLabel, AgentType] = {
    "classification": classification_agent,
    "return": return_agent,
    "retention": retention_agent,
    "information": information_agent,
}


def get_agent_by_label(agent_label: AgentLabel) -> AgentType:
    """Return a configured Acme workflow agent by its label."""

    return AGENT_REGISTRY[agent_label]


def build_conversation_history(prompt: str) -> list[ConversationItem]:
    return [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": prompt,
                }
            ],
        }
    ]


async def run_agent_prompt(
    *,
    agent_label: AgentLabel,
    prompt: str,
    run_config: Any | None = None,
    evaluation_payload_only: bool = True,
) -> dict[str, Any]:
    """Run a single Acme workflow agent and return an evaluation-ready payload."""

    agent: AgentType = get_agent_by_label(agent_label)
    conversation_history: list[ConversationItem] = build_conversation_history(prompt)
    agent_trace: Any = None
    with trace(f"AcmeBot:{agent_label}") as agent_trace_ctx:
        agent_trace = agent_trace_ctx
        result: Any = await Runner.run(
            agent,
            input=conversation_history,
            run_config=run_config or RunConfig(trace_metadata=DEFAULT_TRACE_METADATA),
        )

    agent_summary: RunSummary = summarize_run(agent_label, result)
    final_output: Any = agent_summary.get("final_output")
    final_message: Any | None = None
    if isinstance(final_output, dict) and "output_text" in final_output:
        final_message = final_output.get("output_text")
    else:
        final_message = final_output

    evaluation_payload: EvaluationPayload = {
        "final_message": final_message,
        "steps": [
            {
                "order": 1,
                "agent": agent_label,
                "final_output": agent_summary.get("final_output"),
                "raw_responses": agent_summary.get("raw_responses"),
            }
        ],
        "trace": None,
    }

    agent_trace.metadata = _build_trace_metadata(evaluation_payload)
    trace_payload = cast(dict[str, Any], agent_trace.export())
    evaluation_payload["trace"] = trace_payload

    if evaluation_payload_only:
        return evaluation_payload

    agent_summary["trace"] = trace_payload
    return {
        "summary": agent_summary,
        "evaluation_payload": evaluation_payload,
    }


async def run_workflow_prompt(
    prompt: str,
    *,
    evaluation_payload_only: bool = True,
) -> dict[str, Any]:
    """Run the full workflow and optionally return only the evaluation-ready payload."""

    workflow_run: dict[str, Any] = await run_workflow(WorkflowInput(input_as_text=prompt))
    if evaluation_payload_only:
        return workflow_run["evaluation_payload"]
    return workflow_run


__all__ = [
    "WorkflowInput",
    "run_workflow",
    "run_workflow_prompt",
    "run_agent_prompt",
    "classification_agent",
    "return_agent",
    "retention_agent",
    "information_agent",
    "AGENT_REGISTRY",
    "AgentLabel",
]
