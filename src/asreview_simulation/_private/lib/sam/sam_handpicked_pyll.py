import hyperopt


def sam_handpicked_pyll():
    return {
        "abbr": "sam-handpicked",
        "params": {
            "records": hyperopt.hp.choice("records", [None]),     # TODO
            "rows": hyperopt.hp.choice("rows", [None])            # TODO
        },
    }
