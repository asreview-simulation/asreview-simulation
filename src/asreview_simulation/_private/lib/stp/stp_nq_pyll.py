import hyperopt


def stp_nq_pyll():
    return {
        "abbr": "stp-nq",
        "params": {
            "n_queries": hyperopt.hp.choice("n_queries", [None])   # TODO
        },
    }
