import click
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.cli.cli_msgs import dont_reassign_ofn_msg
from asreview_simulation._private.lib.one_model_config import OneModelConfig


name = "ofn-none"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use no objective function.",
    name=name,
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
    obj.models.ofn = OneModelConfig(abbr=name, params=params)
    obj.provided.ofn = True
