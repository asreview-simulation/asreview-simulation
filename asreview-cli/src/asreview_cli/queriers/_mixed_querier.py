import click
from asreviewlib.queriers import MixedQuerier


name = MixedQuerier.name


@click.command(name=f"q-{name}", help="Use Mixed querier")
@click.option("-strategy1", "strategy1", default="max", type=str, help="hyperparameter 'strategy1'.")
@click.option("-strategy2", "strategy2", default="random", type=str, help="hyperparameter 'strategy2'.")
@click.option("-mix_ratio", "mix_ratio", default=0.95, type=float, help="hyperparameter 'mix_ratio'.")
@click.pass_obj
def mixed_querier(obj, strategy1, strategy2, mix_ratio):
    assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {
        "strategy1": strategy1,
        "strategy2": strategy2,
        "mix_ratio": mix_ratio
    }
    obj.provided.querier = True
