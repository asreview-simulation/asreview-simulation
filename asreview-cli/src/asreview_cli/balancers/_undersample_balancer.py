import click
from asreviewlib.balancers import UndersampleBalancer
from .._epilog import epilog


name = UndersampleBalancer.name


@click.command(name=f"b-{name}", help="Use undersample balancer", epilog=epilog)
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the balancer configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.option("--ratio", "ratio", default=1.0, type=click.FLOAT, help="hyperparameter 'ratio'.")
@click.pass_obj
def undersample_balancer(obj, ratio, force):
    if not force:
        assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.model = name
    obj.balancer.params = {
        "ratio": ratio
    }
    obj.provided.balancer = True
