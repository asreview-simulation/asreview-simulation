from typing import TypedDict


class ParamsType(TypedDict):
    ratio: float


def get_bal_undersample_params() -> ParamsType:
    return {
        "ratio": 1.0,
    }
