from asreview.models.feature_extraction.tfidf import Tfidf


def instantiate_unwrapped_fex_tfidf(params, _random_state):
    mapped_params = {
        "ngram_max": params["ngram_max"],
        "split_ta": {False: 0, True: 1}[params["split_ta"]],
        "stop_words": params["stop_words"],
        "use_keywords": {False: 0, True: 1}[params["use_keywords"]],
    }
    return Tfidf(**mapped_params)
