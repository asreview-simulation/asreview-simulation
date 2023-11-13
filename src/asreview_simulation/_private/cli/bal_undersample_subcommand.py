import click
from asreview.models.balance import UndersampleBalance
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.lib.bal.bal_undersample_config import get_bal_undersample_config


default_params = get_bal_undersample_config().params
name = f"bal-{UndersampleBalance.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Undersample balancer",
    name=name,
    short_help="Undersample balancer",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
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
        assert obj.provided.bal is False, (
            "Attempted reassignment of balancer. Use the --force flag "
            + "if you mean to overwrite the balancer configuration from previous steps. "
        )
    obj.models.bal.abbr = name
    obj.models.bal.params = {
        "ratio": ratio,
    }
    obj.provided.bal = True
