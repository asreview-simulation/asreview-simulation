import click
from asreviewlib.queriers import MixedQuerier
from .._epilog import epilog


name = MixedQuerier.name


@click.command(name=f"q-{name}", help="Use Mixed querier", epilog=epilog)
@click.option("--strategy1", "strategy1", default="max", type=click.STRING, help="hyperparameter 'strategy1'.")
@click.option("--strategy2", "strategy2", default="random", type=click.STRING, help="hyperparameter 'strategy2'.")
@click.option("--mix_ratio", "mix_ratio", default=0.95, type=click.FLOAT, help="hyperparameter 'mix_ratio'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the querier configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def mixed_querier(obj, strategy1, strategy2, mix_ratio, force):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {
        "strategy1": strategy1,
        "strategy2": strategy2,
        "mix_ratio": mix_ratio
    }
    obj.provided.querier = True
