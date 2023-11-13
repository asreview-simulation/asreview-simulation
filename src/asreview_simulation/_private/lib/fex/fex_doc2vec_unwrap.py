from asreview.models.feature_extraction.doc2vec import Doc2Vec


def instantiate_unwrapped_fex_doc2vec(params, _random_state):
    mapped_params = {
        "dbow_words": {True: 1, False: 0}[params["dbow_words"]],
        "dm": {"dbow": 0, "dm": 1, "both": 2}[params["dm"]],
        "dm_concat": {True: 1, False: 0}[params["dm_concat"]],
        "epochs": params["epochs"],
        "min_count": params["min_count"],
        "split_ta": {True: 1, False: 0}[params["split_ta"]],
        "use_keywords": {True: 1, False: 0}[params["use_keywords"]],
        "vector_size": params["vector_size"],
        "window": params["window"],
    }
    return Doc2Vec(**mapped_params)
