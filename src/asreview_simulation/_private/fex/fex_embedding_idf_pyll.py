import hyperopt


def fex_embedding_idf_pyll():
    return {
        "abbr": "fex-embedding-idf",
        "params": {
            "embedding": hyperopt.hp.choice("embedding", [None]),               # TODO
            "split_ta": hyperopt.hp.choice("split_ta", [True, False]),
            "use_keywords": hyperopt.hp.choice("use_keywords", [True, False]),
        },
    }
