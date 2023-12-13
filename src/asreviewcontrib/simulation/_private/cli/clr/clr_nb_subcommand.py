import click
from asreview.models.classifiers import NaiveBayesClassifier
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_clr_msg
from asreviewcontrib.simulation._private.lib.clr.clr_nb_params import get_clr_nb_params
from asreviewcontrib.simulation._private.lib.config import OneModelConfig


default_params = get_clr_nb_params()
abbr = f"clr-{NaiveBayesClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Naive Bayes classifier",
    name=abbr,
    short_help="Naive Bayes classifier",
)
@click.option(
    "--alpha",
    "alpha",
    default=default_params["alpha"],
    help="Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing).",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'clr' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def clr_nb_subcommand(obj, alpha, force):
    if not force:
        assert obj.provided.clr is False, dont_reassign_clr_msg
    params = {
        "alpha": alpha,
    }
    obj.config.clr = OneModelConfig(abbr=abbr, params=params)
    obj.provided.clr = True
