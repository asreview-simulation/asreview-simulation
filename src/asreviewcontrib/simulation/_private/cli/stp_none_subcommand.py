import click
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_stp_msg
from asreviewcontrib.simulation._private.lib.one_model_config import OneModelConfig


name = "stp-none"


@click.command(
    epilog=epilog,
    help="Configure the simulation to stop after evaluating all records, regardless of the relevance of evaluated records.",
    name=name,
    short_help="No stopping rule",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'stp' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def stp_none_subcommand(obj, force):
    if not force:
        assert obj.provided.stp is False, dont_reassign_stp_msg
    params = {}
    obj.models.stp = OneModelConfig(abbr=name, params=params)
    obj.provided.stp = True
