import click
from asreview.models.classifiers import LogisticClassifier
from asreview_simulation._private.cli.epilog import epilog


name = LogisticClassifier.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Logistic Regression classifier.",
    name=f"cls-{name}",
    short_help="Logistic Regression classifier",
)
@click.option(
    "--c",
    "c",
    default=1.0,
    help="Parameter inverse to the regularization strength of the model.",
    show_default=True,
    type=float,
)
@click.option(
    "--class_weight",
    "class_weight",
    default=1.0,
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
def logistic_classifier(obj, c, class_weight, force):
    if not force:
        assert obj.provided.classifier is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.classifier.abbr = name
    obj.classifier.params = {
        "C": c,
        "class_weight": class_weight,
    }
    obj.provided.classifier = True
