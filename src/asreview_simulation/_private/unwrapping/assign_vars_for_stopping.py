from math import ceil
from asreview.data import ASReviewData
from asreview_simulation._private.models import Models


def assign_vars_for_stopping(models: Models, as_data: ASReviewData, n_instances: int):
    if models.stopping.abbr == "stp-none":
        if models.sampler.abbr == "sam-handpicked":
            records = models.sampler.params.get("records", None)
            rows = models.sampler.params.get("rows", None)
            if rows is not None:
                return int(ceil((len(as_data) - len(rows)) / n_instances))
            elif records is not None:
                return int(ceil((len(as_data) - len(records)) / n_instances))
            else:
                raise ValueError("Neither rows or records have been defined.")
        elif models.sampler.abbr == "sam-random":
            n_excluded = models.sampler.params.get("n_excluded")
            n_included = models.sampler.params.get("n_included")
            return int(ceil((len(as_data) - n_excluded - n_included) / n_instances))
        else:
            raise ValueError("Unknown sampler.")
    if models.stopping.abbr == "stp-nq":
        return models.stopping.params["n_queries"]
    if models.stopping.abbr == "stp-rel":
        return "min"
    raise ValueError("Unexpected value in stopping model abbreviation.")
