import click
from asreview.models.query import ClusterQuery
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.lib.qry.qry_cluster_params import get_qry_cluster_params


default_params = get_qry_cluster_params()
name = f"qry-{ClusterQuery.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Cluster query strategy",
    name=name,
    short_help="Cluster query strategy",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--cluster_size",
    "cluster_size",
    default=default_params["cluster_size"],
    help="Size of the clusters to be made. If the size of the clusters is smaller than "
    + "the size of the pool, fall back to max sampling.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_instances",
    "n_instances",
    default=default_params["n_instances"],
    help="Number of records per query",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--update_interval",
    "update_interval",
    default=default_params["update_interval"],
    help="Update the clustering every x instances.",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def qry_cluster_subcommand(obj, force, cluster_size, n_instances, update_interval):
    if not force:
        assert obj.provided.qry is False, (
            "Attempted reassignment of querier. Use the --force flag "
            + "if you mean to overwrite the querier configuration from previous steps. "
        )
    obj.models.qry.abbr = name
    obj.models.qry.params = {
        "cluster_size": cluster_size,
        "n_instances": n_instances,
        "update_interval": update_interval,
    }
    obj.provided.qry = True
