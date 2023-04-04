import click
from asreviewlib.balancers import DoubleBalancer
from .._epilog import epilog


name = DoubleBalancer.name


@click.command(epilog=epilog,
               help="Use double balancer",
               name=f"b-{name}")
@click.option("--a", "a",
              default=2.155,
              help="hyperparameter 'a'.",
              show_default=True,
              type=click.FLOAT)
@click.option("--alpha", "alpha",
              default=0.94,
              help="hyperparameter 'alpha'.",
              show_default=True,
              type=click.FLOAT)
@click.option("--b", "b",
              default=0.789,
              help="hyperparameter 'b'.",
              show_default=True,
              type=click.FLOAT)
@click.option("--beta", "beta",
              default=1.0,
              help="hyperparameter 'beta'.",
              show_default=True,
              type=click.FLOAT)
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.pass_obj
def double_balancer(obj, a, alpha, b, beta, force):
    if not force:
        assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.model = name
    obj.balancer.params = {
        "a": a,
        "alpha": alpha,
        "b": b,
        "beta": beta
    }
    obj.provided.balancer = True
