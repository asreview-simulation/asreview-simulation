from typing import Any
from typing import Dict


def get_fex_embedding_lstm_params() -> Dict[str, Any]:
    return {
        "embedding": None,
        "fill": "loop",
        "max_sequence_length": 1000,
        "num_words": 20000,
        "split_ta": False,
        "truncating": "post",
        "use_keywords": False,
    }
