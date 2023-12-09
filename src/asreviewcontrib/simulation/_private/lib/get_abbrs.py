from typing import List


def get_abbrs() -> List[str]:
    """
    Returns:

        A list of recognized model abbreviations.
    """
    return [
        "bal-double",
        "bal-simple",
        "bal-undersample",
        "clr-logistic",
        "clr-lstm-base",
        "clr-lstm-pool",
        "clr-nb",
        "clr-nn-2-layer",
        "clr-rf",
        "clr-svm",
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
