# type: ignore
import math
from typing import Dict, List, Union, Optional

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter

from aymara_ai.types.evals import EvalRunResult


def eval_pass_stats(
    eval_runs: Union[EvalRunResult, List[EvalRunResult]],
) -> pd.DataFrame:
    """
    Create a DataFrame of pass rates and pass totals from one or more score runs.

    :param eval_runs: One or a list of test score runs to graph.
    :type eval_runs: Union[EvalRunResponse, List[EvalRunResponse]]
    :return: DataFrame of pass rates per test score run.
    :rtype: pd.DataFrame
    """
    if not isinstance(eval_runs, list):
        eval_runs = [eval_runs]

    data = [
        (
            run.name or run.evaluation.name if run.evaluation else "",
            run.pass_rate,
            min(run.pass_rate or 0, 0) * min(run.num_responses_scored or 0, 0),
        )
        for run in eval_runs
    ]

    return pd.DataFrame(
        data=data,
        columns=["name", "pass_rate", "pass_total"],
        index=pd.Index([run.eval_run_uuid for run in eval_runs], name="eval_run_uuid"),
    )


def _plot_pass_stats(
    names: pd.Series,
    pass_stats: pd.Series,
    title: Optional[str],
    xlabel: Optional[str],
    ylabel: Optional[str],
    xtick_rot: Optional[float],
    xtick_labels_dict: Optional[Dict[str, str]],
    yaxis_is_percent: bool,
    ylim_min: Optional[float],
    ylim_max: Optional[float],
    **kwargs,
) -> None:
    """Helper function to plot pass statistics."""
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots()
    ax.bar(names, pass_stats, **kwargs)

    # Title
    ax.set_title(title)

    # x-axis
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(ax.get_xticklabels(), rotation=xtick_rot, ha="right")
    ax.set_xlabel(xlabel, fontweight="bold")
    if xtick_labels_dict:
        xtick_labels = [label.get_text() for label in ax.get_xticklabels()]
        new_labels = [xtick_labels_dict.get(label, label) for label in xtick_labels]
        ax.set_xticklabels(new_labels)

    # y-axis
    ax.set_ylabel(ylabel, fontweight="bold")
    ax.set_ylim(
        bottom=ylim_min or max(0, math.floor((min(pass_stats) - 0.001) * 10) / 10),
        top=ylim_max or min(1, ax.get_ylim()[1]),
    )

    if yaxis_is_percent:

        def to_percent(y, _):
            return f"{y * 100:.0f}%"

        ax.yaxis.set_major_formatter(FuncFormatter(to_percent))

    plt.tight_layout()
    plt.show()


def graph_eval_stats(
    eval_runs: Union[List[EvalRunResult], EvalRunResult],
    title: Optional[str] = None,
    ylim_min: Optional[float] = None,
    ylim_max: Optional[float] = None,
    yaxis_is_percent: Optional[bool] = True,
    ylabel: Optional[str] = "Responses Passed",
    xaxis_is_eval_run_uuids: Optional[bool] = False,
    xlabel: Optional[str] = None,
    xtick_rot: Optional[float] = 30.0,
    xtick_labels_dict: Optional[Dict[str, str]] = None,
    **kwargs,
) -> None:
    """
    Draw a bar graph of pass rates from one or more score runs.

    :param eval_runs: One or a list of eval runs to graph.
    :type eval_runs: Union[List[EvalRunResult], EvalRunResult]
    :param title: Graph title.
    :type title: str, optional
    :param ylim_min: y-axis lower limit, defaults to rounding down to the nearest ten.
    :type ylim_min: float, optional
    :param ylim_max: y-axis upper limit, defaults to matplotlib's preference but is capped at 100.
    :type ylim_max: float, optional
    :param yaxis_is_percent: Whether to show the pass rate as a percent (instead of the total number of prompts passed), defaults to True.
    :type yaxis_is_percent: bool, optional
    :param ylabel: Label of the y-axis, defaults to 'Responses Passed'.
    :type ylabel: str
    :param xaxis_is_eval_run_uuids: Whether the x-axis represents tests (True) or score runs (False), defaults to True.
    :type xaxis_is_test: bool, optional
    :param xlabel: Label of the x-axis, defaults to 'Eval Runs' if xaxis_is_eval_run_uuids=True and 'Evals' otherwise.
    :type xlabel: str
    :param xtick_rot: rotation of the x-axis tick labels, defaults to 30.
    :type xtick_rot: float
    :param xtick_labels_dict: Maps eval names (keys) to x-axis tick labels (values).
    :type xtick_labels_dict: dict, optional
    :param kwargs: Options to pass to matplotlib.pyplot.bar.
    """

    if not isinstance(eval_runs, list):
        eval_runs = [eval_runs]

    for eval_run in eval_runs:
        if not eval_run.status == "finished":
            raise ValueError(f"Eval run {eval_run.eval_run_uuid} has no Responses")

    df_pass_stats = eval_pass_stats(eval_runs)

    if not xlabel:
        xlabel = "Eval Runs" if xaxis_is_eval_run_uuids else "Evals"

    _plot_pass_stats(
        names=df_pass_stats["eval_run_uuid" if xaxis_is_eval_run_uuids else "name"],
        pass_stats=df_pass_stats["pass_rate" if yaxis_is_percent else "pass_total"],
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        xtick_rot=xtick_rot,
        xtick_labels_dict=xtick_labels_dict,
        yaxis_is_percent=yaxis_is_percent,
        ylim_min=ylim_min,
        ylim_max=ylim_max,
        **kwargs,
    )
