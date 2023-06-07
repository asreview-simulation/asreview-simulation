import click
from asreview.models.balance import TripleBalance
from .._epilog import epilog


name = TripleBalance.name


@click.command(
    epilog=epilog,
    help="Use triple balancer",
    name=f"bal:{name}",
)
@click.option(
    "--a",
    "a",
    default=2.155,
    help="hyperparameter",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--alpha",
    "alpha",
    default=0.94,
    help="hyperparameter",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--b",
    "b",
    default=0.789,
    help="hyperparameter",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--beta",
    "beta",
    default=1.0,
    help="hyperparameter",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--c",
    "c",
    default=0.835,
    help="hyperparameter",
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
@click.option(
    "--gamma",
    "gamma",
    default=2.0,
    help="hyperparameter",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--shuffle",
    "shuffle",
    help="hyperparameter",
    is_flag=True,
)
@click.pass_obj
def triple_balancer(obj, a, alpha, b, beta, c, force, gamma, shuffle):
    if not force:
        assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.abbr = name
    obj.balancer.params = {
        "a": a,
        "alpha": alpha,
        "b": b,
        "beta": beta,
        "c": c,
        "gamma": gamma,
        "shuffle": shuffle,
    }
    obj.provided.balancer = True
