import hyperopt


def get_pyll_bal_undersample():
    return {
        "undersample": {
            "ratio": hyperopt.hp.lognormal("ratio", 0, 1),
        }
    }
