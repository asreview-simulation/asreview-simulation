def _make_msg(fex):
    return f"asreview.models.feature_extraction.{fex} instance doesn't have a method named 'get_embedding_matrix'"


def get_xfails_mocked(parameterization):
    reasons = {
        "doc2vec,lstm-base": _make_msg("Doc2Vec"),
        "doc2vec,lstm-pool": _make_msg("Doc2Vec"),
        "embedding-idf,lstm-base": _make_msg("EmbeddingIdf"),
        "embedding-idf,lstm-pool": _make_msg("EmbeddingIdf"),
        "sbert,lstm-base": _make_msg("SBERT"),
        "sbert,lstm-pool": _make_msg("SBERT"),
        "tfidf,lstm-base": _make_msg("Tfidf"),
        "tfidf,lstm-pool": _make_msg("Tfdf"),
    }
    present = parameterization in reasons.keys()
    return present, reasons[parameterization] if present else ""
