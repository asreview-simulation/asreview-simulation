import hyperopt


def fex_doc2vec_pyll():
    return {
        "abbr": "fex-doc2vec",
        "params": {
            "dbow_words": hyperopt.hp.choice("dbow_words", [True, False]),
            "dm": hyperopt.hp.choice("dm_concat", ["dbow", "dm", "both"]),
            "dm_concat": hyperopt.hp.choice("dm_concat", [True, False]),
            "epochs": hyperopt.hp.choice("epochs", range(20, 51, 1)),
            "min_count": hyperopt.hp.choice("min_count", [1, 2]),
            "split_ta": hyperopt.hp.choice("split_ta", [True, False]),
            "use_keywords": hyperopt.hp.choice("use_keywords", [True, False]),
            "vector_size": hyperopt.hp.choice("vector_size", range(32, 129, 8)),
            "window": hyperopt.hp.choice("window", range(5, 10, 1)),
        },
    }
