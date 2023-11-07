from asreview.models.feature_extraction.embedding_idf import EmbeddingIdf


def fex_embedding_idf_unwrap(params, random_state):
    mapped_params = {
        "split_ta": {False: 0, True: 1}[params["split_ta"]],
        "use_keywords": {False: 0, True: 1}[params["use_keywords"]],
    }
    return EmbeddingIdf(**mapped_params, random_state=random_state)
