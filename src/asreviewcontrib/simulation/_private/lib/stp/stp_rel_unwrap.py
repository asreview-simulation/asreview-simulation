from typing import Literal
from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.config import Config


def stp_rel_unwrap(_config: Config, _as_data: ASReviewData) -> Literal["min"]:
    return "min"
