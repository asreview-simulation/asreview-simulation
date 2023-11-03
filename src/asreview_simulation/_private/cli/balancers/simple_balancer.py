import click
from asreview.models.balance import SimpleBalance
from asreview_simulation._private.cli.epilog import epilog


name = SimpleBalance.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use no balancer",
    name=f"bal-{name}",
    short_help="No balancer",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def simple_balancer(obj, force):
    if not force:
        assert obj.provided.balancer is False, (
            "Attempted reassignment of balancer. Use the --force flag "
            + "if you mean to overwrite the balancer configuration from previous steps. "
        )
    obj.balancer.abbr = name
    obj.balancer.params = {}
    obj.provided.balancer = True
