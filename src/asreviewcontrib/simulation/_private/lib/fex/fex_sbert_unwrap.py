from asreview.models.feature_extraction.sbert import SBERT


def instantiate_unwrapped_fex_sbert(params, _random_state):
    mapped_params = {
        "split_ta": {False: 0, True: 1}[params["split_ta"]],
        "transformer_model": params["transformer_model"],
        "use_keywords": {False: 0, True: 1}[params["use_keywords"]],
    }
    return SBERT(**mapped_params)
