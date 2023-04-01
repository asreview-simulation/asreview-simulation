import click
from asreviewlib.queriers import ClusterQuerier


name = ClusterQuerier.name


@click.command(name=f"q-{name}", help="Use Cluster querier")
@click.option("-cluster_size", "cluster_size", default=350, type=int, help="hyperparameter 'cluster_size'.")
@click.option("-update_interval", "update_interval", default=200, type=int, help="hyperparameter 'update_interval'.")
@click.pass_obj
def cluster_querier(obj, cluster_size, update_interval):
    assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {
        "cluster_size": cluster_size,
        "update_interval": update_interval
    }
    obj.provided.querier = True
