import click
from asreview.models.classifiers import LogisticClassifier
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.lib.cls.cls_logistic_config import get_cls_logistic_config


default_params = get_cls_logistic_config().params
name = f"cls-{LogisticClassifier.name}"


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
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def cls_logistic_subcommand(obj, c, class_weight, force):
    if not force:
        assert obj.provided.cls is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.models.cls.abbr = name
    obj.models.cls.params = {
        "c": c,
        "class_weight": class_weight,
    }
    obj.provided.cls = True
