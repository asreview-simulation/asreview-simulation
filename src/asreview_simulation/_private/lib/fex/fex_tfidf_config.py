from asreview_simulation._private.lib.model_config import ModelConfig


def get_fex_tfidf_config():
    abbr = "fex-tfidf"
    params = {
        "ngram_max": 1,
        "split_ta": False,
        "stop_words": "english",
        "use_keywords": False,
    }
    return ModelConfig(abbr=abbr, params=params)
