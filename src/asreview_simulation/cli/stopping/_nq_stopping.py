import click
from .._epilog import epilog


name = "nq"


@click.command(
    epilog=epilog,
    help="Configure the simulation to stop after evaluating N_QUERIES queries, "
    + "regardless of the relevance of evaluated records.",
    name=f"stp-{name}",
    short_help="Number of queries based stopping rule",
)
@click.argument(
    "n_queries",
    default=None,
    type=click.INT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the stopping configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def nq_stopping(obj, force, n_queries):
    if not force:
        assert obj.provided.stopping is False, (
            "Attempted reassignment of stopping. Use the --force flag "
            + "if you mean to overwrite the stopping configuration from previous steps. "
        )
    obj.stopping.abbr = name
    obj.stopping.params = {
        "n_queries": n_queries,
    }
    obj.provided.stopping = True
