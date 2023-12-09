from typing import Any
from typing import Dict


def get_qry_cluster_params() -> Dict[str, Any]:
    return {
        "cluster_size": 350,
        "n_instances": 1,
        "update_interval": 200,
    }
