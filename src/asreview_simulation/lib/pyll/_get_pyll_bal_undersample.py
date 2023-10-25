import hyperopt


def get_pyll_bal_undersample():
    return {
        "abbr": "undersample",
        "params": {
            "ratio": hyperopt.hp.lognormal("ratio", 0, 1),
        }
    }