from typing import Optional
from typing import TypedDict


class ParamsType(TypedDict):
    embedding: Optional[str]
    fill: str
    max_sequence_length: int
    num_words: int
    split_ta: bool
    truncating: str
    use_keywords: bool


def get_fex_embedding_lstm_params() -> ParamsType:
    return {
        "embedding": None,
        "fill": "loop",
        "max_sequence_length": 1000,
        "num_words": 20000,
        "split_ta": False,
        "truncating": "post",
        "use_keywords": False,
    }
