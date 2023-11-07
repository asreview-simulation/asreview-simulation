from asreview.data import ASReviewData
from asreview.review.simulate import ReviewSimulate
from asreview_simulation._private.remove_abstraction import remove_abstraction
from asreview_simulation._private.model_configs import ModelConfigs


def run(models: ModelConfigs, project, as_data: ASReviewData, write_interval: int = None, seed: int = None):

    # prep
    kwargs = remove_abstraction(models, as_data, seed)
    reviewer = ReviewSimulate(as_data, project=project, **kwargs, write_interval=write_interval)

    # run
    project.update_review(status="review")  # (has side effects on disk)
    reviewer.review()
    project.mark_review_finished()  # (has side effects on disk)

