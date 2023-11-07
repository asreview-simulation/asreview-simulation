from asreview.models.balance.undersample import UndersampleBalance


def bal_undersample_unwrap(params, random_state):
    mapped_params = {
        "ratio": params["ratio"],
    }
    return UndersampleBalance(**mapped_params, random_state=random_state)
