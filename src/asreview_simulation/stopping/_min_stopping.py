import click
from .._epilog import epilog


name = "min"


@click.command(
    epilog=epilog,
    help="Stop the simulation once all relevant records have been found.",
    name=f"stp:{name}",
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
def min_stopping(obj, force):
    if not force:
        assert obj.provided.stopping is False, "Attempted reassignment of stopping"
    obj.stopping.model = name
    obj.stopping.params = {}
    obj.provided.stopping = True
