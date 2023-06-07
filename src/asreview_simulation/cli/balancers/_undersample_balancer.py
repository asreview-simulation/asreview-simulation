import click
from asreview.models.balance import UndersampleBalance
from .._epilog import epilog


name = UndersampleBalance.name


@click.command(
    epilog=epilog,
    help="Use undersample balancer",
    name=f"bal:{name}",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--ratio",
    "ratio",
    default=1.0,
    help="hyperparameter",
    show_default=True,
    type=click.FLOAT,
)
@click.pass_obj
def undersample_balancer(obj, force, ratio):
    if not force:
        assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.abbr = name
    obj.balancer.params = {
        "ratio": ratio,
    }
    obj.provided.balancer = True
