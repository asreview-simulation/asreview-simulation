import click
from asreview.models.classifiers import LSTMBaseClassifier
from .._epilog import epilog


name = LSTMBaseClassifier.name


@click.command(
    epilog=epilog,
    help="Use LSTM Base classifier",
    name=f"cls:{name}",
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
def lstm_base_classifier(obj, force):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.abbr = name
    obj.classifier.params = {}
    obj.provided.classifier = True
