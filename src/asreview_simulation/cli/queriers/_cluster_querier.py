import click
from asreview.models.query import ClusterQuery
from .._epilog import epilog


name = ClusterQuery.name


@click.command(
    epilog=epilog,
    help="Use Cluster query strategy",
    name=f"qry:{name}",
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
    "--n_instances",
    "n_instances",
    default=1,
    help="Number of records per query",
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
def cluster_querier(obj, force, cluster_size, n_instances, update_interval):
    if not force:
        assert obj.provided.querier is False, (
            "Attempted reassignment of querier. Use the --force flag "
            + "if you mean to overwrite the querier configuration from previous steps. "
        )
    obj.querier.abbr = name
    obj.querier.params = {
        "cluster_size": cluster_size,
        "n_instances": n_instances,
        "update_interval": update_interval,
    }
    obj.provided.querier = True
