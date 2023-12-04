def get_fex_embedding_lstm_params():
    return {
        "embedding": None,
        "fill": "loop",
        "max_sequence_length": 1000,
        "num_words": 20000,
        "split_ta": False,
        "truncating": "post",
        "use_keywords": False,
    }
