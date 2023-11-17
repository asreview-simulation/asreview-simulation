from typing import Optional
from asreview.compat import convert_id_to_idx
from asreview.data import ASReviewData
from asreview_simulation._private.lib.all_model_config import AllModelConfig


def unwrap_prior_sampling_vars(
    models: AllModelConfig, as_data: ASReviewData
) -> (Optional[int], Optional[int], Optional[int], Optional[int]):
    if models.sam.abbr == "sam-handpicked":
        prior_rows = models.sam.params.get("rows", None)
        prior_records = models.sam.params.get("records", None)
        n_prior_included = 1
        n_prior_excluded = 1
        init_seed = None
        if prior_records is not None:
            prior_indices = convert_id_to_idx(as_data, prior_records)
        elif prior_rows is not None:
            prior_indices = prior_rows
        else:
            raise ValueError("prior_records and prior_rows should not both be not None.")
    elif models.sam.abbr == "sam-random":
        prior_indices = list()
        n_prior_included = models.sam.params["n_included"]
        n_prior_excluded = models.sam.params["n_excluded"]
        init_seed = models.sam.params["init_seed"]
    else:
        raise ValueError("Unexpected sampler model abbreviation.")
    return prior_indices, n_prior_included, n_prior_excluded, init_seed
