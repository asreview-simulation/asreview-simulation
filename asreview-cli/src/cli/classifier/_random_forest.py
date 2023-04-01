import click


@click.command(name="c-rf", help="Use Random Forest classifier")
@click.option("-n_estimators", "n_estimators", default=100, type=int, help="hyperparameter 'n_estimators'.")
@click.option("-max_features", "max_features", default=10, type=int, help="hyperparameter 'max_features'.")
@click.option("-class_weight", "class_weight", default=1.0, type=float, help="hyperparameter 'class_weight'.")
@click.pass_obj
def random_forest(obj, n_estimators, max_features, class_weight):
    assert obj.provided.classifier is False, "Attempted reassignment of random forest classifier"
    obj.classifier.model = "rf"
    obj.classifier.params = {
        "n_estimators": n_estimators,
        "max_features": max_features,
        "class_weight": class_weight
    }
    obj.provided.classifier = True
