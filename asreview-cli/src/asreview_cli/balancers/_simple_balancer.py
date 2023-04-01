import click
from asreviewlib.balancers import SimpleBalancer


name = SimpleBalancer.name


@click.command(name=f"b-{name}", help="Use simple balancer")
@click.pass_obj
def simple_balancer(obj):
    assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.model = name
    obj.balancer.params = {}
    obj.provided.balancer = True
