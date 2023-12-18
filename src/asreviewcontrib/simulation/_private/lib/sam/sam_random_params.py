from typing import Any
from typing import Dict


def get_sam_random_params() -> Dict[str, Any]:
    return {
        "n_excluded": 1,
        "n_included": 1,
        "seed": None,
    }
