import click
from asreview_simulation._private.cli.epilog import epilog


name = "none"


@click.command(
    epilog=epilog,
    help="Configure the simulation to stop after evaluating all records, "
    + "regardless of the relevance of evaluated records.",
    name=f"stp-{name}",
    short_help="No stopping rule",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the stopping configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def none_stopping(obj, force):
    if not force:
        assert obj.provided.stopping is False, (
            "Attempted reassignment of stopping. Use the --force flag "
            + "if you mean to overwrite the stopping configuration from previous steps. "
        )
    obj.stopping.abbr = name
    obj.stopping.params = {}
    obj.provided.stopping = True
