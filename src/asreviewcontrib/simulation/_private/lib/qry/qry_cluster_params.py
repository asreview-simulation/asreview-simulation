from typing import TypedDict


class ParamsType(TypedDict):
    cluster_size: int
    n_instances: int
    update_interval: int


def get_qry_cluster_params() -> ParamsType:
    return {
        "cluster_size": 350,
        "n_instances": 1,
        "update_interval": 200,
    }
