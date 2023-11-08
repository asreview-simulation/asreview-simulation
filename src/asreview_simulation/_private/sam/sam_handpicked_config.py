from asreview_simulation._private.lib.model_config import ModelConfig


def get_sam_handpicked_config():
    abbr = "sam-handpicked"
    params = {
        "records": None,
        "rows": None,
    }
    return ModelConfig(abbr=abbr, params=params)
