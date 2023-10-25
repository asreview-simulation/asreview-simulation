import hyperopt


def get_pyll_fex_doc2vec():
    return {
        "abbr": "doc2vec",
        "params": {
            "dbow_words": hyperopt.hp.randint("dbow_words", 2),
            "dm_concat": hyperopt.hp.randint("dm_concat", 2),
            "dm": hyperopt.hp.randint("dm", 3),
            "epochs": hyperopt.hp.quniform("epochs", 20, 50, 1),
            "min_count": hyperopt.hp.quniform("min_count", 0.5, 2.499999, 1),
            "split_ta": hyperopt.hp.randint("split_ta", 2),
            "use_keywords": hyperopt.hp.randint("use_keywords", 2),
            "vector_size": hyperopt.hp.quniform("vector_size", 31.5, 127.499999, 8),
            "window": hyperopt.hp.quniform("window", 4.5, 9.4999999, 1),
        },
    }
