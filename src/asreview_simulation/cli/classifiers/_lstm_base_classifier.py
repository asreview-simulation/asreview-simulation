import click
from asreview.models.classifiers import LSTMBaseClassifier
from .._epilog import epilog


name = LSTMBaseClassifier.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use LSTM Base classifier",
    name=f"cls-{name}",
    short_help="LSTM Base classifier",
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
        assert obj.provided.classifier is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.classifier.abbr = name
    obj.classifier.params = {}
    obj.provided.classifier = True
