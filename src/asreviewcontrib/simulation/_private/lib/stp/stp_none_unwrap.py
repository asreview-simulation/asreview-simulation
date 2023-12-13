from math import ceil
from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.config import Config


def stp_none_unwrap(config: Config, as_data: ASReviewData) -> int:
    if config.sam.abbr == "sam-handpicked":
        records = config.sam.params.get("records", None)
        rows = config.sam.params.get("rows", None)
        if rows is not None:
            n_remaining = len(as_data) - len(rows)
        elif records is not None:
            n_remaining = len(as_data) - len(records)
        else:
            raise ValueError("Neither rows or records have been defined.")
    elif config.sam.abbr == "sam-random":
        n_excluded = config.sam.params.get("n_excluded")
        n_included = config.sam.params.get("n_included")
        assert isinstance(n_excluded, int), "Expected n_excluded to be of type int"
        assert isinstance(n_included, int), "Expected n_included to be of type int"
        n_remaining = len(as_data) - n_excluded - n_included
    else:
        raise ValueError("Unknown sampler.")

    n_instances = config.qry.params.get("n_instances")
    assert isinstance(n_instances, int), "Expected n_instances to be of type int"
    return int(ceil(n_remaining / n_instances))
