import click
from asreview_simulation._private.cli.epilog import epilog


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
    default=None,
    required=True,
    type=click.INT,
)
@click.pass_obj
def stp_nq(obj, force, n_queries):
    if not force:
        assert obj.provided.stopping is False, (
            "Attempted reassignment of stopping. Use the --force flag "
            + "if you mean to overwrite the stopping configuration from previous steps. "
        )
    obj.models.stopping.abbr = name
    obj.models.stopping.params = {
        "n_queries": n_queries,
    }
    obj.provided.stopping = True
