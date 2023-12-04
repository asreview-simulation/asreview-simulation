import hyperopt


def bal_undersample_pyll():
    return {
        "abbr": "bal-undersample",
        "params": {
            "ratio": hyperopt.hp.lognormal("ratio", 0, 1),
        },
    }
