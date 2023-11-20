from typing import Optional
from asreview.data import ASReviewData
from asreview.project import ASReviewProject
from asreview.review.simulate import ReviewSimulate
from asreviewcontrib.simulation._private.lib.all_model_config import AllModelConfig
from asreviewcontrib.simulation._private.lib.calc_ofn_score import calc_ofn_score
from asreviewcontrib.simulation._private.lib.unwrapping.get_review_simulate_kwargs import get_review_simulate_kwargs


def run(
    models: AllModelConfig,
    project: ASReviewProject,
    as_data: ASReviewData,
    write_interval: int = None,
    seed: int = None,
) -> Optional[float]:
    # prep
    kwargs = get_review_simulate_kwargs(models, as_data, seed)
    reviewer = ReviewSimulate(as_data, project=project, **kwargs, write_interval=write_interval)

    # run
    project.update_review(status="review")  # (has side effects on disk)
    reviewer.review()
    project.mark_review_finished()  # (has side effects on disk)

    return calc_ofn_score(models.ofn, project.project_path)
