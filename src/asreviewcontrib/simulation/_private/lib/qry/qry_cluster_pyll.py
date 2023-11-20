import hyperopt


def qry_cluster_pyll():
    return {
        "abbr": "qry-cluster",
        "params": {
            "cluster_size": hyperopt.hp.quniform("cluster_size", 50, 1000, 1),
            "n_instances": hyperopt.hp.choice("n_instances", range(1, 100, 1)),
            "update_interval": hyperopt.hp.quniform("update_interval", 100, 300, 1),
        },
    }
