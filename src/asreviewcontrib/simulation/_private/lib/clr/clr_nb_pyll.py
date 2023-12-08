import hyperopt


def clr_nb_pyll():
    return {
        "abbr": "clr-nb",
        "params": {
            "alpha": hyperopt.hp.lognormal("alpha", 0, 1),
        },
    }
