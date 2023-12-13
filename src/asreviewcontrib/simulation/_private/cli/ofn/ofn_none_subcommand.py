import click
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_ofn_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig


abbr = "ofn-none"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use no objective function.",
    name=abbr,
    short_help="No objective function",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'ofn' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def ofn_none_subcommand(obj, force):
    if not force:
        assert obj.provided.ofn is False, dont_reassign_ofn_msg
    params = {}
    obj.config.ofn = OneModelConfig(abbr=abbr, params=params)
    obj.provided.ofn = True
