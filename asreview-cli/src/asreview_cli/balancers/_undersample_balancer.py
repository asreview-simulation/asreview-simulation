import click
from asreviewlib.balancers import UndersampleBalancer


name = UndersampleBalancer.name


@click.command(name=f"b-{name}", help="Use undersample balancer")
@click.option("-ratio", "ratio", default=1.0, type=float, help="hyperparameter 'ratio'.")
@click.pass_obj
def undersample_balancer(obj, ratio):
    assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.model = name
    obj.balancer.params = {
        "ratio": ratio
    }
    obj.provided.balancer = True
