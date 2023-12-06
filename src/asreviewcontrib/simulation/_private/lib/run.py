import os
import shutil
from typing import Optional
from asreview.data import ASReviewData
from asreview.project import ASReviewProject
from asreview.review.simulate import ReviewSimulate
from asreviewcontrib.simulation._private.lib.calc_ofn_score import calc_ofn_score
from asreviewcontrib.simulation._private.lib.config import Config
from asreviewcontrib.simulation._private.lib.unwrapping.get_review_simulate_kwargs import get_review_simulate_kwargs


def run(
    config: Config,
    project: ASReviewProject,
    as_data: ASReviewData,
    write_interval: int = None,
    seed: int = None,
    no_zip: bool = False,
) -> Optional[float]:
    # prep
    kwargs = get_review_simulate_kwargs(config, as_data, seed)
    reviewer = ReviewSimulate(as_data, project=project, **kwargs, write_interval=write_interval)

    # run
    project.update_review(status="review")  # (has side effects on disk)
    reviewer.review()
    project.mark_review_finished()  # (has side effects on disk)

    # wrap-up
    p = project.project_path
    if no_zip:
        # rename the .asreview.tmp directory to just .asreview
        os.rename(p, p.with_suffix(""))
    else:
        # zip the results
        project.export(p.with_suffix(""))
        shutil.rmtree(p)

    return calc_ofn_score(config.ofn, p.with_suffix(""))
