from typing import TypedDict


class ParamsType(TypedDict):
    ngram_max: int
    split_ta: bool
    stop_words: str
    use_keywords: bool


def get_fex_tfidf_params() -> ParamsType:
    return {
        "ngram_max": 1,
        "split_ta": False,
        "stop_words": "english",
        "use_keywords": False,
    }
