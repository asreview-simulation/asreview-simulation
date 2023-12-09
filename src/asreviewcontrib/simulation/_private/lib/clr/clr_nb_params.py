from typing import TypedDict


class ParamsType(TypedDict):
    alpha: float


def get_clr_nb_params() -> ParamsType:
    return {
        "alpha": 3.822,
    }
