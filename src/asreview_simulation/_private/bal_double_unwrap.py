from asreview.models.balance.double import DoubleBalance


def bal_double_unwrap(params, random_state):
    mapped_params = {
        "a": params["a"],
        "alpha": params["alpha"],
        "b": params["b"],
        "beta": params["beta"],
    }
    return DoubleBalance(**mapped_params, random_state=random_state)
