import hyperopt


def get_pyll_qry_cluster():
    return {
        "abbr": "cluster",
        "params": {
            "cluster_size": hyperopt.hp.quniform("cluster_size", 50, 1000, 1),
            "update_interval": hyperopt.hp.quniform("update_interval", 100, 300, 1),
        }
    }
