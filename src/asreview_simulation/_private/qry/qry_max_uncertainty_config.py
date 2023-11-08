from asreview_simulation._private.lib.model_config import ModelConfig


def get_qry_max_uncertainty_config():
    abbr = "qry-max-uncertainty"
    params = {
        "fraction_max": 0.95,
        "n_instances": 1,
    }
    return ModelConfig(abbr=abbr, params=params)
