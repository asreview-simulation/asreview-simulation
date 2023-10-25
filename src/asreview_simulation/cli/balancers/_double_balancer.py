import click
from asreview.models.balance import DoubleBalance
from .._epilog import epilog


name = DoubleBalance.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Double balancer",
    name=f"bal-{name}",
    short_help="Double balancer",
)
@click.option(
    "--a",
    "a",
    default=2.155,
    help="Weight of the 1's. Higher values mean linearly more 1's in your training sample.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--alpha",
    "alpha",
    default=0.94,
    help="Scaling of the weight of the 1's, as a function of the ratio of ones to zeros. " +
         "A positive value means that the lower the ratio of zeros to ones, the higher " +
         "the weight of the ones.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--b",
    "b",
    default=0.789,
    help="How strongly we want to sample depending on the total number of samples. A value " +
         "of 1 means no dependence on the total number of samples, while lower " +
         "values mean increasingly stronger dependence on the number of samples.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--beta",
    "beta",
    default=1.0,
    help="Scaling of the weight of the zeros depending on the number of samples. Higher " +
         "values means that larger samples are more strongly penalizing zeros.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def double_balancer(obj, a, alpha, b, beta, force):
    if not force:
        assert obj.provided.balancer is False, (
            "Attempted reassignment of balancer. Use the --force flag "
            + "if you mean to overwrite the balancer configuration from previous steps. "
        )
    obj.balancer.abbr = name
    obj.balancer.params = {
        "a": a,
        "alpha": alpha,
        "b": b,
        "beta": beta,
    }
    obj.provided.balancer = True
