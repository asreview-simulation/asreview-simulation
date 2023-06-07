import click
from asreview.models.classifiers import RandomForestClassifier
from .._epilog import epilog


name = RandomForestClassifier.name


@click.command(
    epilog=epilog,
    help="Use Random Forest classifier",
    name=f"cls:{name}",
)
@click.option(
    "--class_weight",
    "class_weight",
    default=1.0,
    help="hyperparameter",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--max_features",
    "max_features",
    default=10,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_estimators",
    "n_estimators",
    default=100,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def random_forest_classifier(obj, class_weight, force, max_features, n_estimators):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.abbr = name
    obj.classifier.params = {
        "class_weight": class_weight,
        "max_features": max_features,
        "n_estimators": n_estimators,
    }
    obj.provided.classifier = True
