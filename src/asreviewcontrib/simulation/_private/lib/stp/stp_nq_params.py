from typing import Optional
from typing import TypedDict


class ParamsType(TypedDict):
    n_queries: Optional[int]


def get_stp_nq_params():
    return {
        "n_queries": None,
    }
