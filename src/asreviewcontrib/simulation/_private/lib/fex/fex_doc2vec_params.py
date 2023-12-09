from typing import TypedDict


class ParamsType(TypedDict):
    dbow_words: bool
    dm: str
    dm_concat: bool
    epochs: int
    min_count: int
    split_ta: bool
    use_keywords: bool
    vector_size: int
    window: int


def get_fex_doc2vec_params() -> ParamsType:
    return {
        "dbow_words": False,
        "dm": "both",
        "dm_concat": False,
        "epochs": 33,
        "min_count": 1,
        "split_ta": False,
        "use_keywords": False,
        "vector_size": 40,
        "window": 7,
    }
