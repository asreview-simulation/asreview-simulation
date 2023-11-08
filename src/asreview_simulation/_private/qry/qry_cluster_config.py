from asreview_simulation._private.lib.model_config import ModelConfig


def get_qry_cluster_config():
    abbr = "qry-cluster"
    params = {
        "cluster_size": 350,
        "n_instances": 1,
        "update_interval": 200,
    }
    return ModelConfig(abbr=abbr, params=params)
