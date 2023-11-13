import hyperopt


def qry_uncertainty_pyll():
    return {
        "abbr": "qry-uncertainty",
        "params": {
            "n_instances": hyperopt.hp.choice("n_instances", range(1, 100, 1))
        },
    }
