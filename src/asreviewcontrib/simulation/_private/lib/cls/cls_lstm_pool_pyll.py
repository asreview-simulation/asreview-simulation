import hyperopt


def cls_lstm_pool_pyll():
    return {
        "abbr": "cls-lstm-pool",
        "params": {
            "batch_size": hyperopt.hp.choice("batch_size", [32]),  # TODO
            "class_weight": hyperopt.hp.choice("class_weight", [30.0]),  # TODO
            "dropout": hyperopt.hp.choice("dropout", [0.4]),  # TODO
            "epochs": hyperopt.hp.choice("epochs", [35]),  # TODO
            "forward": hyperopt.hp.choice("forward", [True, False]),
            "learn_rate": hyperopt.hp.choice("learn_rate", [1.0]),  # TODO
            "lstm_out_width": hyperopt.hp.choice("lstm_out_width", [20]),  # TODO
            "lstm_pool_size": hyperopt.hp.choice("lstm_pool_size", [128]),  # TODO
            "optimizer": hyperopt.hp.choice("optimizer", ["sgd", "rmsprop", "adagrad", "adam", "nadam"]),
            "shuffle": hyperopt.hp.choice("shuffle", [True, False]),
        },
    }
