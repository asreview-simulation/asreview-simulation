import click
from asreviewlib.classifiers import RandomForestClassifier
from .._epilog import epilog


name = RandomForestClassifier.name


@click.command(name=f"c-{name}", help="Use Random Forest classifier", epilog=epilog)
@click.option("--n_estimators", "n_estimators", default=100, type=click.INT, help="hyperparameter 'n_estimators'.")
@click.option("--max_features", "max_features", default=10, type=click.INT, help="hyperparameter 'max_features'.")
@click.option("--class_weight", "class_weight", default=1.0, type=click.FLOAT, help="hyperparameter 'class_weight'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the classifier configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def random_forest_classifier(obj, n_estimators, max_features, class_weight, force):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "n_estimators": n_estimators,
        "max_features": max_features,
        "class_weight": class_weight
    }
    obj.provided.classifier = True
