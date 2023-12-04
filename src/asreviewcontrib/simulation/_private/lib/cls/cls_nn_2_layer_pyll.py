import hyperopt


def cls_nn_2_layer_pyll():
    return {
        "abbr": "cls-nn-2-layer",
        "params": {
            "batch_size": hyperopt.hp.choice("batch_size", [32]),  # TODO
            "class_weight": hyperopt.hp.lognormal("class_weight", 3, 1),
            "dense_width": hyperopt.hp.quniform("dense_width", 2, 100, 1),
            "epochs": hyperopt.hp.quniform("epochs", 20, 60, 1),
            "learn_rate": hyperopt.hp.lognormal("learn_rate", 0, 1),
            "optimizer": hyperopt.hp.choice("optimizer", ["sgd", "rmsprop", "adagrad", "adam", "nadam"]),
            "regularization": hyperopt.hp.lognormal("regularization", -4, 2),
            "shuffle": hyperopt.hp.choice("shuffle", [True, False]),
        },
    }
