import click
from asreview.models.query import MaxRandomQuery
from .._epilog import epilog


name = MaxRandomQuery.name


@click.command(
    epilog=epilog,
    help="Mixed query strategy ('max' and 'random')",
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
    "--mix_ratio",
    "mix_ratio",
    default=0.95,
    help="Mix ratio",
    show_default=True,
    type=click.FLOAT,
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
def max_random_querier(obj, force, mix_ratio, seed):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {"mix_ratio": mix_ratio, "seed": seed}
    obj.provided.querier = True
