from typing import Any
from typing import Dict


def get_sam_random_params() -> Dict[str, Any]:
    return {
        "init_seed": None,
        "n_excluded": 1,
        "n_included": 1,
    }
