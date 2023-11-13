from asreview_simulation._private.lib.model_config import ModelConfig


def get_fex_embedding_idf_config():
    abbr = "fex-embedding-idf"
    params = {
        "embedding": None,
        "split_ta": False,
        "use_keywords": False,
    }
    return ModelConfig(abbr=abbr, params=params)
