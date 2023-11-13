from asreview.models.query.cluster import ClusterQuery


def instantiate_unwrapped_qry_cluster(params, random_state):
    mapped_params = {
        "cluster_size": params["cluster_size"],
        "update_interval": params["update_interval"],
    }
    return ClusterQuery(**mapped_params, random_state=random_state)
