import click
from asreviewlib.balancers import UndersampleBalancer
from .._epilog import epilog


name = UndersampleBalancer.name


@click.command(epilog=epilog,
               help="Use undersample balancer",
               name=f"bal:{name}")
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--ratio", "ratio",
              default=1.0,
              help="hyperparameter 'ratio'.",
              show_default=True,
              type=click.FLOAT)
@click.option("--seed", "seed",
              default=535,
              help="Random seed",
              show_default=True,
              type=click.INT)
@click.pass_obj
def undersample_balancer(obj, force, ratio, seed):
    if not force:
        assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.model = name
    obj.balancer.params = {
        "ratio": ratio,
        "seed": seed
    }
    obj.provided.balancer = True
