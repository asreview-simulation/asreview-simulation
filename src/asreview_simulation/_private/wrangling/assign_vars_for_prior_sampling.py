from asreview.compat import convert_id_to_idx


def assign_vars_for_prior_sampling(obj, as_data):
    if obj.sampler.abbr == "handpicked":
        prior_rows = obj.sampler.params.get("rows", None)
        prior_records = obj.sampler.params.get("records", None)
        n_prior_included = 1
        n_prior_excluded = 1
        init_seed = None
        if prior_records is not None:
            prior_indices = convert_id_to_idx(as_data, prior_records)
        elif prior_rows is not None:
            prior_indices = prior_rows
        else:
            raise ValueError("prior_records and prior_rows should not both be not None.")
    elif obj.sampler.abbr == "random":
        prior_indices = list()
        n_prior_included = obj.sampler.params["n_included"]
        n_prior_excluded = obj.sampler.params["n_excluded"]
        init_seed = obj.sampler.params["init_seed"]
    else:
        raise ValueError("Unexpected sampler model abbreviation.")
    return prior_indices, n_prior_included, n_prior_excluded, init_seed
