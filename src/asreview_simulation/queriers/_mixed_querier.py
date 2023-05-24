import click
from asreviewlib.queriers import MixedQuerier
from .._epilog import epilog


name = MixedQuerier.name


@click.command(epilog=epilog,
               name=f"qer:{name}",
               help="Use Mixed querier")
@click.option("--mix_ratio", "mix_ratio",
              default=0.95,
              help="hyperparameter",
              show_default=True,
              type=click.FLOAT)
@click.option("--seed", "seed",
              default=535,
              help="Random seed",
              show_default=True,
              type=click.INT)
@click.option("--strategy1", "strategy1",
              default="max",
              help="hyperparameter",
              show_default=True,
              type=click.Choice(["max"]))
@click.option("--strategy2", "strategy2",
              default="random",
              help="hyperparameter",
              show_default=True,
              type=click.Choice(["random"]))
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.pass_obj
def mixed_querier(obj, force, mix_ratio, seed, strategy1, strategy2):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {
        "mix_ratio": mix_ratio,
        "seed": seed,
        "strategy1": strategy1,
        "strategy2": strategy2
    }
    obj.provided.querier = True
