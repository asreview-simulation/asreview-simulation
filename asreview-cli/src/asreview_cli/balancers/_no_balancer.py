import click
from asreviewlib.balancers import NoBalancer
from .._epilog import epilog


name = NoBalancer.name


@click.command(epilog=epilog,
               help="Use no balancer",
               name=f"b-{name}")
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.pass_obj
def no_balancer(obj, force):
    if not force:
        assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.model = name
    obj.balancer.params = {}
    obj.provided.balancer = True
