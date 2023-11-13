import hyperopt


def fex_tfidf_pyll():
    return {
        "abbr": "fex-tfidf",
        "params": {
            "ngram_max": hyperopt.hp.choice("ngram_max", range(1, 4, 1)),
            "split_ta": hyperopt.hp.choice("split_ta", [True, False]),
            "stop_words": hyperopt.hp.choice("stop_words", ["english", "none"]),
            "use_keywords": hyperopt.hp.choice("use_keywords", [True, False]),
        },
    }
