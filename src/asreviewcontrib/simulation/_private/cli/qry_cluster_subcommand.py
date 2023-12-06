import click
from asreview.models.query import ClusterQuery
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_qry_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig
from asreviewcontrib.simulation._private.lib.qry.qry_cluster_params import get_qry_cluster_params


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
    help="Force setting the 'qry' configuration, even if that means overwriting a previous configuration.",
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
        assert obj.provided.qry is False, dont_reassign_qry_msg
    params = {
        "cluster_size": cluster_size,
        "n_instances": n_instances,
        "update_interval": update_interval,
    }
    obj.config.qry = OneModelConfig(abbr=name, params=params)
    obj.provided.qry = True
