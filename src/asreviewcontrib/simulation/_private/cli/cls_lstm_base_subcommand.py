import click
from asreview.models.classifiers import LSTMBaseClassifier
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_cls_msg
from asreviewcontrib.simulation._private.lib.cls.cls_lstm_base_params import get_cls_lstm_base_params
from asreviewcontrib.simulation._private.lib.one_model_config import OneModelConfig


default_params = get_cls_lstm_base_params()
name = f"cls-{LSTMBaseClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use LSTM Base classifier",
    name=name,
    short_help="LSTM Base classifier",
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
    "--dense_width",
    "dense_width",
    default=default_params["dense_width"],
    help="Size of the dense layer of the model.",
    show_default=True,
    type=click.INT,
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
    help="Force setting the 'cls' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--forward",
    "forward",
    default=default_params["forward"],
    help="Include this flag for forward LSTM (default is backward).",
    is_flag=True,
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
    "--shuffle",
    "shuffle",
    default=default_params["shuffle"],
    help="Include this flag to shuffle the data before starting to train.",
    is_flag=True,
)
@click.pass_obj
def cls_lstm_base_subcommand(
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
        assert obj.provided.cls is False, dont_reassign_cls_msg
    params = {
        "batch_size": batch_size,
        "class_weight": class_weight,
        "dense_width": dense_width,
        "dropout": dropout,
        "epochs": epochs,
        "forward": forward,
        "optimizer": optimizer,
        "learn_rate": learn_rate,
        "lstm_out_width": lstm_out_width,
        "shuffle": shuffle,
    }
    obj.models.cls = OneModelConfig(abbr=name, params=params)
    obj.provided.cls = True
