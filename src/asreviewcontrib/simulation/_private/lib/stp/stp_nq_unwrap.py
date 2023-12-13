from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.config import Config


def stp_nq_unwrap(config: Config, _as_data: ASReviewData) -> int:
    n_queries = config.stp.params["n_queries"]
    assert isinstance(n_queries, int), "Expected n_queries to be of type int"
    return n_queries
