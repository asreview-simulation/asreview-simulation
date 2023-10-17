import hyperopt


def get_pyll_cls_nb():
    return {
        "nb": {
            "alpha": hyperopt.hp.lognormal("alpha", 0, 1),
        }
    }
