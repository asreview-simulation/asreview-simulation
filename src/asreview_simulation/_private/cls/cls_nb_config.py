from asreview_simulation._private.lib.model_config import ModelConfig


def get_cls_nb_config():
    abbr = "cls-nb"
    params = {
        "alpha": 3.822
    }
    return ModelConfig(abbr=abbr, params=params)
