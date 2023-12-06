import click
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_ofn_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig
from asreviewcontrib.simulation._private.lib.ofn.ofn_wss_params import get_ofn_wss_params


default_params = get_ofn_wss_params()
name = "ofn-wss"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use work saved over sampling objective function.",
    name=name,
    short_help="WSS objective function",
)
@click.option(
    "--at_pct",
    "at_pct",
    default=default_params["at_pct"],
    help="At what percentage recall the WSS should be calculated",
    show_default=True,
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
def ofn_wss_subcommand(obj, at_pct, force):
    if not force:
        assert obj.provided.ofn is False, dont_reassign_ofn_msg
    assert 0 <= at_pct <= 100, "Expected value of --at_pct to be in interval [0,100]"
    params = {
        "at_pct": at_pct,
    }
    obj.config.ofn = OneModelConfig(abbr=name, params=params)
    obj.provided.ofn = True
