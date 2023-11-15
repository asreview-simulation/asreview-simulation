from math import ceil
from asreview.data import ASReviewData
from asreview_simulation._private.lib.config import CompleteConfig


def unwrap_stopping_vars(models: CompleteConfig, as_data: ASReviewData, n_instances: int):
    if models.stp.abbr == "stp-none":
        if models.sam.abbr == "sam-handpicked":
            records = models.sam.params.get("records", None)
            rows = models.sam.params.get("rows", None)
            if rows is not None:
                return int(ceil((len(as_data) - len(rows)) / n_instances))
            elif records is not None:
                return int(ceil((len(as_data) - len(records)) / n_instances))
            else:
                raise ValueError("Neither rows or records have been defined.")
        elif models.sam.abbr == "sam-random":
            n_excluded = models.sam.params.get("n_excluded")
            n_included = models.sam.params.get("n_included")
            return int(ceil((len(as_data) - n_excluded - n_included) / n_instances))
        else:
            raise ValueError("Unknown sampler.")
    if models.stp.abbr == "stp-nq":
        return models.stp.params["n_queries"]
    if models.stp.abbr == "stp-rel":
        return "min"
    raise ValueError("Unexpected value in stopping model abbreviation.")
