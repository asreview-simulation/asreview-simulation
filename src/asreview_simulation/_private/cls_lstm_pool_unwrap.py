from asreview.models.classifiers.lstm_pool import LSTMPoolClassifier


def cls_lstm_pool_unwrap(params, _random_state):
    mapped_params = {
        "backwards": not params["forward"],
        "batch_size": params["batch_size"],
        "class_weight": params["class_weight"],
        "dropout": params["dropout"],
        "epochs": params["epochs"],
        "learn_rate": params["learn_rate"],
        "lstm_out_width": params["lstm_out_width"],
        "lstm_pool_size": params["lstm_pool_size"],
        "optimizer": params["optimizer"],
        "shuffle": params["shuffle"],
    }
    return LSTMPoolClassifier(**mapped_params)
