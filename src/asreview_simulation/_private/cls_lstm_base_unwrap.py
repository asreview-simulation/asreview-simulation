from asreview.models.classifiers.lstm_base import LSTMBaseClassifier


def cls_lstm_base_unwrap(params, _random_state):
    mapped_params = {
        "backwards": not params["forward"],
        "batch_size": params["batch_size"],
        "class_weight": params["class_weight"],
        "dense_width": params["dense_width"],
        "dropout": params["dropout"],
        "epochs": params["epochs"],
        "optimizer": params["optimizer"],
        "learn_rate": params["learn_rate"],
        "lstm_out_width": params["lstm_out_width"],
        "shuffle": params["shuffle"],
    }
    return LSTMBaseClassifier(**mapped_params)
