from typing import Any
from typing import Dict


def get_fex_tfidf_params() -> Dict[str, Any]:
    return {
        "ngram_max": 1,
        "split_ta": False,
        "stop_words": "english",
        "use_keywords": False,
    }
