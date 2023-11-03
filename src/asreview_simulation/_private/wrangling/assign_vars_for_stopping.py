from math import ceil


def assign_vars_for_stopping(obj, as_data, n_instances):
    if obj.stopping.abbr == "none":
        if obj.sampler.abbr == "handpicked":
            records = obj.sampler.params.get("records", None)
            rows = obj.sampler.params.get("rows", None)
            if rows is not None:
                return int(ceil((len(as_data) - len(rows)) / n_instances))
            elif records is not None:
                return int(ceil((len(as_data) - len(records)) / n_instances))
            else:
                raise ValueError("Neither rows or records have been defined.")
        elif obj.sampler.abbr == "random":
            n_excluded = obj.sampler.params.get("n_excluded")
            n_included = obj.sampler.params.get("n_included")
            return int(ceil((len(as_data) - n_excluded - n_included) / n_instances))
        else:
            raise ValueError("Unknown sampler.")
    if obj.stopping.abbr == "nq":
        return obj.stopping.params["n_queries"]
    if obj.stopping.abbr == "rel":
        return "min"
    raise ValueError("Unexpected value in stopping model abbreviation.")
