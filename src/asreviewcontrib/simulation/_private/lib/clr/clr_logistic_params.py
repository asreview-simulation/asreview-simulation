from typing import Any
from typing import Dict


def get_clr_logistic_params() -> Dict[str, Any]:
    return {
        "c": 1.0,
        "class_weight": 1.0,
    }
