import hyperopt


def sam_random_pyll():
    return {
        "abbr": "sam-random",
        "params": {
            "n_excluded": hyperopt.hp.choice("n_excluded", [1]),  # TODO
            "n_included": hyperopt.hp.choice("n_included", [1]),  # TODO
            "seed": hyperopt.hp.choice("seed", [None]),  # TODO
        },
    }
