import hyperopt


def get_pyll_cls_nb():
    return {
        "abbr": "nb",
        "params": {
            "alpha": hyperopt.hp.lognormal("alpha", 0, 1),
        }
    }
