from typing import TypedDict


class ParamsType(TypedDict):
    batch_size: int
    class_weight: float
    dense_width: int
    dropout: float
    epochs: int
    forward: bool
    optimizer: str
    learn_rate: float
    lstm_out_width: int
    shuffle: bool


def get_clr_lstm_base_params() -> ParamsType:
    return {
        "batch_size": 32,
        "class_weight": 30.0,
        "dense_width": 128,
        "dropout": 0.4,
        "epochs": 35,
        "forward": False,
        "optimizer": "rmsprop",
        "learn_rate": 1.0,
        "lstm_out_width": 20,
        "shuffle": False,
    }
