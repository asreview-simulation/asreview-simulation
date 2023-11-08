from asreview.models.balance.undersample import UndersampleBalance


def instantiate_unwrapped_bal_undersample(params, random_state):
    mapped_params = {
        "ratio": params["ratio"],
    }
    return UndersampleBalance(**mapped_params, random_state=random_state)
