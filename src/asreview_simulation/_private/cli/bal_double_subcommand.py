import click
from asreview.models.balance import DoubleBalance
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.cli.cli_msgs import dont_reassign_bal_msg
from asreview_simulation._private.lib.bal.bal_double_params import get_bal_double_params
from asreview_simulation._private.lib.one_model_config import OneModelConfig


default_params = get_bal_double_params()
name = f"bal-{DoubleBalance.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Double balancer",
    name=name,
    short_help="Double balancer",
)
@click.option(
    "--a",
    "a",
    default=default_params["a"],
    help="Weight of the 1's. Higher values mean linearly more 1's in your training sample.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--alpha",
    "alpha",
    default=default_params["alpha"],
    help="Scaling of the weight of the 1's, as a function of the ratio of ones to zeros. "
    + "A positive value means that the lower the ratio of zeros to ones, the higher "
    + "the weight of the ones.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--b",
    "b",
    default=default_params["b"],
    help="How strongly we want to sample depending on the total number of samples. A value "
    + "of 1 means no dependence on the total number of samples, while lower "
    + "values mean increasingly stronger dependence on the number of samples.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--beta",
    "beta",
    default=default_params["beta"],
    help="Scaling of the weight of the zeros depending on the number of samples. Higher "
    + "values means that larger samples are more strongly penalizing zeros.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'bal' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def bal_double_subcommand(obj, a, alpha, b, beta, force):
    if not force:
        assert obj.provided.bal is False, dont_reassign_bal_msg
    params = {
        "a": a,
        "alpha": alpha,
        "b": b,
        "beta": beta,
    }
    obj.models.bal = OneModelConfig(abbr=name, params=params)
    obj.provided.bal = True
