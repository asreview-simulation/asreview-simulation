import click
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.sam.sam_random_config import get_sam_random_config


default_params = get_sam_random_config().params
name = "sam-random"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Random prior sampler",
    name=name,
    short_help="Random prior sampler",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--init_seed",
    "init_seed",
    default=default_params["init_seed"],
    help="Random seed",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_excluded",
    "n_excluded",
    default=default_params["n_excluded"],
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_included",
    "n_included",
    default=default_params["n_included"],
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def sam_random_subcommand(obj, force, init_seed, n_excluded, n_included):
    if not force:
        assert obj.provided.sam is False, (
            "Attempted reassignment of sampler. Use the --force flag "
            + "if you mean to overwrite the sampler configuration from previous steps. "
        )
    obj.models.sam.abbr = name
    obj.models.sam.params = {
        "init_seed": init_seed,
        "n_excluded": n_excluded,
        "n_included": n_included,
    }
    obj.provided.sam = True
