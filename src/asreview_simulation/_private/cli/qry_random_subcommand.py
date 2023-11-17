import click
from asreview.models.query import RandomQuery
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.lib.qry.qry_max_random_params import get_qry_max_random_params
from asreview_simulation._private.lib.one_model_config import OneModelConfig


default_params = get_qry_max_random_params()
name = f"qry-{RandomQuery.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Random query strategy",
    name=name,
    short_help="Random query strategy",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
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
def qry_random_subcommand(obj, force, n_instances):
    if not force:
        assert obj.provided.qry is False, (
            "Attempted reassignment of querier. Use the --force flag "
            + "if you mean to overwrite the querier configuration from previous steps. "
        )
    params = {
        "n_instances": n_instances,
    }
    obj.models.qry = OneModelConfig(abbr=name, params=params)
    obj.provided.qry = True
