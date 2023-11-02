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
    "--batch_size",
    "batch_size",
    default=32,
    help="Size of the batch size for the LSTM model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--class_weight",
    "class_weight",
    default=30.0,
    help="Class weight for the included papers.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--dense_width",
    "dense_width",
    default=128,
    help="Size of the dense layer of the model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--dropout",
    "dropout",
    default=0.4,
    help="Value in [0, 1.0) that gives the dropout and recurrent dropout rate for the LSTM model.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--epochs",
    "epochs",
    default=35,
    help="Number of epochs to train the LSTM model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--forward",
    "forward",
    help="Include this flag for forward LSTM (default is backward).",
    is_flag=True,
)
@click.option(
    "--optimizer",
    "optimizer",
    default="rmsprop",
    help="Optimizer to use.",
    show_default=True,
    type=click.Choice(["rmsprop", "sgd", "adagrad", "adam", "nadam"]),
)
@click.option(
    "--learn_rate",
    "learn_rate",
    default=1.0,
    help="Learn rate multiplier of default learning rate.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--lstm_out_width",
    "lstm_out_width",
    default=20,
    help="Output width of the LSTM.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--shuffle",
    "shuffle",
    help="Include this flag to shuffle the data before starting to train.",
    is_flag=True,
)
@click.pass_obj
def lstm_base_classifier(
    obj,
    batch_size,
    class_weight,
    dense_width,
    dropout,
    epochs,
    force,
    forward,
    optimizer,
    learn_rate,
    lstm_out_width,
    shuffle,
):
    if not force:
        assert obj.provided.classifier is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.classifier.abbr = name
    obj.classifier.params = {
        "backwards": not forward,
        "batch_size": batch_size,
        "class_weight": class_weight,
        "dense_width": dense_width,
        "dropout": dropout,
        "epochs": epochs,
        "optimizer": optimizer,
        "learn_rate": learn_rate,
        "lstm_out_width": lstm_out_width,
        "shuffle": shuffle,
    }
    obj.provided.classifier = True
