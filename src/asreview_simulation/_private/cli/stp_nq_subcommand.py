import click
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.lib.stp.stp_nq_params import get_stp_nq_params
from asreview_simulation._private.lib.one_model_config import OneModelConfig


default_params = get_stp_nq_params()
name = "stp-nq"


@click.command(
    epilog=epilog,
    help="Configure the simulation to stop after evaluating N_QUERIES queries, "
    + "regardless of the relevance of evaluated records.",
    name=name,
    short_help="Number of queries based stopping rule",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the stopping configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--n_queries",
    "n_queries",
    help="Number of queries after which the simulation ends",
    default=default_params["n_queries"],
    required=True,
    type=click.INT,
)
@click.pass_obj
def stp_nq_subcommand(obj, force, n_queries):
    if not force:
        assert obj.provided.stp is False, (
            "Attempted reassignment of stopping. Use the --force flag "
            + "if you mean to overwrite the stopping configuration from previous steps. "
        )
    params = {
        "n_queries": n_queries,
    }
    obj.models.stp = OneModelConfig(abbr=name, params=params)
    obj.provided.stp = True
