import click
from asreview.models.balance import UndersampleBalance
from .._epilog import epilog


name = UndersampleBalance.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Undersample balancer",
    name=f"bal-{name}",
    short_help="Undersample balancer",
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
    help="Undersampling ratio of the zeros. If for example we set a ratio of " +
         "0.25, we would sample only a quarter of the zeros and all the ones.",
    show_default=True,
    type=click.FLOAT,
)
@click.pass_obj
def undersample_balancer(obj, force, ratio):
    if not force:
        assert obj.provided.balancer is False, (
            "Attempted reassignment of balancer. Use the --force flag "
            + "if you mean to overwrite the balancer configuration from previous steps. "
        )
    obj.balancer.abbr = name
    obj.balancer.params = {
        "ratio": ratio,
    }
    obj.provided.balancer = True
