from typing import TypedDict


class ParamsType(TypedDict):
    at_pct: int


def get_ofn_wss_params() -> ParamsType:
    return {
        "at_pct": 95,
    }
