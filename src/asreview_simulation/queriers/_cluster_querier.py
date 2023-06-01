import click
from asreview.models.query import ClusterQuery
from .._epilog import epilog


name = ClusterQuery.name


@click.command(
    epilog=epilog,
    help="Use Cluster querier",
    name=f"qer:{name}",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--cluster_size",
    "cluster_size",
    default=350,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--seed",
    "seed",
    default=535,
    help="Random seed",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--update_interval",
    "update_interval",
    default=200,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def cluster_querier(obj, force, cluster_size, seed, update_interval):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {
        "cluster_size": cluster_size,
        "seed": seed,
        "update_interval": update_interval,
    }
    obj.provided.querier = True
