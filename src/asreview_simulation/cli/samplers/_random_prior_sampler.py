import click
from .._epilog import epilog


name = "random"


@click.command(
    epilog=epilog,
    help="Use random prior sampler",
    name=f"sam:{name}",
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
    "--init_seed",
    "init_seed",
    default=535,
    help="Random seed",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_excluded",
    "n_excluded",
    default=1,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_included",
    "n_included",
    default=1,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def random_prior_sampler(obj, force, init_seed, n_excluded, n_included):
    if not force:
        assert obj.provided.sampler is False, "Attempted reassignment of sampler"
    obj.sampler.abbr = name
    obj.sampler.params = {
        "init_seed": init_seed,
        "n_excluded": n_excluded,
        "n_included": n_included,
    }
    obj.provided.sampler = True
