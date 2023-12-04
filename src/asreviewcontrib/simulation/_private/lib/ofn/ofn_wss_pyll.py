import hyperopt


def ofn_wss_pyll():
    return {
        "abbr": "ofn-wss",
        "params": {
            "at_pct": hyperopt.hp.choice("at_pct", range(0, 101, 1)),
        },
    }
