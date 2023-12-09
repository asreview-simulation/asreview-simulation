from typing import Any
from typing import Dict


def get_fex_doc2vec_params() -> Dict[str, Any]:
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
