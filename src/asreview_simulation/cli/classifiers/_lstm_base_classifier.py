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
    "--backwards",
    "backwards",
    help="hyperparameter",
)
@click.option(
    "--dropout",
    "dropout",
    help="hyperparameter",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--optimizer",
    "optimizer",
    help="hyperparameter",
)
@click.option(
    "--lstm_out_width",
    "lstm_out_width",
    help="hyperparameter",
)
@click.option(
    "--learn_rate",
    "learn_rate",
    help="hyperparameter",
)
@click.option(
    "--dense_width",
    "dense_width",
    help="hyperparameter",
)
@click.option(
    "--batch_size",
    "batch_size",
    help="hyperparameter",
)
@click.option(
    "--epochs",
    "epochs",
    help="hyperparameter",
)
@click.option(
    "--shuffle",
    "shuffle",
    help="hyperparameter",
)
@click.option(
    "--class_weight",
    "class_weight",
    help="hyperparameter",
)
@click.pass_obj
def lstm_base_classifier(obj, backwards, dropout, force, optimizer, lstm_out_width, learn_rate, dense_width, batch_size, epochs, shuffle, class_weight):
    if not force:
        assert obj.provided.classifier is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.classifier.abbr = name
    obj.classifier.params = {
        "backwards": backwards,
        "dropout": dropout,
        "optimizer": optimizer,
        "lstm_out_width": lstm_out_width,
        "learn_rate": learn_rate,
        "dense_width": dense_width,
        "batch_size": batch_size,
        "epochs": epochs,
        "shuffle": shuffle,
        "class_weight": class_weight
    }
    obj.provided.classifier = True
