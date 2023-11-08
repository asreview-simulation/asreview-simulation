import click
from asreview.models.classifiers import NN2LayerClassifier
from asreview_simulation._private.cli_epilog import epilog
from asreview_simulation._private.cls.cls_nn_2_layer_config import get_cls_nn_2_layer_config


default_params = get_cls_nn_2_layer_config().params
name = f"cls-{NN2LayerClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use 2-layer Neural Net classifier",
    name=name,
    short_help="2-layer Neural Net classifier",
)
@click.option(
    "--batch_size",
    "batch_size",
    default=default_params["batch_size"],
    help="Batch size used for the neural network.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--class_weight",
    "class_weight",
    default=default_params["class_weight"],
    help="Class weights for inclusions (1's).",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--dense_width",
    "dense_width",
    default=default_params["dense_width"],
    help="Size of the dense layers.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--epochs",
    "epochs",
    default=default_params["epochs"],
    help="Number of epochs to train the neural network.",
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
    "--learn_rate",
    "learn_rate",
    default=default_params["learn_rate"],
    help="Learning rate multiplier of the default learning rate.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--optimizer",
    "optimizer",
    default=default_params["optimizer"],
    help="Name of the Keras optimizer.",
    show_default=True,
    type=click.Choice(["sgd", "rmsprop", "adagrad", "adam", "nadam"]),
)
@click.option(
    "--regularization",
    "regularization",
    default=default_params["regularization"],
    help="Strength of the regularization on the weights and biases.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--shuffle",
    "shuffle",
    default=default_params["shuffle"],
    help="Whether to shuffle the training data prior to training.",
    is_flag=True,
)
@click.pass_obj
def cls_nn_2_layer_subcommand(
    obj,
    batch_size,
    class_weight,
    dense_width,
    epochs,
    force,
    learn_rate,
    optimizer,
    regularization,
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
        "dense_width": dense_width,
        "epochs": epochs,
        "learn_rate": learn_rate,
        "optimizer": optimizer,
        "regularization": regularization,
        "shuffle": shuffle,
    }
    obj.provided.cls = True
