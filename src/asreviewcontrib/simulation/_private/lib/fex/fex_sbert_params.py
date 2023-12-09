from typing import Any
from typing import Dict


def get_fex_sbert_params() -> Dict[str, Any]:
    return {
        "split_ta": False,
        "transformer_model": "all-mpnet-base-v2",
        "use_keywords": False,
    }
