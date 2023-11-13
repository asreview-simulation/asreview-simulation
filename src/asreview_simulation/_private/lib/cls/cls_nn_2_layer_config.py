from asreview_simulation._private.lib.model_config import ModelConfig


def get_cls_nn_2_layer_config():
    abbr = "cls-nn-2-layer"
    params = {
        "batch_size": 32,
        "class_weight": 30.0,
        "dense_width": 128,
        "epochs": 35,
        "learn_rate": 1.0,
        "optimizer": "rmsprop",
        "regularization": 0.01,
        "shuffle": False,
    }
    return ModelConfig(abbr=abbr, params=params)
