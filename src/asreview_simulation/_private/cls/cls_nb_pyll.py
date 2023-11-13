import hyperopt


def cls_nb_pyll():
    return {
        "abbr": "cls-nb",
        "params": {
            "alpha": hyperopt.hp.lognormal("alpha", 0, 1),
        },
    }
