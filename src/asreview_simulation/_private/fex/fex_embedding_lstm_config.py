from asreview_simulation._private.lib.model_config import ModelConfig


def get_fex_embedding_lstm_config():
    abbr = "fex-embedding-lstm"
    params = {
        "embedding": None,
        "loop_sequence": 1,
        "max_sequence_length": 1000,
        "num_words": 20000,
        "padding": "post",
        "split_ta": False,
        "truncating": "post",
        "use_keywords": False,
    }
    return ModelConfig(abbr=abbr, params=params)
