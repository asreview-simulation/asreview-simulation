from typing import List
from typing import Optional
from typing import Tuple
from asreview.compat import convert_id_to_idx
from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.config import Config


TSamResult = Tuple[List[int], int, int, Optional[int]]


def sam_handpicked_unwrap(config: Config, as_data: ASReviewData) -> TSamResult:
    prior_rows = config.sam.params.get("rows", None)
    prior_records = config.sam.params.get("records", None)
    n_prior_included = 1
    n_prior_excluded = 1
    init_seed = None
    if prior_records is not None:
        prior_indices = convert_id_to_idx(as_data, prior_records)
    elif prior_rows is not None:
        prior_indices = prior_rows
    else:
        raise ValueError("prior_records and prior_rows should not both be not None.")
    return prior_indices, n_prior_included, n_prior_excluded, init_seed
