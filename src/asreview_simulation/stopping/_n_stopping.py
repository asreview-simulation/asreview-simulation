import click
from .._epilog import epilog


name = "n"


@click.command(
    epilog=epilog,
    help="Stop the simulation after evaluating N records, regardless of the relevance of evaluated "
    + "records. N does not include any prior records.",
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
        assert obj.provided.stopping is False, "Attempted reassignment of stopping"
    obj.stopping.model = name
    obj.stopping.params = {
        "n": n,
    }
    obj.provided.stopping = True
