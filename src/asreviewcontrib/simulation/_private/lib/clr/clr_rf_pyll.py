import hyperopt


def clr_rf_pyll():
    return {
        "abbr": "clr-rf",
        "params": {
            "class_weight": hyperopt.hp.choice("class_weight", [1.0]),  # TODO
            "max_features": hyperopt.hp.choice("max_features", [10]),  # TODO
            "n_estimators": hyperopt.hp.choice("n_estimators", [100]),  # TODO
        },
    }
