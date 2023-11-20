import hyperopt


def ofn_wss_pyll():
    return {
        "abbr": "ofn-wss",
        "params": {
            "at_perc": hyperopt.hp.choice("at_perc", range(0, 101, 1)),
        },
    }
