import click
from asreview_simulation._private.cli.epilog import epilog


name = "min"


@click.command(
    epilog=epilog,
    help="Configure the simulation to stop once all relevant records have been found.",
    name=f"stp-{name}",
    short_help="'min' stopping rule",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the stopping configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def min_stopping(obj, force):
    if not force:
        assert obj.provided.stopping is False, (
            "Attempted reassignment of stopping. Use the --force flag "
            + "if you mean to overwrite the stopping configuration from previous steps. "
        )
    obj.stopping.abbr = name
    obj.stopping.params = {}
    obj.provided.stopping = True
