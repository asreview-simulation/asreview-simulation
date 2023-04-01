import click
from asreviewlib.classifiers import NaiveBayesClassifier


name = NaiveBayesClassifier.name


@click.command(name=f"c-{name}", help="Use Naive Bayes classifier")
@click.option("-alpha", "alpha", default=3.822, type=float, help="hyperparameter 'alpha'.")
@click.pass_obj
def naive_bayes_classifier(obj, alpha):
    assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "alpha": alpha
    }
    obj.provided.classifier = True
