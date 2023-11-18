import click
from asreview.models.classifiers import NaiveBayesClassifier
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.cli.cli_msgs import dont_reassign_cls_msg
from asreview_simulation._private.lib.cls.cls_nb_params import get_cls_nb_params
from asreview_simulation._private.lib.one_model_config import OneModelConfig


default_params = get_cls_nb_params()
name = f"cls-{NaiveBayesClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Naive Bayes classifier",
    name=name,
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
    help="Force setting the 'cls' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def cls_nb_subcommand(obj, alpha, force):
    if not force:
        assert obj.provided.cls is False, dont_reassign_cls_msg
    params = {
        "alpha": alpha,
    }
    obj.models.cls = OneModelConfig(abbr=name, params=params)
    obj.provided.cls = True
