import hyperopt


def sam_random_pyll():
    return {
        "abbr": "sam-random",
        "params": {
            "init_seed": hyperopt.hp.choice("init_seed", [None]),  # TODO
            "n_excluded": hyperopt.hp.choice("n_excluded", [1]),  # TODO
            "n_included": hyperopt.hp.choice("n_included", [1]),  # TODO
        },
    }
