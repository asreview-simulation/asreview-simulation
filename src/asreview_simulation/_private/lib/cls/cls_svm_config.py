from asreview_simulation._private.lib.model_config import ModelConfig


def get_cls_svm_config():
    abbr = "cls-svm"
    params = {
        "c": 15.4,
        "class_weight": 0.249,
        "gamma": "auto",
        "kernel": "linear",
    }
    return ModelConfig(abbr=abbr, params=params)
