import hyperopt


def qry_random_pyll():
    return {
        "abbr": "qry-random",
        "params": {
            "n_instances": hyperopt.hp.choice("n_instances", range(1, 100, 1))
        },
    }
