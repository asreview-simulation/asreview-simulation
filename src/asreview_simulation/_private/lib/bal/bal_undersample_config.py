from asreview_simulation._private.lib.model_config import ModelConfig


def get_bal_undersample_config():
    abbr = "bal-undersample"
    params = {
        "ratio": 1.0,
    }
    return ModelConfig(abbr=abbr, params=params)
