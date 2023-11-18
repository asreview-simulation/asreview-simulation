import click
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.cli.cli_msgs import dont_reassign_ofn_msg
from asreview_simulation._private.lib.ofn.ofn_wss_params import get_ofn_wss_params
from asreview_simulation._private.lib.one_model_config import OneModelConfig


default_params = get_ofn_wss_params()
name = "ofn-wss"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use work saved over sampling objective function.",
    name=name,
    short_help="WSS objective function",
)
@click.option(
    "--at_perc",
    "at_perc",
    default=default_params["at_perc"],
    help="At what fraction the WSS should be calculated",
    type=click.INT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'ofn' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def ofn_wss_subcommand(obj, at_perc, force):
    if not force:
        assert obj.provided.ofn is False, dont_reassign_ofn_msg
    params = {
        "at_perc": at_perc,
    }
    obj.models.ofn = OneModelConfig(abbr=name, params=params)
    obj.provided.ofn = True
