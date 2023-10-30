msgs = [
    lambda fex: f"asreview.models.feature_extraction.{fex} instance doesn't have a method named 'get_embedding_matrix'",
    "'asreview simulate' doesn't use its '--embedding' argument (#34)"
]


def get_xfails_mocked(parameterization):
    reasons = {
        "doc2vec,lstm-base": msgs[0]("Doc2Vec"),
        "doc2vec,lstm-pool": msgs[0]("Doc2Vec"),
        "embedding-idf,logistic": msgs[1],
        "embedding-idf,lstm-base": " and ".join([msgs[1], msgs[0]("EmbeddingIdf")]),
        "embedding-idf,lstm-pool": " and ".join([msgs[1], msgs[0]("EmbeddingIdf")]),
        "embedding-idf,nb": msgs[1],
        "embedding-idf,nn-2-layer": msgs[1],
        "embedding-idf,rf": msgs[1],
        "embedding-idf,svm": msgs[1],
        "sbert,lstm-base": msgs[0]("SBERT"),
        "sbert,lstm-pool": msgs[0]("SBERT"),
        "tfidf,lstm-base": msgs[0]("Tfidf"),
        "tfidf,lstm-pool": msgs[0]("Tfidf"),
    }
    present = parameterization in reasons.keys()
    return present, reasons[parameterization] if present else ""
