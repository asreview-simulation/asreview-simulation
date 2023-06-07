import click
from asreview.models.query import UncertaintyQuery
from .._epilog import epilog


name = UncertaintyQuery.name


@click.command(
    epilog=epilog,
    help="Uncertainty query strategy",
    name=f"qry:{name}",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def uncertainty_querier(obj, force):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.abbr = name
    obj.querier.params = {}
    obj.provided.querier = True
