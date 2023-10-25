import hyperopt


def get_pyll_cls_nn_2_layer():
    return {
        "abbr": "nn-2-layer",
        "params": {
            "dense_width": hyperopt.hp.quniform("dense_width", 2, 100, 1),
            "epochs": hyperopt.hp.quniform("epochs", 20, 60, 1),
            "optimizer": hyperopt.hp.choice(
                "optimizer", ["sgd", "rmsprop", "adagrad", "adam", "nadam"]
            ),
            "learn_rate": hyperopt.hp.lognormal("learn_rate", 0, 1),
            "class_weight": hyperopt.hp.lognormal("class_weight", 3, 1),
            "regularization": hyperopt.hp.lognormal("regularization", -4, 2),
        },
    }
