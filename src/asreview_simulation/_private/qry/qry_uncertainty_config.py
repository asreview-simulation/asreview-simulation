from asreview_simulation._private.lib.model_config import ModelConfig


def get_qry_uncertainty_config():
    abbr = "qry-uncertainty"
    params = {
        "n_instances": 1,
    }
    return ModelConfig(abbr=abbr, params=params)
