from asreview_simulation._private.lib.model_config import ModelConfig


def get_fex_sbert_config():
    abbr = "fex-sbert"
    params = {
        "split_ta": False,
        "transformer_model": "all-mpnet-base-v2",
        "use_keywords": False,
    }
    return ModelConfig(abbr=abbr, params=params)
