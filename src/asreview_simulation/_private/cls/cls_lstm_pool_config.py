from asreview_simulation._private.lib.model_config import ModelConfig


def get_cls_lstm_pool_config():
    abbr = "cls-lstm-pool"
    params = {
        "batch_size": 32,
        "class_weight": 30.0,
        "dropout": 0.4,
        "epochs": 35,
        "forward": False,
        "learn_rate": 1.0,
        "lstm_out_width": 20,
        "lstm_pool_size": 128,
        "optimizer": "rmsprop",
        "shuffle": False,
    }
    return ModelConfig(abbr=abbr, params=params)
