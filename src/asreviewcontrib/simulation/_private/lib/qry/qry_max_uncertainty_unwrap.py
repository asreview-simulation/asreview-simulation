from asreview.models.query.mixed import MixedQuery


def instantiate_unwrapped_qry_max_uncertainty(params, random_state):
    mapped_params = {
        "strategy_1": "max",
        "strategy_2": "uncertainty",
        "mix_ratio": params["fraction_max"],
    }
    return MixedQuery(**mapped_params, random_state=random_state)