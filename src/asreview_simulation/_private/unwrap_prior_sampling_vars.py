from asreview.compat import convert_id_to_idx
from asreview.data import ASReviewData
from asreview_simulation._private.model_configs import ModelConfigs


def unwrap_prior_sampling_vars(models: ModelConfigs, as_data: ASReviewData):
    if models.sampler.abbr == "sam-handpicked":
        prior_rows = models.sampler.params.get("rows", None)
        prior_records = models.sampler.params.get("records", None)
        n_prior_included = 1
        n_prior_excluded = 1
        init_seed = None
        if prior_records is not None:
            prior_indices = convert_id_to_idx(as_data, prior_records)
        elif prior_rows is not None:
            prior_indices = prior_rows
        else:
            raise ValueError("prior_records and prior_rows should not both be not None.")
    elif models.sampler.abbr == "sam-random":
        prior_indices = list()
        n_prior_included = models.sampler.params["n_included"]
        n_prior_excluded = models.sampler.params["n_excluded"]
        init_seed = models.sampler.params["init_seed"]
    else:
        raise ValueError("Unexpected sampler model abbreviation.")
    return prior_indices, n_prior_included, n_prior_excluded, init_seed
