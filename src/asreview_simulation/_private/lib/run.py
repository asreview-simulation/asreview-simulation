from asreview.data import ASReviewData
from asreview.project import ASReviewProject
from asreview.review.simulate import ReviewSimulate
from asreview_simulation._private.lib.config import CompleteConfig
from asreview_simulation._private.lib.unwrapping.get_review_simulate_kwargs import get_review_simulate_kwargs


def run(
    models: CompleteConfig,
    project: ASReviewProject,
    as_data: ASReviewData,
    write_interval: int = None,
    seed: int = None,
) -> None:
    # prep
    kwargs = get_review_simulate_kwargs(models, as_data, seed)
    reviewer = ReviewSimulate(as_data, project=project, **kwargs, write_interval=write_interval)

    # run
    project.update_review(status="review")  # (has side effects on disk)
    reviewer.review()
    project.mark_review_finished()  # (has side effects on disk)
