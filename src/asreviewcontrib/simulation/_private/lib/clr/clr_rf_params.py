from typing import Any
from typing import Dict


def get_clr_rf_params() -> Dict[str, Any]:
    return {
        "class_weight": 1.0,
        "max_features": 10,
        "n_estimators": 100,
    }
