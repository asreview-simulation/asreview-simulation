import click
from asreview.models.query import MaxQuery
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.lib.one_model_config import OneModelConfig
from asreview_simulation._private.lib.qry.qry_max_params import get_qry_max_params


default_params = get_qry_max_params()
name = f"qry-{MaxQuery.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Max query strategy",
    name=name,
    short_help="Max query strategy",
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
def qry_max_subcommand(obj, force, n_instances):
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
