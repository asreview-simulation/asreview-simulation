import click
from asreviewlib.balancers import DoubleBalancer


name = DoubleBalancer.name


@click.command(name=f"b-{name}", help="Use double balancer")
@click.option("--a", "a", default=2.155, type=click.FLOAT, help="hyperparameter 'a'.")
@click.option("--alpha", "alpha", default=0.94, type=click.FLOAT, help="hyperparameter 'alpha'.")
@click.option("--b", "b", default=0.789, type=click.FLOAT, help="hyperparameter 'b'.")
@click.option("--beta", "beta", default=1.0, type=click.FLOAT, help="hyperparameter 'beta'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the balancer configura" +
              "tion, even if that means overwriting a previous configuration.")
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
