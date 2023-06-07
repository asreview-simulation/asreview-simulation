def assign_vars_for_stopping(obj):
    if obj.stopping.abbr == "none":
        return -1
    if obj.stopping.abbr == "n":
        return obj.stopping.params["n"]
    if obj.stopping.abbr == "min":
        return "min"
    raise ValueError("Unexpected value in stopping model abbreviation.")
