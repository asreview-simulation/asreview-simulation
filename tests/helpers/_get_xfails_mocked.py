def _make_msg(fex):
    return f"{fex} instance doesn't have a method named 'get_embedding_matrix'"


def get_xfails_mocked(parameterization):
    reasons = {
        "doc2vec,lstm-base": _make_msg("asreview.models.feature_extraction.Doc2Vec"),
        "doc2vec,lstm-pool": _make_msg("asreview.models.feature_extraction.Doc2Vec"),
        "embedding-idf,lstm-base": _make_msg("asreview.models.feature_extraction.EmbeddingIdf"),
        "embedding-idf,lstm-pool": _make_msg("asreview.models.feature_extraction.EmbeddingIdf"),
        "sbert,lstm-base": _make_msg("asreview.models.feature_extraction.SBERT"),
        "sbert,lstm-pool": _make_msg("asreview.models.feature_extraction.SBERT"),
        "tfidf,lstm-base": _make_msg("asreview.models.feature_extraction.Tfidf"),
        "tfidf,lstm-pool": _make_msg("asreview.models.feature_extraction.Tfdf"),
    }
    present = parameterization in reasons.keys()
    return present, reasons[parameterization] if present else ""
