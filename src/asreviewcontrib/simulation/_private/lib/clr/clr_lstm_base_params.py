from typing import Any
from typing import Dict


def get_clr_lstm_base_params() -> Dict[str, Any]:
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
