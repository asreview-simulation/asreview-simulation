import click
from asreviewlib.balancers import NoBalancer
from .._epilog import epilog


name = NoBalancer.name


@click.command(name=f"b-{name}", help="Use no balancer", epilog=epilog)
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the balancer configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def no_balancer(obj, force):
    if not force:
        assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.model = name
    obj.balancer.params = {}
    obj.provided.balancer = True
