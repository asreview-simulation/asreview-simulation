from asreview_simulation._private.lib.model_config import ModelConfig


def get_fex_doc2vec_config():
    abbr = "fex-doc2vec"
    params = {
        "dbow_words": False,
        "dm": "both",
        "dm_concat": False,
        "epochs": 33,
        "min_count": 1,
        "split_ta": False,
        "use_keywords": False,
        "vector_size": 40,
        "window": 7,
    }
    return ModelConfig(abbr=abbr, params=params)
