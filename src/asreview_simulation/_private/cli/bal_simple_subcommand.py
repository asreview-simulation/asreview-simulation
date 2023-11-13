import click
from asreview.models.balance import SimpleBalance
from asreview_simulation._private.cli.cli_epilog import epilog


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
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def bal_simple_subcommand(obj, force):
    if not force:
        assert obj.provided.bal is False, (
            "Attempted reassignment of balancer. Use the --force flag "
            + "if you mean to overwrite the balancer configuration from previous steps. "
        )
    obj.models.bal.abbr = name
    obj.models.bal.params = {}
    obj.provided.bal = True
