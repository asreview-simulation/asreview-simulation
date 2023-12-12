from typing import List
from asreviewcontrib.simulation._private.lib.get_quads import get_quads


TAbbrs = List[str]


def get_abbrs() -> TAbbrs:
    """
    Returns:

        A list of recognized model abbreviations.
    """
    my_abbrs = {
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
    }
    other_abbrs = set([abbr for abbr, _ in get_quads()])
    return sorted(my_abbrs.union(other_abbrs))
