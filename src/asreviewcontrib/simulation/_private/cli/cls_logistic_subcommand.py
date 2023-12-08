import click
from asreview.models.classifiers import LogisticClassifier
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_clr_msg
from asreviewcontrib.simulation._private.lib.clr.clr_logistic_params import get_clr_logistic_params
from asreviewcontrib.simulation._private.lib.config import OneModelConfig


default_params = get_clr_logistic_params()
name = f"clr-{LogisticClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Logistic Regression classifier.",
    name=name,
    short_help="Logistic Regression classifier",
)
@click.option(
    "--c",
    "c",
    default=default_params["c"],
    help="Parameter inverse to the regularization strength of the model.",
    show_default=True,
    type=float,
)
@click.option(
    "--class_weight",
    "class_weight",
    default=default_params["class_weight"],
    help="Class weight of the inclusions.",
    type=click.FLOAT,
    show_default=True,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'clr' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def clr_logistic_subcommand(obj, c, class_weight, force):
    if not force:
        assert obj.provided.clr is False, dont_reassign_clr_msg
    params = {
        "c": c,
        "class_weight": class_weight,
    }
    obj.config.clr = OneModelConfig(abbr=name, params=params)
    obj.provided.clr = True
