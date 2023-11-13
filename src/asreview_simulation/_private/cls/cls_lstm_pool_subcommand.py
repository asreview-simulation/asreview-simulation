import click
from asreview.models.classifiers import LSTMPoolClassifier
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.cls.cls_lstm_pool_config import get_cls_lstm_pool_config


default_params = get_cls_lstm_pool_config().params
name = f"cls-{LSTMPoolClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use LSTM Pool classifier",
    name=name,
    short_help="LSTM Pool classifier",
)
@click.option(
    "--batch_size",
    "batch_size",
    default=default_params["batch_size"],
    help="Size of the batch size for the LSTM model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--class_weight",
    "class_weight",
    default=default_params["class_weight"],
    help="Class weight for the included papers.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--dropout",
    "dropout",
    default=default_params["dropout"],
    help="Value in [0, 1.0) that gives the dropout and recurrent dropout rate for the LSTM model.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--epochs",
    "epochs",
    default=default_params["epochs"],
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
    default=default_params["forward"],
    help="Include this flag to have a forward LSTM (default is backward).",
    is_flag=True,
)
@click.option(
    "--learn_rate",
    "learn_rate",
    default=default_params["learn_rate"],
    help="Learn rate multiplier of default learning rate.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--lstm_out_width",
    "lstm_out_width",
    default=default_params["lstm_out_width"],
    help="Output width of the LSTM.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--lstm_pool_size",
    "lstm_pool_size",
    default=default_params["lstm_pool_size"],
    help="Size of the pool, must be a divisor of max_sequence_length.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--optimizer",
    "optimizer",
    default=default_params["optimizer"],
    help="Optimizer to use.",
    show_default=True,
    type=click.Choice(["rmsprop", "sgd", "adagrad", "adam", "nadam"]),
)
@click.option(
    "--shuffle",
    "shuffle",
    default=default_params["shuffle"],
    help="Include this flag to shuffle the data before starting to train.",
    is_flag=True,
)
@click.pass_obj
def cls_lstm_pool_subcommand(
    obj,
    batch_size,
    class_weight,
    dropout,
    epochs,
    force,
    forward,
    learn_rate,
    lstm_out_width,
    lstm_pool_size,
    optimizer,
    shuffle,
):
    if not force:
        assert obj.provided.cls is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.models.cls.abbr = name
    obj.models.cls.params = {
        "batch_size": batch_size,
        "class_weight": class_weight,
        "dropout": dropout,
        "epochs": epochs,
        "forward": forward,
        "learn_rate": learn_rate,
        "lstm_out_width": lstm_out_width,
        "lstm_pool_size": lstm_pool_size,
        "optimizer": optimizer,
        "shuffle": shuffle,
    }
    obj.provided.cls = True
