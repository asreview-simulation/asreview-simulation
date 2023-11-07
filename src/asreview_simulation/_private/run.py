from asreview.data import ASReviewData
from asreview.review.simulate import ReviewSimulate
from numpy.random import RandomState
from asreview_simulation._private.unwrapping.remove_abstraction import remove_abstraction
from asreview_simulation._private.models import Models


def run(models: Models, project, as_data: ASReviewData, write_interval: int, random_state: RandomState):
    review_simulate_kwargs = remove_abstraction(models, as_data, random_state)
    reviewer = ReviewSimulate(as_data, project=project, **review_simulate_kwargs, write_interval=write_interval)

    # run
    project.update_review(status="review")  # (has side effects on disk)
    reviewer.review()
    project.mark_review_finished()  # (has side effects on disk)

