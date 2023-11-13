from asreview_simulation._private.lib.model_config import ModelConfig


def get_sam_random_config():
    abbr = "sam-random"
    params = {
        "init_seed": None,
        "n_excluded": 1,
        "n_included": 1,
    }
    return ModelConfig(abbr=abbr, params=params)
