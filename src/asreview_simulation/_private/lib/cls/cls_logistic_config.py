from asreview_simulation._private.lib.model_config import ModelConfig


def get_cls_logistic_config():
    abbr = "cls-logistic"
    params = {
        "c": 1.0,
        "class_weight": 1.0,
    }
    return ModelConfig(abbr=abbr, params=params)
