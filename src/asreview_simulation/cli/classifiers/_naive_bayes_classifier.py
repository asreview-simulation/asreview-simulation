import click
from asreview.models.classifiers import NaiveBayesClassifier
from .._epilog import epilog


name = NaiveBayesClassifier.name


@click.command(
    epilog=epilog,
    help="Use Naive Bayes classifier",
    name=f"cls:{name}",
)
@click.option(
    "--alpha",
    "alpha",
    default=3.822,
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
@click.pass_obj
def naive_bayes_classifier(obj, alpha, force):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.abbr = name
    obj.classifier.params = {"alpha": alpha}
    obj.provided.classifier = True
