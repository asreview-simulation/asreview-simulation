from typing import TypedDict


class ParamsType(TypedDict):
    batch_size: int
    class_weight: float
    dense_width: int
    epochs: int
    learn_rate: float
    optimizer: str
    regularization: float
    shuffle: bool


def get_clr_nn_2_layer_params() -> ParamsType:
    return {
        "batch_size": 32,
        "class_weight": 30.0,
        "dense_width": 128,
        "epochs": 35,
        "learn_rate": 1.0,
        "optimizer": "rmsprop",
        "regularization": 0.01,
        "shuffle": False,
    }
