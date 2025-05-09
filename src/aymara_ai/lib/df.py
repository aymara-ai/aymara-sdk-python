import re
from typing import Any, Dict, List, Union

import pandas as pd  # type: ignore

from aymara_ai._models import BaseModel
from aymara_ai.types.eval import Eval
from aymara_ai._base_client import BasePage
from aymara_ai.types.eval_prompt import EvalPrompt
from aymara_ai.types.eval_suite_report import EvalSuiteReport
from aymara_ai.types.evals.eval_run_result import EvalRunResult
from aymara_ai.types.evals.scored_response import ScoredResponse


def to_prompts_df(eval: Eval, prompts: List[EvalPrompt]) -> pd.DataFrame:
    """Create a prompts DataFrame."""

    if not prompts:
        return pd.DataFrame()

    rows = [
        {
            "eval_uuid": eval.eval_uuid,
            "eval_name": eval.name,
            "prompt_uuid": prompt.prompt_uuid,
            "prompt_content": prompt.content,
            "prompt_category": prompt.category,
        }
        for prompt in prompts
    ]

    return pd.DataFrame(rows)


def to_scores_df(eval_run: EvalRunResult, prompts: List[EvalPrompt], responses: List[ScoredResponse]) -> pd.DataFrame:
    """Create a scores DataFrame."""
    prompt_map: Dict[str, EvalPrompt] = {prompt.prompt_uuid: prompt for prompt in prompts} if prompts else {}
    rows = (
        [
            {
                "eval_run_uuid": eval_run.eval_run_uuid,
                "eval_uuid": eval_run.eval_uuid,
                "name": eval_run.evaluation.name if eval_run.evaluation else "",
                "prompt_uuid": response.prompt_uuid,
                "response_uuid": response.response_uuid,
                "is_passed": response.is_passed,
                "prompt_content": (prompt.content if (prompt := prompt_map.get(response.prompt_uuid)) else ""),
                "prompt_category": (prompt.category if (prompt := prompt_map.get(response.prompt_uuid)) else ""),
                "response_content": response.content,
                "ai_refused": response.ai_refused,
                "exclude_from_scoring": response.exclude_from_scoring,
                "explanation": response.explanation,
                "confidence": response.confidence,
            }
            for response in responses
        ]
        if responses
        else []
    )

    return pd.DataFrame(rows)


def to_df(results: Union[List[Union[BaseModel, Dict[str, Any]]], Dict[str, Any], BaseModel]) -> pd.DataFrame:
    """Convert a BaseModel or Dict to a DataFrame."""
    if isinstance(results, BasePage):
        return to_df(results.items)  # type: ignore
    if isinstance(results, dict) or isinstance(results, BaseModel):
        results = [results]
    rows = [r.to_dict() if isinstance(r, BaseModel) else r for r in results]

    return pd.DataFrame(rows)


def to_reports_df(suite_report: EvalSuiteReport) -> pd.DataFrame:
    """Create report dataframe by prompt category."""

    rows = []
    for report in suite_report.eval_run_reports:
        if report.eval_run.evaluation.eval_type == "accuracy" if report.eval_run.evaluation else False:
            # Extract sections using XML tags
            passing_sections = re.findall(r"<(\w+)>(.*?)</\1>", report.passing_responses_summary, re.DOTALL)
            failing_sections = (
                re.findall(r"<(\w+)>(.*?)</\1>", report.failing_responses_summary, re.DOTALL)
                if report.failing_responses_summary
                else []
            )
            advice_sections = re.findall(r"<(\w+)>(.*?)</\1>", report.improvement_advice, re.DOTALL)

            # Create a mapping of question types to their content
            passing_by_type = {tag: content.strip() for tag, content in passing_sections}
            failing_by_type = {tag: content.strip() for tag, content in failing_sections}
            advice_by_type = {tag: content.strip() for tag, content in advice_sections}

            # Get ordered unique question types while preserving order
            categories = []
            for tag, _ in passing_sections + failing_sections:
                if tag not in categories:
                    categories.append(tag)  # type: ignore

            # Create a row for each question type
            for q_type in categories:  # type: ignore
                rows.append(  # type: ignore
                    {
                        "eval_name": report.eval_run.evaluation.name
                        if report.eval_run.evaluation
                        else report.eval_run.name,
                        "prompt_category": q_type,
                        "passing_responses_summary": passing_by_type.get(q_type, ""),
                        "failing_responses_summary": failing_by_type.get(q_type, ""),
                        "improvement_advice": advice_by_type.get(q_type, ""),
                    }
                )
        else:
            # Handle non-accuracy tests as before
            rows.append(  # type: ignore
                {
                    "eval_name": report.eval_run.evaluation.name
                    if report.eval_run.evaluation
                    else report.eval_run.name,
                    "passing_responses_summary": report.passing_responses_summary,
                    "failing_responses_summary": report.failing_responses_summary,
                    "improvement_advice": report.improvement_advice,
                }
            )

    # Add overall summary if available
    if suite_report.overall_passing_responses_summary or suite_report.overall_failing_responses_summary:
        rows.append(  # type: ignore
            {
                "eval_name": "Overall",
                "passing_responses_summary": suite_report.overall_passing_responses_summary,
                "failing_responses_summary": suite_report.overall_failing_responses_summary,
                "improvement_advice": suite_report.overall_improvement_advice,
            }
        )

    return pd.DataFrame(rows)
