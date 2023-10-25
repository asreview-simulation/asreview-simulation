import hyperopt


def get_pyll_cls_svm():
    return {
        "abbr": "svm",
        "params": {
            "c": hyperopt.hp.lognormal("c", 0, 2),
            "class_weight": hyperopt.hp.lognormal("class_weight", 0, 1),
            "gamma": hyperopt.hp.choice("gamma", ["auto", "scale"]),
            "kernel": hyperopt.hp.choice(
                "kernel", ["linear", "rbf", "poly", "sigmoid"]
            ),
        },
    }
