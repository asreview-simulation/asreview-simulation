import click
from .._epilog import epilog


name = "n"


@click.command(
    epilog=epilog,
    help="Stop the simulation after evaluating N queries, regardless of the relevance of evaluated records.",
    name=f"stp:{name}",
)
@click.argument(
    "n",
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
def n_stopping(obj, force, n):
    if not force:
        assert obj.provided.stopping is False, (
            "Attempted reassignment of stopping. Use the --force flag "
            + "if you mean to overwrite the stopping configuration from previous steps. "
        )
    obj.stopping.abbr = name
    obj.stopping.params = {
        "n": n,
    }
    obj.provided.stopping = True
