from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.config import Config


def stp_nq_unwrap(config: Config, _as_data: ASReviewData) -> int:
    return config.stp.params["n_queries"]
