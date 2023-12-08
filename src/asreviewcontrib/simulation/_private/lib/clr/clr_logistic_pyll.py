import hyperopt


def clr_logistic_pyll():
    return {
        "abbr": "clr-logistic",
        "params": {
            "c": hyperopt.hp.lognormal("c", 0, 1),
            "class_weight": hyperopt.hp.lognormal("class_weight", 0, 1),
        },
    }
