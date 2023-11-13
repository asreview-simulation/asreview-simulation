import hyperopt


def fex_sbert_pyll():
    return {
        "abbr": "fex-sbert",
        "params": {
            "split_ta": hyperopt.hp.choice("split_ta", [True, False]),
            "transformer_model": hyperopt.hp.choice("transformer_model", ["all-mpnet-base-v2"]),  # TODO
            "use_keywords": hyperopt.hp.choice("use_keywords", [True, False]),
        },
    }
