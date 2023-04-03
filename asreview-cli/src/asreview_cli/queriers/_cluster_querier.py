import click
from asreviewlib.queriers import ClusterQuerier
from .._epilog import epilog


name = ClusterQuerier.name


@click.command(name=f"q-{name}", help="Use Cluster querier", epilog=epilog)
@click.option("--cluster_size", "cluster_size", default=350, type=click.INT, help="hyperparameter 'cluster_size'.")
@click.option("--update_interval", "update_interval", default=200, type=click.INT,
              help="hyperparameter 'update_interval'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the querier configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def cluster_querier(obj, cluster_size, update_interval, force):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {
        "cluster_size": cluster_size,
        "update_interval": update_interval
    }
    obj.provided.querier = True
