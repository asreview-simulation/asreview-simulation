import click
from asreviewlib.queriers import MaxQuerier
from .._epilog import epilog


name = MaxQuerier.name


@click.command(epilog=epilog,
               help="Use Max querier",
               name=f"q-{name}")
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.pass_obj
def max_querier(obj, force):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {}
    obj.provided.querier = True
