from asreview.models.feature_extraction.embedding_lstm import EmbeddingLSTM


def instantiate_unwrapped_fex_embedding_lstm(params, _random_state):
    mapped_params = {
        "loop_sequence":  {"loop": 1, "append-zeros": 0, "prepend-zeros": 0}[params["fill"]],
        "max_sequence_length": params["max_sequence_length"],
        "num_words": params["num_words"],
        "padding": {"loop": "post", "append-zeros": "post", "prepend-zeros": "pre"}[params["fill"]],
        "split_ta": {False: 0, True: 1}[params["split_ta"]],
        "truncating": params["truncating"],
        "use_keywords": {False: 0, True: 1}[params["use_keywords"]],
    }
    return EmbeddingLSTM(**mapped_params)
