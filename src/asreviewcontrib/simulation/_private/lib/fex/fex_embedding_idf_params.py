from typing import Any
from typing import Dict


def get_fex_embedding_idf_params() -> Dict[str, Any]:
    return {
        "embedding": None,
        "split_ta": False,
        "use_keywords": False,
    }
