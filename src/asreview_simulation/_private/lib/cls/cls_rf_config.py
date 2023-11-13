from asreview_simulation._private.lib.model_config import ModelConfig


def get_cls_rf_config():
    abbr = "cls-rf"
    params = {
        "class_weight": 1.0,
        "max_features": 10,
        "n_estimators": 100,
    }
    return ModelConfig(abbr=abbr, params=params)
