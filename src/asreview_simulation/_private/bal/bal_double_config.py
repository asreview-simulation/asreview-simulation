from asreview_simulation._private.lib.model_config import ModelConfig


def get_bal_double_config():
    abbr = "bal-double"
    params = {
        "a": 2.155,
        "alpha": 0.94,
        "b": 0.789,
        "beta": 1.0
    }
    return ModelConfig(abbr=abbr, params=params)
