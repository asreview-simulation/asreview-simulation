from typing import TypedDict


class ParamsType(TypedDict):
    c: float
    class_weight: float


def get_clr_logistic_params() -> ParamsType:
    return {
        "c": 1.0,
        "class_weight": 1.0,
    }
