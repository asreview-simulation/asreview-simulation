from asreview.models.query.cluster import ClusterQuery


def instantiate_unwrapped_qry_cluster(params, random_state):
    mapped_params = {
        "cluster_size": params["cluster_size"],
        "update_interval": params["update_interval"],
    }

    # asreview's query model does not expect n_instances as part
    # of the params dict but as a separate variable
    assert "n_instances" in params.keys()
    assert "n_instances" not in mapped_params.keys()

    return ClusterQuery(**mapped_params, random_state=random_state)
