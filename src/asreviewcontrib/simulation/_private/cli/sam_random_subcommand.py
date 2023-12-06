import click
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_sam_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig
from asreviewcontrib.simulation._private.lib.sam.sam_random_params import get_sam_random_params


default_params = get_sam_random_params()
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
    help="Force setting the 'sam' configuration, even if that means overwriting a previous configuration.",
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
        assert obj.provided.sam is False, dont_reassign_sam_msg
    params = {
        "init_seed": init_seed,
        "n_excluded": n_excluded,
        "n_included": n_included,
    }
    obj.config.sam = OneModelConfig(abbr=name, params=params)
    obj.provided.sam = True
