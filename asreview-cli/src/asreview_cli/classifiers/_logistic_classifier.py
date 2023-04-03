import click
from asreviewlib.classifiers import LogisticClassifier
from .._epilog import epilog


name = LogisticClassifier.name


@click.command(name=f"c-{name}", help="Use Logistic Regression classifier", epilog=epilog)
@click.option("--c", "c", default=1.0, type=float, help="hyperparameter 'C'.")
@click.option("--class_weight", "class_weight", default=1.0, type=click.FLOAT, help="hyperparameter 'class_weight'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the classifier configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def logistic_classifier(obj, c, class_weight, force):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "c": c,
        "class_weight": class_weight
    }
    obj.provided.classifier = True
