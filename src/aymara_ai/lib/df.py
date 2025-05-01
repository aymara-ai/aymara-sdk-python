from typing import Any, Dict, List, Union

import pandas as pd  # type: ignore

from aymara_ai._models import BaseModel
from aymara_ai.types.eval import Eval
from aymara_ai.types.eval_prompt import EvalPrompt
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
    rows = (
        [
            {
                "eval_run_uuid": eval_run.eval_run_uuid,
                "eval_uuid": eval_run.eval_uuid,
                "name": eval_run.evaluation.name if eval_run.evaluation else "",
                "prompt_uuid": response.prompt_uuid,
                "response_uuid": response.response_uuid,
                "is_passed": response.is_passed,
                "prompt_content": prompts[i].content if prompts else "",
                "prompt_category": prompts[i].category if prompts else "",
                "response_content": response.content,
                "ai_refused": response.ai_refused,
                "exclude_from_scoring": response.exclude_from_scoring,
                "explanation": response.explanation,
                "confidence": response.confidence,
            }
            for i, response in enumerate(responses)
        ]
        if responses
        else []
    )

    return pd.DataFrame(rows)


def to_df(results: Union[List[Union[BaseModel, Dict[str, Any]]], Dict[str, Any], BaseModel]) -> pd.DataFrame:
    """Convert a BaseModel or Dict to a DataFrame."""
    if isinstance(results, dict) or isinstance(results, BaseModel):
        results = [results]
    rows = [r.to_dict() if isinstance(r, BaseModel) else r for r in results]

    return pd.DataFrame(rows)
