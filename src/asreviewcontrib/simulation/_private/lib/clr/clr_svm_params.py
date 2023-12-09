from typing import TypedDict


class ParamsType(TypedDict):
    c: float
    class_weight: float
    gamma: str
    kernel: str


def get_clr_svm_params() -> ParamsType:
    return {
        "c": 15.4,
        "class_weight": 0.249,
        "gamma": "auto",
        "kernel": "linear",
    }
