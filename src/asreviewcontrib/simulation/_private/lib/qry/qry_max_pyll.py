import hyperopt


def qry_max_pyll():
    return {
        "abbr": "qry-max",
        "params": {
            "n_instances": hyperopt.hp.choice("n_instances", range(1, 100, 1)),
        },
    }
