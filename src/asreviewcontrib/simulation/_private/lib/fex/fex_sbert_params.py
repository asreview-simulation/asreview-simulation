from typing import TypedDict


class ParamsType(TypedDict):
    split_ta: bool
    transformer_model: str
    use_keywords: bool


def get_fex_sbert_params() -> ParamsType:
    return {
        "split_ta": False,
        "transformer_model": "all-mpnet-base-v2",
        "use_keywords": False,
    }
