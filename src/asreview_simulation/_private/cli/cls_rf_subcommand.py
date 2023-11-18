import click
from asreview.models.classifiers import RandomForestClassifier
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.cli.cli_msgs import dont_reassign_cls_msg
from asreview_simulation._private.lib.cls.cls_rf_params import get_cls_rf_params
from asreview_simulation._private.lib.one_model_config import OneModelConfig


default_params = get_cls_rf_params()
name = f"cls-{RandomForestClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Random Forest classifier.",
    name=name,
    short_help="Random Forest classifier",
)
@click.option(
    "--class_weight",
    "class_weight",
    default=default_params["class_weight"],
    help="Class weight of the inclusions.",
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
@click.option(
    "--max_features",
    "max_features",
    default=default_params["max_features"],
    help="Number of features in the model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_estimators",
    "n_estimators",
    default=default_params["n_estimators"],
    help="Number of trees in the forest.",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def cls_rf_subcommand(obj, class_weight, force, max_features, n_estimators):
    if not force:
        assert obj.provided.cls is False, dont_reassign_cls_msg
    params = {
        "class_weight": class_weight,
        "max_features": max_features,
        "n_estimators": n_estimators,
    }
    obj.models.cls = OneModelConfig(abbr=name, params=params)
    obj.provided.cls = True
