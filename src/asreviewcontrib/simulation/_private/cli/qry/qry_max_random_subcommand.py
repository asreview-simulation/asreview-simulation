import click
from asreview.models.query import MaxRandomQuery
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_qry_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig
from asreviewcontrib.simulation._private.lib.qry.qry_max_random_params import get_qry_max_random_params


default_params = get_qry_max_random_params()
abbr = f"qry-{MaxRandomQuery.name}".replace("_", "-")


@click.command(
    epilog=epilog,
    help="Configure the simulation to use a Mixed query strategy (Max and Random)",
    name=abbr,
    short_help="Mixed query strategy (Max and Random)",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'qry' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--fraction_max",
    "fraction_max",
    default=default_params["fraction_max"],
    help="Fraction of mixture that is queried using the Max strategy",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--n_instances",
    "n_instances",
    default=default_params["n_instances"],
    help="Number of records per query",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def qry_max_random_subcommand(obj, force, fraction_max, n_instances):
    if not force:
        assert obj.provided.qry is False, dont_reassign_qry_msg
    params = {
        "fraction_max": fraction_max,
        "n_instances": n_instances,
    }
    obj.config.qry = OneModelConfig(abbr=abbr, params=params)
    obj.provided.qry = True
