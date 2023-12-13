from asreview.models.query.mixed import MixedQuery


def instantiate_unwrapped_qry_max_random(params, random_state):
    mapped_params = {
        "strategy_1": "max",
        "strategy_2": "random",
        "mix_ratio": params["fraction_max"],
    }

    # asreview's query model does not expect n_instances as part
    # of the params dict but as a separate variable
    assert "n_instances" in params.keys()
    assert "n_instances" not in mapped_params.keys()

    return MixedQuery(**mapped_params, random_state=random_state)
