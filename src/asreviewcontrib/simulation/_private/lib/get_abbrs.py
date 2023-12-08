def get_abbrs() -> [str]:
    """
    Returns:

        A list of recognized model abbreviations.
    """
    return [
        "bal-double",
        "bal-simple",
        "bal-undersample",
        "cls-logistic",
        "cls-lstm-base",
        "cls-lstm-pool",
        "cls-nb",
        "cls-nn-2-layer",
        "cls-rf",
        "cls-svm",
        "fex-doc2vec",
        "fex-embedding-idf",
        "fex-embedding-lstm",
        "fex-sbert",
        "fex-tfidf",
        "ofn-none",
        "ofn-wss",
        "qry-cluster",
        "qry-max",
        "qry-max-random",
        "qry-max-uncertainty",
        "qry-random",
        "qry-uncertainty",
        "sam-handpicked",
        "sam-random",
        "stp-none",
        "stp-nq",
        "stp-rel",
    ]
