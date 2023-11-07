import click
from asreview.models.classifiers import RandomForestClassifier
from asreview_simulation._private.cli.epilog import epilog


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
    default=1.0,
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
    "--max_features",
    "max_features",
    default=10,
    help="Number of features in the model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_estimators",
    "n_estimators",
    default=100,
    help="Number of trees in the forest.",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def cls_rf(obj, class_weight, force, max_features, n_estimators):
    if not force:
        assert obj.provided.classifier is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.models.classifier.abbr = name
    obj.models.classifier.params = {
        "class_weight": class_weight,
        "max_features": max_features,
        "n_estimators": n_estimators,
    }
    obj.provided.classifier = True
