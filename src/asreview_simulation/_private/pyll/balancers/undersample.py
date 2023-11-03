import hyperopt


def bal_undersample():
    return {
        "abbr": "undersample",
        "params": {
            "ratio": hyperopt.hp.lognormal("ratio", 0, 1),
        },
    }
