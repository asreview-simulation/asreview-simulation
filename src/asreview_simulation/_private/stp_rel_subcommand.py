import click
from asreview_simulation._private.cli_epilog import epilog


name = "stp-rel"


@click.command(
    epilog=epilog,
    help="Configure the simulation to stop once all relevant records have been found.",
    name=name,
    short_help="Stop when relevant records are found",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the stopping configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def stp_rel_subcommand(obj, force):
    if not force:
        assert obj.provided.stopping is False, (
            "Attempted reassignment of stopping. Use the --force flag "
            + "if you mean to overwrite the stopping configuration from previous steps. "
        )
    obj.models.stopping.abbr = name
    obj.models.stopping.params = {}
    obj.provided.stopping = True
