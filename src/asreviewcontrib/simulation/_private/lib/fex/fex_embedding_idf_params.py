from typing import Optional
from typing import TypedDict


class ParamsType(TypedDict):
    embedding: Optional[str]
    split_ta: bool
    use_keywords: bool


def get_fex_embedding_idf_params() -> ParamsType:
    return {
        "embedding": None,
        "split_ta": False,
        "use_keywords": False,
    }
