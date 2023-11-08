import click
from asreview.models.query import MaxRandomQuery
from asreview_simulation._private.cli_epilog import epilog
from asreview_simulation._private.qry.qry_max_random_config import get_qry_max_random_config


default_params = get_qry_max_random_config().params
name = f"qry-{MaxRandomQuery.name}".replace("_", "-")


@click.command(
    epilog=epilog,
    help="Configure the simulation to use a Mixed query strategy (Max and Random)",
    name=name,
    short_help="Mixed query strategy (Max and Random)",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
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
        assert obj.provided.qry is False, (
            "Attempted reassignment of querier. Use the --force flag "
            + "if you mean to overwrite the querier configuration from previous steps. "
        )
    obj.models.qry.abbr = name
    obj.models.qry.params = {
        "fraction_max": fraction_max,
        "n_instances": n_instances,
    }
    obj.provided.qry = True
