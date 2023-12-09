from typing import TypedDict


class ParamsType(TypedDict):
    n_instances: int


def get_qry_uncertainty_params() -> ParamsType:
    return {
        "n_instances": 1,
    }
