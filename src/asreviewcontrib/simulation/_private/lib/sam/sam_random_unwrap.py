from typing import List
from typing import Optional
from typing import Tuple
from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.config import Config


TSamResult = Tuple[List[int], int, int, Optional[int]]


def sam_random_unwrap(config: Config, _as_data: ASReviewData) -> TSamResult:
    prior_indices: List[int] = list()
    n_prior_included = config.sam.params["n_included"]
    n_prior_excluded = config.sam.params["n_excluded"]
    seed = config.sam.params["seed"]
    return prior_indices, n_prior_included, n_prior_excluded, seed
