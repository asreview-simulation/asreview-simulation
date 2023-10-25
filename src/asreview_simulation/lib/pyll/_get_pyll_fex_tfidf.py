import hyperopt


def get_pyll_fex_tfidf():
    return {
        "abbr": "tfidf",
        "params": {
            "ngram_max": hyperopt.hp.uniformint("ngram_max", 1, 3),
            "split_ta": hyperopt.hp.randint("split_ta", 2),
            "stop_words": hyperopt.hp.choice("stop_words", ["english", "none"]),
            "use_keywords": hyperopt.hp.randint("use_keywords", 2),
        },
    }
