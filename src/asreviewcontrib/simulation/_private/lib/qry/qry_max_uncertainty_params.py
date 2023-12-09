from typing import Any
from typing import Dict


def get_qry_max_uncertainty_params() -> Dict[str, Any]:
    return {
        "fraction_max": 0.95,
        "n_instances": 1,
    }
