import click
from asreview.models.classifiers import SVMClassifier
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.lib.cls.cls_svm_config import get_cls_svm_config


default_params = get_cls_svm_config().params
name = f"cls-{SVMClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Support Vector Machine classifier.",
    name=name,
    short_help="Support Vector Machine classifier",
)
@click.option(
    "--c",
    "c",
    default=default_params["c"],
    help="C value of the SVM model.",
    show_default=True,
    type=click.FLOAT,
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
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--gamma",
    "gamma",
    default=default_params["gamma"],
    help="Gamma value of the SVM model.",
    show_default=True,
    type=click.Choice(["auto", "scale"]),
)
@click.option(
    "--kernel",
    "kernel",
    default=default_params["kernel"],
    help="Kernel type of the SVM model.",
    show_default=True,
    type=click.Choice(["linear", "rbf", "poly", "sigmoid"]),
)
@click.pass_obj
def cls_svm_subcommand(obj, c, class_weight, gamma, force, kernel):
    if not force:
        assert obj.provided.cls is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.models.cls.abbr = name
    obj.models.cls.params = {
        "c": c,
        "class_weight": class_weight,
        "gamma": gamma,
        "kernel": kernel,
    }
    obj.provided.cls = True
