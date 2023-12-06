import click
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.lib.config import OneModelConfig


name = "stp-rel"


@click.command(
    epilog=epilog,
    help="Configure the simulation to stop once all relevant records have been found.",
    name=name,
    short_help="Stop once all the relevant records have been found",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'stp' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def stp_rel_subcommand(obj, force):
    if not force:
        assert obj.provided.stp is False, (
            "Attempted reassignment of 'stp' model. Use the --force flag "
            + "if you mean to overwrite the configuration from previous steps. "
        )
    params = {}
    obj.config.stp = OneModelConfig(abbr=name, params=params)
    obj.provided.stp = True
