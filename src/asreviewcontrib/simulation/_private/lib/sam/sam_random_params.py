from typing import Optional
from typing import TypedDict


class ParamsType(TypedDict):
    init_seed: Optional[int]
    n_excluded: int
    n_included: int


def get_sam_random_params() -> ParamsType:
    return {
        "init_seed": None,
        "n_excluded": 1,
        "n_included": 1,
    }
