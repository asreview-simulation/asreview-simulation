import hyperopt


def bal_undersample_pyll():
    return {
        "abbr": "undersample",
        "params": {
            "ratio": hyperopt.hp.lognormal("ratio", 0, 1),
        },
    }
