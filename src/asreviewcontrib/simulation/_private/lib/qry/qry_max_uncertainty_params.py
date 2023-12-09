from typing import TypedDict


class ParamsType(TypedDict):
    fraction_max: float
    n_instances: int


def get_qry_max_uncertainty_params() -> ParamsType:
    return {
        "fraction_max": 0.95,
        "n_instances": 1,
    }
