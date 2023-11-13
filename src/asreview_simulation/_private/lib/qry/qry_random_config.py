from asreview_simulation._private.lib.model_config import ModelConfig


def get_qry_random_config():
    abbr = "qry-random"
    params = {
        "n_instances": 1,
    }
    return ModelConfig(abbr=abbr, params=params)
