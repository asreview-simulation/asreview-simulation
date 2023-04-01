import click
from asreviewlib.queriers import MaxQuerier


name = MaxQuerier.name


@click.command(name=f"q-{name}", help="Use Max querier")
@click.pass_obj
def max_querier(obj):
    assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {}
    obj.provided.querier = True
