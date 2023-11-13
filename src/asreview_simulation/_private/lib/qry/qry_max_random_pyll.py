import hyperopt


def qry_max_random_pyll():
    return {
        "abbr": "qry-max-random",
        "params": {
            "fraction_max": hyperopt.hp.choice("fraction_max", [0.95]),          # TODO
            "n_instances": hyperopt.hp.choice("n_instances", range(1, 100, 1))
        },
    }
