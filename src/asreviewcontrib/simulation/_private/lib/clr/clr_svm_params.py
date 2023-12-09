from typing import Any
from typing import Dict


def get_clr_svm_params() -> Dict[str, Any]:
    return {
        "c": 15.4,
        "class_weight": 0.249,
        "gamma": "auto",
        "kernel": "linear",
    }
