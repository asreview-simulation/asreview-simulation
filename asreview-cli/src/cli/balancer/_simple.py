import click


@click.command(name="b-simple", help="Use simple balancer")
@click.pass_obj
def simple(obj):
    assert obj.provided.balancer is False, "Attempted reassignment of simple balancer"
    obj.balancer.model = "simple"
    obj.balancer.params = {}
    obj.provided.balancer = True
