import click
from asreview.models.query import MaxUncertaintyQuery
from .._epilog import epilog


name = MaxUncertaintyQuery.name


@click.command(
    epilog=epilog,
    help="Mixed query strategy ('max' and 'uncertainty')",
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
@click.option(
    "--mix_ratio",
    "mix_ratio",
    default=0.95,
    help="Mix ratio",
    show_default=True,
    type=click.FLOAT,
)
@click.pass_obj
def max_uncertainty_querier(obj, force, mix_ratio):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.abbr = name
    obj.querier.params = {
        "mix_ratio": mix_ratio,
    }
    obj.provided.querier = True
