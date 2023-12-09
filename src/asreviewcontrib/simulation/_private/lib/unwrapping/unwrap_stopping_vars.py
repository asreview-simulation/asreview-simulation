from math import ceil
from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.config import Config


def unwrap_stopping_vars(config: Config, as_data: ASReviewData, n_instances: int):
    if config.stp.abbr == "stp-none":
        if config.sam.abbr == "sam-handpicked":
            records = config.sam.params.get("records", None)
            rows = config.sam.params.get("rows", None)
            if rows is not None:
                return int(ceil((len(as_data) - len(rows)) / n_instances))
            elif records is not None:
                return int(ceil((len(as_data) - len(records)) / n_instances))
            else:
                raise ValueError("Neither rows or records have been defined.")
        elif config.sam.abbr == "sam-random":
            n_excluded = config.sam.params.get("n_excluded")
            n_included = config.sam.params.get("n_included")
            assert isinstance(n_excluded, int), "Expected n_excluded to be of type int"
            assert isinstance(n_included, int), "Expected n_included to be of type int"
            return int(ceil((len(as_data) - n_excluded - n_included) / n_instances))
        else:
            raise ValueError("Unknown sampler.")
    if config.stp.abbr == "stp-nq":
        return config.stp.params["n_queries"]
    if config.stp.abbr == "stp-rel":
        return "min"
    raise ValueError("Unexpected value in stopping model abbreviation.")
