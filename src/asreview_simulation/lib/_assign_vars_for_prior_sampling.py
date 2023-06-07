def assign_vars_for_prior_sampling(obj):
    prior_indices = list()
    n_prior_included = 1
    n_prior_excluded = 1
    init_seed = None
    if obj.sampler.abbr == "handpicked":
        prior_indices = obj.sampler.params["ids"]
    elif obj.sampler.abbr == "random":
        n_prior_included = obj.sampler.params["n_included"]
        n_prior_excluded = obj.sampler.params["n_excluded"]
        init_seed = obj.sampler.params["init_seed"]
    else:
        raise "Unexpected sampler model abbreviation."
    return prior_indices, n_prior_included, n_prior_excluded, init_seed
