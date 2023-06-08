import click
from asreview.models.classifiers import LogisticClassifier
from .._epilog import epilog


name = LogisticClassifier.name


@click.command(
    epilog=epilog,
    help="Use Logistic Regression classifier",
    name=f"cls:{name}",
)
@click.option(
    "--c",
    "c",
    default=1.0,
    help="hyperparameter",
    show_default=True,
    type=float,
)
@click.option(
    "--class_weight",
    "class_weight",
    default=1.0,
    help="hyperparameter",
    type=click.FLOAT,
    show_default=True,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def logistic_classifier(obj, c, class_weight, force):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.abbr = name
    obj.classifier.params = {
        "C": c,
        "class_weight": class_weight,
    }
    obj.provided.classifier = True
