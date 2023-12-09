from typing import TypedDict


class ParamsType(TypedDict):
    a: float
    alpha: float
    b: float
    beta: float


def get_bal_double_params() -> ParamsType:
    return {
        "a": 2.155,
        "alpha": 0.94,
        "b": 0.789,
        "beta": 1.0,
    }
