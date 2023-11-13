import hyperopt


def qry_max_uncertainty_pyll():
    return {
        "abbr": "qry-max-uncertainty",
        "params": {
            "fraction_max": hyperopt.hp.choice("fraction_max", [0.95]),  # TODO
            "n_instances": hyperopt.hp.choice("n_instances", range(1, 100, 1)),
        },
    }
