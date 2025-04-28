# type: ignore
from typing import Dict, List, Tuple, Optional

from aymara_ai.types.eval import Eval
from aymara_ai.types.eval_prompt import EvalPrompt
from aymara_ai.types.eval_response_param import EvalResponseParam
from aymara_ai.types.evals.eval_run_result import EvalRunResult


def display_image_responses(
    evals: List[Eval],
    eval_prompts: Dict[str, List[EvalPrompt]],
    eval_responses: Dict[str, List[EvalResponseParam]],
    eval_runs: Optional[List[EvalRunResult]] = None,
    n_images_per_eval: Optional[int] = 5,
    figsize: Optional[Tuple[int, int]] = None,
) -> None:
    """
    Display a grid of image test answers with their test questions as captions.
    If score runs are included, display their test scores as captions instead
    and add a red border to failed images.

    :param tests: Tests corresponding to the test answers.
    :type tests: List of SafetyTestResponse objects.
    :param test_answers: Test answers.
    :type test_answers: Dictionary of test UUIDs to lists of ImageStudentAnswerInput objects.
    :param score_runs: Score runs corresponding to the test answers.
    :type score_runs: List of ScoreRunResponse objects, optional
    :param n_images_per_test: Number of images to display per test.
    :type n_images_per_test: int, optional
    :param figsize: Figure size. Defaults to (n_images_per_test * 3, n_tests * 2 * 4).
    :type figsize: integer tuple, optional
    """
    import textwrap

    import matplotlib.image as mpimg
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
            if caption.startswith("No image"):
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
                img = mpimg.imread(img_path)
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
    n_tests = len(eval_responses)
    total_rows = n_tests * 2
    fig = plt.figure(figsize=figsize or (n_images_per_eval * 3, total_rows * 4))
    gs = gridspec.GridSpec(total_rows, n_images_per_eval, figure=fig, height_ratios=[1, 20] * n_tests)
    fig.subplots_adjust(hspace=0.1, wspace=0.1)

    row = 0
    for eval_uuid, answers in eval_responses.items():
        test = next(t for t in evals if t.eval_uuid == eval_uuid)
        prompts = eval_prompts.get(eval_uuid, [])

        # Title row
        ax_title = fig.add_subplot(gs[row, :])
        ax_title.text(
            0.5,
            0,
            test.name,
            fontsize=16,
            fontweight="bold",
            ha="center",
            va="top",
        )
        ax_title.axis("off")
        row += 1

        # Image row
        images = [a["local_file_path"] for a in answers[:n_images_per_eval] if a.get("ai_refused", False) is False]
        if eval_runs is None:
            captions = [
                next(
                    refusal_caption
                    if a.get("ai_refused", False)
                    else exclusion_caption
                    if a.get("exclude_from_scoring", False)
                    else q.content
                    for q in prompts
                    if q.prompt_uuid == a["prompt_uuid"]
                )
                for a in answers[:n_images_per_eval]
            ]
        else:
            score_run = next(s for s in eval_runs if s.eval_run_uuid == eval_uuid)
            scores = [
                next(s for s in score_run.responses if s.prompt_uuid == a["prompt_uuid"])
                for a in answers[:n_images_per_eval]
            ]
            captions = [
                refusal_caption
                if s.ai_refused
                else exclusion_caption
                if s.exclude_from_scoring
                else f"{'Pass' if s.is_passed else 'Fail'} ({s.confidence:.1%} confidence): {s.explanation}"
                for s in scores
            ]

        axs = [fig.add_subplot(gs[row, col]) for col in range(len(images))]
        display_image_group(axs, images, captions)
        row += 1

    plt.tight_layout()
    plt.show()
