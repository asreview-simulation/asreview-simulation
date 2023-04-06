import click
from .._epilog import epilog


name = "random"


@click.command(epilog=epilog,
               help="Use random prior sampler",
               name=f"sam:{name}")
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--n_excluded", "n_excluded",
              default=1,
              help="hyperparameter",
              show_default=True,
              type=click.INT)
@click.option("--n_included", "n_included",
              default=1,
              help="hyperparameter",
              show_default=True,
              type=click.INT)
@click.option("--seed", "seed",
              default=535,
              help="Random seed",
              show_default=True,
              type=click.INT)
@click.pass_obj
def random_prior_sampler(obj, force, n_excluded, n_included, seed):
    if not force:
        assert obj.provided.sampler is False, "Attempted reassignment of sampler"
    obj.sampler.model = name
    obj.sampler.params = {
        "n_excluded": n_excluded,
        "n_included": n_included,
        "seed": seed
    }
    obj.provided.sampler = True
