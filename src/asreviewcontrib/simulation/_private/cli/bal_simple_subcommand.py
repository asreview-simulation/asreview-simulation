import click
from asreview.models.balance import SimpleBalance
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_bal_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig


name = f"bal-{SimpleBalance.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use no balancer",
    name=name,
    short_help="No balancer",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'bal' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def bal_simple_subcommand(obj, force):
    if not force:
        assert obj.provided.bal is False, dont_reassign_bal_msg
    params = {}
    obj.config.bal = OneModelConfig(abbr=name, params=params)
    obj.provided.bal = True
