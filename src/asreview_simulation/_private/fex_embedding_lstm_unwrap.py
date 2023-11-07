from asreview.models.feature_extraction.embedding_lstm import EmbeddingLSTM


def fex_embedding_lstm_unwrap(params, _random_state):
    mapped_params = {
        "loop_sequence": params["loop_sequence"],
        "max_sequence_length": params["max_sequence_length"],
        "num_words": params["num_words"],
        "padding": params["padding"],
        "split_ta": {False: 0, True: 1}[params["split_ta"]],
        "truncating": params["truncating"],
        "use_keywords": {False: 0, True: 1}[params["use_keywords"]],
    }
    return EmbeddingLSTM(**mapped_params)
