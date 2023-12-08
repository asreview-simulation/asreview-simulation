import hyperopt


def clr_lstm_base_pyll():
    return {
        "abbr": "clr-lstm-base",
        "params": {
            "batch_size": hyperopt.hp.choice("batch_size", [32]),  # TODO
            "class_weight": hyperopt.hp.choice("class_weight", [30.0]),  # TODO
            "dense_width": hyperopt.hp.choice("dense_width", [128]),  # TODO
            "dropout": hyperopt.hp.choice("dropout", [0.4]),  # TODO
            "epochs": hyperopt.hp.choice("epochs", [35]),  # TODO
            "forward": hyperopt.hp.choice("forward", [True, False]),
            "optimizer": hyperopt.hp.choice("optimizer", ["sgd", "rmsprop", "adagrad", "adam", "nadam"]),
            "learn_rate": hyperopt.hp.choice("learn_rate", [1.0]),  # TODO
            "lstm_out_width": hyperopt.hp.choice("lstm_out_width", [20]),  # TODO
            "shuffle": hyperopt.hp.choice("shuffle", [True, False]),
        },
    }
