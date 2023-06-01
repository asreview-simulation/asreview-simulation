import click
from asreview.models.query import RandomQuery
from .._epilog import epilog


name = RandomQuery.name


@click.command(
    epilog=epilog,
    help="Random query",
    name=f"qer:{name}",
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
    "--seed",
    "seed",
    default=535,
    help="Random seed",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def random_querier(obj, force, seed):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {"seed": seed}
    obj.provided.querier = True
