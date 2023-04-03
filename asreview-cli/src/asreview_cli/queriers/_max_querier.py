import click
from asreviewlib.queriers import MaxQuerier
from .._epilog import epilog


name = MaxQuerier.name


@click.command(name=f"q-{name}", help="Use Max querier", epilog=epilog)
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the querier configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def max_querier(obj, force):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {}
    obj.provided.querier = True
