import hyperopt


def fex_embedding_lstm_pyll():
    return {
        "abbr": "fex-embedding-lstm",
        "params": {
            "embedding": hyperopt.hp.choice("embeddding", [None]),  # TODO
            "fill": hyperopt.hp.choice("fill", ["loop", "append-zeros", "prepend-zeros"]),
            "max_sequence_length": hyperopt.hp.choice("max_sequence_length", [1000]),  # TODO
            "num_words": hyperopt.hp.choice("num_words", [20000]),  # TODO
            "split_ta": hyperopt.hp.choice("split_ta", [True, False]),
            "truncating": hyperopt.hp.choice("truncating", ["pre", "post"]),
            "use_keywords": hyperopt.hp.choice("use_keywords", [True, False]),
        },
    }
