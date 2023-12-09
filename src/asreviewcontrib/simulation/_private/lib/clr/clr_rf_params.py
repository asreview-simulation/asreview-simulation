from typing import TypedDict


class ParamsType(TypedDict):
    class_weight: float
    max_features: int
    n_estimators: int


def get_clr_rf_params() -> ParamsType:
    return {
        "class_weight": 1.0,
        "max_features": 10,
        "n_estimators": 100,
    }
