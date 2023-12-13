import click
from asreview.models.balance import UndersampleBalance
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_bal_msg
from asreviewcontrib.simulation._private.lib.bal.bal_undersample_params import get_bal_undersample_params
from asreviewcontrib.simulation._private.lib.config import OneModelConfig


default_params = get_bal_undersample_params()
abbr = f"bal-{UndersampleBalance.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Undersample balancer",
    name=abbr,
    short_help="Undersample balancer",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'bal' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--ratio",
    "ratio",
    default=default_params["ratio"],
    help="Undersampling ratio of the zeros. If for example we set a ratio of "
    + "0.25, we would sample only a quarter of the zeros and all the ones.",
    show_default=True,
    type=click.FLOAT,
)
@click.pass_obj
def bal_undersample_subcommand(obj, force, ratio):
    if not force:
        assert obj.provided.bal is False, dont_reassign_bal_msg
    params = {
        "ratio": ratio,
    }
    obj.config.bal = OneModelConfig(abbr=abbr, params=params)
    obj.provided.bal = True
