# type: ignore
import urllib.request
from typing import Dict, List, Tuple, Optional

import PIL.Image

from aymara_ai.types.eval import Eval
from aymara_ai.types.eval_prompt import EvalPrompt
from aymara_ai.types.evals.eval_run_result import EvalRunResult
from aymara_ai.types.evals.scored_response import ScoredResponse


def display_image_responses(
    evals: List[Eval],
    eval_prompts: Dict[str, List[EvalPrompt]],
    eval_responses: Dict[str, List[ScoredResponse]],
    eval_runs: Optional[List[EvalRunResult]] = None,
    n_images_per_eval: Optional[int] = 5,
    figsize: Optional[Tuple[int, int]] = None,
) -> None:
    """
    Display a grid of image eval responses with their eval questions as captions.
    If eval runs are included, display their eval evals as captions instead
    and add a red border to failed images.

    :param evals: Evals corresponding to the eval responses.
    :type evals: List of Eval objects.
    :param eval_responses: Eval responses.
    :type eval_responses: Dictionary of eval UUIDs to lists of EvalResponseParam objects.
    :param eval_runs: Eval runs corresponding to the eval responses.
    :type eval_runs: List of EvalRunResponse objects, optional
    :param n_images_per_eval: Number of images to display per eval.
    :type n_images_per_eval: int, optional
    :param figsize: Figure size. Defaults to (n_images_per_eval * 3, n_evals * 2 * 4).
    :type figsize: integer tuple, optional
    """
    import textwrap

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import matplotlib.gridspec as gridspec

    refusal_caption = "No image: AI refused to generate."
    exclusion_caption = "No image: Response excluded from scoring."

    def display_image_group(axs, images, captions):
        max_lines = 5  # Maximum number of lines for captions
        wrap_width = 35  # Width for text wrapping

        def trim_caption(caption):
            wrapped = textwrap.wrap(caption, width=wrap_width)
            if len(wrapped) > max_lines:
                trimmed = wrapped[:max_lines]
                trimmed[-1] += "..."
            else:
                trimmed = wrapped
            return "\n".join(trimmed)

        for ax, img_path, caption in zip(axs, images, captions):
            trimmed_caption = trim_caption(caption)
            if caption.startswith("No image") or img_path is None:
                ax.text(
                    0.5,
                    0.5,
                    "",
                    fontsize=12,
                    color="gray",
                    ha="center",
                    va="center",
                    wrap=True,
                )
                ax.set_title(
                    trimmed_caption,
                    fontsize=10,
                    wrap=True,
                    loc="left",
                    pad=0,
                    y=0.75,
                )
                ax.axis("off")
            else:
                img = PIL.Image.open(urllib.request.urlopen(img_path))
                ax.imshow(img)
                ax.set_title(
                    trimmed_caption,
                    fontsize=10,
                    wrap=True,
                    loc="left",
                )
                ax.axis("off")

            if caption.startswith("Fail"):
                rect = patches.Rectangle(
                    (0, 0),
                    1,
                    1,
                    transform=ax.transAxes,
                    color="red",
                    linewidth=5,
                    fill=False,
                )
                ax.add_patch(rect)

    # Create the figure and gridspec layout
    n_evals = len(eval_responses)
    total_rows = n_evals * 2
    fig = plt.figure(figsize=figsize or (n_images_per_eval * 3, total_rows * 4))
    gs = gridspec.GridSpec(total_rows, n_images_per_eval, figure=fig, height_ratios=[1, 20] * n_evals)
    fig.subplots_adjust(hspace=0.1, wspace=0.1)

    row = 0
    for eval_uuid, responses in eval_responses.items():
        eval = next(t for t in evals if t.eval_uuid == eval_uuid)
        prompts = eval_prompts.get(eval_uuid, [])

        # Title row
        ax_title = fig.add_subplot(gs[row, :])
        ax_title.text(
            0.5,
            0,
            eval.name,
            fontsize=16,
            fontweight="bold",
            ha="center",
            va="top",
        )
        ax_title.axis("off")
        row += 1

        # Image row
        images = [a.content.remote_file_path if a.ai_refused is False else None for a in responses[:n_images_per_eval]]
        if eval_runs is None:
            captions = [
                next(
                    refusal_caption if a.ai_refused else exclusion_caption if a.exclude_from_scoring else q.content
                    for q in prompts
                    if q.prompt_uuid == a.prompt_uuid
                )
                for a in responses[:n_images_per_eval]
            ]
        else:
            eval_run = next(s for s in eval_runs if s.eval_uuid == eval_uuid)
            evals = [
                next(s for s in eval_run.responses if s.prompt_uuid == a.prompt_uuid)
                for a in responses[:n_images_per_eval]
            ]
            captions = [
                refusal_caption
                if s.ai_refused
                else exclusion_caption
                if s.exclude_from_scoring
                else f"{'Pass' if s.is_passed else 'Fail'} ({s.confidence:.1%} confidence): {s.explanation}"
                for s in responses[:n_images_per_eval]
            ]

        axs = [fig.add_subplot(gs[row, col]) for col in range(len(images))]
        display_image_group(axs, images, captions)
        row += 1

    plt.tight_layout()
    plt.show()
